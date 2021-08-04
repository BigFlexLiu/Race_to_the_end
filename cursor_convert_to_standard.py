"""
    Work together with cursor_blueprint.py

    This file converts the symbol cursors are writen in
    to match the standard black='X', white='.', xor='o'
    in pygame.cursors.compile(black='X', white='.', xor='o')
    This document is just a way to make work load easier
    it is to be changed accordingly, depending on situations
"""
import cursor_blueprint

# our beloved associated file for appending back the result
file = 'cursor_blueprint.py'

# The cursor blueprint that will be edited
lines = cursor_blueprint.onichan

line = []
for i in range(len(lines)):
    line.append(lines[i])
    line[i] = line[i].replace('o', '.')

for i in line:
    print(i)

with open(file, 'a') as f:
    for i in line:
        f.writelines('\t"' + i + '",\n')


