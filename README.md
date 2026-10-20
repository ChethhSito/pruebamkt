# Laboratorio 02 — Redes 2 — Ejercicios 01–10

Dos juegos de diez proyectos `.pkt`, uno por ejercicio y estudiante:

| Archivos | Nombre | Código |
|---|---|---|
| `LAB02_E01_TorresAndre.pkt` … `LAB02_E10_TorresAndre.pkt` | Andre Torres | 202210073 |
| `LAB02_E01_LauraCarranzaMarin.pkt` … `LAB02_E10_LauraCarranzaMarin.pkt` | Laura Carranza Marin | 202211310 |

Generados offline con **pkt-core 0.2.0**, herramienta de terceros. Destino: Cisco Packet Tracer **9.0.1.0858**. No se han abierto en Cisco ni ejecutado pruebas de red. La recarga con el codec confirma integridad de generación; no confirma aceptación por Cisco, sintaxis IOS ni funcionamiento de protocolos.

## Etiquetas de texto

En los veinte archivos se activó la visualización nativa de nombres/modelos de equipos y nombres de puertos (`PORTSHOWN=true`, `HIDEDEVICELABEL=false`). Las interfaces IOS incluyen descripciones del vecino y su puerto. El perfil, las descripciones de equipos, los banners y la página HTTP de E08 llevan los datos de cada estudiante.

Estas son etiquetas nativas y descripciones; **no se generaron notas libres de lienzo tipo Place Note**, porque su estructura no está documentada en la API instalada. Añadir esa nota en Cisco con nombre y código. Para automatizarla con seguridad se necesita un `.pkt` de ejemplo guardado por Cisco que contenga una nota. También se debe comprobar visualmente que la versión local respete las opciones de visualización guardadas.

## Generar los archivos con Python

El único script es `generar_pkt.py`; incluye topologías y configuraciones, sin depender de carpetas eliminadas. Requiere Python 3.10 o superior y `pkt-core==0.2.0`.

Crear un entorno virtual:

```bash
python -m venv .venv
```

Windows (PowerShell):

```powershell
.\.venv\Scripts\python.exe -m pip install pkt-core==0.2.0
.\.venv\Scripts\python.exe generar_pkt.py
.\.venv\Scripts\python.exe generar_pkt.py --student-name "Laura Carranza Marin" --student-code 202211310 --file-suffix LauraCarranzaMarin
```

Linux/macOS:

```bash
.venv/bin/python -m pip install pkt-core==0.2.0
.venv/bin/python generar_pkt.py
.venv/bin/python generar_pkt.py --student-name "Laura Carranza Marin" --student-code 202211310 --file-suffix LauraCarranzaMarin
```

Por defecto escribe los diez proyectos de Andre en `generados/`. La segunda invocación añade los diez de Laura. `--output-dir ruta` cambia la carpeta destino; usar una carpeta nueva para preservar modificaciones hechas después en Cisco. Cada archivo se guarda, se recarga y se comprueba su contenido XML, nombres y cantidades de dispositivos/enlaces. El script muestra los resultados por consola. Los nombres/códigos se personalizan dentro del contenido, no solo en el nombre del archivo.

## Contenido de los proyectos y validación pendiente

Se consultaron las figuras y tablas del PDF original: páginas 3–14 para E01–E06, 15–22 para E07–E10. Los proyectos llevan el estado final propuesto. Las fases iniciales y fallas temporales del laboratorio no se presentan como ya realizadas; deben ejecutarse y documentarse en Cisco.

