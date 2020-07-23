import sys, getopt
from PIL import Image

def main(argv):
   inputIMG = ''
   inputDATA = ''
   try:
      opts, args = getopt.getopt(argv,"hed",["ii=","id="])
   except getopt.GetoptError:
      print('invalid arguments \nhdii.py -e/-d --ii <input_image_file> --id <input_data_file>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('hdii.py -e/-d --ii <input_image_file> --id <input_data_file>')
         sys.exit()
      elif opt in ("--ii"):
         inputIMG = arg
      elif opt in ("--id"):
         inputDATA = arg
   for opt, arg in opts:
      if opt == '-e':
         hideData(inputIMG,inputDATA)
      elif opt == '-d':
          retriveData(inputIMG)

def hideData(imgSrc,dataSrc):
    print("------- opening Data file")
    f = open(dataSrc, "r")
    data =f.read()
    print(data)
    print("------- opening Data file : sucessful\n")
    print("------- converting data to binary")
    bdata=' '.join(format(ord(x), 'b') for x in data)
    print(bdata)
    print("------- converting data to binary:sucessful\n")
    print("------- opening image ")
    img = Image.open(imgSrc)
    pixels=img.load()
    print("------- opening image :sucessful\n")
    print("------- writing data to image")
    width,height=img.size
    length=len(bdata)
    temp=0
    print("h=",height)
    print("w=",width)
    print("data  length=",length)
    cor=x,y=0,0
    print(img.getpixel(cor)[2])  
    if(length>(height*width)):
        print("image too small")
        exit()
    end=False
    print(height,width)
    for j in range(height):
        if end==True:
            break
        for k in range(width):
            cor=k,j
            if temp<length:
                if(bdata[temp]==' '):
                  pixels[cor]=(pixels[cor][0],2,pixels[cor][2])
                  #img.putpixel((j, k), (img.getpixel(cor)[0],img.getpixel(cor)[1],2))
                  temp+=1
                else:
                  pixels[cor]=(pixels[cor][0],int(bdata[temp]),pixels[cor][2])
                  #img.putpixel((j, k), (img.getpixel(cor)[0],img.getpixel(cor)[1],int(bdata[temp])))
                  temp+=1
            else:
               pixels[cor]=(pixels[cor][0],3,pixels[cor][2])
               print(cor)
               end=True
               break
    name=raw_input("enter image name to save:")
    name+='.png'
    img.save(name)
    print("------- writing data to image: sucessful : saved as ",name)


def retriveData(imgSrc):
    print("------- opening image")
    img=Image.open(imgSrc)
    width,height=img.size
    print("------- opening image:sucessful")
    cor=j,k=479,359
    end=False
    x=' '
    bdata=' '
    print("------- retriving binary data")
    for j in range(height):
        for k in range(width):
            cor=k,j
            if(end==False):
               if(img.getpixel(cor)[1]==3):
                  end=True
                  break
               else:
                  if(img.getpixel(cor)[1]==2):
                     bdata+=x
                  else:
                     bdata+=str(img.getpixel(cor)[1])
            else:
               break
    print("------- retriving binary data:sucessful")
    print("------- converting binary to ascii")
    binary_values = bdata.split()
    ascii_string = ""
    for binary_value in binary_values:
         base2=int(binary_value, 2)
         ascii_car=chr(base2)
         ascii_string+=ascii_car
    print("------- converting binary to ascii:sucessful")
    print(ascii_string)
    
main(sys.argv[1:])   