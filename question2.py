class Picture:
    def __init__(self, d, h, w, fc):
        self.__Description = d #as STRING
        self.__Height = h #as INTEGER
        self.__Width = w #as INTEGER
        self.__FrameColour = fc #as STRING
    
    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__FrameColour
    def SetDescription(self, NewDesc):
        self.__Description = NewDesc

def ReadData(myArray):
    filename = r"C:\Users\Abood\Desktop\School\Final Revision Files\Computer Science\Past paper python\P4 Papers\Oct Nov 2021\Pictures.txt"
    count = 0
    try:
        file = open(filename, "r")
        Description = (file.readline()).strip().lower()
        while Description != "":
            Width = int((file.readline()).strip())
            Height = int((file.readline()).strip())
            FrameColour = (file.readline()).strip().lower()
            myArray[count] = Picture(Description, Height, Width, FrameColour)
            Description = (file.readline()).strip().lower()
            count = count + 1
        file.close()
    except IOError:
        print("Could not find File")
    return count

myArray = [Picture("",0,0,"") for i in range(100)]

FrameColour = input("Input frame colour: ").lower()
MaxWidth = int(input("Input max width: "))
MaxHeight = int(input("Input max height: "))
picCount = ReadData(myArray)
print("Search results:")
for i in range(picCount):
    if myArray[i].GetColour() == FrameColour:
        if myArray[i].GetHeight() <= MaxHeight:
            if myArray[i].GetWidth() <= MaxWidth:
                print(myArray[i].GetDescription(),"", myArray[i].GetWidth(),"",myArray[i].GetHeight())

