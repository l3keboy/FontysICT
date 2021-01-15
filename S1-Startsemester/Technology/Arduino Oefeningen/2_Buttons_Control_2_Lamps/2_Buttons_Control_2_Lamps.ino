const int LeftButtonPin = 3;
const int RightButtonPin = 2;
const int LeftLamp = 12;
const int RightLamp = 13;



void setup() {
  // put your setup code here, to run once:
pinMode(LeftLamp, OUTPUT);
pinMode(RightLamp, OUTPUT);
pinMode(LeftButtonPin, INPUT);
pinMode(RightButtonPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int LeftButtonState = 0;
  int RightButtonState = 0;

  LeftButtonState = digitalRead(LeftButtonPin);
  RightButtonState = digitalRead(RightButtonPin);

if (LeftButtonState == HIGH){
    digitalWrite(LeftLamp, HIGH);
}else
    digitalWrite(LeftLamp, LOW);

if (RightButtonState == HIGH){
    digitalWrite(RightLamp, HIGH);
}else
    digitalWrite(RightLamp, LOW);

}
