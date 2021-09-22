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


def showip():
    """
    查看本机内网和外网ip地址
    :return: 以json格式返回ip地址信息
    """

    try:
        # ip作为命令行第一个参数传进来
        ip = sys.argv[1]
    except:
        # 如果参数为空,调用接口查询本地公网ip,并显示本地ip配置信息
        view_public_network_ip()
        ipconfig()

    else:
        # 如果ip参数为a,就执行ipconfig /all
        if ip == 'a':
            ipconfig()
        # 如果传参的第一位书数字,或第二位是字母,就调用接口查询ip或域名
        elif ip[0].isdigit() or ip[1].isalpha():
            query_ip_attribution(ip)


def view_public_network_ip():
    """
    查看本地公网ip
    :return:打印json格式的ip信息
    """
    try:
        response = requests.get(
            'https://myip.ipip.net/', timeout=2)
        print(response.text, end='')
    except:
        response = requests.get(
            f'http://ip-api.com/json/?lang=zh-CN', timeout=7)
        pprint(response.json())


def query_ip_attribution(ip):
    """
    查询ip归属地
    :param ip:传入ip或域名
    :return: 打印json格式的ip信息
    """
    try:
        response = requests.get(
            f'http://ip-api.com/json/{ip}?lang=zh-CN', timeout=7)

        pprint(response.json())
    except Exception as e:
        print(e)


def ipconfig():
    """
    显示本地ip配置信息
    :return:
    """
    exec_ipconfig = os.popen('ipconfig /all')
    exec_ipconfig = exec_ipconfig.buffer.read().decode(encoding='gbk').splitlines()
    # 格式优化
    for i in exec_ipconfig:
        if i:
            print(i.replace('. ', ''))


if __name__ == '__main__':
    showip()
