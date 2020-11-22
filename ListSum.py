import numpy as np

tot_time=[]
i=0
with open('log_file.txt') as input_file:
  for line in input_file:
    tot_time.append(int(line.split()[-1]))

print("Average : " + str(sum(tot_time)/len(tot_time)))
print("Max : " + str(max(tot_time)))
print("95th percentile : " + str(np.percentile(tot_time, 95)))
