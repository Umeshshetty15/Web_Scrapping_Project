import pandas as pd
from bs4 import BeautifulSoup
import requests
import pandas

url = 'https://www.worlddata.info/largest-economies.php'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

tables = soup.find_all('table', 'std100 hover tabsort sticky')
# print(table)

titlefind = soup.find_all('th', 'left')
titlefind1 = soup.find_all('th', 'right')
res = titlefind + titlefind1
# print(res)

world_title = [title.text.strip() for title in res]
print(world_title)

df = pd.DataFrame(columns= world_title)

# tables = soup.find_all('table', 'std100 hover tabsort sticky')
# data = []
for table in tables:
    rows = table.find_all('tr')

    for row in rows[1:]:
        rowdata = row.find_all('td')
        individualdata = [data.text.strip() for data in rowdata]
        print(individualdata)
        length = len(df)
        df.loc[length] = individualdata


df.to_csv(r'C:\Users\Chandrashekar\Desktop\Umesh V\PYTHON CLASS\API\web scrapping project\Output\economy.csv', index= False)







