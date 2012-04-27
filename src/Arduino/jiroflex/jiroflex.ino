unsigned const LED_START = 11; 
unsigned const LED_STOP = 12;
unsigned const BAUD = 9600;

boolean stopState = 0;
int taskState = 0;


void setup()
{
  Serial.begin(BAUD);
  pinMode(LED_START, OUTPUT);
  pinMode(LED_STOP, OUTPUT);  
}

void loop()
{
  
    if (Serial.available() > 0) {
        taskState = Serial.read() - '0';
    }

    if (taskState == 1) {
      taskStarted();
    } else if (taskState == 0) {
      taskStopped();
    } else {
      off(); 
    }
}

void taskStopped()
{
  digitalWrite(LED_STOP, stopState);
  digitalWrite(LED_START, 0);

  stopState = !stopState;
  delay(100);
}

void taskStarted()
{
  digitalWrite(LED_START, HIGH);  
  digitalWrite(LED_STOP, LOW);
}

void off()
{
  digitalWrite(LED_START, LOW);
  digitalWrite(LED_STOP, LOW); 
}
