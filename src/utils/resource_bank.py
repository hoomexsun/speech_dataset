# Transliteration resource generator

bn_c_to_mm_c = {
    "\u0995": "\uabc0",  # \u0995 -> ক : \uabc0 -> ꯀ
    "\u0996": "\uabc8",  # \u0996 -> খ : \uabc8 -> ꯈ
    "\u0997": "\uabd2",  # \u0997 -> গ : \uabd2 -> ꯒ
    "\u0998": "\uabd8",  # \u0998 -> ঘ : \uabd8 -> ꯘ
    "\u0999": "\uabc9",  # \u0999 -> ঙ : \uabc9 -> ꯉ
    "\u099a": "\uabc6",  # \u099a -> চ : \uabc6 -> ꯆ
    "\u099b": "\uabc1",  # \u099b -> ছ : \uabc1 -> ꯁ
    "\u099c": "\uabd6",  # \u099c -> জ : \uabd6 -> ꯖ
    "\u099d": "\uabc3",  # \u099d -> ঝ : \uabd3 -> ꯓ
    "\u099e": "\uabc5",  # \u099e -> ঞ : \uabc5 -> ꯅ
    "\u099f": "\uabc7",  # \u099f -> ট : \uabc7 -> ꯇ
    "\u09a0": "\uabca",  # \u09a0 -> ঠ : \uabca -> ꯊ
    "\u09a1": "\uabd7",  # \u09a1 -> ড : \uabd7 -> ꯗ (not there in s550)
    "\u09a2": "\uabd9",  # \u09a2 -> ঢ : \uabd9 -> ꯙ
    "\u09a3": "\uabc5",  # \u09a3 -> ণ : \uabc5 -> ꯅ
    "\u09a4": "\uabc7",  # \u09a4 -> ত : \uabc7 -> ꯇ
    "\u09a5": "\uabca",  # \u09a5 -> থ : \uabca -> ꯊ
    "\u09a6": "\uabd7",  # \u09a6 -> দ : \uabd7 -> ꯗ
    "\u09a7": "\uabd9",  # \u09a7 -> ধ : \uabd9 -> ꯙ
    "\u09a8": "\uabc5",  # \u09a8 -> ন : \uabc5 -> ꯅ
    "\u09aa": "\uabc4",  # \u09aa -> প : \uabc4 -> ꯄ
    "\u09ab": "\uabd0",  # \u09ab -> ফ : \uabd0 -> ꯐ
    "\u09ac": "\uabd5",  # \u09ac -> ব : \uabd5 -> ꯕ
    "\u09ad": "\uabda",  # \u09ad -> ভ : \uabda -> ꯚ
    "\u09ae": "\uabc3",  # \u09ae -> ম : \uabc3 -> ꯃ
    "\u09af": "\uabcc",  # \u09af -> য় : \uabcc -> ꯌ (not there in s550)
    "\u09b0": "\uabd4",  # \u09b0 -> র : \uabd4 -> ꯔ
    "\u09b2": "\uabc2",  # \u09b2 -> ল : \uabc2 -> ꯂ
    "\u09b6": "\uabc1",  # \u09b6 -> শ : \uabc1 -> ꯁ
    "\u09b7": "\uabc1",  # \u09b7 -> ষ : \uabc1 -> ꯁ
    "\u09b8": "\uabc1",  # \u09b8 -> স : \uabc1 -> ꯁ
    "\u09b9": "\uabcd",  # \u09b9 -> হ : \uabcd -> ꯍ
    "\u09dc": "\uabd4",  # \u09dc -> ড় : \uabd4 -> ꯔ
    "\u09dd": "\uabd4",  # \u09dd -> ঢ় : \uabd4 -> ꯔ (not there in s550)
    "\u09df": "\uabcc",  # \u09df -> য় : \uabcc -> ꯌ
    "\u09f0": "\uabd4",  # \u09f1 -> ৰ : \uabd4 -> ꯔ (not there in s550)
    "\u09f1": "\uabcb",  # \u09f1 -> ৱ : \uabcb -> ꯋ
}

bn_v_to_mm_v_begin = {
    "\u0985": "\uabd1",  # \u0985 -> অ : \uab -> ꯑ
    "\u0986": "\uabd1\uabe5",  # \u0986 -> আ : \uabd1\uabe5 -> ꯑꯥ
    "\u0987": "\uabcf",  # \u0987 -> ই : \uabcf -> ꯏ
    "\u0988": "\uabcf",  # \u0988 -> ঈ : \uabcf -> ꯏ
    "\u0989": "\uabce",  # \u0989 -> উ : \uabce -> ꯎ
    "\u098a": "\uabce",  # \u098a -> ঊ : \uabce -> ꯎ
    "\u098b": "\uabe4",  # \u098b -> ঋ : \uabe4 -> ꯔ
    "\u098f": "\uabd1\uabe6",  # \u098f -> এ : \uabd1\uabe6 -> ꯑꯦ
    "\u0990": "\uabd1\uabe9",  # \u0990 -> ঐ : \uabd1\uabe9 -> ꯑꯩ
    "\u0993": "\uabd1\uabe3",  # \u0993 -> ও : \uabd1\uabe3 -> ꯑꯣ
    "\u0994": "\uabd1\uabe7",  # \u0994 -> ঔ : \uabd1\uab -> ꯑꯧ
}

bn_v_to_mm_v_mid = {
    "\u09be": "\uabe5",  # \u09be -> া : \uabe5 -> ꯥ
    "\u09bf": "\uabe4",  # \u09bf -> ি : \uabe4 -> ꯤ
    "\u09c0": "\uabe4",  # \u09c0 -> ী : \uabe4 -> ꯤ
    "\u09c1": "\uabe8",  # \u09c1 -> ু : \uabe8 -> ꯨ
    "\u09c2": "\uabe8",  # \u09c2 -> ূ : \uabe8 -> ꯨ
    "\u09c3": "\uabed\uabe4",  # \u09c3 -> ৃ : \uabed\uabe4 -> ꯭ꯔ
    "\u09c7": "\uabe6",  # \u09c7 -> ে : \uabe6 -> ꯦ
    "\u09c8": "\uabe9",  # \u09c8 -> ৈ : \uabe9 -> ꯩ
    "\u09cb": "\uabe3",  # \u09cb -> ো : \uabe3 -> ꯣ
    "\u09cc": "\uabe7",  # \u09cc -> ৌ : \uab -> ꯧ
    "\u09ce": "\uabe0",  # \u09ce -> ৎ : \uab -> ꯠ
}

