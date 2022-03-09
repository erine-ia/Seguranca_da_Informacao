from threading import Thread
import time

def carro1(velocidade, piloto):
    trajeto = 0 #inicio trajeto por km
    while trajeto <= 100:
        print('Carro1: ',piloto,trajeto)
        trajeto += velocidade
        time.sleep(0)
        print('Piloto: {} Km: {}\n'.format(piloto, trajeto))


t_carro1 = Thread(target = carro1, args = [1, 'Um'])
t_carro2 = Thread(target = carro1, args = [1.5, 'Dois'])

t_carro1.start()
t_carro2.start()
