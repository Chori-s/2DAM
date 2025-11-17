package edu.dam.gamecharacters.app;

import edu.dam.gamecharacters.dao.CharacterDAO;
import edu.dam.gamecharacters.model.Character;
import edu.dam.gamecharacters.util.ConexionSQLite;

public class App {
    public static void main(String[] args) {
        try {

            // Al iniciar el programa tambien hay que iniciar la bbdd
            ConexionSQLite.inicializar();

            CharacterDAO dao = new CharacterDAO();

            System.out.println("\n === CREANDO PERSONAJES === 🎮");
            dao.insertar(new Character("Aragorn", "Guerrero", 10, 150));
            dao.insertar(new Character("Gandalf", "Mago", 50, 80));
            dao.insertar(new Character("Legolas", "Arquero", 15, 120));

            System.out.println("\n === LISTA DE PERSONAJES === ");
            dao.listar().forEach(System.out::println);

            System.out.println("\n⬆ === SUBIENDO DE NIVEL === ⬆");

            Character aragorn = new Character();
            aragorn.setId(1);
            aragorn.setNombre("Aragorn");
            aragorn.setNivel(11);
            aragorn.setPuntosVida(170);
            dao.actualizar(aragorn);

            System.out.println("\n === ELIMINANDO PERSONAJE === ");
            dao.eliminar(2);

            System.out.println("\n === LISTA FINAL === ");
            dao.listar().forEach(System.out::println);

        } catch (Exception e) {
            System.err.println(" Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}