# Map Build SDK

The Map Build SDK provides a cross-platform solution for building MapLink maps and terrain databases from existing projects and source datasets. We provide the following ways to add map generation to your workflows:
- The C++ `envitia::MapLinkProject` API for direct integration into your solution.
- The **MapCompiler64** for generating a map from an existing MapLink Studio project.
- The **MapFactory64** for scripting based generation of maps.

Generated maps can then be loaded into any MapLink based application as with maps generated from MapLink Studio.


## Using the C++ API

To get started include `<tslmapbuildproject.h>` in your project.  Then include the appropriate library for your platform:


| Platform | Map Build link library | Runtime library |
| --- | --- | --- |
| Windows x64 | `MapLinkMapBuild64.lib` | `MapLinkMapBuild64.dll` |
| Linux | `libMapLinkMapBuild64.so` | Matching shared library and dependencies |


At runtime, supply the corresponding DLLs or `.so` files, dataset-filter libraries, licence, and MapLink configuration. 

On all platforms ensure that MAPL_HOME is set to your MapLink installation location.

On Linux ensure that LD_LIBRARY_PATH includes `<maplinkHome>/lib64` otherwise the Map Build SDK will fail to find installed filters.

### Create and compile a map

This example adds a shapefile to an existing MapLink project then generates an output map.  It takes an installed MapLink home directory, an existing shape input file, a project destination ending in `.mlp`, and an output destination ending in `.map` as input parameters. 

Note : `CreateMap` requires an **absolute** output path (and accepts `.map` or `.mpc`).

```cpp
#include <tslmapbuildproject.h>

#include <exception>
#include <filesystem>
#include <iostream>
#include <string>

int main(int argc, char* argv[])
{
	if (argc != 5) {
		std::cerr << "Usage: example <maplink-home> <input.shp> <project.mlp> <output.map>\n";
		return 1;
	}

	try {
		envitia::MapLinkProject project{std::filesystem::path{argv[1]}, {}};
		if (!project.create()) return 1;

		auto* section = project.createFeatureBookSection("SHP");
		auto* layer = project.newLayer("Layer1");
		auto* filter = envitia::loadFilter("SHP"); // Loads SHP.
		if (!section || !layer || !filter) return 1;

		const std::string datasetName = "SHP";
		auto* dataset = project.createDataset(layer, filter, section, &datasetName);
		if (!dataset || !project.addData(dataset, std::filesystem::absolute(argv[2]))) return 1;

		if (!project.save(std::filesystem::absolute(argv[3]))) return 1;
		if (!project.SelectAllLayersForMap()) return 1;
		if (!project.CreateMap(std::filesystem::absolute(argv[4]))) return 1;
	} catch (const std::exception& error) {
		std::cerr << error.what() << '\n';
		return 1;
	}
	return 0;
}
```

The `SHP` filter must be installed and able to read the input. `loadFilter` manages its returned filter pointer; do not delete it. To compile an existing project instead, call `project.load(projectPath)`, optionally `project.SelectLayersForMap({"Layer1"})`, and then `project.CreateMap(outputPath)`. For suitable terrain projects, use `project.CreateTerrainDatabase(outputPath)` to generate a `.tdf`.

## MapCompiler64: compile an existing project

```text
MapCompiler64 [-c maplink-home] [-u user-config-file] project.mlp output.map
MapCompiler64 [-c maplink-home] [-u user-config-file] project.mlp output.tdf
```

`project.mlp` must already exist: this tool does not create projects or add data. 

`.map` builds a map using the current MapLink version; `.tdf` builds a terrain database. 

The output suffix check is case-sensitive. 

`-c` selects the MapLink home/config directory (otherwise the MAPL_HOME location is used), 

`-u` is a user configuration **file** path (otherwise the installation default is used). 

`-h` displays help. Use an absolute map output path. 

For example: `MapCompiler64 -c /opt/maplink /data/atlas.mlp /data/atlas.map`.


## MapFactory64: run commands from a file

```text
MapFactory64 [-c maplink-home] [-u user-config-file] FactoryCommands.mbc
```

