#!/usr/bin/env python

#Biblioteca para trabajar con ROS
import rospy
# Biblioteca para trabajar con mensajes
from std_msgs.msg import String

from rossP.msg import joystick_msg

# Biblioteca para controlar el raspberry pi
import RPi.GPIO as GPIO
# Biblioteca para trabajar con los sleeps
from time import sleep
# Biblioteca para modelar los motores
from Motor import Motor
'''
Nodo suscriptor al topico de Ros del envio de caracteres.
Recibe el mensaje, lo clasifica y tiene como actuador un motor.

MOTOR DERECHO DEL ROBOT

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

motor = Motor(2, 3, 4)

motor2 = Motor(16, 20, 21)

def subscriber():

    sub = rospy.Subscriber('/chatter', String, callback_function)

    sub2 = rospy.Subscriber('/chatter2', joystick_msg, modifica_velocidades)

    rospy.spin()

def modifica_velocidades(message): 
    
    #print("Velocidad del motor derecho: "+ str(message.RightWheel))
    
    #print("Velocidad del motor izquierdo: "+ str(message.LeftWheel))
    
    motor.modificar_velocidad(message.RightWheel)
    
    motor2.modificar_velocidad(message.LeftWheel)

def callback_function(message):

    rospy.loginfo("He recibido: %s"%message.data)

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)

    # Este nodo modela un motor del robot, digamos, el motor izquierdo.
    # motor = Motor(2, 3, 4)

    # Vamos a clasificar el tipo de dato
    data = message.data

    if(data == 'w'): # Movimiento hacia adelante

        print("Moviendo motor A hacia adelante")
        
        motor.moveF()
        
        motor2.moveF()

    elif(data == 's'): #Movimiento hacia atras

        print("Moviendo motor A hacia atras")

        motor.moveB()
        
        motor2.moveB()

    if(data == 'a'): # Este motor se detendra mientras que el otro se movera; Movimiento a la izquierda

        print("Moviendo el motor A hacia la izquierda")
        
        motor.stop(1)
        
        motor2.moveF()

    elif(data == 'd'): # El otro motor se movera; Movimiento a la derecha

        print("Moviendo el motor A hacia la derecha")
        
        motor.moveF()
        
        motor2.stop(1)

    if(data == 'm'): # Aumentar la velocidad

        print("Aumentando velocidad en motor A a: "+str(motor.velocidad))

        motor.aumenta_velocidad(5)
        
        motor2.aumenta_velocidad(5)

    elif(data == 'l'): #Disminuir la velocidad

        print("Disminuyendo velocidad en motor A a: "+str(motor.velocidad))

        motor.disminuye_velocidad(5)

        motor2.disminuye_velocidad(5)

    elif(data == 'k'): #Detener el motor por 10 segundos

        print("Deteniendo el motor A")

        motor.stop(10)
        
        motor2.stop(10)

if __name__ == "__main__":

    rospy.init_node("motor_A_subscriber")

    subscriber()
