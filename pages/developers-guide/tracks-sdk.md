---
title: "Tracks SDK"
---

# Tracks SDK

The [TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html) provides an easy way to create and display dynamic objects representing real-world entities that frequently change position. Tracks can be styled using application-defined symbols, or the APP6A and 2525B military symbology standards.

Each real-world entity is represented in the application by an instance of the Track class, which contains information about the entity such as its position, speed and velocity. Each track uses one or more symbol derived classes to define the appearance of the track at various zoom levels, as well as the appearance of the track's selection indicator (to visually identify when a track will be used for application-defined operations) and the appearance of the track's history trail.

Tracks are associated with a drawing surface using the [TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html) class. The [TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html) acts as a container for a group of tracks within the application, and provides methods for efficiently updating common properties on large numbers of tracks at once. It also provides the capability to record and replay the status of tracks over time, allowing the viewing of the history of the tracks in the [TrackDisplayManager](mk:@MSITStore:C:\Maplink_Installations\Maplink_10_2\MapLink%20Documentation\Developer\MapLinkAPI.chm::/class_t_s_l_track_display_manager.html).

## Library Usage and Configuration

**As of version 11.1, MapLink is no longer supplied with Debug or 32-bit libraries**. Therefore, your application's build should link against the Release Mode libraries in all configurations.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **MapLinkTrackManager64.lib**                                                                                                                                                                  |
|                                                                                                                                                                                                |
| Release mode, DLL version.                                                                                                                                                                     |
|                                                                                                                                                                                                |
| Uses Multithreaded DLL C++ run-time library.                                                                                                                                                   |
|                                                                                                                                                                                                |
| Must also link the MapLink CoreSDK library MapLink.lib/MapLink64.lib                                                                                                                           |
|                                                                                                                                                                                                |
| Requires TTLDLL preprocessor directive.                                                                                                                                                        |
|                                                                                                                                                                                                |
| Refer to the document "MapLink Pro X.Y: Deployment of End User Applications" for a list of run-time dependencies when redistributing. Where X.Y is the version of MapLink you are deploying. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Track Display Manager Basics

See the API documentation for further details.

