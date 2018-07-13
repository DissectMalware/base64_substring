import math
import base64

def get_base64_substr(substr_arr, char_sizeof=1):
	step = char_sizeof
	for i in range(0,3*step, step):
		left_context = math.ceil((((2*step - i)*8) / 6))
		encoded = base64.b64encode( substr_arr[i:])[left_context:]
		pad_count = encoded.count(b'=')
		right_context = math.ceil((pad_count * 8) / 6)
		yield encoded[:len(encoded) - right_context].decode('ascii')
			
def get_padded_unicode(text):
	res = bytearray(b'\x00\x00\x00\x00')
	res[2:] = bytearray(text.encode('utf-16'))
	return res
		  
def get_padded_ascii(text):
	res = bytearray(b'\x00\x00')
	res[2:] = bytearray(text.encode('ascii'))
	return res
	

if __name__ == "__main__":
	print("please enter a text:")
	
	input_str = input()
	bytearr_ascii = get_padded_ascii(input_str)
	bytearr_unicode = get_padded_unicode(input_str)
	
	for i in get_base64_substr(bytearr_ascii):
		print(i)
	
	for i in get_base64_substr(bytearr_unicode, 2):
		print(i)