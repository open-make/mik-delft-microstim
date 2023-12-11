// The Arduino DUE is used to transfer the signal from the BPOD to the pulse-configuring Arduino UNO.
// We have to ues the DUE, because the BPOD only interfaces through a BPOD shield: https://sanworks.github.io/Bpod_Wiki/assembly/arduino-shield-gen2-assembly/. But the DUE only outputs 3.3V

int stimPin = 8; // Pin to send TTL signal from DUE to UNO

void setup() {
  Serial.begin(1312500); // Set serial communication rate to match the BPOD
  pinMode(stimPin, OUTPUT); // Set pin 8 as an output
}

void loop() {
  if (Serial.available() > 0) { // Check if there's incoming data
    char data_rcvd = Serial.read(); // Read the received data
    if (data_rcvd == '1') {
      digitalWrite(stimPin, HIGH); // Send HIGH signal to the UNO
    } else if (data_rcvd == '0') {
      digitalWrite(stimPin, LOW); // Send LOW signal to the UNO
    }
  }
}
