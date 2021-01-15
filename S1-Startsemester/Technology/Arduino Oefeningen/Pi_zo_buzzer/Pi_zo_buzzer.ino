void setup() {
  // put your setup code here, to run once:
  pinMode(7, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  tone(7, 1000);
  delay(1000);
  noTone(7);
  delay(1000);
}
