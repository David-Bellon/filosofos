import threading
import time
from random import randint as rd


n = 5

class Filosofo(threading.Thread):
    lock = threading.Lock()
    tenedores = []
    count = 0
    estado = []
    def __init__(self):
        super().__init__()
        self.id = Filosofo.count
        self.veces_comida = 0
        Filosofo.estado.append("Pensando")
        Filosofo.count += 1
        Filosofo.tenedores.append(threading.Semaphore(0))
        print("Filosofo {0} pensando".format(self.id))

    def pensar(self):
        time.sleep(rd(1, 3))

    def izquierda(self):
        return (self.id + 1) % n
    
    def derecha(self):
        return (self.id - 1) % n
    
    def comer(self):
        if Filosofo.estado[self.id] == "Hambriento" and Filosofo.estado[self.izquierda()] != "Comiendo" and Filosofo.estado[self.derecha()] != "Comiendo":
            Filosofo.estado[self.id] = "Comiendo"
            print("Filosofo {0} comiendo".format(self.id))
            time.sleep(rd(1, 3))
            self.veces_comida += 1
            print("Filosofo {0} deja de comer".format(self.id))
            

    def querer(self):
        Filosofo.estado[self.id] = "Hambriento"

    def parar_comer(self):
        Filosofo.estado[self.id] = "Pensando"
        print("Filosofo {0} pensando".format(self.id))

    def run(self):
        while self.veces_comida != 3:
            self.pensar()
            self.querer()
            self.comer()
            self.parar_comer()

    def __del__(self):
        
        print("Filosofo " + str(self.id) + " comido " + str(self.veces_comida) + "/3")

def main():
    lista = []
    for i in range(5):
        lista.append(Filosofo())

    for i in lista:
        i.start()

    for i in lista:
        i.join()

if __name__=="__main__":
    start = time.time()
    main()
    print("Tiempo transcurrido " + str(time.time() - start))