#! /usr/bin/env python3

f = open('msgpack.nvgt', 'rb')
lines = f.read().splitlines()
f.close()
startline = lines.index(b'/// BEGIN DEBUG ///')
newlines = []
for i in range(startline):
    line = lines[i]
    if b'dbgout' not in line:
        newlines.append(line)
f = open('msgpack.nvgt', 'wb')
f.write(b'\n'.join(newlines))
f.close()