#!/usr/bin/env pybricks-micropython

# script.py
from titas_lib import HubType, RoboHub, SeguidorLinha, RoboBrick, RoboMotor, RoboCor, RoboUltrassonico, RoboBase, RoboImports, Color
from pybricks.tools import wait 
import os 

# DEFINIÇÕES

hub_type = HubType(RoboHub.EV3BRICK)

robo_brick = RoboBrick()

sensor_ultrassonico = RoboUltrassonico(Port="2")

cor_direita = RoboCor(Port="4")
cor_esquerda = RoboCor(Port="3")

motor_d = RoboMotor(Port="d")
motor_e = RoboMotor(Port="a", reverse = True)
#motor_garra = RoboMotor(Port="b", reverse= True)

sensor_vendra = hub_type.getImports().getLUMPDevice(Port="1") 

codigoSeguidor = SeguidorLinha()

# print(sensor_vendra.read(0))

base = RoboBase(  # passando as informações do robo p uma variavel
    motorDireito= motor_d,
    motorEsquerdo= motor_e,
    diametroRoda= 44,
    distanciaEntreAsRodas= 320
    )

# VARIAVEIS

# para andar enquanto a distancia for maior que 100 
# quando for menor que 100, ira parar lentamente 
distancia = 1000

angulo_verificar = 10

viradaAngulo = 0

BRANCO = 65

PRETO = 35

pretoEsqCor = 1

brancoEsqCor = 2

pretoDirCor = 3

brancoDirCor = 4

BRANCODIR = 52

BRANCOESQ = 52

PRETODIR = 10 

PRETOESQ = 10

contadorGap = 0

seguindoLinha = True

distanciaArea = 1000

# FUNÇÕES

def VerificarCorVE():
    return sensor_vendra.read(0)[1] 

def VerificarCorVEEx():
    return sensor_vendra.read(0)[0] 

def VerificarCorVD():
    return sensor_vendra.read(0)[2]

def VerificarCorVDEx():
    return sensor_vendra.read(0)[3]

def beep(frequencia: int, duracao: int):  #Função de Beep
      comando = "beep -f " + str(frequencia) + " -l " + str(duracao) + " &"
      os.system(comando)

def TudoPreto():
    if sensor_dir_vedra <= PRETO and sensor_dirEx_vedra <= PRETO and sensor_esq_vedra <= PRETO and sensor_esqEx_vedra <= PRETO:
        base.moverDistancia(50)
        base.pararMotores()

def alinharLinha():
        i=0
        base.pararMotores()
        while i < 100:
            sensor_esqEx_vedra = VerificarCorVEEx()
            sensor_esq_vedra = VerificarCorVE() 
            sensor_dirEx_vedra = VerificarCorVDEx()
            sensor_dir_vedra = VerificarCorVD()
            codigoSeguidor.seguirLinhaPreta(
            kd=0.5, # analisa de acordo com a poisçao do começo
            kp=1, # proporcional no momento instante que ocorre o erro
            cor_vermelha_direta=(sensor_esq_vedra + sensor_esqEx_vedra * 3) - 20,
            cor_vermelha_esquerda=sensor_dir_vedra + sensor_dirEx_vedra * 3,
            motor_direito=motor_d,
            motor_esquerdo=motor_e,
            potencia_motores=0
            )
            i=i+1
            wait(10)

def eVermelhoD(): # funcao para pegar a cor vermelha do lado direito usando sistema rgb, usando verde e azul p comparacao
    cor = cor_direita.pegarRGB()
    # print(cor)
    if cor[0] > 35 and cor[0] < 57:
        if cor[0] >= (2 * cor[1]) or cor[0] >= (2 * cor[2]):
            return True
        
def eVermelhoE(): # funcao para pegar a cor vermelha do lado esquerda usando sistema rgb, usando verde e azul p comparacao
    cor = cor_direita.pegarRGB()
    # print(cor)
    if cor[0] > 35 and cor[0] < 57:
        if cor[0] >= (2 * cor[1]) or cor[0] >= (2 * cor[2]):
            return True
        


def eVerdeD(): # funcao para pegar a cor verde do lado direito usando sistema rgb, usando verde e vermelho p comparacao
    cor = cor_direita.pegarRGB()
    # print(cor)
    if cor[1] > 10 and cor[1] < 57:
        if cor[1] >= (2 * cor[0]):
            return True
        
    return False

def eVerdeE(): # funcao para pegar a cor verde do lado esquerda usando sistema rgb, usando verde e vermelho p comparacao
    cor = cor_esquerda.pegarRGB()
    # print(cor) 
    if cor[1] > 12 and cor[1] < 65:
        if cor[1] >= (2 * cor[0]):
            return True
        
    return False



# funcao para mover para esquerda quando ver verde
def VerdeEsquerda():
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dir_vedra = VerificarCorVD()
    print ("mover")
    base.moverDistancia(80)
    # base.virar90grausDireita()
    base.virarAngulo(-90)
    base.pararMotores()

    while sensor_esq_vedra >= BRANCO or sensor_dir_vedra >= BRANCO: 
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dir_vedra = VerificarCorVD()
        base.virarAngulo(-10)
        print(" branco virar verde esq")


        if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
            sensor_esq_vedra = VerificarCorVE() 
            sensor_dir_vedra = VerificarCorVD()
            print("achou preto esq") 
            break


