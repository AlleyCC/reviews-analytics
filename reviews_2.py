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


 