# virtualenv
* virtualenv主要用创建不同python版本的独立开发环境
* 安装pip install virtualenv
* virtualenv myproject创建项目文件夹
* cd myproject 进入工作区，用source bin/activate激活该环境 
 
**注意**：
---
如果已经在本地安装了不同版本的python,可以用参数--python=python(版本号)  
e.g:
virtualenv --python=python2.7 venv 表示venv是2.7的开发环境  
virtualenv --Python=Python3.6 venv 表示创建了3.6开发环境  
*参数--no-site-packages可以创建一个不带任何包的空开发环境*
---