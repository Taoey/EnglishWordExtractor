import IoUtil
import Mydic

if __name__ == '__main__':
    wList=IoUtil.getWords()
    for word in wList:
        restult = Mydic.getPhonetic(word["word"])
        if  restult:
            word["enPhonetic"]=restult["en"]
            word["amPhonetic"]=restult["am"]
            print(word)
