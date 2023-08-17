from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20


def loadfont(fontpath, private=True, enumerable=False):
    """
    Makes fonts located in file `fontpath` available to the font system.

    `private`     if True, other processes cannot see this font, and this
                  font will be unloaded when the process dies
    `enumerable`  if True, this font will appear when enumerating fonts

    See https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx
    """
    if isinstance(fontpath, str):
        pathbuf = create_string_buffer(fontpath.encode("utf-8"))
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError("fontpath must be of type str")

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)
