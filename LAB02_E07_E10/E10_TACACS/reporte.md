# Laboratorio 02 — Ejercicio 10

Alumno: **Andre Torres** · Código: **202210073**
Packet Tracer objetivo: **9.0.1.0858**. Sección/grupo y fecha de entrega: completar por el alumno.

## Estado y alcance

Se generó un `.pkt` offline con pkt-core 0.2.0 y se verificó su recarga con el codec. No se ha abierto en Cisco Packet Tracer: no está instalado aquí. No hay resultados de ping, DHCP, SSH, OSPF o AAA ejecutados. Ver LEEME_PRIMERO.md para ajustes manuales pendientes. La sintaxis IOS incrustada requiere validación en los equipos simulados.

## Topología y direccionamiento

Ver `montaje.md` para equipos, cableado y disposición de la figura original. `figura_fuente.png` es una reproducción de la fuente, no una captura del montaje. Insertar aquí una captura propia después de construirlo.

| Equipo | Interfaz | Dirección/prefijo objetivo | Gateway |
|---|---|---|---|
| R-LIMA | G0/0 | 10.10.10.1/24 | — |
| R-LIMA | S0/0/0 DCE | 172.30.0.1/30 | — |
| R-AREQ | S0/0/0 | 172.30.0.2/30 | — |
| R-AREQ | G0/0 | 10.20.20.1/24 | — |
| SW-AREQ | VLAN 1 | 10.20.20.2/24 | 10.20.20.1 |
| SRV-TACACS | NIC | 10.10.10.100/24 | 10.10.10.1 |
| PC-NOC | NIC | 10.10.10.20/24 | 10.10.10.1 |
| PC-AQP | NIC | 10.20.20.20/24 | 10.20.20.1 |

/24 = 255.255.255.0; /30 = 255.255.255.252. Tabla extraída de la fuente, pendiente de contraste con configuración y resultados reales.

## Configuraciones propuestas por dispositivo

Los comandos básicos fijan hostname, secreto de enable, cifrado de contraseñas y banner personal. `no shutdown` habilita interfaces. Los pools definen parámetros DHCP; las rutas y OSPF dan alcance remoto; las listas AAA eligen servidor y después respaldo local. Estas configuraciones de entrada no son salidas de `show running-config`.

### R-AREQ

```cisco
enable
configure terminal
hostname R-AREQ
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
interface GigabitEthernet0/0
 ip address 10.20.20.1 255.255.255.0
 no shutdown
exit
interface Serial0/0/0
 ip address 172.30.0.2 255.255.255.252
 no shutdown
exit
router ospf 1
 network 10.20.20.0 0.0.0.255 area 0
 network 172.30.0.0 0.0.0.3 area 0
exit
ip domain-name urp.lab
crypto key generate rsa
1024
ip ssh version 2
username localadmin secret Local2026
aaa new-model
tacacs-server host 10.10.10.100 key TacacsURP2026
aaa authentication login CONSOLA group tacacs+ local
aaa authentication login REMOTO group tacacs+ local
line console 0
 login authentication CONSOLA
exit
line vty 0 4
 login authentication REMOTO
 transport input ssh
exit
end
copy running-config startup-config
```

### R-LIMA

```cisco
enable
configure terminal
hostname R-LIMA
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
interface GigabitEthernet0/0
 ip address 10.10.10.1 255.255.255.0
 no shutdown
exit
interface Serial0/0/0
 ip address 172.30.0.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
router ospf 1
 network 10.10.10.0 0.0.0.255 area 0
 network 172.30.0.0 0.0.0.3 area 0
exit
ip domain-name urp.lab
crypto key generate rsa
1024
ip ssh version 2
username localadmin secret Local2026
aaa new-model
tacacs-server host 10.10.10.100 key TacacsURP2026
aaa authentication login CONSOLA group tacacs+ local
aaa authentication login REMOTO group tacacs+ local
line console 0
 login authentication CONSOLA
exit
line vty 0 4
 login authentication REMOTO
 transport input ssh
exit
end
copy running-config startup-config
```

