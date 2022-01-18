# Time in seconds

time = int(input('Please enter your number:'))
hour = time //3600
r = time - 3600 * hour
miniute = r // 60
second = r - 60 * miniute

print(f'{hour}:{miniute}:{second}')