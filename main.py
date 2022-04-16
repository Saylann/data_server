
import requests 
from bs4 import BeautifulSoup 

  
url = "https://saylann.github.io/data_server/"
  
response = requests.get(url) 
  
soup = BeautifulSoup(response.text, 'html.parser') 
  
links = soup.find_all('a') 
  
i = 0
  
for link in links: 
    if ('.exe' in link.get('href', [])): 
        i += 1
        print("Downloading file: ", i) 

        response = requests.get(link.get('href')) 


        
        pdf = open("hack"+str(i)+"", 'wb') 
        pdf.write(response.content) 
        pdf.close() 
        print("File ", i, " downloaded") 
  
print("All data files downloaded")