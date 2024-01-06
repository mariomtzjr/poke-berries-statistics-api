import requests

from fastapi import HTTPException


def get_paginated_data(api_url):
    all_data = []

    while api_url:
        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                current_page_data = response.json()

                response.raise_for_status()
                all_data.extend(current_page_data.get('results', []))

                api_url = current_page_data.get('next')
            else:
                print(f"Error fetching data. Status code: {response.status_code}")
                break
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Error fetching data from PokeAPI: {str(e)}")
    return all_data


def get_names(data):
    names = []

    for item in data:
        if isinstance(item, dict):
            # If the item is a dictionary, recursively call the function
            names.append(item.get('name'))
        elif isinstance(item, list):
            # If the item is a list, recursively call the function
            names.append(get_names(item))

    return names

def get_ids_by_berry_url(data):
    ids = []
    
    for item in data:
        if isinstance(item, dict):
            url_slices = list(filter(None, item.get("url").split("/")))
            berry_id = url_slices[-1]
            ids.append(berry_id)
        elif isinstance(item, list):
            get_ids_by_berry_url(item)
    return ids

def get_berry_growth_times(url: str, ids: list):
    growth_times = []

    for berry_id in ids:
        berry_url = url + berry_id
        try:
            response = requests.get(berry_url)
            if response.status_code == 200:
                response = response.json()
                growth_time = response.get("growth_time")
                growth_times.append(growth_time)
            
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Error fetching data from PokeAPI: {str(e)}")
    return growth_times
