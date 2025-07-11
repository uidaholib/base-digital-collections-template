#!/usr/bin/env python3
"""
Script to extract ABSTRACT and BIOGRAPHY sections from HTML files in the turning/ directory
and save them to a CSV file.
"""

import os
import re
import csv
from bs4 import BeautifulSoup
from pathlib import Path


def extract_section_content(soup, section_heading):
    """
    Extract content following a specific h2 heading until the next h2 or end of content.
    
    Args:
        soup: BeautifulSoup object of the HTML
        section_heading: The text content of the h2 heading to find
    
    Returns:
        tuple: (clean_text, html_content) - both versions of the content
    """
    # Find the h2 element with the specified text
    h2_element = soup.find('h2', string=section_heading)
    
    if not h2_element:
        return "", ""
    
    clean_content_parts = []
    html_content_parts = []
    
    # Get all siblings after the h2 element until we hit another h2 or end
    for sibling in h2_element.find_next_siblings():
        if sibling.name == 'h2':
            # Stop when we hit the next h2
            break
        elif sibling.name == 'p':
            # Extract clean text from paragraph
            clean_text = sibling.get_text(strip=True)
            if clean_text:  # Only add non-empty paragraphs
                clean_content_parts.append(clean_text)
            
            # Extract HTML content (convert back to string, removing outer <p> tags)
            html_content = str(sibling)
            if html_content:
                html_content_parts.append(html_content)
    
    # Join paragraphs
    clean_result = '\n\n'.join(clean_content_parts)
    html_result = '\n'.join(html_content_parts)
    
    return clean_result, html_result


def extract_eventdate(soup):
    """
    Extract content from p element with class "eventdate".
    
    Args:
        soup: BeautifulSoup object of the HTML
    
    Returns:
        str: The eventdate text or empty string if not found
    """
    eventdate_element = soup.find('p', class_='eventdate')
    if eventdate_element:
        return eventdate_element.get_text(strip=True)
    return ""


def extract_person_title(soup):
    """
    Extract content from span element with class "prof".
    
    Args:
        soup: BeautifulSoup object of the HTML
    
    Returns:
        str: The person title text or empty string if not found
    """
    prof_element = soup.find('span', class_='prof')
    if prof_element:
        return prof_element.get_text(strip=True)
    return ""


def process_html_file(file_path):
    """
    Process a single HTML file and extract abstract, biography sections, eventdate, and person title.
    
    Args:
        file_path: Path to the HTML file
    
    Returns:
        tuple: (filename, eventdate, person_title, clean_abstract, clean_biography, html_abstract, html_biography)
    """
    filename = os.path.basename(file_path)
    # Remove .html extension and convert to lowercase
    filename_clean = filename.replace('.html', '').lower()
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract eventdate and person title
        eventdate = extract_eventdate(soup)
        person_title = extract_person_title(soup)
        
        # Extract abstract and biography sections (both clean and HTML versions)
        clean_abstract, html_abstract = extract_section_content(soup, 'ABSTRACT')
        clean_biography, html_biography = extract_section_content(soup, 'BIOGRAPHY')
        
        return filename_clean, eventdate, person_title, clean_abstract, clean_biography, html_abstract, html_biography
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return filename_clean, "", "", "", "", "", ""


def main():
    """Main function to process all HTML files and create CSV output."""
    
    # Set up paths
    turning_dir = Path('/Users/devinbecker/Documents/GitHub/base-digital-collections-template/turning')
    output_file = Path('/Users/devinbecker/Documents/GitHub/base-digital-collections-template/abstracts_biographies.csv')
    
    # Check if turning directory exists
    if not turning_dir.exists():
        print(f"Directory not found: {turning_dir}")
        return
    
    # Get all HTML files in the turning directory
    html_files = list(turning_dir.glob('*.html'))
    
    if not html_files:
        print(f"No HTML files found in {turning_dir}")
        return
    
    print(f"Found {len(html_files)} HTML files to process...")
    
    # Process files and collect results
    results = []
    
    for file_path in sorted(html_files):
        print(f"Processing: {file_path.name}")
        filename_clean, eventdate, person_title, clean_abstract, clean_biography, html_abstract, html_biography = process_html_file(file_path)
        results.append([filename_clean, eventdate, person_title, clean_abstract, clean_biography, html_abstract, html_biography])
    
    # Write results to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Write header
        writer.writerow(['filename', 'eventdate', 'person_title', 'abstract_clean', 'biography_clean', 'abstract_html', 'biography_html'])
        
        # Write data
        writer.writerows(results)
    
    print(f"\nResults saved to: {output_file}")
    print(f"Processed {len(results)} files total.")
    
    # Show summary of files with content
    files_with_abstract = sum(1 for row in results if row[3].strip())
    files_with_biography = sum(1 for row in results if row[4].strip())
    files_with_eventdate = sum(1 for row in results if row[1].strip())
    files_with_person_title = sum(1 for row in results if row[2].strip())
    
    print(f"Files with ABSTRACT section: {files_with_abstract}")
    print(f"Files with BIOGRAPHY section: {files_with_biography}")
    print(f"Files with EVENTDATE: {files_with_eventdate}")
    print(f"Files with PERSON_TITLE: {files_with_person_title}")


if __name__ == "__main__":
    main()
