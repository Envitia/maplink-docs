---
title: "MapLink and your Development Environment"
---

# MapLink and your Development Environment

## Library Usage and Configuration

**As of version 11.1, MapLink is no longer supplied with Debug or 32-bit libraries.** Therefore, your application's build should link against the Release Mode libraries in all configurations.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **MapLink64.dll**                                                                                                                                                                             |
|                                                                                                                                                                                               |
| Release mode, DLL version.                                                                                                                                                                    |
|                                                                                                                                                                                               |
| Uses Multithreaded DLL C++ run-time library.                                                                                                                                                  |
|                                                                                                                                                                                               |
| Requires TTLDLL preprocessor directive.                                                                                                                                                       |
|                                                                                                                                                                                               |
| Refer to the document "MapLink Pro X.Y: Deployment of End User Applications" for a list of run-time dependencies when redistributing. Where X.Y is the version of MapLink you are deploying. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