# funcao para mover pra direita quando for verde
def VerdeDireita():
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dir_vedra = VerificarCorVD()
    print ("mover")
    base.moverDistancia(80)
    # base.virar90grausEsquerda()
    base.virarAngulo(90)
    base.pararMotores()
    while sensor_esq_vedra >= BRANCO or sensor_dir_vedra >= BRANCO:
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dir_vedra = VerificarCorVD()
        print(" branco virar verde") 
        base.virarAngulo(10)
        
        if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
            sensor_esq_vedra = VerificarCorVE() 
            sensor_dir_vedra = VerificarCorVD() 
            print("achou preto")
            break

def VerificarCorVE():
    return sensor_vendra.read(0)[2] 

def VerificarCorVEEx():
    return sensor_vendra.read(0)[3] 

def VerificarCorVD():
    return sensor_vendra.read(0)[1]

def VerificarCorVDEx():
    return sensor_vendra.read(0)[0]

# realiza verificacao se é gap o nao, se nao achar nada no final, retorna True e começa a realizar o gap
def VerificarGap():
    global angulo_verificar
    viradaMaxima = 10
    base.moverDistancia(10)

    print("VerificarGap")  
    viradaAngulo = 0

    while viradaAngulo <= viradaMaxima:
        
        base.virarAngulo(angulo=- angulo_verificar)
        viradaAngulo += 1
        print("virarAngulo")
    
        if VerificarCorVD() < PRETO or VerificarCorVE() < PRETO:
            print("deu false") 
            base.pararMotores()
            print("pararMotorInstantaneamente")      
            return False

    print("entrou aqui")

    while viradaAngulo >= -viradaMaxima:
        base.virarAngulo(angulo= angulo_verificar)
        viradaAngulo -= 1
        print("virarAngulo")            

        if VerificarCorVD() < PRETO or VerificarCorVE() < PRETO:
            print("deu false") 
            base.pararMotores()
            return False
        print("entrou aqui")    


    base.virarAngulo(angulo=( viradaMaxima* - angulo_verificar))
    # base.virar90grausDireita()
    return True   

# quando entra no gap
def taNoGap():
     global contadorGap
     print("taNoGap")
    #  if VerificarGap() == True: 
     base.pararMotores()
     base.moverDistancia(100)
     base.pararMotores()
     sensor_esqEx_vedra = VerificarCorVEEx()
     sensor_esq_vedra = VerificarCorVE() 
     sensor_dirEx_vedra = VerificarCorVDEx()
     sensor_dir_vedra = VerificarCorVD()

     if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
        motor_d.pararMotorInstantaneamente()
        motor_e.pararMotorInstantaneamente()
        print ("resetei contador")
        contadorGap = 0
        return False
     
     base.moverDistancia(100)
     base.pararMotores()
     Gap2()
     base.pararMotores()

    #  while sensor_esq_vedra >= 70 and sensor_dir_vedra >= 70:
    #     base.moverDistancia(100)
    #     base.pararMotores()

# funcao que pegab a distancia do sensor ultrasspnico, e quando a distancia (anteriprmente 1000) for menor que 50, ele printa a disytancia e para
def Distancia():
    distancia = sensor_ultrassonico.pegarDistancia()
    if distancia < 50:
        print (distancia)
        base.pararMotores()
        if distancia < 50: 
            return True 

# fncao para desviar do obstaculo
# def Obstaculo():
#     sensor_esq_vedra = VerificarCorVE() 
#     sensor_dir_vedra = VerificarCorVD()
#     if Distancia() == True: 
#         print ("obstaculo")
#         alinharLinha()
#         base.moverDistancia(-50)
#         base.pararMotores()
#         base.virarAngulo(-90)
#         base.pararMotores()
#         base.moverDistancia(350)
#         base.pararMotores()
#         base.virarAngulo(90)
#         base.pararMotores()
#         sensor_esq_vedra = VerificarCorVE() 
#         sensor_dir_vedra = VerificarCorVD()
#         base.moverDistancia(680)
#         base.pararMotores()
#         base.virarAngulo(90)
#         sensor_esq_vedra = VerificarCorVE() 
#         sensor_dir_vedra = VerificarCorVD()
#         while sensor_dir_vedra > PRETO and sensor_esq_vedra > PRETO:
#             print(sensor_dir_vedra, sensor_esq_vedra)
#             base.moverSemParar(100, 0)
#             sensor_esq_vedra = VerificarCorVE() 
#             sensor_dir_vedra = VerificarCorVD()
#             cor_esquerda.pegarRGB()
#             cor_direita.pegarRGB()
#             sensor_esq_vedra = VerificarCorVE() 
#             sensor_dir_vedra = VerificarCorVD()
#             if sensor_esq_vedra <= PRETO or sensor_dir_vedra <= PRETO:
#                 print("preto obstaculo")
#                 cor_esquerda.pegarRGB()
#                 cor_direita.pegarRGB()
#                 sensor_esq_vedra = VerificarCorVE() 
#                 sensor_dir_vedra = VerificarCorVD()  
#                 base.moverDistancia(100)
#                 if sensor_esq_vedra <= PRETO or sensor_dir_vedra <= PRETO:
#                     cor_esquerda.pegarRGB()
#                     cor_direita.pegarRGB()
#                     sensor_esq_vedra = VerificarCorVE() 
#                     sensor_dir_vedra = VerificarCorVD()               
#                     base.pararMotores()
#                     wait(100)
#                     base.moverDistancia(50)
#                     base.pararMotores()
#                     base.virarAngulo(-90)
#                     base.pararMotores()
#                 break

