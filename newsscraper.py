
import requests
from bs4 import BeautifulSoup


url = "https://www.indiatoday.in/" 

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


headlines = soup.find_all(['h3', 'h2'])


headline_list = []
for tag in headlines:
    title = tag.get_text(strip=True)  
    if title and title not in headline_list:  
        headline_list.append(title)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headline_list, start=1):
        file.write(f"{i}. {headline}\n")  

print("✅ All headlines saved in 'headlines.txt'")
