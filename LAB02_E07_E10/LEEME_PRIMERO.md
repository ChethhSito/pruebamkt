# Laboratorio 02 — E07 a E10 — Andre Torres (202210073)

## Abrir las topologías generadas

Ahora se incluyen cuatro **contenedores .pkt generados offline con pkt-core 0.2.0**. La librería ha podido guardarlos y volver a leerlos conservando el documento. **No han sido abiertos en Cisco Packet Tracer ni se han ejecutado pruebas funcionales.** No son una entrega terminada ni garantizada compatible; abrirlos primero en tu Packet Tracer 9.0.1.0858.

| Proyecto | Equipos/enlaces incluidos | Trabajo visual pendiente |
|---|---|---|
| E07_DHCP/LAB02_E07_TorresAndre.pkt | 6 equipos, 5 enlaces | Añadir Printer-PT IMP-B, conectar a SW-ACA F0/3 y configurar 172.16.20.5/24, gateway 172.16.20.1 |
| E08_DHCP_RELAY/LAB02_E08_TorresAndre.pkt | 8 equipos, 7 enlaces | Revisar etiquetas/notas |
| E09_RADIUS/LAB02_E09_TorresAndre.pkt | 6 equipos, 5 enlaces | Revisar etiquetas/notas |
| E10_TACACS/LAB02_E10_TorresAndre.pkt | 7 equipos, 6 enlaces | Revisar etiquetas/notas y serial DCE |

Se colocaron equipos con coordenadas siguiendo las figuras y se incorporaron las configuraciones IOS no interactivas. Esto evita construir manualmente la mayor parte de las topologías. El JSON es solo un manifiesto; los .pkt se escribieron con el codec de pkt-core, no renombrando texto.

## Pasos pendientes al abrirlos (obligatorios)

1. Abrir cada .pkt con Packet Tracer 9.0.1. Si aparece un error, guardar el mensaje exacto. No confundir una recarga mediante pkt-core con una prueba en Cisco.
2. Revisar modelos, interfaces y cableado frente a montaje.md y figura_fuente.png. Añadir Place Note **Andre Torres — 202210073** y etiquetas de enlaces conforme al PDF; no se generaron notas gráficas con una estructura no documentada.
3. E07: añadir la impresora que falta; su modelo no viene en las 137 plantillas de la versión instalada. No fue sustituida por un PC.
4. E08: verificar DHCP en las PC y configurar manualmente Services > DNS: registro A www.urp.lab → 10.0.0.10. La página index.html ya contiene nombre/código dentro del archivo; verificar que HTTP esté On y la muestre.
5. E09/E10: generar claves SSH desde la CLI de cada router: `enable`, `configure terminal`, `crypto key generate rsa`, responder 1024 al prompt, `ip ssh version 2`, `end`. La generación interactiva de claves no se incrustó como si fuese una línea de running-config. Verificar con `show ip ssh`.
6. E09: usuarios y clientes RADIUS están cargados según los campos de la plantilla; revisar IP de origen, servicio On y puerto de autenticación (plantilla 1645) frente al comportamiento IOS. Comprobar consola y SSH. Credenciales y pruebas están en servicios_y_pruebas.md.
7. E10: los usuarios están cargados, pero el servicio AAA se dejó **Off** deliberadamente; registrar los tres clientes tipo **Tacacs**, clave TacacsURP2026 e IP de origen según servicios_y_pruebas.md y activar AAA. El enum interno TACACS no estaba documentado: no se inventó. Durante el montaje puede usarse el respaldo local localadmin / Local2026.
8. Comprobar que IOS haya aplicado las configuraciones incrustadas; ante errores usar configs/*.ios por bloques, conservando consola de recuperación. Consultar las guías por ejercicio para enrutamiento, DHCP, OSPF y AAA.
9. Ejecutar todos los procedimientos de servicios_y_pruebas.md, guardar capturas auténticas en evidencias/ y actualizar reporte.md. Restaurar los fallos inducidos, ejecutar `copy running-config startup-config`, guardar, cerrar y volver a abrir cada proyecto.
10. Completar sección/grupo y fecha de entrega reales. Convertir informes a Word/PDF y agregar resultados, captura propia de topología y configuraciones finales reales.

## Generador reproducible

En la raíz del repositorio:

```bash
python -m venv .venv
# Linux/macOS:
.venv/bin/python -m pip install -r herramientas/requirements.txt
.venv/bin/python herramientas/generar_pkt.py
# En Windows usar .venv\Scripts\python.exe en lugar de .venv/bin/python
```

La API usada se inspeccionó en la instalación 0.2.0: `Lab`, `add_device`, `link`, `save` y recarga `Lab(seed=..., auto_prune_seed=False)`. Los campos de hosts/servidores se tomaron de las plantillas incluidas. No requiere tener Cisco instalado para generar; sí para verificar funcionamiento. Referencia: https://pypi.org/project/pkt-core/0.2.0/ . Es una herramienta de terceros por ingeniería inversa, no una API oficial de Cisco.

## Alcance y evidencias

Los archivos validacion_generacion.json registran equipos, enlaces y recarga del codec; **no** certifican apertura en Cisco ni pruebas DHCP, ping, DNS, SSH, OSPF o AAA. Las tablas de los informes permanecen NO EJECUTADA hasta obtener resultados reales. El paquete solo cubre E07–E10, no los ejercicios 01–06 que también pide el PDF para la entrega total.

Se conservan configs/*.ios, guías de montaje completo, informes con análisis, fuente y figuras. Las guías de montaje sirven también como alternativa si Cisco rechaza algún archivo generado. E08 elige SW-CEN F0/1 y F0/2 porque la figura no los numera; E09 SW1 usa Telnet por decisión didáctica, SSH obligatorio en routers; E10 dominio urp.lab/RSA1024 son elecciones documentadas; SW-LIMA no recibe IP de gestión inventada.
