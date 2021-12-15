import csv
file = open('agaa-obj.csv')
csvreader = csv.reader(file)

# counting the years 
years = []
counter = 0

with open('agaa-obj.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	for row in file:
		if (not row[0]):
			break;
		years.append(row.split('.')[0])
		counter+=1
	# file.close()

year_freq = {}

# iterating over the list
for item in years:
	if len(item) == 4:
		if item in year_freq:
			# incrementing the counr
			year_freq[item] += 1
		else:
			# initializing the count
			year_freq[item] = 1

keys = list(year_freq.keys())

# import matplotlib.pyplot as plt
# plt.figure()
# plt.bar(keys,year_freq.values())
# plt.show()


# materials 
letters = []
rowList = []


# with open('types.csv', newline='') as csvfile:
# 	reader = csv.reader(csvfile)
# 	for row in csvfile:
# 		print(row)
# 		rowList = row.split(',')
# 		# if (not row[0]):
# 		# 	break;
		
# 		letters.append(rowList[9].split(':')[0])

# print(rowList)
# print(letters)

medias = []

media = open('media.csv')
for line in media:
	medias.append(line)

media_freq = {}
# iterating over the list
for item in medias:
	print (item)
	if item in media_freq:
		# incrementing the counr
		media_freq[item] += 1
	else:
		# initializing the count
		media_freq[item] = 1

keys = list(media_freq.keys())