### SW-AREQ

```cisco
enable
configure terminal
hostname SW-AREQ
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
interface FastEthernet0/2
 switchport mode access
 no shutdown
exit
interface FastEthernet0/24
 switchport mode access
 no shutdown
exit
interface Vlan1
 ip address 10.20.20.2 255.255.255.0
 no shutdown
exit
ip default-gateway 10.20.20.1
username localadmin secret Local2026
aaa new-model
tacacs-server host 10.10.10.100 key TacacsURP2026
aaa authentication login CONSOLA group tacacs+ local
aaa authentication login REMOTO group tacacs+ local
line console 0
 login authentication CONSOLA
exit
line vty 0 15
 login authentication REMOTO
 transport input telnet
exit
end
copy running-config startup-config
```

### SW-LIMA

```cisco
enable
configure terminal
hostname SW-LIMA
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
line console 0
 password cisco
 login
exit
interface FastEthernet0/1
 switchport mode access
 no shutdown
exit
interface FastEthernet0/2
 switchport mode access
 no shutdown
exit
interface FastEthernet0/24
 switchport mode access
 no shutdown
exit
end
copy running-config startup-config
```

Los hosts y servicios se configuran desde GUI conforme a `servicios_y_pruebas.md`; index.html de E08 contiene nombre y código. En configuraciones con RSA y copia de startup-config se deben atender los prompts como explica `montaje.md`.

## Registro de pruebas

| Prueba | Resultado observado | Evidencia | Estado |
|---|---|---|---|
| Abrir .pkt real y comprobar modelos, HWIC-2T y cableado | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| DCE en R-LIMA y clock 64000 | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| OSPF FULL y conectividad entre sedes | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Origen y registro de tres clientes TACACS+ | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Accesos netadmin/auditor por SSH y Telnet indicados | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Fallback por consola con WAN caída | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Restaurar WAN, OSPF y AAA; guardar y reabrir .pkt | Sin ejecución en simulador | Pendiente | NO EJECUTADA |

Seguir `servicios_y_pruebas.md`, adjuntar salidas completas/capturas auténticas en evidencias/ y actualizar esta tabla con el resultado observado. Anotar errores de sintaxis y alternativas exactas aplicadas. No cambiar estados a APROBADA sin evidencia.

## Análisis

1. **Comparación.**

| Aspecto | RADIUS tradicional | TACACS+ |
|---|---|---|
| Transporte/puertos | UDP 1812 autenticación y 1813 accounting; 1645/1646 heredados | TCP 49 |
| Confidencialidad | Oculta User-Password; el paquete completo no se cifra | Protege el cuerpo del paquete; cabecera visible, protección clásica basada en secreto compartido |
| Separación AAA | Autenticación y autorización habitualmente combinadas; accounting separado | Intercambios diferenciados para autenticación, autorización y accounting |
| Uso habitual | Acceso a red, VPN, 802.1X | Administración de dispositivos |

No confundir la protección tradicional de TACACS+ con TLS ni asumir que toda versión ofrece seguridad moderna de transporte.

2. **Separación.** Permite comprobar identidad, decidir permisos y registrar acciones de forma independiente; por ejemplo, autorizar comandos distintos por rol y auditar su uso. Este laboratorio configura listas de autenticación, no implementa automáticamente autorización de comandos ni accounting.
3. **Consola.** Cortar la WAN elimina el camino hacia el servidor y puede impedir SSH desde otra sede. La consola funciona fuera de banda, sin depender de rutas ni OSPF, y permite demostrar el timeout de TACACS+ seguido por la base local, además de restaurar la interfaz. La existencia de una sesión anterior no prueba el fallback.

Conclusión de diseño: OSPF une las sedes y TACACS+ centraliza login con respaldo por consola; la vecindad, autenticación y restauración aún necesitan validación real.
