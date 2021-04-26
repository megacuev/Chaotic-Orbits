from numpy import *
from scipy import *
from matplotlib.pyplot import *
from random import randrange 

#number of steps
N = 1500;

def StandardMap((x,p)):
    pn = mod(p+K*sin(x), 2*pi)
    xn = mod(x+pn, 2*pi)
    return (xn, pn)

#making phase space
x0 = linspace(0, 2*pi, 7)
p0 = linspace(0, 2*pi, 12)
mesh = list()
for ii in xrange(len(x0)):
    for jj in xrange(len(p0)):
        mesh.append((x0[ii], p0[jj]))

#kicking parameter K
Kvals = [1.0, 1.2, 1.4, 1.6]

for val in Kvals:
    K = val
    fig = figure(figsize=(5,5))
    for item in mesh:
        traj = [item]
        for ii in xrange(N):
            traj.append(StandardMap(traj[ii]))
        plot(array(traj).T[0], array(traj).T[1], '.',markersize=2.0)
        hold(True)

    xlim([0, 2*pi])
    ylim([0, 2*pi])
    xlabel('Position (rad)')
    ylabel('Momentum')
    title("K = {}".format(val))
    filename='map-k-%f.pdf'%val
    savefig(filename)
    show()

