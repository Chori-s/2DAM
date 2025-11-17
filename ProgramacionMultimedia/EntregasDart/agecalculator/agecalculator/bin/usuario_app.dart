import 'package:agecalculator/base.dart';
import 'package:agecalculator/usuario.dart';

// Aqui creamos una función principal para probar las clases creadas.
void main() {

// Primero creamos un usuario normal
  var u1 = Usuario(
    id: 1,
    username: 'jaimeruiz',
    password: '1234',
    email: 'jaimeruiz@iesvegademijas.es',
    nombre: 'Jaime',
    apellidos: 'Ruiz Medina',
    nacionalidad: 'Española',
    nacimiento: '2000-04-12', 
  );

  print(u1);
  print('Nombre completo: ${u1.nombreCompleto}');
  print('Edad: ${u1.edad}');

// Ahora usamos tambien el copy with
  var u2 = u1.copyWith(password: 'abcd');
  print('\nUsuario modificado con copyWith():\n$u2');

// Creamos un usuario en cadena con los datos 
  var u3 = Usuario.fromString(
    '2,ana,1234,ana@mail.com,Ana,García,Española,2005-06-01',
  );
  print('\nUsuario creado con factory:\n$u3');

// Tambien se hace uno animo
  var anonimo = Usuario.anonimo();
  print('\nUsuario anónimo:\n$anonimo');

// Aqui miro si el contador estatico de antes de numero de instancias funcion
  print('\nNúmero de instancias creadas: ${Base.numInstancias}');

// Y tambien hacemos un usuario inmutable 
  const u4 = UsuarioNoMutable(
    id: 10,
    username: 'pepe',
    password: 'pass',
    email: 'pepe@mail.com',
  );
  print('\nUsuarioNoMutable:\n$u4');
}

class UsuarioNoMutable {
  const UsuarioNoMutable({
    required int id,
    required String username,
    required String password,
    required String email,
  });
}
