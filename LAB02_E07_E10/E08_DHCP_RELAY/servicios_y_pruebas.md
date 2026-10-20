# E08 — Servicios y pruebas

## Hosts y servicios

SRV-DNS: Desktop > IP Configuration > Static: IP 10.0.0.10, máscara 255.255.255.0, gateway 10.0.0.1 y DNS 10.0.0.10. Services > DNS > On: Name `www.urp.lab`, Type A, Address `10.0.0.10`, Add. Services > HTTP > On: editar index.html, reemplazar por `configs/index.html` y guardar. Las tres PC deben usar DHCP.

## Secuencia y evidencias

1. En SW-SEDE: `show vlan brief`, `show interfaces trunk`. F0/5, F0/10 y F0/15 deben pertenecer a VLAN 10, 20 y 30; G0/1 debe operar como troncal.
2. En R-SEDE: `show ip interface brief`, `show ip interface g0/0.10` (repetir .20 y .30) y `show ip route`. Comprobar helper y ruta por defecto.
3. En R-DHCP: `show ip route`, `show ip dhcp binding`, `show ip dhcp pool`. En cada PC ejecutar `ipconfig /all`; rango asignable por VLAN .21–.254 (234 direcciones), gateway .1 y DNS 10.0.0.10.
4. Desde cada PC: ping al gateway, ping 10.0.0.10, `ping www.urp.lab` para observar resolución y abrir `http://www.urp.lab` en Desktop > Web Browser. Capturar nombre y código mostrados. No basta un ping por IP para validar DNS/HTTP.
5. Prueba de rutas: guardar primero el estado bueno. En R-DHCP, configuración global:

```cisco
no ip route 192.168.10.0 255.255.255.0 10.1.1.2
no ip route 192.168.20.0 255.255.255.0 10.1.1.2
no ip route 192.168.30.0 255.255.255.0 10.1.1.2
```

Capturar `show ip route`; repetir ping y abrir web. Para probar DHCP de nuevo, liberar/renovar una PC y registrar el resultado; una concesión antigua no demuestra un nuevo intercambio exitoso. La pérdida de rutas impide devolver tráfico a redes remotas, incluso respuestas DHCP al giaddr. No suponer el resultado sin observarlo.

6. Restaurar inmediatamente las tres rutas:

```cisco
ip route 192.168.10.0 255.255.255.0 10.1.1.2
ip route 192.168.20.0 255.255.255.0 10.1.1.2
ip route 192.168.30.0 255.255.255.0 10.1.1.2
```

Renovar clientes afectados, repetir DNS/HTTP desde las tres VLAN, guardar y reabrir el `.pkt`. SW-CEN no necesita dirección IP de gestión.
