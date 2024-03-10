import requests
import base64

s = requests.Session()
s.get('http://mercury.picoctf.net:15614/')
cookie = s.cookies['auth_name']
print(cookie)
unb64 = base64.b64decode(cookie)
print(unb64)
unb64b = base64.b64decode(unb64)
print(unb64b)
for i in range(0,128):
    pos = i // 8 
    guessdec = unb64b[0:pos] + bytes([unb64b[pos] ^ (1 << (i % 8))]) + unb64b[pos+1:]
    quessencl = base64.b64encode(guessdec)
    guess=base64.b64encode(base64.b64encode(guessdec)).decode()
    r = requests.get('http://mercury.picoctf.net:15614/', cookies={'auth_name': guess})

    if 'pico' in r.text:
        print(r.text)
        break