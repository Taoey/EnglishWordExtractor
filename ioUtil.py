import  re


filePath="data.txt"

def getWords0():
    fr = open(filePath, "r", encoding="UTF-8")
    fw = open(filePath, "w", encoding="UTF-8")

    str = fr.read()
    wList = re.findall(r"#.*", str)

    for a in wList:
        fw.write(a[1:] + "\n")
    fw.close()
    fr.close()

def getWorlds():
    fr=open(filePath,"r",encoding="UTF-8")
    str = fr.read()
    wList = re.findall(r"#.*", str)
    fr.close()
    return wList


