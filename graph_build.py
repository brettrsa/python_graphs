#!/usr/bin/python
#
# Testing graphs out
#
# Start
#

# Import Libraries
import pylab as pl
import sys
import datetime as dt

# Variables
file_in = sys.argv[1]
data = open(file_in, 'r')

# Intialise arrays
pps_in = []
pps_out = []
timestamp = []

# Loop through input data and load into array, format timestamps
for i in data:

   columns = i.split()
   # Append data to array and convert bytes to mbps
   pps_in.append((int(columns[0]) / 131072))
   pps_out.append((int(columns[1]) / 131072))
   # Append data to array in the specified timestamp
   timestamp.append(dt.datetime.strptime((columns[2]),"%H:%M:%S-%d/%m/%Y"))

# Close the input data
data.close()

# Generate the graph
pl.title('asa-firewall-line-tag - gi0/0 - outside interface')
pl.xlabel('time')
pl.ylabel('megabits per second')
pl.subplots_adjust(left=0.2)
pl.subplots_adjust(bottom=0.2)
pl.xticks(rotation = 25)
pl.grid(True)
pl.plot(timestamp, pps_in, 'b', label='input')
pl.plot(timestamp, pps_out, 'g', label='output')
pl.legend(loc='upper right')
pl.savefig('test.png')

# End
