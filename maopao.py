def bub(bublist):
	listlength = len(bublist)
	while listlength > 0:
		for i in range(listlength - 1):
		 if bublist[i] > bublist[i+1]:
			bublist[i]=bublist[i]+bublist[i+1];
			bublist[i+1]=bublist[i]-bublist[i+1];
			bublist[i]=bublist[i]-bublist[i+1];
		listlength -= 1
	print bublist

if __name__=='__main__':
	bublist=[60,50,30,40,20,10];
	bub(bublist);
