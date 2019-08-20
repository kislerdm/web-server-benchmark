#! /bin/bash
# benchmark runner

fout=$1 
url="http://0.0.0.0:4500/"
script=benchmark_summary.lua

wrk -t1 -c100 -d10s -s ${script} "${url}" > ${fout}
# wrk -t1 -c200 -d10s "${url}" >> ${fout}
# wrk -t10 -c100 -d10s "${url}" >> ${fout}
# wrk -t10 -c200 -d10s "${url}" >> ${fout}