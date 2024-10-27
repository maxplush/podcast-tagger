import requests
from bs4 import BeautifulSoup
import csv
import re

# Base URL for the podcast episodes page
URL = "https://ethicalschools.org/category/podcast-episode/"

# Function to scrape "Read More" links and generate transcription URLs
def get_read_more_and_transcription_urls(limit=5):
    # Send a request to the page
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize a list to store the episode and transcription URLs
    episode_links = []
    
    # Find all "Read More" links and limit to the first `limit` items
    for link in soup.find_all('a', class_='more-link')[:limit]:
        episode_url = link['href']
        transcription_url = episode_url.replace("ethicalschools.org", "0da.6f4.myftpupload.com").replace('/podcast-episode/', '/transcript-of-the-episode/')
        
        episode_links.append({
            'episode_url': episode_url,
            'transcription_url': transcription_url
        })
    
    return episode_links

# Function to scrape episode name and transcription text from the transcription URL
def scrape_transcription(transcription_url):
    try:
        # Send a request to the transcription URL
        response = requests.get(transcription_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the episode name from the <h1> tag with class 'blog-page-title'
        episode_name_tag = soup.find('h1', class_='blog-page-title')
        episode_name = episode_name_tag.text.strip() if episode_name_tag else "N/A"
        
        # Extract the transcription text
        transcription_text = ""
        for paragraph in soup.find_all('p'):
            text = paragraph.text.strip()
            
            # Filter out unwanted lines
            if any(keyword in text.lower() for keyword in ["download file", "subscribe:", "transcript", "references", "soundtrack"]):
                continue
            transcription_text += text + "\n"
        
        # Remove any extra patterns like timestamps, etc., if needed
        transcription_text = re.sub(r'\b\d{2}:\d{2}\b', '', transcription_text)  # Remove timestamps like 00:00
        
        return episode_name, transcription_text.strip()
    
    except Exception as e:
        print(f"Error scraping {transcription_url}: {e}")
        return "N/A", "N/A"


# Function to store episode details and transcription in a CSV file
def save_to_csv(episodes_data, filename='episodes_transcriptions.csv'):
    # Open the file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Episode Name', 'Episode URL', 'Transcription URL', 'Transcription Text'])
        
        # Iterate through the episodes and fetch the transcription data
        for episode in episodes_data:
            episode_url = episode['episode_url']
            transcription_url = episode['transcription_url']
            
            # Scrape the episode name and transcription text
            episode_name, transcription_text = scrape_transcription(transcription_url)
            
            # Write the episode details to the CSV
            writer.writerow([episode_name, episode_url, transcription_url, transcription_text])
            print(f"Saved data for episode: {episode_name}")

# Main function to combine scraping URLs and transcription text
if __name__ == "__main__":
    # Step 1: Get all episode and transcription URLs
    episode_links = get_read_more_and_transcription_urls(limit=5)
    
    # Step 2: Save the data (episode name, URL, transcription URL, transcription text) to CSV
    save_to_csv(episode_links)

# TODO:
# clean up hmtl scraped content (have it just be the overview? or the text content)
# create a database of the tags(with other columns)
# RAG summaries of each of the text content
# TAG the summaries
# Output DB with tags for each episode
