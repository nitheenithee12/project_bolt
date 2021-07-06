#include <Ultrasonic.h>

int MOTOR = 7;

int Light_red = 2;


Ultrasonic us(12,13);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(MOTOR,OUTPUT);
  pinMode(2,OUTPUT);
  analogReference(EXTERNAL); 

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(us.distanceRead()); 
  int k = us.distanceRead();
  if (k >= 50){          //consider tank depth is 70meters, if water level is only 20meters then we will turn on the motor
    analogWrite(MOTOR,255);  //To turn on the motor. (I have used 12v pump motor. SO I needed an extra transistor.)
    digitalWrite(2,HIGH);
    delay(50000);
  }
  else if (k <= 5){
    analogWrite(MOTOR,0);
    digitalWrite(2,LOW);
  }
  delay(5000);

}
