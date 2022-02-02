from contextlib import redirect_stderr
from threading import currentThread
from xml.etree.ElementPath import get_parent_map
from PIL import Image 
import sys
#USAGE = python3 steno.py [image filename] [word/name] [lsb/msb] [encode/decode]
#author Matthew Jacobson - 10433353 
# I pledge my honor that I have abided by the Stevens Honor System - Matthew Jacobson
"""
general sudocode but ill code this out anways

Inputs: python3 steno.py [image filename] [word/name] [lsb/msb] [encode/decode]

Outputs: Success/Error message and new image file with filename = filename+(lsb/msb)+msgenc + .jpg or whatever

Algo: 
Check for inputs, lsb or msb ( least signfigant bit or most signifigant bit ), encode or decode
(might add check if the image is big enough to encode data just for fun)
if encode,
take word/name and encode it into a list of bits
then take image and using Python image library (Pillow) get per pixel information and encode data 
save and output new image with corresponding technique (lsb or msb)
if decode, 
check if lsb or msb 
read either lsb or msb and put into a list to be decoded 
decode based on list back to string values
else, 
wtf was the input, there arent any other options
"""

# def converttobitstream(word):
#     #list to hold my answer
#     done = []
#     #take my word and split it into a list so its easy to process
#     listInput = list(word)
#     #now iterate through the word and turn it into a bitstream with all the correct values
#     for x in listInput: 
#     #return answer
#     return done
def strtobitstream(inputString):
    # this magic line is from https://www.geeksforgeeks.org/python-convert-string-to-binary/ using byte array to convert each character in a string to binary effeicently
    return str(''.join(format(i, '08b') for i in bytearray(inputString, encoding ='utf-8')))

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
        
def binarychangemsb(binary,bit):
    #normalizes binary to 8 digits (API can return binary values with less than 8 bits)
    length = len(str(binary))
    if len(str(binary)) != 8 :
        modbin = ((8-length)*"0")+str(binary)
    #edit lsb
    modbin = list(str(binary))
    modbin[0] = str(bit)
    #join back together and return answer as a single string 
    return "".join(str(b) for b in modbin)        
        
#encode data into image for given technique
def encode(filename,word,technique): 
    #convert the word to a form that we can put into the pixels
    info = list(strtobitstream(word))
    #variable to keep track of where we are in the information that we have to encode
    infopos = 0
    #load image 
    im = Image.open(filename)
    pixels = im.load()
    # x = start pixel ( maybe add interesting offset )
    # y = end pixel
    # z = distance from the top 
    x = 0
    #make sure there is space to write the exact amount of bytes of data
    y = x+len(info)
    # default zero, can increase security by tying the height to the key being encoded (idk just a suggestion)
    z = 0
    #now get these pixel values
    # for i in range(x, y): 
    #     print(pixels[i, z])
    #if lsb, encode via lsb
    if technique == "lsb":
        print(info)
        for q in range(x,y): # for pixel location in range x -> y 
           #now take pixels and edit them with lsb information 
           #grab current pixel rgb values curr @ (q,z) 
           curr = list(pixels[q,z])
           #now for each pixel in the range (which is the exact amount needed to encode bits) turn to binary and make change 
           newred = bin(curr[0])[2:]
           newgreen = bin(curr[1])[2:]
           newblue = bin(curr[2])[2:] 
           print("------")
           print(str(newred)+" "+str(newgreen)+" "+str(newblue))
           red = binarychangelsb(newred,info[infopos])
           infopos+=1
           green = binarychangelsb(newgreen,info[infopos])
           infopos+=1
           blue =  binarychangelsb(newred,info[infopos])
           if infopos == len(info)-1:
            break
           else:
                infopos+=1
           print(red+" "+green+" "+blue)
           print("------")
           
           
        #    currred =  curr[0]
        #    currgreen = curr[1] 
        #    currblue =  curr[2]
        #    print("curr values")
        #    print(bin(currred)[2:])
        #    print(bin(currgreen)[2:])
        #    print(bin(currred)[2:])
        #    print('-------')
        #    #encode each bit into the lsb of the pixel information  
        #    #this can be done with a loop but written out for testing purposes
        #    newred =  binarychangelsb(bin(currred)[2:],info[infopos])
        #    infopos+=1
        #    newgreen = binarychangelsb(bin(currgreen)[2:],info[infopos])
        #    infopos+=1
        #    newblue =  binarychangelsb(bin(currblue)[2:],info[infopos])
        #    infopos+=1
        #    print("New values: ")
        #    print(newred)
        #    print(newred)
        #    print(newblue)
        #    print('-------')

            
               
        
           
           
           
           
           
           
           
    #if msb, encode via msb
    if technique == "msb":
        print("msb")
        
#decode data out of an image for a given technique    
def decode(filename,technique,lengthofkey):
    #load image 
    im = Image.open(filename)
    pixels = im.load()
    #check for technique
    if technique == lsb :
        #now for the length grab values and concat them 
        None
    

def main():
    if len(sys.argv) != 5:
        print(len(sys.argv))
        print("Correct Usage: python3 steno.py [image filename] [word/name] [lsb/msb] [encode/decode]")
    else:
        # check for encode or decode
        if sys.argv[4]=="encode" :
            #return 0 if successful we can error check later
            return encode(sys.argv[1],sys.argv[2],sys.argv[3])
        if sys.argv[4]=="decode" :
            #return encoded information 
            return decode(sys.argv[1],sys.argv[3])

if __name__ == "__main__":
    main()
