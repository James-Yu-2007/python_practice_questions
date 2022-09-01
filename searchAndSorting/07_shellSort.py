def shellSort(arr, n):
	gap=n//2	
	while gap>0:
		j=gap
		while j<n:
			i=j-gap			
			while i>=0:
				if arr[i+gap]>arr[i]:
					break
				else:
					arr[i+gap],arr[i]=arr[i],arr[i+gap]
				i=i-gap
			j+=1
		gap=gap//2

arr2 = [5,2,3,1,4]
print("input array:",arr2)

shellSort(arr2,len(arr2))
print("sorted array",arr2)

# algerism above was learned from another source
# code above still not fully understood