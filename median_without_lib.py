num=[3,6,2,5,6,7,3,7,3,6,8,2,5,6]
n=len(num)
num.sort()

if n%2==0:
	med1=num[n//2]
	med2=num[n//2-1]
	med=med1+med2

else:
	med=num[n//2]

print("Median="+str(med))