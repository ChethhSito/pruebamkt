# Instrucciones para Codex — Laboratorio 02, Redes 2 (URP)

> **Propósito:** implementar y comprobar **exclusivamente los ejercicios 07, 08, 09 y 10** del documento `Laboratorio 02 - Redes 2 - URP - 2026-II.pdf`, y entregar **cuatro archivos independientes de Cisco Packet Tracer (`.pkt`)** más el material necesario para el informe.
>
> Este archivo es una **especificación de trabajo para Codex o un agente asistido por MCP**. No constituye evidencia de que las redes ya hayan sido creadas o verificadas.

## 0. Principios obligatorios de ejecución

1. Leer y utilizar el PDF original, especialmente las **figuras 7–10 y sus tablas de direccionamiento** (páginas 15–22 del PDF). Las figuras prevalecen para ubicar y conectar físicamente los dispositivos; las tablas prevalecen para las direcciones.
2. Usar **Cisco Packet Tracer 8.2 o superior** y los modelos del documento. **No cambiar** nombres, IP, máscaras, gateways, VLAN, puertos, contraseñas ni parámetros exigidos.
3. Crear **un proyecto `.pkt` independiente por ejercicio**, no una sola topología con las cuatro prácticas juntas.
4. Emplear, según disponibilidad y compatibilidad, una librería de generación `.pkt`, un puente MCP hacia Packet Tracer o el propio entorno de Packet Tracer. **Investigar/documentar la API exacta instalada antes de escribir scripts**; no inventar métodos de librerías ni afirmar compatibilidad sin probarla.
5. Si la generación directa del `.pkt` no es posible, producir archivos de configuración IOS por equipo, manifiestos de topología/cableado y procedimientos de importación/manuales, **identificando la limitación**. Nunca renombrar un JSON o un archivo de texto como `.pkt` ni declarar terminada una simulación que no pudo abrirse.
6. Probar **cada `.pkt` abriéndolo en Packet Tracer**, revisando puertos, interfaces, configuraciones, servicios y conectividad. Registrar resultados reales, no supuestos. Si no se dispone de Packet Tracer o de herramientas de interacción, marcar la verificación como pendiente.
7. Aplicar a routers y switches, salvo las excepciones de AAA en ejercicios 09 y 10: `hostname` acorde al diagrama, `no ip domain-lookup`, `enable secret class`, contraseña de consola `cisco` con `login`, `service password-encryption` y banner MOTD con **[NOMBRE_COMPLETO]** y **[CODIGO_ALUMNO]**. No inventar los datos del estudiante.
8. Etiquetar dispositivos y enlaces igual que en el diagrama original. Agregar una nota **Place Note** con nombre y código del alumno en cada `.pkt`.
9. Priorizar que las redes sean operativas; si un comando IOS es incompatible con el modelo/versión, documentar el error y la alternativa exacta aplicada. No reemplazar protocolos solicitados por otros.
10. Guardar evidencias de los comandos y pruebas señalados por el docente, junto con las configuraciones finales. Evitar capturas simuladas.

## 1. Estructura de carpetas y entregables

```text
LAB02_E07_E10/
├── INSTRUCCIONES_CODEX_LAB02.md
├── fuente/
│   └── Laboratorio 02 - Redes 2 - URP - 2026-II.pdf
├── E07_DHCP/
│   ├── LAB02_E07_ApellidoNombre.pkt
│   ├── configs/
│   ├── evidencias/
│   └── reporte.md
├── E08_DHCP_RELAY/
│   ├── LAB02_E08_ApellidoNombre.pkt
│   ├── configs/
│   ├── evidencias/
│   └── reporte.md
├── E09_RADIUS/
│   ├── LAB02_E09_ApellidoNombre.pkt
│   ├── configs/
│   ├── evidencias/
│   └── reporte.md
└── E10_TACACS/
    ├── LAB02_E10_ApellidoNombre.pkt
    ├── configs/
    ├── evidencias/
    └── reporte.md
```