def Obstaculo(): # direita 
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dir_vedra = VerificarCorVD()
    if Distancia() == True: 
        print ("obstaculo")
        alinharLinha()
        base.moverDistancia(-50)
        base.pararMotores()
        base.virarAngulo(90)
        base.pararMotores()
        base.moverDistancia(350)
        base.pararMotores()
        base.virarAngulo(-90)
        base.pararMotores()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dir_vedra = VerificarCorVD()
        base.moverDistancia(680)
        base.pararMotores()
        base.virarAngulo(-90)
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dir_vedra = VerificarCorVD()
        while sensor_dir_vedra > PRETO and sensor_esq_vedra > PRETO:
            print(sensor_dir_vedra, sensor_esq_vedra)
            base.moverSemParar(100, 0)
            sensor_esq_vedra = VerificarCorVE() 
            sensor_dir_vedra = VerificarCorVD()
            cor_esquerda.pegarRGB()
            cor_direita.pegarRGB()
            sensor_esq_vedra = VerificarCorVE() 
            sensor_dir_vedra = VerificarCorVD()
            if sensor_esq_vedra <= PRETO or sensor_dir_vedra <= PRETO:
                print("preto obstaculo")
                cor_esquerda.pegarRGB()
                cor_direita.pegarRGB()
                sensor_esq_vedra = VerificarCorVE() 
                sensor_dir_vedra = VerificarCorVD()  
                base.moverDistancia(100)
                if sensor_esq_vedra <= PRETO or sensor_dir_vedra <= PRETO:
                    cor_esquerda.pegarRGB()
                    cor_direita.pegarRGB()
                    sensor_esq_vedra = VerificarCorVE() 
                    sensor_dir_vedra = VerificarCorVD()               
                    base.pararMotores()
                    wait(100)
                    base.moverDistancia(50)
                    base.pararMotores()
                    base.virarAngulo(90)
                    # base.moverDistancia(-20)
                    base.pararMotores()
                break

def NoventaGrausD(): 
    sensor_esq_vedra = VerificarCorVE() # definindo variveis 
    sensor_dir_vedra = VerificarCorVD()
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_esqEx_vedra = VerificarCorVEEx()
    cor_direita.pegarRGB()
    cor_esquerda.pegarRGB()
    if sensor_dir_vedra <= PRETO - 25 and sensor_dirEx_vedra <= PRETO - 20 and sensor_esq_vedra >= BRANCO - 5 and sensor_esqEx_vedra >= BRANCO and cor_direita.pegarRGB()[0] >= (BRANCODIR) or cor_esquerda.pegarRGB( )[0] >= (BRANCOESQ):
        base.moverDistancia(-10)
        base.pararMotores()
        sensor_esq_vedra = VerificarCorVE() # definindo variveis 
        sensor_dir_vedra = VerificarCorVD()
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_esqEx_vedra = VerificarCorVEEx()
        cor_direita.pegarRGB()
        cor_esquerda.pegarRGB()
        wait(20)
        if sensor_dir_vedra <= PRETO - 25 and sensor_dirEx_vedra <= PRETO - 20 and sensor_esq_vedra >= BRANCO - 5 and sensor_esqEx_vedra >= BRANCO and cor_direita.pegarRGB()[0] >= (BRANCODIR) or cor_esquerda.pegarRGB()[0] >= (BRANCOESQ ):
            print ("noventa grau dir")
            base.moverDistancia(117)
            base.moverDistancia(-50)
            base.virar90grausDireita()
            base.pararMotores()
            return True
    return False


def NoventaGrausE(): 
    sensor_esq_vedra = VerificarCorVE() # definindo variveis 
    sensor_dir_vedra = VerificarCorVD()
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_esqEx_vedra = VerificarCorVEEx()
    cor_direita.pegarRGB()
    cor_esquerda.pegarRGB()
    if sensor_esq_vedra <= PRETO - 25 and sensor_esqEx_vedra <= PRETO - 20 and sensor_dir_vedra >= BRANCO - 5 and sensor_dirEx_vedra >= BRANCO  and cor_direita.pegarRGB()[0] >= (BRANCODIR) and cor_esquerda.pegarRGB()[0] >= (BRANCOESQ):
        base.moverDistancia(-7)
        base.pararMotores()
        sensor_esq_vedra = VerificarCorVE() # definindo variveis 
        sensor_dir_vedra = VerificarCorVD()
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_esqEx_vedra = VerificarCorVEEx()
        cor_direita.pegarRGB()
        cor_esquerda.pegarRGB()
        wait(20)
        if sensor_esq_vedra <= PRETO - 25 and sensor_esqEx_vedra <= PRETO -20  and sensor_dir_vedra >= BRANCO - 5 and sensor_dirEx_vedra >= BRANCO  and cor_direita.pegarRGB()[0] >= (BRANCODIR) and cor_esquerda.pegarRGB()[0] >= (BRANCOESQ) :            
            print ("noventa graus esq")
            base.moverDistancia(117)
            base.moverDistancia(-50)
            base.virar90grausEsquerda()
            base.pararMotores()
            return True

    return False 

