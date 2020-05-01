import xml.etree.ElementTree as ET

tree = ET.parse('./Legis.xml')
root = tree.getroot()

of = open('regulations-by-act.csv', 'w')

of.write('Act ID,Act number,Act title,Regulation ID,Regulation title\n')
for act in root.iter('Act'):
	actId = act.find('UniqueId')
	actNumber = act.find('OfficialNumber')
	actTitle = act.find('Title')
	for regRef in act.findall('.//Reg[@idRef]'):
		regRefId = regRef.get('idRef')
		reg = root.find('.//Regulation[@id=\'' + regRefId + '\']')
		regId = reg.find('UniqueId')
		regTitle = reg.find('Title')
		of.write('"' + actId.text + '","' + actNumber.text + '","' + actTitle.text + '","' + regId.text + '","' + regTitle.text + '"\n')
