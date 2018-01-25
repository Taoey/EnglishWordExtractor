import urllib.request
import json

class dic:
    #金山词霸的API的key
    key = "B02371606E81A113AEB37D8DB0C5194E"
    def getAllData(word):
        url = "http://dict-co.iciba.com/api/dictionary.php?w={}&key={}&type=json".format(word, dic.key)
        response = urllib.request.urlopen(url).read().decode('utf8')
        getJson = json.loads(response)
        return getJson

    def getPhonetic(word):
        url = "http://dict-co.iciba.com/api/dictionary.php?w={}&key={}&type=json".format(word, dic.key)
        response = urllib.request.urlopen(url).read().decode('utf8')
        jsonData = json.loads(response)
        am = jsonData["symbols"][0]["ph_am"]
        en = jsonData["symbols"][0]["ph_en"]
        result="/en:{}/,am:/{}/".format(en,am)
        return  result

    # if __name__ == '__main__':
    #     jsonData=getData("hello")
    #     am = jsonData["symbols"][0]["ph_am"]
    #     en = jsonData["symbols"][0]["ph_en"]
    #     result="/en:{}/,am:/{}/".format(en,am)
    #     print(result)

