import xml.etree.ElementTree as ET


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
        print(type(root[1][count][0].text))
        print(root[1][count][1].text)
        root[1][count][1].text = dict[root[1][count][0].text]
        count+=1
    file.write('new.xml')

def main():
    # load rss from web to update existing xml file
    # parse xml file
    file1 = parseFile('pink.xml')
    file2 = parseFile('black.xml')

    print(file1)
    print(file2)
    file3 = combine(file1, file2)
    print(file3)
    generateXML(file3)
    # store news items in a csv file
    
      
      
if __name__ == "__main__":
  
    main()