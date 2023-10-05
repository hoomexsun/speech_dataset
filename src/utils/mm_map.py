from typing import Dict


MM_ONSET = {
    "\u0995": "\uabc0",  # \u0995 -> ক : \uabc0 -> ꯀ
    "\u099b": "\uabc1",  # \u099b -> ছ : \uabc1 -> ꯁ
    "\u09b6": "\uabc1",  # \u09b6 -> শ : \uabc1 -> ꯁ
    "\u09b7": "\uabc1",  # \u09b7 -> ষ : \uabc1 -> ꯁ
    "\u09b8": "\uabc1",  # \u09b8 -> স : \uabc1 -> ꯁ
    "\u09b2": "\uabc2",  # \u09b2 -> ল : \uabc2 -> ꯂ
    "\u09ae": "\uabc3",  # \u09ae -> ম : \uabc3 -> ꯃ
    "\u09aa": "\uabc4",  # \u09aa -> প : \uabc4 -> ꯄ
    "\u099e": "\uabc5",  # \u099e -> ঞ : \uabc5 -> ꯅ
    "\u09a3": "\uabc5",  # \u09a3 -> ণ : \uabc5 -> ꯅ
    "\u09a8": "\uabc5",  # \u09a8 -> ন : \uabc5 -> ꯅ
    "\u099a": "\uabc6",  # \u099a -> চ : \uabc6 -> ꯆ
    "\u099f": "\uabc7",  # \u099f -> ট : \uabc7 -> ꯇ
    "\u09a4": "\uabc7",  # \u09a4 -> ত : \uabc7 -> ꯇ
    "\u0996": "\uabc8",  # \u0996 -> খ : \uabc8 -> ꯈ
    "\u0999": "\uabc9",  # \u0999 -> ঙ : \uabc9 -> ꯉ
    "\u09a0": "\uabca",  # \u09a0 -> ঠ : \uabca -> ꯊ
    "\u09a5": "\uabca",  # \u09a5 -> থ : \uabca -> ꯊ
    "\u09f1": "\uabcb",  # \u09f1 -> ৱ : \uabcb -> ꯋ
    "\u09af": "\uabcc",  # \u09af -> য় : \uabcc -> ꯌ (not there in s550)
    "\u09df": "\uabcc",  # \u09df -> য় : \uabcc -> ꯌ
    "\u09b9": "\uabcd",  # \u09b9 -> হ : \uabcd -> ꯍ
    "\u09ab": "\uabd0",  # \u09ab -> ফ : \uabd0 -> ꯐ
    "\u0997": "\uabd2",  # \u0997 -> গ : \uabd2 -> ꯒ
    "\u099d": "\uabc3",  # \u099d -> ঝ : \uabd3 -> ꯓ
    "\u09b0": "\uabd4",  # \u09b0 -> র : \uabd4 -> ꯔ
    "\u09c3": "\uabe4",  # \u09c3 -> ৃ : \uabe4 -> ꯔ
    "\u09dc": "\uabd4",  # \u09dc -> ড় : \uabd4 -> ꯔ
    "\u09dd": "\uabd4",  # \u09dd -> ঢ় : \uabd4 -> ꯔ (not there in s550)
    "\u09f0": "\uabd4",  # \u09f1 -> ৰ : \uabd4 -> ꯔ (not there in s550)
    "\u098b": "\uabe4",  # \u098b -> ঋ : \uabe4 -> ꯔ
    "\u09ac": "\uabd5",  # \u09ac -> ব : \uabd5 -> ꯕ
    "\u099c": "\uabd6",  # \u099c -> জ : \uabd6 -> ꯖ
    "\u09a1": "\uabd7",  # \u09a1 -> ড : \uabd7 -> ꯗ (not there in s550)
    "\u09a6": "\uabd7",  # \u09a6 -> দ : \uabd7 -> ꯗ
    "\u0998": "\uabd8",  # \u0998 -> ঘ : \uabd8 -> ꯘ
    "\u09a2": "\uabd9",  # \u09a2 -> ঢ : \uabd9 -> ꯙ
    "\u09a7": "\uabd9",  # \u09a7 -> ধ : \uabd9 -> ꯙ
    "\u09ad": "\uabda",  # \u09ad -> ভ : \uabda -> ꯚ
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

MM_CODA = {
    "\u0995": "\uabdb",  # \u0995 -> ক : \uabdb -> ꯛ
    "\u099b": "\uabc1",  # \u099b -> ছ : \uabc1 -> ꯁ
    "\u09b6": "\uabc1",  # \u09b6 -> শ : \uabc1 -> ꯁ
    "\u09b7": "\uabc1",  # \u09b7 -> ষ : \uabc1 -> ꯁ
    "\u09b8": "\uabc1",  # \u09b8 -> স : \uabc1 -> ꯁ
    "\u09b2": "\uabdc",  # \u09b2 -> ল : \uabdc -> ꯜ
    "\u09ae": "\uabdd",  # \u09ae -> ম : \uabdd -> ꯝ
    "\u09aa": "\uabde",  # \u09aa -> প : \uabde -> ꯞ
    "\u099e": "\uabdf",  # \u099e -> ঞ : \uabdf -> ꯟ
    "\u09a3": "\uabdf",  # \u09a3 -> ণ : \uabdf -> ꯟ
    "\u09a8": "\uabdf",  # \u09a8 -> ন : \uabdf -> ꯟ
    "\u099a": "\uabc6",  # \u099a -> চ : \uabc6 -> ꯆ
    "\u099f": "\uabe0",  # \u099f -> ট : \uabe0 -> ꯠ
    "\u09a4": "\uabe0",  # \u09a4 -> ত : \uabe0 -> ꯠ
    "\u09ce": "\uabe0",  # \u09ce -> ৎ : \uabe0 -> ꯠ
    "\u0996": "\uabc8",  # \u0996 -> খ : \uabc8 -> ꯈ
    "\u0999": "\uabc9",  # \u0999 -> ঙ : \uabea -> ꯪ
    "\u09a0": "\uabca",  # \u09a0 -> ঠ : \uabca -> ꯊ
    "\u09a5": "\uabca",  # \u09a5 -> থ : \uabca -> ꯊ
    "\u09f1": "\uabcb",  # \u09f1 -> ৱ : \uabcb -> ꯋ
    "\u09af": "\uabcc",  # \u09af -> য় : \uabcc -> ꯌ (not there in s550)
    "\u09df": "\uabcc",  # \u09df -> য় : \uabcc -> ꯌ
    "\u09b9": "\uabcd",  # \u09b9 -> হ : \uabcd -> ꯍ
    "\u09ab": "\uabd0",  # \u09ab -> ফ : \uabd0 -> ꯐ
    "\u0997": "\uabd2",  # \u0997 -> গ : \uabd2 -> ꯒ
    "\u099d": "\uabc3",  # \u099d -> ঝ : \uabd3 -> ꯓ
    "\u09b0": "\uabd4",  # \u09b0 -> র : \uabd4 -> ꯔ
    "\u09dc": "\uabd4",  # \u09dc -> ড় : \uabd4 -> ꯔ
    "\u09dd": "\uabd4",  # \u09dd -> ঢ় : \uabd4 -> ꯔ (not there in s550)
    "\u09f0": "\uabd4",  # \u09f1 -> ৰ : \uabd4 -> ꯔ (not there in s550)
    "\u098b": "\uabe4",  # \u098b -> ঋ : \uabe4 -> ꯔ
    "\u09ac": "\uabd5",  # \u09ac -> ব : \uabd5 -> ꯕ
    "\u099c": "\uabd6",  # \u099c -> জ : \uabd6 -> ꯖ
    "\u09a1": "\uabd7",  # \u09a1 -> ড : \uabd7 -> ꯗ (not there in s550)
    "\u09a6": "\uabd7",  # \u09a6 -> দ : \uabd7 -> ꯗ
    "\u0998": "\uabd8",  # \u0998 -> ঘ : \uabd8 -> ꯘ
    "\u09a2": "\uabd9",  # \u09a2 -> ঢ : \uabd9 -> ꯙ
    "\u09a7": "\uabd9",  # \u09a7 -> ধ : \uabd9 -> ꯙ
    "\u09ad": "\uabda",  # \u09ad -> ভ : \uabda -> ꯚ
}


MM_NUCLEUS_BEGIN = {
    "\u0985": "\uabd1",  # \u0985 -> অ : \uabd1 -> ꯑ
    "\u0986": "\uabd1\uabe5",  # \u0986 -> আ : \uabd1\uabe5 -> ꯑꯥ
    "\u0987": "\uabcf",  # \u0987 -> ই : \uabcf -> ꯏ
    "\u0988": "\uabcf",  # \u0988 -> ঈ : \uabcf -> ꯏ
    "\u0989": "\uabce",  # \u0989 -> উ : \uabce -> ꯎ
    "\u098a": "\uabce",  # \u098a -> ঊ : \uabce -> ꯎ
    "\u098f": "\uabd1\uabe6",  # \u098f -> এ : \uabd1\uabe6 -> ꯑꯦ
    "\u0990": "\uabd1\uabe9",  # \u0990 -> ঐ : \uabd1\uabe9 -> ꯑꯩ
    "\u0993": "\uabd1\uabe3",  # \u0993 -> ও : \uabd1\uabe3 -> ꯑꯣ
    "\u0994": "\uabd1\uabe7",  # \u0994 -> ঔ : \uabd1\uab -> ꯑꯧ
}

MM_NUCLEUS_MID = {
    "\u09be": "\uabe5",  # \u09be -> া : \uabe5 -> ꯥ
    "\u09bf": "\uabe4",  # \u09bf -> ি : \uabe4 -> ꯤ
    "\u09c0": "\uabe4",  # \u09c0 -> ী : \uabe4 -> ꯤ
    "\u09c1": "\uabe8",  # \u09c1 -> ু : \uabe8 -> ꯨ
    "\u09c2": "\uabe8",  # \u09c2 -> ূ : \uabe8 -> ꯨ
    "\u09c7": "\uabe6",  # \u09c7 -> ে : \uabe6 -> ꯦ
    "\u09c8": "\uabe9",  # \u09c8 -> ৈ : \uabe9 -> ꯩ
    "\u09cb": "\uabe3",  # \u09cb -> ো : \uabe3 -> ꯣ
    "\u09cc": "\uabe7",  # \u09cc -> ৌ : \uab -> ꯧ
}

MM_NUCLEUS_END = {
    "\u0987": "\uabcf",  # \u0987 -> ই : \uabcf -> ꯢ
    "\u09be": "\uabe5",  # \u09be -> া : \uabe5 -> ꯥ
    "\u09bf": "\uabe4",  # \u09bf -> ি : \uabe4 -> ꯤ
    "\u09c0": "\uabe4",  # \u09c0 -> ী : \uabe4 -> ꯤ
    "\u09c1": "\uabe8",  # \u09c1 -> ু : \uabe8 -> ꯨ
    "\u09c2": "\uabe8",  # \u09c2 -> ূ : \uabe8 -> ꯨ
    "\u09c7": "\uabe6",  # \u09c7 -> ে : \uabe6 -> ꯦ
    "\u09c8": "\uabe9",  # \u09c8 -> ৈ : \uabe9 -> ꯩ
    "\u09cb": "\uabe3",  # \u09cb -> ো : \uabe3 -> ꯣ
    "\u09cc": "\uabe7",  # \u09cc -> ৌ : \uab -> ꯧ
}


def get_post_map() -> Dict[str, str]:
    # \uabea -> ꯪ : \uabe1 -> ꯡ (only when prefix is cheitap)
    return {
        f"{cheitap[-1]}\uabea": f"{cheitap[-1]}\uabe1" for cheitap in MM_NUCLEUS_MID
    }
