import requests

def get_data():
    url = "http://bitdog.me/api/bitcoin"
    #bitcoin是比特币的英文名，获取其他币种价格可以在bitdog.me查询
    s = requests.Session()
    string = s.get(url).content.decode('utf-8')
    s.close()
    return string

if __name__ == '__main__':
    d = get_data()
    print(d)