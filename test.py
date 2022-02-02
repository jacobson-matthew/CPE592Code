import sys
from PIL import Image 

im = Image.open("blue.jpg")

# def pixelTest():
#     pixels = im.load()

#     mypixels = []

#     for i in range(0, 10): 
#             mypixels.append(pixels[i, 0])
            
#     for x in mypixels : 
#         for z in str(x)[1:-1].split(','):
#             value = list(str(bin(int(z))))
#             value[-1] = "1"
#             ''.join(value)
#             print(value)
#         print(" ")
        

        
  
# def binarychangelsb(binary,bit):
#     #normalizes binary to 8 digits (API can return binary values with less than 8 bits)
#     print(binary)
#     length = len(str(binary))
#     if len(str(binary)) != 8 :
#         modbin = ((8-length)*"0")+str(binary)
#     #edit lsb
#     modbin = list(str(binary))
#     modbin[-1] = str(bit)
#     return "".join(str(b) for b in modbin)
    
def binarychangelsb(binary,bit):
        #normalizes binary to 8 digits (API can return binary values with less than 8 bits)
    length = len(str(binary))
    if len(str(binary)) != 8 :
        modbin = ((8-length)*"0")+str(binary)
    #edit lsb
    modbin = list(str(binary))
    modbin[-1] = str(bit)
    #join back together and return answer as a single string 
    return "".join(str(b) for b in modbin)  
    
        
        
        
        
        
    

print(int(binarychangelsb("01001101",0),base=2))
  
  
        
# pixelTest()

# def strtobitstream(inputString):
#     # this magic line is from https://www.geeksforgeeks.org/python-convert-string-to-binary/ using byte array to convert each character in a string to binary effeicently
#     return str(''.join(format(i, '08b') for i in bytearray(inputString, encoding ='utf-8')))

# print(list(strtobitstream("Matthew")))

# temp = list(c)
# print(temp)
# done = []
# for i in temp:
#     res = ''.join(format(i, '08b') for x in bytearray(i, encoding ='utf-8'))
#     done.append(res)
# print(done0)

#https://www.geeksforgeeks.org/python-convert-string-to-binary/
#https://www.kite.com/python/examples/3199/pil-edit-an-image-pixel-by-pixel
# using join() + bytearray() + format()
# # Converting String to binary
# res = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))


# test_str = "GeeksforGeeks"
  
# # printing original string 
# print("The original string is : " + str(test_str))
  
# # using join() + bytearray() + format()
# # Converting String to binary
# res = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))
  
# # printing result 
# print("The string after binary conversion : " + str(res))

# print(map(bin,bytearray(sys.argv[1].encoding("utf-8"))))


