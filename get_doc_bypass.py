# with open("1.txt", 'r', encoding='utf') as f:
#     read_data = f.read()
#     text = read_data

import requests
import time,sys,os
print("Tool make by vha")
x = input('enter url doc:')




text = requests.get(x)


loading = "VHA - Loading: [----------]"
for i in range(101):
    
    time.sleep(0.001)
    sys.stdout.write("\r"+loading+" %d%%" % i)
    if i == 10 or i == 20 or i == 30 or i == 40 or i == 50 or i == 60 or i == 70 or i == 80 or i == 90 or i == 100:
        loading = loading.replace("-","=",1)
        os.system('cls')
    sys.stdout.flush()

text=text.text


t = text.count('<script type="text/javascript" nonce="')

vanban = ""
for i in range(4,t):
  if(i%2==0):
    vanban += text.split('<script type="text/javascript" nonce="')[i].split('"')[10].replace("\\n", "\n").replace("\\t", " ").replace("\\u003d", "=").replace("\\u003e", ">").replace("\\u003c", "<")
    print(vanban)

