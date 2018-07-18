#coding=utf8
#start
import requests
import itchat
import itchat, time
from PIL import ImageFilter
import matplotlib.pyplot as plt  
from itchat.content import *

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'Silverwings',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
      
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    defaultReply = msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

@itchat.msg_register([RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register([PICTURE])
def download_files(msg):
    msg.download(msg.fileName)
    print(msg.fileName)
    im02 = plt.imread(msg.fileName)
    im = im02.filter(ImageFilter.CONTOUR)
    im.save(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

itchat.auto_login(hotReload = True)
itchat.run()
