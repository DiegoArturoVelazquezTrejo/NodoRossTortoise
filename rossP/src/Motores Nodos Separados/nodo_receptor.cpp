#include "ros/ros.h"

#include <std_msgs/String.h>

#include <wiringPi.h>

using namespace std;

/**
Nodo que se encargará de recibir los comandos del nodo emisor 
y con base en ellos realizará distintas acciones como moverse, aumentar 
la velocidad, girar, etcétera. 
**/

void subscriber_Callback(const std_msgs::String::ConstPtr &received){
  
  //ROS_INFO("I received the following: %s", received->data.c_str()); 
  cout << "Tecla presionada: " << received->data << endl; 

  // Hacer un switch de la tecla recibirda

  /**
  switch(received -> data){

    // Caso para avanzar
    case 'w':

      break; 
    // Caso para aumentar la velicidad
    case 'm':

      break; 
    // Caso para girar a la derecha
    case 'd':

      break; 
    // Caso para girar a la izquierda
    case 'a':

      break; 
    // Caso para ir disminuir la velocidad
    case 'l':

      break; 
    // Caso para reversa 
    case 'r':

      break; 
  }
  **/

}

int main(int argc, char **argv){

  ros::init(argc, argv, "listener_node");

  ros::NodeHandle node_handle;

  ros::Subscriber sub = node_handle.subscribe("/chatter", 1,subscriber_Callback);
  ros::spin();

  return 0; 

}
