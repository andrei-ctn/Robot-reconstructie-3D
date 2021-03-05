//numarul pinilor
const int echoPinSensor1 = 6;
const int trigPinSensor1 = 5;
const int echoPinSensor2 = 8;
const int trigPinSensor2 = 7;
const int echoPinSensor3 = 10;
const int trigPinSensor3 = 9;
const int echoPinSensor4 = 12;
const int trigPinSensor4 = 11;
const int echoPinSensor5 = 24;
const int trigPinSensor5 = 22;
const int echoPinSensor6 = 26;
const int trigPinSensor6 = 28;
const int stepPin=3;
const int dirPin=4;
//variablile
long duration,distance,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5,Sensor6;

void setup() {
  //Senzorii de Ultrasunete    
  pinMode(trigPinSensor1, OUTPUT); // Setez trigPin ca si Output
  pinMode(echoPinSensor1, INPUT);  // Setez echoPin ca si Input
  pinMode(trigPinSensor2, OUTPUT); 
  pinMode(echoPinSensor2, INPUT); 
  pinMode(trigPinSensor3, OUTPUT); 
  pinMode(echoPinSensor3, INPUT); 
  pinMode(trigPinSensor4, OUTPUT); 
  pinMode(echoPinSensor4, INPUT); 
  pinMode(trigPinSensor5, OUTPUT); 
  pinMode(echoPinSensor5, INPUT); 
  pinMode(trigPinSensor6, OUTPUT); 
  pinMode(echoPinSensor6, INPUT); 
  //Motorul Pas cu Pas
  pinMode(stepPin,OUTPUT); // Setez stepPin ca si Output
  pinMode(dirPin,OUTPUT);  // Setez dirPin ca si Output
  Serial.begin(9600);
}
void loop() {
  //Introducem ca input de la tastatura caracterul "s" in serial pentru a porni programul
  if(Serial.available()){
    char ch=Serial.read();
    if (ch == 's'){
      digitalWrite(dirPin,HIGH); // permite motorului sa se miste intr-o directie
      //Trimitem 200 de pulsatii in stepPin pentru a face o rotatie full(1,8 grade pe pas => 1,8*200=360)
      for(int x = 0; x < 200; x++) {
        digitalWrite(stepPin,HIGH);
        delayMicroseconds(1000);
        //Calculeaza distanta pentru fiecare Senzor
        Sensor1=Distance_Calc(trigPinSensor1,echoPinSensor1);
        Sensor2=Distance_Calc(trigPinSensor2,echoPinSensor2);
        Sensor3=Distance_Calc(trigPinSensor3,echoPinSensor3);
        Sensor4=Distance_Calc(trigPinSensor4,echoPinSensor4);
        Sensor5=Distance_Calc(trigPinSensor5,echoPinSensor5);
        Sensor6=Distance_Calc(trigPinSensor6,echoPinSensor6);
        //Se afiseaza distantele calculate
        Serial.print("Distance Sensor_1: ");
        Serial.println(Sensor1);
        Serial.print("Distance Sensor_2: ");
        Serial.println(Sensor2);
        Serial.print("Distance Sensor_3: ");
        Serial.println(Sensor3);
        Serial.print("Distance Sensor_4: ");
        Serial.println(Sensor4);
        Serial.print("Distance Sensor_5: ");
        Serial.println(Sensor5);
        Serial.print("Distance Sensor_6: ");
        Serial.println(Sensor6);
        digitalWrite(stepPin,LOW); 
        delayMicroseconds(1000);
 
      }
      delay(1000); // delay de o secunda
      //Aducem motorul in punctul de start
      digitalWrite(dirPin,LOW);// permite motorului sa se miste in directia opusa
      for(int x = 0; x < 200; x++) {
        digitalWrite(stepPin,HIGH);
        delayMicroseconds(1000);
        digitalWrite(stepPin,LOW);
        delayMicroseconds(1000);
      }
      delay(1000);
    }
  }
}

int Distance_Calc(int trigPin,int echoPin)
{
    // curata trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(1);
    // pune trigPin pe HIGH state pentru 10 micro secunde
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // citeste echoPin, retuneaza timpul parcurs de sunet in microsecunde 
    duration = pulseIn(echoPin, HIGH);
    // Calculeaza distanta
    distance = duration*0.034/2;

    return distance;
}
