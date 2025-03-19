#include <PubSubClient.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>

// 設定 WiFi 連線資訊
const char* ssid = "YOUR WIFI SSID";
const char* password = "YOUR WIFI PASSWORD";
const char* mqtt_server = "YOUR LAPTOP IP";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
    delay(10);
    Serial.println("[INFO] Connecting to WiFi...");
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\n[INFO] WiFi Connected!");
    Serial.println(WiFi.localIP());
}

void reconnect_mqtt() {
    while (!client.connected()) {
        Serial.print("[INFO] Connecting to MQTT Broker...");
        String clientId = "ESP8266-" + String(ESP.getChipId());
        if (client.connect(clientId.c_str())) {
            Serial.println(" connected!");
        } else {
            Serial.print(" failed, rc=");
            Serial.print(client.state());
            Serial.println(" retrying in 5 seconds...");
            delay(5000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    setup_wifi();
    client.setServer(mqtt_server, mqtt_port);
}

void loop() {
    if (!client.connected()) {
        reconnect_mqtt();
    }
    client.loop();
    
    int temperature = random(0, 30);  // 模擬溫度數據
    String topic = "home/" + String(ESP.getChipId());
    Serial.printf("[%s]: 現在溫度：%d\n", topic.c_str(), temperature);
    client.publish(topic.c_str(), String(temperature).c_str());
    
    delay(2000);
}
