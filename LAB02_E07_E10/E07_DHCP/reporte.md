# Laboratorio 02 — Ejercicio 07

Alumno: **Andre Torres** · Código: **202210073**
Packet Tracer objetivo: **9.0.1.0858**. Sección/grupo y fecha de entrega: completar por el alumno.

## Estado y alcance

Se generó un `.pkt` offline con pkt-core 0.2.0 y se verificó su recarga con el codec. No se ha abierto en Cisco Packet Tracer: no está instalado aquí. No hay resultados de ping, DHCP, SSH, OSPF o AAA ejecutados. Ver LEEME_PRIMERO.md para ajustes manuales pendientes. La sintaxis IOS incrustada requiere validación en los equipos simulados.

## Topología y direccionamiento

Ver `montaje.md` para equipos, cableado y disposición de la figura original. `figura_fuente.png` es una reproducción de la fuente, no una captura del montaje. Insertar aquí una captura propia después de construirlo.

| Equipo | Interfaz | Dirección/prefijo objetivo | Gateway |
|---|---|---|---|
| R1 | G0/0 | 172.16.10.1/24 | — |
| R1 | G0/1 | 172.16.20.1/24 | — |
| PC-A1 | NIC | DHCP: ADMIN | DHCP |
| PC-A2 | NIC | DHCP: ADMIN | DHCP |
| PC-B1 | NIC | DHCP: ACADEMICO | DHCP |
| IMP-B | NIC | 172.16.20.5/24 | 172.16.20.1 |

/24 = 255.255.255.0; /30 = 255.255.255.252. Tabla extraída de la fuente, pendiente de contraste con configuración y resultados reales.

## Configuraciones propuestas por dispositivo

Los comandos básicos fijan hostname, secreto de enable, cifrado de contraseñas y banner personal. `no shutdown` habilita interfaces. Los pools definen parámetros DHCP; las rutas y OSPF dan alcance remoto; las listas AAA eligen servidor y después respaldo local. Estas configuraciones de entrada no son salidas de `show running-config`.

### R1

```cisco
enable
configure terminal
hostname R1
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
line console 0
 password cisco
 login
exit
interface GigabitEthernet0/0
 ip address 172.16.10.1 255.255.255.0
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 172.16.20.1 255.255.255.0
 no shutdown
exit
ip dhcp excluded-address 172.16.10.1 172.16.10.10
ip dhcp excluded-address 172.16.20.1 172.16.20.50
ip dhcp excluded-address 172.16.20.200 172.16.20.254
ip dhcp pool ADMIN
 network 172.16.10.0 255.255.255.0
 default-router 172.16.10.1
 dns-server 8.8.8.8
 domain-name urp.lab
exit
ip dhcp pool ACADEMICO
 network 172.16.20.0 255.255.255.0
 default-router 172.16.20.1
 dns-server 8.8.8.8
 domain-name urp.lab
exit
end
copy running-config startup-config
```

### SW-ACA

```cisco
enable
configure terminal
hostname SW-ACA
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
interface FastEthernet0/3
 switchport mode access
 no shutdown
exit
end
copy running-config startup-config
```

### SW-ADM

```cisco
enable
configure terminal
hostname SW-ADM
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
interface FastEthernet0/3
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
| Abrir .pkt real y comprobar nombres/modelos/cableado | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Tres PC reciben DHCP con rangos, gateway y DNS correctos | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Renovación DHCP PC-B1 con comparación de bindings | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Ping inter-LAN y a IMP-B | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Configuraciones finales, persistencia tras reabrir y nota del alumno | Sin ejecución en simulador | Pendiente | NO EJECUTADA |

Seguir `servicios_y_pruebas.md`, adjuntar salidas completas/capturas auténticas en evidencias/ y actualizar esta tabla con el resultado observado. Anotar errores de sintaxis y alternativas exactas aplicadas. No cambiar estados a APROBADA sin evidencia.

## Análisis

1. **DORA.** DHCPDISCOVER normalmente usa broadcast de cliente 0.0.0.0:68 a 255.255.255.255:67. DHCPOFFER puede ser broadcast o unicast según el bit broadcast, estado y capacidad del cliente. DHCPREQUEST inicial suele ser broadcast para indicar el servidor seleccionado; durante renovación T1 suele ser unicast al servidor, y en rebinding T2 broadcast. DHCPACK puede ser broadcast o unicast según el estado/flags; con relay, servidor y relay intercambian normalmente por unicast. No todos los mensajes DORA son siempre broadcast.
2. **Capacidad.** /24 tiene 254 hosts utilizables. ADMIN excluye 10: 254 − 10 = **244**, .11–.254. ACADEMICO excluye 50 y 55: 254 − 50 − 55 = **149**, .51–.199. La impresora .5 está excluida. Red .0 y broadcast .255 no son hosts.
3. **Sin DHCP.** El cliente reintenta y puede autoasignarse una dirección link-local de 169.254.0.0/16 (APIPA), normalmente con máscara /16 y sin gateway útil. No proporciona comunicación enrutada con las LAN indicadas. La conducta concreta depende del cliente de Packet Tracer y debe observarse.

Conclusión de diseño: los dos pools separan las LAN y reservan direcciones fijas; la operación y renovación todavía deben comprobarse en el simulador.
