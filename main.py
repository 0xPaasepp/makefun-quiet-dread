# Two Days of Quiet Dread entry: one code review comment, a single line
# of at most 140 characters, approving a pull request while carrying
# quiet existential dread. Standard library only, no network.
# The entry (120 characters, one line):
#   Approved. Green tests, tidy diff, and the quiet certainty that the
#   heat death of the universe is the only true deadline.
# Why this line: it approves outright ("Approved"), then lets the dread
# do the joking — the only true deadline is the heat death of the
# universe, stated flat, the way a tired engineer would paste it
# before clicking approve. No exclamation, no melodrama, no cry for
# help; the laugh comes from the dread itself, not from a joke bolted
# onto it. "The only true deadline" is the fresh turn: a deadline is
# the reviewer's own word, turned cosmic.
import os

ENTRY = (
    "Approved. Green tests, tidy diff, and the quiet certainty that "
    "the heat death of the universe is the only true deadline."
)

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(ENTRY) <= 140, "entry must be 1 to 140 characters"
assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = ENTRY.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
assert text.strip(), "entry must not be only whitespace"
assert "\n" not in text, "entry must be a single line"

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(text)

# Read back what was written and confirm it is exactly the entry:
# one line, 120 characters, byte for byte.
written = open(OUTPUT_PATH, encoding="utf-8").read()
assert written == ENTRY, "written entry differs from ENTRY"
assert len(written.encode("utf-8")) == 120, "written entry must be 120 bytes"
