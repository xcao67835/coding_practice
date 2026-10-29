# -*- coding: utf-8 -*-

dick={
"Tetrahedron":4,
"Cube":6,
"Octahedron":8,
"Dodecahedron":12,
"Icosahedron":20
}
a=0
for i in range(int(input())):
    a+=dick[input()]
print(a)