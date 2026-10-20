"""Generación offline de los diez ejercicios con pkt-core 0.2.0.
No sustituye apertura, ejecución IOS ni validación funcional en Packet Tracer.
"""
from pathlib import Path
import argparse, json, xml.etree.ElementTree as ET
from pkt_core import Lab

parser=argparse.ArgumentParser(description='Genera E01–E10 offline; no verifica funcionamiento en Cisco.')
parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent/'generados', help='Carpeta de salida (predeterminada: generados/).')
parser.add_argument('--student-name', default='Andre Torres')
parser.add_argument('--student-code', default='202210073')
parser.add_argument('--file-suffix', default='TorresAndre')
args=parser.parse_args()
import re
if any(c in args.student_name for c in '\r\n#'):
    parser.error('El nombre no puede contener saltos de línea ni #.')
if not re.fullmatch(r'[A-Za-z0-9_-]+',args.file_suffix):
    parser.error('El sufijo de archivos solo permite letras ASCII, números, _ y -.')
if not re.fullmatch(r'[A-Za-z0-9]+',args.student_code):
    parser.error('El código solo permite letras y números.')
args.output_dir.mkdir(parents=True,exist_ok=True)
DATA=json.loads('[{"spec": {"exercise": 7, "student": {"name": "Andre Torres", "code": "202210073"}, "target_packet_tracer": "9.0.1.0858", "pkt_created": true, "simulation_verified": false, "devices": [{"name": "IMP-B", "model": "Printer-PT"}, {"name": "PC-A1", "model": "PC-PT"}, {"name": "PC-A2", "model": "PC-PT"}, {"name": "PC-B1", "model": "PC-PT"}, {"name": "R1", "model": "1941"}, {"name": "SW-ACA", "model": "2960"}, {"name": "SW-ADM", "model": "2960"}], "links": [{"device_a": "R1", "port_a": "G0/0", "device_b": "SW-ADM", "port_b": "F0/1", "cable": "directo", "source": "figura 7"}, {"device_a": "R1", "port_a": "G0/1", "device_b": "SW-ACA", "port_b": "F0/1", "cable": "directo", "source": "figura 7"}, {"device_a": "SW-ADM", "port_a": "F0/2", "device_b": "PC-A1", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 7"}, {"device_a": "SW-ADM", "port_a": "F0/3", "device_b": "PC-A2", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 7"}, {"device_a": "SW-ACA", "port_a": "F0/2", "device_b": "PC-B1", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 7"}, {"device_a": "SW-ACA", "port_a": "F0/3", "device_b": "IMP-B", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 7"}], "addressing": [{"device": "R1", "interface": "G0/0", "address": "172.16.10.1/24", "gateway": "—"}, {"device": "R1", "interface": "G0/1", "address": "172.16.20.1/24", "gateway": "—"}, {"device": "PC-A1", "interface": "NIC", "address": "DHCP: ADMIN", "gateway": "DHCP"}, {"device": "PC-A2", "interface": "NIC", "address": "DHCP: ADMIN", "gateway": "DHCP"}, {"device": "PC-B1", "interface": "NIC", "address": "DHCP: ACADEMICO", "gateway": "DHCP"}, {"device": "IMP-B", "interface": "NIC", "address": "172.16.20.5/24", "gateway": "172.16.20.1"}], "generated_devices": ["PC-A1", "PC-A2", "PC-B1", "R1", "SW-ACA", "SW-ADM"], "generation_limitations": ["IMP-B: modelo Printer-PT no incluido en las plantillas; añadir manualmente con sus dos parámetros IP y gateway y conectar IMP-B a SW-ACA F0/3; IP 172.16.20.5/24, gateway 172.16.20.1."]}, "configs": {"R1": "enable\\nconfigure terminal\\nhostname R1\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\ninterface GigabitEthernet0/0\\n ip address 172.16.10.1 255.255.255.0\\n no shutdown\\nexit\\ninterface GigabitEthernet0/1\\n ip address 172.16.20.1 255.255.255.0\\n no shutdown\\nexit\\nip dhcp excluded-address 172.16.10.1 172.16.10.10\\nip dhcp excluded-address 172.16.20.1 172.16.20.50\\nip dhcp excluded-address 172.16.20.200 172.16.20.254\\nip dhcp pool ADMIN\\n network 172.16.10.0 255.255.255.0\\n default-router 172.16.10.1\\n dns-server 8.8.8.8\\n domain-name urp.lab\\nexit\\nip dhcp pool ACADEMICO\\n network 172.16.20.0 255.255.255.0\\n default-router 172.16.20.1\\n dns-server 8.8.8.8\\n domain-name urp.lab\\nexit\\nend\\ncopy running-config startup-config\\n", "SW-ACA": "enable\\nconfigure terminal\\nhostname SW-ACA\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\ninterface FastEthernet0/1\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/2\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/3\\n switchport mode access\\n no shutdown\\nexit\\nend\\ncopy running-config startup-config\\n", "SW-ADM": "enable\\nconfigure terminal\\nhostname SW-ADM\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\ninterface FastEthernet0/1\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/2\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/3\\n switchport mode access\\n no shutdown\\nexit\\nend\\ncopy running-config startup-config\\n"}, "html": ""}, {"spec": {"exercise": 8, "student": {"name": "Andre Torres", "code": "202210073"}, "target_packet_tracer": "9.0.1.0858", "pkt_created": true, "simulation_verified": false, "devices": [{"name": "PC-V10", "model": "PC-PT"}, {"name": "PC-V20", "model": "PC-PT"}, {"name": "PC-V30", "model": "PC-PT"}, {"name": "R-DHCP", "model": "1941"}, {"name": "R-SEDE", "model": "1941"}, {"name": "SRV-DNS", "model": "Server-PT"}, {"name": "SW-CEN", "model": "2960"}, {"name": "SW-SEDE", "model": "2960"}], "links": [{"device_a": "R-DHCP", "port_a": "G0/1", "device_b": "R-SEDE", "port_b": "G0/1", "cable": "cruzado", "source": "figura 8"}, {"device_a": "R-DHCP", "port_a": "G0/0", "device_b": "SW-CEN", "port_b": "F0/1", "cable": "directo", "source": "puerto SW-CEN elegido; figura no lo rotula"}, {"device_a": "SW-CEN", "port_a": "F0/2", "device_b": "SRV-DNS", "port_b": "FastEthernet0", "cable": "directo", "source": "puerto SW-CEN elegido; figura no lo rotula"}, {"device_a": "R-SEDE", "port_a": "G0/0", "device_b": "SW-SEDE", "port_b": "G0/1", "cable": "directo", "source": "figura 8"}, {"device_a": "SW-SEDE", "port_a": "F0/5", "device_b": "PC-V10", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 8"}, {"device_a": "SW-SEDE", "port_a": "F0/10", "device_b": "PC-V20", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 8"}, {"device_a": "SW-SEDE", "port_a": "F0/15", "device_b": "PC-V30", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 8"}], "addressing": [{"device": "R-DHCP", "interface": "G0/0", "address": "10.0.0.1/24", "gateway": "—"}, {"device": "R-DHCP", "interface": "G0/1", "address": "10.1.1.1/30", "gateway": "—"}, {"device": "R-SEDE", "interface": "G0/1", "address": "10.1.1.2/30", "gateway": "—"}, {"device": "R-SEDE", "interface": "G0/0.10", "address": "192.168.10.1/24", "gateway": "—"}, {"device": "R-SEDE", "interface": "G0/0.20", "address": "192.168.20.1/24", "gateway": "—"}, {"device": "R-SEDE", "interface": "G0/0.30", "address": "192.168.30.1/24", "gateway": "—"}, {"device": "SRV-DNS", "interface": "NIC", "address": "10.0.0.10/24", "gateway": "10.0.0.1"}, {"device": "PC-V10", "interface": "NIC", "address": "DHCP: VLAN10", "gateway": "DHCP"}, {"device": "PC-V20", "interface": "NIC", "address": "DHCP: VLAN20", "gateway": "DHCP"}, {"device": "PC-V30", "interface": "NIC", "address": "DHCP: VLAN30", "gateway": "DHCP"}], "generated_devices": ["PC-V10", "PC-V20", "PC-V30", "R-DHCP", "R-SEDE", "SRV-DNS", "SW-CEN", "SW-SEDE"], "generation_limitations": []}, "configs": {"R-DHCP": "enable\\nconfigure terminal\\nhostname R-DHCP\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\ninterface GigabitEthernet0/0\\n ip address 10.0.0.1 255.255.255.0\\n no shutdown\\nexit\\ninterface GigabitEthernet0/1\\n ip address 10.1.1.1 255.255.255.252\\n no shutdown\\nexit\\nip route 192.168.10.0 255.255.255.0 10.1.1.2\\nip dhcp excluded-address 192.168.10.1 192.168.10.20\\nip dhcp pool VLAN10\\n network 192.168.10.0 255.255.255.0\\n default-router 192.168.10.1\\n dns-server 10.0.0.10\\n domain-name urp.lab\\nexit\\nip route 192.168.20.0 255.255.255.0 10.1.1.2\\nip dhcp excluded-address 192.168.20.1 192.168.20.20\\nip dhcp pool VLAN20\\n network 192.168.20.0 255.255.255.0\\n default-router 192.168.20.1\\n dns-server 10.0.0.10\\n domain-name urp.lab\\nexit\\nip route 192.168.30.0 255.255.255.0 10.1.1.2\\nip dhcp excluded-address 192.168.30.1 192.168.30.20\\nip dhcp pool VLAN30\\n network 192.168.30.0 255.255.255.0\\n default-router 192.168.30.1\\n dns-server 10.0.0.10\\n domain-name urp.lab\\nexit\\nend\\ncopy running-config startup-config\\n", "R-SEDE": "enable\\nconfigure terminal\\nhostname R-SEDE\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\ninterface GigabitEthernet0/1\\n ip address 10.1.1.2 255.255.255.252\\n no shutdown\\nexit\\ninterface GigabitEthernet0/0\\n no shutdown\\nexit\\ninterface GigabitEthernet0/0.10\\n encapsulation dot1Q 10\\n ip address 192.168.10.1 255.255.255.0\\n ip helper-address 10.1.1.1\\nexit\\ninterface GigabitEthernet0/0.20\\n encapsulation dot1Q 20\\n ip address 192.168.20.1 255.255.255.0\\n ip helper-address 10.1.1.1\\nexit\\ninterface GigabitEthernet0/0.30\\n encapsulation dot1Q 30\\n ip address 192.168.30.1 255.255.255.0\\n ip helper-address 10.1.1.1\\nexit\\nip route 0.0.0.0 0.0.0.0 10.1.1.1\\nend\\ncopy running-config startup-config\\n", "SW-CEN": "enable\\nconfigure terminal\\nhostname SW-CEN\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\ninterface FastEthernet0/1\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/2\\n switchport mode access\\n no shutdown\\nexit\\nend\\ncopy running-config startup-config\\n", "SW-SEDE": "enable\\nconfigure terminal\\nhostname SW-SEDE\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\nvlan 10\\n name ALUMNOS\\nexit\\ninterface FastEthernet0/5\\n switchport mode access\\n switchport access vlan 10\\n no shutdown\\nexit\\nvlan 20\\n name DOCENTES\\nexit\\ninterface FastEthernet0/10\\n switchport mode access\\n switchport access vlan 20\\n no shutdown\\nexit\\nvlan 30\\n name ADMINISTRATIVOS\\nexit\\ninterface FastEthernet0/15\\n switchport mode access\\n switchport access vlan 30\\n no shutdown\\nexit\\ninterface GigabitEthernet0/1\\n switchport mode trunk\\n no shutdown\\nexit\\nend\\ncopy running-config startup-config\\n"}, "html": "<!doctype html>\\n<html><head><title>URP - Laboratorio 02</title></head><body><h1>Andre Torres</h1><p>Codigo: 202210073</p><p>Ejercicio 08 - DHCP relay, DNS y HTTP</p></body></html>\\n"}, {"spec": {"exercise": 9, "student": {"name": "Andre Torres", "code": "202210073"}, "target_packet_tracer": "9.0.1.0858", "pkt_created": true, "simulation_verified": false, "devices": [{"name": "PC-ADMIN", "model": "PC-PT"}, {"name": "PC-REMOTO", "model": "PC-PT"}, {"name": "R1", "model": "1941"}, {"name": "R2", "model": "1941"}, {"name": "SRV-RADIUS", "model": "Server-PT"}, {"name": "SW1", "model": "2960"}], "links": [{"device_a": "R1", "port_a": "G0/1", "device_b": "R2", "port_b": "G0/1", "cable": "cruzado", "source": "figura 9"}, {"device_a": "R1", "port_a": "G0/0", "device_b": "SW1", "port_b": "F0/24", "cable": "directo", "source": "figura 9"}, {"device_a": "SW1", "port_a": "F0/1", "device_b": "SRV-RADIUS", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 9"}, {"device_a": "SW1", "port_a": "F0/2", "device_b": "PC-ADMIN", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 9"}, {"device_a": "R2", "port_a": "G0/0", "device_b": "PC-REMOTO", "port_b": "FastEthernet0", "cable": "cruzado", "source": "figura 9"}], "addressing": [{"device": "R1", "interface": "G0/0", "address": "192.168.50.1/24", "gateway": "—"}, {"device": "R1", "interface": "G0/1", "address": "10.0.12.1/30", "gateway": "—"}, {"device": "R2", "interface": "G0/1", "address": "10.0.12.2/30", "gateway": "—"}, {"device": "R2", "interface": "G0/0", "address": "192.168.60.1/24", "gateway": "—"}, {"device": "SW1", "interface": "VLAN 1", "address": "192.168.50.2/24", "gateway": "192.168.50.1"}, {"device": "SRV-RADIUS", "interface": "NIC", "address": "192.168.50.100/24", "gateway": "192.168.50.1"}, {"device": "PC-ADMIN", "interface": "NIC", "address": "192.168.50.10/24", "gateway": "192.168.50.1"}, {"device": "PC-REMOTO", "interface": "NIC", "address": "192.168.60.10/24", "gateway": "192.168.60.1"}], "generated_devices": ["PC-ADMIN", "PC-REMOTO", "R1", "R2", "SRV-RADIUS", "SW1"], "generation_limitations": []}, "configs": {"R1": "enable\\nconfigure terminal\\nhostname R1\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\ninterface GigabitEthernet0/0\\n ip address 192.168.50.1 255.255.255.0\\n no shutdown\\nexit\\ninterface GigabitEthernet0/1\\n ip address 10.0.12.1 255.255.255.252\\n no shutdown\\nexit\\nip route 192.168.60.0 255.255.255.0 10.0.12.2\\nip domain-name urp.lab\\ncrypto key generate rsa\\n1024\\nip ssh version 2\\nusername localadmin secret Local2026\\naaa new-model\\nradius-server host 192.168.50.100 key RadiusURP2026\\naaa authentication login default group radius local\\nline console 0\\n login authentication default\\nexit\\nline vty 0 4\\n login authentication default\\n transport input ssh\\nexit\\nend\\ncopy running-config startup-config\\n", "R2": "enable\\nconfigure terminal\\nhostname R2\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\ninterface GigabitEthernet0/0\\n ip address 192.168.60.1 255.255.255.0\\n no shutdown\\nexit\\ninterface GigabitEthernet0/1\\n ip address 10.0.12.2 255.255.255.252\\n no shutdown\\nexit\\nip route 192.168.50.0 255.255.255.0 10.0.12.1\\nip domain-name urp.lab\\ncrypto key generate rsa\\n1024\\nip ssh version 2\\nusername localadmin secret Local2026\\naaa new-model\\nradius-server host 192.168.50.100 key RadiusURP2026\\naaa authentication login default group radius local\\nline console 0\\n login authentication default\\nexit\\nline vty 0 4\\n login authentication default\\n transport input ssh\\nexit\\nend\\ncopy running-config startup-config\\n", "SW1": "enable\\nconfigure terminal\\nhostname SW1\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\ninterface FastEthernet0/1\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/2\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/24\\n switchport mode access\\n no shutdown\\nexit\\ninterface Vlan1\\n ip address 192.168.50.2 255.255.255.0\\n no shutdown\\nexit\\nip default-gateway 192.168.50.1\\nusername localadmin secret Local2026\\naaa new-model\\nradius-server host 192.168.50.100 key RadiusURP2026\\naaa authentication login default group radius local\\nline console 0\\n login authentication default\\nexit\\nline vty 0 15\\n login authentication default\\n transport input telnet\\nexit\\nend\\ncopy running-config startup-config\\n"}, "html": ""}, {"spec": {"exercise": 10, "student": {"name": "Andre Torres", "code": "202210073"}, "target_packet_tracer": "9.0.1.0858", "pkt_created": true, "simulation_verified": false, "devices": [{"name": "PC-AQP", "model": "PC-PT"}, {"name": "PC-NOC", "model": "PC-PT"}, {"name": "R-AREQ", "model": "2911 + HWIC-2T"}, {"name": "R-LIMA", "model": "2911 + HWIC-2T"}, {"name": "SRV-TACACS", "model": "Server-PT"}, {"name": "SW-AREQ", "model": "2960"}, {"name": "SW-LIMA", "model": "2960"}], "links": [{"device_a": "R-LIMA", "port_a": "S0/0/0", "device_b": "R-AREQ", "port_b": "S0/0/0", "cable": "serial DCE en R-LIMA", "source": "figura 10"}, {"device_a": "R-LIMA", "port_a": "G0/0", "device_b": "SW-LIMA", "port_b": "F0/24", "cable": "directo", "source": "figura 10"}, {"device_a": "SW-LIMA", "port_a": "F0/1", "device_b": "SRV-TACACS", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 10"}, {"device_a": "SW-LIMA", "port_a": "F0/2", "device_b": "PC-NOC", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 10"}, {"device_a": "R-AREQ", "port_a": "G0/0", "device_b": "SW-AREQ", "port_b": "F0/24", "cable": "directo", "source": "figura 10"}, {"device_a": "SW-AREQ", "port_a": "F0/2", "device_b": "PC-AQP", "port_b": "FastEthernet0", "cable": "directo", "source": "figura 10"}], "addressing": [{"device": "R-LIMA", "interface": "G0/0", "address": "10.10.10.1/24", "gateway": "—"}, {"device": "R-LIMA", "interface": "S0/0/0 DCE", "address": "172.30.0.1/30", "gateway": "—"}, {"device": "R-AREQ", "interface": "S0/0/0", "address": "172.30.0.2/30", "gateway": "—"}, {"device": "R-AREQ", "interface": "G0/0", "address": "10.20.20.1/24", "gateway": "—"}, {"device": "SW-AREQ", "interface": "VLAN 1", "address": "10.20.20.2/24", "gateway": "10.20.20.1"}, {"device": "SRV-TACACS", "interface": "NIC", "address": "10.10.10.100/24", "gateway": "10.10.10.1"}, {"device": "PC-NOC", "interface": "NIC", "address": "10.10.10.20/24", "gateway": "10.10.10.1"}, {"device": "PC-AQP", "interface": "NIC", "address": "10.20.20.20/24", "gateway": "10.20.20.1"}], "generated_devices": ["PC-AQP", "PC-NOC", "R-AREQ", "R-LIMA", "SRV-TACACS", "SW-AREQ", "SW-LIMA"], "generation_limitations": []}, "configs": {"R-AREQ": "enable\\nconfigure terminal\\nhostname R-AREQ\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\ninterface GigabitEthernet0/0\\n ip address 10.20.20.1 255.255.255.0\\n no shutdown\\nexit\\ninterface Serial0/0/0\\n ip address 172.30.0.2 255.255.255.252\\n no shutdown\\nexit\\nrouter ospf 1\\n network 10.20.20.0 0.0.0.255 area 0\\n network 172.30.0.0 0.0.0.3 area 0\\nexit\\nip domain-name urp.lab\\ncrypto key generate rsa\\n1024\\nip ssh version 2\\nusername localadmin secret Local2026\\naaa new-model\\ntacacs-server host 10.10.10.100 key TacacsURP2026\\naaa authentication login CONSOLA group tacacs+ local\\naaa authentication login REMOTO group tacacs+ local\\nline console 0\\n login authentication CONSOLA\\nexit\\nline vty 0 4\\n login authentication REMOTO\\n transport input ssh\\nexit\\nend\\ncopy running-config startup-config\\n", "R-LIMA": "enable\\nconfigure terminal\\nhostname R-LIMA\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\ninterface GigabitEthernet0/0\\n ip address 10.10.10.1 255.255.255.0\\n no shutdown\\nexit\\ninterface Serial0/0/0\\n ip address 172.30.0.1 255.255.255.252\\n clock rate 64000\\n no shutdown\\nexit\\nrouter ospf 1\\n network 10.10.10.0 0.0.0.255 area 0\\n network 172.30.0.0 0.0.0.3 area 0\\nexit\\nip domain-name urp.lab\\ncrypto key generate rsa\\n1024\\nip ssh version 2\\nusername localadmin secret Local2026\\naaa new-model\\ntacacs-server host 10.10.10.100 key TacacsURP2026\\naaa authentication login CONSOLA group tacacs+ local\\naaa authentication login REMOTO group tacacs+ local\\nline console 0\\n login authentication CONSOLA\\nexit\\nline vty 0 4\\n login authentication REMOTO\\n transport input ssh\\nexit\\nend\\ncopy running-config startup-config\\n", "SW-AREQ": "enable\\nconfigure terminal\\nhostname SW-AREQ\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\ninterface FastEthernet0/2\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/24\\n switchport mode access\\n no shutdown\\nexit\\ninterface Vlan1\\n ip address 10.20.20.2 255.255.255.0\\n no shutdown\\nexit\\nip default-gateway 10.20.20.1\\nusername localadmin secret Local2026\\naaa new-model\\ntacacs-server host 10.10.10.100 key TacacsURP2026\\naaa authentication login CONSOLA group tacacs+ local\\naaa authentication login REMOTO group tacacs+ local\\nline console 0\\n login authentication CONSOLA\\nexit\\nline vty 0 15\\n login authentication REMOTO\\n transport input telnet\\nexit\\nend\\ncopy running-config startup-config\\n", "SW-LIMA": "enable\\nconfigure terminal\\nhostname SW-LIMA\\nno ip domain-lookup\\nenable secret class\\nservice password-encryption\\nbanner motd #Laboratorio URP - Andre Torres - 202210073#\\nline console 0\\n password cisco\\n login\\nexit\\ninterface FastEthernet0/1\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/2\\n switchport mode access\\n no shutdown\\nexit\\ninterface FastEthernet0/24\\n switchport mode access\\n no shutdown\\nexit\\nend\\ncopy running-config startup-config\\n"}, "html": ""}]')
POSITIONS={
7:{'R1':(450,130),'SW-ADM':(230,300),'SW-ACA':(670,300),'PC-A1':(140,460),'PC-A2':(320,460),'PC-B1':(590,460)},
8:{'R-DHCP':(220,120),'R-SEDE':(650,120),'SW-CEN':(220,300),'SRV-DNS':(220,470),'SW-SEDE':(650,300),'PC-V10':(470,490),'PC-V20':(650,490),'PC-V30':(830,490)},
9:{'R1':(420,130),'R2':(760,130),'SW1':(420,330),'SRV-RADIUS':(220,510),'PC-ADMIN':(470,510),'PC-REMOTO':(760,330)},
10:{'R-LIMA':(260,140),'R-AREQ':(720,140),'SW-LIMA':(260,330),'SW-AREQ':(720,330),'SRV-TACACS':(150,510),'PC-NOC':(370,510),'PC-AQP':(720,510)}}