bn_num_to_mm_num = {
    "\u09e6": "\uabf0",  # \u09e6 -> ০ : \uab -> ꯰
    "\u09e7": "\uabf1",  # \u09e7 -> ১ : \uab -> ꯱
    "\u09e8": "\uabf2",  # \u09e8 -> ২ : \uab -> ꯲
    "\u09e9": "\uabf3",  # \u09e9 -> ৩ : \uab -> ꯳
    "\u09ea": "\uabf4",  # \u09ea -> ৪ : \uab -> ꯴
    "\u09eb": "\uabf5",  # \u09eb -> ৫ : \uab -> ꯵
    "\u09ec": "\uabf6",  # \u09ec -> ৬ : \uab -> ꯶
    "\u09ed": "\uabf7",  # \u09ed -> ৭ : \uab -> ꯷
    "\u09ee": "\uabf8",  # \u09ee -> ৮ : \uab -> ꯸
    "\u09ef": "\uabf9",  # \u09ef -> ৯ : \uab -> ꯹
}

bn_punctuation = {
    "\u0981": "",  # \u0981 -> ঁ : \uab  ->
    "\u0982": "\uabe1",  # \u0982 -> ং : \uabea -> ꯡ
    "\u0983": "",  # \u0983 -> ঃ : \uab ->
}

bn_viramma_mm_apun = {
    "\u09cd\uabd4": "\uabed\uabd4",  # \u09cd\uabd4 -> ্ + ꯔ : \uabed\uabd4 -> ꯭ꯔ
    "\u09cd\uabcc": "\uabed\uabcc",  # \u09cd\uabcc -> ্ + ꯌ : \uabed\uabd4 -> ꯭ꯌ
    "\uabc1\u09cd": "\uabc1\uabed",  # \uabc1\u09cd -> ꯁ + ্ : \uabc1\uabed -> ꯁ ꯭
}

bn_viramma_mm_coda = {
    "\uabc0\u09cd": "\uabdb",  # \uabc0\u09cd -> ꯀ + ্ : \uabdb -> ꯛ
    "\uabc2\u09cd": "\uabdc",  # \uabc2\u09cd -> ꯂ + ্ : \uabdc -> ꯜ
    "\uabc3\u09cd": "\uabdd",  # \uabc3\u09cd -> ꯃ + ্ : \uabdd -> ꯝ
    "\uabc4\u09cd": "\uabde",  # \uabc4\u09cd -> ꯄ + ্ : \uabde -> ꯞ
    "\uabc5\u09cd": "\uabdf",  # \uabc5\u09cd -> ꯅ + ্ : \uabdf -> ꯟ
    "\uabc7\u09cd": "\uabe0",  # \uabc7\u09cd -> ꯇ + ্ : \uabe0 -> ꯠ
    "\uabc9\u09cd": "\uabea",  # \uabc9\u09cd -> ꯉ + ্ : \uabea -> ꯪ (\uabe1 -> ꯡ only when prefix is cheitap)
}

mm_e_lonsum_coda = {
    "\uabe5\uabcf": "\uabe5\uabe2",  # \uabe5\uabcf -> ꯥ + ꯏ : \uabe5\uabe2 -> ꯥꯢ
    "\uabe3\uabcf": "\uabe3\uabe2",  # \uabe3\uabcf -> ꯣ + ꯏ : \uabe3\uabe2 -> ꯣꯢ
    "\uabe8\uabcf": "\uabe8\uabe2",  # \uabe8\uabcf -> ꯨ + ꯏ : \uabe8\uabe2 -> ꯨꯢ
    "\uabe5\uabcc": "\uabe5\uabe2",  # \uabe5\uabcc -> ꯥ + ꯌ : \uabe5\uabe2 -> ꯥꯢ
    "\uabe3\uabcc": "\uabe3\uabe2",  # \uabe3\uabcc -> ꯣ + ꯌ : \uabe3\uabe2 -> ꯣꯢ
    "\uabe8\uabcc": "\uabe8\uabe2",  # \uabe8\uabcc -> ꯨ + ꯌ : \uabe8\uabe2 -> ꯨꯢ
}

mm_mapum_to_lonsum = {
    "\uabc0": "\uabdb",  # \uabc0 -> ꯀ : \uabdb -> ꯛ
    "\uabc2": "\uabdc",  # \uabc2 -> ꯂ : \uabdc -> ꯜ
    "\uabc3": "\uabdd",  # \uabc3 -> ꯃ : \uabdd -> ꯝ
    "\uabc4": "\uabde",  # \uabc4 -> ꯄ : \uabde -> ꯞ
    "\uabc5": "\uabdf",  # \uabc5 -> ꯅ : \uabdf -> ꯟ
    "\uabc7": "\uabe0",  # \uabc7 -> ꯇ : \uabe0 -> ꯠ
    "\uabc9": "\uabea",  # \uabc9 -> ꯉ : \uabea -> ꯪ (\uabe1 -> ꯡ only when prefix is cheitap)
    "\uabea": "\uabe1",  # \uabea -> ꯪ : \uabe1 -> ꯡ (it follows the previous map)
    # '\uabc0', # \uabc0 -> ꯀ
    # '\uabc1', # \uabc1 -> ꯁ
    # '\uabc2', # \uabc2 -> ꯂ
    # '\uabc3', # \uabc3 -> ꯃ
    # '\uabc4', # \uabc4 -> ꯄ
    # '\uabc5', # \uabc5 -> ꯅ
    # '\uabc6', # \uabc6 -> ꯆ
    # '\uabc7', # \uabc7 -> ꯇ
    # '\uabc8', # \uabc8 -> ꯈ
    # '\uabc9', # \uabc9 -> ꯉ
    # '\uabca', # \uabca -> ꯊ
    # '\uabcb', # \uabcb -> ꯋ
    # '\uabcc', # \uabcc -> ꯌ
    # '\uabcd', # \uabcd -> ꯍ
    # '\uabce', # \uabce -> ꯎ
    # '\uabcf', # \uabcf -> ꯏ
    # '\uabd0', # \uabd0 -> ꯐ
    # '\uabd1', # \uabd1 -> ꯑ
    # '\uabd2', # \uabd2 -> ꯒ
    # '\uabd3', # \uabd3 -> ꯓ
    # '\uabd4', # \uabd4 -> ꯔ
    # '\uabd5', # \uabd5 -> ꯕ
    # '\uabd6', # \uabd6 -> ꯖ
    # '\uabd7', # \uabd7 -> ꯗ
    # '\uabd8', # \uabd8 -> ꯘ
    # '\uabd9', # \uabd9 -> ꯙ
    # '\uabda', # \uabda -> ꯚ
}

