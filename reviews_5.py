data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1 #count = count + 1
        data.append(line)
        if count % 100000== 0:
            print(len(data))
print('檔案讀取完成,共有',len(data),'筆資料')

#print(data[0])


wc = {} #word_count
for d in data: #d是data清單中的每一筆留言
    words = d.split(' ')
    for word in words:  #檢查words清單中的每一個字有沒有出現在字典裡
        if word in wc:  #如果word有在字典裡出現過
            wc[word] += 1  #value + 1
        else:
            wc[word] = 1 #新增key進字典
for word in wc: #word就是Dict裡面的每一個key
    if wc[word] > 1000000:
       print(word, wc[word]) #把word跟key value都一起印出來
print(len(wc))
while True:
    word = input('What word do you want to find?')
    if word == 'q':
        print('Thanks for using.')
        break
    print(word,'There are', wc[word],'times in all comments.')    
    