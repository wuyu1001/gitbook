# Heroku部署步骤：

* 注册一个 Heroku 账号
* 安装 Heroku 命令行工具 
* 命令行下 Heroku login
* heroku create yourappname （此时建立了一个到 Heroku 的远程连接，可使用git remote -v 查看）
* git add .
* git commit -m 'comment content'
* git push heroku master
* heroku open

## 创建Procfile
* 安装gunicorn(Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.)
	* $pip install gunicorn
	
* 在文档中写入web: gunicorn -w 4 myapp:app

## 创建Pipfile
这是一个环境配置安装文档，通过pipenv安装时可以自动生成  
跟requirements.txt文档类似

## 连接Postgres数据库
* $heroku addons显示安装的插件
* $heroku config显示环境配置参数
* $heroku pg:psql打开本地数据库,pg跟vi命令相似
