# Job Sequencing with Deadline--Greedy method

#  Problem Statement:
# You have n jobs.

# Each job has:

# an id

# a deadline (by which it needs to be finished)

# a profit (earned if job is completed within deadline)

# Each job takes 1 unit of time

# You can schedule only one job at a time.

# 📝 Goal:

# Schedule jobs to maximize total profit.

# Return number of jobs done and total profit.

class Job:
    def __init__(self,id,deadline,profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit
def job_sequencing(jobs,n):
    jobs.sort(key=lambda x:x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    slots = [-1] * (max_deadline + 1)
    count_jobs = 0
    total_profit = 0
    for job in jobs:
        for d in range(job.deadline,0,-1):
            if slots[d] == -1:
                slots[d] = job.id
                count_jobs += 1
                total_profit += job.profit
                break
    return count_jobs, total_profit
jobs = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 1, 40), Job(4, 1, 30)]
n = len(jobs)

print(job_sequencing(jobs, n))
                
    
        
        
        



