# Release Notes - MapLink Pro - Version 11.2.2

* toc
{:toc}

# Related Pages

- **[Previous Release](../11.2.1/release-notes)**

- [Upgrade Notes](../../support/install-and-upgrade)
- [Supported Platforms](../../support/platform-support)
- [Supported SDKs](../../support/sdk-support.md)


# Improvements
    * 654   [TS023856] BUG: MapLink memory consumption when loading SLD
    * 3072  [TS023893] BUG: Linux redist library conflict on Rocky 9.2
    * 3730  [TS023900] BUG: Cannot load rasters into TSLRasterFilterDataLayer
    * 3890 BUG: LibTiff requires JPEG support
    * 4075 Misc fixes and changes for Delphi and COM application upgrade work
        * Avoid STATUS_FLOAT_DIVIDE_BY_ZERO crash in ttltxf64.dll when loading MapLink from Delphi and COM
        * Tweak Doxygen for various API classes (Core, Editor, GMLInterop)
    * 4384  BUG: Drawing surface goes crazy when moving from monitor to laptop screen
    * 4391  BUG: 11.2.1 installer tries to patch 11.1 installation
