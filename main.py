from stenography import encode_jpg,decode_jpg,clear_jpg_information

user_input = input("Enter Your Text to encode: ")
encode_jpg("pic.jpg",user_input)
print("Decoded version: ",decode_jpg("pic.jpg"))
clear_jpg_information("pic.jpg")