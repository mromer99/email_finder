import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from openpyxl import load_workbook
import re


# Load the list of websites
df = pd.read_excel('gruenderwettberbe.xlsx', engine='openpyxl')

# Prepare a list to store the emails
emails = []

# Function to extract email from tag
def extract_email(tag):
    try:
        user_part = tag.contents[0]
        domain_part = tag.contents[2]
        return f'{user_part}@{domain_part}'
    except IndexError:
        return None
    
# Function to extract obfuscated email from tag
def extract_obfuscated_email(tag):
    obfuscated_email = tag.string
    return obfuscated_email.replace('[at]', '@').replace('(at)', '@')

# Function to extract obfuscated email from script tag
def extract_script_email(tag):
    # Extract the arrays from the script's text
    arrays_text = tag.string.split('([', 1)[1].rsplit('])', 1)[0]
    
    # Split the arrays into two separate strings
    array1_text, array2_text = arrays_text.split('],[')
    
    # Remove quotes and split by comma to get the arrays
    array1 = array1_text.replace("'", "").split(',')
    array2 = [int(i) for i in array2_text.split(',')]
    
    # Use the indices to get the email parts and join them
    email_parts = [array1[i] for i in array2]
    email = ''.join(email_parts)
    
    # Extract the email from the mailto link
    email = email.split(':', 1)[1].rsplit('">')[0]
    return email

def extract_emails_from_text(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)


def decode_email(encoded_email):
    parts = encoded_email.split('([', 1)[1].rsplit('])', 1)[0]
    array1, array2 = parts.split('],[')
    array1 = array1.replace("'", "").split(',')
    array2 = [int(i) for i in array2.split(',')]
    email_parts = [array1[i] for i in array2]
    email = ''.join(email_parts)
    email = email.split(':', 1)[1].rsplit('">')[0]
    return email

# Function to extract email from 'a' tag with 'mailto:' href
def extract_email_from_a_tag(soup):
    a_tag = soup.find('a', href=lambda href: href and href.startswith('mailto:'))
    if a_tag:
        email = a_tag.text
        return email
    return None



# Go through all websites
for website in df['website']:
    print(f'Scraping {website}')
    try:
        # Send a get request
        response = get(website)

        # If the get request is successful, the status code will be 200
        if response.status_code == 200:
            # Get the content of the response
            page_content = BeautifulSoup(response.content, 'html.parser')

            
            # Find all 'a' tags with a 'mailto:' href, 'a' tags with a 'javascript:linkTo_UnCryptMailto' href, 'a' tags with a '[at]' or '(at)' in the text, and script tags with a type of "text/javascript" that contain a mailto link
            elements = page_content.select('a[href^=mailto], a[href^="javascript:linkTo_UnCryptMailto"], a:contains("[at]"), a:contains("(at)"), script[type="text/javascript"]:contains("mailto")')
            for i in elements:
                
                if i.name == 'a':
                    # Check if it's a regular mailto link
                    if i['href'].startswith('mailto:'):
                        # Extract the email
                        email = i['href']

                        # Remove the 'mailto:' part
                        email = email.replace('mailto:', '')
                            
                        emails.append(email)
                        print(f'Found email: {email}')
                        break
                    else:
                        # Check if it's an obfuscated email link
                        if i.find('i', {'class': 'fa fa-at'}):
                            email = extract_email(i)
                            if email is not None:
                                emails.append(email)
                                print(f'Found email: {email}')
                                break
                            
                        else:
                            # Check if it's an obfuscated email with [at] or (at)
                            if '[at]' in i.string or '(at)' in i.string:
                                email = extract_obfuscated_email(i)
                                emails.append(email)
                                print(f'Found email: {email}')
                                break
                
                elif i.name == 'script':
                    # Extract the obfuscated email from the script tag
                    try:
                        encoded_email = i.string.split('([', 1)[1].rsplit('])', 1)[0]
                        email = decode_email(encoded_email)
                        emails.append(email)
                        print(f'Found email: {email}')
                        break
                    except: 
                        continue
            else:
                print('No email found on main page, checking Impressum...')
                # Find a link that contains "impressum" or "imprint" in the href
                impressum_link = page_content.find('a', href=lambda href: href and ('impressum' in href.lower() or 'imprint' in href.lower()))
                if impressum_link:
                    # Get the href of the impressum link
                    impressum_href = impressum_link.get('href')
                    # Make it an absolute URL
                    impressum_url = urljoin(website, impressum_href)
                    impressum_response = get(impressum_url)
                    if impressum_response.status_code == 200:
                        impressum_content = BeautifulSoup(impressum_response.content, 'html.parser')

                        # New code: extract emails from text content of the Impressum page
                        impressum_text = impressum_content.get_text()
                        impressum_emails = extract_emails_from_text(impressum_text)
                        if impressum_emails:
                            for email in impressum_emails:
                                emails.append(email)
                                print(f'Found email in Impressum: {email}')
                                break
                        else:

                            impressum_mailtos = impressum_content.select('a[href^=mailto], a[href^="javascript:linkTo_UnCryptMailto"], a:contains("[at]"), a:contains("(at)")')
                            for i in impressum_mailtos:
                                # Check if it's a regular mailto link
                                if i['href'].startswith('mailto:'):
                                    # Extract the email
                                    email = i['href']

                                    # Remove the 'mailto:' part
                                    email = email.replace('mailto:', '')
                                    
                                    emails.append(email)
                                    print(f'Found email in Impressum: {email}')
                                    break
                                else:
                                    # Check if it's an obfuscated email link
                                    if i.find('i', {'class': 'fa fa-at'}):
                                        email = extract_email(i)
                                        if email is not None:
                                            emails.append(email)
                                            print(f'Found email: {email}')
                                            break
                                    else:
                                        # Check if it's an obfuscated email with [at] or (at)
                                        if '[at]' in i.string or '(at)' in i.string:
                                            email = extract_obfuscated_email(i)
                                            emails.append(email)
                                            print(f'Found email in Impressum: {email}')
                                            break
                            else:
                                emails.append('No email found in Impressum')
                                print('No email found in Impressum')
                    else:
                        emails.append('Impressum not accessible')
                        print('Impressum not accessible')
                else:
                    emails.append('No Impressum link found')
                    print('No Impressum link found')
        else:
            emails.append('Website not accessible')
            print('Website not accessible')
    except Exception as e:
        emails.append(f'Error: {str(e)}')
        print(f'Error: {str(e)}')

# Add the emails to the dataframe
df['Emails'] = emails

# Save the dataframe to a new .xlsx file
try:
    df.to_excel('gruenderwettberbe_email.xlsx', index=False, engine='openpyxl')
    print('Results saved to your excel file')
except Exception as e:
    print(f'Error when saving results: {e}')