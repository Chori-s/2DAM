package es.dam.gamevault;

import es.dam.gamevault.dao.BibliotecaDAO;
import es.dam.gamevault.models.*;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class TestBusquedas {
    public static void main(String[] args) {
        System.out.println("╔═══════════════════════════════════════════════╗");
        System.out.println("║  TEST DE BÚSQUEDAS Y ESTRATEGIAS DE CARGA     ║");
        System.out.println("╚═══════════════════════════════════════════════╝\n");

        SessionFactory factory = null;

        try {
            factory = new Configuration()
                    .configure("hibernate.cfg.xml")
                    .addAnnotatedClass(Usuario.class)
                    .addAnnotatedClass(Videojuego.class)
                    .addAnnotatedClass(Prestamo.class)
                    .buildSessionFactory();

            BibliotecaDAO dao = new BibliotecaDAO(factory);

            // TEST 1: GET
            dao.buscarUsuarioConGet(1L);
            pausa(1500);
            dao.buscarJuegoConGet(1L);
            pausa(1500);
            dao.buscarUsuarioConGet(9999L);
            pausa(2000);

            // TEST 2: LOAD
            dao.buscarUsuarioConLoad(1L);
            pausa(2000);
            dao.demostrarLoadConIdInexistente();
            pausa(2000);

            // TEST 3: LAZY LOADING
            dao.demostrarLazyLoading(1L);
            pausa(2000);

            // TEST 4: LAZY INITIALIZATION EXCEPTION
            dao.demostrarLazyInitializationException(1L);
            pausa(2000);
            dao.solucionLazyInitializationException(1L);
            pausa(2000);

            // TEST 5: COMPARACIÓN DE RENDIMIENTO
            dao.compararRendimientoGetVsLoad();
            pausa(2000);

            // TEST 6: CASO DE USO REAL
            Long prestamoId = dao.crearPrestamoOptimizadoConLoad(2L, 2L);
            if (prestamoId != null) {
                System.out.println("ID del nuevo préstamo: " + prestamoId);
            }

            System.out.println("\n╔═══════════════════════════════════════════════╗");
            System.out.println("║           TEST COMPLETADO CORRECTAMENTE       ║");
            System.out.println("╚═══════════════════════════════════════════════╝");

        } catch (Exception e) {
            System.err.println("\n ERROR CRÍTICO: " + e.getMessage());
            e.printStackTrace();
        } finally {
            if (factory != null) {
                factory.close();
                System.out.println("\n SessionFactory cerrada correctamente");
            }
        }
    }

    private static void pausa(int milisegundos) {
        try {
            Thread.sleep(milisegundos);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
