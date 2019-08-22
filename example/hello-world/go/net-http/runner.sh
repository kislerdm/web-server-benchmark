#! /bin/sh

./run_server &

proc=$(echo $(ps | grep "run_server$" | awk '{print $1}'))

# taskset -c 0 -p ${proc}

chmod +x wrk_benchmark.sh
sh wrk_benchmark.sh results.txt
