# Laboratorio 02 — Ejercicio 08

Alumno: **Andre Torres** · Código: **202210073**
Packet Tracer objetivo: **9.0.1.0858**. Sección/grupo y fecha de entrega: completar por el alumno.

## Estado y alcance

Se generó un `.pkt` offline con pkt-core 0.2.0 y se verificó su recarga con el codec. No se ha abierto en Cisco Packet Tracer: no está instalado aquí. No hay resultados de ping, DHCP, SSH, OSPF o AAA ejecutados. Ver LEEME_PRIMERO.md para ajustes manuales pendientes. La sintaxis IOS incrustada requiere validación en los equipos simulados.

## Topología y direccionamiento

Ver `montaje.md` para equipos, cableado y disposición de la figura original. `figura_fuente.png` es una reproducción de la fuente, no una captura del montaje. Insertar aquí una captura propia después de construirlo.

| Equipo | Interfaz | Dirección/prefijo objetivo | Gateway |
|---|---|---|---|
| R-DHCP | G0/0 | 10.0.0.1/24 | — |
| R-DHCP | G0/1 | 10.1.1.1/30 | — |
| R-SEDE | G0/1 | 10.1.1.2/30 | — |
| R-SEDE | G0/0.10 | 192.168.10.1/24 | — |
| R-SEDE | G0/0.20 | 192.168.20.1/24 | — |
| R-SEDE | G0/0.30 | 192.168.30.1/24 | — |
| SRV-DNS | NIC | 10.0.0.10/24 | 10.0.0.1 |
| PC-V10 | NIC | DHCP: VLAN10 | DHCP |
| PC-V20 | NIC | DHCP: VLAN20 | DHCP |
| PC-V30 | NIC | DHCP: VLAN30 | DHCP |

/24 = 255.255.255.0; /30 = 255.255.255.252. Tabla extraída de la fuente, pendiente de contraste con configuración y resultados reales.

## Configuraciones propuestas por dispositivo

Los comandos básicos fijan hostname, secreto de enable, cifrado de contraseñas y banner personal. `no shutdown` habilita interfaces. Los pools definen parámetros DHCP; las rutas y OSPF dan alcance remoto; las listas AAA eligen servidor y después respaldo local. Estas configuraciones de entrada no son salidas de `show running-config`.

### R-DHCP

```cisco
enable
configure terminal
hostname R-DHCP
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
line console 0
 password cisco
 login
exit
interface GigabitEthernet0/0
 ip address 10.0.0.1 255.255.255.0
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 10.1.1.1 255.255.255.252
 no shutdown
exit
ip route 192.168.10.0 255.255.255.0 10.1.1.2
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 10.0.0.10
 domain-name urp.lab
exit
ip route 192.168.20.0 255.255.255.0 10.1.1.2
ip dhcp excluded-address 192.168.20.1 192.168.20.20
ip dhcp pool VLAN20
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 10.0.0.10
 domain-name urp.lab
exit
ip route 192.168.30.0 255.255.255.0 10.1.1.2
ip dhcp excluded-address 192.168.30.1 192.168.30.20
ip dhcp pool VLAN30
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1
 dns-server 10.0.0.10
 domain-name urp.lab
exit
end
copy running-config startup-config
```

### R-SEDE

```cisco
enable
configure terminal
hostname R-SEDE
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
line console 0
 password cisco
 login
exit
interface GigabitEthernet0/1
 ip address 10.1.1.2 255.255.255.252
 no shutdown
exit
interface GigabitEthernet0/0
 no shutdown
exit
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ip helper-address 10.1.1.1
exit
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ip helper-address 10.1.1.1
exit
interface GigabitEthernet0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ip helper-address 10.1.1.1
exit
ip route 0.0.0.0 0.0.0.0 10.1.1.1
end
copy running-config startup-config
```

### SW-CEN

```cisco
enable
configure terminal
hostname SW-CEN
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
end
copy running-config startup-config
```

### SW-SEDE

```cisco
enable
configure terminal
hostname SW-SEDE
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
line console 0
 password cisco
 login
exit
vlan 10
 name ALUMNOS
exit
interface FastEthernet0/5
 switchport mode access
 switchport access vlan 10
 no shutdown
exit
vlan 20
 name DOCENTES
exit
interface FastEthernet0/10
 switchport mode access
 switchport access vlan 20
 no shutdown
exit
vlan 30
 name ADMINISTRATIVOS
exit
interface FastEthernet0/15
 switchport mode access
 switchport access vlan 30
 no shutdown
exit
interface GigabitEthernet0/1
 switchport mode trunk
 no shutdown
exit
end
copy running-config startup-config
```

Los hosts y servicios se configuran desde GUI conforme a `servicios_y_pruebas.md`; index.html de E08 contiene nombre y código. En configuraciones con RSA y copia de startup-config se deben atender los prompts como explica `montaje.md`.

## Registro de pruebas

| Prueba | Resultado observado | Evidencia | Estado |
|---|---|---|---|
| Abrir .pkt real y comprobar nombres/modelos/cableado | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| VLAN, trunk, subinterfaces, helper y rutas | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| DHCP desde servidor remoto en las tres VLAN | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Resolución www.urp.lab y HTTP con nombre/código en cada PC | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Retirada de rutas y restauración verificadas | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Persistencia tras reabrir y nota del alumno | Sin ejecución en simulador | Pendiente | NO EJECUTADA |

Seguir `servicios_y_pruebas.md`, adjuntar salidas completas/capturas auténticas en evidencias/ y actualizar esta tabla con el resultado observado. Anotar errores de sintaxis y alternativas exactas aplicadas. No cambiar estados a APROBADA sin evidencia.

## Análisis

1. **giaddr.** Al retransmitir un broadcast DHCP, el relay coloca la IP de la interfaz de la red del cliente en giaddr. El servidor la utiliza para escoger la subred/pool y devolver la respuesta al agente. Para VLAN10 debe corresponder a 192.168.10.1, aunque el destino configurado por helper sea 10.1.1.1.
2. **Retorno.** R-DHCP conoce directamente 10.0.0.0/24 y 10.1.1.0/30, pero no las tres LAN remotas. Necesita rutas vía 10.1.1.2 tanto para responder al relay por giaddr como para el resto del tráfico de retorno. Sin ellas fallan nuevos intercambios y respuestas a las VLAN; una concesión ya existente puede permanecer almacenada sin demostrar conectividad.
3. **Otros UDP.** En Cisco IOS clásico, helper reenvía por defecto UDP 37 (Time), 49 (TACACS histórico), 53 (DNS), 67/68 (BOOTP/DHCP), 69 (TFTP), 137 (NetBIOS name) y 138 (NetBIOS datagram). El UDP 49 histórico no es TACACS+ TCP 49. No implica que todos estén simulados en Packet Tracer; verificar `show ip forward-protocol` si está soportado o documentar la limitación.

Conclusión de diseño: router-on-a-stick, relay y rutas de retorno permiten centralizar DHCP; DNS y HTTP requieren pruebas desde cada VLAN y siguen pendientes.
