import xml.etree.ElementTree as ET  # Import the ElementTree module for XML parsing.

input = '''  # Define a multiline string containing XML data.
        <stuff>
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Chuck</name>
                </user>
                <user x="7">
                    <id>009</id>
                    <name>Brent</name>   
                </user>
            </users>
        </stuff>
        '''

stuff = ET.fromstring(input)  # Parse the XML data into an ElementTree object.
lst = stuff.findall('users/user')  # Find all <user> elements within <users>.
print('User count:', len(lst))  # Print the count of <user> elements.

for item in lst:  # Iterate over each <user> element.
    print('Name', item.find('name').text)  # Print the text of the <name> element.
    print('Id', item.find('id').text)  # Print the text of the <id> element.
    print('Attribute', item.get('x'))  # Print the value of the 'x' attribute of the <user> element.