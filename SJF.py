waiting_time = 0
turnaround_time = 0
burst_time = []
arrival_time = []

num = int(input("How many processes you want enter ?"))

for i in range(num):
    print('Enter Arrival time of Process P',i,": ")
    arrival_time.append(int(input()))
    print("Enter Burst time of Process P",i,": ")
    burst_time.append(int(input()))

small= 1

for j in range(num):
    if arrival_time[j] < arrival_time[small]:
        small = j

start_time = arrival_time[small]
arrival_time.append(1000)
for i in range(num):
    small = num
    for j in range(num):
        if (arrival_time[j]<= arrival_time[small]) and (burst_time[j] > 0):
            if arrival_time[j] is arrival_time[small]:
                if (burst_time[j]< burst_time[small]):
                    small = j
               
        if start_time > arrival_time[small]:
            waiting_time = start_time - arrival_time[small]
        else:
            waiting_time = arrival_time[small] - start_time
        start_time = start_time + burst_time[small]
        turnaround_time = waiting_time + burst_time[small]
        print('P', small, ":", "\t\tturnaround time: ", turnaround_time, "\t\tWaiting Time: ", waiting_time)
        burst_time[small] = 0