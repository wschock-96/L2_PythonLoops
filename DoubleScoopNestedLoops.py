# TASK 1 YOUR MOOD TRACKER
import random

moods = ["happy", "sad", "energetic", "calm", "grumpy", "tired", "excited"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["morning", "afternoon", "evening"]

for i in range(len(days)):
    for j in range(len(times)):
        days_of_week = days[i]
        feeling_today = random.choice(moods)
        time_of_day = times[j]
        if time_of_day:
            print(f"Today is {days_of_week} {time_of_day} and I am feeling {feeling_today}!")
        elif time_of_day:
            print(f"Today is {days_of_week} {time_of_day} and I am feeling {feeling_today}!")
        else:
            print(f"Today is {days_of_week} {time_of_day} and I am feeling {feeling_today}!")   
 
        
    


