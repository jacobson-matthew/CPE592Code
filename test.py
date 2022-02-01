import sys
from PIL import Image 

im = Image.open("blue.jpg")

pixels = im.load()

mypixels = []

for i in range(0, 10): 
        mypixels.append(pixels[i, 0])
        
for x in mypixels : 
    for z in str(x)[1:-1].split(','):
         value = bin(int(z))
         print(value)
         
    print(" ")

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


