# 安装
brew install vim

# Vundle
vim扩展管理器  
用git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim进行安装

# 配置文档
## 在.vimrc文档进行配置，在顶部： 
set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

## 这样就完成了Vundle使用前的配置，打开Vim,运行下面命令：
	：PulginInatall  
一键自动下载所有插件

## 自动补全插件
YouCompleteMe(必须根据官方文档步骤进行安装)

## shortcut操作
* 按esc进入normal模式，可以进行键盘操作：
  
	w，e, $, h, j, k, l，gg, G属于移动操作  
	dd, r, x, de, 属于修改操作  
	：可以跳到地板进行命令操作  
	space键可以折叠代码  
* i, a, A, o, O从normal模式进入编译模式
* 按v,V,ctr+v三种方式进入可视化模式,该模式下可以进行复制，粘贴等操作： 
 
	y复制, p粘贴, >可以缩进, **最强大是=可以自动的全部缩进**，J可以把所选内容变成一行  
	ctr+v 进入可视化block模式，如：I-- [ESC] → 进入模式后通过移动键选择要插入那几行，然后I是插入，插入“--”，按ESC键来为每一行生效
	
* 按R进入REPLACE mode,该模式下可以进行替代修改

* 按u可以回到上一步操作
* 数字0移动到行头

