# Laboratorio 02 — Ejercicio 09

Alumno: **Andre Torres** · Código: **202210073**
Packet Tracer objetivo: **9.0.1.0858**. Sección/grupo y fecha de entrega: completar por el alumno.

## Estado y alcance

Material de preparación, no implementación verificada. No se ha creado ni abierto un `.pkt`: este entorno Linux no dispone de Packet Tracer, puente MCP ni paquete instalado para generarlo. No hay resultados de ping, DHCP, SSH, OSPF o AAA ejecutados. La sintaxis IOS propuesta requiere validación en los equipos simulados.

## Topología y direccionamiento

Ver `montaje.md` para equipos, cableado y disposición de la figura original. `figura_fuente.png` es una reproducción de la fuente, no una captura del montaje. Insertar aquí una captura propia después de construirlo.

| Equipo | Interfaz | Dirección/prefijo objetivo | Gateway |
|---|---|---|---|
| R1 | G0/0 | 192.168.50.1/24 | — |
| R1 | G0/1 | 10.0.12.1/30 | — |
| R2 | G0/1 | 10.0.12.2/30 | — |
| R2 | G0/0 | 192.168.60.1/24 | — |
| SW1 | VLAN 1 | 192.168.50.2/24 | 192.168.50.1 |
| SRV-RADIUS | NIC | 192.168.50.100/24 | 192.168.50.1 |
| PC-ADMIN | NIC | 192.168.50.10/24 | 192.168.50.1 |
| PC-REMOTO | NIC | 192.168.60.10/24 | 192.168.60.1 |

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
interface GigabitEthernet0/0
 ip address 192.168.50.1 255.255.255.0
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 10.0.12.1 255.255.255.252
 no shutdown
exit
ip route 192.168.60.0 255.255.255.0 10.0.12.2
ip domain-name urp.lab
crypto key generate rsa
1024
ip ssh version 2
username localadmin secret Local2026
aaa new-model
radius-server host 192.168.50.100 key RadiusURP2026
aaa authentication login default group radius local
line console 0
 login authentication default
exit
line vty 0 4
 login authentication default
 transport input ssh
exit
end
copy running-config startup-config
```

### R2

```cisco
enable
configure terminal
hostname R2
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
interface GigabitEthernet0/0
 ip address 192.168.60.1 255.255.255.0
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 10.0.12.2 255.255.255.252
 no shutdown
exit
ip route 192.168.50.0 255.255.255.0 10.0.12.1
ip domain-name urp.lab
crypto key generate rsa
1024
ip ssh version 2
username localadmin secret Local2026
aaa new-model
radius-server host 192.168.50.100 key RadiusURP2026
aaa authentication login default group radius local
line console 0
 login authentication default
exit
line vty 0 4
 login authentication default
 transport input ssh
exit
end
copy running-config startup-config
```

### SW1

```cisco
enable
configure terminal
hostname SW1
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - Andre Torres - 202210073#
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
interface Vlan1
 ip address 192.168.50.2 255.255.255.0
 no shutdown
exit
ip default-gateway 192.168.50.1
username localadmin secret Local2026
aaa new-model
radius-server host 192.168.50.100 key RadiusURP2026
aaa authentication login default group radius local
line console 0
 login authentication default
exit
line vty 0 15
 login authentication default
 transport input telnet
exit
end
copy running-config startup-config
```

Los hosts y servicios se configuran desde GUI conforme a `servicios_y_pruebas.md`; index.html de E08 contiene nombre y código. En configuraciones con RSA y copia de startup-config se deben atender los prompts como explica `montaje.md`.

## Registro de pruebas

| Prueba | Resultado observado | Evidencia | Estado |
|---|---|---|---|
| Abrir .pkt real y comprobar nombres/modelos/cableado | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Conectividad completa y origen real de tres clientes AAA | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| SSH v2 válido admin/soporte y rechazo de inexistente | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Consola y VTY con AAA en los tres equipos | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Fallback local con servicio AAA sin respuesta | Sin ejecución en simulador | Pendiente | NO EJECUTADA |
| Reactivar AAA y reabrir .pkt; guardar evidencias | Sin ejecución en simulador | Pendiente | NO EJECUTADA |

Seguir `servicios_y_pruebas.md`, adjuntar salidas completas/capturas auténticas en evidencias/ y actualizar esta tabla con el resultado observado. Anotar errores de sintaxis y alternativas exactas aplicadas. No cambiar estados a APROBADA sin evidencia.

## Análisis

1. **Transporte y puertos.** RADIUS tradicional usa UDP 1812 para autenticación/autorización y UDP 1813 para accounting; existen puertos heredados 1645/1646. Packet Tracer/IOS puede mostrar variantes heredadas: registrar los puertos observados y compatibilidad real sin asumir que se ejecuta accounting por haber configurado login.
2. **Protección.** RADIUS tradicional oculta el atributo User-Password mediante el secreto compartido y mecanismos basados en MD5; no cifra todo el paquete. Muchos atributos permanecen visibles. No proporciona confidencialidad general del transporte y debe protegerse la red de gestión; RADIUS sobre TLS es otra modalidad y no se ha configurado aquí.
3. **Respaldo.** `group radius local` mantiene acceso cuando el servidor no responde o devuelve error de disponibilidad, utilizando la base local. Un rechazo explícito por usuario/contraseña inválidos normalmente finaliza el intento y no activa fallback. La cuenta local permite recuperación sin convertir un rechazo del servidor en un acceso alternativo.

Conclusión de diseño: la autenticación se centraliza conservando recuperación local; aceptación, rechazo y caída del servidor deben demostrarse en sesiones nuevas.
