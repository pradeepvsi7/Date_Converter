def date_changer(n): 
	month = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
	n[1] = month[n[1]]
	return n
n = [int(date) for date in input("Enter the date ").split()]
for date in date_changer(n):
	print(date,end=" / ")
