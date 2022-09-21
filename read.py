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

# Calculate how many messages are there wiht length lower than 100
new = [] # 'new' list to store messages with length lower than 100
i = 0 # message count of message length < 100
for message in data:
	if len(message) < 100:
		new.append(message.strip())
		i += 1
print('There are', i, 'message(s) whose length is lower 100')
print(new)

# Filter out messages with word 'good'
new2 = [] # 'new2' list to store messages with good or Good
for message in data:
	if 'good' in message or 'Good' in message:
		new2.append(message.strip())
print('There are', len(new2), 'message(s) with good or Good word inside')

# Show ?th message as user's requirement
# while True:
# 	num = int(input('Which ?th message do you want to show?(? is integer from 1 to 1000000) '))
# 	print(data[num - 1])
# 	print('------------------------------------')