from bs4 import BeautifulSoup
import requests
import time
import os

print('Put some skill that you are not familiar with:')
unfamiliar_skill = input('> ')
print(f"Filtering out '{unfamiliar_skill}'...")

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    ).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if '' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills_tag = job.find('span', class_='srp-skills')
            if not skills_tag:
                continue  # skip this job listing if skills are not found
            print(skills_tag)
            skills = skills_tag.text.strip().lower()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill.lower() not in skills:
                print(f"\nCompany Name: {company_name}")
                print(f"Required Skills: {skills}")
                print(f"More Info: {more_info}")

                with open(f'posts/job_{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")
                    f.write("\n")

if __name__ == '__main__':
    if not os.path.exists('posts'):
        os.makedirs('posts')
    while True:
        find_jobs()
        time_wait = 10  # minutes
        print(f"\nWaiting {time_wait} minutes before next check...\n")
        time.sleep(time_wait * 1)
