# webFlask
flask入门实践
学生信息管理系统初步

# 环境配置：
python3.6.3

mysql  Ver 14.14 Distrib 5.7.19, for macos10.12

    pipenv install
# 如何运行项目
数据库导入：

    mysql>create database admintest;
    mysql -u root -pfengyufei123 admintest < admintest.sql

程序入口：
python3 flaskr.py

# 目前实现功能：

登注册，上传文件，信息的增删改查等简单操作

全量数据导出到文件(格式为csv)

后续实现：

完善css，在页面中显示全量数据

课程表功能完善

权限设置等



