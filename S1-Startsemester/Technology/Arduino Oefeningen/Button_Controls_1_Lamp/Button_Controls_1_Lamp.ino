const int ledPin = 13;
const int buttonPin = 2;

void setup() {
  // put your setup code here, to run once:
pinMode(ledPin, OUTPUT);
pinMode(buttonPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int buttonState = 0;
  buttonState = digitalRead(buttonPin);
if (buttonState == HIGH){
      digitalWrite(ledPin, HIGH);
}else 
      digitalWrite(ledPin, LOW);
}
