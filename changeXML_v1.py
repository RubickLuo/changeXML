# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:31:18 2019

@author: LqH-_
"""

import os
import xml.etree.ElementTree as ET
import time

start_time = time.time()
end_time = 0
for dir_path, dirs, files in os.walk("Annotations/"):
    for file in files:
        dir = os.path.join(dir_path, file)
        updateTree = ET.parse(dir)
        root = updateTree.getroot()
        path = root.find("path")
        path.text = "/home/lqh/Downloads/darknet/scripts/VOCdevkit/VOC2007/JPEGImages/" + file
        updateTree.write("Annotations/" + file)
end_time = time.time()
cost_time = (end_time - start_time)
print("cost time:" + str(cost_time))
