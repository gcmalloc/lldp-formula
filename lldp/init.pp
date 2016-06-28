# -*- coding: utf-8 -*-
# vim: ft=sls

{## import settings from map.jinja ##}
{% from "lldp/map.jinja" import lldp_settings with context %}

lldp-pkg:
  pkg.installed:
    - name: {{ lldp_settings.pkg }}
    - failhard: True

lldp-service:
  service.running:
    enable: {{ lldp_settings.service.enable }}
    name: {{ lldp_settings.service.name }}
    - require:
      - pkg {{ lldp_settings.pkg }}
