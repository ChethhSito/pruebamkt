# Montaje E07 — Andre Torres, 202210073

Estado: material para montaje; no existe todavía un `.pkt` ni validación IOS en simulador.
Fuente: páginas 15–16 del PDF original. Ver `figura_fuente.png` (fuente, no evidencia propia).

## Equipos y disposición

| Nombre | Modelo |
|---|---|
| IMP-B | Printer-PT |
| PC-A1 | PC-PT |
| PC-A2 | PC-PT |
| PC-B1 | PC-PT |
| R1 | 1941 |
| SW-ACA | 2960 |
| SW-ADM | 2960 |

Reproducir la posición de la figura. Renombrar Display Name en Config además del hostname IOS. Añadir Place Note: **Andre Torres — 202210073**. Rotular interfaces, redes y VLAN como en la figura.

## Cableado

| Equipo A | Puerto A | Equipo B | Puerto B | Cable | Origen |
|---|---|---|---|---|---|
| R1 | G0/0 | SW-ADM | F0/1 | directo | figura 7 |
| R1 | G0/1 | SW-ACA | F0/1 | directo | figura 7 |
| SW-ADM | F0/2 | PC-A1 | FastEthernet0 | directo | figura 7 |
| SW-ADM | F0/3 | PC-A2 | FastEthernet0 | directo | figura 7 |
| SW-ACA | F0/2 | PC-B1 | FastEthernet0 | directo | figura 7 |
| SW-ACA | F0/3 | IMP-B | FastEthernet0 | directo | figura 7 |

Los nombres de NIC pueden variar en la interfaz gráfica: usar la NIC Ethernet disponible del host. En E08 los puertos F0/1 y F0/2 de SW-CEN son elecciones documentadas porque la figura no los numera.

## Direccionamiento objetivo (aún no verificado)

| Equipo | Interfaz | Dirección/prefijo | Gateway |
|---|---|---|---|
| R1 | G0/0 | 172.16.10.1/24 | — |
| R1 | G0/1 | 172.16.20.1/24 | — |
| PC-A1 | NIC | DHCP: ADMIN | DHCP |
| PC-A2 | NIC | DHCP: ADMIN | DHCP |
| PC-B1 | NIC | DHCP: ACADEMICO | DHCP |
| IMP-B | NIC | 172.16.20.5/24 | 172.16.20.1 |

Máscara /24 = 255.255.255.0; /30 = 255.255.255.252. Las IP recibidas por DHCP se registran después de ejecutar, no se anticipan.

## Aplicar configuraciones

1. Crear un proyecto nuevo y cablear según la tabla; no mezclar los cuatro ejercicios.
2. En cada router/switch, abrir CLI. Si aparece el diálogo inicial, responder `no` y pulsar Enter. Partir de equipos nuevos, no reutilizar configuraciones de otra práctica.
3. Abrir el `.ios` correspondiente de `configs/` y pegar bloques pequeños. Son comandos CLI, no archivos `.pkt` ni salidas capturadas de running-config.
4. Ante cualquier `% Invalid input`, detener ese bloque y registrar comando y error. No dar por aplicada una configuración rechazada. Consultar `?` del equipo y documentar cualquier alternativa.
5. `crypto key generate rsa` es interactivo: introducir `1024` solo cuando pida el tamaño; no pegar esa línea como comando independiente. `copy running-config startup-config` puede pedir el nombre destino: pulsar Enter. Ver guía AAA para el orden seguro.
6. Configurar hosts/servidores desde Desktop > IP Configuration y Services según `servicios_y_pruebas.md`.
7. Ejecutar las pruebas, capturar resultados auténticos, restaurar los fallos inducidos y guardar el proyecto. Cerrar y volver a abrirlo para verificar persistencia.

Archivo que se debe guardar desde File > Save As: `LAB02_E07_TorresAndre.pkt` en esta carpeta. No crear ese archivo renombrando texto.
