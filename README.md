# Manipuri Speech Dataset Tools

This repository contains a collection of tools used to create a Manipuri dataset in both Bengali and Meetei/Meitei Mayek scripts.

## 1. Overview

The project consists of several modules:

| Title               | Description                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Preprocessing**   | Formats news text into raw data suitable for further processing.                                                                |
| **Utterance**       | Generates utterance files with utterances and IDs from script text files for s550 glyphs. Also includes utility functions.      |
| **Correction**      | Converts s-550 glyphs into correct Bengali Unicode characters.                                                                  |
| **Transliteration** | Transliterates Bengali Unicode to Meetei Mayek Unicode using a rule-based method, supporting transliteration through a wordmap. |
| **GUI Mode**        | Provides a GUI interface to test functions using input strings.                                                                 |
| **Script Mode**     | Offers CLI-based access to essential features.                                                                                  |
| **Dataset**         | The main class containing the project pipeline.                                                                                 |
| **Utils & Project** | A base class with utility functions and a framework for main classes.                                                           |
| **Describe**        | Describe the dataset including speaker and utterance infos.                                                                     |

## 2. Use Cases

Import the necessary classes (always import Utils). Here's an example of reading a text file:

- _Using Utils as a utility class (since most methods are static):_

```python
from utils.utils import Utils
...
content = Utils.read_text_file(file_path)
```

- _Inheriting from Utils:_

```python
from utils.utils import Utils
class MyClass(Utils):
    ...
    def some_method():
        content = self.read_text_file(file_path)
        ...
```

### 2.1. Preprocessing

Create a `Preprocessing` object and call the `preprocess_file()` method to format the news text from all files stored inside a specific directory into raw text files which can be used as input in further implementations.

- _Initialization_

```python
from steps.preprocessing import Preprocessing
p = Preprocessing()
```

- _Multiple Files in a directory_

```python
for file_path in files:
    content = p.preprocess_file(file_path)
```

### 2.2. Utterance

Create a `Utterance` object and call the `utterance()` method to generate utterances from all files stored inside a specific directory.

- _Initialization_

```python
from steps.utterance import Utterance
u = Utterance()
```

- _All text files in a directory_

```python
files = Utils.get_files(SCP_S550_DIR)
for file_path in enumerate(files):
    content = u.utterance(file_path)
```

### 2.3. Correction

Create a `Correction()` object and call the `correct()`, `correct_script()` or `correct_utterances()` method to generate the correct Bengali unicode from the s-550 glyphs.

- _Initialization_

```python
from correction import Correction
c = Correction()
```

- _String_

```python
output_text = c.correct('text in s550')
```

- _Script file_

```python
content = c.correct_script("path/to/file")
```

- _Utterance file_

```python
content = c.correct_utterances("path/to/file")
```

- _All script files inside a directory_

```python
files = Utils.get_files("path/to/directory")
for file_path in files:
    content = c.correct_script(file_path)
```

- _All utterance files inside a directory_

```python
files = Utils.get_files("path/to/directory")
for file_path in files:
    content = c.correct_utterances(file_path)
```

### 2.4. Transliteration

Create a `Transliteration()` object and call the `transliterate()`, `transliterate_script()` or `transliterate_utterances()` method to generate the correct Meetei Mayek unicode from the Bengali unicode.

- _Initialization_

```python
from transliteration import Transliteration
t = Transliteration()
```

- _String_

```python
output_text = t.transliterate('some text in bengali')
```

- _Script file_

```python
content = t.transliterate_script("path/to/file")
```

- _Utterance file_

```python
content = t.transliterate_utterances("path/to/file")
```

- _All script files inside a directory_

```python
files = Utils.get_files("path/to/directory")
for file_path in files:
    content = t.transliterate_script(file_path)
```

- _All utterance files inside a directory_

```python
files = Utils.get_files("path/to/directory")
for file_path in files:
    content = t.transliterate_utterances(file_path)
```

## 3. GUI Mode

Use the provided GUI through `gui.py` or `main.py -g` [Underway].

- The GUI is styled with the [SunValley Theme](https://github.com/rdbende/Sun-Valley-ttk-theme).

- **Test Mode** allows testing main features using input strings.

![GUI Test Mode](./images/test_snap.png)

- **Analyze Mode** helps find words containing a specific character.

![GUI Analyze Mode](./images/analyze_snap.png)

- `Toggle` function in `Analyze mode` is currently available for only Windows at the moment.

## 4. Script Mode

You can use the script mode for different functions:

```bash
correction.py string
correction.py -f path/to/file
correction.py -d path/to/dir
transliteration.py string
transliteration.py -f path/to/file
transliteration.py -d path/to/dir
transliteration.py string -w path/to/wordmap
transliteration.py -f path/to/file -w path/to/wordmap
transliteration.py -d path/to/dir -w path/to/wordmap
```

## 5. Directory Structure

The project's directory structure is organized as follows:

- `config`, `data`, `local`, `res`, `steps`, `theory`, `output`, and `utils` folders containing various modules.
- Different subfolders within `data`, `res`, and `utils` for better organization.
- Configuration files, text files, scripts, and resource files are appropriately placed.

## 6. Known Issues

The project has identified issues that need resolution:

- Preprocessing cannot ignore `UnicodeDecodeError` characters in RTF files encoded in `cp1252`.
- Correction may have issues with characters with virama.
- Transliteration algorithm might skip last two characters.
- Transliteration might fail to identify coda as lonsum for non-virama clusters.

## 7. New Approach

A new approach aims to process words instead of entire files:

1. Divide meaningful sentences during preprocessing.
2. Perform correction and transliteration at the word level.
3. Target invisible characters for correction.

Extra:

- ¡ is used to transform d to u i.e., l is d -> l¡ü is u, And ü is dependent suffix.
- for spelling of words like security
  - vowel is repeated (u and uu) change it to u
  - position in s550 is at the left but on bn it is at the right (which is correct).

## See also

- [SunValley Theme](https://github.com/rdbende/Sun-Valley-ttk-theme).
- [Loading Custom Fonts in TKinter for Windows](<https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx>).
