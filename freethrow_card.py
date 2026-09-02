# ============================================================
#  freethrow_card.py  —  Python Day 2
#  Turn your free-throw data into a stat card you can show off.
#  Fill in each STEP. Run after every step:  click the  >  button.
# ============================================================

# ===== STEP 1 — your data =====================================
# Copy the ten boxes from your score sheet. 1 = made, 0 = missed.

name = "Alexander"
before = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # <-- your ROUND 1 boxes
after  = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]   # <-- your ROUND 3 boxes


# ===== STEP 2 — the math ======================================
# You already know all of this from yesterday.

before_made = sum(before)
after_made = sum(after)
attempts = len(before)

before_pct = before_made / attempts * 100
after_pct = after_made / attempts * 100
improvement = after_pct - before_pct


# ===== STEP 3 — the bars  (NEW SYNTAX — read the handout) =====
# "#" * 4   builds the string   "####"
# So "#" * before_made draws one # per shot you MADE,
# and "." * (attempts - before_made) draws a dot for each MISS.

before_bar = "#" * before_made + "." * (attempts - before_made)
after_bar = "#" * after_made + "." * (attempts - after_made)


# ===== STEP 4 — the verdict ===================================
# Write an if / elif / else that sets `verdict` to a message.
# Improved? Stayed the same? Went down? All three are real outcomes.

verdict = "???"          # <-- replace this with your if/elif/else


# ===== STEP 5 — print the card ================================
# Make it look good. Use f-strings. {before_pct:.1f} shows one decimal.

print("========================================")
print(f"|  FREE THROW CARD  ·  {name}       |")
print("========================================")
print(f"  Improvement: +{improvement:.1f} points")
print("========================================")
print(f"  Before   {before_bar}   {before_pct:.1f}%")
print(f"  After    {after_bar}   {after_pct:.1f}%")
if improvement > 0:
    verdict = "You improved! Keep it up!"
elif improvement == 0:
    verdict = "You didn't improve."
else:
    verdict = "You got worse."
print(f"{verdict}")
print("========================================")


# ===== STRETCH (only if you're flying) ========================
# A) Add a third line for your best streak of makes in a row.
# B) Ask the user for their name with input() instead of hard-coding it.
# C) Add a "class average" line using numbers from the board.


# ===== BEFORE YOU PUSH ========================================
# One thing that surprised you about your own data:
# One thing you had to fix before it ran:
