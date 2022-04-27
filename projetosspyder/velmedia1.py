# CÓDIGO DA VELOCIDADE MÉDIA MAIS OTIMIZADO

class vel_media:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def velocidade(vel):  # método para calcular a VELOCIDADE (x= distancia e y= tempo)
        return (vel.x/vel.y)

    def distancia(dist):  # método para calcular a DISTANCIA (x= velocidade e y= tempo)
        return (dist.x * dist.y)

    def tempo(temp):  # método para calcular o TEMPO (x= distancia e y= velocidade)
        return (temp.x/temp.y)


teste = vel_media(100, 23)
print(teste.velocidade())