mm_mapum = [
    "\uabc0",  # \uabc0 -> ꯀ
    "\uabc1",  # \uabc1 -> ꯁ
    "\uabc2",  # \uabc2 -> ꯂ
    "\uabc3",  # \uabc3 -> ꯃ
    "\uabc4",  # \uabc4 -> ꯄ
    "\uabc5",  # \uabc5 -> ꯅ
    "\uabc6",  # \uabc6 -> ꯆ
    "\uabc7",  # \uabc7 -> ꯇ
    "\uabc8",  # \uabc8 -> ꯈ
    "\uabc9",  # \uabc9 -> ꯉ
    "\uabca",  # \uabca -> ꯊ
    "\uabcb",  # \uabcb -> ꯋ
    "\uabcc",  # \uabcc -> ꯌ
    "\uabcd",  # \uabcd -> ꯍ
    "\uabce",  # \uabce -> ꯎ
    "\uabcf",  # \uabcf -> ꯏ
    "\uabd0",  # \uabd0 -> ꯐ
    "\uabd1",  # \uabd1 -> ꯑ
    "\uabd2",  # \uabd2 -> ꯒ
    "\uabd3",  # \uabd3 -> ꯓ
    "\uabd4",  # \uabd4 -> ꯔ
    "\uabd5",  # \uabd5 -> ꯕ
    "\uabd6",  # \uabd6 -> ꯖ
    "\uabd7",  # \uabd7 -> ꯗ
    "\uabd8",  # \uabd8 -> ꯘ
    "\uabd9",  # \uabd9 -> ꯙ
    "\uabda",  # \uabda -> ꯚ
]

mm_lonsum = [
    "\uabdb",  # \uabdb -> ꯛ
    "\uabdc",  # \uabdc -> ꯜ
    "\uabdd",  # \uabdd -> ꯝ
    "\uabde",  # \uabde -> ꯞ
    "\uabdf",  # \uabdf -> ꯟ
    "\uabe0",  # \uabe0 -> ꯠ
    "\uabe1",  # \uabe1 -> ꯡ
    "\uabe2",  # \uabe2 -> ꯢ
]

mm_cheitap = [
    "\uabe3",  # \uabe3 -> ꯣ
    "\uabe4",  # \uabe4 -> ꯤ
    "\uabe5",  # \uabe5 -> ꯥ
    "\uabe6",  # \uabe6 -> ꯦ
    "\uabe7",  # \uabe7 -> ꯧ
    "\uabe8",  # \uabe8 -> ꯨ
    "\uabe9",  # \uabe9 -> ꯩ
    "\uabea",  # \uabea -> ꯪ
]

mm_cheising = [
    "\uabf0",  # \uabf0 -> ꯰
    "\uabf1",  # \uabf1 -> ꯱
    "\uabf2",  # \uabf2 -> ꯲
    "\uabf3",  # \uabf3 -> ꯳
    "\uabf4",  # \uabf4 -> ꯴
    "\uabf5",  # \uabf5 -> ꯵
    "\uabf6",  # \uabf6 -> ꯶
    "\uabf7",  # \uabf7 -> ꯷
    "\uabf8",  # \uabf8 -> ꯸
    "\uabf9",  # \uabf9 -> ꯹
]

mm_khudam = [
    "\uabeb",  # \uabeb -> ꯫
    "\uabec",  # \uabec -> ꯬
    "\uabed",  # \uabed -> ꯭
]


############### Transformation Resources #####################
s550_triple_charmap = {
    "\u00de\u00f8\u00fd": "\u09a8\u09cd\u09a7\u09cd\u09b0",  # \u00de\u00f8\u00fd -> Þøý : \u09a8\u09cd\u09a7\u09cd\u09b0 -> ন্ + ধ্ + র -> ন্ধ্র
}


s550_double_charmap = {
    "\u0022\u00e0": "\u0986",  # \u0022\u00e0 -> "à : \u0986 -> আ
    "\u0076\u00fb": "\u0995\u09cd\u09a4",  # \u0076\u00fb -> vû : \u0995\u09cd\u09a4 -> ক্ + ত -> ক্ত
    "\u0079\u00fb": "\u0995\u09cd\u09b0",  # \u0076\u00fb -> yû : \u0995\u09cd\u09a4 -> ক্ + র -> ক্র
    "\u00d2\u00fc": "\u0987",  # \u00d2\u00fc -> Òü : \u0987 -> ই
    "\u00de\u00ea": "\u09a8\u09cd\u09a7",  # \u00de\u00ea -> Þê : \u09a8\u09cd\u09a7 -> ন্ + ধ -> ন্ধ
}


