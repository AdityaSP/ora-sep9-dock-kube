import sys
import csv
import unittest

if len(sys.argv) != 2:
    print("Usage: mainrunner.py <path to test csv>")
    exit(-1)
    
ts = unittest.TestSuite()    
fh = open(sys.argv[1])
#sys.argv = sys.argv[0]

for testline in csv.DictReader(fh):
    if testline['run'] not in ['y','Y','1']:
        continue
    imptest = "import {}".format(testline['Module'])
    exec(imptest)
    tc = "{}.{}('{}')".format(testline['Module'], testline['testcase'], testline['test'])
    ts.addTest(eval(tc))
    
r = unittest.TextTestRunner(verbosity = 3)
r.run(ts)
