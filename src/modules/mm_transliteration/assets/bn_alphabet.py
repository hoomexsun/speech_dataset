BN_ALPHABET = {
    "\u098b",  # \u098b -> ঋ
    "\u099a",  # \u099a -> চ
    "\u099b",  # \u099b -> ছ
    "\u099c",  # \u099c -> জ
    "\u099d",  # \u099d -> ঝ
    "\u099e",  # \u099e -> ঞ
    "\u099f",  # \u099f -> ট
    "\u09a0",  # \u09a0 -> ঠ
    "\u09a1",  # \u09a1 -> ড
    "\u09a2",  # \u09a2 -> ঢ
    "\u09a3",  # \u09a3 -> ণ
    "\u09a4",  # \u09a4 -> ত
    "\u09a5",  # \u09a5 -> থ
    "\u09a6",  # \u09a6 -> দ
    "\u09a7",  # \u09a7 -> ধ
    "\u09a8",  # \u09a8 -> ন
    "\u09aa",  # \u09aa -> প
    "\u09ab",  # \u09ab -> ফ
    "\u09ac",  # \u09ac -> ব
    "\u09ad",  # \u09ad -> ভ
    "\u09ae",  # \u09ae -> ম
    "\u09af",  # \u09af -> য
    "\u09b0",  # \u09b0 -> র
    "\u09b2",  # \u09b2 -> ল
    "\u09b6",  # \u09b6 -> শ
    "\u09b7",  # \u09b7 -> ষ
    "\u09b8",  # \u09b8 -> স
    "\u09b9",  # \u09b9 -> হ
    "\u09dc",  # \u09dc -> ড়
    "\u09dd",  # \u09dd -> ঢ়
    "\u09df",  # \u09df -> য়
    "\u09F1",  # \u09f1 -> ৱ
}

VIRAMA = "\u09cd"  # \u09cd -> ্
SOMETHING = "\u09d7"  # \u09d7 -> ৗ

BN_INDEPENDENT_VELAR = {
    "\u0995",  # \u0995 -> ক
    "\u0996",  # \u0996 -> খ
    "\u0997",  # \u0997 -> গ
    "\u0998",  # \u0998 -> ঘ
    "\u0999",  # \u0999 -> ঙ
}
#! Arrange the characters according to SSP arranged using acoustic intensity (11->1)
#! glide > rhotic > lateral > flap > trill > nasal > h > voiced fricative >
#! voiced stop/affricate > voiceless fricative > voiceless stop/affricate

GLIDE = {}
RHOTIC = {}
LATERAL = {}
FLAP = {}
TRILL = {}
NASAL = {}
H = {}
VOICED_FRICATIVE = {}
VOICED_AFFRICATE = {}
VOICELESS_FRICATIVE = {}
VOICELESS_AFFRICATE = {}


BN_DEPENDENT_CONSONANT = {
    "\u09c3",  # \u09c3 -> ৃ
    "\u09ce",  # \u09ce -> ৎ
    "\u0982",  # \u0982 -> ং
}

BN_INDEPENDENT_VOWEL = {
    "\u0985",  # \u0985 -> অ
    "\u0986",  # \u0986 -> আ
    "\u0987",  # \u0987 -> ই
    "\u0988",  # \u0988 -> ঈ
    "\u0989",  # \u0989 -> উ
    "\u098a",  # \u098a -> ঊ
    "\u098f",  # \u098f -> এ
    "\u0990",  # \u0990 -> ঐ
    "\u0993",  # \u0993 -> ও
    "\u0994",  # \u0994 -> ঔ
}

BN_DEPENDENT_VOWEL = {
    "\u09be",  # \u09be -> া
    "\u09bf",  # \u09bf -> ি
    "\u09c0",  # \u09c0 -> ী
    "\u09c1",  # \u09c1 -> ু
    "\u09c2",  # \u09c2 -> ূ
    "\u09c7",  # \u09c7 -> ে
    "\u09c8",  # \u09c8 -> ৈ
    "\u09cb",  # \u09cb ->  ো
    "\u09cc",  # \u09cc ->  ৌ
}
BN_DEPENDENT_VOWEL_2 = {
    "\u09be",  # \u09be -> া
    "\u09bf",  # \u09bf -> ি
    "\u09c0",  # \u09c0 -> ী
    "\u09c1",  # \u09c1 -> ু
    "\u09c2",  # \u09c2 -> ূ
    "\u09c7",  # \u09c7 -> ে
    "\u09c8",  # \u09c8 -> ৈ
    "\u09cb",  # \u09cb ->  ো
    "\u09cc",  # \u09cc ->  ৌ
}

BN_PUNCTUATION = {
    "\u0983",  # \u0983 -> ঃ
}

BN_NUMERAL = {
    "\u09e6",  # \u09e6 -> ০
    "\u09e7",  # \u09e7 -> ১
    "\u09e8",  # \u09e8 -> ২
    "\u09e9",  # \u09e9 -> ৩
    "\u09ea",  # \u09ea -> ৪
    "\u09eb",  # \u09eb -> ৫
    "\u09ec",  # \u09ec -> ৬
    "\u09ed",  # \u09ed -> ৭
    "\u09ee",  # \u09ee -> ৮
    "\u09ef",  # \u09ef -> ৯
}
