from bs4 import BeautifulSoup
import requests
import re

'''
# Program that checks if there is a job listing for IT APP DEV/SUP ANALYST I in the county of Santa Cruz.
'''
data = []
scc_jobs = 'https://www.jobapscloud.com/SCRUZ/'

# Get the information from the Santa Cruz County job board
scc_jobs_object = requests.get(scc_jobs)
scc_jobs_text = scc_jobs_object.text


scc_jobs_soup = BeautifulSoup(scc_jobs_text, 'html.parser')

# Find everything witht the class JobTitle from the HTML
for jobs in scc_jobs_soup.find_all('a', class_ = 'JobTitle'):
    data.append(jobs)

job_list = []
bad = ['amp;', '<br/>']
for i in range(2, len(data)):
    # Convert the HTML tag to a string
    job = str(data[i])
    # Search for everything in between the '>' and ' <'
    result = re.search('>(.*) <', job)
    new_job = result.group(1)

    # Check if the string of jobs contain any of the bad characters
    if bad[0] in new_job and bad[1] in new_job:
        new_job = new_job.replace(bad[0], '')
        new_job = new_job.replace(bad[1], ' ')
    elif bad[0] in new_job:
        new_job = new_job.replace(bad[0], '')
    elif bad[1] in new_job:
        new_job = new_job.replace(bad[1], ' ')
    job_list.append(new_job)

# Check if a job listing is currently open
if any('IT APP DEV/SUP ANALYST I' in job for job in job_list):
    print('true')
else:
    print('No jobs :(')



 
