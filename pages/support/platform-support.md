---
title: MapLink Pro Platform and Operating System Support
---

# Operating Systems


For the time being, MapLink Pro releases are targeting Windows and Linux operating systems. The next MapLink for Android release will follow, but users can continue to use MapLink 10.2 on Android.

The following table lists the operating systems that the MapLink release has been tested on. 

## Supported Operating Systems

| Supported OS | OS Versions | Tested MapLink Version |
| ----- | ----- | ----- |
| Windows | 11, 10 | 11.3 |
| Linux: Rocky | 8 | 11.3 |
| Linux: RHEL | 8 | 11.3 |
| Android | - | 10.2 |

## Compilers

MapLink Pro is built with these components:

| MapLink version | OS | Compiler | Version |
| ----- | ----- | ----- | ----- |
| 11.3 | Linux | GCC | 11.4 |
| | Windows | MSVC | v145 (VS2026) |
| | |  | .NET 10 |
| 11.1, 11.2 | Linux | GCC | 11.4 |
| | Windows | MSVC | v143 (VS2022) |
| | |  | .NET Framework 4.8 |

## C++ Version
The MapLink Pro C++ API is C++ 03 compliant to ensure maximum compatibility.
On Windows and Linux, the minimum required version is C++17 to ensure compatibility with latest third party dependencies. 
