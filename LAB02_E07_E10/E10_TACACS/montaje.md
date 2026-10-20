# Montaje E10 — Andre Torres, 202210073

Estado: material para montaje; no existe todavía un `.pkt` ni validación IOS en simulador.
Fuente: páginas 21–22 del PDF original. Ver `figura_fuente.png` (fuente, no evidencia propia).

## Equipos y disposición

| Nombre | Modelo |
|---|---|
| PC-AQP | PC-PT |
| PC-NOC | PC-PT |
| R-AREQ | 2911 + HWIC-2T |
| R-LIMA | 2911 + HWIC-2T |
| SRV-TACACS | Server-PT |
| SW-AREQ | 2960 |
| SW-LIMA | 2960 |

Reproducir la posición de la figura. Renombrar Display Name en Config además del hostname IOS. Añadir Place Note: **Andre Torres — 202210073**. Rotular interfaces, redes y VLAN como en la figura.

## Cableado

| Equipo A | Puerto A | Equipo B | Puerto B | Cable | Origen |
|---|---|---|---|---|---|
| R-LIMA | S0/0/0 | R-AREQ | S0/0/0 | serial DCE en R-LIMA | figura 10 |
| R-LIMA | G0/0 | SW-LIMA | F0/24 | directo | figura 10 |
| SW-LIMA | F0/1 | SRV-TACACS | FastEthernet0 | directo | figura 10 |
| SW-LIMA | F0/2 | PC-NOC | FastEthernet0 | directo | figura 10 |
| R-AREQ | G0/0 | SW-AREQ | F0/24 | directo | figura 10 |
| SW-AREQ | F0/2 | PC-AQP | FastEthernet0 | directo | figura 10 |

Los nombres de NIC pueden variar en la interfaz gráfica: usar la NIC Ethernet disponible del host. En E08 los puertos F0/1 y F0/2 de SW-CEN son elecciones documentadas porque la figura no los numera.

## Direccionamiento objetivo (aún no verificado)

| Equipo | Interfaz | Dirección/prefijo | Gateway |
|---|---|---|---|
| R-LIMA | G0/0 | 10.10.10.1/24 | — |
| R-LIMA | S0/0/0 DCE | 172.30.0.1/30 | — |
| R-AREQ | S0/0/0 | 172.30.0.2/30 | — |
| R-AREQ | G0/0 | 10.20.20.1/24 | — |
| SW-AREQ | VLAN 1 | 10.20.20.2/24 | 10.20.20.1 |
| SRV-TACACS | NIC | 10.10.10.100/24 | 10.10.10.1 |
| PC-NOC | NIC | 10.10.10.20/24 | 10.10.10.1 |
| PC-AQP | NIC | 10.20.20.20/24 | 10.20.20.1 |

Máscara /24 = 255.255.255.0; /30 = 255.255.255.252. Las IP recibidas por DHCP se registran después de ejecutar, no se anticipan.

## Aplicar configuraciones

1. Crear un proyecto nuevo y cablear según la tabla; no mezclar los cuatro ejercicios.
2. En cada router/switch, abrir CLI. Si aparece el diálogo inicial, responder `no` y pulsar Enter. Partir de equipos nuevos, no reutilizar configuraciones de otra práctica.
3. Abrir el `.ios` correspondiente de `configs/` y pegar bloques pequeños. Son comandos CLI, no archivos `.pkt` ni salidas capturadas de running-config.
4. Ante cualquier `% Invalid input`, detener ese bloque y registrar comando y error. No dar por aplicada una configuración rechazada. Consultar `?` del equipo y documentar cualquier alternativa.
5. `crypto key generate rsa` es interactivo: introducir `1024` solo cuando pida el tamaño; no pegar esa línea como comando independiente. `copy running-config startup-config` puede pedir el nombre destino: pulsar Enter. Ver guía AAA para el orden seguro.
6. Configurar hosts/servidores desde Desktop > IP Configuration y Services según `servicios_y_pruebas.md`.
7. Ejecutar las pruebas, capturar resultados auténticos, restaurar los fallos inducidos y guardar el proyecto. Cerrar y volver a abrirlo para verificar persistencia.

Archivo que se debe guardar desde File > Save As: `LAB02_E10_TorresAndre.pkt` en esta carpeta. No crear ese archivo renombrando texto.
