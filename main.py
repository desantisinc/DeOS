#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configobj
import simplejson as json
import jsonschema
import web
import ruamel.yaml as yaml

config = configobj.ConfigObj('deos.ini')

def main():
    with open('.deos.yml') as f:
        raw_data = f.read()
    if isinstance(raw_data, basestring):
        data = yaml.safe_load(raw_data)
    with open('.deos-schema.yml') as f:
        raw_schema = f.read()
    if isinstance(raw_schema, basestring):
        schema = yaml.safe_load(raw_schema)
    if isinstance(data, dict) and isinstance(schema, dict):
        jsonschema.validate(data, schema)
        print json.dumps(data, sort_keys=True, indent=2)

if __name__ == "__main__":
    main()
