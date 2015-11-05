import json

extraneous_keys = ['position', 'meta', 'sid', 'updated_meta', 'created_meta']
numeric_keys    = ['count', 'percent', 'year']

def to_dict_without(keys_to_ignore, keys, vals):
  proto = {}
  for i, key in enumerate(keys): 
    if not key in keys_to_ignore:
      proto[key] = vals[i]
  return proto

def data_dir(filename):
  return "./data/" + filename

with open( data_dir('nyc-popular-deaths.gov.json') ) as data:
  nyc = json.load(data)

lower_case_cols = [ mixedCaseKey.lower() for mixedCaseKey in [ col['name'] for col in nyc['meta']['view']['columns'] ] ]

print(lower_case_cols)

deaths = [ to_dict_without(extraneous_keys, lower_case_cols, row) for row in nyc['data'] ]

deaths_by_count = sorted( deaths, key=lambda row: row.get('count'), reverse=True )

with open( data_dir('cleaned.json') , 'w') as output:
  output.write( json.dumps( deaths_by_count, indent=2) )
  output.close()
