# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:53:44 2019

@author: LqH-_
"""
import os
import shutil
from pathlib import Path
import xml.etree.ElementTree as ET
from os import getcwd
import time

# 计算开始时间及获取当前目录
start_time = time.time()
end_time = 0
pwd = getcwd()
# print("pwd：", pwd)
imgPWD = os.path.join(pwd, "JPEGImages")
xmlPWD = os.path.join(pwd, "Annotations")
# print("imgPwd：", imgPWD)

# os.listdir()方法遍历目录：根据xml文件中imgName构建img目录，并查询imgDir是否存在。
total_xml = os.listdir("Annotations")
# print(len(total_xml))
for xml in total_xml:
    imgName = xml.split('.')[0] + '.jpg'
    imgDir = os.path.join(imgPWD, imgName)
    xmlDir = os.path.join(xmlPWD, xml)

    # 处理文件不对应的问题，并放置到新文件夹下。
    # if os.path.exists(imgName)
    if Path(imgDir).exists():
        shutil.copy(imgDir, 'img')
        # shutil.move(imgDir, 'img')
    elif not Path(imgDir).exists():
        # os.remove(xmlDir)
        shutil.move(xmlDir, 'noImgXml')
        continue
    # # 在try 语句块中，可以使用 resolve() 方法来判断：
    # try:
    #     my_abs_path = imgDir.resolve()
    # except FileNotFoundError:
    #     # 不存在
    #     pass
    # else:
    #     # 存在
    #     pass
    updateTree = ET.parse(xmlDir)
    root = updateTree.getroot()

    folder = root.find("folder")
    filename = root.find("filename")
    path = root.find("path")

    if path is None:
        # 删除错误的文件
        try:
            os.remove(imgDir)
        except Exception as e:
            print(e)
            print("Image Maybe removed！")
        else:
            os.remove(xmlDir)
    else:
        folder.text = "JPEGImages"
        filename.text = imgName
        path.text = xmlDir
        updateTree.write(xmlDir)

end_time = time.time()
cost_time = (end_time - start_time)
print("cost time:" + str(cost_time))

# 遍历Annotations目录
# dir_path是依次遍历Annotations及其下的文件夹目录(str)
# dirs是Annotations下的文件目录(list)
# files是对应目录下的所有文件名(list)

# for dir_path, dirs, files in os.walk("Annotations"):
#     for file in files:
#         dir = os.path.join(dir_path, file)
#         # print(dir)
#         imgName = file.split('.')[0] + ".jpg"
#         imgDir = os.path.join(imgPWD, imgName)
#
#         # if os.path.exists(imgName)
#         if imgDir.exists():
#             pass
#         # 在try 语句块中你可以使用 resolve() 方法来判断：
#         try:
#             my_abs_path = imgDir.resolve()
#         except FileNotFoundError:
#             # 不存在
#             pass
#         else:
#             # 存在
#             pass
