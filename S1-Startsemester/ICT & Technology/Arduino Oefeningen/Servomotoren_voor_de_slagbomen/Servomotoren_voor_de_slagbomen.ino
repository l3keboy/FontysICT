#include <Servo.h>
int servoPin1 = 2; //Servomotor 1.
Servo Servo1;
int servoPin2 = 3; //Servomotor 2.
Servo Servo2;

void setup() {
  // put your setup code here, to run once:
  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
}

  void barrierDown(){
  //Barrier goes up and down.
  Servo1.write(0);
    Servo2.write(0);
  }

  void barrierUp(){
    Servo1.write(90);
    Servo2.write(90);
  }
  
void loop() {
  // put your main code here, to run repeatedly:
  barrierUp();
  barrierDown();
}