Los nombres de los `.pkt` son los indicados por el laboratorio; sustituir `ApellidoNombre` al conocer los datos. No generar resultados falsos de ping, SSH, DHCP, OSPF o AAA.

## 2. Ejercicio 07 — Servidor DHCP en un router Cisco para dos LAN

**Fuente:** PDF, páginas 15–16, figura 7.

### Topología

- **R1**: router **1941**; servidor DHCP para las dos LAN.
- **SW-ADM** y **SW-ACA**: switches **2960**.
- **PC-A1**, **PC-A2**: clientes en Administración, conectados a SW-ADM.
- **PC-B1**: cliente en Académico, conectado a SW-ACA.
- **IMP-B**: impresora con dirección estática en Académico, conectada a SW-ACA.
- Usar los puertos y conexiones dibujados en la figura 7; no agregar VLAN o servidores innecesarios.

### Direccionamiento requerido

| Equipo | Interfaz | IP/máscara | Gateway |
|---|---|---|---|
| R1 | G0/0 | `172.16.10.1/24` | — |
| R1 | G0/1 | `172.16.20.1/24` | — |
| PC-A1, PC-A2 | NIC | DHCP | DHCP |
| PC-B1 | NIC | DHCP | DHCP |
| IMP-B | NIC | `172.16.20.5/24` | `172.16.20.1` |

### Pasos de implementación

1. Construir la figura 7 y activar las interfaces G0/0 y G0/1 de R1.
2. Excluir del DHCP de Administración: **`172.16.10.1`–`172.16.10.10`**.
3. Excluir del DHCP de Académico: **`172.16.20.1`–`172.16.20.50`** y **`172.16.20.200`–`172.16.20.254`**.
4. Crear `ip dhcp pool ADMIN`, red `172.16.10.0/24`, gateway `172.16.10.1`, DNS `8.8.8.8`, dominio `urp.lab`.
5. Crear `ip dhcp pool ACADEMICO`, red `172.16.20.0/24`, gateway `172.16.20.1`, DNS `8.8.8.8`, dominio `urp.lab`.
6. Configurar en DHCP las tres PC y dejar la impresora con su IP fija.
7. Registrar `ipconfig /all` de cada PC (IP, máscara, gateway, DNS).
8. En PC-B1 ejecutar `ipconfig /release` y `ipconfig /renew`. Revisar las asignaciones del router antes y después; **no asumir que cambiará la dirección IP**: lo importante es confirmar la renovación/concesión.
9. Comprobar conectividad entre las LAN y con IMP-B.

### Configuración IOS de referencia para R1

```cisco
hostname R1
no ip domain-lookup
enable secret class
service password-encryption
banner motd #Laboratorio URP - [NOMBRE_COMPLETO] - [CODIGO_ALUMNO]#
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
```

### Verificaciones obligatorias

`show ip dhcp binding`, `show ip dhcp pool`, `show ip dhcp server statistics`, `show running-config | section dhcp`, `ipconfig /all` en las PC, ping inter-LAN y ping a la impresora.

### Preguntas de análisis del PDF

1. Explicar DORA e indicar cuáles mensajes son broadcast y cuáles pueden ser unicast, según contexto.
2. Calcular capacidad: **ADMIN = 244 direcciones** (`.11`–`.254`); **ACADEMICO = 149 direcciones** (`.51`–`.199`).
3. Explicar qué ocurre sin respuesta DHCP y el posible autoasignado **APIPA 169.254.0.0/16**, dependiendo del cliente/implementación de Packet Tracer.

**Archivo final:** `LAB02_E07_ApellidoNombre.pkt`.

## 3. Ejercicio 08 — DHCP centralizado, relay y router-on-a-stick

**Fuente:** PDF, páginas 17–18, figura 8.

### Topología

