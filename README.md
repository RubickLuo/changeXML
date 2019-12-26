#ChangeXml
修改YOLO-v3的annotations文件夹下的xml文件。通过遍历文件夹读取xml文件结构，搜索相应关键字，匹配当前工作目录并修改错误条目。
###主要功能

* 删除与JPEGImages文件夹不匹配的xml文件及jpg文件
* 删除xml文件夹中存在错误的文件（例如，path参数为空）
* 处理xml文件中path条目与当前工作目录不匹配的问题，自动修改为当前工作目录。
* 修改xml文件中filename及folder条目
######[此外，为了保证annotations文件夹数据完整，将存在img的图片copy到img目录下；将不存在img的xml文件move到noImgXml文件夹下]