# para quando ver prata
def Prata():
    sensor_esqEx_vedra = VerificarCorVEEx()
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_dir_vedra = VerificarCorVD()
    if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
        print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())
        base.moverDistancia(10)
        base.pararMotores()

        if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
            print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())
            base.moverDistancia(-10)
            base.pararMotores()
            
            if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
                print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())

            base.moverDistancia(20)
            base.pararMotores()
        
            if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
                print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())
                return True
    
    return False


# seguir linha
#  base.moverSemParar(velocidade=100, angulo_curvatura=0)

# WHILE TRUE
      
#     motor_garra.resetarAngulo()
#     motor_garra.moverUmAngulo(60, 10)

# while True: 
#     print(cor_direita.pegarRGB())
#     wait(2000)

# while True: 
#     sensor_esqEx_vedra = VerificarCorVEEx()
#     sensor_esq_vedra = VerificarCorVE() 
#     sensor_dirEx_vedra = VerificarCorVDEx()
#     sensor_dir_vedra = VerificarCorVD()
#     print(sensor_vendra.read(0))
#     wait(2000)
0
# while True: 
#     base.moverSemParar(500, 180)
#     wait(2000)

def Gap2():
    global contadorGap
    base.pararMotores()
    wait(100)
    motor_d.moverUmAngulo(500, 2 * 360, False)
    motor_e.moverUmAngulo(500, - 2 * 360, False)
    i = 0 
    while i < 100:
        sensor_esqEx_vedra = VerificarCorVEEx()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_dir_vedra = VerificarCorVD()

        if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
            motor_d.pararMotorInstantaneamente()
            motor_e.pararMotorInstantaneamente()
            print ("resetei contador")
            contadorGap = 0
            return False 
        wait(20)
        i += 1 
    base.pararMotores()
    base.moverDistancia(-60)
    base.pararMotores()

    sensor_esqEx_vedra = VerificarCorVEEx()
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_dir_vedra = VerificarCorVD()

    if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
            motor_d.pararMotorInstantaneamente()
            motor_e.pararMotorInstantaneamente()
            print ("resetei contador")
            contadorGap = 0
            return False 
        
    base.moverDistancia(60)
    base.pararMotores()

    motor_d.moverUmAngulo(500, - 4 * 360, False)
    motor_e.moverUmAngulo(500, 4 * 360, False)
    i = 0 
    while i < 120:
        
        sensor_esqEx_vedra = VerificarCorVEEx()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_dir_vedra = VerificarCorVD()

        if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
            motor_d.pararMotorInstantaneamente()
            motor_e.pararMotorInstantaneamente()
            contadorGap = 0
            print("resetei o gap")
            return False 
        wait(20)
        i += 1

    base.pararMotores()
    base.moverDistancia(-60)
    base.pararMotores()

    sensor_esqEx_vedra = VerificarCorVEEx()
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_dir_vedra = VerificarCorVD()

    if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
            motor_d.pararMotorInstantaneamente()
            motor_e.pararMotorInstantaneamente()
            print ("resetei contador")
            contadorGap = 0
            return False 
        
    base.moverDistancia(60)
    base.pararMotores()

    motor_d.moverUmAngulo(500,1.8 *360,False)
    motor_e.moverUmAngulo(500,-1.8 * 360)
    return True
        
# while True: 
#     Gap2()
#     wait(2000)

def seguidorLinha():
    global seguindoLinha
    global distancia
    global angulo_verificar
    global viradaAngulo
    global BRANCO
    global PRETO
    global pretoEsqCor
    global brancoEsqCor
    global pretoDirCor
    global brancoDirCor 
    global BRANCODIR
    global BRANCOESQ
    global PRETODIR
    global PRETOESQ
    global contadorGap

    # motor_d.moverPorPotencia(potencia=70)
    # motor_e.moverPorPotencia(potencia=70)
    sensor_esq_vedra = VerificarCorVE() # definindo variveis 
    sensor_dir_vedra = VerificarCorVD()
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_esqEx_vedra = VerificarCorVEEx()

    if cor_esquerda.pegarRGB()[0] <= 5: 
        ultimaCorEsq = pretoEsqCor
    else: 
        ultimaCorEsq = brancoEsqCor

    if cor_direita.pegarRGB()[0] <= 5: 
        ultimaCorDireita = pretoDirCor
    else:
        ultimaCorDireita = brancoDirCor

    # distanciaParar()

    # if distancia < 100:
    #     distanciaParar()
    #     break