def set_text(parent,tag,value):
    el=parent.find(tag)
    if el is None:el=ET.SubElement(parent,tag)
    el.text=str(value)

def full_port(p):
    if p.startswith('G0/'):return p.replace('G0/','GigabitEthernet0/')
    if p.startswith('F0/'):return p.replace('F0/','FastEthernet0/')
    if p.startswith('S0/'):return p.replace('S0/','Serial0/')
    return p

def ios_lines(text):
    # RUNNINGCONFIG contiene configuración, no un diálogo interactivo de CLI.
    lines=text.splitlines()
    return [s for s in lines if s.strip() not in {'enable','configure terminal','copy running-config startup-config','crypto key generate rsa','1024'}]

def configure_server(eng,n,html):
    # Todos estos campos están presentes en la plantilla distribuida.
    # El DHCP heredado de la plantilla se desactiva: el servidor DHCP es router.
    for e in eng.findall('.//DHCP_SERVER/ENABLED'):e.text='0'
    acs=eng.find('ACS_SERVER')
    if n==8:
        set_text(acs,'ENABLED','0')
        for manager in eng.findall('FILE_MANAGER'):
            for f in manager.findall('.//FILE'):
                if f.findtext('NAME')=='index.html':
                    text=f.find('FILE_CONTENT/TEXT')
                    if text is not None:text.text=html
        # Estructura de registro DNS no documentada por la API: completar en GUI.
        return
    set_text(acs,'ENABLED','0' if n==10 else '1')
    users=acs.find('USERS');users.clear()
    pairs=[('admin','Admin2026'),('soporte','Soporte2026')] if n==9 else [('netadmin','Net2026'),('auditor','Audit2026')]
    for name,password in pairs:
        user=ET.SubElement(users,'USER')
        for tag,val in [('NAME',name),('PASSWORD',password),('DESCRIPTION','')]:set_text(user,tag,val)
    clients=acs.find('ACS_CLIENTS');clients.clear()
    if n==9:
        for name,ip in [('R1','192.168.50.1'),('R2','10.0.12.2'),('SW1','192.168.50.2')]:
            client=ET.SubElement(clients,'CLIENT')
            for tag,val in [('HOST_IP',ip),('KEY','RadiusURP2026'),('DESCRIPTION',name),('SERVER_TYPE','RADIUS')]:set_text(client,tag,val)
    # TACACS: no inventar el enum interno. Usuarios ya colocados; registrar
    # clientes tipo Tacacs y activar servicio desde GUI antes de probar AAA.

