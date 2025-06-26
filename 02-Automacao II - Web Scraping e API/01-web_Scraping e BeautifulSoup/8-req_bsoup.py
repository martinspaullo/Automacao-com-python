import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1 - Coletando Vagas Python
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
print(jobs[:3])
print(len(jobs))

companys = []
skills = []
pub_date = []
# 2 - Estruturando informações
for job in jobs[:20]:
    name_company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skill = job.find('li', class_='job-description__').text.replace(' ', '')
    published_date = job.find('span', class_='sim-posted').span.text[7:]
    print(name_company.strip())
    print(skill)
    print(published_date)
    
# 3 - Exportando Informações para CSV
    companys.append(name_company.strip())
    skills.append(skill.strip())
    pub_date.append(published_date)
    
python_vagas = pd.DataFrame()
python_vagas['companys'] = companys
python_vagas['skills'] = skills
python_vagas['pub_date'] = pub_date
python_vagas.to_csv('python_vagas.csv')
