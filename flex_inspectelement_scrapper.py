import requests
from bs4 import BeautifulSoup
url="https://flexstudent.nu.edu.pk/Login"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

print(soup)



