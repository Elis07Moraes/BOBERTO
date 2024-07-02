#!/usr/bin/env pybricks-micropython

# script.py
from titas_lib import HubType, RoboHub, SeguidorLinha, RoboBrick, RoboMotor, RoboCor, RoboUltrassonico, RoboBase, RoboImports

# DEFINIÇÕES
 
HubType(RoboHub.EV3BRICK)

# definindo as portas e o que cada coisa é
robo_brick = RoboBrick()

sensor_ultrassonico = RoboUltrassonico(Port="1")

cor_direita = RoboCor(Port="4")
cor_esquerda = RoboCor(Port="3")

motor_d = RoboMotor(Port="d")
motor_e = RoboMotor(Port="a")

sensorLinha = type.getImports().getLUMPDevice(port="2") 

codigoSeguidor = SeguidorLinha()


sensorLinha.read(0)[0]

base = RoboBase(  # passando as informações do robo p uma variavel
    motorDireito= motor_d,
    motorEsquerdo= motor_e,
    diametroRoda= 32,
    distanciaEntreAsRodas= 140
    )

# VARIAVEIS

# para andar enquanto a distancia for maior que 100 
# quando for menor que 100, ira parar lentamente 
distancia = 1000


# FUNÇÕES

while distancia > 100:
    motor_d.moverPorPotencia(potencia=100)
    motor_e.moverPorPotencia(potencia=-100)
    distancia = sensor_ultrassonico.pegarDistancia()
    print (distancia)
    motor_d.paraMotorLentamente()
    motor_e.paraMotorLentamente()

# seguir linha
#  base.moverSemParar(velocidade=100, angulo_curvatura=0)


# WHILE TRUE

# vai parar quando for branco e depois seguir reto ate encontrar preto, e quando isso acontecer, vai seguir reto
while True:
    cor_direita = cor_direita.pegarCor()
    cor_esquerda = cor_esquerda.pegarCor()
    motor_d.moverPorPotencia(potencia=100)
    motor_e.moverPorPotencia(potencia=-100)

    if (cor_esquerda > 30 and cor_direita > 30):
        motor_e.moverPorPotencia(-100)
        motor_d.moverPorPotencia(100)

    else: 
        codigoSeguidor.seguirLinhaPreta(
    kd=10,
    kp=8,
    cor_vermelha_direta=cor_direita.pegarCor(),
    cor_vermelha_esquerda=cor_esquerda.pegarCor(),
    motor_direito=motor_d,
    motor_esquerdo=motor_e,
    potencia_motores=100
    )