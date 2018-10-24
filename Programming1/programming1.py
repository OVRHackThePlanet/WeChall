# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:34:09 2018

@author: mfulghum
"""

import urllib2

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'WC=10920010-22768-MDaEYdKv4BOldUfK'))

token = opener.open('http://www.wechall.net/challenge/training/programming1/index.php?action=request').read()
opener.open('http://www.wechall.net/challenge/training/programming1/index.php?answer=%s' % token).read()