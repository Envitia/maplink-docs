with open(r'c:/maplink/maplink-docs/pages/developers-guide/threading.md', 'rb') as f:
    content = f.read()

# Find the SquareClient section
start = content.find(b'class SquareClient')
end = content.find(b'\r\n```\r\n', start + 500) + 6  # end after last fence
print('SQUARECLIENT SECTION:')
print(repr(content[start:end]))
print()

# Find T11 user geometry creation section
start2 = content.find(b'TSL3DStandardDataLayer\\* stdLayer')
end2 = content.find(b'delete client;', start2) + 60
print('T11 USER GEOMETRY:')
print(repr(content[start2:end2]))
print()

# Find T13 load callback section
start3 = content.find(b'TSL3DUserGeometryEntity::')
end3 = content.find(b'\r\n```\r\n', start3 + 500) + 6
print('T13 LOAD CALLBACK:')
print(repr(content[start3:end3]))
