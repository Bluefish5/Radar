/*
 * A0 - Podpięty czujnik odległości
 * 9D - servo
 * 10D - HIGH
*/


#include <Servo.h>

Servo myservo; 

int pos = 90;
int input = 0;         
bool is_input = false;
int sensorValue = 0;
int x = 1;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  pinMode(10,OUTPUT);
  digitalWrite(10, HIGH);
  myservo.write(pos);
  delay(300);
}

void loop() {
   if (Serial.available() > 0) {
      input = Serial.read();
      if(input == 49){
        is_input=true;
        sensorValue = analogRead(A0);
        sensorValue = map(sensorValue,50,900,0,100);
        Serial.print(pos);
        Serial.print(" ");
        Serial.println(sensorValue);
      }
      if(is_input){
        is_input = false;
        if(pos>180)x=-1;
        if(pos<0)x=1;
        pos=pos+x;
        myservo.write(pos);
      }
   }
}
