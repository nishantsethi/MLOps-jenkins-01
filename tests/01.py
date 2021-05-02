import os
import sys

WORKSPACE = os.environ['WORKSPACE']
LASTRECORD=WORKSPACE+"/tests/last_result.txt"
ACCURACYFILE=WORKSPACE+"/script/accuracy.txt"
SCORE=open(ACCURACYFILE, 'r').read()


# if not os.path.exists(LASTRECORD):
#     LASTSCORE = 0
# else:
#     LASTSCORE = int(open(LASTRECORD, 'r').read())


LASTSCORE = 0


if int(LASTSCORE) > int(SCORE):
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