# para quando ver verde: 
#     quando cor esquerda
    if eVerdeE():
        sensor_esqEx_vedra = VerificarCorVEEx()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_dir_vedra = VerificarCorVD()
        print ("verde esquerda visto")
        print(cor_esquerda.pegarRGB())
        base.moverDistancia(-10)
        base.pararMotores()
        # robo_brick.beep(500, 100)
        # wait(20)

        if eVerdeE():
            wait(20)
            base.moverDistancia(2)
            base.pararMotores()
            print("verde dnv esquerda")
            print(cor_esquerda.pegarRGB())
            # robo_brick.beep(500, 100)
            # cor_esquerda.pegarRGB()[1]
            # wait(20)(
            print("teste")
            # if eVerdeD(): # sem redutor
            #     print ("verde direita")
            #     base.moverDistancia(-80)
            #     # base.pararMotores()
            #     base.virarAngulo(-182)


            #     base.pararMotores()

            if eVerdeD(): # dois verdes com um redutor atras
                print ("verde direita")
                base.moverDistancia(2)
                base.pararMotores()
                # base.moverDistancia(90)
                # # base.pararMotores()
                # base.virarAngulo(-182)
                # base.pararMotores()
                wait(20)
                cor_esq_verm = cor_esquerda.pegarRGB()[0]
                cor_esq_verd = cor_esquerda.pegarRGB()[1]

                if eVerdeD() == True:
                    base.moverDistancia(90)
                    # base.pararMotores()
                    base.virarAngulo(-182)
                    base.pararMotores()
                    wait(20)
                    cor_esq_verm = cor_esquerda.pegarRGB()[0]
                    cor_esq_verd = cor_esquerda.pegarRGB()[1]

                # if eVerdeD() == True and eVerdeE() == True:
                #     cor_esq_verm = cor_esquerda.pegarRGB()[0]
                #     cor_esq_verd = cor_esquerda.pegarRGB()[1]
                #     base.moverDistancia(90)
                #     # base.pararMotores()
                #     base.virarAngulo(-182)
                #     base.pararMotores()
                
            else:
                cor_esq_verm = cor_esquerda.pegarRGB()[0]
                cor_esq_verd = cor_esquerda.pegarRGB()[1] # preto usando o vermelho 
                if cor_esq_verm < PRETOESQ:
                    # robo_brick.beep(100, 100)
                    if cor_esq_verd > cor_esq_verm:
                        print("preto apos verde esquerda")
                        base.moverDistancia(70)
                        base.pararMotores()
                        VerdeEsquerda()
                        base.moverDistancia(-50)
                        base.pararMotores()


                if cor_esq_verm > BRANCOESQ: #branco tb usando vermelho 
                    print ("branco apos verde")
                    if cor_esq_verd > cor_esq_verm:
                        base.moverDistancia(10)
                        base.pararMotores()                   

    # # quando a direita ver verde 
    elif eVerdeD():
        sensor_esqEx_vedra = VerificarCorVEEx()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_dir_vedra = VerificarCorVD()
        cor_esq_verm = cor_esquerda.pegarRGB()[0]
        cor_esq_verd = cor_esquerda.pegarRGB()[1]

        print ("verde direito visto")
        print(cor_direita.pegarRGB())
        base.moverDistancia(-10)
        base.pararMotores()

        if eVerdeD():
            print("verde dnv direita")
            print(cor_direita.pegarRGB())
            base.moverDistancia(2)
            base.pararMotores()
            # cor_direita.pegarRGB()[1]
            # print("teste")
            # if eVerdeE(): #verificar se o outro tb eh verde mas sem redutor
            #     print ("verde esquerda")
            #     base.pararMotores()
            #     if eVerdeE():
            #         base.moverDistancia(-80)
            #             # base.pararMotores()
            #         base.virarAngulo(-182)
            #         base.pararMotores()

            if eVerdeE(): #verificar se o outro tb eh verde c redutor atras
                print ("verde esquerda")
                cor_esq_verm = cor_esquerda.pegarRGB()[0]
                cor_esq_verd = cor_esquerda.pegarRGB()[1]
                base.pararMotores()
                wait(20)
                if eVerdeE():
                    # base.moverDistancia(90)
                    #     # base.pararMotores()
                    # base.virarAngulo(-182)
                    # base.pararMotores()
                    base.moverDistancia(90)
                    # base.pararMotores()
                    base.virarAngulo(-182)
                    base.pararMotores()
                    wait(20)
                    cor_esq_verm = cor_esquerda.pegarRGB()[0]
                    cor_esq_verd = cor_esquerda.pegarRGB()[1]

                    # if eVerdeD() == True and eVerdeE() == True:
                    #     cor_esq_verm = cor_esquerda.pegarRGB()[0]
                    #     cor_esq_verd = cor_esquerda.pegarRGB()[1]
                    #     base.moverDistancia(90)
                    #     # base.pararMotores()
                    #     base.virarAngulo(-182)
                    #     base.pararMotores()

            else:
                cor_dir_verm = cor_direita.pegarRGB()[0]
                cor_dir_verd = cor_direita.pegarRGB()[1]
                if cor_dir_verm < PRETODIR:
                    if cor_dir_verd > cor_dir_verm:
                            print("preto apos verde direita")
                            base.moverDistancia(70)
                            base.pararMotores()
                            print(cor_direita.pegarRGB())
                            VerdeDireita()
                            base.moverDistancia(-50)
                            base.pararMotores()

                if cor_dir_verm > BRANCODIR:
                    print ("branco apos verde")
                    if cor_dir_verd > cor_dir_verm:
                            base.moverDistancia(20)
                            base.pararMotores()
 
    elif eVermelhoE(): # vermelho esquerdo
        sensor_esqEx_vedra = VerificarCorVEEx()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_dir_vedra = VerificarCorVD()
        print ("vermelho esquerda visto")
        print(cor_esquerda.pegarRGB())
        base.moverDistancia(-2)
        wait(50)
        base.pararMotores()


        if eVermelhoE():
            base.moverDistancia(2)
            base.pararMotores()
            print("vermelho dnv esquerda")
            print(cor_esquerda.pegarRGB())
            print("vermelho parar")
            base.pararMotores()
            while True: 
                base.pararMotores()

    elif eVermelhoD(): # vermelho direito
        sensor_esqEx_vedra = VerificarCorVEEx()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_dir_vedra = VerificarCorVD()
        print (" vermelho direito visto")
        print(cor_esquerda.pegarRGB())
        base.moverDistancia(-2)
        wait(50)
        base.pararMotores()


        if eVermelhoD():
            base.moverDistancia(2)
            base.pararMotores()
            print("vermelho dnv direito")
            print(cor_esquerda.pegarRGB())
            print("vermelho parar")
            base.pararMotores()
            while True: 
                base.pararMotores()
        
    # quando entrar no branco, 
    # ele vai verificar se ta no gap, caso esteja, 
    # vai realizar o codigo de gap e caso nao, vai ir p preto

    elif sensor_esq_vedra >= BRANCO and sensor_dir_vedra >= BRANCO:
        sensor_esqEx_vedra = VerificarCorVEEx()
        sensor_esq_vedra = VerificarCorVE() 
        sensor_dirEx_vedra = VerificarCorVDEx()
        sensor_dir_vedra = VerificarCorVD()
        print("viu branco")
        print(sensor_esq_vedra, sensor_dir_vedra)
        # base.moverDistancia(-45)
        base.pararMotores()

        # #<LIGAR>
        if sensor_dirEx_vedra <= PRETO - 25 or sensor_esqEx_vedra <= PRETO - 25 :
            sensor_esqEx_vedra = VerificarCorVEEx()
            sensor_esq_vedra = VerificarCorVE() 
            sensor_dirEx_vedra = VerificarCorVDEx()
            sensor_dir_vedra = VerificarCorVD()
            if sensor_dirEx_vedra <= PRETO - 25 and sensor_dir_vedra >= BRANCO: 
                print ("viu extremidade branco dir ")
                # base.moverDistancia(-50)
                base.virarAngulo(20)
                base.pararMotores()

            if sensor_esqEx_vedra <= PRETO - 25 and sensor_esq_vedra >= BRANCO:
                print ("viu extremidade branco esq ") 
                # base.moverDistancia(-50)
                base.virarAngulo(-20)
                base.pararMotores()

        if Gap2() == True: 

            while sensor_esq_vedra >= BRANCO and sensor_dir_vedra >= BRANCO:
                taNoGap()
                global contadorGap
                contadorGap += 1
                print ("+ contador")
                sensor_esq_vedra = VerificarCorVE()
                sensor_dir_vedra = VerificarCorVD()
                sensor_dirEx_vedra = VerificarCorVDEx()
                sensor_esqEx_vedra = VerificarCorVEEx()

                if contadorGap == 2: 
                    print("contador deu 2")
                    base.moverDistancia(-600)
                    base.pararMotores()
                    seguindoLinha = False
                    break

                if sensor_esq_vedra <= PRETO or sensor_dir_vedra <= PRETO or sensor_dirEx_vedra <= PRETO or sensor_esqEx_vedra <= PRETO:
                    contadorGap = 0 
                    break
        else: 
            contadorGap = 0
            print ("saiu do branco")

    elif Distancia(): # obstaculo 
        Obstaculo()
        base.pararMotores()

    elif Prata() == True: 
        print ("prata")
        seguindoLinha = False
        return
    #     base.pararMotores()

    # elif TudoPreto():
    #     print("tudo preto")
    #     base.pararMotores()


    # elif NoventaGrausD() == True:
    #     base.pararMotores()
    #     wait(3000)
    #     if NoventaGrausD() == False: 
    #         print("noventa graus falso")

    # elif NoventaGrausE() == True:
    #     print("noventa grau esquerda")
    #     base.pararMotores()
    #     wait(3000)
    #     if NoventaGrausE() == False:
    #         print("noventa graus falso")

    elif sensor_dirEx_vedra <= PRETO or sensor_esqEx_vedra <= PRETO:
        # wait(100)
        # base.pararMotores()
        if sensor_esqEx_vedra <= PRETO and  sensor_esq_vedra > PRETO:
            print("viu extremidade esquerda ") 
            # motor_e.moverDuranteUmTempo(-250, 1000)
            # motor_d.moverDuranteUmTempo(-500, 1000)
            base.moverDistancia(-30)
            base.virarAngulo(-15)
            base.pararMotores()
            return 
        if sensor_dirEx_vedra <= PRETO and sensor_dir_vedra > PRETO: 
                print("viu extremidade direita")
                # motor_e.moverDuranteUmTempo(-500, 1000)
                # motor_d.moverDuranteUmTempo(-250, 1000)
                base.moverDistancia(-30)
                base.virarAngulo(15)
                base.pararMotores()
                return
        
        else: 
            base.moverDistancia(80)
            base.pararMotores()
        #     # wait(5000)
        # return

    # codigo seguidor de linha
    print("seguindo linha")
    sensor_esqEx_vedra = VerificarCorVEEx()
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_dir_vedra = VerificarCorVD()
    codigoSeguidor.seguirLinhaPreta(
    kd=0.3, # analisa de acordo com a poisçao do começo
    kp=1, # proporcional no momento instante que ocorre o erro
    cor_vermelha_direta=sensor_dir_vedra + sensor_dirEx_vedra,
    cor_vermelha_esquerda=sensor_esq_vedra + sensor_esqEx_vedra + 25,
    motor_direito=motor_d, 
    motor_esquerdo=motor_e,
    potencia_motores=70
    )