Options are the same as MapCompiler64. MapFactory parses the **entire** file before executing any commands, then runs commands in order and stops on a failure. 

The first line identifies the format, for example `TSLMAPLBATCHCOMMANDS 101` (`100` is also accepted). 

Start with `OPEN` on an existing `.mlp` before modifying or compiling it.  This `.mlp` can be entirely empty.  It is possible to use the template project shipped with MapLink.

Each subsequent line has one **uppercase, case-sensitive** command; use `;` between the command and its arguments. 

Leading indentation is allowed, but spaces within arguments are significant. 

`#` begins a comment anywhere on a line; quoting or escaping `;` and `#` is not supported. 

Empty arguments (including trailing semicolons) are rejected. 

Prefer absolute paths: relative paths use the process working directory, not necessarily the command file's directory.

Example `FactoryCommands.mbc`:

```text
TSLMAPLBATCHCOMMANDS 101
# Compile all layers from an existing project.
OPEN;/data/atlas.mlp
CREATEOUTPUTMAP;ALL;/data/atlas.map
QUIT
```

### Supported command lines

In the table, `<value>` is a required argument and `[;<value>...]` means an optional semicolon-separated list. Do not include the angle/square brackets in the file. Names must match the existing project exactly. Dataset selectors use `LayerName/DatasetName` with **one forward slash**, including on Windows.

| Syntax | Meaning |
| --- | --- |
| `OPEN;<project.mlp>` | Load an existing MapLink project. |
| `RECATALOGUE` | Recatalogue the loaded project's files; no arguments. |
| `ADDDATATOALLDATASETS;<datafile>` | Offer the file to every dataset; fails if none accepts it. |
| `ADDDATA;<datafile>;<Layer/Dataset>` | Offer the file to a specific dataset; fails if it doesn't accept it. |
| `SETMAPOUTPUTCOORDINATESYSTEM;<name>` | Set the map output coordinate system by its configured name. |
| `SETLAYEROUTPUTCLIPPING;<minX>;<maxX>;<minY>;<maxY>[;<layer>...]` | Set output-space bounds for the specified layers, or for all layers if none are listed. |
| `SETLAYERGEODETICCLIPPING;<minLatitude>;<maxLatitude>;<minLongitude>;<maxLongitude>[;<layer>...]` | Set geodetic bounds for selected or all layers. Latitude must lie within `[-90, 90]`. **Latitude arguments come first**, unlike X/Y clipping. |
| `SETDATASETINPUTCLIPPING;<minX>;<maxX>;<minY>;<maxY>[;<Layer/Dataset>...]` | Set input-space bounds for the specified datasets, or for all datasets if none are listed. |
| `CREATEOUTPUTMAP;ALL;<output.map>` | Select every layer and build an output map at an absolute `.map` path. |
| `CREATEOUTPUTMAP;SELECTED;<output.map>;<layer>[;<layer>...]` | Select at least one named layer and build an output map at an absolute `.map` path. |
| `QUIT` | Terminate command execution successfully; no arguments. |

The four clipping values are numeric and describe closed intervals: each minimum must be **no greater than** its maximum (equal endpoints are allowed). 

Use the coordinate system and units appropriate to the project. A missing layer or dataset selector causes that command to fail. 

For example, after `OPEN`: `SETLAYERGEODETICCLIPPING;-45;45;-90;90;Layer1`, `SETDATASETINPUTCLIPPING;0;100;0;100;Layer1/ASCII`, then `CREATEOUTPUTMAP;SELECTED;/data/clipped.map;Layer1`.


## Known Limitations

Map Compiler - The current `.tdf` path can return exit code 0 in a non-assert build even if terrain creation returned false. Check diagnostics and the output file rather than relying only on the exit code.

Map Factory - `LOGFILE` and `CREATEOUTPUTMAP;MERGE;...` are **rejected** by the current parser. MapFactory has no terrain-database command at this time; use MapCompiler64 or `MapLinkProject::CreateTerrainDatabase` for `.tdf` output.

Map Factory - The path to datafiles in the `.mlp` must be lowercase if run on Linux.

Map Factory - The output directory must exist on Linux.
