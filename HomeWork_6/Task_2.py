# Самая далекая планета
from math import pi
def find_farthest_orbit(a, b):
	s = pi * a * b
	return s

def find_elips(array,x):
	for item in range(len(array)):
		m = array[item]
		if x == find_farthest_orbit(m[0], m[1]):
			return m

orbits = [(1,3), (2.5,10), (7,2), (6,6), (4,2)]
new_arr = []
for item in range(len(orbits)):
	arr = orbits[item]
	if arr[0] != arr[1]:
		new_arr.append(find_farthest_orbit(arr[0], arr[1]))

max_orbit = max(new_arr)

print(find_elips(orbits,max_orbit))

