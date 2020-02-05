import requests

url = 'http://127.0.0.1:8000/api/rfidregister'
myobj = {'rrn': '171291601102','RFID':'171291601102'}

x = requests.post(url, data = myobj)

print(x.text)
