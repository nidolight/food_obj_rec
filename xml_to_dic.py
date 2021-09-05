from xml.etree.ElementTree import Element, dump, ElementTree
import xml.etree.ElementTree as ET

import os
import shutil
from tqdm import tqdm

folder = r"C:\Users\junho\Desktop\xml_downloaded"
inputs = r'C:\Users\junho\Desktop\xml_downloaded'
outputs = r'C:\Users\junho\Desktop\xml_downloaded\result'
for r, d, f in os.walk(inputs):
    for file in f:
        full = os.path.join(r, file)
        shutil.move(full, outputs)


# xml_file = 'D:\\test.xml'
# doc = ET.parse(xml_file)
# root = doc.getroot()

# size_tag = root.findall("size")
