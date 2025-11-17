// Esta clase abstracta sirve como superclase, la propiedad de context puede ser cualquier objeto de la clase Base. Y un contador estatico de instancias que se van creando.

abstract class Base {
  final Base? context;
  static int _numInstancias = 0;

  Base({this.context}) {
    _numInstancias++;
  }

  static int get numInstancias => _numInstancias;
}
