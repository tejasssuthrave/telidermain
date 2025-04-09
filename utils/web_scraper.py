import trafilatura
import requests
from bs4 import BeautifulSoup

def get_website_text_content(url: str) -> str:
    """
    This function takes a url and returns the main text content of the website.
    The text content is extracted using trafilatura and easier to understand.
    
    Args:
        url: The URL of the webpage to scrape
        
    Returns:
        str: The extracted text content
    """
    try:
        # Send a request to the website
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(downloaded)
            if text:
                return text
        
        # Fallback to requests + BeautifulSoup if trafilatura fails
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text(separator='\n')
            
            # Remove excess whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
        
        return "Could not extract text from the website."
        
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def get_disease_info_from_web(disease_name: str) -> dict:
    """
    Search for information about a skin disease from reliable medical websites.
    
    Args:
        disease_name: The name of the skin disease to search for
        
    Returns:
        dict: Information about the disease including description, causes, symptoms, treatments
    """
    search_query = f"{disease_name} skin condition mayo clinic"
    
    # Priority websites for medical information
    priority_domains = [
        'mayoclinic.org',
        'aad.org',  # American Academy of Dermatology
        'medlineplus.gov',
        'nhs.uk',
        'healthline.com',
        'skincancer.org',
        'webmd.com'
    ]
    
    # Search for the disease on a reliable medical website
    try:
        # Use a simple approach to search for the disease
        for domain in priority_domains:
            url = f"https://www.{domain}/search?q={disease_name.replace(' ', '+')}"
            content = get_website_text_content(url)
            if content and len(content) > 500:  # Ensure we have meaningful content
                return {
                    'name': disease_name,
                    'description': f"Information about {disease_name} from {domain}:\n\n{content[:1000]}...",
                    'causes': extract_section(content, ['causes', 'cause', 'risk factors']),
                    'symptoms': extract_section(content, ['symptoms', 'signs', 'characteristics']),
                    'treatments': extract_section(content, ['treatment', 'therapy', 'management', 'how to treat']),
                    'when_to_see_doctor': extract_section(content, ['when to see a doctor', 'medical attention', 'seek care']),
                    'prevention': extract_section(content, ['prevention', 'prevent', 'reducing risk']),
                    'source': domain
                }
        
        # If no priority domain provided good content, return basic info
        return {
            'name': disease_name,
            'description': f"Information about {disease_name} was not found online. Please consult a dermatologist for details.",
            'causes': "Not available from online sources",
            'symptoms': "Not available from online sources",
            'treatments': "Not available from online sources",
            'when_to_see_doctor': "If you notice any unusual skin changes, consult a dermatologist.",
            'prevention': "Not available from online sources",
            'source': "No reliable source found"
        }
        
    except Exception as e:
        # Return a basic structure if scraping fails
        return {
            'name': disease_name,
            'description': f"Error retrieving information about {disease_name}. Please consult a dermatologist.",
            'causes': "Information retrieval error",
            'symptoms': "Information retrieval error",
            'treatments': "Information retrieval error",
            'when_to_see_doctor': "If you notice any unusual skin changes, consult a dermatologist.",
            'prevention': "Information retrieval error",
            'source': f"Error: {str(e)}"
        }

def extract_section(text, keywords):
    """
    Extract a specific section from text based on keywords.
    
    Args:
        text: The full text to search in
        keywords: List of keywords that might indicate the start of the relevant section
        
    Returns:
        str: The extracted section or a default message if not found
    """
    if not text:
        return "Not available"
    
    # Convert text to lowercase for case-insensitive search
    text_lower = text.lower()
    
    # First try to find sections by looking for the keywords followed by ":"
    for keyword in keywords:
        # Search for patterns like "Causes:" or "Symptoms:"
        search_pattern = f"{keyword}:"
        if search_pattern in text_lower:
            start_idx = text_lower.find(search_pattern)
            # Find the start of the next section (or end of text)
            end_markers = ['\n\n', '\r\n\r\n', '. ', '.\n']
            end_idx = len(text)
            for marker in end_markers:
                next_marker = text.find(marker, start_idx + len(search_pattern))
                if next_marker != -1 and next_marker < end_idx:
                    end_idx = next_marker + len(marker)
            
            extract = text[start_idx:end_idx].strip()
            if len(extract) > 20:  # Ensure we have meaningful content
                return extract
    
    # If section headers weren't found, try to extract sentences containing the keywords
    sentences = []
    for keyword in keywords:
        if keyword in text_lower:
            # Find all sentences containing the keyword
            for sentence in text.split('.'):
                if keyword in sentence.lower():
                    sentences.append(sentence.strip() + '.')
    
    if sentences:
        return ' '.join(sentences[:3])  # Return up to 3 most relevant sentences
    
    return "Not available from the source"