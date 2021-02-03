#!/usr/bin/env python

#Biblioteca para trabajar con ROS
import rospy
# Biblioteca para trabajar con mensajes
from std_msgs.msg import String

# Biblioteca para controlar el raspberry pi
import RPi.GPIO as GPIO
# Biblioteca para trabajar con los sleeps
from time import sleep
# Biblioteca para modelar los motores
from Motor import Motor
'''
Nodo suscriptor al topico de Ros del envio de caracteres.
Recibe el mensaje, lo clasifica y tiene como actuador un motor.

MOTOR IZQUIERDO DEL ROBOT

Definamos convenciones:

    Tecla w  ---------> Mover hacia adelante
    Tecla s  ---------> Mover hacia atras
    Tecla a  ---------> Mover hacia la izquierda
    Tecla d  ---------> Mover hacia la derecha
    Tecla m  ---------> Aumentar velocidad
    Tecla l  ---------> Disminuir la velocidad
    Tecla k  ---------> Detener el robot

'''

global motor

motor = Motor(16, 20, 21)

def subscriber():

    sub = rospy.Subscriber('/chatter', String, callback_function)

    rospy.spin()

def callback_function(message):

    rospy.loginfo("He recibido: %s"%message.data)

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)

    # Este nodo modela un motor del robot, digamos, el motor izquierdo.
    # motor = Motor(16, 20, 21)

    # Vamos a clasificar el tipo de dato
    data = message.data

    if(data == 'w'): # Movimiento hacia adelante

        print("Moviendo el motor B hacia adelante")
        
        motor.moveF()

    elif(data == 's'): #Movimiento hacia atras

        print("Moviendo el motor B hacia atras")
        
        motor.moveB()

    if(data == 'a'): # Este motor se movera mientras que el otro se detendra; Movimiento a la izquierda

        print("Moviendo el motor B hacia la izquierda")
        
        motor.moveF()

    elif(data == 'd'): # El otro motor se detendra; Movimiento a la derecha

        print("Moviendo el motor B hacia la derecha")
        
        motor.stop(1)

    if(data == 'm'): # Aumentar la velocidad

        print("Aumentando velocidad en motor B a: "+str(motor.velocidad))
        
        motor.aumenta_velocidad(5)

    elif(data == 'l'): #Disminuir la velocidad

        print("Disminuyendo velocidad en motor B a: "+str(motor.velocidad))
        
        motor.disminuye_velocidad(5)

    elif(data == 'k'): #Detener el motor por 10 segundos

        print("Deteniendo el motor B")
        
        motor.stop(10)

if __name__ == "__main__":

    rospy.init_node("B")

    subscriber()
