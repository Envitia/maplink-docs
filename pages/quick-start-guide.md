---
title: MapLink Pro Quick Start Guide
---

# MapLink Pro Quick Start Guide

> **MapLink Pro 11 is now available.** This guide covers initial installation and setup for MapLink Pro. For the latest release notes, see the [Releases page](/pages/releases/).

MapLink Pro is a powerful geospatial SDK for building high-performance mapping applications. This guide walks you through installation, licensing, and your first steps with the SDK across Windows, Linux, and Android platforms.

---

## Release Limitations

Please refer to the Release Notes for your platform before using MapLink Pro.

### Windows 8.0/8.1 Installation

Installing on Windows 8.0 will result in a minimal set of shortcuts on the Start Screen. Windows 8.1 does not permit installing shortcuts directly to the Start Screen — they are placed on the full Apps Screen instead. Pin any favourite shortcuts to the Start Screen manually.

---

## Windows Installation

If installing MapLink Pro from a CD, insert the disc and run one of the MSI installers. Once MapLink is installed, also install any available patches.

Several installers are available:

| Installer | Description |
|---|---|
| `MapLinkPro_<version>_x64.exe` | 64-bit MapLink Pro development. Includes MapLink Studio and OGC Services. |
| `MapLinkStudio_<version>_x64.exe` | 64-bit MapLink Pro Studio only. |
| `MapLinkOGCServices_<version>_x64.msi` | MapLink OGC Services only. |

Once the installer starts, follow the on-screen instructions. Additional installation notes:

- If you installed an **Evaluation** version, you must uninstall it before installing the full version.
- You cannot install the full version of MapLink Pro and the MapLink Studio standalone installer on the same machine — the full MapLink Pro package already includes Studio.

### MapLink Pro Installation Process

The MapLink Pro installer is a WiX bundle that also installs prerequisites (such as Visual Studio redistributables).

1. Run the installer — a Windows UAC prompt will appear. Click **Yes** to allow it.
2. On the Welcome Screen, click **Next** and review the licence agreement. You must accept it to proceed.
3. Choose an installation directory.
   > **Note:** The directory path must contain only printable ASCII characters.
4. Optionally choose to install Sample and Documentation shortcuts. Launcher programs are used by default to reduce clutter on the Windows Start Screen.
5. Click **Install**. Accept any UAC prompt that appears.
6. Click **Finish** when complete.
7. The **Licence Key Administrator** starts automatically after installation — you will need to answer a UAC prompt for it as well.
8. Remember to close the base installer after the Licence Key Administrator opens.

### MapLink Studio Installation Process

The MapLink Studio installer follows the same sequence as the MapLink Pro installer:

1. Click **Next**, review and accept the licence agreement.
2. Choose an installation directory. (If installing on Wine, refer to the Wine-specific guidance in the full documentation.)
3. Choose whether to install Sample and Documentation shortcuts, then click **Next**.
4. Click **Install** and accept any UAC prompt.
5. Click **Finish** when complete. The **Licence Key Administrator** launches automatically.

#### Licensing

Once you have licensed MapLink Studio, do not change the Windows version — doing so will invalidate the licence.

#### Fonts

MapLink Studio and its tools use a number of fonts. You may need to install additional fonts or modify the `tslfonts.dat` file to match fonts available on your system. The `tslfonts.dat` file includes hints on where to obtain TrueType fonts and is located in the MapLink Studio installation `config` directory.

### MapLink OGC Services Installation Process

The OGC Services installer is a minimal installation containing only the MapLink Gateway, WMS/WPS Servers, and server plugins. It is only available as 64-bit, though the same components are also included in the full MapLink Pro installation.

Key differences from the full installer:

- Only a minimal set of runtime libraries is installed — enough to support the provided WMS and WPS plugins. Custom plugin development requires the full MapLink Pro installation.
- Only a minimal set of Start Menu shortcuts is created.
- OGC Services **may** be installed alongside a MapLink Pro or MapLink Studio installation, but **must not** be installed to the same directory. The installer will warn if another MapLink installation is detected.

