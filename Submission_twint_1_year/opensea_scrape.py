import cloudscraper
import json

def filter_typename(dict):
  return dict["__typename"] == "AssetQuantityType"

def filter_quantityInEth_exists(dict):
  if "quantityInEth" in dict:
    return True
  else:
    return False

def get_floor_price_in_eth(dict):
  return float(dict["quantity"]) / 1000000000000000000

def get_floor_prices(slug):
  scraper = cloudscraper.create_scraper(
    browser={
      'browser': 'chrome',
      'platform': 'android',
      'desktop': False
    }
  )
  url = "https://opensea.io/collection/{}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW".format(slug);
  html = scraper.get(url).text
  json_string = html.split("</script>",2)[0].split("window.__wired__=",2)[1]
  data = json.loads(json_string)
  data_values = data["records"].values() # get all values type...
  data_list = [*data_values] # convert to list =~ array in js
  data_list = list(filter(filter_typename, data_list))
  data_list = list(filter(filter_quantityInEth_exists, data_list))
  data_list = list(map(get_floor_price_in_eth, data_list))
  return data_list


# scraping floor prices from opensea
#print("RUNNING FOR cool-cats-nft")
#print(get_floor_prices("cool-cats-nft"))
#print("RUNNING FOR treeverse")
#print(get_floor_prices("treeverse"))

import pandas as pd
import numpy as np

data = pd.read_csv('opensea_collection_1_year.csv')
collection_name = data['collection name']

Avg_price = []
for i in range(len(collection_name)): 
    p = np.mean(get_floor_prices(collection_name[i]))
    Avg_price.append(p)
    
data['Average_price'] = Avg_price


data.to_csv('opensea_collection_final_data.csv', index = False)

data['Average_price'].isnull().sum()