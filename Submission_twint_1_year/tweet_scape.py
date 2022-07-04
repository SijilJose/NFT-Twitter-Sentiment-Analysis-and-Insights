import nest_asyncio
nest_asyncio.apply()

import twint


seed_terms = ['#nfts', '#nft', '#nftart', '#nftcommunity', '#nftcollector', '#NFTs', '#NFT', '#NFTCommunity', '#NFTcommunity', '#nftgiveaway', '#NFTGiveaway', '#metaverse', '#web3', '#NFTCollection', '#NFTGame', '#NFTdrop', '#NFTartists', '#NFTProject', '#NFTMarketplace', '#NFTdrops' , '@opensea']
#seed_terms = ['opensea', 'rarible', 'larvalab', 'decentraland', 'superrare', 'mintable', 'knownorigin','axieinfinity']
search_terms = ' OR '.join(seed_terms)
print(search_terms)

# Configure
c = twint.Config()
c.Search = search_terms
#c.User_full = True
c.Media = True
c.Resume = 'Resume_total.csv'
c.Since = "2021-01-01"
c.Until = "2022-03-24"
c.Min_likes = 100
c.Filter_retweets = True
c.Popular_tweets = True
c.Store_csv = True
c.Hide_output = True
c.Output = 'NFT_tweet_1_year_mp.csv'

# Run
twint.run.Search(c)
print('complete')







########################## PART 2 ##################################
# Extracting userinformation of users posting trending nft tweets
 # The following code should be run only aftert EDA_twint.ipynb is run 

# Extracting profile information of dailytop10 users
import pandas as pd
d = pd.read_csv('SA_data_1_year.csv')   # SA_data_1_year.csv from running exploratory_data_analysis_twint.ipynb
username = d['username'].unique().tolist()

for j in range(1938,len(username)):
    user = username[j]
    c = twint.Config()
    c.Username = user
    c.Store_csv = True
    c.Hide_output = True
    c.Output = 'user_info_1_year_1.csv'
    twint.run.Lookup(c)