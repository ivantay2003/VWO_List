
import requests
from bs4 import BeautifulSoup
import csv
import os.path

url = 'https://www.ncss.gov.sg/GatewayPages/Social-Service-Organisations/Membership/List-of-NCSS-Members'

page = requests.get(url)
print ("status code " + str(page.status_code))

# print (page.content)
soup = BeautifulSoup(page.content, 'html.parser')
maincontent = list(soup.children)
#
# print (maincontent)

result = soup.find_all('a')[150].get_text()

print (result)

index=0;
data=[]
data.append([])

for a in soup.find_all('a', href=True):
    print ("Found the URL " + str(index) + ":" + a['href'])

    try:
        if ((index>=38) and (index<=470)):
            if (a.attrs['href'] !='#top'):
                data[0].append ([a.attrs['href'], a.get_text()])
    except IndexError:
        print ("Exception Index Error")

    index=index+1

print (data[0])

for index in data[0]:
    print (index)

file_name = "vwo.csv"
bFileExist = os.path.isfile(file_name)

if not bFileExist:
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

with open(file_name, 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"')

    for index in data[0]:
        csv_writer.writerow([index[1], index[0]])
