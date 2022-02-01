
import xml.etree.ElementTree as ET
tree = ET.parse('contry_data.xml')
root =  tree.getroot()

print(tree)
for child in root:
    print(child.tag, child.attrib)