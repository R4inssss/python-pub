#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myservo.attach(9);  // Added the missing semicolon
}

void loop() {
  int val;

  while (Serial.available() > 0) {
    val = Serial.parseInt();
    if(val != 0){
      Serial.print(val);
      myservo.write(val);
    }
    delay(5);
  }
}
