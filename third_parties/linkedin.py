import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock:bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/zganjei/73528c9e7ec73295580ac577c6cd0d04/raw/2750e19851cdc25fdf86d356de0d61fa7723c75c/borje-ekholm-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,)
    else:
        api_endpoint = "https://api.scrapin.io/enrinchment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,)
        
    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in [[], "", "",]
        and k not in ["certifications"]
    }
    return data


if __name__ == "__main__":
    # Example usage
    linkedin_profile_url = "https://www.linkedin.com/in/borje-ekholm/"
    profile_data = scrape_linkedin_profile(linkedin_profile_url,True)
    print(profile_data)