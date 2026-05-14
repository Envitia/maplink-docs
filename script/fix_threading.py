"""Fix prose-in-fence inversions in threading.md"""

with open(r'c:\maplink\maplink-docs\pages\developers-guide\threading.md', 'rb') as f:
    content = f.read()

fixes = []

# Fix T1: Prose text (method list) wrongly inside ```cpp fence at top of file
fixes.append(('T1 threading options prose in fence',
    b'```cpp\r\n'
    b'If you are using MapLink for drawing in multiple threads, then you may need to use the following methods:\r\n\r\n'
    b'- TSLUtilityFunctions::getThreadedOptions\r\n\r\n'
    b'- TSLUtilityFunctions::setThreadedOptions\r\n'
    b'```\r\n'
    b'The following classes have been updated',
    b'If you are using MapLink for drawing in multiple threads, then you may need to use the following methods:\r\n\r\n'
    b'- TSLUtilityFunctions::getThreadedOptions\r\n\r\n'
    b'- TSLUtilityFunctions::setThreadedOptions\r\n\r\n'
    b'The following classes have been updated'
))

# Fix T2: Prose text about StandardDataLayer thread safety wrongly inside ```cpp fence
fixes.append(('T2 DrawingSurface rendering prose in fence',
    b'```cpp\r\n'
    b'While in general the drawing is thread safe you should avoid sharing layers between threads (see [28.8](#data-layers-1)).\r\n\r\n'
    b'If you wish to share the TSLStandardDataLayer (see [28.9](#standard-data-layer-1)) between threads then you need to call TSLUtilityFunctions::setThreadedOptions to set the bit represented by TSLThreadedOptionsRenderingSupport.\r\n'
    b'```\r\n'
    b'## Coordinate System Resource Loading',
    b'While in general the drawing is thread safe you should avoid sharing layers between threads (see [28.8](#data-layers-1)).\r\n\r\n'
    b'If you wish to share the TSLStandardDataLayer (see [28.9](#standard-data-layer-1)) between threads then you need to call TSLUtilityFunctions::setThreadedOptions to set the bit represented by TSLThreadedOptionsRenderingSupport.\r\n\r\n'
    b'## Coordinate System Resource Loading'
))

# Fix T3: Prose text about 3DStandardDataLayer thread safety wrongly inside ```cpp fence
fixes.append(('T3 3D DrawingSurface rendering prose in fence',
    b'```cpp\r\n'
    b'While in general the drawing is thread safe you should avoid sharing layers between threads (see [28.8](#data-layers-1)).\r\n\r\n'
    b'If you wish to share the TSL3DStandardDataLayer between threads, you must call TSLUtilityFunctions::setThreadedOptions to set the bit represented by TSLThreadedOptionsRenderingSupport. In addition, you must add the layer to all drawing surfaces before you start any drawing and you should not edit the layer once drawing has occurred.\r\n'
    b'```\r\n'
    b'Ideally you should not share the TSL3DStandardDataLayer',
    b'While in general the drawing is thread safe you should avoid sharing layers between threads (see [28.8](#data-layers-1)).\r\n\r\n'
    b'If you wish to share the TSL3DStandardDataLayer between threads, you must call TSLUtilityFunctions::setThreadedOptions to set the bit represented by TSLThreadedOptionsRenderingSupport. In addition, you must add the layer to all drawing surfaces before you start any drawing and you should not edit the layer once drawing has occurred.\r\n\r\n'
    b'Ideally you should not share the TSL3DStandardDataLayer'
))

for name, old, new in fixes:
    found = old in content
    print(f'{name}: found={found}')
    if found:
        content = content.replace(old, new, 1)
    else:
        print(f'  first 60: {old[:60]}')
        print(f'  first 60 found: {old[:60] in content}')

with open(r'c:\maplink\maplink-docs\pages\developers-guide\threading.md', 'wb') as f:
    f.write(content)
print('threading.md written')
