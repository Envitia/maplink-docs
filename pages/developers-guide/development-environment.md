---
title: "MapLink and your Development Environment"
---

# MapLink and your Development Environment


## Library Usage and Configuration

The MapLink C++ SDK's on Windows platforms are supplied in 2 different
flavours. These are release and debug versions as dynamically linked
libraries. The table below describes the pre-processor directives and
link options that should be set in the Project Properties for using the
MapLink Core SDK. For X11 targets, refer to the product Release Notes.

Note that these settings apply when using Visual Studio 2015 SP3 only.
If using a different version of Visual Studio, please see section
[5.2](#using-other-versions-of-visual-studio-with-maplink).

+--------------------------------+--------------------------------+
| **MapLink64.dll**              | **MapLink64d.dll**             |
|                                |                                |
| Release mode, DLL version.     | Debug mode, DLL version.       |
|                                |                                |
| Uses Multithreaded DLL C++     | Uses Debug Multithreaded DLL   |
| run-time library.              | C++ run-time library.          |
|                                |                                |
| Requires TTLDLL preprocessor   | Requires TTLDLL preprocessor   |
| directive.                     | directive.                     |
|                                |                                |
| Refer to the document "MapLink | No redistributable run-time    |
| Pro X.Y: Deployment of End     | available.                     |
| User Applications\" for a list |                                |
| of run-time dependencies when  | **KEYED: Development machines  |
| redistributing. Where X.Y is   | only**.                        |
| the version of MapLink you are |                                |
| deploying.                     |                                |
+--------------------------------+--------------------------------+

You must ensure that your own code settings match, especially in the use
of the C++ run-time library and only link debug applications with debug
versions of the libraries. This is necessary since amongst other things,
the Microsoft memory management library is quite different in debug and
release mode. For more information about this, see the MSDN articles
Q166504 and Q94248.

If you are using multiple MapLink SDKs, they must all be the same
configuration as regards debug/release on Windows platforms.

### Windows DLL/LIB Naming Convention

Having both release and debug DLLs and Libraries means that a naming
convention is required to allow both to coexist.

As such the following convention has been adopted (where \'**D**\'
indicates debug). The '**64**' indicates that the library is 64-bit,
which used to be a necessary distinction before we removed support for
32-bit.

  ----------------------------------------------------------------------------
  Build            DLL Name             Lib Name             Directory
  Configuration                                              
  ---------------- -------------------- -------------------- -----------------
  64-bit Release   DLLName**64**.DLL    DLLName**64**.LIB    bin64, lib64

  64-bit Debug     DLLName**64D**.DLL   DLLName**64D**.LIB   bin64, lib64
  ----------------------------------------------------------------------------

### Visual Studio Warnings and Errors

The debug memory manager of Visual Studio attempts to report any memory
that it considers have leaked. Unfortunately, it does this after
destruction of any statically linked global objects but before
destruction of any dynamically linked global objects. This means that in
the Debug DLL version of the MapLink library, Visual Studio will
erroneously report a few memory leaks. This should be ignored since they
are not true leaks and merely memory that is still in use prior to the
static objects being destroyed.

Unfortunately, since the MapLink libraries are not supplied with debug
information, more complex memory managers such as Purify also
erroneously report memory leaks and free memory mismatches.

A final point to note is that the Keying functionality sometimes reports
"First Chance Exceptions" generated upon application start-up. These are
handled internally within MapLink and may be safely ignored.

## Using other versions of Visual Studio with MapLink 

All libraries in this release of MapLink have been compiled and built
using Microsoft Visual Studio 2015 Update 3 (Please see the Release
Notes for the version used when building MapLink Pro).

It is possible however, for applications built using other releases of
Visual Studio to use this release of MapLink. There are a few
limitations and rules that must be followed to avoid problems with the
C++ run-time library.

Firstly, it is only possible to use the DLL versions of the MapLink
libraries.

Secondly, Envitia are not allowed to redistribute the Microsoft C++
run-time debug libraries. This means that unless these already exist on
your machine, the MapLink debug libraries will have unresolved symbols
and cannot be used. You can do one of two things:

- Obtain the appropriate Visual Studio debug run-time libraries and
  install them on your system. If you have installed this release of
  Visual Studio then they may already exist.

- Do not use the debug version of MapLink libraries, but build your
  release mode application with optimisations disabled and debug
  generation turned on. This should be done both in the C++ compiler
  options and the linker options. In Microsoft parlance this is termed
  'pseudo-debug' and is used for example, when debugging Visual Studio
  extensions.

Most sample applications have both Visual Studio 2010 files, and Visual
Studio 2015 files. These are configured appropriately so can be used as
reference for the settings.

If you have any other issues, or questions regarding Visual Studio
support, then please contact the Envitia support desk at
<support@envitia.com> .

If you are using .NET languages other than C++, then you can use the
.NET interop manager to import the MapLink .NET libraries and use them
instead.

### Visual Studio Pseudo Debug

Setting up Visual Studio for pseudo-debug requires the project to be
modified in two places. The Visual Studio 2010 solutions have been
changed to this configuration.

The first modification is to use the Release Runtime Library:

![Figure 1 Release Runtime Library
Setting](/assets/images/developers-guide/media/image4.png)

The second modification is to use the Release versions of the MapLink
DLLs:

![Figure 2 Additional
Dependencies](/assets/images/developers-guide/media/image5.png)

The \"\_DEBUG\" preprocessor definition should be replaced with the
\"NDEBUG\" one.



---

[← Unicode](/pages/developers-guide/unicode) | [Deployment of End User Application →](/pages/developers-guide/deployment)
