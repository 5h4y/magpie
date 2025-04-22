import requests
from bs4 import BeautifulSoup
import os

url = input("Enter the base url: ")

if not url.endswith('/'):
    url += '/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    # search for hyperlink tags
    links = soup.find_all('a')

    # filter links (and exclude if necessary) by file ext
    grab_links = [os.path.join(url, link['href']) for link in links if 'href' in link.attrs and
                   (link['href'].endswith('mp3'))] # and not link['href'].endswith('example.mp4')]

    # write to text file
    with open('urls.txt', 'w') as f:
        for link_match in grab_links:
            f.write(link_match + '\n')

    print("Matching links have been saved to urls.txt")

    # just in case, wget instructions
    print("\nTo download files recursively, disable robots.txt, and limit requests to 5 per second, use the following wget command:")
    print(f"wget -i urls.txt --wait=0.2 --limit-rate=5 --random-wait --no-robots")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")