# E07 — Servicios y pruebas

## Hosts y servicios

En Desktop > IP Configuration, seleccionar DHCP en PC-A1, PC-A2 y PC-B1. En IMP-B > Config > FastEthernet0, configurar 172.16.20.5, máscara 255.255.255.0; colocar gateway 172.16.20.1 en la configuración global del dispositivo. No se requiere servidor DNS real ni salida a Internet: 8.8.8.8 es el parámetro solicitado del pool.

## Secuencia y evidencias

1. En R1: `show ip interface brief`, `show ip dhcp binding`, `show ip dhcp pool`, `show ip dhcp server statistics`, `show running-config | section dhcp`. Guardar capturas de cada salida.
2. En cada PC: `ipconfig /all`. PC-A1/A2 deben obtener direcciones de .11–.254 de 172.16.10.0/24; PC-B1 de .51–.199 de 172.16.20.0/24. Registrar valores reales, gateway .1 y DNS 8.8.8.8.
3. Capturar bindings en R1, ejecutar `ipconfig /release` y `ipconfig /renew` en PC-B1; capturar de nuevo `ipconfig /all`, bindings y estadísticas. Es válido que se renueve la misma IP.
4. PC-A1: ping a 172.16.10.1, a la IP real de PC-B1 y a 172.16.20.5. PC-B1: ping a la IP real de PC-A2 y a la impresora. Repetir tras resolución ARP si hubo pérdida inicial, registrándola.
5. Guardar configuraciones y `.pkt`; reabrirlo y comprobar DHCP y ping. Copiar configuraciones finales reales a evidencias/. Los switches no necesitan IP de gestión en este ejercicio.
