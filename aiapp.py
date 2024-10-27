import requests
from bs4 import BeautifulSoup
import csv
import os
import re
import groq

# Base URL for the podcast episodes page
URL = "https://ethicalschools.org/category/podcast-episode/"

# Groq API client setup
client = groq.Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Function to get episode URLs
def get_episode_urls(limit=5):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    episode_urls = [link['href'] for link in soup.find_all('a', class_='more-link')[:limit]]
    return episode_urls

# Function to scrape episode content
def scrape_episode_content(episode_url):
    response = requests.get(episode_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    episode_name_tag = soup.find('h1', class_='blog-page-title')
    episode_name = episode_name_tag.text.strip() if episode_name_tag else "N/A"
    
    transcription_text = ""
    for paragraph in soup.find_all('p'):
        text = paragraph.text.strip()
        if any(keyword in text.lower() for keyword in ["download file", "subscribe:", "transcript", "references", "soundtrack"]):
            continue
        transcription_text += text + "\n"
    
    transcription_text = re.sub(r'\b\d{2}:\d{2}\b', '', transcription_text)
    
    return episode_name, transcription_text.strip()

# Function to run Groq API for tags extraction
def extract_tags_with_groq(episode_name, transcription_text):
    system = "You are a podcast listener. Please provide only the top 5 relevant tags for the podcast in comma-separated values without any additional text."
    user = f"Episode name: {episode_name}\n\nTranscript:\n{transcription_text}"
    
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': system},
            {"role": "user", "content": user}
        ],
        model='llama3-8b-8192'
    )
    
    return chat_completion.choices[0].message.content.split('\n')  # Assuming tags are returned as a list

# Function to save tags to CSV
def save_tags_to_csv(data, filename='/Users/maxplush/Documents/podcastscraper/newtags.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Episode Name', 'Episode URL', 'Tags'])
        
        for episode_url in data:
            episode_name, transcription_text = scrape_episode_content(episode_url)
            tags = extract_tags_with_groq(episode_name, transcription_text)
            writer.writerow([episode_name, episode_url, ', '.join(tags)])
            print(f"Tags for episode '{episode_name}' saved.")

# Main function
if __name__ == "__main__":
    episode_urls = get_episode_urls(limit=5)
    save_tags_to_csv(episode_urls)