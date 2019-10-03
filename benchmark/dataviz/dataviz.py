import os
import sys
import json

EXAMPLE = 'hello-world/gcp/g1-small'
DIR = os.getcwd()

PATH_IN = os.path.join(DIR, f"../results/{EXAMPLE}")

# data
BECNHMARK_PAR = {
    "duration": 10,
    "threads": 1,
    "connections": 1,
}
FILE_SUFFIX = '_'.join([f"{k[0].lower()}{v}" for k, v in BECNHMARK_PAR.items()])
if len(FILE_SUFFIX) > 0:
    FILE_IN = f"data_{FILE_SUFFIX}.json"
else:
    FILE_IN = "data.json"
PATH_IN += f"/{FILE_IN}"

PATH_OUT = os.path.join(DIR, EXAMPLE, FILE_SUFFIX)

# templates
TEMPLATE_HTML = os.path.join(DIR, "template.html")
TEMPLATE_JS = os.path.join(DIR, "template.js")
JS_NAME_OUT = 'graph.js'

# sanity check
assert os.path.isfile(PATH_IN), \
    f"Data file cannot be found in {PATH_IN}"
assert os.path.isfile(TEMPLATE_HTML), \
  f"HTML template doesn't exist in {TEMPLATE_HTML}"
assert os.path.isfile(TEMPLATE_JS), \
    f"JS template doesn't exist in {TEMPLATE_JS}"

if __name__ == "__main__":
    try:
      data = json.load(open(PATH_IN, 'r'))    
    except Exception as ex:
      print(ex)
      sys.exit(1)
    
    # adjust js  
    js_template = f"""var connections = {BECNHMARK_PAR['connections']};
var threads = {BECNHMARK_PAR['threads']};
var duration = {BECNHMARK_PAR['duration']};
var data = {json.dumps(data)}
    """
  
    js_file = open(TEMPLATE_JS, 'r').read()
    js_file = f"{js_template}\n{js_file}"
    
    # save js into a new dir
    if not os.path.isdir(PATH_OUT):
      os.makedirs(PATH_OUT)
    
    with open(os.path.join(PATH_OUT, JS_NAME_OUT), 'w') as f:
      f.write(js_file)
    
    os.system(f"cp {TEMPLATE_HTML} {os.path.join(PATH_OUT, 'index.html')}")