## Duda 

def frenteArea(tamanho:int): #Função para mover pra frente rapido
    base.pararMotores()
    motor_d.moverPorPotencia(90)
    motor_e.moverPorPotencia(90)
    wait(tamanho)
    base.pararMotores()

    # global sensor_dir_vedra
    # global sensor_dirEx_vedra
    # global sensor_esq_vedra
    # global sensor_esqEx_vedra
    # global seguindoLinha
    # print("frente area")
    # contador = 0
    # # motor_d.moverUmAngulo(700, 0, False)
    # # motor_e.moverUmAngulo(700, 0, False)
    # motor_d.moverPorPotencia(90)
    # motor_e.moverPorPotencia(90)
    # while contador < tamanho:
    #     sensor_esqEx_vedra = VerificarCorVEEx()
    #     sensor_esq_vedra = VerificarCorVE() 
    #     sensor_dirEx_vedra = VerificarCorVDEx()
    #     sensor_dir_vedra = VerificarCorVD()

    #     if sensor_dir_vedra <= PRETO or sensor_esq_vedra <= PRETO:
    #         motor_d.pararMotorInstantaneamente()
    #         motor_e.pararMotorInstantaneamente()
    #         seguindoLinha = True
    #         print ("to saindo")
    #         base.moverDistancia(100)
    #         base.pararMotores()
    #         return 
    #     wait(20)
    #     contador += 1
    # motor_d.moverPorPotencia(0)
    # motor_e.moverPorPotencia(0) 
    