- Dos routers **1941**: **R-DHCP** (data center, servidor DHCP) y **R-SEDE** (router-on-a-stick y relay).
- Switches **SW-CEN** y **SW-SEDE** (2960).
- Servidor **SRV-DNS** en la LAN `10.0.0.0/24`.
- Tres PC: **PC-V10**, **PC-V20** y **PC-V30**, cada una en su VLAN.
- R-DHCP G0/1 ↔ R-SEDE G0/1 en red `10.1.1.0/30`.
- R-SEDE G0/0 ↔ SW-SEDE G0/1 por troncal 802.1Q.
- En SW-SEDE: F0/5 = VLAN 10, F0/10 = VLAN 20, F0/15 = VLAN 30, según la figura 8.

### Direccionamiento requerido

| Equipo | Interfaz | IP/máscara | Gateway |
|---|---|---|---|
| R-DHCP | G0/0 | `10.0.0.1/24` | — |
| R-DHCP | G0/1 | `10.1.1.1/30` | — |
| R-SEDE | G0/1 | `10.1.1.2/30` | — |
| R-SEDE | G0/0.10 | `192.168.10.1/24` | — |
| R-SEDE | G0/0.20 | `192.168.20.1/24` | — |
| R-SEDE | G0/0.30 | `192.168.30.1/24` | — |
| SRV-DNS | NIC | `10.0.0.10/24` | `10.0.0.1` |
| PC-V10/V20/V30 | NIC | DHCP | DHCP |

### Pasos de implementación

1. Crear en SW-SEDE las VLAN **10 ALUMNOS**, **20 DOCENTES**, **30 ADMINISTRATIVOS** y asignar los puertos indicados.
2. Configurar el troncal de SW-SEDE hacia R-SEDE. Usar subinterfaces G0/0.10, G0/0.20, G0/0.30 con `encapsulation dot1Q` y direcciones de la tabla. Mantener encendida la interfaz física G0/0.
3. En R-SEDE configurar una ruta por defecto hacia `10.1.1.1`.
4. En R-DHCP configurar rutas estáticas hacia las tres VLAN de la sede usando `10.1.1.2` como siguiente salto.
5. En R-DHCP excluir `.1`–`.20` de **cada** red `192.168.10.0/24`, `192.168.20.0/24`, `192.168.30.0/24`.
6. En R-DHCP crear pools **VLAN10**, **VLAN20**, **VLAN30**, con gateways `.1`, DNS `10.0.0.10`, dominio `urp.lab`.
7. En **cada** subinterfaz de R-SEDE agregar `ip helper-address 10.1.1.1`.
8. En SRV-DNS habilitar servicio DNS con registro A **`www.urp.lab` → `10.0.0.10`** y servicio HTTP con página donde figuren nombre y código del alumno.
9. Poner las tres PC en DHCP; registrar `ipconfig /all` y abrir `http://www.urp.lab` desde cada PC.
10. Efectuar prueba controlada eliminando temporalmente las rutas estáticas de R-DHCP; registrar resultado y **restaurar** las rutas para el `.pkt` final.

### Configuración IOS de referencia

**R-SEDE:**

```cisco
hostname R-SEDE
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
```

**R-DHCP:**

```cisco
hostname R-DHCP
interface GigabitEthernet0/0
 ip address 10.0.0.1 255.255.255.0
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 10.1.1.1 255.255.255.252
 no shutdown
exit
ip route 192.168.10.0 255.255.255.0 10.1.1.2
ip route 192.168.20.0 255.255.255.0 10.1.1.2
ip route 192.168.30.0 255.255.255.0 10.1.1.2
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp excluded-address 192.168.20.1 192.168.20.20
ip dhcp excluded-address 192.168.30.1 192.168.30.20
ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 10.0.0.10
 domain-name urp.lab
exit
ip dhcp pool VLAN20
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 10.0.0.10
 domain-name urp.lab
exit
ip dhcp pool VLAN30
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1
 dns-server 10.0.0.10
 domain-name urp.lab
exit
```

