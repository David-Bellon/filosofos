import keyboard
import time

file = r"C:\Users\dadbc\Desktop\Phy\Repositorios\filosofos\texto.txt"
f = open(file, "w")
activation = time.time()
while True:
    a = keyboard.read_key()
    if time.time() >= activation + 10:
        break
    f.write(a)
    f.write(" ")
f.close()