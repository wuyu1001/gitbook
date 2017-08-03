git运用
===
* git init创建.git文件夹
* git add提交文档 用*git add .* 可以一次性提交已经存在文件夹的所有文档 
* git commit -m "  "  
完成文档提交  

---
   
* git branch创建分支
* git checkout切换分支
* git merge合拼分支  
分支管理

---
* git status查看状态
* git diff检查所修改的内容
* git log显示当前分支历史版本  
信息查看

---
* git remote add git@github:uresname/demo.git增加远程仓库 git remote -v查看远程信息
* git pull取回远程仓库的变化，并与本地分支合并
* git push [branch]推送当前分支到远程  
 **注意**：首次推送用git push *-u* origin master,如果远程有更新则使用git push *-f* origin master
* git push --all推送所以分支
* git clone克隆远程仓库到本地

---
参考资料：[git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
