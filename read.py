data = []
count = 0 # loop count
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print('We are running to', count, 'th message') # print every 1000 loop

print('In total, we have', len(data), 'message')

# Calculate average message length
sum_length = 0 # initial length
for d in data:
	sum_length += len(d)
print('Average message length is:', sum_length / len(data))

# Show ?th message as user's requirement
while True:
	num = int(input('Which ?th message do you want to show?(? is integer from 1 to 1000000) '))
	print(data[num - 1])
	print('------------------------------------')