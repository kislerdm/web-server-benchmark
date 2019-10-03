import os
import sys
import csv
import re
import json
import pickle
from typing import Tuple, List

EXAMPLE = 'hello-world/gcp/g1-small'
DIR = os.getcwd()
PATH_RAW = os.path.join(DIR, f"results/{EXAMPLE}/raw")
PATH_JSON = os.path.join(DIR, f"results/{EXAMPLE}/json")

SPLIT_PATTERN = "---"
SPLIT_TESTS = "--new-test--"


def parser(document: str) -> Tuple[dict, str]:
    """ Function to parse summary file """
    def _scanner(pattern: str, search_str: str, **args) -> str:
        found_element = re.findall(pattern, search_str, **args)
        if found_element:
            return found_element[0]
        return None

    def _tab_parser(table_lst: list, delimeter: str = ',', header: bool = True) -> dict:
        """ Function to parse tables from the summary """
        reader = csv.reader(table_lst, delimiter=delimeter)

        try:
            if header:
                headers = next(reader, None)

            columns = {k: [] for k in headers}

            for row in reader:
                for k, v in zip(headers, row):
                    columns[k].append(v)
        except Exception as ex:
            print(ex)
            return None

        return columns

    list_tests = []

    for doc in document.split(SPLIT_TESTS):
        template = {
            "duration": None,
            "threads": None,
            "connections": None,
            "requests": None,
            "total_time": None,
            "latency": {},
            "req_throughput": {}
        }

        document_list = [i.strip() for i in doc.split(SPLIT_PATTERN)]

        # parse pt.1 of the summary
        try:
            template['duration'] = int(
                _scanner("Running (\d+).? test", document_list[0], flags=re.I))
            template['threads'] = int(
                _scanner("(\d+) threads", document_list[0], flags=re.I))
            template['connections'] = int(
                _scanner("(\d+) connections", document_list[0], flags=re.I))
            template['requests'] = int(
                _scanner("(\d+) requests in", document_list[0], flags=re.I))
            template['total_time'] = float(
                _scanner("requests in (\d+.\d+).?,", document_list[0], flags=re.I))
        except Exception as ex:
            return None, f"Parsing of the 1st summary part error:\n{ex}"
        # parse pt.2 of the summary
        template['latency'] = _tab_parser(document_list[1].split('\n')[1:])
        # parse pt.3 of the summary
        template['req_throughput'] = _tab_parser(
            document_list[2].split('\n')[1:])

        list_tests.append(template)

    return list_tests, None


def reader(path: str) -> Tuple[List[str], str]:
    """ Function to read the file """
    if not os.path.isfile(path):
        return None, "No file %s found", path

    with open(path, 'r') as f:
        try:
            return f.read(), None

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


if __name__ == "__main__":

    files = [i for i in os.listdir(PATH_RAW) if i.endswith('.txt')]
    if len(files) == 0:
        print("No files to process")
        sys.exit(0)

    for iFile in files:
        fin, err = reader(os.path.join(PATH_RAW, iFile))
        if err:
            print(err)
            sys.exit(1)

        dat, err = parser(fin)
        if err:
            print(err)
            sys.exit(1)

        iFile_OUT = '{}.json'.format(''.join(iFile.split('.')[:-1]))
        PATH_OUT = os.path.join(PATH_JSON, iFile_OUT)

        err = writer(PATH_OUT, dat)
        if err:
            print(err)
            sys.exit(1)
