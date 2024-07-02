#!/usr/bin/env pybricks-micropython

# script.py
from titas_lib import HubType, RoboHub, SeguidorLinha, RoboBrick, RoboMotor, RoboCor, RoboUltrassonico, RoboBase, RoboImports, Color

# DEFINIÇÕES

hub_type = HubType(RoboHub.EV3BRICK)

robo_brick = RoboBrick()

sensor_ultrassonico = RoboUltrassonico(Port="2")

cor_direita = RoboCor(Port="4")
cor_esquerda = RoboCor(Port="3")

motor_d = RoboMotor(Port="d")
motor_e = RoboMotor(Port="a")

sensor_vendra = hub_type.getImports().getLUMPDevice(Port="1") 

codigoSeguidor = SeguidorLinha()

print(sensor_vendra.read(0))

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

def gap():
    motor_d.moverDuranteUmTempo(2)
    motor_e.pararMotorInstantaneamente()
    motor_e.moverDuranteUmTempo(4)
    motor_d.pararMotorInstantaneamente()


def distanciaParar():
    # if distancia < 100:
        distancia = sensor_ultrassonico.pegarDistancia()
        print (distancia)
        motor_d.pararMotorInstantaneamente()
        motor_e.pararMotorInstantaneamente()

# seguir linha
#  base.moverSemParar(velocidade=100, angulo_curvatura=0)

# WHILE TRUE

# vai parar quando for branco e depois seguir reto ate encontrar preto, e quando isso acontecer, vai seguir reto
while True:
    motor_d.moverPorPotencia(potencia=100)
    motor_e.moverPorPotencia(potencia=-100)
    # distanciaParar()

    # if distancia < 100:
    #     distanciaParar()
    #     break

    if (cor_direita.pegarCor()== hub_type.getImports().getColor().WHITE and
           cor_esquerda.pegarCor()== hub_type.getImports().getColor().WHITE):
        # motor_e.moverPorPotencia(-100)
        # motor_d.moverPorPotencia(100)
        motor_d.moverPorPotencia(potencia=100)
        motor_e.moverPorPotencia(potencia=-100)


    elif (cor_direita.pegarCor()== hub_type.getImports().getColor().BLACK and
           cor_esquerda.pegarCor()== hub_type.getImports().getColor().BLACK):
         motor_d.pararMotorInstantaneamente()
         motor_e.pararMotorInstantaneamente()
         gap()
         break
        # if cor_esquerda.pegarCor()== hub_type.getImports().getColor().GREEN:
        #     motor_d.moverPorPotencia(70)
        #     motor_e.moverPorPotencia(70)

        # if cor_direita.pegarCor()== hub_type.getImports().getColor().GREEN:
        #     motor_d.moverPorPotencia(-70)
        #     motor_e.moverPorPotencia(-70)

        # sensor_vendra.read(0)
        # print(sensor_vendra.read(0))
        # # if cor_esq.pegarReflexao() <= (10):
        # # if cor_vendra(0)[1] <= 10:
        # if sensor_vendra.read(0)[1] <= (20):
        #         motor_d.moverPorPotencia(-70)
        #         motor_e.moverPorPotencia(-70)
        #         # print (cor_vendra.read(0))
        # #if cor_dir.pegarReflexao() <= (10):
        # # if cor_vendra(0)[2] <= 10:
        
        # elif sensor_vendra.read(0)[2] <= (20):
        #         motor_d.moverPorPotencia(70)
        #         motor_e.moverPorPotencia(70)

        # else:
        #         motor_d.moverPorPotencia(70)
        #         motor_e.moverPorPotencia(-70)
        #         # print (cor_vendra.read())

    else: 
        codigoSeguidor.seguirLinhaPreta(
    kd=10,
    kp=8,
    cor_vermelha_direta=cor_direita.pegarCor()== hub_type.getImports().getColor(),
    cor_vermelha_esquerda=cor_esquerda.pegarCor()== hub_type.getImports().getColor(),
    motor_direito=motor_d,
    motor_esquerdo=motor_e,
    potencia_motores=100
    )
