"""Generación offline con API inspeccionada de pkt-core 0.2.0.
No sustituye apertura, ejecución IOS ni validación funcional en Packet Tracer.
"""
from pathlib import Path
import json, xml.etree.ElementTree as ET
from pkt_core import Lab

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'LAB02_E07_E10'
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

def ios_lines(path):
    # RUNNINGCONFIG contiene configuración, no un diálogo interactivo de CLI.
    lines=path.read_text().splitlines()
    return [s for s in lines if s.strip() not in {'enable','configure terminal','copy running-config startup-config','crypto key generate rsa','1024'}]

def configure_server(eng,n,folder):
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
                    if text is not None:text.text=(folder/'configs/index.html').read_text()
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

for folder in sorted(BASE.glob('E*')):
    spec=json.loads((folder/'topologia.json').read_text());n=spec['exercise'];lab=Lab();ids={};missing=[]
    for d in spec['devices']:
        name=d['name'];model=d['model'].split(' + ')[0]
        if model=='2960':model='2960-24TT'
        if model not in lab.models:
            missing.append(f'{name}: modelo {model} no incluido en las plantillas; añadir manualmente con sus dos parámetros IP y gateway y conectar según montaje.md.')
            continue
        kw={}
        conf=folder/'configs'/f'{name}.ios'
        if conf.exists():kw['ios_config']=ios_lines(conf)
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
        if name.startswith('SRV-'):configure_server(eng,n,folder)
    for link in spec['links']:
        a,b=link['device_a'],link['device_b']
        if a not in ids or b not in ids:continue
        kwargs={'kind':'serial','dce':ids['R-LIMA'],'clock':64000} if link['cable'].startswith('serial') else {}
        lab.link(ids[a],full_port(link['port_a']),ids[b],full_port(link['port_b']),**kwargs)
        if link['cable']=='cruzado':
            # Mismo campo TYPE del cable; variante eCrossOver del formato PT.
            lab.net.find('LINKS').findall('LINK')[-1].find('CABLE/TYPE').text='eCrossOver'
    path=folder/f'LAB02_E{n:02d}_TorresAndre.pkt';lab.save(path)
    # Recarga con validación del contenedor por el codec, NO por Packet Tracer.
    loaded=Lab(seed=path,auto_prune_seed=False)
    assert loaded.device_count==len(ids)
    assert loaded.link_count==sum(l['device_a'] in ids and l['device_b'] in ids for l in spec['links'])
    assert set(loaded.device_names())==set(ids)
    assert loaded.to_xml()==lab.to_xml()
    spec.update(pkt_created=True,simulation_verified=False,generated_devices=list(ids),generation_limitations=missing)
    (folder/'topologia.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
    result={'file':path.name,'pkt_core_version':'0.2.0','devices':loaded.device_count,'links':loaded.link_count,'codec_roundtrip':'PASS','packet_tracer_opened':False,'functional_tests':'NO EJECUTADAS','missing_devices':missing}
    (folder/'validacion_generacion.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
