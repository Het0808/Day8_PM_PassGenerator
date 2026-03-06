# ============================================================
#  Day-08 PM | PART A — Password Strength Analyzer & Generator
#  Topics: for loop, while loop, break, continue, string iteration
# ============================================================

import random
import string

SPECIAL_CHARS = set("!@#$%^&*")
MAX_SCORE     = 7


# ════════════════════════════════════════════════════════════
#  ANALYZER
# ════════════════════════════════════════════════════════════

def analyze_password(password: str) -> dict:
    """
    Score a password and return a full analysis dict.

    Scoring breakdown (max 7):
      Length   : ≥8 → +1 | ≥12 → +2 | ≥16 → +3
      Uppercase: +1
      Lowercase: +1
      Digit    : +1
      Special  : +1
      No triple-repeat consecutive chars: +1
    """
    score   = 0
    missing = []

    # ── Length check (for loop not needed — len() is O(1)) ──
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        missing.append("too short (< 8 chars)")

    # ── Character-type checks via for loop ───────────────────
    has_upper   = False
    has_lower   = False
    has_digit   = False
    has_special = False

    for ch in password:                  # for loop: iterate characters
        if ch.isupper():   has_upper   = True
        if ch.islower():   has_lower   = True
        if ch.isdigit():   has_digit   = True
        if ch in SPECIAL_CHARS: has_special = True

    if has_upper:   score += 1
    else:           missing.append("uppercase letter")

    if has_lower:   score += 1
    else:           missing.append("lowercase letter")

    if has_digit:   score += 1
    else:           missing.append("digit")

    if has_special: score += 1
    else:           missing.append("special character (!@#$%^&*)")

    # ── No-triple-repeat check via for loop with index ───────
    triple_found = False
    for i in range(len(password) - 2):   # for loop: sliding window of 3
        if password[i] == password[i+1] == password[i+2]:
            triple_found = True
            break                        # break: stop as soon as found

    if not triple_found:
        score += 1
    else:
        missing.append("no triple-repeat characters (e.g. 'aaa')")

    # ── Rating ───────────────────────────────────────────────
    if score >= 7:   rating = "Very Strong"
    elif score >= 5: rating = "Strong"
    elif score >= 3: rating = "Medium"
    else:            rating = "Weak"

    return {
        "score":   score,
        "max":     MAX_SCORE,
        "rating":  rating,
        "missing": missing,
    }


def print_analysis(result: dict) -> None:
    score, max_s = result["score"], result["max"]
    print(f"  Strength : {score}/{max_s} ({result['rating']})")
    if result["missing"]:
        print(f"  Missing  : {', '.join(result['missing'])}")


# ════════════════════════════════════════════════════════════
#  GENERATOR
# ════════════════════════════════════════════════════════════

CHAR_POOL = string.ascii_letters + string.digits + string.punctuation


def generate_password(length: int) -> str:
    """
    Generate a random password of given length using a for loop.
    Guarantees at least one char from each required category.
    """
    # Guarantee categories first
    required = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*"),
    ]

    # Fill the rest with random pool via for loop
    rest = []
    for _ in range(length - len(required)):   # for loop: build password chars
        rest.append(random.choice(CHAR_POOL))

    combined = required + rest
    random.shuffle(combined)

    # Join with for loop (explicit, per assignment requirement)
    password = ""
    for ch in combined:                       # for loop: assemble string
        password += ch

    return password


# ════════════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════════════

def main() -> None:
    print("=" * 52)
    print("   Password Strength Analyzer & Generator")
    print("=" * 52)

    # ── Section 1: Analyzer with while loop ──────────────────
    print("\n[ ANALYZER ]")
    print("  Enter passwords below. Loop exits when score ≥ 5.\n")

    attempts = 0
    while True:                              # while loop: keep asking
        attempts += 1
        pwd = input(f"  Enter password (attempt {attempts}): ").strip()

        if not pwd:
            print("  ✗ Password cannot be empty.\n")
            continue                          # continue: skip to next iteration

        result = analyze_password(pwd)
        print_analysis(result)

        if result["score"] >= 5:
            print("  ✅ Password accepted!\n")
            break                            # break: exit while loop on success
        else:
            print("  ↻ Try again...\n")

    # ── Section 2: Generator ─────────────────────────────────
    print("[ GENERATOR ]")
    while True:
        raw = input("  Length for generated password (8–64): ").strip()
        try:
            gen_len = int(raw)
            if 8 <= gen_len <= 64:
                break
            print("  ✗ Must be between 8 and 64.")
        except ValueError:
            print("  ✗ Enter a whole number.")

    gen_pwd = generate_password(gen_len)
    print(f"\n  Generated : {gen_pwd}")
    gen_result = analyze_password(gen_pwd)
    print("  Analysis  :")
    print_analysis(gen_result)
    print()


if __name__ == "__main__":
    main()
