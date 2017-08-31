# 安装
npm install gitbook-cli -g

# gitbook cmd
* gitbook init创建README.md,SUMMARY.md两个文档
* gitbook serve创建本地服务端，可以在浏览器实时观察
* gitbook build创建_book文件夹，生成静态网页

# 结构
* SUMMARY.md存放GitBook的文件目录信息
* book.json存放配置信息

# 插件安装
* 配置格式{"plugins": ["github"],

		"pluginsConfig": {
			"github": {
			"url": "https:github.com/wuyu1001"
			}
		}

}

* gitbook install安装插件