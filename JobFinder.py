import requests
from bs4 import BeautifulSoup


def indeed():
    job_title = input('Please Enter Job-Title: ')
    url = f'https://www.indeed.com/jobs?q={job_title}&l='
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(id='resultsCol')
    job_elems = result.find_all('div', class_='jobsearch-SerpJobCard')

    for job_elem in job_elems:
        title = job_elem.find('h2', class_='title')
        company = job_elem.find('span', class_='company')
        location = job_elem.find('span', class_='location')
        summary = job_elem.find('div', class_='summary')
        date = job_elem.find('span', class_='date')
        link = job_elem.find('a')['href']
        if None in (title, company, location, summary):
            continue
        print()
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print(summary.text.strip())
        print(date.text.strip())
        print(f"Apply here: https://indeed.com{link}\n")


def monster():
    job_title = input('Please Enter Job-Title: ')

    url = f'https://www.monster.com/jobs/search/?q={job_title}&stpage=1&page=7'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    job_elems = results.find_all('section', class_='card-content')

    for job_elem in job_elems:
        title = job_elem.find('h2', class_='title')
        company = job_elem.find('div', class_='company')
        location = job_elem.find('div', class_='location')

        if None in (title, company, location):
            continue

        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print()

monster()
