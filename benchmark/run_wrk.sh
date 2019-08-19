#! /bin/bash

source wrk_config.sh

BASE_URL="http://0.0.0.0"
PATH_RESULTS="results"

for i in ${!PORTS[@]}; do

  url=${BASE_URL}:${PORTS[${i}]}

  echo "Testing API (label: ${LABEL[${i}]}) access on ${url}"

  curl -I -X GET ${url} > /dev/null 2>&1
  if [[ ! $? -eq 0 ]]; then
    echo "Cannot reach APi on ${url}"
    continue
  fi

  echo "Benchmarking API (label: ${LABEL[${i}]}) on ${url}"
  fout=${PATH_RESULTS}/${PATH_SOURCE}/${LABEL[${i}]}_throughput.dat

  wrk -t1 -c100 -d10s "${url}" > ${fout};
  wrk -t1 -c200 -d10s "${url}" >> ${fout};
  wrk -t10 -c100 -d10s "${url}" >> ${fout};
  wrk -t10 -c200 -d10s "${url}" >> ${fout};

done
