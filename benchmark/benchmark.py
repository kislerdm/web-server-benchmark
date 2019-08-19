from requests import get
import time
import json
import numpy as np
import scipy.stats as statistics

REPETITIONS = 1000

fOUT = 'benchmark_hex.json'
URL = {'py': "http://0.0.0.0:10011/hex?hexcode=f0a0ff",
       'go': "http://0.0.0.0:10010/hex?hexcode=f0a0ff",
       }
# fOUT = 'benchmark_rgb.json'
# URL = {'py': "http://0.0.0.0:10011/rgb?r=240&g=160&b=255",
#        'go': "http://0.0.0.0:10010/rgb?r=240&g=160&b=255",
#        }


def benchmark(URL: dict) -> dict:
  
    timimng = {k: [] for k in URL.keys()}
    
    for api, url in URL.items():
      for _ in range(REPETITIONS):
        t0 = time.time()
        resp = get(url)
        try:
            if resp.json()['data']['is_warm'] == 0:
              timimng[api].append(time.time() - t0)
            else:
              timimng[api].append(None)
        except Exception as ex:
            timimng[api].append(None)
    
    return timimng


def stats(arr: list) -> dict:
    """ Function to calculate summary stats
        
        Args:
            arr: list of numbers for stats
        
        Returns:
            dict with stats:
                {'count': int,
                 'median': float,
                 'mean': float,
                 'std': float
                }
    """

    def _is_normal(arr: list,
                   alpha: float = 0.05) -> bool:
        return True if statistics.shapiro(arr)[1] < alpha else False
  
    cnt = len([i for i in arr if i is not None])

    return {
        'count': int(cnt),
        'median': float(np.median(arr)),
        'mean': float(np.mean(arr)),
        'std': float(np.std(arr)),
        'is_normal_dist': _is_normal(arr)
    }


def is_different_dist(arr_a: list,
                      arr_b: list,
                      alpha: float = 0.05) -> bool:
    return True if statistics.ttest_ind(arr_a, arr_b)[1] < alpha else False


if __name__ == "__main__":
    timimng = benchmark(URL)
    
    summary = {}
    for api, arr in timimng.items():
      summary[api] = stats(arr)
    
    output = {"data": timimng,
              "stats": summary
              }
    
    if False not in [j['is_normal_dist'] for j in [i for i in summary.values()]]:
        output['stats']['is_significantly_different'] = is_different_dist(timimng['py'], 
                                                                          timimng['go'])
    
    json.dump(output, open(fOUT, 'w'))
