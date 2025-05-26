/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.registroempleados.util;

/**
 *
 * @author Jhon Sanchez
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class conexionOracle {
    public static Connection getConnection() throws SQLException {
        String url = "jdbc:oracle:thin:@oracle-db:1522:XE"; // oracle-db es el nombre del contenedor Docker
        String user = "system";
        String password = "oracle";
        return DriverManager.getConnection(url, user, password);
    }
}
