Amount = int(input("What amount of money do you wish to withdraw : "))
note1 = Amount//100
note2 = (Amount%100)//50
note3 =((Amount%100)%50)//10

print("You will need this many 100 rupees :" , note1)
print("You will need this many 50 rupees :" , note2)
print("You will need this many 10 rupees :" , note3)