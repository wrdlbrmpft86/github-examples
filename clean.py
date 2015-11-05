import json

extraneous_keys = ['position', 'meta', 'sid', 'updated_meta', 'created_meta']

def to_dict_without(keys_to_ignore, keys, vals):
  proto = {}
  for i, key in enumerate(keys): 
    if not key in keys_to_ignore: proto[key] = vals[i]
  return proto


with open('./new-york-most-popular-ways-to-die.json') as data:
  nyc = json.load(data)

lower_case_cols = [ mixedCaseKey.lower() for mixedCaseKey in [ col['name'] for col in nyc['meta']['view']['columns'] ] ]

deaths = [ to_dict_without(extraneous_keys, lower_case_cols, row) for row in nyc['data'] ]

deaths_by_count = sorted( deaths, key=lambda row: row.get('count'), reverse=True )

with open('nyc-deaths-by-count.json', 'w') as output:
  output.write( json.dumps( deaths_by_count, indent=2) )
  output.close()
