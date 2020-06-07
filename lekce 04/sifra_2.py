text = list(input("Zadej text, který chceš zašifrovat:"))

while True:
	try:
		key = int(input("Zadej klíč, který bude pozitivní celé číslo:"))
		assert(key > 0), 'Číslo musí být větší než 0'
		break
	except:
		print("Zkus to znova!")

new_text = ""
while text:
    text_2 = text.pop(0)
    if str(text_2).isalnum():
        slovo = chr(ord(text_2)+key)
        new_text = new_text + slovo    
    else:
        new_text = new_text + text_2
print("Zašifrovaný text je:", new_text)