To use the included web services, MapLink OGC Services must be deployed in either **Microsoft IIS** or **Apache Tomcat**. Deployment procedures are described in the [MapLink OGC Services Deployment User Guide](/pages/MapLink%20OGC%20Services%20Deployment%20User%20Guide).

---

## Linux Installation

The Linux installation is provided as one of the following formats:

- Compressed tar archive
- DVD/CD
- ISO image

In all cases, copy the distribution contents to a disk location and read the **Release Notes** section "For X11 Developers".

> You will need a Windows installation of MapLink Studio to create maps for use with the Linux runtime.

### Documentation and Samples

- Documentation is contained in the `docs` directory.
- Sample applications are in the `samples` directory.

### Linux Evaluation

The MapLink Pro Linux evaluation is node-locked and requires a working `eth0` interface (it does not need internet access).

To request a 30-day evaluation key, send the output of the following command (as a plain text file) to Envitia:

```bash
/sbin/ifconfig -a
```

Contact Envitia for licensing queries:
- **Phone:** +44 1403 273 173
- **Email:** licensing@envitia.com

---

## Android Installation

Please read the `Readme.html` included in the Android distribution for installation instructions. A version of MapLink Studio is required to create maps for use in Android applications.

### Android Licensing

The MapLink Pro CoreSDK and each additional SDK/runtime component are protected by a licence key and must be unlocked before use. Licence keys are obtained directly from Envitia support and are handled separately from the Windows licensing system.

Licence keys may be:
- **Full** — unrestricted use
- **Evaluation** — time-limited; displays a watermark in the application

Contact Envitia for Android licensing:
- **Phone:** +44 1403 273 173
- **Email:** licensing@envitia.com

---

## Uninstalling MapLink Pro

### Windows

Use the **Programs and Features** entry in Control Panel to uninstall. Do not use any other method.

> The installer intentionally leaves licence files in place after uninstall. Do not delete them — they are required by other Envitia products and must be present in their expected location.

### Linux and Android

The Linux and Android installations can be removed by deleting the installation directory.

---

## Licence Key Administration

Windows installations of MapLink Pro must be licensed using the **Licence Key Administrator** before they can be used.

Open the Licence Key Administrator from the Start Menu under **Envitia MapLink Pro**. A UAC prompt may appear — click **Yes** to allow it.

The Licence Key Administrator window lists all MapLink Pro products. Before requesting a licence, fill in your account information via **Account → Information** (or the **Edit Account Details** toolbar button). Fields marked in red are mandatory.

### Request a Licence

