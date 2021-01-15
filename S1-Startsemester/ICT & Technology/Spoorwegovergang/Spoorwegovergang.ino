#include <Servo.h>
int servoPin1 = 2; //Servomotor 1.
Servo Servo1;
int servoPin2 = 3; //Servomotor 2.
Servo Servo2;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT); //Lampje 1.
  pinMode(12, OUTPUT); //Lampje 2.
  pinMode(11, OUTPUT); //Lampje 3.
  pinMode(10, OUTPUT); //Lampje 4.
  pinMode(7, OUTPUT); //Piëzo.
  
  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
}

  void firstLightOn(){
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  }

  void firstLightOff(){
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  }
  
  void secondLightOn(){
  digitalWrite(11, LOW);
  digitalWrite(10, HIGH);
  }

  void secondLightOff(){
  digitalWrite(10, LOW);
  digitalWrite(11, HIGH);
  }
  
  void firstTone(){
  //Speaker warnings! 
  tone(7, 1000, 100); 
  }

  void secondTone(){
  tone(7, 500, 100);
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
  void pause(int x){
  delay(x);
  }

void loop() {
 // put your main code here, to run repeatedly:
  firstTone();
  pause(250);
  secondTone();
  pause(250);
  firstLightOn();
  secondLightOn();
  pause(500);
  firstTone();
  pause(250);
  secondTone();
  pause(250);
  firstLightOff();
  secondLightOff();
  pause(500);
  barrierUp();
  //barrierDown();
}
