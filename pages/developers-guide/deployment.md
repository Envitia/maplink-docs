---
title: "Deployment of End User Application"
---

# Deployment of End User Application


Please refer to the \"MapLink Pro X.Y: Deployment of End User
Applications\" for detailed information for deploying an application,
including copyrights, deployment restrictions and required DLLs.

The following sections are an overview of the necessary code changes for
deployment.

## Configuration Files

MapLink Pro loads all of its necessary configuration files from the
'\<MapLink Installation\>\\config' directory, usually through a call to
TSLDrawingSurface::loadStandardConfig. When deploying an application
based upon MapLink, a copy of this folder must be shipped along with the
application.

The MapLink Pro installer adds a reference to the system registry to
allow the MapLink libraries to locate the config directory at runtime.
Envitia do not recommend however, that this registry key or any MapLink
environment variables are used when deploying applications based upon
MapLink.

Therefore as the MapLink libraries will not know the new location of
this directory on the deployment machine's file system, calls to various
MapLink methods will need to be changed to be passed the location of the
config directory. The following table lists the current method calls
which will need to be updated, depending upon the technology being used:

**Note**: If an application to be deployed does not use a method
mentioned, then that method may be ignored.

## C++

  -----------------------------------------------------------------------
  **Method**
  -----------------------------------------------------------------------
  TSLDrawingSurface::loadStandardConfig

  TSLDrawingSurface::setupColours - Pass the location of the
  tslcolours.dat file that the config directory contains.

  TSLDrawingSurface::setupFillStyles - Pass the location of the
  tslfillstyles.dat file that the config directory contains.

  TSLDrawingSurface::setupFonts - Pass the location of the tslfonts.dat
  file that the config directory contains.

  TSLDrawingSurface::setupLineStyles - Pass the location of the
  tsllinestyles.dat file that the config directory contains.

  TSLDrawingSurface::setupSymbols - Pass the location of the
  tslsymbols.dat file that the config directory contains.

  TSLCoordinateSystem::loadCoordinateSystems - Pass the location of the
  tsltransforms.dat file that the config directory contains.

  TSLAPP6AHelper::TSLAPP6AHelper

  TSLAPP6AHelper::setDefaultConfigPath

  TSL3DDrawingSurface::loadStandardConfig

  TSL3DDrawingSurface::setupModels - Pass the location of the
  tslmodels.dat file that the config directory contains.

  TSLUtilityFunctions::setMapLinkHome - set the directory that contains
  the MapLink config **directory.**
  -----------------------------------------------------------------------

## .NET

  -----------------------------------------------------------------------
  Method
  -----------------------------------------------------------------------
  TSLNDrawingSurface::loadStandardConfig

  TSLNDrawingSurface::setupColours - Pass the location of the
  tslcolours.dat file that the config directory contains.

  TSLNDrawingSurface::setupFillStyles - Pass the location of the
  tslfillstyles.dat file that the config directory contains.

  TSLNDrawingSurface::setupFonts - Pass the location of the tslfonts.dat
  file that the config directory contains.

  TSLNDrawingSurface::setupLineStyles - Pass the location of the
  tsllinestyles.dat file that the config directory contains.

  TSLNDrawingSurface::setupSymbols - Pass the location of the
  tslsymbols.dat file that the config directory contains.

  TSLNCoordinateSystem::loadCoordinateSystems - Pass the location of the
  tsltransforms.dat file that the config directory contains.

  TSLNAPP6AHelper::TSLAPP6AHelper

  TSLNAPP6AHelper::setDefaultConfigPath

  TSLN3DDrawingSurface::loadStandardConfig

  TSLN3DDrawingSurface::setupModels - Pass the location of the
  tslmodels.dat file that the config directory contains.

  TSLNUtilityFunctions::setMapLinkHome - set the directory that contains
  the MapLink config **directory.**
  -----------------------------------------------------------------------



---

[← MapLink and your Development Environment](development-environment) | [Samples →](samples)
