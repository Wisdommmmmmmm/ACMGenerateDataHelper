import os
import zipfile
import subprocess
import configparser
from tkinter import messagebox

cf = configparser.ConfigParser()
#改配置文件config.ini,不要在这里改
#生成数据的程序名
generatename = "create.exe"
#标程程序名
standardname = "standard.exe"
#生成的输入数据文件名
inputname = "sample"
#生成的输入数据文件后缀
inputsuffix = "in"
#生成的输出数据文件名
outputname = "sample"
#生成的输出数据文件后缀
outputsuffix = "out"
#生成的压缩包名
archivename = "data"

def findfile(filename):
    list = os.listdir("./")
    for i in range(0, len(list)):
        path = os.path.join("./", list[i])
        if os.path.isfile(path):
            if (list[i] == filename):
                return True
    return False

def readconfig():
    if(not findfile("config.ini")):
        messagebox.showeinfo("提示", "找不到配置文件config.ini，请新建配置文件config.ini，参考网址https://github.com/Wisdommmmmmmm/ACMGenerateDataHelper")
    global cf
    cf.read("./config.ini")
    global generatename
    generatename = cf.get("File", "generatename")
    global standardname
    standardname = cf.get("File", "standardname")
    global inputname
    inputname = cf.get("File", "inputname")
    global inputsuffix
    inputsuffix = cf.get("File", "inputsuffix")
    global outputname
    outputname = cf.get("File", "outputname")
    global outputsuffix
    outputsuffix = cf.get("File", "outputsuffix")
    global archivename
    archivename = cf.get("File", "archivename")
    if(outputname+outputsuffix == inputname+inputsuffix):
        messagebox.showerror("错误", "输入和输出文件名称加后缀不能一样")
        os.exit(0)

def create(l, r):
    global inputname
    global inputsuffix
    global outputname
    global outputsuffix
    global generatename
    global standardname
    for num in range(l, r):
        inputfilename = inputname+str(num)+"."+inputsuffix
        outputfilename = outputname+str(num)+"."+outputsuffix
        subprocess.getoutput(generatename+" 1>"+inputfilename)
        subprocess.getoutput(standardname+" 0<"+inputfilename+" 1>"+outputfilename)

def compress(l, r):
    global archivename
    zip_name = archivename+".zip"
    zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for num in range(l, r):
        inputfilename = inputname + str(num) +"."+ inputsuffix
        outputfilename = outputname + str(num) +"."+ outputsuffix
        zp.write(os.path.join("./", inputfilename))
        os.remove(os.path.join("./", inputfilename))
        zp.write(os.path.join("./", outputfilename))
        os.remove(os.path.join("./", outputfilename))
    zp.close

def check():
    global generatename
    global standardname
    if(not findfile(generatename)):
        messagebox.showerror("错误", "找不到生成数据的程序"+generatename)
        os._exit(0)
    if (not findfile(standardname)):
        messagebox.showerror("错误", "找不到标程"+standardname)
        os._exit(0)

if __name__ == '__main__':
    readconfig()
    check()
    l = int(input("请输入数据文件编号起点:"))
    r = int(input("请输入数据文件编号终点:"))+1
    iscompress = int(input("请输入是否压缩(否:0,是:1):"))
    create(l, r)
    if iscompress == 1:
        compress(l, r)