**SW-SEDE (fragmento):**

```cisco
vlan 10
 name ALUMNOS
vlan 20
 name DOCENTES
vlan 30
 name ADMINISTRATIVOS
interface FastEthernet0/5
 switchport mode access
 switchport access vlan 10
exit
interface FastEthernet0/10
 switchport mode access
 switchport access vlan 20
exit
interface FastEthernet0/15
 switchport mode access
 switchport access vlan 30
exit
interface GigabitEthernet0/1
 switchport mode trunk
 no shutdown
exit
```

### Verificaciones obligatorias

`show ip dhcp binding`, `show ip dhcp pool`, `show ip interface g0/0.10`, `show interfaces trunk`, `show ip route`, `ipconfig /all`, resolución DNS y carga de la web en las tres PC.

### Preguntas de análisis

1. Explicar `giaddr` (dirección del agente de retransmisión) como selector de red/pool en el servidor DHCP.
2. Explicar por qué el servidor central debe conocer rutas de retorno hacia las redes remotas.
3. Enumerar otros servicios UDP que retransmite `ip helper-address` por defecto en Cisco IOS y comprobar soporte de simulación cuando sea necesario.

**Archivo final:** `LAB02_E08_ApellidoNombre.pkt`.

## 4. Ejercicio 09 — AAA centralizado con RADIUS

**Fuente:** PDF, páginas 19–20, figura 9.

### Topología

- Routers **R1** y **R2** (1941); switch **SW1** (2960).
- Servidor **SRV-RADIUS** conectado a SW1 en la LAN de gestión `192.168.50.0/24`.
- **PC-ADMIN** conectada a SW1; **PC-REMOTO** conectada a R2.
- Enlace entre R1 G0/1 y R2 G0/1 en `10.0.12.0/30`.
- Seguir el cableado y puertos que muestra la figura 9.

### Direccionamiento requerido

| Equipo | Interfaz | IP/máscara | Gateway |
|---|---|---|---|
| R1 | G0/0 | `192.168.50.1/24` | — |
| R1 | G0/1 | `10.0.12.1/30` | — |
| R2 | G0/1 | `10.0.12.2/30` | — |
| R2 | G0/0 | `192.168.60.1/24` | — |
| SW1 | VLAN 1 | `192.168.50.2/24` | `192.168.50.1` |
| SRV-RADIUS | NIC | `192.168.50.100/24` | `192.168.50.1` |
| PC-ADMIN | NIC | `192.168.50.10/24` | `192.168.50.1` |
| PC-REMOTO | NIC | `192.168.60.10/24` | `192.168.60.1` |

### Parámetros AAA requeridos

| Elemento | Valor |
|---|---|
| Servicio | RADIUS (Services > AAA en servidor) |
| Clientes registrados | R1, R2 y SW1 |
| Clave compartida | `RadiusURP2026` |
| Usuario RADIUS 1 | `admin` / `Admin2026` |
| Usuario RADIUS 2 | `soporte` / `Soporte2026` |
| Respaldo local en los tres equipos | `localadmin` / `Local2026` |
| Orden de autenticación | RADIUS y luego local |
| Acceso remoto a routers | SSH versión 2 |
| Dominio SSH | `urp.lab` |
| RSA | 1024 bits (según PDF) |

### Pasos de implementación

