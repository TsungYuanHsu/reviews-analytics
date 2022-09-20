data = []
count = 0 # loop count
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print('We are running to', count, 'th message')

print('In total, we have', len(data), 'message')

# Show ?th message as user's requirement
while True:
	num = int(input('Which ?th message do you want to show?(? is integer from 1 to 1000000) '))
	print(data[num - 1])
	print('------------------------------------')