#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myservo.attach(9);
}

void loop() {
  int val;

  while (Serial.available() > 0) {
    val = Serial.parseInt();
    if(val != 0){
      Serial.println();
      Serial.print("Setting servo to: ");
      Serial.print(val);
      myservo.write(val);
    }
    delay(0);
  }
}
