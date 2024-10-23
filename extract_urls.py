import requests
from bs4 import BeautifulSoup

# Base URL for the podcast episodes page
URL = "https://ethicalschools.org/category/podcast-episode/"

# Function to scrape "Read More" links and generate transcription URLs
def get_read_more_and_transcription_urls():
    # Send a request to the page
    response = requests.get(URL)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize a list to store the episode and transcription URLs
    episode_links = []
    
    # Find all "Read More" links
    for link in soup.find_all('a', class_='more-link'):
        # Extract the URL from the "Read More" link
        episode_url = link['href']
        
        # Construct the transcription URL by appending 'transcript' to the episode URL
        transcription_url = episode_url.replace("ethicalschools.org", "0da.6f4.myftpupload.com").replace('/podcast-episode/', '/transcript-of-the-episode/')
        
        # Add the details to the list
        episode_links.append({
            'episode_url': episode_url,
            'transcription_url': transcription_url
        })
    
    return episode_links

# Run the function and print the results
if __name__ == "__main__":
    links = get_read_more_and_transcription_urls()
    for link in links:
        print(f"Episode URL: {link['episode_url']}")
        print(f"Transcription URL: {link['transcription_url']}\n")

