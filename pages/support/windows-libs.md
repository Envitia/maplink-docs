# MapLink Pro Windows Libraries

This page describes which MapLink Pro libraries should be shipped when deploying an application based upon MapLink Pro.

All MapLink Pro libraries that are to be deployed with an application should be copied from the **/redist64** directory of the MapLink Pro installation.
The tables below list the files you may need to include in your application to support the MapLink Pro functions. Some of the libraries listed are required for all applications, whilst others are only required if certain functionality or SDKs are used. If a library is not listed, then it is likely that it may not be redistributable. If you are unsure as to whether a library may be redistributed, then please contact Envitia Support. 

If any issues are found when running a deployed application on Windows, [Dependency Walker](https://www.dependencywalker.com/) can be used to determine any missing DLLs or version mismatches. It can also be used to determine the libraries loaded in your development environment, and therefore inform what libraries should be deployed.

> You may not copy or redistribute any file supplied with MapLink Pro without first having obtained the proper licence.

# Core MapLink Pro Windows Libraries

These libraries are required by every application developed with MapLink Pro.

- MAPLINK64.DLL
- TTLTGM64.DLL
- TTLTMS64.DLL
- TTLCH64.DLL
- TTLTXF64.DLL
- TTLMT64.DLL
- TTLCOMPRESSION64.DLL
- TTLCLSWF64.DLL
- TTLCLSSTRK64.DLL
- TTLTRASHLT64.DLL

Redistributed third-party libraries:
- boost*
- lt*.dll