def basic(name):
    return (f'hostname {name}\nno ip domain-lookup\nenable secret class\nservice password-encryption\n'
            'banner motd #Laboratorio URP - Andre Torres - 202210073#\n'
            'line console 0\n password cisco\n login\nexit\n')


def vlans(pairs):
    return ''.join(f'vlan {v}\n name {name}\nexit\n' for v,name in pairs)


def interface(port, body):
    return f'interface {full_port(port)}\n{body}exit\n'


def svi(v,ip):
    return interface(f'Vlan{v}',f' ip address {ip} 255.255.255.0\n no shutdown\n')


def access_port(port,v=1,guard=False):
    return interface(port,f' switchport mode access\n switchport access vlan {v}\n'+
                     (' spanning-tree portfast\n spanning-tree bpduguard enable\n' if guard else '')+' no shutdown\n')


def trunk(port,multilayer=False):
    return interface(port,(' switchport trunk encapsulation dot1q\n' if multilayer else '')+
                     ' switchport mode trunk\n switchport trunk native vlan 99\n switchport trunk allowed vlan 10,20,99\n no shutdown\n')


def channel(ports,num,mode,multilayer=False):
    text=''
    for port in ports:
        text+=interface(port,' shutdown\n'+(' switchport trunk encapsulation dot1q\n' if multilayer else '')+
                        ' switchport mode trunk\n switchport trunk native vlan 99\n switchport trunk allowed vlan 10,20,99\n'+f' channel-group {num} mode {mode}\n')
    text+=trunk(f'Port-channel{num}',multilayer)
    for port in ports:text+=interface(port,' no shutdown\n')
    return text


