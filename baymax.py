# cording:utf-8
import os, time

msg="Hello. I am Baymax, Your Personal Healthcare Companion."
url ='"'+'http://translate.google.com/translate_tts?tl=en&q='+msg+'"'
#url='"http://translate.google.com/translate_tts?tl=en&q=HelloImbaymax"'
cmd = 'mplayer '+url

def main():
    os.system('irsend SEND_ONCE LED on')
    os.system('irsend SEND_ONCE LED w')
    os.system(cmd)
    time.sleep(0.5)
    os.system('irsend SEND_ONCE LED off')

main()
