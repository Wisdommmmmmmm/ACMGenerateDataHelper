import os
import zipfile
import configparser
from tkinter import messagebox

cf = configparser.ConfigParser()
inputsuffix = "in"
outputsuffix = "out"
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
    if (not findfile("config.ini")):
        messagebox.showinfo("提示", "找不到配置文件config.ini，请新建配置文件config.ini，参考网址https://github.com/Wisdommmmmmmm/ACMGenerateDataHelper")
    global cf
    cf.read("./config.ini")
    global inputsuffix
    inputsuffix = cf.get("File", "inputsuffix")
    global outputsuffix
    outputsuffix = cf.get("File", "outputsuffix")
    global archivename
    archivename = cf.get("File", "archivename")

def compress():
    global inputsuffix
    global outputsuffix
    global archivename
    zip_name = archivename + ".zip"
    zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    list = os.listdir("./")
    for i in range(0, len(list)):
        path = os.path.join("./", list[i])
        if os.path.isfile(path):
            if((inputsuffix in list[i] or outputsuffix in list[i]) and ("ini" not in list[i]) and ("exe" not in list[i])and("py" not in list[i])):
                zp.write(path)
                os.remove(path)
    zp.close()

if __name__ == '__main__':
    readconfig()
    compress()

