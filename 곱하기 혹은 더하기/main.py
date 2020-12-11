data=input()

result=int(data[0])

for i in range(1,len(data)):
    if data[i]==0 or result==0:
        result+= int(data[i])
    else:
        result *=int(data[i])

print(result)

'''
입력값#1
02984

입력값#2
567
'''