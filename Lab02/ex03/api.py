from cipher.railfence import RailFenceCipher
api.py

railfence_cipher = RailFenceCipher()

def encrypt():
	data = request.json
	plain_text = data['plain_text']
	key = int(data['key'])
	encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
	return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods= ['POST'])
def decrypt():
	data = request.json
	cipher_text = data['cipher_text']
	key = int(data['key'])
	decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
	return jsonify({'decrypted_text': decrypted_text})