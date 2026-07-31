import time

user_time = int(input("Enter time in seconds: "))

for i in range(user_time, 0, -1):
    sec = i % 60
    min = int((i / 60) % 60)
    hour = int(i / 3600)

    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)