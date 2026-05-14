import re
with open(r'c:/maplink/maplink-docs/pages/developers-guide/ogc-services-sdk.md', 'rb') as f:
    content = f.read()
start = content.find(b'TSLWPSProcessDescriptionType\\* SampleWPSDataSource')
# find all ``` positions after start
fences = [m.start() for m in re.finditer(b'```', content[start:])]
print('fence offsets from start:', fences[:20])
end = start + fences[-1] + 3
section = content[start:end]
print(repr(section))
