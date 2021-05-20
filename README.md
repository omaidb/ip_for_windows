ip_for _windows

Linux下的`ip`命令显示本机ip地址非常好用,Windows下要输入很长的`ipconfig`

搜了下竟然没有相关的工具,就是自己用python写了一个,即可以查看内网地址,也可以查看公网地址

使用了request去请求ip接口,返回响应结果

然后用`pyinstaller -F ip.py `编译成ip.exe

### 安装方法

将pip.exe 复制到`C:\Windows\system32\`目录下

#### 查看本机ip

```bash
#cmd命令行下输入
ip
# 会显示本机内网ip和公网ip地址
```
![image](https://user-images.githubusercontent.com/18365223/118925359-306fac00-b971-11eb-84d2-e24e5e6028e4.png)



#### 查看域名

```bash
#cmd命令行下输入
ip baidu.com

# 显示结果
C:\Users\qiaofei> ip baidu.com
{'as': 'AS23724 IDC, China Telecommunications Corporation',
 'city': '北京',
 'country': '中国',
 'countryCode': 'CN',
 'isp': 'IDC, China Telecommunications Corporation',
 'lat': 39.9042,
 'lon': 116.407,
 'org': '',
 'query': '220.181.38.148',
 'region': 'BJ',
 'regionName': '北京市',
 'status': 'success',
 'timezone': 'Asia/Shanghai',
 'zip': ''}
```



#### 查询ip地址

```bash
#cmd命令行下输入
ip 114.114.114

# 显示结果
 C:\Users\qiaofei> ip 114.114.114.114
{'as': 'AS4134 CHINANET-BACKBONE',
 'city': '北京',
 'country': '中国',
 'countryCode': 'CN',
 'isp': 'China Unicom Shandong Province network',
 'lat': 39.9042,
 'lon': 116.407,
 'org': 'NanJing XinFeng Information Technologies, Inc.',
 'query': '114.114.114.114',
 'region': 'BJ',
 'regionName': '北京市',
 'status': 'success',
 'timezone': 'Asia/Shanghai',
 'zip': ''}
```



