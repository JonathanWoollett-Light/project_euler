"""Draw progress.svg: one square per Project Euler problem, filled if solved.

A problem counts as solved when a .py file in problems/ links to it, which
each solution does on its first line, e.g. `# https://projecteuler.net/problem=6`.
Solutions are read from HEAD by default, so the grid matches what gets pushed.

    python scripts/progress_grid.py             # grid for HEAD
    python scripts/progress_grid.py --worktree  # include uncommitted solutions

Runs automatically from the pre-push hook in .githooks/.
"""

import argparse
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SVG_PATH = ROOT / "progress.svg"
PROBLEMS_URL = "https://projecteuler.net/minimal=problems"
SOLUTION_LINK = r"projecteuler\.net/problem=[0-9]+"

COLUMNS = 50  # matches the Project Euler archive's 50 problems a page
CELL, GAP = 12, 2
GROUP_GAP = 4  # extra space after every 10 columns, to make counting easier
LABEL_WIDTH = 32  # room for the row labels, up to "1001"
HEADER_HEIGHT = 28

# The README can be viewed on a light or dark page, so these colours work on both.
SOLVED = "#2a78d6"
UNSOLVED = "#898781"  # drawn at 20% opacity
INK = "#7d7b76"


def grep_solutions(rev, option):
    """Run `git grep <option>` for problem links over problems/*.py at `rev` (the worktree if None)."""
    cmd = ["git", "grep", "--no-color", "--no-line-number", "--no-column", option, "-E", SOLUTION_LINK]
    if rev:
        cmd.append(rev)
    cmd += ["--", ":(glob)problems/*.py"]
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode > 1:  # 1 only means nothing matched
        sys.exit(result.stderr.strip())
    return result.stdout.splitlines()


def solved_problems(rev):
    """Problems linked from .py files in problems/ at `rev` (the worktree if None)."""
    # A solution without a link would silently leave the grid stale, so refuse instead.
    unlinked = [path.removeprefix(f"{rev}:") for path in grep_solutions(rev, "-L")]
    if unlinked:
        sys.exit(
            "progress_grid: add a first line like `# https://projecteuler.net/problem=N` to:\n  "
            + "\n  ".join(unlinked)
        )

    # Only a file's first link counts, so a comment mentioning another problem is ignored.
    first_link = {}
    for line in grep_solutions(rev, "-o"):
        path, _, link = line.rpartition(":")
        first_link.setdefault(path, int(link.rpartition("=")[2]))
    return set(first_link.values())


def published_problems():
    """The number of problems Project Euler has published, or None if unreachable."""
    request = urllib.request.Request(PROBLEMS_URL, headers={"User-Agent": "project_euler progress grid"})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            rows = response.read().decode().splitlines()[1:]  # skip the "ID##Title##..." header
        return max(int(row.split("##")[0]) for row in rows if row)
    except (OSError, ValueError) as error:
        print(f"progress_grid: couldn't fetch {PROBLEMS_URL}: {error}", file=sys.stderr)
        return None


def previous_total():
    """The problem count recorded in the last progress.svg, if there is one."""
    try:
        match = re.search(r'data-problems="(\d+)"', SVG_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    return int(match[1]) if match else None


def render(solved, total):
    pitch = CELL + GAP
    rows = -(-total // COLUMNS)
    width = LABEL_WIDTH + COLUMNS * pitch - GAP + (COLUMNS - 1) // 10 * GROUP_GAP
    height = HEADER_HEIGHT + rows * pitch - GAP
    summary = f"{len(solved)} of {total:,} problems solved"

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" data-problems="{total}">',
        f"<title>Project Euler progress: {summary}</title>",
        "<style>",
        f"text {{ font: 10px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: {INK} }}",
        ".head { font-size: 13px; font-weight: 600 }",
        ".row { text-anchor: end; font-variant-numeric: tabular-nums }",
        f"rect {{ fill: {UNSOLVED}; fill-opacity: 0.2 }}",
        f".solved {{ fill: {SOLVED}; fill-opacity: 1 }}",
        "</style>",
        # The headline sits beside a filled square, so it doubles as the legend.
        f'<rect class="solved" x="{LABEL_WIDTH}" y="5" width="{CELL}" height="{CELL}" rx="2"/>',
        f'<text class="head" x="{LABEL_WIDTH + CELL + 6}" y="16">{summary} ({len(solved) / total:.1%})</text>',
    ]
    for row in range(rows):
        y = HEADER_HEIGHT + row * pitch
        svg.append(f'<text class="row" x="{LABEL_WIDTH - 6}" y="{y + 10}">{row * COLUMNS + 1}</text>')
    for n in range(1, total + 1):
        row, col = divmod(n - 1, COLUMNS)
        x = LABEL_WIDTH + col * pitch + col // 10 * GROUP_GAP
        y = HEADER_HEIGHT + row * pitch
        attrs = ' class="solved"' if n in solved else ""
        status = ": solved" if n in solved else ""
        svg.append(
            f'<rect{attrs} x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2">'
            f"<title>Problem {n}{status}</title></rect>"
        )
    svg.append("</svg>")
    return "\n".join(svg) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--worktree", action="store_true", help="read solutions from the working tree, not HEAD")
    args = parser.parse_args()

    solved = solved_problems(None if args.worktree else "HEAD")
    # Offline, keep the last known count so the grid doesn't shrink and grow back.
    total = published_problems() or previous_total()
    if total is None:
        sys.exit("progress_grid: couldn't determine how many problems there are")
    total = max(total, max(solved, default=0))

    svg = render(solved, total)
    changed = not SVG_PATH.exists() or SVG_PATH.read_text(encoding="utf-8") != svg
    if changed:
        SVG_PATH.write_text(svg, encoding="utf-8", newline="\n")
    print(f"progress_grid: {len(solved)} of {total:,} problems solved{'' if changed else ' (unchanged)'}")


if __name__ == "__main__":
    main()
