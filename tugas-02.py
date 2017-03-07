print "\tDaftar KODE ASCII"
print("---------------------------------------")
print("%9s | %7s | %4s | %9s |" %("character","decimal","hex","binary")) 
print("---------------------------------------")
	
for i in range(32,126):
	print("%9c | %7d | %4s | %9s |" %(i, i, hex(i),bin(i)))  
print("---------------------------------------")
	

	
