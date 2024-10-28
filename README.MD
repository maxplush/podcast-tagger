# Podcast Scraper

This project scrapes podcast episode information from the Ethical Schools website and uses the Groq API to extract relevant tags for each episode. The scraped data is saved in a CSV file for easy access and analysis.

## Features

- Scrapes the latest podcast episode URLs from the Ethical Schools website.
- Retrieves and cleans the episode content and transcription.
- Utilizes the Groq API to extract relevant tags from the episode content.
- Saves the episode names, URLs, and extracted tags in a CSV file.

## Requirements

To run this project, you need to pip install requirements.txt

```bash
pip install requirements.txt
```

## Prerequisites

- Before running the script, make sure you have the packages listed in the requirements.txt file.
- A `.env` file in the same directory containing your  [Groq API KEY](https://groq.com). The file should have the following format:
  
  ```env
  GROQ_API_KEY=your_groq_api_key_here

- Ensure your .env file is configured correctly with your Groq API key. Connect your .env by running the command.

```
$ export $(cat .env)
```
## Usage

1. Clone the repository or download the project files.
2. Update the script with any necessary configurations (e.g., URL paths).
3. Run the script to scrape the data:

   ```bash
   python3 aiapp.py
   ```

4. After execution, the scraped data will be saved in `episodes_transcriptions.csv`.

## Data Structure

The CSV file contains the following columns:

- `episode_name`: The title of the podcast episode.
- `episode_url`: The URL of the podcast episode.
- `tag`: LLM generated tag of the podcast episode. 


