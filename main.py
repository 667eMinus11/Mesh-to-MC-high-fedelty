import trimesh
import math
import numpy as np
from trimesh.voxel import creation
from trimesh.transformations import scale_matrix
import mcschematic
from collections import defaultdict
from mcpi.minecraft import Minecraft
import mcpi.block as block


Block_shape_dict = {
    0: 'minecraft:air',
    3: 'minecraft:air',
    66: 'minecraft:air',
    9: 'minecraft:air',
    72: 'minecraft:air',
    20: 'minecraft:air',
    132: 'minecraft:air',
    160: 'minecraft:air',
    48: 'minecraft:air',
    5: 'minecraft:air',
    129: 'minecraft:air',
    130: 'minecraft:air',
    96: 'minecraft:air',
    11: 'minecraft:stone_slab[type=bottom]',
    67: 'minecraft:stone_slab[type=bottom]',
    73: 'minecraft:stone_slab[type=bottom]',
    74: 'minecraft:stone_slab[type=bottom]',
    52: 'minecraft:stone_slab[type=top]',
    148: 'minecraft:stone_slab[type=top]',
    164: 'minecraft:stone_slab[type=top]',
    176: 'minecraft:stone_slab[type=top]',
    1:'minecraft:air',
    2:'minecraft:air',
    4:'minecraft:air',
    8:'minecraft:air',
    16:'minecraft:air',
    32:'minecraft:air',
    64:'minecraft:air',
    128:'minecraft:air',
    75: 'minecraft:stone_slab[type=bottom]',
    180: 'minecraft:stone_slab[type=top]',
    207: 'minecraft:stone_stairs[facing=west,half=bottom]',
    95: 'minecraft:stone_stairs[facing=north,half=bottom]',
    123:'minecraft:stone_stairs[facing=east,half=bottom]',
    235: 'minecraft:stone_stairs[facing=south,half=bottom]',
    183: 'minecraft:stone_stairs[facing=west,half=top]',
    189: 'minecraft:stone_stairs[facing=north,half=top]',
    252:'minecraft:stone_stairs[facing=east,half=top]',
    246: 'minecraft:stone_stairs[facing=south,half=top]',
    255: 'minecraft:stone'
}


def slice_to_2by2(voxels):
    shape=voxels.matrix.shape
    blockShapes=np.zeros( (math.ceil(shape[0]/2),math.ceil(shape[1]/2),math.ceil(shape[2]/2)))#x,y,z val=8 bit unsignd int
    for i in range(shape[0]-1):
       for j in range(shape[1]-1):
           for k in range(shape[2]-1):
              if (i%2)==0 and (j%2)==0 and (k%2)==0:
                num=voxels.matrix[i,j,k]+voxels.matrix[i,j,k+1]*2+voxels.matrix[i,j+1,k]*4+voxels.matrix[i+1,j,k]*8+voxels.matrix[i+1,j+1,k]*16+voxels.matrix[i+1,j+1,k+1]*32+voxels.matrix[i+1,j,k+1]*64+voxels.matrix[i,j+1,k+1]*128
                #print(num)
                blockShapes[math.ceil(i/2),math.ceil(j/2),math.ceil(k/2)]=num
    return blockShapes

def blockesToSchematic(filename,blocks):
    shape=blocks.shape
    schem = mcschematic.MCSchematic()
    for i in range(shape[0]) :
        for j in range(shape[1]):
            for k in range(shape[2]):
                block=Block_shape_dict.get(blocks[i,j,k],"minecraft:stone")
                print(block)
                schem.setBlock((i,j,k),block)
    schem.save("", filename, mcschematic.Version.JE_1_18_2)
    return
# Load mesh data
def previewSchematic():
    # Connect to the Minecraft game
    mc = Minecraft.create()

    # Set the starting position for the schematic
    x, y, z = 0, 0, 0

    # Replace "schematic_file.schematic" with the name of your schematic file
    with open("test.schem", "rb") as f:
     # Load the schematic from the file
      data = f.read()
       # Paste the schematic in the game
      mc.setBlocks(x, y, z, x+15, y+15, z+15, block.AIR.id)
      mc.setSchematic(x, y, z, data, block.AIR.id)


mesh_data = trimesh.load('test.stl')
voxels = mesh_data.voxelized(0.05)

blockesToSchematic("test",slice_to_2by2(voxels))
previewSchematic()
#voxels.show()