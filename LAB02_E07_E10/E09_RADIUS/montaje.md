# Montaje E09 — Andre Torres, 202210073

Estado: existe un `.pkt` generado offline y recargado con pkt-core; apertura y validación IOS en Cisco pendientes. Ver ../LEEME_PRIMERO.md antes de comenzar. Los pasos de montaje desde cero se conservan como referencia/alternativa.
Fuente: páginas 19–20 del PDF original. Ver `figura_fuente.png` (fuente, no evidencia propia).

## Equipos y disposición

| Nombre | Modelo |
|---|---|
| PC-ADMIN | PC-PT |
| PC-REMOTO | PC-PT |
| R1 | 1941 |
| R2 | 1941 |
| SRV-RADIUS | Server-PT |
| SW1 | 2960 |

Reproducir la posición de la figura. Renombrar Display Name en Config además del hostname IOS. Añadir Place Note: **Andre Torres — 202210073**. Rotular interfaces, redes y VLAN como en la figura.

## Cableado

| Equipo A | Puerto A | Equipo B | Puerto B | Cable | Origen |
|---|---|---|---|---|---|
| R1 | G0/1 | R2 | G0/1 | cruzado | figura 9 |
| R1 | G0/0 | SW1 | F0/24 | directo | figura 9 |
| SW1 | F0/1 | SRV-RADIUS | FastEthernet0 | directo | figura 9 |
| SW1 | F0/2 | PC-ADMIN | FastEthernet0 | directo | figura 9 |
| R2 | G0/0 | PC-REMOTO | FastEthernet0 | cruzado | figura 9 |

Los nombres de NIC pueden variar en la interfaz gráfica: usar la NIC Ethernet disponible del host. En E08 los puertos F0/1 y F0/2 de SW-CEN son elecciones documentadas porque la figura no los numera.

## Direccionamiento objetivo (aún no verificado)

| Equipo | Interfaz | Dirección/prefijo | Gateway |
|---|---|---|---|
| R1 | G0/0 | 192.168.50.1/24 | — |
| R1 | G0/1 | 10.0.12.1/30 | — |
| R2 | G0/1 | 10.0.12.2/30 | — |
| R2 | G0/0 | 192.168.60.1/24 | — |
| SW1 | VLAN 1 | 192.168.50.2/24 | 192.168.50.1 |
| SRV-RADIUS | NIC | 192.168.50.100/24 | 192.168.50.1 |
| PC-ADMIN | NIC | 192.168.50.10/24 | 192.168.50.1 |
| PC-REMOTO | NIC | 192.168.60.10/24 | 192.168.60.1 |

Máscara /24 = 255.255.255.0; /30 = 255.255.255.252. Las IP recibidas por DHCP se registran después de ejecutar, no se anticipan.

## Aplicar configuraciones

1. Crear un proyecto nuevo y cablear según la tabla; no mezclar los cuatro ejercicios.
2. En cada router/switch, abrir CLI. Si aparece el diálogo inicial, responder `no` y pulsar Enter. Partir de equipos nuevos, no reutilizar configuraciones de otra práctica.
3. Abrir el `.ios` correspondiente de `configs/` y pegar bloques pequeños. Son comandos CLI, no archivos `.pkt` ni salidas capturadas de running-config.
4. Ante cualquier `% Invalid input`, detener ese bloque y registrar comando y error. No dar por aplicada una configuración rechazada. Consultar `?` del equipo y documentar cualquier alternativa.
5. `crypto key generate rsa` es interactivo: introducir `1024` solo cuando pida el tamaño; no pegar esa línea como comando independiente. `copy running-config startup-config` puede pedir el nombre destino: pulsar Enter. Ver guía AAA para el orden seguro.
6. Configurar hosts/servidores desde Desktop > IP Configuration y Services según `servicios_y_pruebas.md`.
7. Ejecutar las pruebas, capturar resultados auténticos, restaurar los fallos inducidos y guardar el proyecto. Cerrar y volver a abrirlo para verificar persistencia.

Archivo que se debe guardar desde File > Save As: `LAB02_E09_TorresAndre.pkt` en esta carpeta. No crear ese archivo renombrando texto.
