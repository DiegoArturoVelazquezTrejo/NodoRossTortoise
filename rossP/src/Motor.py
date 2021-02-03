# Biblioteca para controlar el raspberry pi
import RPi.GPIO as GPIO
# Biblioteca para trabajar con los sleeps
from time import sleep

'''
Clase para modelar el comportamiento de un motor de corriente directa
'''
class Motor:
    # Constructor de la clase motor
    def __init__(self, Ena, In1, In2):

        GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)

        self.Ena = Ena

        self.In1 = In1

        self.In2 = In2
        # Definimos el modo de las entradas

        GPIO.setup(self.Ena, GPIO.OUT)

        GPIO.setup(self.In1, GPIO.OUT)

        GPIO.setup(self.In2, GPIO.OUT)

        # Definimos el pwm

        self.pwm = GPIO.PWM(self.Ena, 100 )

        self.pwm.start(0)

        self.velocidad = 50

        self.movimientos = {"adelante": self.moveF, "atras":self.moveB}

        self.movimiento = self.movimientos["adelante"]
        
        # Moving Forward
    '''
    @param: Velocidad
    @param: Delay
    '''
    def moveF(self, x=50, t = 0):  # x esta entre 0 y 100

        self.movimiento = self.movimientos["adelante"]
        
        #print("Moviendo hacia adelante")
        
        GPIO.output(self.In1, GPIO.LOW)

        GPIO.output(self.In2, GPIO.HIGH)

        #self.pwm.ChangeDutyCycle(x)
        
        self.pwm.ChangeDutyCycle(self.velocidad)

        sleep(t)
    # Moving Backward
    '''
    @param: Velocidad
    @param: Delay
    '''
    def moveB(self, x=50, t = 0):  # x esta entre 0 y 100

        self.movimiento = self.movimientos["atras"]
        
        #print("Moviendo hacia atras")
        
        GPIO.output(self.In1, GPIO.HIGH)

        GPIO.output(self.In2, GPIO.LOW)

        #self.pwm.ChangeDutyCycle(x)

        self.pwm.ChangeDutyCycle(self.velocidad)
        
        sleep(t)
    # Stopping the motor
    '''
    @param: Tiempo
    '''
    def stop(self, t= 0):

        self.pwm.ChangeDutyCycle(0)

        sleep(t)

    # Metodo para aumentar la velocidad
    '''
    @param: Velocidad 
    '''
    def aumenta_velocidad(self, x):

        if(self.velocidad < 100):
        
            self.velocidad = self.velocidad + x

        self.movimiento()
        
    # Metodo para disminuir la velocidad
    '''
    @param: velocidad
    '''
    def disminuye_velocidad(self, x):

        if(self.velocidad > 0 ):
        
            self.velocidad = self.velocidad - x

        self.movimiento()
        
    # Metodo para modificar la velocidad de los motores
    '''
    @param: Velocidad 
    '''
    def modificar_velocidad(self, x):

        if(x >= 0 and x <= 100):

            self.velocidad = x

        self.movimiento()
