import os.path

LASTRECORD="$WORKSPACE/tests/last_result.txt"
ACCURACYFILE="$WORKSPACE/script/accuracy.txt"
SCORE=open(ACCURACYFILE, 'r').read()


if not os.path.exists(LASTRECORD):
    LASTSCORE = 0
else:
    LASTSCORE = open(LASTRECORD+'.txt', 'r').read()



if LASTSCORE > SCORE:
    print("New Accuracy(",SCORE,") is lower than Previous accuracy(",LASTSCORE,")")
    print("Test 1 Failed as Accuracy is not above the Last recorded accuracy")
    sys.exit('Exiting Script')
else:
    text_file = open(LASTRECORD, "w")
    text_file.write(SCORE)
    text_file.close()
    print("New Accuracy($SCORE) is greater or equal to the Previous accuracy(",LASTSCORE,")")
    eprint("Test 1 Passed")

print("All Tests Passed")
print("Script Termed OK")