small = 0
waiting_time = 0
turnaround_time = 0
burst_time = []
arrival_time = []
burst =[]

num = int(input("How many processes you want to enter ?"))

for i in range(num):
    print('Enter Arrival time of Process P',i,": ")
    arrival_time.append(int(input()))
    print("Enter Burst time of Process P",i,": ")
    burst_time.append(int(input()))
for i in range(num):
    burst.append(burst_time[i])


for j in range(num):
    if arrival_time[j]<arrival_time[small]:
        small = j
start_time = arrival_time[small]
arrival_time.append(100000)
burst_time.append(100000)
i = 0
while i < num:
    small = num
    for j in range(num):
        if (arrival_time[j] <= start_time) and (burst_time[j]<burst_time[small]) and (burst_time[j]>0):
            small = j
    burst_time[small] = burst_time[small]-1
    start_time = start_time+1
    if burst_time[small] is 0:
        waiting_time = start_time - arrival_time[small]- burst[small]
        turnaround_time = waiting_time + burst[small]
        i+=1
        print('P', small, ":", "\t\tturnaround time: ", turnaround_time, "\t\tWaiting Time: ", waiting_time)