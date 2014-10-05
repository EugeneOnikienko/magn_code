import numpy as np
from matplotlib import pyplot as pp

#------------------------------------------------------------------------------------------------

def draw_angles_2d( angs, t ):
	max0 = angs[:, 0].max()
	min0 = angs[:, 0].min()
	
	max1 = angs[:, 1].max()
	min1 = angs[:, 1].min()

	max2 = angs[:, 2].max()
	min2 = angs[:, 2].min()
	
	mi = min(min0, min1)
	ma = max(max0, max1)

	yticks = np.linspace(mi, ma, 5)
	yt_labels = [ '$'+str(round(num, 1))+'\pi$' for num in yticks / np.pi]

	yticks2 = np.linspace(min2, max2, 5)
	yt_labels2 = [ '$'+str(round(num, 1))+'\pi$' for num in yticks2 / np.pi]
	
	fig = pp.figure()

	pp.subplot(211)
	pp.plot(t, angs[:, 2], 'g', label='$\Delta\phi$')
	pp.xlabel(r'time')
	pp.ylabel(r'$\Delta\phi$')
	pp.yticks(yticks2, yt_labels2)
	pp.grid(True)

	pp.subplot(212)
	pp.plot(t, angs[:, 0], 'r', label='$M_1$')
	pp.plot(t, angs[:, 1], 'b', label='$M_2$')
	pp.xlabel(r'time')
	pp.ylabel(r'$\theta$')
	pp.yticks(yticks, yt_labels)
	pp.legend(loc=7)
	pp.grid(True)

	pp.show()

#------------------------------------------------------------------------------------------------

def draw_angles_3d( angs ):
	from objects3D import sphere, Arrow3D

	m1  = np.array([
		np.sin(angs[:,0])*np.cos(0.5*angs[:,2]),
		np.sin(angs[:,0])*np.sin(0.5*angs[:,2]),
		np.cos(angs[:,0])
	])
	
	m2 = np.array([
		np.sin(angs[:,1])*np.cos(0.5*angs[:,2]),
		-np.sin(angs[:,1])*np.sin(0.5*angs[:,2]),
		np.cos(angs[:,1])
	])

	fig = pp.figure(figsize=(8, 6))
	
	ax1 = fig.add_axes([0.0, 0.0, 0.8, 1.0], projection='3d')

	ax1.set_xlim([-1, 1])
	ax1.set_ylim([-1, 1])
	ax1.set_zlim([-1, 1])

	axes = [
		Arrow3D([-1,1],[0,0],[0,0], mutation_scale=20, lw=0.5, arrowstyle="-|>", color="k"), 
		Arrow3D([0,0],[-1,1],[0,0], mutation_scale=20, lw=0.5, arrowstyle="-|>", color="k"),
		Arrow3D([0,0],[0,0],[-1,1], mutation_scale=20, lw=0.5, arrowstyle="-|>", color="k")
	]
	for axis in axes:
		ax1.add_artist( axis )

	sphere( ax1, np.zeros(3) )	
	ax1.plot( m1[0], m1[1], m1[2], 'r' )
	ax1.plot( m2[0], m2[1], m2[2], 'b' )


	ax2 = fig.add_axes([0.6, 0.55, 0.4, 0.4], polar=True, axisbg='#eeefff')
	ax3 = fig.add_axes([0.6, 0.05, 0.4, 0.4], polar=True, axisbg='#eeefff')
	
	r1 = np.sin(angs[:, 0])
	r2 = np.sin(angs[:, 1])
	theta1 = 0.5*angs[:, 2]
	theta2 = -0.5*angs[:, 2]
	
	ax2.plot(theta1, r1, color='red', lw=1.)
	ax2.set_rmax(1.0)
	ax2.set_yticks([0, 0.5, 1])
	pp.grid(True)
	
	ax3.plot(theta2, r2, color='blue', lw=1.)
	ax3.set_rmax(1.0)
	ax3.set_yticks([0, 0.5, 1])
	pp.grid(True)

	pp.show()