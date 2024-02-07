import os
from supabase import create_client, Client
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import re

def get_link_at_position(url, position):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    # Check if the specified position is valid
    if position >= len(links):
        raise IndexError("Position is out of range")

    # Get the link at the specified position
    link = links[position]['href']

    return link

# Use the function
url = "https://www.dsu.toscana.it/i-menu"  # replace with the URL you want to connect to
position = 66  # replace with the desired position (0-based index)
link = get_link_at_position(url, position)
corrLink=url+link
corrLink=re.sub(r'(\.pdf/).*$', r'\1', link)
# save the img at the link
response = requests.get(corrLink)
file = open("menu.pdf", "wb")
file.write(response.content)
file.close()


'''
<strong>Martiri</strong>&nbsp;&nbsp;<br>
<a href="/documents/4390857/16670109/MENSA+MARTIRI+4%C2%B0+sett.+05-11.02.2024.pdf">Menù dal 05.02.2024 al 11.02.2024</a>


load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
'''