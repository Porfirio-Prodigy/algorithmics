
n1 = int(input("add first number: "))
n2 = int(input("add second number: "))
n3 = int(input("add third number: "))
n4 = int(input("add forth number: "))
n5 = int(input("add fifth number: "))

string_number = [n1, n2, n3, n4, n5]

init_set = 1 # variable used to set cn for continuing at looping
ani = 0 #alternation number index
cn = 1 #count number
ml = len(string_number) - 1 #max lenght

while ani <= ml: 
	if string_number[0] != min(string_number):
		while ani < ml:
			if string_number[ani] == min(string_number):
				string_value = string_number[0] #switch values 
				string_number[0] = string_number[ani]
				string_number[ani] = string_value
				break
			
			else:
				ani += 1
		ani = 0


	while cn <= ml:
		if string_number[ani] <= string_number[cn]:
			pass
		
		if string_number[ani] > string_number[cn]:
			string_value = string_number[ani] #switch values
			string_number[ani] = string_number[cn]
			string_number[cn] = string_value
			
		cn += 1
		
	ani += 1
	init_set += 1
	cn = init_set
	
print(string_number)
