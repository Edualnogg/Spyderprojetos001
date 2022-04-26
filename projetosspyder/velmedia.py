# programa que calcula a  velocidade média v(m/s) e s(m)

class vel_media:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def velocidade(vel):  # método para calcular a VELOCIDADE (x= distancia e y= tempo)
        return (vel.x/vel.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(dist):  # método para calcular a DISTANCIA (x= velocidade e y= tempo)
        return (dist.x * dist.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tempo(temp):  # método para calcular o TEMPO (x= distancia e y= velocidade)
        return (temp.x/temp.y)


# AQUI É SÓ COLOCAR AS VARIÁVEIS
teste = vel_media(50, 10)
print(teste.distancia())
# print(teste.velocidade())
# print(teste.tempo())


### EU PODERIA USAR APENAS 1 '__init__', DEIXARIA O CÓDIGO MAIS LIMPO