s550_single_single = {
    "\u0021": "\u0021",  # \u0021 -> ! : \u0021 -> !
    "\u0022": "\u0985",  # \u0022 -> " : \u0985 -> অ
    "\u0023": "\u0988",  # \u0023 -> # : \u0988 -> ঈ
    "\u0024": "\u098a",  # \u0024 -> $ : \u098a -> ঊ
    "\u0025": "\u0025",  # \u0025 -> % : \u0025 -> %
    "\u0026": "\u098f",  # \u0026 -> & : \u098f -> এ
    "\u0027": "\u0990",  # \u0027 -> ' : \u0990 -> ঐ
    "\u0028": "\u0028",  # \u0028 -> ( : \u0028 -> (
    "\u0029": "\u0029",  # \u0029 -> ) : \u0029 -> )
    "\u002a": "\u0993",  # \u002a -> * : \u0993 -> ও
    "\u002b": "\u0994",  # \u002b -> + : \u0994 -> ঔ
    "\u002c": "\u002c",  # \u002c -> , : \u002c -> ,
    "\u002d": "\u002d",  # \u002d -> - : \u002d -> -
    "\u002e": "\u002e",  # \u002e -> . : \u002e -> .
    "\u0030": "\u09e6",  # \u0030 -> 0 : \u09e6 -> ০
    "\u0031": "\u09e7",  # \u0031 -> 1 : \u09e7 -> ১
    "\u0032": "\u09e8",  # \u0032 -> 2 : \u09e8 -> ২
    "\u0033": "\u09e9",  # \u0033 -> 3 : \u09e9 -> ৩
    "\u0034": "\u09ea",  # \u0034 -> 4 : \u09ea -> ৪
    "\u0035": "\u09eb",  # \u0035 -> 5 : \u09eb -> ৫
    "\u0036": "\u09ec",  # \u0036 -> 6 : \u09ec -> ৬
    "\u0037": "\u09ed",  # \u0037 -> 7 : \u09ed -> ৭
    "\u0038": "\u09ee",  # \u0038 -> 8 : \u09ee -> ৮
    "\u0039": "\u09ef",  # \u0039 -> 9 : \u09ef -> ৯
    "\u003a": "\u003a",  # \u003a -> : : \u003a -> :
    "\u003b": "\u09ce",  # \u003b -> ; : \u09ce -> ৎ
    "\u003d": "\u09a5",  # \u003d -> = : \u09a5 -> থ
    "\u003e": "\u09a8",  # \u003e -> > : \u09a8 -> ন
    "\u003f": "\u003f",  # \u003f -> ? : \u003f -> ?
    "\u0040": "\u0983",  # \u0040 -> @ : \u0983 -> ঃ
    "\u0041": "\u0995",  # \u0041 -> A : \u0995 -> ক
    "\u004a": "\u0996",  # \u004a -> J : \u0996 -> খ
    "\u004b": "\u0997",  # \u004b -> K : \u0997 -> গ (removed viramma suffix)
    "\u004e": "\u0997",  # \u004e -> N : \u0997 -> গ
    "\u0051": "\u0998",  # \u0051 -> Q : \u0998 -> ঘ
    "\u0052": "\u0999",  # \u0052 -> R : \u0999 -> ঙ
    "\u0057": "\u099a",  # \u0057 -> W : \u099a -> চ
    "\u005b": "\u09bf",  # \u005b -> [ : \u09bf -> ি
    "\u005c": "\u099c",  # \u005c -> \ : \u099c -> জ
    "\u0063": "\u099d",  # \u0063 -> c : \u099d -> ঝ
    "\u0064": "\u099e",  # \u0064 -> d : \u099e -> ঞ
    "\u0069": "\u099f",  # \u0069 -> i : \u099f -> ট
    "\u006b": "\u09a0",  # \u006b -> k : \u09a0 -> ঠ
    "\u006c": "\u0989",  # \u006c -> l : \u0989 -> উ
    "\u006e": "\u09a2",  # \u006e -> n : \u09a2 -> ঢ
    "\u006f": "\u09a3",  # \u006f -> o : \u09a3 -> ণ
    "\u0074": "\u09a4",  # \u0074 -> t : \u09a4 -> ত
    "\u007d": "\u0982",  # \u007d -> } : \u0982 -> ং
    "\u00a3": "\u09ab",  # \u00a3 -> £ : \u09ab -> ফ
    "\u00a4": "\u09ac",  # \u00a4 -> ¤ : \u09ac -> ব
    "\u00ac": "\u09ac",  # \u00ac -> ¬ : \u09ac -> ব (removed viramma prefix)
    "\u00a5": "\u0981",  # \u00a5 -> ¥ : \u0981 -> ঁ
    "\u00ae": "\u09ad",  # \u00ae -> ® : \u09ad -> ভ
    "\u00af": "\u09f1",  # \u00af -> ¯ : \u09f1 -> ৱ (check)
    "\u00b3": "\u09ae",  # \u00b3 -> ³ : \u09ae -> ম
    "\u00b9": "\u09b0",  # \u00b9 -> ¹ : \u09b0 -> র
    "\u00ba": "\u09b2",  # \u00ba -> º : \u09b2 -> ল
    "\u00c5": "\u09b6",  # \u00c5 -> Å : \u09b6 -> শ
    "\u00c8": "\u09b7",  # \u00c8 -> È : \u09b7 -> ষ
    "\u00ce": "\u09b8",  # \u00ce -> Î : \u09b8 -> স
    "\u00d2": "\u09b9",  # \u00d2 -> Ò : \u09b9 -> হ
    "\u00d8": "\u09dc",  # \u00d8 -> Ø : \u09dc -> ড় (changed)
    "\u00da": "\u09df",  # \u00da -> Ú : \u09df -> য়
    "\u00e0": "\u09be",  # \u00e0 -> à : \u09be -> া
    "\u00e1": "\u099b",  # \u00e1 -> á : \u099b -> ছ
    "\u00e2": "\u09a4",  # \u00e2 -> â : \u09a4 -> ত
    "\u00e3": "\u09c0",  # \u00e3 -> ã : \u09c0 -> ী
    "\u00e5": "\u09c1",  # \u00e5 -> å : \u09c1 -> ু
    "\u00e6": "\u09c1",  # \u00e6 -> æ : \u09c1 -> ু
    "\u00e7": "\u09c1",  # \u00e7 -> ç : \u09c1 -> ু
    "\u00e8": "\u09c2",  # \u00e8 -> è : \u09c2 -> ূ
    "\u00e9": "\u09c2",  # \u00e9 -> é : \u09c2 -> ূ
    "\u00ea": "\u09c2",  # \u00ea -> ê : \u09c2 -> ূ (check, found as fragment for dha sound)
    "\u00eb": "\u09c7",  # \u00eb -> ë : \u09c7 -> ে
    "\u00ec": "\u09c7",  # \u00ec -> ì : \u09c7 -> ে
    "\u00ed": "\u09c8",  # \u00ed -> í : \u09c8 -> ৈ
    "\u00ee": "\u09c8",  # \u00ee -> î : \u09c8 -> ৈ
    "\u00ef": "\u09d7",  # \u00ef -> ï : \u09d7 -> ৗ
    "\u00f1": "\u0993",  # \u00f1 -> ñ : \u0993 -> ও
    "\u00f2": "\u0981",  # \u00f2 -> ò : \u0981 -> ঁ
    "\u00f3": "\u09ab",  # \u00f3 -> ó : \u09ab -> ফ
    "\u00f4": "\u09cd",  # \u00f4 -> ô : \u09cd -> ্
    "\u00f5": "\u09c3",  # \u00f5 -> õ : \u09c3 -> ৃ
    "\u00fa": "\u200c",  # \u00fa -> ú : \u200c -> whitespace
    "\u00fc": "",  # \u00fc -> ü : whitespace
    "\u0161": "\u09aa",  # \u0022 -> š : \u09aa -> প
    "\u0192": "\u09a6",  # \u0192 -> ƒ : \u09a6 -> দ
    "\u2018": "\u2018",  # \u2018 -> ‘ : \u2018 -> ‘
    "\u2019": "\u2019",  # \u2019 -> ’ : \u2019 -> ’
    "\u201a": "\u09a5",  # \u201a -> ‚ : \u09a5 -> থ
    "\u2039": "\u09a7",  # \u2039 -> ‹ : \u09a7 -> ধ
    "\u2122": "\u09df",  # \u2122 -> ™ : \u09df -> য়
}


