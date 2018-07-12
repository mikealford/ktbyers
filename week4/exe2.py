houston_dc = ['192.168.5.1','192.168.5.2','192.168.5.3','192.168.5.4','192.168.5.5','192.168.5.6','192.168.5.6','192.168.5.7','192.168.5.8','192.168.5.9','192.168.5.10','192.168.5.11','192.168.5.1', '192.168.5.5','192.168.5.6','192.168.5.15']

atlanta_dc = ['10.0.0.1','10.0.0.2','10.0.0.3','10.0.0.4','10.0.0.5','10.0.0.6','10.0.0.7','10.0.0.8','192.168.5.1','192.168.5.6']

chicago_dc = ['172.16.0.1', '172.16.0.2','172.16.0.3','172.16.0.4','172.16.0.5','172.16.0.6','192.168.5.6','10.0.0.2','10.0.0.4']

houston_dc = set(houston_dc)
atlanta_dc = set(atlanta_dc)
chicago_dc = set(chicago_dc)

houston_and_atanta = houston_dc & atlanta_dc
print(houston_and_atanta)
in_all_sites = houston_dc & atlanta_dc & chicago_dc
print(in_all_sites)
just_chicago = chicago_dc.difference(houston_dc).difference(atlanta_dc)
print(just_chicago)

