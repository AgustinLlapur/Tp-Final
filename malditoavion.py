import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


voxelarray = np.zeros((15, 15, 10), dtype=bool)
voxelarray[0:4, 1:2, 0:1] = True 
voxelarray[2:3, 0:3, 0:1] = True 
voxelarray[0:1, 1:2, 0:2] = True 

# = voxelarray[coordenada x:largo, coord y:coord y + 1, coord z:coord z +1]
# = voxelarray[coord x+2:coord x +3, coord y-1:coord y + 2, coord z:coord z +1]

# = voxelarray[coord x :coord x +1, coord y:coord y + 1, coord z:coord z +2]



fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()