s550_prefix = {
    "\u002f": "\u09ac\u09cd",  # \u002f -> / : \u09ac\u09cd -> ব্
    "\u004f": "\u0997\u09cd",  # \u004f -> O : \u0997\u09cd -> গ্
    "\u0056": "\u0999\u09cd",  # \u0056 -> V : \u0999\u09cd -> ঙ্
    "\u005a": "\u099a\u09cd",  # \u005a -> Z : \u099a\u09cd -> চ্
    "\u0073": "\u09a3\u09cd",  # \u0073 -> s : \u09a3\u09cd -> ণ্
    "\u00a9": "\u09b9\u09cd",  # \u00a9 -> © : \u09b9\u09cd -> হ্
    "\u00b4": "\u09ae\u09cd",  # \u00b4 -> ´ : \u09ae\u09cd -> ম্
    "\u00c2": "\u09b2\u09cd",  # \u00c2 -> Â : \u09b2\u09cd -> ল্
    "\u00c6": "\u09b6\u09cd",  # \u00c6 -> Æ : \u09b6\u09cd -> শ্
    "\u00cd": "\u09b7\u09cd",  # \u00cd -> Í : \u09b7\u09cd -> ষ্
    "\u00d1": "\u09b8\u09cd",  # \u00d1 -> Ñ : \u09b8\u09cd -> স্
    "\u0160": "\u09a6\u09cd",  # \u0160 -> Š : \u09a6\u09cd -> দ্
    "\u0178": "\u09aa\u09cd",  # \u0178 -> Ÿ : \u09aa\u09cd -> প্
    "\u2013": "\u09a8\u09cd",  # \u2013 -> – : \u09a8\u09cd -> ন্
    "\u201d": "\u09a8\u09cd",  # \u201d -> ” : \u09a8\u09cd -> ন্
}

# ! Some undesired error
# s550_prefix = {
#     "\u002f": "\u09ac",  # \u002f -> / : \u09ac\u09cd -> ব্
#     "\u004f": "\u0997",  # \u004f -> O : \u0997\u09cd -> গ্
#     "\u0056": "\u0999",  # \u0056 -> V : \u0999\u09cd -> ঙ্
#     "\u005a": "\u099a",  # \u005a -> Z : \u099a\u09cd -> চ্
#     "\u0073": "\u09a3",  # \u0073 -> s : \u09a3\u09cd -> ণ্
#     "\u00a9": "\u09b9",  # \u00a9 -> © : \u09b9\u09cd -> হ্
#     "\u00b4": "\u09ae",  # \u00b4 -> ´ : \u09ae\u09cd -> ম্
#     "\u00c2": "\u09b2",  # \u00c2 -> Â : \u09b2\u09cd -> ল্
#     "\u00c6": "\u09b6",  # \u00c6 -> Æ : \u09b6\u09cd -> শ্
#     "\u00cd": "\u09b7",  # \u00cd -> Í : \u09b7\u09cd -> ষ্
#     "\u00d1": "\u09b8",  # \u00d1 -> Ñ : \u09b8\u09cd -> স্
#     "\u0160": "\u09a6",  # \u0160 -> Š : \u09a6\u09cd -> দ্
#     "\u0178": "\u09aa",  # \u0178 -> Ÿ : \u09aa\u09cd -> প্
#     "\u2013": "\u09a8",  # \u2013 -> – : \u09a8\u09cd -> ন্
#     "\u201d": "\u09a8",  # \u201d -> ” : \u09a8\u09cd -> ন্
# }


