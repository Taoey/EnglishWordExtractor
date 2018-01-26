import  re


filePath="datas/data.txt"

def getWords0():
    '''
    文件读写测试,实际开发用不到
    :return:
    '''
    fr = open(filePath, "r", encoding="UTF-8")
    fw = open(filePath, "w", encoding="UTF-8")

    str = fr.read()
    wList = re.findall(r"#.*", str)

    for a in wList:
        fw.write(a[1:] + "\n")
    fw.close()
    fr.close()

def getWords():
    '''
    获取带有标记的单词列表(数据格式为:"#about prep.关于；在…周围"),将其转化为字典数据数组
    :return:
    '''
    resultList=[]
    fr=open(filePath,"r",encoding="UTF-8")
    strData = fr.read()
    words = re.findall(r"#.*", strData)
    for word in words:
        word = word[1:]  # 去除数据的标记
        word = word.lstrip()  # 去除字符左空格,lstrip()方法返回处理过后的字符串
        wordSpilt = word.split(" ", 1)
        wdic = {
            "word": wordSpilt[0],
            "enPhonetic": "",
            "amPhonetic":"",
            "explain": wordSpilt[1]
        }
        resultList.append(wdic)
    fr.close()
    return resultList



# if __name__ == '__main__':
#
#     datas=getWorlds()
#     print(datas)
#     pass


