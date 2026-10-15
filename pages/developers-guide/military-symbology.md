---
title: "Military Symbology"
---

# Military symbology

The Military Symbology API provides generation of high-quality MIL-STD-2525D and APP-6D symbols.
It is available as a C++ API and a C# API.
It is part of the MapLink Core SDK and is included in `Maplink64.lib`.
The symbols are generated from SVG files to create high quality raster sprites.

## Using the C++ API

```
#include <tslmilitarysymbologygenerator.h>

...

    TSLMilitarySymbologyGenerator symbolGenerator;

    symbolGenerator.loadSymbols("path/to/config/symbols/MILSTD_2525D");

    auto sidc = TSLSidc2525d{ "10031000001211000000" };
    TSLSymbol* symbol = symbolGenerator.getSymbol(sidc, TSLSidc2525d::SymbolSet::Unknown);
    if (symbol)
    {
        symbol->move(TSLCoord{x, y}, {0,0});
        standard_data_layer->entitySet()->insert(symbol);
        standard_data_layer->notifyChanged(true);
    }
```

`loadSymbols()` needs a path to a directory containing the following directories, each containing SVGs.
This will be shipped with the MapLink installation, but alternate sets can be used, providing they conform to the naming scheme.
After `loadSymbols()` returns, the MS API has cached the location of all SVGs, but not loaded them.

`getSymbol()` takes an optional parameter for display options.

- `.scale` How large should the symbols be rendered?
  _Warning: be careful of scales less than 0.3, the resolution may be insufficient to communicate all symbol details!_
- `.civilianFill` Some entities and modifiers mark a symbol as civilian, for these symbols this controls the fill colour.
- `.ocaStyle` There are different styles of Operational Condition Amplifiers, this controls which is used.

When calling `getSymbol()` the component SVGs will be loaded if they have not already and a symbol rendered.
The caller is responsible for cleaning up the returned TSLSymbol object.
Subsequent calls to `getSymbol()` with the same arguments will not re-render the symbol, but will provide new map objects that use the raster.

## Known Limitations

1. APP-6D support currently only includes icons which are part of MIL-STD 2525D.
