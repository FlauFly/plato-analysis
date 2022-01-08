import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def load_page(url):
    url = fix_string(url)
    response = requests_retry_session().get(url, timeout=5)
    raw_html = response.text
    html = BeautifulSoup(raw_html, 'html.parser')
    return html

def fix_string(text):
    if ('//' in text):
        dummy = list(text)
        dummy = dummy[3:]
        text = "entries" + "".join(dummy)
    elif ('..' in text):
        # Usuwam '..' z text
        dummy = list(text)
        dummy = dummy[2:]
        text = "entries" + "".join(dummy)
        # Dodaje entries przed poprawiony text
    # Dodaje 'https://plato.stanford.edu/'
    text = 'https://plato.stanford.edu/' + text
    return text

# Ładuję spis treści
html = load_page('contents.html')

# Biorę wszystkie tagi 'strong'
topics = html.find_all('strong')

# Wyciagam z wszystkich tagow linki
def take_links_from_tags(topics):
    # Zdefiniuj zbior adresow
    links = []
    for topic in topics:
        link = topic.find_parent('a')['href']
        # Dodaj element do zbioru adresow
        links.append(link)
    return links

def download_page_data(link):
    # Otwieram stronę
    page = load_page(link)
    
    # Find title of the page
    title = page.h1.string
    if title is None:
        strings = [string for string in page.h1.strings]
        title = ''.join(strings)
        
    # Find links to related articles
    rel = page.find(id='related-entries')
    links = rel.p.find_all('a')
    links = [link['href'] for link in links]
    links = [fix_string(text) for text in links]
    
    return (title, links)

df = pd.DataFrame()
link_title_table = {}
links = take_links_from_tags(topics)
for link in links:
    title, related_links = download_page_data(link)
    link_title_table[fix_string(link)] = title
    print(title) # For tracking purposes
    for related in related_links:
        df = df.append({'From': title, 'To': related}, ignore_index=True)

df = df.replace(link_title_table)
df.to_csv('data.csv', index=False)
