import argparse
import datetime as dt

parser = argparse.ArgumentParser(description='Add time strings')
parser.add_argument('times', type=str, nargs='+')
args = parser.parse_args()
print(args.times)

sum = dt.timedelta()

for time in args.times:
    ( m, s) = time.split(':')
    d = dt.timedelta(minutes=float(m), seconds=float(s))
    sum += d
print("Time sum is " + str(sum)),

print ('\nNote! Please pass values as MM:SS, or you will get bad results.')
