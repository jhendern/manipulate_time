import time
import datetime
import os
import subprocess

# === system clock time (local) ===
print (time.strftime("%Y%m%d%H"))

# ===
#Return date object with same year, month and day.
#print (datetime.date.today())
print (datetime.date(2000, 1,  1))

# ===
split_date = '2018-03-15-00'

print (datetime.datetime.strptime(split_date, '%Y-%m-%d-%H'))
# subtract 1.5 hours
print (datetime.datetime.strptime(split_date, '%Y-%m-%d-%H') - 
           datetime.timedelta(hours=1.5))
#          datetime.timedelta(days=1))

# =======
#yr = os.system("date -u +%Y")
#print(yr(0))

# === get UTC time year, month, day, hour ==
command = "date -u +%Y"
process = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
output, err = process.communicate()
tmp1 = output.decode("utf-8")
yr = (tmp1[0]+tmp1[1]+tmp1[2]+tmp1[3])
print(yr)

command = "date -u +%m"
process = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
output, err = process.communicate()
tmp1 = output.decode("utf-8")
mn = (tmp1[0]+tmp1[1])
print(mn)

command = "date -u +%d"
process = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
output, err = process.communicate()
tmp1 = output.decode("utf-8")
dy = (tmp1[0]+tmp1[1])
print(dy)

command = "date -u +%H"
process = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
output, err = process.communicate()
tmp1 = output.decode("utf-8")
hr = (tmp1[0]+tmp1[1])
print(hr)

