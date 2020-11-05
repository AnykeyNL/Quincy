import struct


def readFloat(filepointer):
    rawbytes = filepointer.read(4)
    [f] = struct.unpack('f', rawbytes)
    return f

def writeFloat(filepointer, value):
    rawbytes = struct.pack('f', value)
    filepointer.write(rawbytes)

def readInt(filepointer):
    rawbytes = filepointer.read(4)
    [i] = struct.unpack('i', rawbytes)
    return i

def writeFloat(filepointer, value):
    rawbytes = struct.pack('i', value)
    filepointer.write(rawbytes)


file =  open("test.pmd","wb")
file.write(struct.pack('b', 1))
file.write(struct.pack('i', 2))


points = []
x = float(22.0)
y = float(135.0)
while x < 90:
    points.append([x,y])
    x = x + 0.1
file.write(struct.pack('i', len(points)))
for p in points:
    file.write(struct.pack('f', p[0]))
    file.write(struct.pack('f', p[1]))

points = []
x = float(45)
y = float(155)
while y > 90:
    points.append([x,y])
    y = y - 0.1
file.write(struct.pack('i', len(points)))
for p in points:
    file.write(struct.pack('f', p[0]))
    file.write(struct.pack('f', p[1]))


file.close()


