#include "DHT.h"

#define DHTPIN 15
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  float umid = dht.readHumidity();

  if (isnan(temp) || isnan(umid)) {
    Serial.println("Erro na leitura do sensor!");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temp);
  Serial.print(" °C | Umidade: ");
  Serial.print(umid);
  Serial.println(" %");

  delay(3000);
}
