# Break-Build Algorithm

## 1. Overview

This is the overview

## 2. Breaking

This is breaking

## 3. Transliteration Unit (TU)

A TU has C\*VC\* structure.

A Syllable TU contains a tuple of three substrings; the onset, the nucleus and the coda. Nucleus is a vowel or a group of vowel, while the onset and coda are consonant or consonant clusters and they are optional.

In implementation, TU can be of two types:

1. Whitespace:
   - Blank Space: type <- ws, str <- ' '
   - New line Character: type <- ws, str <- '\n'
2. Syllable:
   - type <- sy, str <- (onset,nucleus,coda)
   - sy can be v, vc, cv, cvc depending on the nature of syllable (c is actually c+ in re)

Initializing a syllable TU:

1. A TU read a string
2. If string is whitespace (blank space or new line character) content <- character, type <- ws
3. Find the vowels in the string. There should only be one contiguous sequence of vowel. Throw error otherwise.
4. Assign vowels as nucleus, every consonants before the nucleus as onset, every consonants after the nucleus as coda if it exists.
5. Make a three tuple containing the onset, nucleus and coda. If onset and/or coda doesn't exist, put an empty string. str <- (onset, nucleus, coda)
6. Check the str of 3-tuple.
   6.1. if both onset and coda is empty, type <- v
   6.2. else if only onset is missing, type <- cv
   6.3. else if only coda is missing, type <- vc
   6.4. else, type <- cvc

## 3. Building

Transliteration Unit (TU) -> Meitei Mayek Characters

1. A TU is read
2. If type of TU is a whitespace, write the syllable.str
3. Else, extract the syllable.syllable into a 3-tuple:
   - transform the first element into mapum mayek and insert apun if there are multiple character
   - transform the second element into its corresponding vowel
   - transform the first element into lonsum mayek and insert apun if there are multiple character
4. If lonsum mayek isunavailable, mapum mayek is inserted instead

These process is repeated for each TU till the utterance is completely transformed into a single meetei/mayek string.
