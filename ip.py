"""
===========
@author: qiaofei
@time:2021/5/20:11:18
@IDE:PyCharm
@blog: https://blog.csdn.net/omaidb
===========
"""
import os
import sys
from pprint import pprint

import requests


def showip(ip=None):
    """
    查看本机内网和外网ip地址
    :param ip:传入ip地址,查本机内网地址可不传
    :return: 以json格式返回ip地址信息
    """

    try:
        # ip作为命令行第一个参数传进来
        ip = sys.argv[1]
    except:
        ip = None
        # 如果ip为真,就调用ip查询接口查询ip
    if ip:
        try:
            response = requests.get(
                f'http://ip-api.com/json/{ip}?lang=zh-CN', timeout=7)

            pprint(response.json())
        except Exception as e:
            print(e)
    # 如果不为真,就调用接口查询本机外网ip
    else:
        try:
            response = requests.get(
                'https://myip.ipip.net/', timeout=2)
            print(response.text, end='')
        except:
            response = requests.get(
                f'http://ip-api.com/json/?lang=zh-CN', timeout=7)
            pprint(response.json())
        # 执行本机自带的ipconfig命令显示本机内网ip
        ipconfig = os.popen('ipconfig')
        ipconfig = ipconfig.buffer.read().decode(encoding='gbk').splitlines()
        # 格式优化
        for i in ipconfig:
            if i:
                print(i.replace('. ', ''))


if __name__ == '__main__':
    showip()
