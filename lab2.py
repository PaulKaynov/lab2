massive=[14, 15, 16, 167, 71]
line = "hello, world"

ivan = {
   "name" : "ivan" ,
	"age" : 34,
	"children" : [{
	   "name" : "vasja" ,
	   "age" : 19,
   }, {
       "name" : "petja" ,
       "age" : 19,
   }],
}
darja = {
   "name" : "darja" ,
   "age" : 41,
   "children" : [{
       "name" : "kirill" ,
       "age" : 21,
   }, {
       "name" : "pavel" ,
       "age" : 15,
   }],
}
emps = [ivan, darja]

def fun_begin(massive): 
	print("massive: ")
	for i in range(len(massive)):
	       print(massive[i])

def fun_min(massive):
	print("min of massive:")
	return print(min(massive))

def fun_med(massive):
	print ("med of massive:")
	med = sum(massive)/len(massive)
	return print(med)
	
def fun_line(line):
	print (line)
	out = line[::-1]
	print(out)
	
def fun_worker(emps, age_of_child):
	filtered = []
	for work in emps:
		for child in work['children']:
		    if child['age'] > age_of_child:
			    filtered.append(work['name'])
			    break
	return filtered
		
	
fun_begin(massive)
fun_min(massive)
fun_med(massive)
fun_line(line)
print(fun_worker(emps, 18))