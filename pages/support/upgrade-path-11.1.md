# Upgrading to MapLink 11.1

* toc
{:toc}

> **MapLink Pro 11: The next major release of MapLink Pro is coming soon. When this happens, MapLink Pro 8.x will enter support and maintenance end-of-life. If this affects your contracts, [please contact us to discuss how to bring your systems up-to-date](https://forms.office.com/e/6ydUswfjEe).**

If you have an active MapLink Pro support and maintenance contract with Envitia, you can upgrade to MapLink Pro 11.1 when it becomes available ([see the Support page for more details of the release date](index.md)).

There are structural differences between 11.1 and previous versions of MapLink Pro. This page explains how to upgrade your application to MapLink Pro 11.1.

# Can I Install MapLink Pro 11.1 Alongside Earlier Versions?
Yes, MapLink Pro 11.1 can be installed alongside earlier versions of MapLink Pro (back to 4.0 SP3).

All installations of MapLink Pro since MapLink Pro 4.0 SP3 can happily co-exist on the same
machine without interfering with one another. It is quite common for developers to retain
installations of older versions of MapLink Pro to allow them to support their legacy applications
built against them.

# Windows
## Installation
Envitia MapLink Pro is typically installed on a Windows machine using an installation executable supplied by Envitia.

## Windows Environment Variables
When MapLink Pro is installed on a Windows machine, an environment variable named *MAPL_PATH* is added to the system and it contains
the location of the bin directory of the installation. The *MAPL_PATH* environment variable is
then referenced from the *PATH* environment variable.
Whichever version of MapLink Pro has been installed most recently will therefore be referenced by the *MAPL_PATH* environment variable.
This means that when attempting to run an
application that requires the MapLink Pro runtime libraries from an older version of MapLink
Pro, it will load the latest version instead.
To ensure that your application runtime loads the desired MapLink Pro library versions:
- Update the value of the *MAPL_PATH* environment variable to point to the desired MapLink Pro version's bin directory.
> NOTE: Changing the environment variable will only affect applications that are started
after the change has been made, not ones that were opened before. If the application is
a system service, such as Microsoft's Internet Information Services (IIS), a reboot may
be required.
- Or, set the application's working directory to the desired MapLink Pro version's bin directory.

# Linux
## Linux Environment Variables
When MapLink Pro is installed on a Linux machine, 