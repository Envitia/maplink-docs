---
title: "Tracks SDK"
---

# Tracks SDK


The
[TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html)
provides an easy way to create and display dynamic objects representing
real-world entities that frequently change position. Tracks can be
styled using application-defined symbols, or the APP6A and 2525B
military symbology standards.

Each real-world entity is represented in the application by an instance
of the Track class, which contains information about the entity such as
its position, speed and velocity. Each track uses one or more symbol
derived classes to define the appearance of the track at various zoom
levels, as well as the appearance of the track\'s selection indicator
(to visually identify when a track will be used for application-defined
operations) and the appearance of the track\'s history trail.

Tracks are associated with a drawing surface using the
[TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html)
class. The
[TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html)
acts as a container for a group of tracks within the application, and
provides methods for efficiently updating common properties on large
numbers of tracks at once. It also provides the capability to record and
replay the status of tracks over time, allowing the viewing of the
history of the tracks in the
[TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html).

## Library Usage and Configuration

As with the MapLink Core SDK, the Tracks SDK comes in 2 different
configurations. It should be noted that the library to be linked with
should be determined by the Core SDK library that you are using within
your application. For example, if you are using the Release mode, DLL
version of the Core SDK (MapLink.lib) then you must use the equivalent
Tracks SDK library (MapLinkTrackManager.lib or
MapLinkTrackManager64.lib).

+---------------------------------+------------------------------------+
| **MapLinkTrackManager.lib or    | **MapLinkTrackManager d.lib or     |
| MapLinkTrackManager 64.lib**    | MapLinkTrackManager 64d.lib**      |
|                                 |                                    |
| Release mode, DLL version.      | Debug mode, DLL version.           |
|                                 |                                    |
| Uses Multithreaded DLL C++      | Uses Debug Multithreaded DLL C++   |
| run-time library.               | run-time library.                  |
|                                 |                                    |
| Must also link the MapLink      | Must also link the MapLink CoreSDK |
| CoreSDK library                 | library                            |
| MapLink.lib/MapLink64.lib       | MapLinkd.lib/MapLink64d.lib        |
|                                 |                                    |
| Requires TTLDLL preprocessor    | Requires TTLDLL preprocessor       |
| directive.                      | directive.                         |
|                                 |                                    |
| Refer to the document \"MapLink | No redistributable run-time        |
| Pro X.Y: Deployment of End User | available.                         |
| Applications\" for a list of    |                                    |
| run-time dependencies when      | **KEYED : Development machines     |
| redistributing. Where X.Y is    | only.**                            |
| the version of MapLink you are  |                                    |
| deploying.                      |                                    |
+---------------------------------+------------------------------------+

## Track Display Manager Basics

See the API documentation for further details.



---

[← Direct Import SDK](direct-import-sdk) | [Dynamic Overlays with the DDO SDK →](ddo-sdk)