1. Construir la topología e introducir las IP estáticas de la tabla.
2. Configurar rutas estáticas en R1 y R2 para alcanzar ambas LAN. Comprobar ping entre las redes y desde cada dispositivo hasta SRV-RADIUS.
3. En `SRV-RADIUS > Services > AAA`, habilitar RADIUS, registrar los tres clientes con la clave exacta, y crear los dos usuarios.
4. **Revisar la dirección IP de origen real** que utiliza cada cliente al enviar solicitudes RADIUS. R2 puede usar la interfaz de tránsito `10.0.12.2`, y el switch su SVI `192.168.50.2`; registrar exactamente esas direcciones en el servidor o configurar la interfaz de origen si IOS lo soporta.
5. En R1, R2 y SW1 configurar usuario de respaldo local, `aaa new-model`, servidor RADIUS y lista de autenticación con método RADIUS primero y local después.
6. Aplicar la lista a consola (`line con 0`) y VTY (`line vty ...`). Tener cuidado de conservar una sesión activa de recuperación durante el cambio de AAA.
7. En R1 y R2 configurar `ip domain-name urp.lab`, generar claves RSA de 1024 bits, `ip ssh version 2` y `transport input ssh` en VTY.
8. Probar desde PC-ADMIN `ssh -l admin 192.168.50.1` y desde PC-REMOTO `ssh -l soporte 192.168.60.1`; probar además un usuario inexistente y registrar rechazo.
9. Desactivar temporalmente AAA en el servidor y comprobar que el acceso local con `localadmin` funciona cuando RADIUS **no responde**. Reactivar AAA. No presentar como evidencia de fallback un rechazo explícito por contraseña errónea: normalmente el método local se intenta al quedar el servidor no disponible, no por `Access-Reject`.

### Ejemplo lógico de configuración IOS (adaptar a sintaxis soportada)

```cisco
username localadmin secret Local2026
aaa new-model
radius-server host 192.168.50.100 key RadiusURP2026
aaa authentication login default group radius local
ip domain-name urp.lab
crypto key generate rsa
! Cuando IOS solicite modulus, introducir 1024.
ip ssh version 2
line console 0
 login authentication default
exit
line vty 0 4
 login authentication default
 transport input ssh
exit
```

**Atención:** este bloque es orientativo y **no reemplaza** configurar interfaces, rutas, dirección de origen y verificar la sintaxis que admita la versión de IOS de Packet Tracer. El switch puede necesitar un tratamiento VTY distinto del router, según el requisito del docente. Registrar correctamente los tres clientes en el servidor.

### Verificaciones obligatorias

`show running-config | include aaa|radius`, `debug aaa authentication`, `show ip ssh`, `show users`, `show ip route`, intentos SSH válidos/inválidos y demostración del respaldo local.

### Preguntas de análisis

1. Describir RADIUS: UDP, puertos de autenticación y accounting (1812/1813 normalmente).
2. Explicar qué porción de la comunicación cifra RADIUS tradicional y su consecuencia para la seguridad.
3. Justificar el uso de autenticación local de respaldo.

**Archivo final:** `LAB02_E09_ApellidoNombre.pkt`.

## 5. Ejercicio 10 — AAA con TACACS+ en red multisede

**Fuente:** PDF, páginas 21–22, figura 10.

### Topología

- **R-LIMA** y **R-AREQ**, routers Cisco **2911**, ambos con módulo **HWIC-2T** y conexión serial `S0/0/0 ↔ S0/0/0`.
- El lado **DCE es R-LIMA**, con `clock rate 64000`.
- **SW-LIMA** y **SW-AREQ**, switches **2960**.
- **SRV-TACACS** y **PC-NOC** en la LAN de Lima.
- **PC-AQP** en la LAN de Arequipa.
- R-LIMA G0/0 ↔ SW-LIMA, R-AREQ G0/0 ↔ SW-AREQ; replicar los puertos de la figura 10.

### Direccionamiento requerido

| Equipo | Interfaz | IP/máscara | Gateway |
|---|---|---|---|
| R-LIMA | G0/0 | `10.10.10.1/24` | — |
| R-LIMA | S0/0/0 (DCE) | `172.30.0.1/30` | — |
| R-AREQ | S0/0/0 | `172.30.0.2/30` | — |
| R-AREQ | G0/0 | `10.20.20.1/24` | — |
| SW-AREQ | VLAN 1 | `10.20.20.2/24` | `10.20.20.1` |
| SRV-TACACS | NIC | `10.10.10.100/24` | `10.10.10.1` |
| PC-NOC | NIC | `10.10.10.20/24` | `10.10.10.1` |
| PC-AQP | NIC | `10.20.20.20/24` | `10.20.20.1` |

