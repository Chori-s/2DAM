package es.dam.gamevault;

import es.dam.gamevault.dao.BibliotecaDAO;
import es.dam.gamevault.models.*;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class TestCRUD {
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════════╗");
        System.out.println("║   TEST DE OPERACIONES CRUD CON HIBERNATE   ║");
        System.out.println("╚════════════════════════════════════════════╝\n");

        SessionFactory factory = null;

        try {
            factory = new Configuration()
                    .configure("hibernate.cfg.xml")
                    .addAnnotatedClass(Usuario.class)
                    .addAnnotatedClass(Videojuego.class)
                    .addAnnotatedClass(Prestamo.class)
                    .buildSessionFactory();

            BibliotecaDAO dao = new BibliotecaDAO(factory);

            // ==================== CREATE ====================
            System.out.println("\n" + "=".repeat(50));
            System.out.println("CREATE - Insertando datos");
            System.out.println("=".repeat(50) + "\n");

            Long usuario1Id = dao.crearUsuario("Juan Pérez", "juan.perez@email.com");
            Long usuario2Id = dao.crearUsuario("María García", "maria.garcia@email.com");
            Long usuario3Id = dao.crearUsuario("Carlos López", "carlos.lopez@email.com");

            Long juego1Id = dao.crearVideojuego("The Legend of Zelda: Tears of the Kingdom", "Nintendo Switch", 69.99,
                    "Aventura", 2023);
            Long juego2Id = dao.crearVideojuego("Elden Ring", "PS5", 59.99, "RPG", 2022);
            Long juego3Id = dao.crearVideojuego("FIFA 24", "Xbox Series X", 69.99, "Deportes", 2023);
            Long juego4Id = dao.crearVideojuego("Baldur's Gate 3", "PC", 59.99, "RPG", 2023);

            Long prestamo1Id = dao.crearPrestamo(usuario1Id, juego1Id);
            Long prestamo2Id = dao.crearPrestamo(usuario2Id, juego2Id);
            Long prestamo3Id = dao.crearPrestamo(usuario3Id, juego3Id);

            Thread.sleep(2000);

            // ==================== UPDATE ====================
            System.out.println("\n" + "=".repeat(50));
            System.out.println("UPDATE - Actualizando datos");
            System.out.println("=".repeat(50) + "\n");

            dao.actualizarEmailUsuario(usuario1Id, "juan.perez.nuevo@email.com");
            dao.aplicarOferta(juego2Id, 39.99);
            dao.aplicarOferta(juego4Id, 44.99);
            dao.registrarDevolucion(prestamo1Id);

            Thread.sleep(2000);

            // ==================== DELETE ====================
            System.out.println("\n" + "=".repeat(50));
            System.out.println("DELETE - Eliminando datos");
            System.out.println("=".repeat(50) + "\n");

            System.out.println("Intentando eliminar usuario con préstamos activos:");
            dao.eliminarUsuario(usuario2Id);

            dao.eliminarPrestamo(prestamo3Id);

            System.out.println("Eliminando usuario sin préstamos activos:");
            dao.eliminarUsuario(usuario3Id);

            dao.eliminarVideojuego(juego4Id);

            // ==================== RESUMEN ====================
            System.out.println("\n" + "=".repeat(50));
            System.out.println("RESUMEN DE OPERACIONES");
            System.out.println("=".repeat(50));
            System.out.println("Usuarios creados: 3");
            System.out.println("Videojuegos creados: 4");
            System.out.println("Préstamos creados: 3");
            System.out.println("Actualizaciones realizadas: 4");
            System.out.println("Devolución registrada: 1");
            System.out.println("Eliminaciones realizadas: 3");
            System.out.println("=".repeat(50));

            System.out.println("\n╔════════════════════════════════════════════╗");
            System.out.println("║         TEST COMPLETADO CORRECTAMENTE      ║");
            System.out.println("╚════════════════════════════════════════════╝");

        } catch (Exception e) {
            System.err.println("\nERROR: " + e.getMessage());
            e.printStackTrace();
        } finally {
            if (factory != null) {
                factory.close();
                System.out.println("\nSessionFactory cerrada correctamente");
            }
        }
    }
}