s550_suffix = {
    "\u0048": "\u09cd\u0995",  # \u0048 -> H : \u09cd\u0995 -> ্ক
    "\u007a": "\u09cd\u09a4",  # \u007a -> z : \u09cd\u09a4 -> ্ত
    "\u00ab": "\u09cd\u09ac",  # \u00ab -> « : \u09cd\u09ac -> ্ব (changed from viramma suffix to prefix)
    "\u00b1": "\u09cd\u09ad",  # \u00b1 -> ± : \u09cd\u09ad -> ্ভ
    "\u00b5": "\u09cd\u09ae",  # \u00b5 -> µ : \u09cd\u09ae -> ্ম
    "\u00b6": "\u09cd\u09ae",  # \u00b6 -> ¶ : \u09cd\u09ae -> ্ম
    "\u00b8": "\u09cd\u09af",  # \u00b8 -> ¸ : \u09cd\u09af -> ্য
    "\u00c3": "\u09cd\u09b2",  # \u00c3 -> Ã : \u09cd\u09b2 -> ্ল
    "\u00f6": "\u09cd\u09b0",  # \u00f6 -> ö : \u09cd\u09b0 -> ্র
    "\u00f7": "\u09cd\u09b0",  # \u00f7 -> ÷ : \u09cd\u09b0 -> ্র
    "\u00f8": "\u09cd\u09b0",  # \u00f8 -> ø : \u09cd\u09b0 -> ্র
    "\u00f9": "\u09cd\u09b0",  # \u00f9 -> ù : \u09cd\u09b0 -> ্র
    "\u2014": "\u09cd\u09a8",  # \u2014 -> — : \u09cd\u09a8 -> ্ন
    "\u2022": "\u09cd\u09a8",  # \u2022 -> • : \u09cd\u09a8 -> ্ন
}


s550_single_double_v = {
    "\u0050": "\u0997\u09c1",  # \u0050 -> P : \u0997\u09c1 -> গু
    "\u005d": "\u09d7\u0981",  # \u005d -> ] : \u09d7\u0981 -> ৗঁ
    "\u007b": "\u09bf\u0981",  # \u007b -> { : \u09bf\u0981 -> িঁ  (this need to be moved left together)
    "\u00c7": "\u09b6\u09c1",  # \u00c7 -> Ç : \u09b6\u09c1 -> শু
    "\u00d7": "\u09b9\u09c1",  # \u00d7 -> × : \u09b9\u09c1 -> হু
    "\u2026": "\u09c0\u0981",  # \u2026 -> … : \u09c0\u0981 -> ীঁ
}


