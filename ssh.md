# ssh配置
## ssh命令
 用** $ ssh-keygen **可以在主目录创建一个.ssh文件夹，然后生成id\_rsa和id_rsa.pub,这是通过Rsa算法产生，前者为私匙，后者为公匙
 
## github上配置公匙
用cat命令打开id\_ras.pub,将其复制  
打开github首页，选择settings,进入后点击[SSH and GPG keys],点击[New SSH key],粘贴公匙在框框内

## 用git链接远程仓库
1 在github上点击[New repository]建立新仓库  
2 本地用git init初始化，得到.git文件夹  
3 git add README.md 添加文件到仓库  
4 git commit -m 'First commit'  
5 git remote add origin git@github.com:username/demo.git **注**：username is your github username, demo is repository name  
6 git push -u origin master 推送本地内容到远程仓库 **注**：-u是首次推送需要参数，再次推送可以省略  
7 **坑**：$ git push -u origin master  
---  
ssh: Could not resolve hostname git: nodename nor servname provided, or not known  
---  
fatal: Could not read from remote repository.  
---  
Please make sure you have the correct access rights  
---  
and the repository exists.  
---
出现这种情况可以用[git remote set-url origin git@github.com:username/demo.git]  
但是一定要****先删除.git文件夹**，然后重新执行上面的操作