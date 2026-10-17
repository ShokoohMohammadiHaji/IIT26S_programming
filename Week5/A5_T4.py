def askDimension ():
    width = float(input ("Insert width: "))
    height = float(input("Insert height: "))
    return width , height
def calcRectangleArea (Pwidth,Pheight):
    area = Pwidth * Pheight
    return area
def main ():
    print("Program starting.")
    (width,height) = askDimension()
    area = calcRectangleArea (width,height) 
    print(f"\nArea is {round(area,1)}²")
    print("Program ending.")
main()