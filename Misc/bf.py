import requests
from bs4 import BeautifulSoup
url='https://www.tripadvisor.com/Restaurant_Review-g293891-d23739197-Reviews-Soul_Origin_Cafe_and_Restaurant-Pokhara_Gandaki_Zone_Western_Region.html'
div_class='SrqKb'
response = requests.get(url)
html_content=response.content
soup = BeautifulSoup(html_content,'html-parser')
div_element = soup.find('div',{'class':div_class})
div_text=div_element.get_text(strip=True)
print(div_text)
print('hello')