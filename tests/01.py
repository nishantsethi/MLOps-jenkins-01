import os
import sys

WORKSPACE = os.environ['WORKSPACE']
LASTRECORD=WORKSPACE+"/tests/last_result.txt"
ACCURACYFILE=WORKSPACE+"/script/accuracy.txt"
SCORE=open(ACCURACYFILE, 'r').read()


if not os.path.exists(LASTRECORD):
    LASTSCORE = 0
else:
    LASTSCORE = float(open(LASTRECORD, 'r').read())




if float(LASTSCORE) > float(SCORE):
    print("New Accuracy(",SCORE,") is lower than Previous accuracy(",LASTSCORE,")")
    print("Test 1 Failed as Accuracy is not above the Last recorded accuracy")
    sys.exit('Exiting Script')
elif float(LASTSCORE) == float(SCORE):
    print("New Accuracy(",SCORE, ") is EQUAL to the Previous accuracy(",LASTSCORE,")")
    print("Test 1 Passed")
else:
    print("New Accuracy(",SCORE,") is GREATER than the Previous accuracy(",LASTSCORE,")")
    print("Test 1 Passed")

text_file = open(LASTRECORD, "w")
text_file.write(SCORE)
text_file.close()

print("All Tests Passed")
print("############################")
print("####  Script Termed OK  ####")
print("############################")