| Ejercicio | Equipos/enlaces por proyecto | Configuración incluida | Comprobación requerida en Cisco |
|---|---|---|---|
| 01 | 7 / 7 | Triángulo 2960, SVI VLAN1, S1 prioridad 4096, S2 8192, PortFast/BPDU Guard en puertos de usuario | Elección inicial/final, cambio de costo, convergencia, err-disabled y recuperación |
| 02 | 8 / 9 | VLAN10/20/99, troncales con nativa99, raíces por VLAN, estado final Rapid PVST+, Root Guard y BPDU Guard | Comparar PVST+ y Rapid PVST+, puertos bloqueados y prueba Root Guard |
| 03 | 6 / 7 | Tres enlaces físicos, Po1 LACP active/passive, VLAN10/20/99, balanceo src-dst-mac | Bundle SU/P, caída de miembro, passive/passive y restauración |
| 04 | 5 / 8 | Núcleo 3560, LACP Po1, PAgP Po2, estático Po3, SVI/routing, raíz MLS1, balanceo src-dst-ip | Canales, troncal, STP y ping inter-VLAN |
| 05 | 6 / 6 | ISP/R1/R2 1941, OSPF1 área0, Lo0 8.8.8.8, HSRPv2 grupo10, R1 prioridad150 y preempt | Vecinos, ping/tracert, MAC virtual, failover y recuperación |
| 06 | 7 / 10 | WAN 2911, dos 3560 y dos 2960, Po1 LACP, OSPF, HSRPv2 VLAN10/20/99, tracking decremento60 | Confirmar soporte de tracking/HSRPv2, roles por VLAN y transferencia al caer uplink |
| 07 | 6 / 5 | Router DHCP, dos LAN, tres PC en DHCP | **Falta impresora**; añadir y probar DHCP/renovación/ping |
| 08 | 8 / 7 | VLAN10/20/30, router-on-a-stick, helper, pools/rutas, IP de servidor y HTML personalizado | Completar registro DNS, comprobar HTTP desde cada VLAN y prueba de rutas |
| 09 | 6 / 5 | IP/rutas, RADIUS con usuarios/clientes, lista default y respaldo local | Generar claves RSA, confirmar origen/puertos, login/rechazo/fallback |
| 10 | 7 / 6 | HWIC-2T, serial DCE en Lima, clock64000, OSPF, listas CONSOLA/REMOTO, usuarios servidor | Registrar clientes Tacacs y activar AAA, generar RSA, probar accesos y respaldo por consola |

### E01–E06: procedimientos para ejecutar, sin resultados inventados

- **E01:** para observar la elección por defecto antes del estado final, guardar copia, poner prioridad32768 en VLAN1 de S1/S2/S3 y desactivar temporalmente las guardas de acceso; capturar Bridge ID/roles. Restaurar S1=4096 y S2=8192; configurar costo100 en S2 F0/1, medir y quitar con `no spanning-tree cost`. Probar ping PC1→PC4 al apagar S1 F0/2; restaurar. Para BPDU Guard, desconectar temporalmente PC4 de S3 F0/12, conectar un switch y registrar err-disabled; retirar el switch y recuperar con shutdown/no shutdown, reconectar PC4. Volver a aplicar las guardas si se retiraron.
- **E02:** el archivo trae Rapid PVST+ final. Para comparar, guardar copia, configurar `spanning-tree mode pvst` en los cuatro switches, medir la caída del troncal activo de AS1 hacia raíz VLAN10 y restaurar; cambiar todos a `spanning-tree mode rapid-pvst`, repetir y restaurar. Bajar AS2 VLAN20 a prioridad0, observar root-inconsistent en DS2 y restaurar AS2 a32768. No anotar tiempos ni puertos bloqueados sin observarlos.
- **E03:** el archivo trae Po1 final. Para capturar el estado previo a EtherChannel, usar copia temporal, apagar F0/1–3 en ambos extremos, retirar channel-group1, eliminar Po1 si corresponde y volver a encender los enlaces; registrar STP. Después reabrir el proyecto final y comprobar LACP. Probar apagado de SW-A F0/1 y restaurarlo. Cambiar SW-A a passive en copia de prueba, observar falta de negociación con SW-B passive y restaurar active.
- **E04:** ejecutar `show etherchannel summary`, `show etherchannel protocol`, `show interfaces trunk`, `show spanning-tree`, `show ip route` y ping PC1→192.168.20.10. Verificar Po1 LACP, Po2 PAgP, Po3 on y puertos según figura. MLS1 debe enrutar y ser raíz; identificar el bloqueo real.
- **E05:** ejecutar `show standby brief`, `show standby`, `show ip ospf neighbor`, `show ip route`; desde PC1, `tracert 8.8.8.8` y `arp -a`. Mientras PC2 hace ping, apagar G0/0 de R1, registrar pérdidas/rol activo/tracert y restaurar. La IP 8.8.8.8 es una loopback simulada, no acceso real a Internet.
- **E06:** revisar `show standby brief`, `show spanning-tree root`, `show etherchannel summary`, `show ip ospf neighbor`, `show ip route` y tracert200.10.10.1 desde PC10/PC20. La configuración propone sintaxis IOS clásica `standby 10 track GigabitEthernet0/1 60` en DSW1 y grupo20 en DSW2. **Su aceptación no está verificada**: registrar cualquier error, consultar ayuda IOS y no marcar tracking como logrado si el simulador lo rechaza. Si el IOS soporta objetos de seguimiento, la alternativa es `track 1 interface GigabitEthernet0/1 line-protocol` y `standby 10 track 1 decrement 60` (grupo20 en DSW2), también sujeta a verificación. Cortar G0/1 de DSW1, observar disminución150→90 y traslado del grupo10, restaurar y comprobar recuperación.

