#!/bin/bash


LASTRECORD="$WORKSPACE/tests/last_result.txt"
ACCURACYFILE="$WORKSPACE/script/accuracy.txt"
SCORE=`cat $ACCURACYFILE`


if [ ! -e "$LASTRECORD" ] ; then
    echo 0 > "$LASTRECORD"
fi

LASTSCORE=`cat $LASTRECORD`

if [[ ! $SCORE -ge $LASTSCORE ]] ; then
    echo "New Accuracy($SCORE) is lower than Previous accuracy($LASTSCORE)"
    echo "Test 1 Failed as Accuracy is not above the Last recorded accuracy"
    echo "Exiting Script"
    exit 42
else
    echo SCORE > "$LASTRECORD"
    echo "New Accuracy($SCORE) is greater or equal to the Previous accuracy($LASTSCORE)"
    echo "Test 1 Passed"
fi

echo "All Tests Passed"
echo "Script Termed OK"