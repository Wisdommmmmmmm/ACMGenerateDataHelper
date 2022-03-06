# ACMGenerateDataHelper
## 简介
这是一个用来帮助算法出题人简化生成数据流程的脚本集合。
## 功能
***GenerateDataFile.exe***  
通过生成输入数据的程序以及标程生成多个输入输出数据文件，可以自定义生成数据文件的编号范围，还可以选择是否压缩  
***Compress.exe***  
根据配置文件里的数据文件格式，将所有数据文件压缩成一个zip压缩包  
## 配置
配置文件***config.ini***  
***generatename***:生成输入数据的程序名  
***standardname***:标程程序名  
***inputname***:生成的输入数据文件名  
***inputsuffix***:生成的输入数据文件后缀  
***outputname***:生成的输出数据文件名  
***outputsuffix***:生成的输出数据文件后缀  
***archivename***:压缩后的压缩包名  
## 使用环境
### 操作系统 
Windows 10
## 使用方法
1.配置config.ini文件；  
2.将生成输入数据的代码(不要带文件输入输出)编译成exe程序，名字和配置里一样；    
3.将标程代码(不要带文件输入输出)编译成exe程序，名字和配置里一样；  
4.将步骤2和步骤3中的程序放到GenerateDataFile.exe一个文件目录；  
5.双击GenerateDataFile.exe，输入生成数据文件编号的起点和终点，选择是否压缩，生产输入输出数据文件；  
6.如果还需要压缩输入输出数据文件，可以双击Compress.exe对同一目录下的输入输出文件进行压缩。
