class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    
    for process in processes:
        current_time = max(current_time, process.arrival_time)
        turnaround_time = current_time - process.arrival_time + process.burst_time
        waiting_time = turnaround_time - process.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        current_time += process.burst_time
        
    return total_turnaround_time / len(processes), total_waiting_time / len(processes)

def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    remaining_processes = list(processes)
    
    while remaining_processes:
        eligible_processes = [p for p in remaining_processes if p.arrival_time <= current_time]
        if not eligible_processes:
            current_time += 1
            continue
        shortest_job = min(eligible_processes, key=lambda x: x.burst_time)
        remaining_processes.remove(shortest_job)
        current_time += shortest_job.burst_time
        turnaround_time = current_time - shortest_job.arrival_time
        waiting_time = turnaround_time - shortest_job.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
    
    return total_turnaround_time / len(processes), total_waiting_time / len(processes)

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    remaining_processes = list(processes)
    
    while remaining_processes:
        eligible_processes = [p for p in remaining_processes if p.arrival_time <= current_time]
        if not eligible_processes:
            current_time += 1
            continue
        highest_priority = min(eligible_processes, key=lambda x: x.priority)
        remaining_processes.remove(highest_priority)
        current_time += highest_priority.burst_time
        turnaround_time = current_time - highest_priority.arrival_time
        waiting_time = turnaround_time - highest_priority.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
    
    return total_turnaround_time / len(processes), total_waiting_time / len(processes)

def round_robin_scheduling(processes, time_quantum):
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    remaining_processes = list(processes)
    
    while remaining_processes:
        process = remaining_processes.pop(0)
        if process.remaining_time <= time_quantum:
            current_time += process.remaining_time
            turnaround_time = current_time - process.arrival_time
            waiting_time = turnaround_time - process.burst_time
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time
        else:
            current_time += time_quantum
            process.remaining_time -= time_quantum
            remaining_processes.append(process)
    
    return total_turnaround_time / len(processes), total_waiting_time / len(processes)

    # Example processes
processes = [
        Process(1, 0, 24, 3),
        Process(2, 4, 3, 1),
        Process(3, 5, 3, 4),
        Process(4, 6, 12, 2),
    ]

avg_turnaround_fcfs, avg_waiting_fcfs = fcfs_scheduling(processes.copy())
avg_turnaround_sjf, avg_waiting_sjf = sjf_scheduling(processes.copy())
avg_turnaround_ps, avg_waiting_ps = priority_scheduling(processes.copy())
avg_turnaround_rr, avg_waiting_rr = round_robin_scheduling(processes.copy(), time_quantum=2)

print("FCFS Average Turnaround Time:", avg_turnaround_fcfs)
print("FCFS Average Waiting Time:", avg_waiting_fcfs)
print("SJF Average Turnaround Time:", avg_turnaround_sjf)
print("SJF Average Waiting Time:", avg_waiting_sjf)
print("Priority Scheduling Average Turnaround Time:", avg_turnaround_ps)
print("Priority Scheduling Average Waiting Time:", avg_waiting_ps)
print("Round Robin Average Turnaround Time:", avg_turnaround_rr)
print("Round Robin Average Waiting Time:", avg_waiting_rr)

# Determine the best algorithm based on ATAT
algorithms = {
        "FCFS": avg_turnaround_fcfs,
        "SJF": avg_turnaround_sjf,
        "Priority Scheduling": avg_turnaround_ps,
        "Round Robin": avg_turnaround_rr
    }

best_algorithm = min(algorithms, key=algorithms.get)
print("The best scheduling algorithm is:",best_algorithm)
   
