# Montaje E08 — Andre Torres, 202210073

Estado: material para montaje; no existe todavía un `.pkt` ni validación IOS en simulador.
Fuente: páginas 17–18 del PDF original. Ver `figura_fuente.png` (fuente, no evidencia propia).

## Equipos y disposición

| Nombre | Modelo |
|---|---|
| PC-V10 | PC-PT |
| PC-V20 | PC-PT |
| PC-V30 | PC-PT |
| R-DHCP | 1941 |
| R-SEDE | 1941 |
| SRV-DNS | Server-PT |
| SW-CEN | 2960 |
| SW-SEDE | 2960 |

Reproducir la posición de la figura. Renombrar Display Name en Config además del hostname IOS. Añadir Place Note: **Andre Torres — 202210073**. Rotular interfaces, redes y VLAN como en la figura.

## Cableado

| Equipo A | Puerto A | Equipo B | Puerto B | Cable | Origen |
|---|---|---|---|---|---|
| R-DHCP | G0/1 | R-SEDE | G0/1 | cruzado | figura 8 |
| R-DHCP | G0/0 | SW-CEN | F0/1 | directo | puerto SW-CEN elegido; figura no lo rotula |
| SW-CEN | F0/2 | SRV-DNS | FastEthernet0 | directo | puerto SW-CEN elegido; figura no lo rotula |
| R-SEDE | G0/0 | SW-SEDE | G0/1 | directo | figura 8 |
| SW-SEDE | F0/5 | PC-V10 | FastEthernet0 | directo | figura 8 |
| SW-SEDE | F0/10 | PC-V20 | FastEthernet0 | directo | figura 8 |
| SW-SEDE | F0/15 | PC-V30 | FastEthernet0 | directo | figura 8 |

Los nombres de NIC pueden variar en la interfaz gráfica: usar la NIC Ethernet disponible del host. En E08 los puertos F0/1 y F0/2 de SW-CEN son elecciones documentadas porque la figura no los numera.

## Direccionamiento objetivo (aún no verificado)

| Equipo | Interfaz | Dirección/prefijo | Gateway |
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

Máscara /24 = 255.255.255.0; /30 = 255.255.255.252. Las IP recibidas por DHCP se registran después de ejecutar, no se anticipan.

## Aplicar configuraciones

1. Crear un proyecto nuevo y cablear según la tabla; no mezclar los cuatro ejercicios.
2. En cada router/switch, abrir CLI. Si aparece el diálogo inicial, responder `no` y pulsar Enter. Partir de equipos nuevos, no reutilizar configuraciones de otra práctica.
3. Abrir el `.ios` correspondiente de `configs/` y pegar bloques pequeños. Son comandos CLI, no archivos `.pkt` ni salidas capturadas de running-config.
4. Ante cualquier `% Invalid input`, detener ese bloque y registrar comando y error. No dar por aplicada una configuración rechazada. Consultar `?` del equipo y documentar cualquier alternativa.
5. `crypto key generate rsa` es interactivo: introducir `1024` solo cuando pida el tamaño; no pegar esa línea como comando independiente. `copy running-config startup-config` puede pedir el nombre destino: pulsar Enter. Ver guía AAA para el orden seguro.
6. Configurar hosts/servidores desde Desktop > IP Configuration y Services según `servicios_y_pruebas.md`.
7. Ejecutar las pruebas, capturar resultados auténticos, restaurar los fallos inducidos y guardar el proyecto. Cerrar y volver a abrirlo para verificar persistencia.

Archivo que se debe guardar desde File > Save As: `LAB02_E08_TorresAndre.pkt` en esta carpeta. No crear ese archivo renombrando texto.
