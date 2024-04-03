from cipher.vigenere import VigenereCipher

vigenere_cipher = VigenereCipher()

@app.route("/api/vingenere/encrypt", methods=["POST"])
def vingenere_encrypt():
	data = request.json
	plain_text = data['plain_text']
	key = data['key']
	encrypted_text = vingenere_cipher.vingenere_encrypt(plain_text,key)
	return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/vingenere/decrypt", methods =["POST"])
def vingenere_decrypt():
	data = request.json
	cipher_text = data['cipher_text']
	key = data['key']
	decrypted_text = vingenere_cipher.vingenere_decrypt(cipher_text, key)
	return jsonify({'decrypted_text': decrypted_text})
