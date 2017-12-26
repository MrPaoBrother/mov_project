mov_project's Document


---
*  创建一个独立的Python虚拟环境, 并进入

```
$ virtualenv --no-site-packages venv

$ source venv/bin/activate

```

*  使用命令安装项目的运行依赖：


```
$ pip install -r requirements.txt
```


* 在mov_project 下运行django应用：

```
$ gunicorn -w 4 -b 服务器ip地址:任意空闲端口号（建议8000以后） wsgi:application
```

*  浏览器打开地址：http://45.77.150.109:8000/xadmin/

登录账号：power     登录密码：13672240290cccc





