#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "your wifi access point name";
const char* password = "your wifi password";
const char* mqtt_server = "your MQTT IP address";
const int buttonPin = D6;
const char* topic = "button_1";
const char* message = "Button 1 pressed";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
  setup_wifi();
  randomSeed(micros());
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  if (digitalRead(buttonPin) == LOW) {
    Serial.println("Publish button pressed ");
    client.publish(topic, message);
    delay(100);
    while (digitalRead(buttonPin) == LOW) {};
    delay(100);
  }
}

void setup_wifi() {
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("MQTT connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


