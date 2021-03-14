from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.cdc.gov/publichealthgateway/accreditation/departments.html').text
soup = BeautifulSoup(source, "lxml")

#csv files
csv_file = open("cms_scrape.csv", "w")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["state \n link"])


departments = soup.find_all(class_ = "col-md-12")[2]

# print(departments.prettify())
# print(departments)
# print(departments.find_all('ul')[1].find_all('li')[1])


listOfStates_uls = departments.find_all('ul')
listOfStates_names = departments.find_all('p')
for state_index in range(len(listOfStates_names)):
    print(listOfStates_names[state_index].contents)
    for link in listOfStates_uls[state_index].find_all('li'):
        try: print(link.find('a')['href'])
        except TypeError: continue
    print("------------------------")


for state_index in range(len(listOfStates_names)):
  csv_writer.writerow([listOfStates_names[state_index].contents])
  for link in listOfStates_uls[state_index].find_all('li'):
        try: csv_writer.writerow([link.find('a')['href']])
        except TypeError: continue 


csv_file.close()