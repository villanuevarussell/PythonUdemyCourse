
#Calculates income taxes using 2018 Federal Tax Brackets for people who are single
def TaxCalcFed(grossincome):
	if grossincome > 510301:
		taxpercentage = .37
		amountover = grossincome - 510301
		totaltaxes = 153798.50 + (amountover*taxpercentage)
	elif grossincome >204101 and grossincome < 510300:
		taxpercentage = .35
		amountover = grossincome - 204100
		totaltaxes = 46628.50+ (amountover*taxpercentage)
	elif grossincome >160726 and grossincome <204100:	
		taxpercentage = .32
		amountover = grossincome - 160726
		totaltaxes = 32748.50 + (amountover*taxpercentage)
	elif grossincome >84201 and grossincome <160725:	
		taxpercentage = .24
		amountover = grossincome - 84201
		totaltaxes = 14382.50 + (amountover*taxpercentage)
	elif grossincome > 39476 and grossincome <84201:	
		taxpercentage = .22
		amountover = grossincome - 39476
		totaltaxes = 4543 + (amountover*taxpercentage)
	elif grossincome > 9701 and grossincome < 39476:	
		taxpercentage = .12
		amountover = grossincome - 39476
		totaltaxes = 970 + (amountover*taxpercentage)
	else:	
		taxpercentage = .10
		totaltaxes = grossincome*taxpercentage

	return totaltaxes

def TaxCalcState(grossincome):

	if grossincome > 1000000000:
		taxpercentage = .133
		totaltaxes = grossincome*taxpercentage
	elif grossincome > 551473:
		taxpercentage = .123
		totaltaxes = grossincome*taxpercentage
	elif grossincome > 330884:
		taxpercentage = .113
		totaltaxes = grossincome*taxpercentage	
	elif grossincome > 275738:
		taxpercentage = .103
		totaltaxes = grossincome*taxpercentage
	elif grossincome > 53980:
		taxpercentage = .093
		totaltaxes = grossincome*taxpercentage	
	elif grossincome > 42711:
		taxpercentage = .08
		totaltaxes = grossincome*taxpercentage	
	elif grossincome > 30769:
		taxpercentage = .04
		totaltaxes = grossincome*taxpercentage	
	elif grossincome > 19485:
		taxpercentage = .03
		totaltaxes = grossincome*taxpercentage		
	elif grossincome > 8223:
		taxpercentage = .02
		totaltaxes = grossincome*taxpercentage
	else:
		taxpercentage = .01
		totaltaxes = grossincome*taxpercentage

		print("hello")

	return totaltaxes


#Running Script
if __name__ == "__main__":
	#Takes in user input
	grossincome = int(input("Input Gross Income: "))

	#Calculates Federal Tax and State Tax
	fedTax = TaxCalcFed(grossincome)
	stateTax = TaxCalcState(grossincome)

	#Output
	print(f"Federal Taxes owed: {round(fedTax,2)}")
	print(f"State Taxes owed: {round(stateTax,2)}")	
	print(f"Total Taxes owed: ${round(fedTax+stateTax,2)}")


