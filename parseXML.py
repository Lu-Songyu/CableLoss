import xml.etree.ElementTree as ET
import sys
from tkinter import *

loop = 282
# parse in XML file
def parseFile(filename):
    file = ET.parse(filename)
    root = file.getroot()
    dict = {"Measurement": "CableLoss"}

    count = 0

    while count < loop :
        dict[root[1][count][0].text] = root[1][count][1].text
        count+=1
    
    return dict

def combine(dict1, dict2):
    for k in dict1:
        if k is not "Measurement":
            dict1[k] = str(float(dict1[k]) + float(dict2[k]))
    
    return dict1

def generateXML(dict):
    file = ET.parse('pink.xml')
    root = file.getroot()

    count = 0
    while count < loop :
        # root[1][count][1].text is loss
        # root[1][count][0].text is measurement
        root[1][count][1].text = dict[root[1][count][0].text]
        count+=1
    file.write('result.xml')

def main():
    # load rss from web to update existing xml file
    # parse xml file
    file1 = parseFile(sys.argv[1])
    file2 = parseFile(sys.argv[2])
    file3 = combine(file1, file2)

    generateXML(file3)

    window=Tk()
    window.title('Combine Cable Loss')
    window.geometry("800x600+100+200")
    window.mainloop()

    # store news items in a csv file
    
      
      
if __name__ == "__main__":
  
    main()