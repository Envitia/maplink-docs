# Installing MapLink

* toc
{:toc}

> **MapLink Pro 11: The next major release of MapLink Pro is coming soon. When this happens, MapLink Pro 8.x will enter support and maintenance end-of-life. If this affects your contracts, [please contact us to discuss how to bring your systems up-to-date](https://forms.office.com/e/6ydUswfjEe).**

If you have an active MapLink Pro support and maintenance contract with Envitia, you can upgrade to MapLink Pro 11.1 when it becomes available ([see the Support page for more details of the release date](index.md)).

There are structural differences between 11.1 and previous versions of MapLink Pro. This page explains how to upgrade your application to MapLink Pro 11.1.

# Windows Development Machine
## Installation
Envitia MapLink Pro is typically installed on a Windows development machine using an installation executable supplied by Envitia.

## Windows Environment Variables
When MapLink Pro is installed on a Windows machine, an environment variable named *MAPL_PATH* is added to the system and it contains
the location of the bin directory of the installation. The *MAPL_PATH* environment variable is
then referenced from the *PATH* environment variable.

> All installations of MapLink Pro on Windows since MapLink Pro 4.0 SP3 can happily co-exist on the same
machine without interfering with one another. It is quite common for developers to retain
installations of older versions of MapLink Pro to allow them to support their legacy applications
built against them. However, the most recently installed version will be referenced by the *MAPL_PATH* environment variable.

To ensure that your application runtime loads the desired MapLink Pro library versions:
- Update the value of the *MAPL_PATH* environment variable to point to the desired MapLink Pro version's *bin* directory.
> NOTE: Changing the environment variable will only affect applications that are started
after the change has been made, not ones that were opened before. If the application is
a system service, such as Microsoft's Internet Information Services (IIS), a reboot may
be required.
- Or, set the application's working directory to the desired MapLink Pro version's bin directory.

## Windows Licensing
Certain MapLink Pro components installed on Windows require a licence to be installed on the machine before they will work.
[Please contact us for a trial licence](https://forms.office.com/e/Lr7jN9TCC0) if you do not yet have a licence.

## Upgrading to MapLink 11.1 on Windows

- MapLink Pro's build dependencies, [including the compilers and frameworks used to build the product](./platform-support.md#maplink-111-compilers), have been updated to ensure security and reliability and to facilitate future development. You will need to update your environment and application accordingly.
- You may encounter some build errors in your C++ application code if you are using features that have been deprecated or removed from the C++ 17 standard. These tend to be concerned with C++ features that have been removed from the C++ standard, and tend to require fairly straight-forward code replacements.
- MapLink Pro no longer includes "Debug for Release" (*xxx64**D**.xxx*) libraries. If your Debug configurations use these libraries, please change them to use the MapLink Pro Release libraries (*xxx64.xxx*). The Release libraries have been updated to include Frame Pointers so there should be no regression of the debugging experience.
- MapLink Pro no longer includes 32-bit libraries. You will need to update your environment and application to a 64-bit architecture.
- [Several older and rarely used SDKs have been archived](./sdk-support.md) and these are no longer available in the product. If you are using any of these libraries, please contact Envitia to discuss workarounds or other options.

[Create a technical support ticket](https://support.envitia.com) if you run into any issues.


# Linux Development Machine

## Installation
Envitia MapLink Pro is typically installed on a Linux development machine using a compressed tarball file supplied by Envitia.

## Linux Environment Variables
A script named *mapl_init* (csh shell) and *mapl_init_bash* (bash shell) is included to initialise
your environment, prior to building the samples. MapLink expects *LD_LIBRARY_PATH* and
*MAPL_HOME* environment variables to be correctly setup when MapLink applications are run. The
samples expect *MAPL_LIB_DIR* to be correctly set in order to build them.

> All installations of MapLink Pro on Linux can happily co-exist on the same
machine without interfering with one another. It is quite common for developers to retain
installations of older versions of MapLink Pro to allow them to support their legacy applications
built against them. However, the most recently installed version will be referenced by the *LD_LIBRARY_PATH* environment variable.

To ensure that your application runtime loads the desired MapLink Pro library versions, update the value of the *LD_LIBRARY_PATH* environment variable to point to the desired MapLink Pro version's *lib64* directory.

## Upgrading to MapLink 11.1 on Linux

- MapLink Pro's build dependencies, [including the compilers and frameworks used to build the product](./platform-support.md#maplink-111-compilers), have been updated to ensure security and reliability and to facilitate future development. You will need to update your environment and application accordingly.
- MapLink Pro no longer includes 32-bit libraries. You will need to update your environment and application to a 64-bit architecture.
- [Several older and rarely used SDKs have been archived](./sdk-support.md) and these are no longer available in the product. If you are using any of these libraries, please contact Envitia to discuss workarounds or other options.

## Linux Licensing
Although the UNIX/Linux/VxWorks runtime libraries are not locked, a valid licence is required to legally use them.

Some SDKs are shipped in encrypted packages in the folder *OptionalComponents*. This folder contains a README.txt file which explains how to decrypt and extract the SDKs.

# Deploying an Application with MapLink Pro
[MapLink 11.0 Deployment of End User Applications.pdf]({{ "/pdf/MapLink 11.0 Deployment of End User Applications.pdf" | relative_url }})