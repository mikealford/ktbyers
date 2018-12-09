#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import jinja2


crypto_vars = {
    'encr': 'aes',
    'dh': '5',
    'isakmp': True
}

crypto_template = '''
crypto isakmp policy 10
 encr {{ encr }}
 authentication pre-share
 group {{ dh }}
{% if isakmp -%}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}
'''

template = jinja2.Template(crypto_template)
print(template.render(crypto_vars))

