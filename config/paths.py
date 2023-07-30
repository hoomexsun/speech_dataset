from pathlib import Path

# -------------------------------- DATA PATHS -------------------------------- #
DATA_ROOT = Path("data")

RTF, RAW, WAV = "rtf", "raw", "wav"
S550, BN, MM = "s550", "bn", "mm"
SCP, UTT, TXT, WORDS, CHARS = "script", "utt", "txt", "words", "chars"

RTF_DATA = DATA_ROOT / RTF  # Directory for s550 rtf file (file level)
RAW_DATA = DATA_ROOT / RAW  # Directory for s550 rtf file (file level)
S550_DATA = DATA_ROOT / S550
BN_DATA = DATA_ROOT / BN
MM_DATA = DATA_ROOT / MM
WAV_DATA = DATA_ROOT / WAV  # Directory for audio files

SCP_S550_DIR = S550_DATA / SCP  # Directory for preprocessed scripts in s550
SCP_BN_DIR = BN_DATA / SCP  # Directory for preprocessed scripts in Bengali Unicode
SCP_MM_DIR = MM_DATA / SCP  # Directory for preprocessed scripts in Meetei Mayek Unicode
UTT_S550_DIR = S550_DATA / UTT  # Directory for utterance in s550
UTT_BN_DIR = BN_DATA / UTT  # Directory for utterance in Bengali Unicode
UTT_MM_DIR = MM_DATA / UTT  # Directory for utterance in Meetei Mayek Unicode

data_dirs = [
    SCP_S550_DIR,
    SCP_BN_DIR,
    SCP_MM_DIR,
    UTT_S550_DIR,
    UTT_BN_DIR,
    UTT_MM_DIR,
    RTF_DATA,
    RAW_DATA,
    WAV_DATA,
]

WORDS_FILE = "words.txt"
CHARS_FILE = "chars.txt"
TEXT_FILE = "text.txt"

WORDS_S550_FILE = S550_DATA / WORDS / WORDS_FILE
WORDS_BN_FILE = BN_DATA / WORDS / WORDS_FILE
WORDS_MM_FILE = MM_DATA / WORDS / WORDS_FILE
CHARS_S550_FILE = S550_DATA / CHARS / CHARS_FILE
CHARS_BN_FILE = BN_DATA / CHARS / CHARS_FILE
CHARS_MM_FILE = MM_DATA / CHARS / CHARS_FILE
TEXT_S550_FILE = S550_DATA / TXT / TEXT_FILE
TEXT_BN_FILE = BN_DATA / TXT / TEXT_FILE
TEXT_MM_FILE = MM_DATA / TXT / TEXT_FILE

# -------------------------------- RESOURCE PATHS -------------------------------- #

RESOURCE_ROOT = Path("res")  # Root directory for resource

ALPHABET_DIR = RESOURCE_ROOT / "alphabet"  # Alphabet Resources
TRANSLITERATION_DIR = RESOURCE_ROOT / "transliteration"  # Transliteration Resources
INFO_DIR = RESOURCE_ROOT / "info"  # Resource directory for Informative resource files
CORRECTION_DIR = RESOURCE_ROOT / "correction"  # Correction Resources
WORD_MAP_DIR = RESOURCE_ROOT / "word_map"  # WordMap Resources

resource_paths = [
    ALPHABET_DIR,
    CORRECTION_DIR,
    TRANSLITERATION_DIR,
    INFO_DIR,
    WORD_MAP_DIR,
]


# -------------------------------- FILE NAME -------------------------------- #

B2M_FILE = "b2m"  # Bengali to Meetei Mayek Character Map filename
SNB_FILE = "s2b"  # Contains s550 and Bengali characters which should be mapped
FPOS_FILE = (
    "fpos"  # Contains Dictionary of List of characters which position needs fixing
)

CLUSTERS_FILE = INFO_DIR / "clusters"  # virama clusters file
CLUSTERS_EGS_FILE = INFO_DIR / "clusters_egs"  # clusters file with examples
CLUSTERS_MAP_FILE = INFO_DIR / "clusters_map"  # clusters file with probable map
CLUSTERS_DETAILED_FILE = INFO_DIR / "clusters_detailed"  # detailed clusters file
CLUSTERS_PCT_FILE = INFO_DIR / "clusters_percentage"  # detailed clusters file

WORDMAP_C_FILE = WORD_MAP_DIR / "s550_bn"
WORDMAP_T_FILE = WORD_MAP_DIR / "bn_mm"

MM_ALPHABET_FILE = (
    ALPHABET_DIR / "mm_alphabet"
)  # Contains Dictionary of List of Meetei Mayek Characters

BN_ALPHABET_FILE = (
    ALPHABET_DIR / "bn_alphabet"
)  # Contains Dictionary of List of Bengali Characters
EN_ALPHABET_FILE = (
    ALPHABET_DIR / "en_alphabet"
)  # Contains Dictionary of List of English Characters

# -------------------------------- COLUMN NAME -------------------------------- #

BN_FIELD = "bengali"  # Column name of Bengali words in WordMap file
MM_FIELD = "meetei_mayek"  # Column name of Meetei Mayek words in WordMap file


# -------------------------------- CREATE DIRS -------------------------------- #
def build_paths():
    # Create data directories if they don't exist
    for path in data_dirs:
        Path(path).mkdir(parents=True, exist_ok=True)

    # Create resource directories if they don't exist
    for path in resource_paths:
        Path(path).mkdir(parents=True, exist_ok=True)
