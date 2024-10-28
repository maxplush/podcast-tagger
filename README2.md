
# Podcast Scraper

This project scrapes podcast episode information from the Ethical Schools website and uses the Groq API to extract relevant tags for each episode. The scraped data is saved in a CSV file for easy access and analysis.

## Features

- Scrapes the latest podcast episode URLs from the Ethical Schools website.
- Retrieves and cleans the episode content and transcription.
- Utilizes the Groq API to extract relevant tags from the episode content.
- Saves the episode names, URLs, and extracted tags in a CSV file.

## Requirements

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library
- `groq` library
- Access to the Groq API (API key required)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4 groq
   ```

3. Set up your Groq API key in your environment variables:

   ```bash
   export GROQ_API_KEY='your_api_key_here'
   ```

## Usage

Run the script to scrape the latest podcast episodes and save the tags to a CSV file:

```bash
python aiapp.py
```

The CSV file will be saved at the specified location (default: `/Users/maxplush/Documents/podcastscraper/ai-tag-episodes.csv`).
