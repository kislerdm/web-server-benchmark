import os
import sys
import json
import pickle
from typing import Tuple, List
from statistics import median


FILTER = {
    "duration": 10,
    "threads": 1,
    "connections": 1,
    "latency": {
        "key": "latency_us",
        "values": {
            "key": "percentile",
            "values": ["1e-06", "25", "50", "50", "75", "100"],
        }
    },
    "req_throughput": {
        "key": "requests",
        "values": {
            "key": "percentile",
            "values": ["1e-06", "25", "50", "50", "75", "100"],
        }
    },
}

FILTER_KEYS = {
    "latency": "latency_us",
    "req_throughput": "requests"
}

EXAMPLE = 'hello-world/gcp/g1-small'
DIR = os.getcwd()

PATH_IN = os.path.join(DIR, f"results/{EXAMPLE}/json")
PATH_OUT = os.path.dirname(PATH_IN)

FILE_SUFFIX = '_'.join([f"{k[0].lower()}{v}" for k, v in FILTER.items() if k in ['duration', 'threads', 'connections']])
if len(FILE_SUFFIX) > 0:
    FILE_OUT = f"data_{FILE_SUFFIX}.json"
else:
    FILE_OUT = "data.json"
PATH_OUT += f"/{FILE_OUT}"


def reader(path: str) -> Tuple[List[str], str]:
    """ Function to read the file """

    if not os.path.isfile(path):
        return None, "No file %s found", path

    with open(path, 'r') as f:
        try:
            return json.load(f), None

        except Exception as ex:
            return None, ex
        

def writer(path: str, obj: dict) -> str:

    try:
        with open(path, 'w') as f:
            json.dump(obj, f)
        return None

    except Exception as ex:
        pickle.dump(obj, path)
        return ex


def filter_list(input: dict, fltr: dict) -> Tuple[dict, str]:
    """ Functino to filter the input list of dict object """

    if len(fltr) == 0:
        return {}, None
    
    def _subset(lst: list, val_filter: str) -> int:
        """ Index from list by the filter value """
        
        for i, v in enumerate(lst):
            if v == val_filter:
                return i
    try:
        for element in input:
            for k, v in fltr.items():
                if k not in element.keys():
                    break
                elif isinstance(v, int):
                    if element[k] != v:
                        break
                    continue                
                elif isinstance(v, dict):                
                    subkey = fltr[k]['values']
                    filtered_indeces = [_subset(element[k][subkey['key']], i) for i in subkey['values']]
                    element[k][fltr[k]['key']] = [int(element[k][fltr[k]['key']][i]) for i in filtered_indeces]
                    element[k][subkey['key']] = [element[k][subkey['key']][i] for i in filtered_indeces]
            return element, None    
    except Exception as ex:
        return {}, ex                


def filter_keys(input: dict, fltr: dict) -> Tuple[dict, str]:
    """ Functino to filter the input dict object by its keys """
    
    if len(fltr) == 0:
        return {}, None
    try:
        return {v: input[k][v] for k, v in fltr.items()}, None
    
    except Exception as ex:
        return {}, ex     


def sorter(input: dict, key: str = "requests", desc: bool = True) -> Tuple[list, str]:
    """ Function to sort the input dict object by its key values median """
    try:        
        median_list0 = [int(median(obj[key])) for obj in input]
        median_list = median_list0.copy()
        median_list.sort(reverse=desc)
        
        scan_indeces = [i for i in range(len(median_list0))]
        sorted_indeces = []          
        for i in range(len(median_list)):
            for j, v in enumerate(scan_indeces):
                if median_list[i] == median_list0[v]:
                    sorted_indeces.append(v)
                    scan_indeces.pop(j)
                    break

        return [input[i] for i in sorted_indeces], None
    
    except Exception as ex:
        return [], ex    

if __name__ == "__main__":

    files = [i for i in os.listdir(PATH_IN) if i.endswith('.json')]
    if len(files) == 0:
        print("No files to process")
        sys.exit(0)

    output = []

    for iFile in files:
        fin, err = reader(os.path.join(PATH_IN, iFile))
        if err:
            print(err)
            sys.exit(1)

        template = {
            "name": ''.join(iFile.split('.')[:-1]),
        }
        
        fin_filter, err = filter_list(fin, FILTER)
        if err:
            print(err)
            sys.exit(1)
        
        if len(fin_filter) == 0:
            continue   
               
        fin_filter, err = filter_keys(fin_filter, FILTER_KEYS)
        if err:
            print(err)
            sys.exit(1)
        
        if len(fin_filter) == 0:
            continue
        
        for v in FILTER_KEYS.values():
            template[v] = fin_filter[v]
            
        output.append(template)
    
    output_sorted, err = sorter(output)
    if err:
        output_sorted = output
        print(f"Sorting unsuccessful. Error:\n{err}")
        print("Save unsorted data.")
          
    err = writer(PATH_OUT, output_sorted)
    if err:
        print(err)
        sys.exit(1)
