# django-fodo
A Django Sample Project
* [Blog](#1)
* [Polls](#2)
* [Run](#3)
	* [command](#3.1)
	* [docker](#3.2)


<h2 id=1>Blog</h2>
- Blog列表页
- 文章页
- 修改页

<h2 id=2>Polls</h2>
- 投票列表页
- 投票页
- 投票结果页

<h2 id=3>Run</h2>
共两张启动方法：
<h3 id=3.1>Command</h3>
git clone 程序到本地以命令行启动：

```
# 先初始化数据库
python manage.py makemigrations
python manage.py migrate
# 再运行程序
python manage.py runserver 
```

<h3 id=3.2>docker</h3>
进入工程目录，输入命令启动程序

```
docker-compose up -d
```

浏览器访问 http://localhost:8000.