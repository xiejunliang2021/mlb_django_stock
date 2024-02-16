# -*- coding: utf-8 -*-
# @Time    : 2023/6/2 19:27
# @Author  : 花本无心
# @Motto   : 梦想，可以天花乱坠，理想，是我们一步一个脚印踩出来的坎坷道路！
# @File    : conn.py
# @Software: PyCharm 
# @Comment : 数据库的连接


import oracledb
import config


class Conn():
    def __init__(self):
        pass

    def conn_mlb(self):
        connection = oracledb.connect(
            user=config.name_mlb,
            password=config.password_mlb,
            dsn="mhuabenwuxin_low",
            config_dir="./config_dir_mlb",
            wallet_location="./config_dir_mlb",
            wallet_password=config.password_wallet_mlb)
        return connection

    def conn_jap(self):
        connection = oracledb.connect(
            user="hbwx_jap",
            password=config.password_jap,
            dsn=config.dsn_jap,
            config_dir="./config_dir_jap",
            wallet_location="./config_dir_jap",
            wallet_password=config.password_wallet_jap)
        return connection


if __name__ == '__main__':
    conn = Conn()
    con = conn.conn_mlb()
    cur = con.cursor()
    sql = "select * from code"
    res = cur.execute(sql)
    for row in res:
        print(row)
    cur.close()
    con.close()


    # con_jap = conn.conn_jap()
    # cur = con_jap.cursor()
    # sql = "select * from code_2"
    # res = cur.execute(sql)
    # for row in res:
    #     print(row)
    #
    # cur.close()
    # con_jap.close()
