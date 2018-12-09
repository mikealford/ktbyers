#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import jinja2

my_vlans = {
    '501': 'blue501',
    '502': 'blue502',
    '503': 'blue503',
    '504': 'blue504',
    '505': 'blue505',
    '506': 'blue506',
    '507': 'blue507',
    '508': 'blue508',
}
template_var = {
	'vlans': my_vlans
}

vlan_template = '''

{%- for vlan_num, vlan_name in vlans.items() %}
vlan {{ vlan_num }}
  name {{ vlan_name }}
{% endfor %}

'''

template = jinja2.Template(vlan_template)
print(template.render(template_var))

