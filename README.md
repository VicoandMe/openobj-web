# openobj
使用python web开发框架django 1.9.2版本，基于python 3.5.1，前端使用Bootstrap
# 环境配置
##Windows

* 1.下载python：去网站https://www.python.org/ 下载python（3.5.1 or 更高），并安装
* 2.检查安装是否成功：安装完成后打开`cmd`，输入`python`后，会显示出版本号信息,确认版本号信息是3.5.1及以上。
* 3.下载工程：`git clone`项目`openobj-web`到本地
* 4.下载依赖包：`cmd`进入`deploy`目录输入：`pip install -r requirements.txt`
* 5.更新数据库信息：`cmd`进入`openobj`目录输入：`python manage.py makemigrations` 和 `python manage.py migrate`
* 6.运行工程：`cmd`进入`openobj`目录输入：`python manage.py runserver`如果没有显示错误信息则启动成功
* 7.进入http://127.0.0.1:8000 可看到实例

##Mac OS X
* 1.下载python：去网站https://www.python.org/ 下载python（3.5.1 or 更高），并安装
* 2.检查安装是否成功：安装完成后打开终端，输入`python3`后，会显示出版本号信息,确认版本号信息是3.5.1及以上。
* 3.下载工程：`git clone`项目`openobj-web`到本地
* 4.下载依赖包：终端进入`deploy`目录输入：`pip3 install -r requirements.txt`
* 5.更新数据库信息：终端进入`openobj`目录输入：`python3 manage.py makemigrations` 和 `python3 manage.py migrate`
* 6.运行工程：终端进入`openobj`目录输入：`python3 manage.py runserver`如果没有显示错误信息则启动成功
* 7.进入http://127.0.0.1:8000 可看到实例

##推荐使用IDE
pycharm
http://www.jetbrains.com/pycharm/download/#section=windows