def ip_port(port,ip,mask='255.255.255.0',routed=False):
    return interface(port,(' no switchport\n' if routed else '')+f' ip address {ip} {mask}\n no shutdown\n')


def ospf(networks):
    return 'router ospf 1\n'+''.join(f' network {ip} {wildcard} area 0\n' for ip,wildcard in networks)+'exit\n'


def hsrp(v,priority):
    return f' standby version 2\n standby {v} ip 192.168.{v}.1\n standby {v} priority {priority}\n standby {v} preempt\n'


def early_labs():
    """Figuras 1–6 y tablas del PDF original, páginas 3–14."""
    items=[]
    def new(n):
        return {'spec':{'exercise':n,'student':{'name':'Andre Torres','code':'202210073'},
                        'devices':[],'links':[],'addressing':[]},'configs':{},'html':''}
    def device(item,name,model,x,y,body=None,ip=None,gw='0.0.0.0'):
        item['spec']['devices'].append({'name':name,'model':model})
        POSITIONS.setdefault(item['spec']['exercise'],{})[name]=(x,y)
        if body is not None:item['configs'][name]=basic(name)+body+'end\n'
        if ip:item['spec']['addressing'].append({'device':name,'interface':'NIC','address':ip,'gateway':gw})
    def link(item,a,ap,b,bp,cross=False):
        item['spec']['links'].append({'device_a':a,'port_a':ap,'device_b':b,'port_b':bp,'cable':'cruzado' if cross else 'directo','source':f"figura {item['spec']['exercise']}"})
    # 01: estado final con raíz/guardas; los estados previos se reconstruyen en pruebas.
    i=new(1)
    device(i,'S1','2960',450,150,svi(1,'192.168.1.1')+'spanning-tree mode pvst\nspanning-tree vlan 1 priority 4096\n'+access_port('F0/1')+access_port('F0/2'))
    for name,last,x in [('S2',2,220),('S3',3,680)]:
        body=svi(1,f'192.168.1.{last}')+'spanning-tree mode pvst\n'+('spanning-tree vlan 1 priority 8192\n' if name=='S2' else '')
        body+=''.join(access_port(p,guard=p in ['F0/11','F0/12']) for p in ['F0/1','F0/2','F0/11','F0/12'])
        device(i,name,'2960',x,340,body)
    link(i,'S1','F0/1','S2','F0/1',True);link(i,'S1','F0/2','S3','F0/1',True);link(i,'S2','F0/2','S3','F0/2',True)
    for idx,sw,port,x in [(1,'S2',11,130),(2,'S2',12,310),(3,'S3',11,590),(4,'S3',12,770)]:
        device(i,f'PC{idx}','PC-PT',x,530,ip=f'192.168.1.{10+idx}/24');link(i,sw,f'F0/{port}',f'PC{idx}','FastEthernet0')
    items.append(i)
    # 02: Rapid PVST+ final, native/management VLAN99; no routing requested.
    i=new(2);vs=[(10,'VENTAS'),(20,'SOPORTE'),(99,'GESTION')]
    for idx,(name,x,y) in enumerate([('DS1',240,150),('DS2',720,150),('AS1',240,400),('AS2',720,400)],1):
        body=vlans(vs)+svi(99,f'192.168.99.{idx}')+'spanning-tree mode rapid-pvst\n'
        if name.startswith('DS'):
            body+=''.join(trunk(p) for p in ['G0/1','F0/1','F0/2'])
            body+=''.join(interface(p,' spanning-tree guard root\n') for p in ['F0/1','F0/2'])
            body+=('spanning-tree vlan 10,99 priority 4096\nspanning-tree vlan 20 priority 8192\n' if name=='DS1' else
                   'spanning-tree vlan 20 priority 4096\nspanning-tree vlan 10,99 priority 8192\n')
        else:body+=trunk('F0/1')+trunk('F0/2')+access_port('F0/11',10,True)+access_port('F0/21',20,True)
        device(i,name,'2960',x,y,body)
    for a,ap,b,bp in [('DS1','G0/1','DS2','G0/1'),('DS1','F0/1','AS1','F0/1'),('DS1','F0/2','AS2','F0/1'),('DS2','F0/2','AS1','F0/2'),('DS2','F0/1','AS2','F0/2')]:link(i,a,ap,b,bp,True)
    for name,sw,v,last,x in [('PC-V10A','AS1',10,11,150),('PC-V20A','AS1',20,11,330),('PC-V10B','AS2',10,12,630),('PC-V20B','AS2',20,12,810)]:
        device(i,name,'PC-PT',x,600,ip=f'192.168.{v}.{last}/24');link(i,sw,'F0/11' if v==10 else 'F0/21',name,'FastEthernet0')
    items.append(i)
    # 03: trois liens physiques, Po1 LACP active/passive.
    i=new(3);vs=[(10,'DOCENTES'),(20,'ALUMNOS'),(99,'GESTION')]
    for name,last,x,mode in [('SW-A',1,250,'active'),('SW-B',2,720,'passive')]:
        body=vlans(vs)+svi(99,f'192.168.99.{last}')+channel(['F0/1','F0/2','F0/3'],1,mode)
        body+=access_port('F0/11',10)+access_port('F0/21',20)+'port-channel load-balance src-dst-mac\n'
        device(i,name,'2960',x,220,body)
    for port in [1,2,3]:link(i,'SW-A',f'F0/{port}','SW-B',f'F0/{port}',True)
    for name,sw,v,last,x in [('PC-A10','SW-A',10,11,150),('PC-A20','SW-A',20,11,350),('PC-B10','SW-B',10,12,620),('PC-B20','SW-B',20,12,820)]:
        device(i,name,'PC-PT',x,450,ip=f'192.168.{v}.{last}/24');link(i,sw,'F0/11' if v==10 else 'F0/21',name,'FastEthernet0')
    items.append(i)
    # 04: 3560 core + LACP, PAgP and static bundles.
    i=new(4);vs=[(10,'DOCENTES'),(20,'ALUMNOS'),(99,'GESTION')]
    body=vlans(vs)+'ip routing\n'+''.join(svi(v,f'192.168.{v}.1') for v in [10,20,99])
    body+=channel(['G0/1','G0/2'],1,'active',True)+channel(['F0/1','F0/2'],2,'desirable',True)
    body+='spanning-tree vlan 10,20,99 priority 4096\nport-channel load-balance src-dst-ip\n'
    device(i,'MLS1','3560-24PS',470,140,body)
    body=vlans(vs)+svi(99,'192.168.99.11')+'ip default-gateway 192.168.99.1\n'
    body+=channel(['G0/1','G0/2'],1,'active')+channel(['F0/1','F0/2'],3,'on')+access_port('F0/11',10)
    device(i,'S1','2960',210,390,body)
    body=vlans(vs)+svi(99,'192.168.99.12')+'ip default-gateway 192.168.99.1\n'
    body+=channel(['F0/1','F0/2'],2,'auto')+channel(['F0/3','F0/4'],3,'on')+access_port('F0/11',20)
    device(i,'S2','2960',730,390,body)
    for j in [1,2]:
        link(i,'MLS1',f'G0/{j}','S1',f'G0/{j}',True);link(i,'MLS1',f'F0/{j}','S2',f'F0/{j}',True);link(i,'S1',f'F0/{j}','S2',f'F0/{j+2}',True)
    for idx,sw,v,x in [(1,'S1',10,210),(2,'S2',20,730)]:
        device(i,f'PC{idx}','PC-PT',x,600,ip=f'192.168.{v}.10/24',gw=f'192.168.{v}.1');link(i,sw,'F0/11',f'PC{idx}','FastEthernet0')
    items.append(i)
    # 05: ISP Lo0 is a simulated destination, not actual internet access.
    i=new(5)
    body=ip_port('G0/0','10.0.1.1','255.255.255.252')+ip_port('G0/1','10.0.2.1','255.255.255.252')+ip_port('Loopback0','8.8.8.8','255.255.255.255')
    body+=ospf([('10.0.1.0','0.0.0.3'),('10.0.2.0','0.0.0.3'),('8.8.8.8','0.0.0.0')]);device(i,'ISP','1941',470,120,body)
    for idx,x in [(1,230),(2,710)]:
        body=ip_port('G0/1',f'10.0.{idx}.2','255.255.255.252')+ip_port('G0/0',f'192.168.10.{idx+1}')
        body+=interface('G0/0',hsrp(10,150 if idx==1 else 100))
        body+=ospf([(f'10.0.{idx}.0','0.0.0.3'),('192.168.10.0','0.0.0.255')]);device(i,f'R{idx}','1941',x,300,body)
        link(i,'ISP',f'G0/{idx-1}',f'R{idx}','G0/1',True)
    device(i,'SW1','2960',470,470,''.join(access_port(p) for p in ['F0/1','F0/2','F0/11','F0/12']))
    for idx in [1,2]:link(i,f'R{idx}','G0/0','SW1',f'F0/{idx}')
    for idx,x in [(1,330),(2,610)]:
        device(i,f'PC{idx}','PC-PT',x,650,ip=f'192.168.10.{20+idx}/24',gw='192.168.10.1');link(i,'SW1',f'F0/{10+idx}',f'PC{idx}','FastEthernet0')
    items.append(i)
    # 06: gateway per VLAN, tracking of routed WAN uplink.
    i=new(6);vs=[(10,'ALUMNOS'),(20,'DOCENTES'),(99,'GESTION')]
    body=ip_port('G0/0','10.1.1.1','255.255.255.252')+ip_port('G0/1','10.1.2.1','255.255.255.252')+ip_port('Loopback0','200.10.10.1','255.255.255.255')
    body+=ospf([('10.1.1.0','0.0.0.3'),('10.1.2.0','0.0.0.3'),('200.10.10.1','0.0.0.0')]);device(i,'R-WAN','2911',480,120,body)
    for idx,x in [(1,210),(2,750)]:
        body=vlans(vs)+'ip routing\n'+ip_port('G0/1',f'10.1.{idx}.2','255.255.255.252',True)
        for v in [10,20,99]:
            priority=150 if (idx==1 and v in [10,99]) or (idx==2 and v==20) else 100
            body+=svi(v,f'192.168.{v}.{idx+1}')+interface(f'Vlan{v}',hsrp(v,priority))
        # IOS clásico: compatibilidad real a verificar, no sustitución de protocolo.
        body+=interface(f'Vlan{10 if idx==1 else 20}',f' standby {10 if idx==1 else 20} track GigabitEthernet0/1 60\n')
        body+=channel(['F0/23','F0/24'],1,'active',True)+trunk('F0/1',True)+trunk('F0/2',True)
        body+=('spanning-tree vlan 10,99 priority 4096\nspanning-tree vlan 20 priority 8192\n' if idx==1 else 'spanning-tree vlan 20 priority 4096\nspanning-tree vlan 10,99 priority 8192\n')
        body+=ospf([(f'10.1.{idx}.0','0.0.0.3')]+[(f'192.168.{v}.0','0.0.0.255') for v in [10,20,99]])
        device(i,f'DSW{idx}','3560-24PS',x,340,body);link(i,'R-WAN',f'G0/{idx-1}',f'DSW{idx}','G0/1')
    for port in [23,24]:link(i,'DSW1',f'F0/{port}','DSW2',f'F0/{port}',True)
    for idx,x in [(1,210),(2,750)]:
        body=vlans(vs)+svi(99,f'192.168.99.{10+idx}')+'ip default-gateway 192.168.99.1\n'+trunk('G0/1')+trunk('G0/2')+access_port('F0/11',10 if idx==1 else 20)
        device(i,f'ASW{idx}','2960',x,570,body)
    for a,ap,b,bp in [('DSW1','F0/1','ASW1','G0/1'),('DSW1','F0/2','ASW2','G0/2'),('DSW2','F0/1','ASW2','G0/1'),('DSW2','F0/2','ASW1','G0/2')]:link(i,a,ap,b,bp,True)
    for name,sw,v,x in [('PC10','ASW1',10,210),('PC20','ASW2',20,750)]:
        device(i,name,'PC-PT',x,760,ip=f'192.168.{v}.10/24',gw=f'192.168.{v}.1');link(i,sw,'F0/11',name,'FastEthernet0')
    items.append(i)
    return items


