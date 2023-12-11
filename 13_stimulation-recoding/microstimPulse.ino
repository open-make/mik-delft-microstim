int stimPin = 8; //which pin to use to turn on the stimulus isolator
int inputPin = 7; //the pin that receives the input from the Arduino DUE with the BPOD shield
void setup() {
  Serial.begin(9600); 
  pinMode(stimPin, OUTPUT); //pin 8 is output
  pinMode(inputPin, INPUT); //pin 7 receives input
}

void loop() {
    if(digitalRead(inputPin, HIGH) { //this means that the UNO receives a ttl from the DUE
        for (int i = 0; i< 40; i++) { //loop that turns pin8 on or off with the delay as frequency 
        digitalWrite(stimPin,HIGH); 
        delay(0.3);
        digitalWrite(stimPin,LOW);
        delay(4.7);
      }
    }
    
    else  {
      digitalWrite(stimPin,LOW); 
    }
  }
}
