package es.dam.gamevault.models;

import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "prestamos")
public class Prestamo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDate fechaPrestamo;
    private LocalDate fechaDevolucion;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "usuario_id")
    private Usuario usuario;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "videojuego_id")
    private Videojuego videojuego;

    public Prestamo() {
    }

    public Prestamo(Usuario usuario, Videojuego videojuego) {
        this.usuario = usuario;
        this.videojuego = videojuego;
        this.fechaPrestamo = LocalDate.now();
    }

    // Getters y setters

    public Long getId() {
        return id;
    }

    public LocalDate getFechaPrestamo() {
        return fechaPrestamo;
    }

    public LocalDate getFechaDevolucion() {
        return fechaDevolucion;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public Videojuego getVideojuego() {
        return videojuego;
    }

    public void setFechaDevolucion(LocalDate fechaDevolucion) {
        this.fechaDevolucion = fechaDevolucion;
    }

    @Override
    public String toString() {
        return "Prestamo{id=" + id + ", fechaPrestamo=" + fechaPrestamo + ", fechaDevolucion=" + fechaDevolucion + "}";
    }
}
