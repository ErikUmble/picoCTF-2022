# measures the time it took to run the command 'echo $1 ./pin_checker'
# $1 should be an 8-digit potential PIN
# echoes the time that the command took to execute
START=$(date +%s.%N)
echo $1 | ./pin_checker
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo $DIFF