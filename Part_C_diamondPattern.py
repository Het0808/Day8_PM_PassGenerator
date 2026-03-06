# ============================================================
#  Day-08 PM | PART C — AI-Augmented Task
#  Diamond Pattern using Nested Loops
# ============================================================


# ════════════════════════════════════════════════════════════
#  SECTION 1: EXACT PROMPT GIVEN TO AI
# ════════════════════════════════════════════════════════════

"""
PROMPT USED:
------------
"Write a Python program that prints a diamond pattern of asterisks.
The user inputs the number of rows for the upper half. Include proper
spacing and use nested loops only (no string multiplication tricks)."
"""


# ════════════════════════════════════════════════════════════
#  SECTION 2: AI-GENERATED CODE (pasted verbatim)
# ════════════════════════════════════════════════════════════

def diamond_ai(n):
    """AI-generated version — pasted as-is from Claude output."""
    # Upper half (including middle)
    for i in range(1, n + 1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    # Lower half
    for i in range(n - 1, 0, -1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")
        print()


# ════════════════════════════════════════════════════════════
#  SECTION 3: CRITICAL EVALUATION
# ════════════════════════════════════════════════════════════

"""
EVALUATION OF AI CODE:
======================

1. SPACING CORRECTNESS — CORRECT ✓
   Upper half row i needs (n-i) leading spaces and (2i-1) stars.
   Lower half row i needs (n-i) leading spaces and (2i-1) stars.
   The formula is mathematically correct for a centred diamond.

2. NESTED LOOPS — CORRECT ✓
   Uses three separate for loops per row (spaces + stars) instead
   of string multiplication — exactly what the prompt asked for.

3. EDGE CASE: n = 0 — FAILS ✗
   range(1, 0+1) = range(1,1) → empty → prints nothing silently.
   No message to tell the user why nothing appeared.

4. EDGE CASE: n = 1 — CORRECT ✓
   Prints a single '*'. Upper half: 1 row, 0 spaces, 1 star.
   Lower half: range(0, 0, -1) is empty → correctly nothing added.

5. READABILITY — AVERAGE ⚠
   Variable names j and k are meaningless.
   No docstring explains the formula for spaces/stars.
   No comments linking the loop to the visual structure.

6. NEGATIVE INPUT — FAILS ✗
   diamond_ai(-3) → range(1, -2) is empty → silent failure.
   Should validate input before running.

7. TIME COMPLEXITY — CORRECT ✓
   O(n²) — two nested loops for each of the 2n-1 rows.
   Cannot be better than O(n²) since we print O(n²) characters.

VERDICT:
  Core logic and formula are correct for valid n ≥ 1.
  Fails silently on n ≤ 0, no input validation, weak variable names.
"""


# ════════════════════════════════════════════════════════════
#  SECTION 4: IMPROVED VERSION
# ════════════════════════════════════════════════════════════

def print_diamond(n: int) -> None:
    """
    Print a diamond pattern of asterisks.

    Formula per row:
      spaces = n - row   (where row counts from 1 at top)
      stars  = 2*row - 1

    Args:
        n: number of rows in the upper half (including middle row)

    Improvements over AI version:
      ① Input validation — rejects n ≤ 0 with a clear message
      ② Meaningful variable names — spaces_count, stars_count
      ③ Single helper to print one row — avoids code duplication
      ④ Comments explain the formula visually
    """

    # ① Validate input
    if n <= 0:
        print("  ✗ n must be a positive integer.")
        return

    # ③ Helper: print one row
    def print_row(spaces_count: int, stars_count: int) -> None:
        for _ in range(spaces_count):   # nested loop: leading spaces
            print(" ", end="")
        for _ in range(stars_count):    # nested loop: asterisks
            print("*", end="")
        print()                         # newline

    # ── Upper half (rows 1 → n, middle = row n) ──────────────
    #   row 1: (n-1) spaces, 1 star
    #   row 2: (n-2) spaces, 3 stars
    #   row n: 0 spaces,     (2n-1) stars
    for row in range(1, n + 1):                 # ② meaningful name
        spaces_count = n - row
        stars_count  = 2 * row - 1
        print_row(spaces_count, stars_count)

    # ── Lower half (rows n-1 → 1, mirror of upper) ───────────
    for row in range(n - 1, 0, -1):
        spaces_count = n - row
        stars_count  = 2 * row - 1
        print_row(spaces_count, stars_count)


# ════════════════════════════════════════════════════════════
#  SECTION 5: DEMO
# ════════════════════════════════════════════════════════════

def main() -> None:
    print("=" * 40)
    print("  Diamond Pattern — AI vs Improved")
    print("=" * 40)

    # ── AI version ───────────────────────────────────────────
    print("\n[ AI Version ] n = 4:")
    diamond_ai(4)

    print("\n[ AI Version ] n = 0 (silent failure):  ", end="")
    diamond_ai(0)
    print("(nothing printed — no error message)")

    # ── Improved version ─────────────────────────────────────
    print("\n[ Improved ] n = 4:")
    print_diamond(4)

    print("\n[ Improved ] n = 1:")
    print_diamond(1)

    print("\n[ Improved ] n = 0 (graceful error):")
    print_diamond(0)

    print("\n[ Improved ] n = -5 (graceful error):")
    print_diamond(-5)

    # ── Interactive ──────────────────────────────────────────
    print("\n" + "─" * 40)
    while True:
        raw = input("Enter rows for upper half (or 0 to quit): ").strip()
        try:
            n = int(raw)
        except ValueError:
            print("  ✗ Enter a whole number.")
            continue
        if n == 0:
            break
        print_diamond(n)


if __name__ == "__main__":
    main()
