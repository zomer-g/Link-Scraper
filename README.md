# Link-Scraper
This Python script is a web crawler designed to extract all links from a specified domain, including internal and external links. It processes each page recursively, ensuring that no link is visited more than once. The extracted links are saved to a CSV file for further analysis.

## Features
- Extracts links from a specified website.
- Categorizes links as internal or external.
- Checks the validity of links (valid or broken).
- Skips unsupported link types like `mailto:` and `tel:`.
- Avoids revisiting already mapped URLs to optimize performance.
- Saves the data to a CSV file with details such as source URL, page title, link text, link type, and link status.

## Requirements
- Python 3.6 or higher
- Libraries:
  - `requests`
  - `BeautifulSoup` (from `bs4`)
  - `csv`
  - `urllib`

Install the required libraries using pip:
```bash
pip install requests beautifulsoup4
```

## How to Use
1. **Set the Start URL**:
   Update the `start_url` variable in the script with the desired starting point. For example:
   ```python
   start_url = "https://example.com/"
   ```

2. **Run the Script**:
   Execute the script in your Python environment:
   ```bash
   python link_scraper.py
   ```

3. **Output**:
   The script generates a CSV file named `all_links.csv` in the same directory. The file contains the following columns:
   - `Source URL`: The URL of the page where the link was found.
   - `Page Title`: The title of the source page.
   - `Link Text`: The anchor text of the link.
   - `Link URL`: The URL of the link.
   - `Link Type`: Indicates whether the link is internal or external.
   - `Link Status`: Indicates whether the link is valid or broken.

## Example Output
Example content of `all_links.csv`:
```
Source URL,Page Title,Link Text,Link URL,Link Type,Link Status
https://example.com/,Home,Contact Us,https://example.com/contact,Internal,Valid
https://example.com/,Home,Facebook,https://www.facebook.com/example,External,Valid
```

## Customization
- **Domain Filtering**: The script currently limits crawling to the specified domain. Adjust the domain check in the `extract_links` function if needed.
- **Output File Name**: Change the `output_file` variable to customize the output file name.
- **Timeouts**: Modify the timeout value in the `requests.head` call to adjust how long the script waits for a response.

## Error Handling
- Links that cannot be accessed are marked as "Broken" in the CSV file.
- The script logs errors and skips unsupported protocols like `mailto:` and `tel:`.

## Notes
- The script is designed for ethical use. Ensure you have permission to crawl the target website.
- Avoid running the script on websites with restrictive rate-limiting or anti-crawling measures.
- This script was written by an AI language model (LLM) and may require adjustments for specific use cases.

## License
This script is provided as-is without warranty. Use at your own risk.

