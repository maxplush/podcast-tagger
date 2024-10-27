import requests
from bs4 import BeautifulSoup
import csv
import re

# Base URL for the podcast episodes page
URL = "https://ethicalschools.org/category/podcast-episode/"

def get_episode_urls(limit=5):
    # Send a request to the main page
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get the first few episode URLs
    episode_urls = [link['href'] for link in soup.find_all('a', class_='more-link')[:limit]]
    return episode_urls

# Function to scrape episode name and transcription text from the transcription URL
def scrape_episode_content(episode_url):
    try:
        # Send a request to the transcription URL
        response = requests.get(episode_url)
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
        print(f"Error scraping {episode_url}: {e}")
        return "N/A", "N/A"


# Function to save episode details to CSV
def save_to_csv(episode_data, filename='episodes_transcriptions.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Episode Name', 'Episode URL', 'Transcription Text'])
        
        # Fetch and write details for each episode
        for episode_url in episode_data:
            episode_name, transcription_text = scrape_episode_content(episode_url)
            writer.writerow([episode_name, episode_url, transcription_text])
            print(f"Saved data for episode: {episode_name}")

# Main script
if __name__ == "__main__":
    # Step 1: Get episode URLs (first 5 episodes for testing)
    episode_urls = get_episode_urls(limit=5)
    
    # Step 2: Save the data (episode name, URL, transcription text) to CSV
    save_to_csv(episode_urls)

# TODO:
# RAG summaries of each of the text content
# TAG the summaries
# Output DB with tags for each episode
