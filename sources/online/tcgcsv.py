#!/bin/python3

###########################
# ZincAlerts - tcgcsv.com #
###########################

# Website - https://tcgcsv.com/
# Price - Free
# Updated - Mar 8, 2025

#####################
# Import Statements #
#####################
import requests
import json

#############
# Constants #
#############
WEBSITE_URL = "https://tcgcsv.com"
WEBSITE_TCGPLAYER = WEBSITE_URL + "/tcgplayer"

#############
# Functions #
#############
# Get All Categories ID', Display Name and Last Modified For internal use
def get_categories_internal():
    payload = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(WEBSITE_TCGPLAYER + "/categories", headers=headers, data=payload)
    data = json.loads(response.text)
    categories_dict = {}  # Dictionary to store categoryId as key and displayName as value
    if "results" in data and isinstance(data["results"], list):
        for item in data["results"]:  # Loop through each object in the array
            category_id = item.get("categoryId", "N/A")
            display_name = item.get("displayName", "N/A")
            last_modified = item.get("modifiedOn", "N/A")
            categories_dict[category_id] = category_id, display_name, last_modified     
    else:
        print("No 'results' array found in JSON.") 
        return {}  # Return empty dictionary if no results
    return categories_dict  # Return dictionary {categoryId: displayName}

# Get All Categories
def get_categories():
    return get_categories_internal()

# Search Categories by ID, Return Display Name and Last Modified If Found
def search_categories_by_id(category_id):
    categories = get_categories_internal()
    if category_id in categories:
        return categories[category_id]
    else:
        return None    
    
# Get All Groups With Suppiled Category ID and Return Group ID, Display Name and Last Modified
def get_groups_internal(category_id):
    payload = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(WEBSITE_TCGPLAYER + "/" + str(category_id) + "/groups", headers=headers, data=payload)
    data = json.loads(response.text)
    groups_dict = {}  # Dictionary to store groupId as key and displayName as value
    if "results" in data and isinstance(data["results"], list):
        for item in data["results"]:  # Loop through each object in the array
            group_id = item.get("groupId", "N/A")
            name = item.get("name", "N/A")
            abbreviation = item.get("abbreviation", "N/A")
            published_on = item.get("publishedOn", "N/A")
            last_modified = item.get("modifiedOn", "N/A")
            groups_dict[group_id] = group_id, name, abbreviation, published_on, last_modified     
    else:
        print("No 'results' array found in JSON.") 
        return {}  # Return empty dictionary if no results
    return groups_dict  # Return dictionary {groupId: displayName}

# Get All Group info With Suppiled Category ID
def get_groups(category_id):
    return get_groups_internal(category_id)

# Search Groups by ID, Return Display Name and Last Modified If Found
def search_groups_by_id(category_id, group_id):
    groups = get_groups_internal(category_id)
    if group_id in groups:
        return groups[group_id]
    else:
        return None

# Get Product Information With Suppiled Group ID and Return Product ID, Returns Category ID, Group ID, Clean Name, Image URL, Product URL, Presale Array Info and Last Modified
def get_products_internal(category_id, group_id):
    payload = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(WEBSITE_TCGPLAYER + "/" + str(category_id) + "/" + str(group_id) + "/products", headers=headers, data=payload)
    data = json.loads(response.text)
    products_dict = {}  # Dictionary to store productId as key and cleanName as value
    if "results" in data and isinstance(data["results"], list):
        for item in data["results"]:  # Loop through each object in the array
            product_id = item.get("productId", "N/A")
            category_id = item.get("categoryId", "N/A")
            group_id = item.get("groupId", "N/A")
            clean_name = item.get("cleanName", "N/A")
            image_url = item.get("imageUrl", "N/A")
            product_url = item.get("url", "N/A")
            last_modified = item.get("modifiedOn", "N/A")
            products_dict[product_id] = product_id, category_id, group_id, clean_name, image_url, product_url, last_modified
    else:
        print("No 'results' array found in JSON.")
        return {}
    return products_dict

# Get All Products With Suppiled Group ID And Category ID
def get_products(category_id, group_id):
    return get_products_internal(category_id, group_id)

# Search Products by ID, Return Clean Name, Image URL, Product URL and Last Modified If Found
def search_products_by_id(category_id, group_id, product_id):
    products = get_products_internal(category_id, group_id)
    if product_id in products:
        return products[product_id]
    else:
        return None

# Get Price Information With Suppiled Group ID and Returns Product ID and Return Product ID, Low Price, Mid Price, High price, Market Price, Direct Low Price, and Sub Type Name
def get_prices_internal(category_id, group_id):
    payload = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(WEBSITE_TCGPLAYER + "/" + str(category_id) + "/" + str(group_id) + "/prices", headers=headers, data=payload)
    data = json.loads(response.text)
    prices_dict = {}  # Dictionary to store productId as key and lowPrice as value
    if "results" in data and isinstance(data["results"], list):
        for item in data["results"]:  # Loop through each object in the array
            product_id = item.get("productId", "N/A")
            low_price = item.get("lowPrice", "N/A")
            mid_price = item.get("midPrice", "N/A")
            high_price = item.get("highPrice", "N/A")
            market_price = item.get("marketPrice", "N/A")
            direct_low_price = item.get("directLowPrice", "N/A")
            sub_type_name = item.get("subTypeName", "N/A")
            prices_dict[product_id] = product_id, low_price, mid_price, high_price, market_price, direct_low_price, sub_type_name
    else:
        print("No 'results' array found in JSON.")
        return {}
    return prices_dict

# Get All Prices With Suppiled Group ID And Category ID
def get_prices(category_id, group_id):
    return get_prices_internal(category_id, group_id)

# Search Prices by ID, Return Low Price, Mid Price, High Price, Market Price, Direct Low Price, and Sub Type Name If Found
def search_prices_by_id(category_id, group_id, product_id):
    prices = get_prices_internal(category_id, group_id)
    if product_id in prices:
        return prices[product_id]
    else:
        return None
