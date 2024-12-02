import streamlit as st
import requests
from urllib.parse import urljoin

# API details
BASE_URL = "https://www.zuerich.com"
API_URL = "/en/api/v2/data"
HEADERS = {"Accept": "application/json"}

@st.cache
def fetch_data():
    """Fetch API data and return as JSON."""
    response = requests.get(urljoin(BASE_URL, API_URL), headers=HEADERS)
    return response.json()

def filter_by_ambience(data, keyword):
    """Filter restaurants based on ambience keyword."""
    return [
        item for item in data
        if keyword.lower() in item.get("description", "").lower()
    ]

# Streamlit app UI
st.title("Restaurant Ambience Filter")
st.write("Filter restaurants based on their ambience!")

# Fetch API data
data = fetch_data()

# Ambience keyword input
keyword = st.text_input("Enter an ambience keyword (e.g., cozy, retro, modern):")

if keyword:
    # Filter restaurants
    filtered_restaurants = filter_by_ambience(data, keyword)
    if filtered_restaurants:
        st.subheader(f"Restaurants matching '{keyword}':")
        for restaurant in filtered_restaurants:
            st.write(f"- **{restaurant['name']}**: {restaurant['description']}")
    else:
        st.write("No restaurants found with the specified ambience.")
else:
    st.write("Enter a keyword to start filtering.")
