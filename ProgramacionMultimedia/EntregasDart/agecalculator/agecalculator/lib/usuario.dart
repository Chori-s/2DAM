import 'package:age_calculator/age_calculator.dart';
import 'base.dart';

// Clase basica que hereda de la superclase
class Usuario extends Base {
  // Estas clases hay que rellenarlas obligatoriamente
  int id;
  String username;
  String password;
  String email;
  // Estas propiedades son nulables por eso el "?"
  String? nombre;
  String? apellidos;
  String? nacionalidad;
  DateTime? nacimiento;
  final DateTime creacion = DateTime.now();

  Usuario({
    required this.id,
    required this.username,
    required this.password,
    required this.email,
    this.nombre,
    this.apellidos,
    this.nacionalidad,
    String? nacimiento,
    Base? context,
  }) : nacimiento = nacimiento != null ? DateTime.tryParse(nacimiento) : null,
       super(context: context);

  String get nombreCompleto => '${nombre ?? ''} ${apellidos ?? ''}'.trim();

  int? get edad =>
      nacimiento == null ? null : AgeCalculator.age(nacimiento!).years;

  // Método copyWith() que crea una nueva instancia copiando el objeto actual,
  // pero con los valores modificados indicados en los parámetros.
  Usuario copyWith({
    int? id,
    String? username,
    String? password,
    String? email,
    String? nombre,
    String? apellidos,
    String? nacionalidad,
    String? nacimiento,
    Base? context,
  }) {
    return Usuario(
      id: id ?? this.id,
      username: username ?? this.username,
      password: password ?? this.password,
      email: email ?? this.email,
      nombre: nombre ?? this.nombre,
      apellidos: apellidos ?? this.apellidos,
      nacionalidad: nacionalidad ?? this.nacionalidad,
      nacimiento: nacimiento ?? this.nacimiento?.toIso8601String(),
      context: context ?? this.context,
    );
  }

  // Constructor nombrado para crear un usuario anónimo.
  Usuario.anonimo()
    : id = 0,
      username = '',
      password = '',
      email = '',
      nombre = null,
      apellidos = null,
      nacionalidad = null,
      nacimiento = null,
      super(context: null);

//Este constructor factory recibe los datos en CSV y devuelve un nuevo objeto Usuario
  factory Usuario.fromString(String datos) {
    var partes = datos.split(',');
    return Usuario(
      id: int.parse(partes[0]),
      username: partes[1],
      password: partes[2],
      email: partes[3],
      nombre: partes.length > 4 ? partes[4] : null,
      apellidos: partes.length > 5 ? partes[5] : null,
      nacionalidad: partes.length > 6 ? partes[6] : null,
      nacimiento: partes.length > 7 ? partes[7] : null,
    );
  }

// Hay que sobreescribir el to string para que se vean bien los datos
  @override
  String toString() =>
      '''
Usuario(
  Id: $id
  Username: $username
  Password: $password
  Email: $email
  Nombre: ${nombre ?? '-'}
  Apellidos: ${apellidos ?? '-'}
  Nacionalidad: ${nacionalidad ?? '-'}
  Fecha de nacimiento: ${nacimiento != null ? nacimiento!.toIso8601String() : '-'}
  Edad: ${edad ?? '-'}
  Creación: $creacion
)
''';
}