def quina(valor: float):  #Função que faz o robô reconhecer que está em uma quina
      print("opa, quina ;)")
      base.virar90grausDireita()
      base.virar90grausDireita()
      base.moverDistancia(-(valor+257))
      base.pararMotores()
      base.moverDistancia(170)
      base.pararMotores()
      base.virar90grausEsquerda()

def andarvira():   #Função que faz o robô se mover na area de resgate
    i = 0
    global seguindoLinha 
    global sensor_dir_vedra
    global sensor_dirEx_vedra
    global sensor_esqEx_vedra
    global sensor_esq_vedra
    base.pararMotores()
    motor_d.moverPorPotencia(90)
    motor_e.moverPorPotencia(90)

    while (i < 45): 
        if ( sensor_dir_vedra > PRETO or sensor_esq_vedra > PRETO):
            sensor_dir_vedra = VerificarCorVD()
            sensor_esq_vedra = VerificarCorVE()
            sensor_dirEx_vedra = VerificarCorVDEx()
            sensor_esqEx_vedra = VerificarCorVEEx()
            if sensor_esq_vedra <= PRETO or sensor_dir_vedra <= PRETO:
                base.pararMotores()
                seguindoLinha = True
                print ("to saindo")
                base.pararMotores()
                return True
        wait(20)
        i += 1

    base.virar90grausEsquerda()
    valor = sensor_ultrassonico.pegarDistancia()
    wait(177)
    if valor < 117:
        print("parede")
        base.virar90grausDireita()
        base.virar90grausDireita()
        base.moverDistancia(-(valor+257))
        print("f")
        base.pararMotores()
        base.moverDistancia(170)
        print("g")
        base.pararMotores()
        base.virar90grausEsquerda()
        valor2 = sensor_ultrassonico.pegarDistancia()
        if valor2 < 177:
                print("h")
                quina(valor2)

    seguindoLinha = False
    return False

