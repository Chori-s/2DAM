import 'package:flutter/material.dart';

class Saludo extends StatelessWidget {
  final String nomnbre;
const Saludo(this.nomnbre, {super.key});


  @override
  Widget build(BuildContext context) {
    return Text('Hola, $nomnbre!');
  }
} 