### E07–E10: ajustes pendientes

- **E07:** la librería no contiene plantilla Printer-PT. Añadir IMP-B, cable directo a SW-ACA F0/3, IP172.16.20.5/24 y gateway172.16.20.1. PC-A1/A2 deben obtener DHCP172.16.10.11–254 y PC-B1 172.16.20.51–199; no se anticipa la IP exacta. Probar release/renew en PC-B1 y revisar bindings; la misma IP renovada es válida.
- **E08:** SRV-DNS=10.0.0.10/24, gateway10.0.0.1. Configurar Services > DNS, registro A `www.urp.lab`→10.0.0.10. HTTP debe estar On y mostrar nombre/código. Probar DHCP, resolución y navegador desde las tres VLAN. SW-CEN F0/1 hacia router y F0/2 hacia servidor son elecciones porque la figura no los rotula. Retirar y restaurar las rutas del servidor para la prueba del PDF.
- **E09:** revisar clientes Radius R1=192.168.50.1, R2=10.0.12.2 y SW1=192.168.50.2, clave `RadiusURP2026`, usuarios `admin/Admin2026` y `soporte/Soporte2026`. Confirmar origen real con Simulation/debug. La plantilla usa puerto1645: contrastar con IOS. SSH es obligatorio en routers; SW1 usa Telnet como decisión didáctica para probar VTY. Probar credenciales válidas, inexistente y respaldo al desactivar temporalmente AAA; reactivarlo al terminar.
- **E10:** en SRV-TACACS registrar clientes tipo **Tacacs** R-LIMA=10.10.10.1, R-AREQ=172.30.0.2 y SW-AREQ=10.20.20.2, clave `TacacsURP2026`; confirmar origen real. Usuarios ya incluidos: `netadmin/Net2026`, `auditor/Audit2026`. **Activar AAA**, dejado Off durante generación porque el enum interno Tacacs no está documentado. No inventar IP de gestión para SW-LIMA. Probar consola con WAN cortada en R-AREQ y restaurar serial/OSPF/AAA.
- **E09/E10, SSH:** en cada router: `enable`, `configure terminal`, `crypto key generate rsa`, responder1024 al prompt, `ip ssh version 2`, `end`. Las claves interactivas no se generan mediante running-config. Verificar `show ip ssh`.

## Finalización y evidencias

Todas las pruebas funcionales están **NO EJECUTADAS** en este entorno. No presentar la generación como simulación validada. Revisar que Cisco haya aplicado los comandos; registrar errores e incompatibilidades. Guardar capturas auténticas de topología y de todos los comandos exigidos en el PDF, tablas reales, análisis e informe Word/PDF. Al terminar pruebas de fallas restaurar todos los puertos/rutas/servicios, ejecutar `copy running-config startup-config` en cada equipo y guardar, cerrar y volver a abrir cada proyecto.

Credenciales didácticas del laboratorio: enable=`class`, consola básica=`cisco`; en los clientes AAA, respaldo=`localadmin/Local2026`. Una sesión ya abierta no valida un nuevo login; un rechazo explícito del servidor AAA normalmente no activa el método local. Las claves compartidas/usuarios son los exigidos por el enunciado y no credenciales personales.
