#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals
import jinja2

active_interfaces = ['Vlan1', 'Vlan2']
networks = ['10.10.10.0/24', '10.10.20.0/24', '10.10.30.0/24']

ospf_vars = {
     '​ospf_process_id': 10,
     'ospf_priority': 100,
     'ospf_active_interfaces': active_interfaces,
     'ospf_area0_networks': networks,
}

template_file = 'ospf_template.j2'
with open(template_file) as f:
    ospf_template = f.read()

template = jinja2.Template(ospf_template)
print(template.render(ospf_vars))
