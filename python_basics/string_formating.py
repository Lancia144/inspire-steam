# Nmae : Daniel nduati
# date : 12/02/2026
# string formating

# Get string length
sentence = 'I watch formula 1'

string_lenght = len(sentence)

print(f"the lenght is:{string_lenght}")

# spliting_string
sentence_2 = "mathematics physics"
split = sentence_2.split(" ")

print(f" the first subject is: ", split[0])

# make everything CAPS
mpesa_code = "ub2e57op"

capitalized = mpesa_code.upper()
print(f"new mpesa code: ", capitalized) 

mpesa_code = "UB2E57OP"

small = mpesa_code.lower()
print(f"new mpesa code: ", small) 

# replacing characters in #string

balance = "900Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes", "")
print("cleaned balance", cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", "")
print("cleaned_amount_added:" , cleaned_amount_added)

new_balance = int(cleaned_balance) + int(cleaned_amount_added)
print(f"new balance is:", new_balance)
 
end = "Kes"
new_balance_complete = str(new_balance) + str(end)
print(f"Confirmed you have recevied {amount_added} from Philip.New balance is:", int(new_balance) + int(50),str(end))
