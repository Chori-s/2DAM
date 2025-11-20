package es.dam.gamevault;

import es.dam.gamevault.models.*;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class TestMapeo {

    public static void main(String[] args) {
        System.out.println("=== INICIANDO TEST DE MAPEO ===\n");

        SessionFactory factory = null;

        try {
            System.out.println("1. Configurando Hibernate...");

            factory = new Configuration()
                    .configure("hibernate.cfg.xml")
                    .addAnnotatedClass(Usuario.class)
                    .addAnnotatedClass(Videojuego.class)
                    .addAnnotatedClass(Prestamo.class)
                    .buildSessionFactory();

            System.out.println("Hibernate configurado correctamente");
            System.out.println("Tablas creadas en la base de datos\n");

            System.out.println("Revisa tu base de datos para ver las tablas:");
            System.out.println("   - usuarios");
            System.out.println("   - videojuegos");
            System.out.println("   - prestamos");

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        } finally {
            if (factory != null) {
                factory.close();
                System.out.println("\nSessionFactory cerrada correctamente");
            }
        }

        System.out.println("\n=== TEST COMPLETADO ===");
    }
}
