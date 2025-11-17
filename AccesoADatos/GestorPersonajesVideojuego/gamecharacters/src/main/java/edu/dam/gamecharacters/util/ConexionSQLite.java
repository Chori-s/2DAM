package edu.dam.gamecharacters.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ConexionSQLite {
    private static final String URL = "jdbc:sqlite:src/main/resources/game.db";

    public static Connection conectar() throws SQLException {
        return DriverManager.getConnection(URL);
    }

    // Primero se crea la tabla dentro de la bbd si no existe
    public static void inicializar() {
        String sql = """
                CREATE TABLE IF NOT EXISTS personajes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    clase TEXT NOT NULL,
                    nivel INTEGER DEFAULT 1,
                    puntos_vida INTEGER DEFAULT 100
                );
                """;
        try (Connection conn = conectar();
                Statement st = conn.createStatement()) {
            st.execute(sql);
            System.out.println(" La base de datos esta lista, listo para empezar");
        } catch (SQLException e) {
            System.err.println(" Error al inicializar: " + e.getMessage());
        }
    }
}