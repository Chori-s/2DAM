package es.dam.gamevault.dao;

import es.dam.gamevault.models.*;
import org.hibernate.Hibernate;
import org.hibernate.ObjectNotFoundException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import java.time.LocalDate;

public class BibliotecaDAO {
    private final SessionFactory factory;

    public BibliotecaDAO(SessionFactory factory) {
        this.factory = factory;
    }

    // ==================== CRUD ====================

    public Long crearUsuario(String nombre, String email) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Usuario usuario = new Usuario(nombre, email);
            session.persist(usuario);
            tx.commit();
            System.out.println(" Usuario creado: " + usuario);
            return usuario.getId();
        }
    }

    public Long crearVideojuego(String titulo, String plataforma, double precio, String genero, int anio) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Videojuego juego = new Videojuego(titulo, plataforma, precio, genero, anio);
            session.persist(juego);
            tx.commit();
            System.out.println(" Videojuego creado: " + juego);
            return juego.getId();
        }
    }

    public Long crearPrestamo(Long idUsuario, Long idJuego) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Usuario usuario = session.get(Usuario.class, idUsuario);
            Videojuego juego = session.get(Videojuego.class, idJuego);
            Prestamo prestamo = new Prestamo(usuario, juego);
            session.persist(prestamo);
            tx.commit();
            System.out.println(" Préstamo creado: " + prestamo);
            return prestamo.getId();
        }
    }

    public void actualizarEmailUsuario(Long idUsuario, String nuevoEmail) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Usuario usuario = session.get(Usuario.class, idUsuario);
            if (usuario != null) {
                usuario.setEmail(nuevoEmail);
                session.merge(usuario);
                tx.commit();
                System.out.println(" Email actualizado: " + usuario);
            }
        }
    }

    public void aplicarOferta(Long idVideojuego, double nuevoPrecio) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Videojuego juego = session.get(Videojuego.class, idVideojuego);
            if (juego != null) {
                juego.setPrecio(nuevoPrecio);
                session.merge(juego);
                tx.commit();
                System.out.println("Precio actualizado: " + juego);
            }
        }
    }

    public void registrarDevolucion(Long idPrestamo) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Prestamo prestamo = session.get(Prestamo.class, idPrestamo);
            if (prestamo != null) {
                prestamo.setFechaDevolucion(LocalDate.now());
                session.merge(prestamo);
                tx.commit();
                System.out.println("Devolución registrada: " + prestamo);
            }
        }
    }

    public void eliminarUsuario(Long idUsuario) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Usuario usuario = session.get(Usuario.class, idUsuario);
            if (usuario != null && usuario.getPrestamos().isEmpty()) {
                session.remove(usuario);
                tx.commit();
                System.out.println(" Usuario eliminado: " + usuario);
            } else {
                System.out.println(" No se puede eliminar: tiene préstamos activos");
            }
        }
    }

    public void eliminarPrestamo(Long idPrestamo) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Prestamo prestamo = session.get(Prestamo.class, idPrestamo);
            if (prestamo != null) {
                session.remove(prestamo);
                tx.commit();
                System.out.println(" Préstamo eliminado: " + prestamo);
            }
        }
    }

    public void eliminarVideojuego(Long idVideojuego) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Videojuego juego = session.get(Videojuego.class, idVideojuego);
            if (juego != null && juego.getPrestamos().isEmpty()) {
                session.remove(juego);
                tx.commit();
                System.out.println(" Videojuego eliminado: " + juego);
            } else {
                System.out.println(" No se puede eliminar: tiene préstamos activos");
            }
        }
    }

    // ==================== Parte 3: Búsquedas y carga ====================

    public void buscarUsuarioConGet(Long id) {
        try (Session session = factory.openSession()) {
            Usuario usuario = session.get(Usuario.class, id);
            System.out.println(usuario != null ? usuario : "No existe usuario con ID " + id);
        }
    }

    public void buscarJuegoConGet(Long id) {
        try (Session session = factory.openSession()) {
            Videojuego juego = session.get(Videojuego.class, id);
            System.out.println(juego != null ? juego : "No existe videojuego con ID " + id);
        }
    }

    public void buscarUsuarioConLoad(Long id) {
        try (Session session = factory.openSession()) {
            Usuario usuario = session.load(Usuario.class, id);
            System.out.println("Proxy devuelto por load(): " + usuario.getClass());
            System.out.println("Accediendo a propiedades: " + usuario.getNombre());
        }
    }

    public void demostrarLoadConIdInexistente() {
        try (Session session = factory.openSession()) {
            Usuario usuario = session.load(Usuario.class, 9999L);
            System.out.println(usuario.getNombre());
        } catch (ObjectNotFoundException e) {
            System.err.println(" ObjectNotFoundException: " + e.getMessage());
        }
    }

    public void demostrarLazyLoading(Long idUsuario) {
        try (Session session = factory.openSession()) {
            Usuario usuario = session.get(Usuario.class, idUsuario);
            System.out.println("Usuario cargado: " + usuario.getNombre());
            usuario.getPrestamos().forEach(System.out::println);
        }
    }

    public void demostrarLazyInitializationException(Long idUsuario) {
        Usuario usuario;
        try (Session session = factory.openSession()) {
            usuario = session.get(Usuario.class, idUsuario);
        }
        try {
            usuario.getPrestamos().forEach(System.out::println);
        } catch (Exception e) {
            System.err.println(" LazyInitializationException: " + e.getMessage());
        }
    }

    public void solucionLazyInitializationException(Long idUsuario) {
        try (Session session = factory.openSession()) {
            Usuario usuario = session.get(Usuario.class, idUsuario);
            Hibernate.initialize(usuario.getPrestamos());
            usuario.getPrestamos().forEach(System.out::println);
        }
    }

    public void compararRendimientoGetVsLoad() {
        long inicio = System.currentTimeMillis();
        try (Session session = factory.openSession()) {
            session.get(Usuario.class, 1L);
        }
        long tiempoGet = System.currentTimeMillis() - inicio;

        inicio = System.currentTimeMillis();
        try (Session session = factory.openSession()) {
            session.load(Usuario.class, 1L);
        }
        long tiempoLoad = System.currentTimeMillis() - inicio;

        System.out.println("Tiempo con get(): " + tiempoGet + " ms");
        System.out.println("Tiempo con load(): " + tiempoLoad + " ms");
    }

    public Long crearPrestamoOptimizadoConLoad(Long idUsuario, Long idJuego) {
        try (Session session = factory.openSession()) {
            Transaction tx = session.beginTransaction();
            Usuario usuario = session.load(Usuario.class, idUsuario);
            Videojuego juego = session.load(Videojuego.class, idJuego);
            Prestamo prestamo = new Prestamo(usuario, juego);
            session.persist(prestamo);
            tx.commit();
            return prestamo.getId();
        }
    }
}
