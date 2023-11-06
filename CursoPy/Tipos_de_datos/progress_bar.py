import time

def progress_bar(total, part, length=30):
    fraction = part / total
    completed = int(fraction * length)
    missing = length - completed
    bar = f"[{'*'*completed}{'-'*missing}]{fraction:.2%}"
        
    return bar 

def call_progress_bar(n, i=0):
    for i in range(n + 1):
        time.sleep(0.1)
        print(progress_bar(n, i),end='\r')
        
call_progress_bar(100)