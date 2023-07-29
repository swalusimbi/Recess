# Introduction to web scraping with beautiful soup
"""
- Extracting information from a website using Beautiful soup and parsing the html and XML code of the web pages.

# Install beautiful soup.
    pip install beautifulsoup4

"""

#  Importing libraries
from bs4 import BeautifulSoup
import requests         #  fetches the HTML content from a webpage
import json

#  URL of the website
# url = "https://xeno-canto.org/"

# response = requests.get(url)    #  returns a response object

# soup = BeautifulSoup(response.content, "html.parser")

#  Get title of the webpage
# title = soup.title
# print(title)

# Get all the links on the webpage
# links = soup.find_all("a")
# print(links)


# Assignment
# Use the API to get data. The endpoint for the webservice is at https://xeno-canto.org/api/2/recordings.
# 1. Extract all the bird species from the website. Generate the csv/json file for the bird species, family and more.

def get_bird_species_data(query):
    url = f"https://xeno-canto.org/api/2/recordings?query={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        bird_species_list = []

        for recording in data['recordings']:
            species_name = recording['en']
            family_name = f"{recording['gen']} {recording['sp']}"
            locality = recording['loc']
            country = recording['cnt']

            # Append the information to the list in the form of a dictionary.
            bird_species_list.append({
                'species_name': species_name,
                'family_name': family_name,
                'locality': locality,
                'country': country,
            })

        return bird_species_list
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    # Get data for bird species in Uganda
    query = "cnt:Uganda"
    bird_species_data = get_bird_species_data(query)

    if bird_species_data:
        json_filename = "bird_species.json"
        with open(json_filename, 'w') as json_file:
            json.dump(bird_species_data, json_file, indent=4)
        print(f"Data saved to {json_filename}.")
    else:
        print("No data retrieved.")



# 2. Extract all the bird songs from the website.

def get_all_bird_songs():
    base_url = "https://xeno-canto.org/api/2/recordings"
    page = 1
    bird_songs = []

    while True:
        url = f"{base_url}?query=X&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_recordings = int(data['numRecordings'])
            num_pages = int(data['numPages'])

            for recording in data['recordings']:
                bird_songs.append({
                    'song_name': recording['en'],
                    'bird_family': f"{recording['gen']} {recording['sp']}",
                    'locality': recording['loc'],
                    'country': recording['cnt'],
                    'audio_url': recording['file']
                })

            if len(bird_songs) >= total_recordings:
                break

            page += 1
        else:
            print(f"Failed to fetch data for page {page}. Status code: {response.status_code}")
            break

    return bird_songs

if __name__ == "__main__":
    bird_songs_data = get_all_bird_songs()

    if bird_songs_data:
        json_filename = "bird_songs.json"
        with open(json_filename, 'w') as json_file:
            json.dump(bird_songs_data, json_file, indent=4)
        print(f"Data saved to {json_filename}.")
    else:
        print("No data retrieved.")