1. Select the checkboxes for the products you wish to licence. Note that some products depend on others (e.g. SDKs require the Developer's Toolkit, which requires Studio).
   > When requesting a **permanent** licence, only select products you have purchased. Selecting others may delay processing and will not result in licences for those additional products.
2. Select **Licence → Request Licence Key(s)** from the menu, or click **Licence Key Request** in the toolbar.
3. Set the **Licence Key Type** to Evaluation or Permanent. For permanent licences, enter the Order Number.
4. Choose how to submit the request:
   - **Email** — automatically sends via your default email client.
   - **Fax** — prints the request ready for faxing.
   - **Phone** — opens a Notepad window with the request text for telephone submission. You can also manually email it to licensing@envitia.com.

After submitting, the selected checkboxes become unselectable and their **Expiration** status changes to **Key Pending**.

Contact details: **Phone:** +44 1403 273 173 &nbsp;|&nbsp; **Email:** licensing@envitia.com

### Install a Licence

When you receive your licence key, select **Licence → Import Licence Key(s)** (or **Import Licence Key** in the toolbar).

- **Email delivery:** Save the attached `.lkf` licence key file to your computer, then click **Open Licence File** and browse to it.
- **Fax or phone delivery:** Click **Enter key supplied by Envitia** and type the key manually.

The Licence Key Administrator will confirm the registered products and show an expiration date (Permanent or 30 days from installation). MapLink Pro is now ready to use.

### Moving a Licence

To install MapLink Pro on a different machine, you must first **de-authorise** the current machine (or purchase an additional developer licence). Once de-authorised, a licence for the new machine can be granted.

Refer to the **Envitia Licence Key Administrator Help** for detailed de-authorisation steps.

---

## Developing an Application

The primary references for MapLink Pro development are:

- [**MapLink Pro Developer's Guide**](/pages/developers-guide) — covers MapLink API concepts and usage.
- **API Reference** — detailed documentation for all API classes (available as a CHM for C++ and .NET in your installation).

These can be accessed via the **MapLink Pro Documentation Launcher** in the Start Menu.

Sample source code is located in `<INSTALL_DIR>\samples\`:

| Folder | Description |
|---|---|
| `NT` | Windows samples using MFC |
| `QT` | Windows & X11 samples using Qt |
| `X11` | X11 samples |
| `Wizards` | Visual Studio wizards for creating basic MapLink applications |

### Training, Consultancy and Sub-Contracting

Envitia offers training courses to help you get the most from MapLink Pro and MapLink Studio. Dedicated on-site or remote consultancy is also available.

Envitia can also develop the MapLink Pro component of your application or undertake more extensive project work on your behalf.

To discuss these options, contact Sales:
- **Email:** sales@envitia.com
- **Phone:** +44 1403 273173

### Documentation

On Windows, the full documentation set is accessible via the **MapLink Pro Documentation** launcher in the Start Menu. Select a document entry to expand it, then press **Launch** to open it (a PDF viewer is required for most documents).

Available documentation includes:

- API Reference Help (C++ and .NET)
- MapLink Studio Help & User Guide
- MapLink Pro Developer's Guide
- MapLink Pro Deployment of End User Applications
- MapLink Pro Installation and Upgrade Notes
- MapLink Pro Windows Release Notes and 3rd Party Licences
- MapLink OGC Services Deployment User Guide
- MapLink WMS CADRG plug-in User's Guide
- S63 Reference Workflow Sample
- MapLink S63 & S52 SDK Developer's Guide
- Print Template Studio Help
- Symbol Studio Help
- Image Studio Help
- Licence Administrator Help

#### MapLink Developer's Guide

The Developer's Guide covers MapLink Pro components, concepts, and the steps required to build an application. Section 5 leads you through writing and building your first MapLink application.

After building the application, you can test it with sample data: run the application and select **File → Open**. Sample maps are under `<INSTALL_DIR>\samples\MapForSamples` — `VMapUK\VMAP0.map` is a good starting point.

#### API Reference

The API Reference is a Windows CHM document covering all MapLink APIs. There are two CHM files — one for C++ and one for .NET.

> Not all SDKs are available on all platforms. Contact Sales if you have a requirement for a specific SDK on a specific platform.

The API Reference can be browsed by:
- Class diagrams
- Documentation tree
- Keyword search

---

## Release Notes

The Release Notes contain important information on:

- Platform information
- Enhancements
- Bug fixes
- Limitations
- Previous release notes

See the [Releases page](/pages/releases/) for the latest version information.

### Deployment of End User Applications

This document contains information about how to deploy a MapLink application and includes copyright statements.

### Installation and Upgrade Notes

This document contains information about installing and [upgrading from a previous MapLink release](/pages/support/install-and-upgrade).

### Tools

MapLink Pro includes the following tools, available as 32-bit or 64-bit. They can be launched via the **MapLink Pro Tools** launcher in the Start Menu.

| Tool | Description |
|---|---|
| **MapLink Studio** | Creates high-performance maps and terrain databases. |
| **Map Viewer** | Views and checks created maps. |
| **Terrain Viewer** | Views and checks terrain databases. |
| **Rendition Editor** | Edits feature rendering of a map and adjusts layer viewpoints. |
| **Symbol Studio** | Creates new vector symbols for applications and maps. |
| **Image Studio** | Gelocates and warps images. |
| **Licence Key Administrator** | Manages MapLink Pro licences. |
| **Print Template Studio** | Creates print templates for maps (using TSLNTSurface). |

### Sample Programs

Numerous samples demonstrate the functionality of each SDK in MapLink Pro. Source code is included for all examples.

Windows samples are generally applicable to X11 targets — the MapLink API is designed to minimise platform differences to a small number of classes.

Samples can be found in `<INSTALL_DIR>\samples\` or launched from the **MapLink Pro Samples** launcher in the Start Menu. Each sample entry expands to show a description, a **Launch** button, and a **Code** button to open the source directory.

---

## Processing a Map

If you have your own map data, you must process it before using it in an application. Processing optimises data for display. Sample source data is provided under `<INSTALL_DIR>\data`.

MapLink Pro can process data via **MapLink Studio**, or via the **Direct Import** mechanism at runtime. MapLink Pro can also handle data processed by other Envitia products — contact sales@envitia.com for details.

### MapLink Studio

MapLink Studio provides a powerful and flexible environment for fusing a wide range of vector and raster map data, with transformation and reprojection into a single integrated map.

Key capabilities include:

- Fusing vector and raster maps, imagery, and terrain from disparate sources and coordinate systems.
- Previewing input data to assess quality and coverage.
- Defining the default colour and style of vector maps.
- Segmenting and filtering data for maximum performance.
- Preparing complex, multi-layer maps and terrain sets in fixed or dynamic coordinate systems.
- Creating templates for runtime map preparation environments.

More information — including exercises using sample data — is in the MapLink Studio User Guide. Sample projects can be found in `<INSTALL_DIR>\Projects`.

### MapLink Studio SDK

An optional Software Development Toolkit provides access to MapLink Studio capabilities via a COM automation interface. This allows MapLink Pro customers to embed map data processing capabilities within their own applications.

---

## Direct Import

As well as pre-processed data, MapLink Pro can import many data formats directly at runtime, providing a flexible ingestion method for applications where pre-processing is not appropriate.

The controlling application determines how maps are displayed, including vector data rendering.

Specialised import mechanisms exist for specific formats:

| Mechanism | Description |
|---|---|
| `TSLKMLDataLayer` | Displays KML/KMZ on 2D drawing surfaces. |
| `TSLS63DataLayer` | Handles S-63 or S-57 data (including updates). |
| `TSLCADRGDataLayer` | Fast runtime rendering of CADRG/CIB data. |
| `TSLFilterDataLayer` | Loads, reprojects, and draws GeoTIFF, NITF/NSIF, and raster data. |
| `TSLUtilityFunctions::importData/appendData` | Vector import for S-57, Shapefile, MIF/MID, KML, OS MasterMap, OS Vector Map Local. |
| `TSLRasterDataLayer` / `TSLRasterFilterDataLayer` | General raster data loading and display. |
| `TSLDatabaseLayer` | Vector data from an Oracle database. |
| `TSLCustomDataLayer` | Custom geospatial data layers implemented in the application. |
| `TSLWMSDataLayer` | Data from an OGC WMS Server. |
| `TSLWMTSDataLayer` | Data from an OGC WMTS Server. |
| DMED data | Via the Terrain SDK. |

> Some Direct Import mechanisms require runtime licence keys. Contact your Envitia sales representative for details.

---

## WMS and WFS

Web services are a popular way to deliver map data to applications. MapLink Pro is certified with the OGC WMS (Web Map Service) standard and also supports WFS (Web Feature Service) client functionality.

With both services, servers may be located on the internet or on a local area network. MapLink Pro's OGC server option can serve MapLink maps, CADRG, historical, or user-specific data to any OGC client.

MapLink Pro includes a client-side SDK for ingesting and displaying data from WMS and WFS servers, including combining served data with locally held sources.
