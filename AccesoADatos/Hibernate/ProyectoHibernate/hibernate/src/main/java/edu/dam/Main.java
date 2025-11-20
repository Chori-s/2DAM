package edu.dam;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Main {
    public static void main(String[] args) {

        try {
            // Carga hibernate.cfg.xml automáticamente
            Configuration config = new Configuration().configure();

            // Si luego usas entidades, las añades así:
            // config.addAnnotatedClass(MiEntidad.class);

            SessionFactory factory = config.buildSessionFactory();
            Session session = factory.openSession();

            System.out.println("Conexión exitosa con la base de datos mediante Hibernate");

            session.close();
            factory.close();

        } catch (Exception e) {
            System.out.println(" Error conectando con Hibernate");
            e.printStackTrace();
        }
    }
}
