import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
	def __init__( self, xs, ys, zs, *args, **kwargs ):
		FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
		self.verts3d = xs, ys, zs
	
	def draw( self, renderer ):
		xs3d, ys3d, zs3d = self.verts3d
		xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
		self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
		FancyArrowPatch.draw(self, renderer)


def sphere( ax, center, radius=1 ):
	u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
	x = radius*np.cos(u)*np.sin(v) + center[0]
	y = radius*np.sin(u)*np.sin(v) + center[1]
	z = radius*np.cos(v) + center[2]
	# ax.plot_wireframe(x, y, z, color='r')
	# ax.contour3D(x, y, z, color='b')
	ax.plot_surface(x, y, z, color='g', alpha=0.15, linewidth=0.7, rstride=4, cstride=4, edgecolor='green')
