# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:30:06 2018

@author: mfulghum
"""

import cv2
import matplotlib.pyplot as plt

im = cv2.imread('MDaEYdKv4BOldUfK.png')
plt.imshow(im[:,:,2] & 0b00001000)
# EILFCOGGFNBO
