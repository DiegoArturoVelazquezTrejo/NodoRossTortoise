#include <ros/ros.h>

#include <std_msgs/String.h>

#include <iostream>

#include <stdio.h>

#include <sstream>

using namespace std; 

/**
Nodo emisor de las teclas presionadas en c++ que adopta el mensaje de joystick 
* Solicita también la velocidad que se le va a poner al robot 
 **/

int main(int argc, char* argv[]){

  // Vamos a registrar el nombre del nodo
  
  ros::init(argc, argv, "talker_node");

  ros::NodeHandle nodo;

  ros::Publisher pub;

  pub = nodo.advertise<std_msgs::String>("/chatter", 1);

  ros::Rate loop_rate(10);
  
  int count = 0; 
  
  int velocidad_a = 0; 
  
  int velocidad_b = 0; 
  
  while(ros::ok()){
	  
	// Vamos a solicitar la velocidad de cada motor 
	cout << "Ingrese la velocidad del motor A: " << velocidad_a
	
	cout << "Ingrese la velocidad del motod B: " << velocidad_b

    std_msgs::String msg;

    std::stringstream ss;

    system("stty raw");

    cout << "\nPresione una tecla : " << endl; 
    
    char input = getchar();

    system("stty cooked"); 
    
    //ss << "Tecla presionada: " << count;

    msg.data = input;

    cout << "----" <<  msg.data << "----" << endl;

    pub.publish(msg);
    
    ros::spinOnce();

    loop_rate.sleep();

    if(input == 'q')

      break; 
    
  }

  return 0; 

}
