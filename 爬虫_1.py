#-*- coding:UTF-8 -*-
import requests

def get_one_page(url):
    try:
        #headers='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            print(response.encoding)
            print(response.apparent_encoding)
            r=response.text
            print(requests.utils.get_encodings_from_content(r)[0])
            a=r.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(r)[0])
            print(a)
            b=r.encode('ISO-8859-1').decode(response.apparent_encoding)
            print(b)
        return None
    except RequestException:
        return None

def main():
    url = 'http://www.biqukan.com/1_1094/5403177.html'
    get_one_page(url)

if __name__=='__main__':
    main()
    #target = 'http://www.biqukan.com/1_1094/5403177.html'
    #req = requests.get(url=target)
    #print(req.text)
