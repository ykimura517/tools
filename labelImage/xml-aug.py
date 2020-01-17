import xml.etree.ElementTree as ET
import glob
import os

how_many_xmls=50
#eg. dupXml(iwaki.xml,3)-----> <filename>iwaki3.jpg</filename> みたいな感じになる
def dupXml(target_xml,afternum):


    # xml_files = glob.glob("xml/*.xml")
    tree = ET.parse(target_xml)
    root = tree.getroot()



    #change xml

    for filename in root.iter("filename"):
        assert ".jpg" in filename.text,"Please .jpg file!"
        filename.text = (filename.text.replace(".jpg",""))+str(afternum)+(".jpg")



    for path in root.iter("path"):
        path.text = (path.text.replace(".jpg",""))+str(afternum)+(".jpg")

    #save
    tree.write(target_xml.replace(".xml","")+str(afternum)+(".xml"))

if __name__ == "__main__":
    xml_files=glob.glob("./*.xml")


    for target_xml in xml_files:
        for i in range(how_many_xmls):
            dupXml(target_xml,i)
