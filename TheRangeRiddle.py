# TASK 1 YOUR MOOD TODAY
import random 

moods = ["happy", "sad", "energetic", "calm", "grumpy", "tired", "excited"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(days)):
    day_of_week = days[i]
    feeling_today = random.choice(moods)
    print(f"Today is {day_of_week} and I am feeling {feeling_today}!")