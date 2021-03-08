#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2021 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Wednesday, December 16th 2020, 11:48:57 am                    #
# -----                                                                        #
# 'basic_animation.py' is part of the project 'basic_animation'.               #
#                                                                              #
# basic_animation is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# basic_animation is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with basic_animation.  If not, see <https://www.gnu.org/licenses/>.    #
################################################################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True
mpl.rcParams['animation.html'] = 'html5'

th = np.linspace(0,2*np.pi,1000)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(9,4))

ax2.plot(th,np.cos(th),color="b",label=r"cos($\theta$)")
ax2.plot(th,np.sin(th),color="g",label=r"sin($\theta$)")
plt.legend()
ax1.plot(np.cos(th),np.sin(th),color="black")

line1, = ax1.plot(np.cos(th),np.sin(th),'o',c="r")
line2, = ax2.plot(th,np.sin(th),'o',c="r")
line3, = ax2.plot(th,np.cos(th),'o',c="r")

ax1.set_xlabel(r"cos($\theta$)")
ax1.set_ylabel(r"sin($\theta$)")

ax2.set_xlabel(r"$\theta$")
ax2.set_ylabel(r"f($\theta$)")

ax1.set_xticks([-1,0,1])
ax2.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi])
ax2.set_xticklabels([0,"$\pi$/2","$\pi$","3$\pi$/2","2$\pi$"])

for ax in (ax1,ax2):
    ax.grid(c="g")
    ax.set_yticks([-1,0,1])

def animate(th):
    line1.set_data(np.cos(th),np.sin(th))
    line2.set_data(th,np.sin(th))
    line3.set_data(th,np.cos(th))
    return line1,line2,line3

plt.tight_layout()
ani = animation.FuncAnimation(fig,animate,np.arange(0,2*np.pi,0.1),interval=50,blit=True)
plt.show()