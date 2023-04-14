# AutoDownloader_Bot
一个解析并下载全网视频的Python爬虫.

目前编写正在进行中,现有代码不在main分支,会在代码稳定之后再merge.

## 关于针对不同网站的下载脚 框架/函数/脚本
对于不同的网站,请创建对应branch,并由一个人开发,其他人未经允许,严禁修改  
任何脚本应在开头前两行加上关于编程语言和编码的注释  
如`#! usr/bin/python3`  
`#coding:UTF-8`

## 编码规范

由于Python的特殊格式,请在每个函数末尾加上 函数名+END注释方便查看  
注释尽量对齐,且注释应约占代码的25%以上  
应在每个具有复杂功能的代码段前一行写注释表明功能  
每个代码断间应空一行

### 关于变量命名标准
C/C++所有变量在赋值前应先在代码段或函数开头定义并初始化  
所有单词见用"_"隔开,如: file_name  
如果变量名是缩写,应在函数开头和初始化时注释全称和作用  
全局变量名 全大写  
局部变量名 全小写  
类名 开头字母大写,其余全小写  
字典前应加前缀"dic_"  
列表前应加前缀"lst_"  
变量名 i,j,k仅限迭代时使用  
变量名 a,b,c,d,e,f,g,h,m,n,x,y,z仅限在数学公式或计算中使用  


### Python编码规范
本仓库中的Python代码请严格遵照[PEP 8文档](https://peps.python.org/pep-0008/)以及[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).包含未按照代码规范编写的Python代码的PR会被无理由Close(事实上只要代码没问题作者还是会merge并之后帮你改一下的).  
对于非Python程序最好可以遵守[Google Style Guide](https://google.github.io/styleguide/).  
.

## 联系作者
E-mail:`hrhszsdtc@gmail.com`  
E-mail:`ZZH20081023@163.com`
## 捐助
BTC:`3J5DfkjrHLxLRwMyeNHfhDd3GxTAo8yRAJ`

## 免责声明
仅供学习使用,滥用后果自负!
