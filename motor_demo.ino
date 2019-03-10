/*
* This file controls the direction of the motor for demo purposes
* Pressing the button turns the motor one direction. 
* Pressing the button again stops the motor and pressing it again 
* turn it the other direction and so on. (for Arduino)
*/

int inPin = 8;   // choose the input pin (for a pushbutton)
int reading = 0;     // variable for reading the pin status
int E1 = 6;
int M1 = 7;
int E2Pin = 11;
int M2Pin = 13;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT); 
  pinMode(inPin, INPUT);    // declare pushbutton as input
  pinMode(E1, OUTPUT);
  pinMode(M1, OUTPUT);
  Serial.begin(9600); 
}

bool state = 1;
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers
int buttonState;

bool last_Button = 0;
int motor_val = 255;
void loop(){

  int reading = digitalRead(inPin);  // read input value
  if (reading != last_Button) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }
  //Serial.println(millis() - lastDebounceTime);
  //filter out any noise by setting a time buffer
  
  if ( (millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      //Serial.println("here");
      if(buttonState == LOW){
        digitalWrite(LED_BUILTIN, LOW); 
        Serial.println("MOTOR STOP");
        digitalWrite(M1,LOW);
        digitalWrite(E1,LOW);
        state = !state;
      }
      if(buttonState == HIGH){
        digitalWrite(LED_BUILTIN, HIGH); 
        Serial.print("MOTOR RUN: ");
        if(state == 1){
          Serial.println("FORWARD");
          digitalWrite(M1,LOW);
          digitalWrite(E1,LOW);   
          digitalWrite(M1,LOW);
          analogWrite(E1,motor_val);
        }
        if(state == 0){
          Serial.println("BACKWARDS");
          digitalWrite(M1,LOW);
          digitalWrite(E1,LOW);
          digitalWrite(M1,HIGH);
          analogWrite(E1,motor_val);
        }
      }
    }
  }
  last_Button = reading;
}
    
