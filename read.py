import time
import re # re module for multiple delimiters split
import progressbar

data = []
count = 0 # loop count
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('In total, we have', len(data), 'message')
print(data[0])

# Turn message list into word list and calculate which word occurs the most often
start_time = time.time()
def word_count(data):
	word_count_dict = {}
	word_count_list = []
	for msg in data:
		word_list = msg.split()
		for word in word_list:
			if word not in word_count_dict:
				word_count_dict[word] = 1
			else:
				word_count_dict[word] += 1
	for key in word_count_dict:
		if word_count_dict[key] > 100:
			print(key, word_count_dict[key])
	for key in word_count_dict:
		word_count_list.append([word_count_dict[key], key])
	word_count_list.sort(reverse=True)
	print('The word' + ' "' + word_count_list[0][1] + '" ' + 'show out the most and show out', word_count_list[0][0], 'time(s)')
	end_time = time.time()
	time_gap = end_time - start_time
	print(start_time)
	print(end_time)
	print('takes', time_gap, 's to finish dict')
	while True:
		word = input('What word do you wanna know how many times it shows: ')
		if word == 'q':
			break
		elif word in word_count_dict:
			print(word, 'shows out', word_count_dict[word], 'time(s)')
		else:
			print('This word does not exist in the messages')

word_count(data)


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
# new2 = [] # 'new2' list to store messages with good or Good
# for message in data:
# 	if 'good' in message or 'Good' in message:
# 		new2.append(message)
# print('There are', len(new2), 'message(s) with good or Good word inside')

# List comprehension (line 36 = line 29 ~ 32)
new2 = [message for message in data if 'good' in message or 'Good' in message]
print('There are', len(new2), 'message(s) with good or Good word inside')

# Show ?th message as user's requirement
# while True:
# 	num = int(input('Which ?th message do you want to show?(? is integer from 1 to 1000000) '))
# 	print(data[num - 1])
# 	print('------------------------------------')