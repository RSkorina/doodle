#Decode Pizza Prob


encoded = 'JCCVVRAIAPXZVBH DR ULQGNTUPBV HXVNS DCI GBH NDY RYS CDX UVBT HS NLZRDQV AC HIEXL HLD LVYS XH E YPBI XSFR IE XR KOS EPVRWFDU SWMWRT TJ AVTGI THB DCPP IS DCI NPBCXV XVCS AYTR'
easyEnc = 'JCCVVRAIAPXZVBH'
easyDec	= 'CONGRATULATIONS'

# for i in range(0, len(easyEnc)):
	# print( chr((ord(easyEnc[i]) - ord(easyDec[i])) % 26 + ord('A'))

key = 'HOPPER'

answer = ""
spaceCount = 0

for j in range(0, len(encoded)):
	if(encoded[j] == " "):
		answer += " "
		spaceCount+= 1
	else: 		
		answer += chr(((ord(encoded[j]) - ord(key[(j-spaceCount) %6]))% 26) + ord('A'))

print(answer)
		
		
	
	