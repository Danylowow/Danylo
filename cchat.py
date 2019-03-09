def encoder_or_decoder(encode_string,plus_or_minus):
	encode_text = ""
	if plus_or_minus.lowe() == "zakodyvatu":
		for s in encode_string:
			r = ord(s)+1
			encode_text = encode_text + chr(r)
	else:
		for s in encode_string:
			r = ord(s)-1
			encode_text = encode_text + chr(r)


	print(enocde_text)		