def PrataVoltar():
    sensor_esqEx_vedra = VerificarCorVEEx()
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_dir_vedra = VerificarCorVD()
    if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
        print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())
        base.moverDistancia(10)
        base.pararMotores()

        if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
            print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())
            base.moverDistancia(-10)
            base.pararMotores()
            
            if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
                print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())

            base.moverDistancia(20)
            base.pararMotores()
        
            if cor_direita.pegarRGB() >= (80, 80, 80) or cor_esquerda.pegarRGB() >= (80, 80, 80):
                print(cor_direita.pegarRGB() and cor_esquerda.pegarRGB())
                return True
            
    
    return False

def alinharesq(valor:float): #Função que se allinha na quina esquerda (area de resgate)
    global seguindoLinha
    global sensor_dir_vedra
    global sensor_dirEx_vedra
    global sensor_esqEx_vedra
    global sensor_esq_vedra
    print("alinhar na esquerda")
    base.virar90grausDireita()
    base.virar90grausDireita() 
    wait(100)
    base.moverDistancia(-(valor+257))
    print("d")
    base.pararMotores()
    base.moverDistancia(170)
    print("e")
    base.pararMotores()
    base.virar90grausEsquerda()
    base.pararMotores()
    while (sensor_dir_vedra > PRETO or sensor_esq_vedra > PRETO):
        if (andarvira() == True): 
            return True
        
        if PrataVoltar() == True: 
            base.moverDistancia(-117)
            base.pararMotores()
            alinharDir()
        
    print("saida")
    seguindoLinha = True
    wait(1000)     
    base.pararMotores()
    return True

def paredeAoLado():    #Função que se alinha na parede esquerda (area de resgate)
      print("parede ao lado")
      base.virar90grausEsquerda()
      base.virar90grausEsquerda()
      frenteArea(tamanho=950)
      print ("a")
      base.pararMotores()
      base.virar90grausDireita()
      frenteArea(tamanho=800)
      print("b")
      base.pararMotores()
      frenteArea(tamanho=370)
      print("c")
      base.pararMotores()
      base.virar90grausEsquerda()

def paredeAoLado():    #Função que se alinha na parede esquerda (area de resgate)
      print("parede ao lado")
      base.virar90grausEsquerda()
      base.virar90grausEsquerda()
      frenteArea(tamanho=950)
      print ("a")
      base.pararMotores()
      base.virar90grausDireita()
      frenteArea(tamanho=800)
      print("b")
      base.pararMotores()
      frenteArea(tamanho=370)
      print("c")
      base.pararMotores()
      base.virar90grausEsquerda()

# def paredeAoLado():    #Função que se alinha na parede direita (area de resgate)
#       print("parede ao lado")
#       base.virar90grausDireita()
#       base.virar90grausDireita()
#       frenteArea(tamanho=950)
#       print ("a")
#       base.pararMotores()
#       base.virar90grausEsquerda()
#       frenteArea(tamanho=800)
#       print("b")
#       base.pararMotores()
#       frenteArea(tamanho=370)
#       print("c")
#       base.pararMotores()
#       base.virar90grausDireita()

def alinharDir(valor:float): #Função que se allinha na quina direita
    global seguindoLinha
    print("alinhar na direita")
    base.virar90grausEsquerda()
    base.virar90grausEsquerda()
    base.moverDistancia(-(valor+257))
    base.pararMotores()
    base.moverDistancia(350)
    base.pararMotores()
    while (sensor_dir_vedra > PRETO or sensor_esq_vedra > PRETO):
        if (andarvira() == True): 
            return True
        
        if PrataVoltar() == True:
            base.moverDistancia(-117)
            base.pararMotores()
            alinharDir()
        
    print("saida")
    seguindoLinha = True
    wait(1000)     
    base.pararMotores()
    return True

                  
def area():  #Fução que chama todas as funções nescessarias para a area de resgate
      base.virar90grausEsquerda()
      base.pararMotores()
      valor = sensor_ultrassonico.pegarDistancia()
      wait(177)
      if valor <= 100:
            print("parede perto")
            if (alinharesq(valor) == True):
                return

      elif 100 < valor <= 200:
            base.moverDistancia(77)
            print("parede perto")
            if (alinharesq(valor) == True):
                return

      elif valor > 190:
            print("verificar outro lado")
            base.virar90grausDireita()
            base.virar90grausDireita()
            valor2 = sensor_ultrassonico.pegarDistancia()
            if valor2 >= 100:
                  paredeAoLado()
            elif valor2 <= 100:
                  alinharDir(valor=valor2)

##INICIO do codigo

#motor_garra.moverDuranteUmTempo(500, 1000)

# while True: 
#     print(cor_esquerda.pegarRGB())
#     wait(2000)

# frenteArea(1000)
# while True:
#     wait(10000)

while True:
    sensor_esqEx_vedra = VerificarCorVEEx()
    sensor_esq_vedra = VerificarCorVE() 
    sensor_dirEx_vedra = VerificarCorVDEx()
    sensor_dir_vedra = VerificarCorVD()
    distanciaArea = sensor_ultrassonico.pegarDistancia()

    if seguindoLinha == True:
        # print("seguidor linha")
        seguidorLinha()
    else:
        beep(500, 100)
        print("area de resgate")
        frenteArea(tamanho=950)
        area()
        print("area de resgate saida")
        beep(700, 100)
    wait(20)
    