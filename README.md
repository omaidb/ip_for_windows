ip_for _windows

Linux下的`ip`命令显示本机ip地址非常好用,Windows下要输入很长的`ipconfig`

搜了下竟然没又相关的工具可以实现,就是自己用python写了一个

使用了request去请求ip接口,返回响应结果

然后用`pyinstaller -F ip.py `编译成ip.exe