DATA=early_labs()+DATA


def annotate(lab,spec,ids):
    # Campos existentes en network_seed.xml: etiquetas nativas y perfil.
    options=lab.base.find('OPTIONS')
    for tag,value in [('PORTSHOWN','true'),('HIDEDEVICELABEL','false'),('MODELSHOWN','true')]:
        set_text(options,tag,value)
    profile=lab.base.find('USER_PROFILE')
    set_text(profile,'NAME',args.student_name)
    set_text(profile,'ADDITIONAL_INFO',f'Codigo {args.student_code} - Ejercicio {spec["exercise"]:02d}')
    set_text(lab.net,'DESCRIPTION',f'Laboratorio 02 - E{spec["exercise"]:02d} - {args.student_name} - {args.student_code} | Generado offline; pruebas en Cisco pendientes.')
    # No conservar los historiales de comandos ajenos heredados del seed.
    logs=lab.base.find('COMMAND_LOGS')
    if logs is not None:logs.clear()
    for el in lab.devs.findall('DEVICE'):
        eng=el.find('ENGINE');name=eng.findtext('NAME')
        host=next((a for a in spec['addressing'] if a['device']==name),None)
        detail=f'{name} - {args.student_name} - {args.student_code}'
        if host:detail+=' | '+host['address']+' | gateway '+host['gateway']
        set_text(eng,'DESCRIPTION',detail)
        if name not in item['configs']:continue
        rc=eng.find('RUNNINGCONFIG')
        # Descripciones IOS, visibles en show interfaces / running-config.
        # Los textos libres Place Note no se inventan: formato aún no verificado.
        extras=[]
        for link in spec['links']:
            if link['device_a']==name:
                local,remote,rport=link['port_a'],link['device_b'],link['port_b']
            elif link['device_b']==name:
                local,remote,rport=link['port_b'],link['device_a'],link['port_a']
            else:continue
            if remote in ids:extras.extend([f'interface {full_port(local)}',f' description Hacia {remote} {rport}','exit'])
        index=len(rc)
        if index and (rc[-1].text or '').strip()=='end':index-=1
        for off,line in enumerate(extras):
            eline=ET.Element('LINE');eline.text=line;rc.insert(index+off,eline)


