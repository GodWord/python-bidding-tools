# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/1/24 22:15'
import pymysql

DB_CONNS = {
    'default': lambda: pymysql.connect(host="localhost", port=3306, user="root",
                                       password="training", db="crawler_db", charset='utf8mb4'),
}
