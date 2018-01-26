import urllib.request
import json

#金山词霸的API的key
key = "B02371606E81A113AEB37D8DB0C5194E"
def getAllData(word):
    url = "http://dict-co.iciba.com/api/dictionary.php?w={}&key={}&type=json".format(word, key)
    response = urllib.request.urlopen(url).read().decode('utf8')
    getJson = json.loads(response)
    return getJson

def getPhonetic(word):
    '''
    获取一个单词的音标
    :return:
    '''
    url = "http://dict-co.iciba.com/api/dictionary.php?w={}&key={}&type=json".format(word, key)
    response = urllib.request.urlopen(url).read().decode('utf8')
    jsonData = json.loads(response)
    dic={}
    try:
        am = jsonData["symbols"][0]["ph_am"]
        en = jsonData["symbols"][0]["ph_en"]
        dic={
            "am":"/{}/".format(am),
            "en":"/{}/".format(en)
        }
    except:
        print("异常:"+jsonData)
    return  dic

# if __name__ == '__main__':
#     jsonData=getData("hello")
#     am = jsonData["symbols"][0]["ph_am"]
#     en = jsonData["symbols"][0]["ph_en"]
#     result="/en:{}/,am:/{}/".format(en,am)
#     print(result)

