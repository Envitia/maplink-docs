import re, os

RAW = 'c:/maplink/maplink-docs/devguide_new_raw.md'
OUT = 'c:/maplink/maplink-docs/pages/developers-guide'

SECTION_MAP = {
    'Introduction': 'introduction.md',
    'MapLink SDK Components and Concepts': 'sdk-components.md',
    'Basic MapLink Applications': 'basic-applications.md',
    'Unicode': 'unicode.md',
    'MapLink and your Development Environment': 'development-environment.md',
    'Deployment of End User Application': 'deployment.md',
    'Samples': 'samples.md',
    'Walkthrough 1 - Your First MapLink Application': 'walkthrough-1.md',
    'Walkthrough 2 - Modifying the Visible Area': 'walkthrough-2.md',
    'Geometry and Overlays': 'geometry-and-overlays.md',
    'Walkthrough 3 - Adding a Simple Vector Overlay': 'walkthrough-3.md',
    'More Features of the Core SDK': 'advanced-features.md',
    'OpenGL Drawing Surface': 'opengl-drawing-surface.md',
    'Direct Import SDK': 'direct-import-sdk.md',
    'Tracks SDK': 'tracks-sdk.md',
    'Dynamic Overlays with the DDO SDK': 'ddo-sdk.md',
    'Terrain SDK': 'terrain-sdk.md',
    'MapLink 3D Earth SDK': 'maplink-3d-earth-sdk.md',
    'Editor SDK': 'editor-sdk.md',
    'Geopackage SDK': 'geopackage-sdk.md',
    'OWSContext SDK': 'owscontext-sdk.md',
    'MapLink OGC Services SDK': 'ogc-services-sdk.md',
    'Spatial SDK': 'spatial-sdk.md',
    'GML SDK': 'gml-sdk.md',
    '.NET SDKs': 'net-sdks.md',
    'Floating Point': 'floating-point.md',
    'Other SDKs': 'other-sdks.md',
    'Threading': 'threading.md',
}

H1_RE = re.compile(r'^#\s+(.+?)\s*\{[^}]*\.(?:ENV|Env)---Heading-1[^}]*\}\s*$')

with open(RAW, encoding='utf-8') as f:
    lines = f.readlines()

sections = []
current = None
start = None
in_code = False
for i, line in enumerate(lines):
    if line.startswith('```') or line.startswith('~~~'):
        in_code = not in_code
    m = H1_RE.match(line)
    if m and not in_code:
        if current is not None:
            sections.append((current, start, i))
        current = m.group(1).strip().replace(' -- ', ' - ')
        start = i
if current:
    sections.append((current, start, len(lines)))

print(f"{'Section':<48} {'Raw':>6} {'Split':>6}  Status")
print('-' * 72)

problems = []
for heading, start, end in sections:
    raw_count = end - start
    fname = SECTION_MAP.get(heading)
    if not fname:
        print(f"{heading[:48]:<48} {raw_count:>6} {'---':>6}  MISSING FILE")
        problems.append(f"No file mapped for: {heading}")
        continue
    path = os.path.join(OUT, fname)
    with open(path, encoding='utf-8') as f:
        split_lines = f.readlines()
    split_count = len(split_lines)
    ratio = split_count / raw_count if raw_count else 0
    if ratio < 0.75 or ratio > 1.6:
        status = 'CHECK'
        problems.append(f"{fname}: ratio {ratio:.2f} (raw={raw_count}, split={split_count})")
    else:
        status = 'ok'
    print(f"{heading[:48]:<48} {raw_count:>6} {split_count:>6}  {status}")

# Check for unclosed code fences in split files
print()
for fname in SECTION_MAP.values():
    path = os.path.join(OUT, fname)
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        content = f.read()
    fences = re.findall(r'^```', content, re.MULTILINE)
    if len(fences) % 2 != 0:
        problems.append(f"{fname}: odd number of code fences ({len(fences)}) - likely unclosed block")

print()
if problems:
    print("PROBLEMS:")
    for p in problems:
        print(f"  {p}")
else:
    print("All sections verified OK.")
