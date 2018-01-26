#测试文件

def testSplitWord():
    '''
    测试如何分割一个形如"a art.一(个)；每一(个)"的字符数据,将其化为键值对形式
    :return:
    '''
    wList=[]

    str="    a art.一(个)；每一(个)"
    str=str.lstrip() #去除字符左空格,lstrip()方法返回处理过后的字符串
    sList=str.split(" ",1)
    wdic={
        "word":sList[0],
        "Phonetic":"",
        "explain":sList[1]
    }
    wList.append(wdic)
    return wList


def dicEmpty():
    dic={"am":"12"}
    if dic:
        print("Y")
    else:
        print("N")


if __name__ == '__main__':
    dicEmpty()