import os
import xml.etree.ElementTree as ET
import re
# Define the folder path containing the XML files
folder_path = 'D:\\goAML_Report_Validator\\Seylan Bank' 

# Define the search and replace strings
main_search_string = 'WEALTH TRUST SECURITIES LIMITED'
search_string = "7056"
replace_string = "WTEYLKLX"

# Iterate over each XML file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xml"):
        file_path = os.path.join(folder_path, filename)
        try:
            # Parse the XML file
            tree = ET.parse(file_path)
            root = tree.getroot()

            print(f"Processing {filename}...")  # Debug print         
            
            modified = False
            #for swift_element in root.findall(".//swift"):
            # Loop through each <transaction> element
            for transaction in root.findall('transaction'):
                # Find all <institution_name> and <swift> elements under <transaction>
                institution_name_elements = transaction.findall('.//institution_name')
                swift_elements = transaction.findall('.//swift')
    
                # Loop through all <institution_name> elements
                for institution_name_element in institution_name_elements:
                    if main_search_string in institution_name_element.text:
                        # Find the corresponding <swift> element
                        for swift_element in swift_elements:
                            if main_search_string in institution_name_element.text and swift_element.text == search_string:
                                print ('SWIFT_search_string ' + str(swift_element.text)+ ' found for Main Search String '+ str(institution_name_element.text))
                                swift_element.text = replace_string
                                modified = True
                                print(f"Modified {filename} (swift: {search_string} -> {replace_string}).")
             
                                 
            # Save the modified XML back to the file if any changes were made
            if modified:
                tree.write(file_path)
                print(f"Saved modifications to {filename}")
            else:
                print(f"No matching 'swift' elements found in {filename}.")
            

        except ET.ParseError as pe:
            print(f"Parse error in {filename}: {pe}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")