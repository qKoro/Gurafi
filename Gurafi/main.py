from pystyle import *
import time,sys,os
from ascii_gr import *
from hashlib import sha256

Anime.Fade(Center.Center(banner1), Colors.rainbow, Colorate.Diagonal, enter=True, interval=0.05)

print(Colorate.Diagonal(Colors.red_to_white, title1, 2))

entree: str = Write.Input(firstInput,Colors.blue_to_purple, interval=0.001)
sortie = Write.Input(secondInput, Colors.blue_to_purple, interval=0.001)
key = Write.Input(key, Colors.blue_to_purple, interval=0.001)
keys = sha256(key.encode('utf-8')).digest()
with open(entree, 'rb') as f_entree:
    with open(sortie, 'wb')as f_sortie:
        i = 0
        while f_entree.peek():
            c = ord(f_entree.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_sortie.write(b)
            i += 1
time.sleep(5)
Anime.Fade(Center.YCenter(finish + "\nPRESS ENTER TO EXIT"), Colors.yellow_to_red, Colorate.Horizontal, enter=True)

 
 