s550_single_double = {
    "\u0042": "\u0995\u09cd\u0995",  # \u0042 -> B : \u0995\u09cd\u0995 -> ক্ + ক -> ক্ক
    "\u0043": "\u0995\u09cd\u099f",  # \u0043 -> C : \u0995\u09cd\u099f -> ক্ + ট -> ক্ট
    "\u0045": "\u0995\u09cd\u09ac",  # \u0045 -> E : \u0995\u09cd\u09ac -> ক্ + ব -> ক্ব
    "\u0046": "\u0995\u09cd\u09ae",  # \u0046 -> F : \u0995\u09cd\u09ae -> ক্ + ম -> ক্ম
    "\u0047": "\u0995\u09cd\u09b8",  # \u0047 -> G : \u0995\u09cd\u09b8 -> ক্ + স -> ক্স
    "\u0049": "\u0995\u09cd\u09b0",  # \u0049 -> I : \u0995\u09cd\u09b0 -> ক্ + র -> ক্র
    "\u004c": "\u0997\u09cd\u0997",  # \u004c -> L : \u0997\u09cd\u0997 -> গ্ + গ -> গ্গ
    "\u004d": "\u0997\u09cd\u09ac",  # \u004d -> M : \u0997\u09cd\u09ac -> গ্ + ব -> গ্ব
    "\u0053": "\u0999\u09cd\u0995",  # \u0053 -> S : \u0999\u09cd\u0995 -> ঙ্ + ক -> ঙ্ক
    "\u0054": "\u0999\u09cd\u0996",  # \u0054 -> T : \u0999\u09cd\u0996 -> ঙ্ + খ -> ঙ্খ
    "\u0055": "\u0999\u09cd\u0997",  # \u0055 -> U : \u0999\u09cd\u0997 -> ঙ্ + গ -> ঙ্গ
    "\u0058": "\u09a8\u09cd\u09b8",  # \u0058 -> X : \u09a8\u09cd\u09b8 -> ন্ + স -> ন্স
    "\u005f": "\u099c\u09cd\u099d",  # \u005f -> _ : \u099c\u09cd\u099d -> জ্ + ঝ -> জ্ঝ
    "\u0060": "\u099c\u09cd\u099e",  # \u0060 -> ` : \u099c\u09cd\u099e -> জ্ + ঞ -> জ্ঞ
    "\u0061": "\u099c\u09cd\u09ac",  # \u0061 -> a : \u099c\u09cd\u09ac -> জ্ + ব -> জ্ব
    "\u0062": "\u099c\u09cd\u09b0",  # \u0062 -> b : \u099c\u09cd\u09b0 -> জ্ + র -> জ্র
    "\u0065": "\u099e\u09cd\u099a",  # \u0065 -> e : \u099e\u09cd\u099a -> ঞ্ + চ -> ঞ্চ
    "\u0066": "\u099e\u09cd\u099b",  # \u0066 -> f : \u099e\u09cd\u099b -> ঞ্ + ছ -> ঞ্ছ
    "\u0067": "\u099e\u09cd\u099c",  # \u0067 -> g : \u099e\u09cd\u099c -> ঞ্ + জ -> ঞ্জ
    "\u0068": "\u099e\u09cd\u099d",  # \u0068 -> h : \u099e\u09cd\u099d -> ঞ্ + ঝ -> ঞ্ঝ
    "\u006a": "\u099f\u09cd\u099f",  # \u006a -> j : \u099f\u09cd\u099f -> ট্ + ট -> ট্ট
    "\u006d": "\u09a1\u09cd\u09a1",  # \u006d -> m : \u09a1\u09cd\u09a1 -> ড্ + ড -> ড্ড
    "\u0070": "\u09a3\u09cd\u09a3",  # \u0070 -> p : \u09a3\u09cd\u09a3 -> ণ্ + ণ -> ণ্ণ
    "\u0071": "\u09a3\u09cd\u09a0",  # \u0071 -> q : \u09a3\u09cd\u09a0 -> ণ্ + ঠ ->  ণ্ঠ
    "\u0072": "\u09a3\u09cd\u09a1",  # \u0072 -> r : \u09a3\u09cd\u09a1 -> ণ্ + ড -> ণ্ড
    "\u0075": "\u09a4\u09cd\u09ae",  # \u0075 -> u : \u09a4\u09cd\u09ae -> ত্ + ম -> ত্ম
    "\u0076": "\u09a4\u09cd\u09a4",  # \u0076 -> v : \u09a4\u09cd\u09a4 -> ত্ + ত -> ত্ত
    "\u0078": "\u09a4\u09cd\u09a5",  # \u0078 -> x : \u09a4\u09cd\u09a5 -> ত্ + থ -> ত্থ
    "\u0079": "\u09a4\u09cd\u09b0",  # \u0079 -> y : \u09a4\u09cd\u09b0 -> ত্ + র -> ত্র
    "\u007c": "\u09a4\u09cd\u09b0",  # \u007c -> | : \u09a4\u09cd\u09b0 -> ত্ + র -> ত্র (changed from ae to tra)
    "\u00a6": "\u09ac\u09cd\u09a6",  # \u00a6 -> ¦ : \u09ac\u09cd\u09a6 -> ব্ + দ -> ব্দ
    "\u00a7": "\u09ac\u09cd\u09a7",  # \u00a7 -> § : \u09ac\u09cd\u09a7 -> ব্ + ধ -> ব্ধ
    "\u00a8": "\u09ac\u09cd\u099d",  # \u00a8 -> ¨ : \u09ac\u09cd\u099d -> ব্ + ঝ -> ব্ঝ (check once)
    "\u00aa": "\u09ac\u09cd\u099c",  # \u00aa -> ª : \u09ac\u09cd\u099c -> ব্ + জ -> ব্জ
    "\u00b0": "\u09ad\u09cd\u09b0",  # \u00b0 -> ° : \u09ad\u09cd\u09b0 -> ভ্ + র -> ভ্র
    "\u00b2": "\u09cd\u09ad\u09cd\u09b0",  # \u00b2 -> ² : \u09cd\u09ad\u09cd\u09b0 -> ্ + ভ্ + র ->   ্ভ্র
    "\u00bb": "\u09b2\u09cd\u0995",  # \u00bb -> » : \u09b2\u09cd\u0995 -> ল্ + ক -> ল্ক
    "\u00bc": "\u09b2\u09cd\u0997",  # \u00bc -> ¼ : \u09b2\u09cd\u0997 -> ল্ + গ -> ল্গ
    "\u00be": "\u09b2\u09cd\u09ac",  # \u00be -> ¾ : \u09b2\u09cd\u09ac -> ল্ + ব -> ল্ব
    "\u00bf": "\u09b2\u09cd\u09aa",  # \u00bf -> ¿ : \u09b2\u09cd\u09aa -> ল্ + প -> ল্প
    "\u00c0": "\u09b2\u09cd\u09b2",  # \u00c0 -> À : \u09b2\u09cd\u09b2 -> ল্ + ল -> ল্ল
    "\u00c1": "\u09b2\u09cd\u09a1",  # \u00c1 -> Á : \u09b2\u09cd\u09a1 -> ল্ +  -> ল্
    "\u00c4": "\u09a8\u09cd\u09a8",  # \u00c4 -> Ä : \u09a8\u09cd\u09a8 -> ন্ + ন -> ন্ন
    "\u00c9": "\u09b7\u09cd\u09ac",  # \u00c9 -> É : \u09b7\u09cd\u09ac -> ষ্ + ব -> ষ্ব
    "\u00ca": "\u09b7\u09cd\u099f",  # \u00ca -> Ê : \u09b7\u09cd\u099f -> ষ্ + ট ->  ষ্ট
    "\u00cb": "\u09b7\u09cd\u09a0",  # \u00cb -> Ë : \u09b7\u09cd\u09a0 -> ষ্ + ঠ ->  ষ্ঠ
    "\u00cc": "\u09b7\u09cd\u09a3",  # \u00cc -> Ì : \u09b7\u09cd\u09a3 -> ষ্ + ণ -> ষ্ণ
    "\u00cf": "\u09b8\u09cd\u0996",  # \u00cf -> Ï : \u09b8\u09cd\u0996 -> স্ + খ -> স্খ
    "\u00d0": "\u09b8\u09cd\u099f",  # \u00d0 -> Ð : \u09b8\u09cd\u099f -> ষ্ + ট -> ষ্ট
    "\u00d3": "\u09b9\u09cd\u09b2",  # \u00d3 -> Ó : \u09b9\u09cd\u09b2 -> হ্ + ল -> হ্ল
    "\u00d4": "\u09b9\u09cd\u09ac",  # \u00d4 -> Ô : \u09b9\u09cd\u09ac -> হ্ + ব -> হ্ব
    "\u00d5": "\u09b9\u09cd\u09ae",  # \u00d5 -> Õ : \u09b9\u09cd\u09ae -> হ্ + ম -> হ্ম
    "\u00d6": "\u09b9\u09cd\u09a3",  # \u00d6 -> Ö : \u09b9\u09cd\u09a3 -> হ্ + ণ -> হ্ণ
    "\u00d9": "\u09aa\u09cd\u09aa",  # \u00d9 -> Ù : \u09aa\u09cd\u09aa -> প্ + প -> প্প
    "\u00db": "\u0995\u09cd\u09b7",  # \u00db -> Û : \u0995\u09cd\u09b7 -> ক্ + ষ -> ক্ষ
    "\u00de": "\u09a8\u09cd\u09a7\u09cd",  # \u00de -> Þ : \u09a8\u09cd\u09a7\u09cd -> ন্ + ধ্ -> ন্ধ্
    "\u00df": "\u09aa\u09cd\u09b0",  # \u00df -> ß : \u09aa\u09cd\u09b0 -> প্ + র -> প্র
    "\u00f0": "\u099c\u09cd\u099c",  # \u00f0 -> ð : \u099c\u09cd\u099c -> জ্ + জ -> জ্জ
    "\u0152": "\u09a7\u09cd\u09ae",  # \u0152 -> Œ : \u09a7\u09cd\u09ae -> ধ্ + ম->ধ্ম (check once)
    "\u0153": "\u09aa\u09cd\u09a4",  # \u0153 -> œ : \u09aa\u09cd\u09a4 -> প্ + ত -> প্ত
    "\u02c6": "\u09a6\u09cd\u09ae",  # \u02c6 -> ˆ : \u09a6\u09cd\u09ae -> দ্ + ম -> দ্ম
    "\u02dc": "\u09b8\u09cd\u09a7",  # \u02dc -> ˜ : \u09b8\u09cd\u09a7 -> স্ + ধ -> স্ধ (check once)
    "\u201c": "\u09a8\u09cd\u09a1",  # \u201c -> “ : \u09a8\u09cd\u09a1 -> ন্ + ড -> ন্ড
    "\u201e": "\u09a6\u09cd\u09a6",  # \u201e -> „ : \u09a6\u09cd\u09a6 -> দ্ + দ -> দ্দ
    "\u2021": "\u09a6\u09cd\u09ac",  # \u2021 -> ‡ : \u09a6\u09cd\u09ac -> দ্ + ব -> দ্ব
    "\u2030": "\u09a6\u09cd\u09b0",  # \u2030 -> ‰ : \u09a6\u09cd\u09b0 -> দ্ + র -> দ্র
    "\u203a": "\u09aa\u09cd\u09b8",  # \u203a -> › : \u09aa\u09cd\u09b8 -> প্ + স -> প্স
}