**Nota de fuente:** el PDF no asigna una IP de gestión a `SW-LIMA`; no inventar una como si fuera obligatoria. Configurar SW-LIMA como switch de acceso para los hosts de Lima.

### Parámetros AAA requeridos

| Elemento | Valor |
|---|---|
| Servicio | TACACS+ (`Services > AAA`) |
| Clientes | R-LIMA, R-AREQ, SW-AREQ |
| Clave compartida | `TacacsURP2026` |
| Usuario 1 | `netadmin` / `Net2026` |
| Usuario 2 | `auditor` / `Audit2026` |
| Usuario local de respaldo | `localadmin` / `Local2026` |
| Lista AAA de consola | `CONSOLA`: grupo TACACS+ → local |
| Lista AAA remota | `REMOTO`: grupo TACACS+ → local |
| Gestión routers | SSH v2 |
| Gestión SW-AREQ | Telnet (requisito didáctico del PDF; no recomendado en redes reales) |
| Enrutamiento | OSPF proceso elegido por el implementador, área 0 |

### Pasos de implementación

1. Montar `HWIC-2T` en ambos routers **con el dispositivo apagado** si Packet Tracer lo exige. Conectar cable serial con DCE en R-LIMA.
2. Configurar interfaces y activar enlaces; aplicar `clock rate 64000` únicamente en la interfaz DCE. Verificar `show controllers s0/0/0`.
3. Configurar OSPF área 0 en ambos routers anunciando LAN y red serial; comprobar vecino FULL y ping entre Lima y Arequipa.
4. En SRV-TACACS habilitar AAA, registrar **R-LIMA**, **R-AREQ** y **SW-AREQ** con tipo **Tacacs** y clave `TacacsURP2026`. Registrar las IP de origen correctas observadas: pueden variar según interfaz o configuración explícita.
5. Crear usuarios `netadmin` y `auditor` con las credenciales exactas en el servidor.
6. En R-LIMA, R-AREQ y SW-AREQ crear el usuario `localadmin` y activar `aaa new-model`.
7. Configurar el servidor TACACS+ y listas AAA con nombre `CONSOLA` y `REMOTO`; aplicar respectivamente a `line console 0` y `line vty ...`.
8. Configurar SSH v2 en R-LIMA y R-AREQ (dominio y RSA si requieren generación de claves; el documento **no fija** un dominio o longitud RSA para este ejercicio: usar valores compatibles y documentarlos). Configurar Telnet en VTY de SW-AREQ **solo para cumplir la práctica**.
9. Desde PC-AQP: entrar en R-AREQ y SW-AREQ usando `netadmin`. Desde PC-NOC: entrar en R-AREQ como `auditor`.
10. Hacer prueba de respaldo: apagar `S0/0/0` de **R-AREQ**, iniciar sesión **por consola** usando `localadmin` y constatar que el servidor remoto quedó inaccesible. Restaurar `S0/0/0` y comprobar OSPF/AAA.

### Configuración IOS de referencia

**R-LIMA (red y OSPF):**

```cisco
hostname R-LIMA
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
```

**R-AREQ (red y OSPF):**

```cisco
hostname R-AREQ
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
```

**Ejemplo orientativo AAA para cada cliente TACACS+ (adaptar y probar):**

```cisco
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
 ! routers: transport input ssh
 ! SW-AREQ: transport input telnet
exit
```

### Verificaciones obligatorias

`show running-config | include aaa|tacacs`, `debug tacacs`, `debug aaa authentication`, `show ip ospf neighbor`, `show controllers s0/0/0`; registrar acceso exitoso e intento de fallback por consola.

### Preguntas de análisis

