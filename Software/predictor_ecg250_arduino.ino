const int pinBoton = 2;  // El número del pin al que está conectado el botón
const int pinECG = A0;   // El número del pin analógico al que está conectado el sensor ECG
const int pinLED = 4;
bool adquiriendoDatos = false;
const int retardo_lectura = 2;
int cont=0;

void setup() {
  Serial.begin(9600);     // Inicializar la comunicación serial a 9600 bps
  pinMode(pinBoton, INPUT_PULLUP); // Configurar el pin del botón como entrada con resistencia pull-up interna
  pinMode(pinLED, OUTPUT);   // Configurar el pin del LED como salida
}

void loop() {
  if (digitalRead(pinBoton) == LOW) {
    // Si el botón está presionado, iniciar la lectura durante 10 segundos
    delay(500);  // Pequeño retardo para evitar lecturas accidentales por el rebote del botón
    adquiriendoDatos = true;
    digitalWrite(pinLED, HIGH); // Encender el LED al iniciar la adquisición
    iniciarAdquisicion();
    digitalWrite(pinLED, LOW);  // Apagar el LED al finalizar la adquisición
    adquiriendoDatos = false;
    cont = 0;
  }
}

void iniciarAdquisicion() {
  Serial.println("START");  // Enviar la señal "START" al programa en Python
  
  while (adquiriendoDatos && (cont < 1250)) {
    // Leer el valor del ECG
    int valor_ecg = analogRead(pinECG);

    // Enviar el valor del ECG a través de la comunicación serial
    Serial.print(valor_ecg);
    Serial.print(','); // Agrega una coma para separar los valores
    delay(retardo_lectura); // Pequeño retardo para estabilizar la comunicación serial
    cont++;
  }
  Serial.println();
  delay(500); // Pequeño retardo antes de reiniciar el bucle
}