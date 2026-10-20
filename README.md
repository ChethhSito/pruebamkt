# Laboratorio 02 — Andre Torres · 202210073

El repositorio contiene los cuatro proyectos `.pkt` y su generador **generar_pkt.py**, con topologías, configuraciones IOS y página HTTP incorporadas. No necesita los JSON ni las carpetas eliminadas.

## Ejecutar el generador

Requiere Python 3.10 o superior y `pkt-core==0.2.0` (terceros, no oficial de Cisco).

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\python.exe -m pip install pkt-core==0.2.0
.venv\Scripts\python.exe generar_pkt.py
```

Linux/macOS:

```bash
.venv/bin/python -m pip install pkt-core==0.2.0
.venv/bin/python generar_pkt.py
```

Guarda los cuatro archivos nuevos en `generados/`, sin sobrescribir los `.pkt` de la raíz. Puede elegirse otra carpeta con `--output-dir ruta`. Cada archivo se recarga con el codec y se comprueba que conserva documento, nombres y cantidades de equipos/enlaces. Esto **no equivale a abrirlo o probarlo en Packet Tracer**.

## Estado y ajustes pendientes en Cisco Packet Tracer 9.0.1.0858

- E07: 6 equipos y 5 enlaces. Falta Printer-PT **IMP-B**, que no está en las plantillas. Añadirla, conectarla a SW-ACA F0/3 y configurar 172.16.20.5/24, gateway 172.16.20.1.
- E08: 8 equipos y 7 enlaces. Configurar Services > DNS en SRV-DNS: registro A `www.urp.lab` → `10.0.0.10`; verificar HTTP y página con nombre/código.
- E09: 6 equipos y 5 enlaces. Revisar AAA RADIUS y orígenes R1=192.168.50.1, R2=10.0.12.2, SW1=192.168.50.2, clave RadiusURP2026. Usuarios admin/Admin2026 y soporte/Soporte2026.
- E10: 7 equipos y 6 enlaces. En SRV-TACACS, registrar clientes tipo Tacacs R-LIMA=10.10.10.1, R-AREQ=172.30.0.2 y SW-AREQ=10.20.20.2; clave TacacsURP2026. Activar AAA, dejado Off durante generación. Usuarios netadmin/Net2026 y auditor/Audit2026. Confirmar las IP de origen reales antes de validar.
- E09/E10: generar RSA en cada router desde CLI: `enable`, `configure terminal`, `crypto key generate rsa`, responder `1024` al prompt, `ip ssh version 2`, `end`. Las claves interactivas no se generan mediante running-config. Respaldo local: localadmin/Local2026; enable: class.
- En todos: revisar configuraciones aplicadas, etiquetas y añadir Place Note **Andre Torres — 202210073**. Guardar running-config a startup-config y el proyecto tras completar pruebas.

Los `.pkt` se generaron offline y se recargaron con pkt-core. **No se han abierto en Cisco ni ejecutado pruebas funcionales.** Faltan evidencias reales de DHCP, ping, DNS/HTTP, SSH/AAA, respaldo local y OSPF. Las configuraciones integradas son propuestas sujetas al soporte IOS del simulador.
