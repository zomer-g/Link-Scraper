# Import required libraries
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlparse

# Function to extract all links from a website
def extract_links(url, visited, domain):
    links_data = []  # List to store link details

    try:
        if url in visited:
            print(f"Skipping already visited URL: {url}")
            return links_data

        print(f"Fetching the website: {url}")
        response = requests.get(url)
        visited.add(url)

        # Check if the request was successful
        if response.status_code == 200:
            print(f"Website fetched successfully. Parsing content: {url}")
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract page title
            page_title = soup.title.string if soup.title else "No Title"

            # Find all <a> tags with href attribute
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                link_text = a_tag.get_text(strip=True)

                # Skip mailto and tel links
                if href.startswith(('mailto:', 'tel:')):
                    print(f"Skipping unsupported link type: {href}")
                    continue

                # Normalize relative links
                if not href.startswith(('http://', 'https://')):
                    href = requests.compat.urljoin(url, href)

                # Check if the link is within the main domain
                parsed_href = urlparse(href)
                if parsed_href.netloc and parsed_href.netloc != domain:
                    link_type = "External"
                else:
                    link_type = "Internal"

                # Add the link only if it hasn't been visited yet
                if href not in visited:
                    # Check if the link is broken
                    try:
                        link_response = requests.head(href, timeout=5)
                        link_status = "Broken" if link_response.status_code >= 400 else "Valid"
                    except Exception as e:
                        link_status = "Broken"

                    links_data.append({
                        'Source URL': url,
                        'Page Title': page_title,
                        'Link Text': link_text,
                        'Link URL': href,
                        'Link Type': link_type,
                        'Link Status': link_status
                    })

        else:
            print(f"Failed to fetch the website. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while processing URL {url}: {e}")

    return links_data

# Recursive function to crawl and map links
def crawl_website(start_url):
    visited = set()
    all_links = []
    queue = [start_url]
    domain = urlparse(start_url).netloc

    while queue:
        current_url = queue.pop(0)
        print(f"Mapping page: {current_url}")
        links = extract_links(current_url, visited, domain)
        all_links.extend(links)

        for link in links:
            if link['Link Type'] == "Internal" and link['Link URL'] not in visited:
                queue.append(link['Link URL'])

    return all_links

# URL of the target website
start_url = input("Enter the start URL (e.g., https://example.com/): ").strip()

# Crawl the website and extract all links
all_links = crawl_website(start_url)

# Save links to a CSV file
output_file = "all_links.csv"
try:
    print(f"Writing links to {output_file}...")
    with open(output_file, "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Source URL', 'Page Title', 'Link Text', 'Link URL', 'Link Type', 'Link Status'])
        writer.writeheader()
        writer.writerows(all_links)
    print(f"Links successfully saved to {output_file}.")
except Exception as e:
    print(f"An error occurred while writing to file: {e}")
