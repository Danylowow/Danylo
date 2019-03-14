#encode = input("input text to encode:  ")
#encode_text = ''
#for letter in encode:
	#encode = ord(letter) + 1
	#encode_text = encode_text + chr(encode)

#print(encode_text)

#x = input('nazad: ')
#if lower(x) == "yes"
	#print


#def hello_world():
	#print('hello_world')

#hello_world()

def encoder(encode_string):
	encoder_text = ""
	if plus_or_minus.lower() == "zakodyvatu":
		for s in encode_string:
			r = ord(s)+1
			encoded_text = encoded_text + chr(r)
	else:
		for s in emcode_string:
			r = ord(s)-1
			encoder_text = encoder_text + chr(r)

	print(encoded_text)


x = input('vvedit text dla zakodyvanya chu kodyvanya: ')
z = input('zakodyvatu chu rozkodyvatu?: ')
encoder_or_decoder(x,z)

def output(z):
	print(z)
