package es.dam.gamevault.models;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "videojuegos")
public class Videojuego {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String titulo;
    private String plataforma;
    private double precio;
    private String genero;
    private int anio;

    @OneToMany(mappedBy = "videojuego", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    private List<Prestamo> prestamos = new ArrayList<>();

    public Videojuego() {
    }

    public Videojuego(String titulo, String plataforma, double precio, String genero, int anio) {
        this.titulo = titulo;
        this.plataforma = plataforma;
        this.precio = precio;
        this.genero = genero;
        this.anio = anio;
    }

    // Getters y setters

    public Long getId() {
        return id;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getPlataforma() {
        return plataforma;
    }

    public double getPrecio() {
        return precio;
    }

    public String getGenero() {
        return genero;
    }

    public int getAnio() {
        return anio;
    }

    public List<Prestamo> getPrestamos() {
        return prestamos;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "Videojuego{id=" + id + ", titulo='" + titulo + "', plataforma='" + plataforma + "', precio=" + precio
                + "}";
    }
}
