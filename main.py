from stenography import encode_jpg,decode_jpg,clear_jpg_information

file_loc = input("Enter the jpg file location: ")
user_input = input("Enter Your Text to encode: ")

encode_jpg(file_loc,user_input)
print("Decoded version: ",decode_jpg(file_loc))
clear_jpg_information(file_loc)