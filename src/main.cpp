
#include "Arduino.h"

void setup()
{
  Serial.begin(115200);
  return;
}

void loop()
{
  Serial.println("hello");
  delay(1000);
  return;
}

