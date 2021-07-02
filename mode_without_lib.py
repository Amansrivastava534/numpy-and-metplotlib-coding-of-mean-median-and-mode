from collections import Counter
num=[3,6,2,5,6,7,3,7,3,6,8,2,5,6]
n=len(num)

data=Counter(num)
get_mode=dict(data)
mode=[k for k,v in get_mode.items()if v==max(list(data.values()))]


if len(mode)==n:
	get_mode="no mode"
else:
	get_mode="mode is:"+",".join(map(str,mode))
	print(get_mode)