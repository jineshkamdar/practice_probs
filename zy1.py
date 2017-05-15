cache_size=20 #change cache size here
cache=[]
id_info={}

file1=open('cache.txt','r')
cached_IDs=file1.readline()
if len(cached_IDs)>0:
	cache=cached_IDs.split(' ')

file4=open('id_info.txt','r')
data4=file4.read()
if len(data4)>0:
	with open('id_info.txt','r') as inf:
		id_info=eval(inf.read())


file2=open('stud_data.txt','r')
data2=file2.readlines()

print ()
print ('curent cache:',cache)
print ()

while True:
	print ('enter ID (from 1001-1300) to access the data or 0 to exit')
	entered_option=input()
	if int(entered_option)==0:
		#save cache to file
		file=open('cache.txt','w')
		for i in range(0,len(cache)):
			if i==len(cache)-1:
				file.write(str(cache[i]))
			else:
				file.write(str(cache[i])+' ')
		file.close()
		#save id_info to file
		file3=open('id_info.txt','w')
		file3.write(str(id_info))
		file3.close()
		exit()
	elif int(entered_option) in range(1001,1300):
		print ()
		print ('current cache:',cache)
		print ()
		if entered_option in cache:
			#bring existing ID to start and shift
			print ('ID already in cache')
			cache.pop(cache.index(entered_option))
			cache.insert(0,entered_option)
			print ()
			print ('current cache:',cache)
			#id_info[entered_option]=data2[int(entered_option)-1000]
			print ('ID info:',id_info[entered_option])
		else:
			print ('ID not in cache') 
			if len(cache)<cache_size:
				#if cache empty then add ID and related data to 'cache' and 'id_info' resp.
				print ('cache is not full, can add',entered_option)
				print ()
				cache.insert(0,entered_option)
				print ('current cache:',cache)
				id_info[entered_option]=data2[int(entered_option)-1000]
				print ('ID info:',id_info[entered_option])
			else:
				#if cache full then pop LRU ID and add NEW ID and related data to 'cache' and 'id_info' resp.
				print ('cache is full, need to pop LRU ID and add',entered_option)
				print ()
				popped=cache[-1]
				cache.pop()
				cache.insert(0,entered_option)
				print ('current cache:',cache)
				del id_info[popped]
				id_info[entered_option]=data2[int(entered_option)-1000]
				print ('ID info:',id_info[entered_option])
	else:
		print ('please enter correct option')
