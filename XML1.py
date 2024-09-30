import xml.etree.ElementTree as ET  # Import the ElementTree module for XML parsing.

data = '''  # Define a multiline string containing XML data.
        <person>
            <name>Chuck</name>
            <phone type='intl'>
                +1 734 303 4456
            </phone>
            <email hide="yes"/>
        </person> 
        '''

tree = ET.fromstring(data)  # Parse the XML data into an ElementTree object.
print('Name:', tree.find('name').text)  # Print the text of the <name> element.
print('Attr:', tree.find('email').get('hide'))  # Print the value of the 'hide' attribute of the <email> element.