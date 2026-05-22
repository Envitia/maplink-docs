---
title: "Unicode"
---

# Unicode

MapLink Pro supports Unicode on all supported platforms. This means that you can display multiple languages on a map or layer using MapLink Pro. The data is stored within MapLink as UTF-8.

## Unicode SDK Support

### C++ SDKs

The MapLink API uses 'char \*' pointers to pass string information to and from an application. MapLink expects data passed to the C++ API to be UTF-8 or 7-bit ASCII (subset of UTF-8). Data passed back to the application will be UTF-8.

Two helper classes have been provided to help convert text data to and from UTF-8:

- TSLUTF8Decoder

- TSLUTF8Encoder

In most cases an application may not need to adjust what is passed into MapLink unless the application is being upgraded to Unicode or the user did not use 7-bit ASCII.

For users migrating from a version of MapLink prior to 8.0 please see the section [4.5](#backwards-compatibility) for backwards compatibility and workarounds.

### .NET SDKs

The .NET SDKs use the Windows concept of Unicode at the MapLink API.

The class TSLNCoordinateConverter takes System::Char for some of the conversion methods. The data passed in and out in these cases is assumed to be 7-bit ASCII.

## Unicode Geometry

The following Geometry Text primitives are currently supported by MapLink:

- TSLText / TSLNText

- TSLGeodeticText / TSLNGeodeticText

- TSL3DText / TSLN3DText

TSL3DText/TSLN3DText only supports a subset of 7-bit ASCII.

TSLText and TSLGeodeticText will display text in multiple languages. The text may contain more than one language and the languages displayed may be left to right and right to left.

## Fonts

The font you use is key to the display of text. If the font does not support the language/script then you need to find an alternative font that does. This may happen because not all fonts contain all the necessary glyph entries to display Unicode strings correctly. You can add new fonts to tslfonts.dat file.

### Freely Available Fonts

The "[Google Noto Font](http://www.google.com/get/noto/#/)s" use the Apache Licence 2.0. This set of fonts aims to support all the world's languages.

The MapLink configuration file 'tslfonts.dat' contains references to other freely useable fonts and some which are commercial (commercial/'non-free' fonts are commented out).

### Vertical Text Layouts

Unicode vertical text layouts are not currently supported. Any vertical text will be drawn horizontally.

### Right to Left Scripts

We support right to left scripts. The alignment of the string is not swapped as it can be in some text editors, therefore the positioning of a left or right aligned text string will be the same for both left to right and right to left strings. You can mix different scripts within a single text item.

### Vector Font

The vector font support is limited to 7-bit ASCII on both the GDI and X11 Drawing Surfaces. Vector font drawing is not supported by the 2D OpenGL Drawing Surfaces.

All MapLink drawing surfaces support drawing rotated system text. This negates the need for the Vector font as this was primarily used for drawing rotated text on platforms that could not support drawing of rotated system fonts.

## Filenames and Paths

- All filenames and paths must be encoded as UTF-8.

- MapLink expects the filenames and paths on Windows to be 'long' paths. Passing a 'short' or '8.3' filename may not work correctly. These can be on a local drive 'C:\\file.txt' or on a network share '\\\\server\\file.txt'.

- MapLink may also accept 'UNC' paths. These can be on a local drive '\\\\?\\C:\\file.txt' or on a network share '\\\\?\\UNC\\server\\file.txt'.

- Unless an application is using 'UNC' paths elsewhere it is recommended that 'long' filenames be used. Applications do not need to covert paths to 'UNC' format for paths longer than \~260 characters.

- Many sections of the MapLink API support additional formats such as folders, URLs, or datatype-specific identifiers.

- Paths relative to a drive-specific working directory are unsupported, e.g d:file.txt (file.txt relative to the current working directory on drive D).

- MapLink will attempt to convert a path without a drive letter using the current working directory, paths such as '/a/b/c/d.e' will work whereas a path such as 'c/d.e' will be treated as relative to the current working directory.

### Path length limitations

On Windows the maximum path length for 'long' file names is \~260 characters. For 'UNC' paths it is 32,767 characters.

The maximum length supported by MapLink is 4096 characters. This applies to both 'long' paths and 'UNC' paths.

## Backwards compatibility

The MapLink Pro backward compatibility (versions prior to MapLink 8.0) has been partially broken with the introduction of Unicode support in the way 8-bit characters are handled.

Prior to support of Unicode users may have relied upon 8-bit character strings being passed through the MapLink Pro API without change. Now this is only true for 7-bit ASCII and 8-bit UTF-8 encoded strings.

You will not be affected by these changes if:

- You only used 7-bit ASCII strings.

- You used the .NET SDKs.

- You use a non-Windows platform (these are usually UTF-8 by default).

In order to support Unicode with MapLink Pro we have had to break the following at the API:

- Filename and path names have to be long filename/paths on Windows

- Text has to be UTF-8. We no longer support Text being passed to MapLink as defined by the System Code page.

- All text is assumed to be UTF-8.

To minimise the impact of this change we will read and convert all text from files generated by MapLink versions prior to 8.0 on load to UTF-8 where possible. The default conversion assumes the files contain text in the System Code Page on Windows, and CP-1252 on other platforms.

### Workarounds

### Text

Text is now expected to be 7-bit ASCII or UTF-8.

When MapLink Pro reads files generated by versions prior to 8.0 we process the string as follows:

Read text

If the text is **not** UTF-8

Convert to UTF-8 using the System Code Page

In most cases this should be completely transparent to the application. If you experience problems with text not being correctly converted, you can override the Code Page used for the application using the following unsupported methods:

- void TSLifstream::legacySetEncodingOverride(TSLTextEncoding encoding);

- TSLTextEncoding TSLifstream::legacyGetEncodingOverride();

- void TSLofstream::legacySetEncodingOverride(TSLTextEncoding encoding);

- TSLTextEncoding TSLofstream::legacyGetEncodingOverride();

Setting a Code Page encoding to use will affect **all** text reading or writing.

**Note**:

Because we convert from UTF-8 to Multi-Byte for saving older version of the MapLink file formats some languages may not convert well. The more complex the script, such as Arabic, the less likely this will work.

If you use this approach, all data stored in the MapLink control files must be 7-bit ASCII or in the Code Page that has been set. You cannot mix text in multiple Code Pages.

### Text File Formats

The MapLink configuration files and control files are principally text based. If you have modified the MapLink configuration files from a version of MapLink prior to 8.0 and you wish to use these with MapLink 8.0 or later you may experience problems.

In the case of configuration files you should open the file in an editor such as [Notepad++](http://notepad-plus-plus.org/) and convert the file to UTF-8 without BOM (Byte Order Mark) and save the file. The version at the top of the file should be updated to the latest version number for that file format.

You should not update layer or MapLink Studio configuration files are these contain multiple objects with each possibly at a different version.

## Unicode FAQ

**Why have you chosen to use UTF-8 as the Unicode representation for MapLink Pro?**

- UTF-8 is cross platform.

- UTF-8 is compatible with 7-bit ASCII.

- The string terminator is still '\\0'.

  This means that significantly less needs to be changed internally to support Unicode text within both MapLink and end user applications across all the platforms supported.

**Why did you not use wchar_t?**

- wchar_t can be any size from 1 byte to 4 bytes depending on the platform being used. The internal encoding of wchar_t is also platform dependent.

- wchar_t is not compatible with 7-bit ASCII.

- The string terminator might not be '\\0'.

- From The Unicode Standard, chapter 5:

  - The width of wchar_t is compiler-specific and can be as small as 8 bits. Consequently, programs that need to be portable across any C or C++ compiler should not use wchar_t for storing Unicode text.

**Why did you not use UCS2?**

- UCS2 is only the default encoding for Unicode text on Windows.

- UCS2 is not backwards compatible with 7-bit ASCII.

**Where can I find out more about UTF-8?**

<http://www.utf8everywhere.org/>






