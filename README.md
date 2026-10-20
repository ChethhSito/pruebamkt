# Laboratorio 02 — E07 a E10 — Andre Torres (202210073)

## Qué contiene esta entrega

Configuraciones IOS propuestas para los 14 routers/switches de cuatro ejercicios, manifiestos de cableado/direccionamiento, guías paso a paso, página HTTP de E08 e informes Markdown con análisis. Fuente original y figuras incluidas. Versión objetivo en tu PC: Cisco Packet Tracer 9.0.1.0858.

**No contiene archivos .pkt ni capturas de pruebas de simulación.** Aquí no hay Packet Tracer ejecutable, MCP de Packet Tracer ni generador instalado y validado. No se han inventado proyectos ni resultados. El PDF permite 8.2 o superior, pero la compatibilidad real se confirma abriendo y probando cada proyecto en tu versión.

## Cómo usarlo en tu otra PC

1. Descomprimir el ZIP. Comenzar por E07_DHCP/montaje.md y figura_fuente.png; crear un proyecto vacío en Packet Tracer.
2. Colocar equipos, poner nombres y cablear según montaje.md. Añadir Place Note con Andre Torres — 202210073.
3. Aplicar configs/*.ios por equipo desde CLI, en bloques y revisando errores. No importar el JSON como .pkt: es solo un manifiesto legible.
4. Aplicar servicios_y_pruebas.md; guardar salidas/capturas auténticas en evidencias/ y actualizar reporte.md. En AAA seguir el orden seguro y los prompts RSA.
5. Guardar desde Packet Tracer los proyectos con estos nombres, cada uno en su carpeta:
   - E07_DHCP/LAB02_E07_TorresAndre.pkt
   - E08_DHCP_RELAY/LAB02_E08_TorresAndre.pkt
   - E09_RADIUS/LAB02_E09_TorresAndre.pkt
   - E10_TACACS/LAB02_E10_TorresAndre.pkt
6. Cerrar y abrir cada archivo, comprobar operación y persistencia. Restaurar rutas, servicio AAA y enlace serial después de las pruebas de fallas.
7. Convertir los informes a Word/PDF, añadir carátula, sección/grupo y fecha de entrega reales, capturas y configuraciones finales reales. Los Markdown no sustituyen el formato Word/PDF exigido.

## Decisiones documentadas

- E08: SW-CEN F0/1 hacia router y F0/2 hacia servidor son elecciones porque la figura no rotula sus puertos.
- E09: SW1 VTY usa Telnet para ejercitar AAA; el PDF exige SSH en los routers. Es una decisión didáctica adicional, no un requisito original para SW1.
- E10: SSH usa urp.lab y RSA 1024 como valores elegidos compatibles con la referencia de E09, pendientes de aceptación del simulador.
- Las IP de origen AAA se anticipan por enrutamiento de salida y deben observarse en Simulation/debug antes de validar el registro.
- SW-LIMA no recibe IP de gestión porque no figura una en el PDF.
- Los .ios son propuestas, no configuraciones extraídas de un equipo. Cualquier incompatibilidad debe registrarse y resolverse con sintaxis soportada sin sustituir el protocolo.

## Alcance académico

Solo ejercicios 07–10 (8 puntos de los 20 del laboratorio completo). El PDF pide los diez ejercicios para la entrega total. Este paquete no cubre 01–06. No entregar informes con estados pendientes como si fueran verificación completa.
