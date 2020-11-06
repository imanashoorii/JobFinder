from bs4 import BeautifulSoup
import requests
def search():
    search = input("name : ")
    #models.Search.objects.create(search=search)
    url = 'https://www.indeed.com/jobs?q={}&l='
    final_url = url.format(search)
    page = requests.get(final_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(id='resultsCol')
    job_elems = result.find_all('div', class_='jobsearch-SerpJobCard')

    final_posting = []
    for job_elem in job_elems:
        title = job_elem.find('h2', class_='title')
        company = job_elem.find('span', class_='company')
        location = job_elem.find('span', class_='location')
        summary = job_elem.find('div', class_='summary')
        date = job_elem.find('span', class_='date')
        link = job_elem.find('a')['href']
        if None in (title, company, location, summary):
            continue
        # print()
        # print(title.text.strip())
        # print(company.text.strip())
        # print(location.text.strip())
        # print(summary.text.strip())
        # print(date.text.strip())
        # print(f"Apply here: https://indeed.com{link}\n")
        final_title = title.text.strip()
        final_company = company.text.strip()
        final_location = location.text.strip()
        final_summary = summary.text.strip()
        final_date = date.text.strip()
        #print(f"Apply here: https://indeed.com{link}\n")
        final_link = f"Apply here: https://indeed.com{link}\n"

        #final_posting.append((final_title, final_company, final_location, final_summary, final_date, final_link))

        print(final_link)

search()