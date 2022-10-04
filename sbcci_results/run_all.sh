#!/bin/bash

echo '' > results.txt

find ../src -iname "*with_regs.v" | while IFS= read -r d; do
  echo "running $d..."
  make SRCS=$d sim | grep throughput >> results.txt
done
