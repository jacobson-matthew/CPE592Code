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
    return str(''.join(format(i, '08b') for i in bytearray(inputString, encoding ='utf-8')))\
    
#encode data into image for given technique 
def encode(filename,word,technique): 
    info = strtobitstream(word)
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
    for i in range(x, y): 
        print(pixels[i, z])
    #if lsb, encode via lsb
    if technique == "lsb":
       for q in range(x,y):
           curr = pixels[q,z]
           
    #if msb, encode via msb
    if technique == "msb":
        print("msb")
        
#decode data out of an image for a given technique    
def decode(filename,technique):
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
