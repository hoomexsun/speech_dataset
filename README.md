# Manipuri Speech Dataset Tools 🚧

This repository contains a collection of tools used to create a Manipuri dataset in both Bengali and Meetei/Meitei Mayek scripts.

What's new?

- Modularised the Correction and Transliteration mechanism to work on improvement.

## 1. Overview

The project consists of several modules:

| Title               | Description                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Preprocessing**   | Formats news text into raw data suitable for further processing. [+Tokenization]                                                |
| **Segmentation**    | Generates utterance files with utterance segments and IDs from script text files for s550 glyphs.                               |
| **Correction**      | Converts s-550 glyphs into correct Bengali Unicode characters.                                                                  |
| **Transliteration** | Transliterates Bengali Unicode to Meetei Mayek Unicode using a rule-based method, supporting transliteration through a wordmap. |
| **Postprocessing**  | Formats utterance text file into complete words. [+Normalization]                                                               |
| **GUI Mode**        | Provides a GUI interface to test functions using input strings.                                                                 |
| **Script Mode**     | Offers CLI-based access to essential features.                                                                                  |
| **Dataset**         | The main class containing the project pipeline.                                                                                 |
| **Utils & Config**  | A group of lower level utility functions.                                                                                       |
| **Describe**        | Describe the dataset including speaker infos.                                                                                   |

## 2. GUI Mode

Use the provided GUI through `gui.py` or `main.py -g`.

- The GUI is styled with the [SunValley Theme](https://github.com/rdbende/Sun-Valley-ttk-theme).

### 2.1 **Test Mode**

- **Test Mode** allows testing main features using input strings

  ![GUI Test Mode](./images/test_mode.png)

### 2.2 **Search Mode**

- **Search Mode** helps find words containing a specific character. Available for S-550, Bengali and Meetei Mayek.
- **Search Mode:** S-550 Unicode

  ![GUI Search Mode](./images/search_s550.png)

- **Search Mode:** S-550 Glyph

  ![GUI Analyze Mode](./images/search_s550_glyph.png)

### 2.3 **Analyze Mode**

- **Analyze Mode** helps find different combinations in words containing a specific character, sorted according to count. Available for S-550, Bengali and Meetei Mayek.
- **Analyze Mode:** S-550
  ![GUI Analyze Mode](./images/analyze_s550.png)

- **Analyze Mode:** Bengali
  ![GUI Analyze Mode](./images/analyze_bn.png)

- **Analyze Mode:** Meetei Mayek
  ![GUI Analyze Mode](./images/analyze_mm.png)

### 2.4 **Glyph**

- The `Glyph` function is a powerful tool designed specifically for Windows users in both `Search Mode` and `Analyze Mode`. It plays a crucial role in displaying English Unicode characters used as building blocks for Bengali glyphs, making it an indispensable feature for various users, including AIR, Sangai Express, as well as various news agencies and press clubs.

### **Last Update Changes:**

1. **Completed Pagination of Search/Analyze Results**

   - We have successfully implemented pagination for both Search and Analyze results, making it easier to navigate through large datasets.

2. **Additional Tabs for Analysis**

   - We have added additional tabs to enhance the analysis experience, providing users with more options and functionalities.

3. **Fixed Unsynchronized States of UI with Data**

   - We addressed issues related to UI and data synchronization, ensuring that the user interface accurately reflects the underlying data.

4. **Fixed Glyphs Not Working When Page is Navigated**

   - We resolved an issue where glyphs were not rendering correctly when navigating between pages, ensuring a seamless user experience.

5. **Fixed Reactivity Issue with Button Commands**

   - We have fixed reactivity issues related to button commands, making sure that all actions trigger the expected responses.

6. **Increased Reusability and Renamed Existing Methods**

   - To enhance code maintainability, we've added more methods and improved the naming conventions of existing methods.

7. **Improved Decoupling**

   - We've improved the decoupling of components within the codebase, promoting modularity and ease of development.

8. **Reduced Use of tkinter Trace to Resolve Memory Leaks**

   - To address memory leak concerns, we've reduced the usage of tkinter trace, ensuring more efficient resource management.

9. **Fixed Appearance of Previous Page Content in Results**

   - We've corrected a bug where previous page content was erroneously displayed in search and analyze results.

10. **Fixed UI of Analyze Displayed with Data from Search and Vice Versa:**

    - We've resolved an issue where the user interface was displaying data from the wrong mode (Search or Analyze).

11. **Disabled Pagination Button at Start and End of Pages**

    - Pagination buttons are now disabled at the start and end of pages when there is no more content to display.

12. **Disabled Manual Input for Analyze Mode**

    - In Analyze mode, manual input has been disabled to prevent user errors and ensure data integrity.

13. **Changed Toggle to Display When a Custom Font is Used to Render `Glyphs`**

    - A toggle has been introduced to indicate when a custom font is being used to render glyphs, providing users with transparency regarding font settings.

14. **Replaced Search Button with Go Button**

    - The `search` button has been replaced with a `Go` button, which provides a more intuitive action for initiating searches.

15. **Added Mode Button to Toggle Between Analyze and Search**

    - A `Mode` button has been added to allow users to easily switch between Analyze and Search modes, enhancing user flexibility.

16. **Disabled Go Button When Input is Empty**

    - The `Go` button is now disabled when there is no input, preventing unnecessary actions and improving user experience.

17. **Reflect Changes When Mode is Toggled Between Search and Analyze**

    - Changes to the user interface and functionality are now immediately reflected when toggling between `Search` and `Analyze` modes.

18. **Removed words.txt and chars.txt from gitignore**

    - To expedite testing, we've removed `words.txt` and `chars.txt` from gitignore, allowing for immediate testing of `Search` and `Analyze` functionality.

19. **Automatically Created Resources at Start of GUI**

    - Resources are now automatically generated at the start of the GUI, eliminating the need to run the `main.py` script before `gui.py`, streamlining the development process.

20. **Other UI Changes**

For any additional information or inquiries, please refer to the accompanying code documentation or open an issue.

## 4. Script Mode

You can use the script mode for different functions.

### 4.1. Main Scripts

These are the primary scripts that can be executed:

- `main.py`: Run the main script.
- `gui.py`: Run the GUI (Graphical User Interface) script.
- `describe.py`: Run the Describe script to analyze the dataset.

### 4.2. Main Script with Options

You can use the `main.py` script with additional options:

- `main.py -g`: Run the main script with GUI mode enabled.
- `main.py -d`: Run the main script with describe mode enabled.

## 5. Known Issues

The project has identified issues that need resolution:

- Preprocessing cannot ignore `UnicodeDecodeError` characters in RTF files encoded in `cp1252`.
- Correction may have issues with characters with virama.
- Transliteration algorithm might skip last two characters.
- Transliteration might fail to identify coda as lonsum for non-virama clusters.

## 6. New Approach

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

- [Speech Dataset](https://github.com/hoomexsun/speech_dataset).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [IPA Keyboard for Windows](https://github.com/hoomexsun/ipa_keyboard).
- [S-550 Glyph Correction](https://github.com/hoomexsun/s550_glyph_correction).
- [Epaomayek Glyph Correction](https://github.com/hoomexsun/epaomayek_glyph_correction).
- [SunValley Theme](https://github.com/rdbende/Sun-Valley-ttk-theme).
- [Loading Custom Fonts in Tkinter for Windows](<https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx>).
