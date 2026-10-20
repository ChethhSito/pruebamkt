# E09 — Servicios y pruebas

## Orden seguro de configuración AAA

Las configuraciones son propuestas IOS basadas en el enunciado, todavía no probadas en Packet Tracer 9.0.1. Aplicarlas por etapas: primero configuración básica, interfaces y rutas; comprobar conectividad; configurar el servidor; crear localadmin y claves SSH; activar AAA y finalmente las líneas. Mantener abierta una consola de recuperación mientras se comprueban nuevas sesiones VTY. Guardar un `.pkt` intermedio antes de activar AAA.

## Hosts y servidor

Configurar las IP estáticas de montaje.md; DNS no es necesario para los accesos por IP. SRV-RADIUS > Services > AAA > On. Crear clientes tipo Radius y clave `RadiusURP2026`:

| Cliente | IP de origen prevista, por confirmar |
|---|---|
| R1 | 192.168.50.1 |
| R2 | 10.0.12.2 |
| SW1 | 192.168.50.2 |

Crear usuarios `admin` / `Admin2026` y `soporte` / `Soporte2026`. No crear localadmin en el servidor: es la cuenta de respaldo del equipo. Confirmar las IP de origen con Simulation (paquetes RADIUS) o debug antes de dar por correcto el registro. No se fuerza una source-interface sin comprobar soporte del IOS.

El PDF exige SSH solo en routers. SW1 se deja con Telnet en VTY como decisión de implementación para poder probar su AAA, no como requisito del docente; sus VTY 0–15 usan la lista default. Telnet se usa únicamente en este laboratorio. Si se prefiere SSH en SW1, comprobar primero su soporte y documentar el cambio.

## Pruebas y evidencias

1. Antes de AAA: ping desde PC-ADMIN a PC-REMOTO y desde cada cliente AAA a 192.168.50.100. SW1 necesita su SVI up/up y gateway configurado; R2 necesita la ruta de retorno indicada.
2. En los routers: `show ip route`, `show ip ssh`, `show users`, `show running-config | include aaa|radius`; en SW1: `show ip interface brief` y las líneas AAA de running-config. Si los filtros no se admiten, capturar `show running-config` completo.
3. Activar `debug aaa authentication`, abrir una nueva sesión de prueba y capturar su salida; terminar con `undebug all`. No dejar debug encendido al finalizar.
4. PC-ADMIN: `ssh -l admin 192.168.50.1` y contraseña Admin2026. PC-REMOTO: `ssh -l soporte 192.168.60.1` y contraseña Soporte2026. Registrar éxito real. Probar usuario `inexistente` con cualquier contraseña y registrar rechazo.
5. Para ejercitar SW1: PC-ADMIN, `telnet 192.168.50.2`, usuario admin / Admin2026. Comprobar también acceso por consola de los tres clientes y capturar autenticación AAA. Usar `enable` y clave class para configuración privilegiada si se necesita.
6. Desactivar temporalmente Services > AAA en SRV-RADIUS. Abrir sesiones nuevas (una sesión existente no valida autenticación), esperar los timeouts y probar localadmin / Local2026 en los tres equipos. Probar que admin sin cuenta local no entra durante la caída. Con servidor activo, una respuesta Access-Reject no debe interpretarse como servidor no disponible ni provocar fallback normal.
7. Reactivar AAA, repetir acceso con admin/soporte, verificar consola y guardar configuraciones y `.pkt`. Reabrir y repetir una sesión SSH. Registrar si la sintaxis `radius-server host ... key ...` es aceptada; si falla, usar ayuda contextual, registrar el error y la alternativa antes de continuar. No desactivar AAA para presentar éxito.
