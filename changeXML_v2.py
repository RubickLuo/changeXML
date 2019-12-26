# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:31:18 2019

@author: LqH-_
"""

import os
import xml.etree.ElementTree as ET
from os import getcwd
import time

start_time = time.time()
end_time = 0
pwd = getcwd()
imgPwd = os.path.join(pwd, "JPEGImages")

for dir_path, dirs, files in os.walk("Annotations"):
    for file in files:
        dir = os.path.join(dir_path, file)
        updateTree = ET.parse(dir)
        root = updateTree.getroot()

        folder = root.find("folder")
        filename = root.find("filename")
        path = root.find("path")
        
        imgname = file.split('.')[0] + ".jpg"
        xmlDir = os.path.join(pwd, dir)
        imgDir = os.path.join(imgPwd, imgname)
        if path != None:
            folder.text = "JPEGImages"
            filename.text = imgname
            path.text = xmlDir
            updateTree.write("Annotations/" + file)
        else:
            # 删除错误的文件
            try:
                os.remove(xmlDir)
                os.remove(imgDir)
            except Exception as e:
                print(e)
                print("Image Maybe removed！")

end_time = time.time()
cost_time = (end_time - start_time)
print("cost time:" + str(cost_time))
