import 'dart:io';
import 'dart:math';

// Primero añadimos un parametro [max], que define el número máximo posible, donde el usuario pone el numero
// El valor no puede modificarse dentro del procedimiento.
void adivinaElNumero({required int max}) {
  // Bucle principal para permitir que el usuario juegue varias veces.
  bool jugarOtraVez = true;

  while (jugarOtraVez) {
    print('¡Bienvenido! Esto es ADIVINA EL NÚMERO');
    print('Estoy pensando en un número entre 0 y $max. ¿Cuál será?');

    // Se genera un número aleatorio entre 0 y max.
    var numeroSecreto = Random().nextInt(max + 1);

    int intentos = 0;
    bool acertado = false;

    // Bucle que se repite hasta que el jugador adivine el número.
    while (!acertado) {
      stdout.write('Intento ${intentos + 1}: ');
      String? entrada = stdin.readLineSync();

      // Ahora aqui tenemos varios controles de posible error, verificar que el valor de lo que pone el usuario sea numérico, no una letra o cadena por ejemplo.
      if (entrada == null) {
        print('Por favor, introduce algo.');
        continue;
      }

      int? numero = int.tryParse(entrada);

      if (numero == null) {
        print('Por favor, introduce un número válido.');
        continue;
      }

      if (numero < 0 || numero > max) {
        print('El número debe estar entre 0 y $max.');
        continue;
      }

      intentos++;

      if (numero > numeroSecreto) {
        print('Te has pasado.');
      } else if (numero < numeroSecreto) {
        print('No llegas.');
      } else {
        print('¡SÍ! ¡ESE ES EL NÚMERO! ');
        print('Descubrirlo te ha llevado $intentos intentos.');
        acertado = true;
      }
    }

    // Preguntar si desea jugar de nuevo
    stdout.write('\n¿Quieres jugar de nuevo? (s/n): ');
    String? respuesta = stdin.readLineSync();

    if (respuesta == null || respuesta.toLowerCase() != 's') {
      jugarOtraVez = false;
      print('¡Gracias por jugar!');
    } else {
      print('\n------------------------------\n');
    }
  }
}

// Esta funcion es la entrada del programa
void main() {
  adivinaElNumero(max: 1000);
}
