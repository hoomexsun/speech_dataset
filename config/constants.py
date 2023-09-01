from enum import Enum


class Language(Enum):
    S550 = "s550"
    BN = "bn"
    MM = "mm"


# Position
BEGIN = "begin"
MID = "mid"
END = "end"

# Syllabic
ONSET = "onset"
NUCLEUS = "nucleus"
CODA = "coda"