s550_single_triple = {
    "\u0044": "\u0995\u09cd\u09a4\u09cd\u09ac",  # \u0044 -> D : \u0995\u09cd\u09a4\u09cd\u09ac -> ক্ত্ব
    "\u0059": "\u099a\u09cd\u099b\u09cd\u09ac",  # \u0059 -> Y : \u099a\u09cd\u099b\u09cd\u09ac -> চ্ছ্ব
    "\u005e": "\u099c\u09cd\u099c\u09cd\u09ac",  # \u005e -> ^ : \u099c\u09cd\u099c\u09cd\u09ac -> জ্জ্ব
    "\u0077": "\u09a4\u09cd\u09a4\u09cd\u09ac",  # \u0077 -> w : \u09a4\u09cd\u09a4\u09cd\u09ac -> ত্ত্ব
    "\u00bd": "\u09b2\u09cd\u0997\u09c1",  # \u00bd -> ½ : \u09b2\u09cd\u0997\u09c1 -> ল্গু
    "\u00dc": "\u0995\u09cd\u09b7\u09cd\u09ae",  # \u00dc -> Ü : \u0995\u09cd\u09b7\u09cd\u09ae -> ক্ষ্ম
    "\u00dd": "\u0995\u09cd\u09b7\u09cd\u09a8",  # \u00dd -> Ý : \u0995\u09cd\u09b7\u09cd\u09a8 -> ক্ষ্নS
    "\u00e4": "\u09a6\u09cd\u09a6\u09cd\u09ac",  # \u00e4 -> ä : \u09a6\u09cd\u09a6\u09cd\u09ac -> দ্দ্ব
    "\u2020": "\u09a9\u09cd\u09a7\u09cd\u09ac",  # \u2020 -> † : \u09a9\u09cd\u09a7\u09cd\u09ac -> ঩্ধ্ব (check once)
}

s550_single_xtra = {
    "\x81": "\u09ac\u09cd\u09a2",  # \x81 -> (invisible) : \u09ac\u09cd\u09a2 -> ব্ঢ
    "\x90": "\u099a\u09cd\u099e",  # \x90 -> (invisible) : \u099a\u09cd\u099e -> চ্ঞ
    "\xa0": "\u00a0",  # \xa0 -> (invisible) : \u00a0 -> (invisible)
    "\xad": "\u09a8\u09cd",  # \xad -> (invisible) : \u09a8\u09cd -> ন্
    "\u0081": "\u09F1",  # \u0081 -> (invisible) : \u09F1 -> ৱ
    "\u008f": "\u09a8\u09cd\u09a8",  # \u008f -> (invisible) : \u09a8\u09cd\u09a8 -> ন্ন (added)
    "\u0090": "\u09a8\u09cd\u09b8",  # \u0090 -> (invisible) : \u09a8\u09cd\u09b8 -> ন্স (added)
    "\u009d": "\u09aa\u09cd\u09aa",  # \u009d -> (invisible) : \u09aa\u09cd\u09aa -> প্প (added)
}


bn_double_vowel_charmap = {
    "\u09c7\u09be": "\u09cb",  # \u09c7\u09be -> ে +  া : \u09cb ->  ো
    "\u09c7\u09d7": "\u09cc",  # \u09c7\u09d7 -> ে +  ৗ : \u09cc ->  ৌ
}


bn_fix_error_charmap = {
    "\u0985\u09be": "\u0986",  # \u0985\u09be -> অ + া : \u0986 -> আ
    "\u09cb\u09be": "\u09cb",  # \u09cb\u09be -> ো + া : \u09cb -> ো
    "\u09cc\u09d7": "\u09cc",  # \u09cc\u09d7 -> ৌ + ৗ : \u09cc -> ৌl[fe]
    "\u09cd\u09cd": "\u09cd",  # \u09cd\u09cd -> ্ +  ্ : \u09cd -> ্
}


s550_post_charmap = {"\u00a2": "\u09b0\u09cd"}  # \u00a2 -> ¢ : \u09b0\u09cd -> র্


s550_invisible_char = [
    "\u00a1",  # \u00a1 -> ¡
    "\u00fe",  # \u00fe -> þ
    "\u00ff",  # \u00ff -> ÿ
    "\uf000",  # \uf000 -> 
]

s550_suffix_char_r = [
    "\u00a2",  # \u00a2 -> ¢
]

bn_prefix_char_v = [
    "\u09bf",  # \u09bf -> ি
    "\u09c7",  # \u09c7 -> ে
    "\u09c8",  # \u09c8 -> ৈ
]

bn_suffix_char_v = [
    "\u09be",  # \u09be -> া
    "\u09c0",  # \u09c1 -> ী
    "\u09c1",  # \u09c1 -> ু
    "\u09c2",  # \u09c2 -> ূ
    "\u09c3",  # \u09c3 -> ৃ
]
