#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configobj
import jsonschema
import web

import simplejson as json
import ruamel.yaml as yaml

config = configobj.ConfigObj('.deos.ini')
templates = "src/templates/"

def read(fname):
    data = open(templates+fname).read()
    data = data.replace('$','$$')
    data = data.replace('Δ with', '$def with')
    data = data.replace('Δ','$')
    return data

def write(fname, code):
    with open(fname, 'w') as f:
        f.write(code)

def render(fname):
    raw = read(fname)
    code = web.template.Template(raw)
    return code

def build(fname, data):
    code = render(fname)
    return str(code(data)).replace(8*' ','\t'
                         ).replace('$(False)', '$(FALSE)'
                         ).replace('$(True)', '$(TRUE)'
                         )[1:]

def load():
    with open('.deos.yml') as f:
        raw_data = f.read()
    if isinstance(raw_data, basestring):
        data = yaml.safe_load(raw_data)
    with open('config/deos/schema.yml') as f:
        raw_schema = f.read()
    if isinstance(raw_schema, basestring):
        schema = yaml.safe_load(raw_schema)
    if isinstance(data, dict) and isinstance(schema, dict):
        jsonschema.validate(data, schema)
        print json.dumps(data, sort_keys=True, indent=2)
    else:
        return None
    return data

def main():
    data = load()
    code = build('make/deosrc.mk', data['.deosrc'])
    write('.deosrc.tmp.mk', code)

if __name__ == "__main__":
    main()
