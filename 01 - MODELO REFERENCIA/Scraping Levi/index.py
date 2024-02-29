import json
import requests
from bs4 import BeautifulSoup
from typing import List
from schema import JobPost
from ai import prompt
from parse import jsonify, extract_json

if __name__ == "__main__":
    headers =  {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1"
               }

    #response = requests.get('https://jobs.apple.com/en-us/search?location=mexico-MEXC', headers=headers)

    base_url = "https://jobs.apple.com"

    with open('response.html', 'r') as f:
        page = BeautifulSoup(f, 'html.parser')

        table = page.select_one('#tblResultSet')

        if table:
            for row in table.findChildren('tbody'):
                a_tag = row.findChild('tr').findChild('td').findChild('a')
                with open(f'{a_tag.text}.html', 'r+') as job_post:
                    # response = requests.get(base_url+a_tag.get('href'), headers = headers)
                    # job_post.write(response.text)
                    print(a_tag['href'])
                    detail = BeautifulSoup(job_post, 'html.parser')
                    description = detail.select_one('#jd-job-summary')

                    # title = detail.select_one('#jdPostingTitle')
                    tags_with_itemprop = detail.findAll(lambda tag: tag.get('itemprop'))

                    job_post_info = { tag['itemprop']: tag.text for tag in tags_with_itemprop }
                    job_post_info['country'] = job_post_info.pop('addressCountry', None)
                    job_post_info['city'] = job_post_info.pop('adressRegion', None)
                    job_post_info['createdAt'] = job_post_info.pop('datePosted', None)
                    job_post_info['name'] = job_post_info.pop('title', None)

                    if description:
                        job_post_info['description'] = description.get_text().replace('\n', ' ')

                        parsed_job_post = JobPost.parse_obj(job_post_info)

                        if parsed_job_post.description:
                            result = extract_json((parsed_job_post.description))

                            # TODO: Process result when openai  

                        with open(f'{a_tag.text}.json', 'w') as json_file :
                            json_file.write(jsonify(dict(parsed_job_post)))