1. Comparar RADIUS y TACACS+ (puertos, UDP/TCP, cifrado, separación AAA y uso típico).
2. Explicar la ventaja de separar autenticación, autorización y accounting en TACACS+.
3. Explicar por qué el fallback del ejercicio se prueba **por consola** y no por SSH después de cortar la WAN.

**Archivo final:** `LAB02_E10_ApellidoNombre.pkt`.

## 6. Protocolo de validación antes de marcar cada ejercicio como listo

Para **cada proyecto**:

- [ ] `.pkt` real, abierto correctamente en Cisco Packet Tracer.
- [ ] Dispositivos con nombres y modelos correctos.
- [ ] Cableado, interfaces y módulos correctos conforme a figura del PDF.
- [ ] Direcciones, máscaras y gateways exactos.
- [ ] Configuración básica y banner aplicados a todos los routers y switches aplicables.
- [ ] Interfaces necesarias habilitadas (`no shutdown`).
- [ ] Servicios/protocolos del ejercicio operativos.
- [ ] Resultado de pruebas funcionales real y documentado.
- [ ] Restauradas todas las interfaces, rutas o servicios alterados durante pruebas de fallas.
- [ ] Capturas auténticas o salidas completas de verificación.
- [ ] Preguntas de análisis respondidas con fundamento y conclusión corta.
- [ ] Se guardó el archivo en el directorio y nombre requeridos.

### Criterios funcionales mínimos

| Ejercicio | Condición mínima comprobable |
|---|---|
| E07 | 3 PC reciben DHCP en la LAN correspondiente; impresora fija; comunicación entre ambas LAN |
| E08 | 3 VLAN reciben DHCP desde R-DHCP por relay; todas resuelven y abren `www.urp.lab` |
| E09 | Credenciales RADIUS funcionan vía SSH; usuario inexistente rechazado; respaldo local al desconectar AAA |
| E10 | Vecindad OSPF; TACACS+ autentica desde ambas sedes; acceso local por consola al interrumpir WAN |

## 7. Guía para el informe parcial (E07–E10)

El PDF solicita, **por cada ejercicio**, lo siguiente:

1. Captura de topología con etiquetas.
2. Tabla completa de direccionamiento verificada.
3. Configuraciones de **cada dispositivo**, en texto (`show running-config` o bloques IOS), con breve comentario.
4. Capturas de comandos de verificación y pruebas reales con interpretación.
5. Respuestas a las tres preguntas de análisis y conclusión breve.

La rúbrica da **1.0** por implementación, **0.5** por verificación y **0.5** por análisis, por ejercicio. Estos cuatro ejercicios suman **8 puntos** de los 20 del laboratorio completo. El PDF original exige los **10 ejercicios** como entrega total; estos archivos **no sustituyen** los ejercicios 01–06 si la entrega final mantiene ese alcance.

## 8. Orden de ejecución solicitado a Codex

1. Detectar sistema operativo, Packet Tracer instalado y disponibilidad de un **MCP** o paquete confiable para generar `.pkt`.
2. Inspeccionar el PDF y confirmar conexiones y puertos con las figuras.
3. Crear primero **E07**, el caso más simple. Guardar y abrir el `.pkt`; resolver problemas de compatibilidad antes de continuar.
4. Crear y probar **E08**, incluyendo DHCP relay, DNS y HTTP.
5. Crear y probar **E09** con RADIUS y respaldo local. Mantener un modo seguro de recuperación durante la configuración de AAA.
6. Crear y probar **E10** con módulos seriales, OSPF y TACACS+.
7. En cada etapa mantener `reporte.md` con tabla: **prueba**, **resultado observado**, **evidencia**, **estado (APROBADA / FALLIDA / NO EJECUTADA)**.
8. Entregar un resumen final con rutas de los cuatro `.pkt`, verificación real de apertura, pruebas aprobadas y limitaciones pendientes.

**Regla final:** no declarar éxito ni fabricar evidencias si Packet Tracer, la extensión de scripting, la librería `.pkt` o las funciones MCP no están disponibles.
