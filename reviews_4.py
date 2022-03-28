data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1 #count = count + 1
		data.append(line)
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成,共有',len(data),'筆資料')
 
sum_len = 0
for d in data:
	sum_len += len(d)	
print('每筆留言的平均長度為', sum_len / len(d))


new = []
for d in data:
 	if len(d) < 100:
 		new.append(d)
print('Total:', len(new),'筆留言小於100字。')
print(new[0])
print(new[15])


good = []

#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('總共有', len(good),'筆留言有good
#print(good[0])
#print(good[14])

good = [d for d in data if 'good' in d]
print(len(good),'筆留言提到good')

bad = []
bad = ['bad' in d for d in data] #'bad' in d在這邊是布林值(True/False)
print(bad)
