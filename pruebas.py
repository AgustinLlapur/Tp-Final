import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Tamaño de la cuadrícula
grid_size_xy= 15
grid_size_z= 10
grid_size_xy= 15
x, y, z = np.indices((15, 15, 10))
# Número de cubos y sus coordenadas
num_cubes = 5
cube_coords = [(1, 1, 1), (4, 4, 4), (2, 6, 3), (5, 2, 6), (6, 6, 2)]


# --- OBJETOS ---
# Crear una matriz booleana para cada cubo
cubes = []
for i in range(num_cubes):
    cube_coords_i = cube_coords[i]
    cube_i = (x >= cube_coords_i[0]) & (y >= cube_coords_i[1]) & (z >= cube_coords_i[2])
    cube_i = cube_i & (x < cube_coords_i[0] + 3) & (y < cube_coords_i[1] + 3) & (z < cube_coords_i[2] + 3)
    cubes.append(cube_i)

num_zep = 3
zep_coords = [(2, 2, 2), (5, 5, 5), (4, 8, 6), (10, 4, 12), (12, 12, 4)]

zeps = []
for i in range(num_zep):
    zep_coords_i = zep_coords[i]
    zep_i = (x >= zep_coords_i[0]) & (y >= zep_coords_i[1]) & (z >= zep_coords_i[2])
    zep_i = zep_i & (x < zep_coords_i[0] + 2) & (y < zep_coords_i[1] + 5) & (z < zep_coords_i[2] + 2)
    zeps.append(zep_i) 

num_el = 1
el_coords = [(2, 2, 2), (5, 5, 5), (4, 8, 6), (10, 4, 12), (12, 12, 4)]

elev = []
for i in range(num_el):
    el_coords_i = el_coords[i]
    el_i = (x >= el_coords_i[0]) & (y >= el_coords_i[1]) & (z >= el_coords_i[2])
    el_i = el_i & (x < el_coords_i[0] + 1) & (y < el_coords_i[1] + 1) & (z < el_coords_i[2] + 10)
    elev.append(el_i) 



# Combinar las matrices booleanas de los cubos
voxelarray = np.zeros((grid_size_xy, grid_size_xy, grid_size_z), dtype=bool)
for cube in cubes:
    voxelarray |= cube
for zep in zeps:
    voxelarray |= zep
for el in elev:
    voxelarray |= el
    

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k')

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
