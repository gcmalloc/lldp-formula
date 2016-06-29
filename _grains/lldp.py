#!/usr/bin/env python
import json
import subprocess

import logging 

log = logging.getLogger(__name__)

def _lldp_neighbors():
    try:
        neighbors = subprocess.check_output(['lldpctl', '-f', 'json'])
    except subprocess.CalledProcessError as e:
        log.warn('issue executing lldpctl')
        log.warn(e)
        return None
    neighbors_dict = json.loads(neighbors)
    return neighbors_dict


def main():
    # initialize a grains dictionary
    grains = {}
    neighbors = _lldp_neighbors()
    if neighbors:
        grains['lldp_neighbors'] = neighbors
    return grains
