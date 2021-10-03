def encode_jpg(filepath:str,content:str):
  with open(filepath, "ab") as f:
    f.write(content.encode('ascii') )

def decode_jpg(filepath:str):
  with open(filepath,"rb") as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    f.seek(offset+2)
    return f.read()


def clear_jpg(filename:str):
  with open(filename,"rb") as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    f.seek(0)
    return f.read(offset+2)

def clear_jpg_information(filename:str):
  data = clear_jpg(filename)
  with open(filename,"wb") as f:
    f.write(data)