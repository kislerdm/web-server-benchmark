#! /bin/bash
# benchmark runner

fout=$1 
url="http://0.0.0.0:4500/"
script=benchmark_summary.lua

wrk -t1 -c1 -d10s -s ${script} "${url}" > ${fout}

echo "--new-test--">> ${fout}
wrk -t1 -c100 -d10s -s ${script} "${url}" >> ${fout}

echo "--new-test--">> ${fout}
wrk -t10 -c100 -d10s -s ${script} "${url}" >> ${fout}