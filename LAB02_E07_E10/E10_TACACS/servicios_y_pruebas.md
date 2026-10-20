# E10 — Servicios y pruebas

## Módulos y red

En Physical, apagar ambos 2911, colocar HWIC-2T en el slot que produzca Serial0/0/0, volver a encender y comprobar el nombre de interfaz. No cambiar por otra numeración sin documentar la diferencia respecto al PDF. Seleccionar cable Serial DCE y conectar primero R-LIMA para que sea DCE. Confirmar con `show controllers s0/0/0`: solo R-LIMA lleva clock rate 64000.

Aplicar primero interfaces y OSPF, comprobar vecino FULL y ping entre sedes. Después configurar servidor, localadmin, SSH, AAA y líneas. Mantener consola de recuperación abierta y guardar un proyecto intermedio antes de AAA.

## Hosts y servidor

Configurar hosts estáticos según montaje.md. SRV-TACACS > Services > AAA > On, tipo Tacacs y clave `TacacsURP2026` para:

| Cliente | IP de origen prevista, por confirmar |
|---|---|
| R-LIMA | 10.10.10.1 |
| R-AREQ | 172.30.0.2 |
| SW-AREQ | 10.20.20.2 |

Verificar origen real con Simulation/debug y corregir el registro si fuera necesario. Crear `netadmin` / `Net2026` y `auditor` / `Audit2026`. localadmin / Local2026 solo se crea en los tres equipos cliente, no en el servidor. SW-LIMA es un switch de acceso: no se inventa IP de gestión ni se registra como cliente TACACS+.

Decisiones para SSH no fijadas por el PDF de E10: dominio urp.lab y RSA 1024 bits, siguiendo el valor didáctico de E09 y sujeto al soporte de Packet Tracer; comprobar generación interactiva y documentar su aceptación. SW-AREQ permite Telnet conforme al requisito del ejercicio y aplica AAA a VTY 0–15.

## Pruebas y evidencias

1. `show controllers s0/0/0` en ambos routers, `show ip interface brief`, `show ip ospf neighbor`, `show ip route`. Esperar vecindad FULL y rutas OSPF a la LAN opuesta. Ping PC-NOC ↔ PC-AQP y desde cada cliente AAA a 10.10.10.100.
2. En clientes: `show running-config | include aaa|tacacs`. En routers: `show ip ssh`. Activar `debug tacacs` y `debug aaa authentication` durante un inicio de sesión; capturar y ejecutar `undebug all`. Si un comando no es aceptado, guardar el error, consultar `debug ?` y usar solo una alternativa admitida, documentándola.
3. En PC-AQP: `ssh -l netadmin 10.20.20.1` con Net2026 y `telnet 10.20.20.2` con netadmin / Net2026. En PC-NOC: `ssh -l auditor 10.20.20.1` con Audit2026. Capturar resultados. Probar también consola AAA en los tres clientes y acceso a R-LIMA para verificar que está registrado.
4. Prueba de respaldo en R-AREQ, conservando una consola de recuperación:

```cisco
enable
configure terminal
interface Serial0/0/0
 shutdown
end
```

Confirmar caída de WAN y pérdida de acceso a SRV-TACACS. Abrir una autenticación nueva por consola (salir de la sesión de prueba; no basta una sesión preexistente), esperar timeout e ingresar localadmin / Local2026. Si se necesita cable de consola, conectar temporalmente RS232 de PC-AQP al Console de R-AREQ con cable azul, Desktop > Terminal, valores predeterminados. No usar SSH cruzando la WAN como prueba de fallback.

5. Restaurar desde consola en R-AREQ:

```cisco
enable
configure terminal
interface Serial0/0/0
 no shutdown
end
```

Esperar OSPF FULL, comprobar ping y volver a autenticar netadmin/auditor contra el servidor. Desactivar debug, guardar running-config en startup-config y guardar `.pkt`. Reabrirlo y verificar OSPF y autenticación. Retirar cable de consola temporal si se quiere replicar exactamente la figura. No afirmar autorización por comando/accounting: este ejercicio configura autenticación, aunque TACACS+ permite separar los tres servicios.