for item in DATA:
    # Personalizar las cadenas antes de construir la topología.
    def personalized(value):
        if isinstance(value,str):return value.replace('Andre Torres',args.student_name).replace('202210073',args.student_code)
        if isinstance(value,list):return [personalized(v) for v in value]
        if isinstance(value,dict):return {k:personalized(v) for k,v in value.items()}
        return value
    item=personalized(item)
    spec=item['spec'];n=spec['exercise'];lab=Lab();ids={};missing=[]
    used_ports=set()
    for edge in spec['links']:
        for side in ['a','b']:
            endpoint=(edge['device_'+side],full_port(edge['port_'+side]))
            assert endpoint not in used_ports, f'Puerto repetido: {endpoint}'
            used_ports.add(endpoint)
    for d in spec['devices']:
        name=d['name'];model=d['model'].split(' + ')[0]
        if model=='2960':model='2960-24TT'
        if model not in lab.models:
            missing.append(f'{name}: modelo {model} no incluido en las plantillas; añadir manualmente con sus dos parámetros IP y gateway y conectar IMP-B a SW-ACA F0/3; IP 172.16.20.5/24, gateway 172.16.20.1.')
            continue
        kw={}
        conf=item['configs'].get(name)
        if conf:kw['ios_config']=ios_lines(conf)
        if n==10 and name.startswith('R-'):kw['install']='HWIC-2T'
        host=next((a for a in spec['addressing'] if a['device']==name and a['interface']=='NIC'),None)
        if host and '/' in host['address']:
            import ipaddress
            ip=ipaddress.ip_interface(host['address']);kw['pc_ip']=(str(ip.ip),str(ip.netmask),host['gateway'])
        x,y=POSITIONS[n][name]
        ids[name]=lab.add_device(model,name,x=x,y=y,**kw)
        el=next(e for e in lab.devs.findall('DEVICE') if e.findtext('ENGINE/NAME')==name);eng=el.find('ENGINE')
        if host:
            port=el.find('.//PORT')
            if host['address'].startswith('DHCP'):
                for tag,val in [('IP','0.0.0.0'),('SUBNET','0.0.0.0'),('PORT_GATEWAY','0.0.0.0'),('PORT_DNS','0.0.0.0'),('PORT_DHCP_ENABLE','true')]:set_text(port,tag,val)
            else:set_text(eng,'GATEWAY',host['gateway'])
        if name.startswith('SRV-'):configure_server(eng,n,item['html'])
    for link in spec['links']:
        a,b=link['device_a'],link['device_b']
        if a not in ids or b not in ids:continue
        kwargs={'kind':'serial','dce':ids['R-LIMA'],'clock':64000} if link['cable'].startswith('serial') else {}
        lab.link(ids[a],full_port(link['port_a']),ids[b],full_port(link['port_b']),**kwargs)
        if link['cable']=='cruzado':
            # Mismo campo TYPE del cable; variante eCrossOver del formato PT.
            lab.net.find('LINKS').findall('LINK')[-1].find('CABLE/TYPE').text='eCrossOver'
    annotate(lab,spec,ids)
    path=args.output_dir/f'LAB02_E{n:02d}_{args.file_suffix}.pkt';lab.save(path)
    # Recarga con validación del contenedor por el codec, NO por Packet Tracer.
    loaded=Lab(seed=path,auto_prune_seed=False)
    assert loaded.device_count==len(ids)
    assert loaded.link_count==sum(l['device_a'] in ids and l['device_b'] in ids for l in spec['links'])
    assert set(loaded.device_names())==set(ids)
    assert loaded.to_xml()==lab.to_xml()
    result={'file':path.name,'pkt_core_version':'0.2.0','devices':loaded.device_count,'links':loaded.link_count,'codec_roundtrip':'PASS','packet_tracer_opened':False,'functional_tests':'NO EJECUTADAS','missing_devices':missing}
    print(json.dumps(result,ensure_ascii=False))
