print("===========================================================")
print("============Welcome to Bay Area Maker Faire 2019===========")
print("===========================================================")
print("============Let's have some fun with Mad Libs!=============")
print("===========================================================")
filename=input("Enter MadLibs File Name(it is tarzan.txt):")
print("===============OK...let's start the fun====================")

f=open(filename,'r')
wordList=f.read().split()
f.close()

position=0
for i in wordList:
    if i[0]=="<":
        wordList[position]=input("Enter "+ i[1:len(i)-1]+" :")
    position+=1

print("===========================================================")
print("=========Here is super funny Mad Libs you created==========")
print("===========================================================")

for i in wordList:
    print(i,end=" ")
f.close
