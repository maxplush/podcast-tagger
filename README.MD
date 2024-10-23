# Podcast Transcription Scraper

This project scrapes podcast episode information from the Ethical Schools website, collects episode names, URLs, transcription URLs, and the corresponding text of the transcriptions. The data is stored in a CSV file for further analysis or processing.

## Features

- Scrapes episode names and URLs from the podcast episode page.
- Constructs transcription URLs based on the episode URLs.
- Extracts transcription text from the corresponding URLs.
- Stores the collected data in a CSV file for easy access.

## Requirements

To run this project, you need to pip install requirements.txt

```bash
pip install requirements.txt
```

## How to Use

1. Clone the repository or download the project files.
2. Update the script with any necessary configurations (e.g., URL paths).
3. Run the script to scrape the data:

   ```bash
   python app.py
   ```

4. After execution, the scraped data will be saved in `episodes_transcriptions.csv`.

## Data Structure

The CSV file contains the following columns:

- `episode_name`: The title of the podcast episode.
- `episode_url`: The URL of the podcast episode.
- `transcription_url`: The URL of the transcription page.
- `transcription_text`: The text content of the transcription.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
