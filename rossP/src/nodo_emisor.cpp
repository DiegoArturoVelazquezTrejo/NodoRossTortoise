#include <ros/ros.h>

#include <std_msgs/String.h>

#include <rossP/joystick_msg.h>

#include <iostream>

#include <stdio.h>

#include <sstream>

using namespace std; 

/**
Nodo emisor de las teclas presionadas en c++
 **/

int main(int argc, char* argv[]){

  // Vamos a registrar el nombre del nodo
  
  ros::init(argc, argv, "talker_node");

  ros::NodeHandle nodo;

  ros::Publisher pub;
  
  ros::Publisher pub2; 

  pub = nodo.advertise<std_msgs::String>("/chatter", 1);

  pub2 = nodo.advertise<rossP::joystick_msg>("/chatter2", 1); 

  ros::Rate loop_rate(10);
  
  int count = 0; 
  
  int velocidad_a = 0; 
  
  int velocidad_b = 0; 
  
  while(ros::ok()){
    
    // Vamos a pedir la velocidad para los respectivos motores 
    
    cout << "Ingrese la velocidad del motor derecho: " << endl; 
    
    cin >> velocidad_a; 
    
    cout << "Ingrese la velocidad del motor izquierdo: " << endl; 
    
    cin >> velocidad_b; 

    std_msgs::String msg;
    
    rossP::joystick_msg msg2; 

    std::stringstream ss;
    
    //system("stty raw");
    
    cout << "\nPresione una tecla : " << endl; 
    
    char input;  
    
    cin >> input; 
    
    // char input = getchar();

    //system("stty cooked"); 
    
    //ss << "Tecla presionada: " << count;

    msg.data = input;
    
    msg2.RightWheel = velocidad_a; 
    
    msg2.LeftWheel = velocidad_b; 

    cout << "----" <<  msg.data << "----" << endl;

    pub.publish(msg);
    
    pub2.publish(msg2);
    
    ros::spinOnce();

    loop_rate.sleep();

    if(input == 'q')

      break; 
    
  }

  return 0; 

}
