---
title: "Samples"
---

# Samples

MapLink Pro includes numerous samples to help you with starting development with an SDK.

Samples are provided for .NET and C++.

While many of the samples are platform specific MapLink Pro itself can be used on both Windows and X11 platforms (Linux and Solaris. Other platforms can be ported to so please contact your Sales representative to discuss).

The samples for all platforms can be used to help inform you as to how to use the SDKs on all platforms.

There are several classes that you need to swap out between platforms that relate to Drawing technology (Drawing Surfaces).

If an SDK is not supported on your platform, please contact your Sales representative to discuss.

## Qt Samples

This section assumes that the reader is familiarly with developing with Qt.

The Qt samples do not have pre-configured Visual Studio or makefiles. Instead we ship QMake project '.pro' ([See QMake Project](http://doc.qt.nokia.com/latest/qmake-project-files.html)) files from which you need to generate the necessary build files.

The following is a summary of the necessary steps to build the samples on Windows.

- Install Qt or build Qt yourself.

  - You should match the Qt version with the version of Visual Studio you are using.

  - The samples are configured to build in the MapLink Pro installation. If they are moved the pro/pri files will need to be updated.

- Open the 'Qt' Command prompt.

  - Change directory to the sample.

- set QMAKESPEC=win-64msvc2022

  - qmake -t vcapp

- Load the generated.vcxproj into Visual Studio.

- Depending on the version of the Visual Studio you are using you may be prompted to upgrade the project. Accept this upgrade.

- Set the Path to the Qt and MapLink libraries if necessary. By default, the samples are set to be built from the directory they are installed to.

- Build the solution.

- Run the example.

  On X11 systems QMake will generate makefiles suitable for use with GNU Make. The MapLink installation will be located using the MAPL_HOME environmental variable, which can be set automatically using the mapl_init or mapl_init_bash scripts.

  Additional Notes:

- If using QtCreator load the .pro file as a project into QtCreator.

- If you move the samples you need to modify the .pro file before you create the project to point to the MapLink headers and lib files.

