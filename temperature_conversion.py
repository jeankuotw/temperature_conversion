# 小程式:溫度轉換(攝氏與華氏)

# 攝氏c轉為華氏f
c = input('請輸入攝氏溫度:') #創造c攝氏變數,並請使用者輸入攝氏溫度
c = float(c) #型別轉換成小數。(注意)如果寫c = int(c),只轉換成整數int,那使用者就不能輸入小數,程式會顯示錯誤

f = c * 9 / 5 + 32 #創造f華氏溫度變數

print('華氏溫度為:', f , '度')

# 華氏f轉為攝氏c
f = input('請輸入華氏溫度:')
f = float(f)

c= ( f - 32 ) * 5 / 9
print('攝氏溫度為:', c , '度')