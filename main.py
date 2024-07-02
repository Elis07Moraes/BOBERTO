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
motor_e = RoboMotor(Port="a", reverse= True)

sensor_vendra = hub_type.getImports().getLUMPDevice(Port="1") 

codigoSeguidor = SeguidorLinha()

# print(sensor_vendra.read(0))

base = RoboBase(  # passando as informações do robo p uma variavel
    motorDireito= motor_d,
    motorEsquerdo= motor_e,
    diametroRoda= 46,
    distanciaEntreAsRodas= 140
    )

# VARIAVEIS

# para andar enquanto a distancia for maior que 100 
# quando for menor que 100, ira parar lentamente 
distancia = 1000

# FUNÇÕES

angulo_verificar = 180

def VerificarCorVE():
    return sensor_vendra.read(0)[1] 

def VerificarCorVD():
    return sensor_vendra.read(0)[2]

# def VerificarGap():
#     print("VerificarGap")
#     base.virarAngulo(angulo=angulo_verificar)
    
#     while angulo_verificar <= 180:
#         print("virarAngulo")
#     VerificarCorVD()
    
#     if VerificarCorVD() < 30 or VerificarCorVE() < 30:
#                     print("deu false") 
#     base.pararMotores()
#     print("pararMotorInstantaneamente")
#     return False
# print("entrou aqui")

# while angulo_verificar <= 2*angulo_verificar:
#     if VerificarCorVD() < 30 or VerificarCorVE() < 30:
#         print("deu false") 
#     return False
#     print("entrou aqui")
    
#     base.virarAngulo(angulo=-2* angulo_verificar)
#     base.pararMotores()
#     if VerificarCorVD() < 30 or VerificarCorVE() < 30: 
#         return False
    
#     base.virarAngulo(angulo=angulo_verificar)
    return True

def VerificarGap(): # consertar aqui, colocar para verificar enquanto vira
    print("VerificarGap")
    base.virarAngulo(angulo=angulo_verificar)
    print("virarAngulo")
    base.pararMotores()
    print("pararMotorInstantaneamente")
    if VerificarCorVD() < 30 or VerificarCorVE() < 30:
        print("deu false") 
        return False
    print("entrou aqui")
    
    base.virarAngulo(angulo=-2* angulo_verificar)
    base.pararMotores()
    if VerificarCorVD() < 30 or VerificarCorVE() < 30: 
        return False
    
    base.virarAngulo(angulo=angulo_verificar)
    return True
    

def taNoGap():
     print("taNoGap")
     if VerificarGap() == True: 
        base.pararMotores()
        base.moverDistancia(150)
        base.pararMotores()
        return


def distanciaParar():
    # if distancia < 100:
        distancia = sensor_ultrassonico.pegarDistancia()
        print (distancia)
        motor_d.pararMotorInstantaneamente()
        motor_e.pararMotorInstantaneamente()
        return

# seguir linha
#  base.moverSemParar(velocidade=100, angulo_curvatura=0)

# WHILE TRUE

# vai parar quando for branco e depois seguir reto ate encontrar preto, e quando isso acontecer, vai seguir reto
while True:
    # motor_d.moverPorPotencia(potencia=70)
    # motor_e.moverPorPotencia(potencia=70)
    sensor_esq_vedra = VerificarCorVE()
    sensor_dir_vedra = VerificarCorVD()
    # distanciaParar()

    # if distancia < 100:
    #     distanciaParar()
    #     break

    # if (cor_direita.pegarCor()== hub_type.getImports().getColor().WHITE and
    #        cor_esquerda.pegarCor()== hub_type.getImports().getColor().WHITE):
    #     # motor_e.moverPorPotencia(-100)
    #     # motor_d.moverPorPotencia(100)
    #     motor_d.moverPorPotencia(potencia=100)
    #     motor_e.moverPorPotencia(potencia=-100)


    # elif (cor_direita.pegarCor()== hub_type.getImports().getColor().BLACK and
    #        cor_esquerda.pegarCor()== hub_type.getImports().getColor().BLACK):
    #      motor_d.pararMotorInstantaneamente()
    #      motor_e.pararMotorInstantaneamente()
    #      gap()
    #      break

# para quando ver verde: 
# quando cor esquerda
    # if cor_esquerda.pegarCor()== hub_type.getImports().getColor().GREEN:
    #     motor_d.moverPorPotencia(70)
    #     motor_e.moverPorPotencia(-70)

    # if cor_direita.pegarCor()== hub_type.getImports().getColor().GREEN:
    #     motor_d.moverDuranteUmTempo(70, 1) #priorizar distancia inves de tempo
    #     motor_e.moverDuranteUmTempo(70, 1)
    #     motor_d.moverParaUmAnguloSuavemente(70, 90)
    #     motor_e.pararMotorInstantaneamente()

    # sensor_vendra.read(0)
    # print(sensor_vendra.read(0))
        # if cor_esq.pegarReflexao() <= (10):
        # if cor_vendra(0)[1] <= 10:
    # if sensor_vendra.read(0)[1] <= (30):
    #     motor_d.moverPorPotencia(70)
    #     motor_e.moverPorPotencia(-70)
    #             # print (cor_vendra.read(0))
    #     #if cor_dir.pegarReflexao() <= (10):
    #     # if cor_vendra(0)[2] <= 10:
        
        #ta no branco
    if sensor_esq_vedra >= 70 and sensor_dir_vedra >= 70:
        print("entrou no gap")
        print(sensor_esq_vedra, sensor_dir_vedra)
        taNoGap()

    # else:
    #     motor_d.moverPorPotencia(70)
    #     motor_e.moverPorPotencia(70)
    #     print (sensor_vendra.read())

    else: 
        sensor_esq_vedra = VerificarCorVE()
        sensor_dir_vedra = VerificarCorVD()
        codigoSeguidor.seguirLinhaPreta(
    kd=1,
    kp=2,
    cor_vermelha_direta=sensor_esq_vedra,
    cor_vermelha_esquerda=sensor_dir_vedra,
    motor_direito=motor_d,
    motor_esquerdo=motor_e,
    potencia_motores=50
    )
