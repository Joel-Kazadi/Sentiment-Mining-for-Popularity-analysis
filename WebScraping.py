# 1. Libraries
# !pip install snscrape --upgrade
import pandas as pd
from snscrape.modules import twitter as sntwitter

# 2. Common settings
COLUMNS = ['Date', 'UserName', 'Comment', 'Reply', 'Retweet',
           'Like', 'Quote', 'Creation', 'Place', 'Followers']
DATE_RANGE = dict(since='2018-11-20', until='2018-12-30')

def scrape_candidate(leader_name:str,lang:str='fr')->pd.DataFrame:
    """
    Scrape tweets for a given candidate name and return
    a DataFrame with the specified columns plus a 'Leader' column.
    """
    query = (f'{leader_name} lang:{lang} '
             f'until:{DATE_RANGE["until"]} '
             f'since:{DATE_RANGE["since"]}')
    scraper = sntwitter.TwitterSearchScraper(query)

    records = []
    for tweet in scraper.get_items():
        records.append([
            tweet.date,
            tweet.user.displayname,     # this feature has to be removed because of ethical concerns
            tweet.rawContent,
            tweet.replyCount,
            tweet.retweetCount,
            tweet.likeCount,
            tweet.quoteCount,
            tweet.user.created,
            tweet.user.location,
            tweet.user.followersCount,
        ])


    df = pd.DataFrame(records, columns=COLUMNS)
    df['Leader'] = leader_name
    return df

# 3. Scrape each candidate
candidates = ['Tshisekedi', 'Fayulu', 'Ramazani']

dfs = [scrape_candidate(name) for name in candidates]

# 4. Combine and clean up
df = pd.concat(dfs, ignore_index=True)
df['Date']     = pd.to_datetime(df['Date']).dt.date
df['Creation'] = pd.to_datetime(df['Creation']).dt.date
df.sort_values('Date', inplace=True)

# 5. Export and inspect
output_path = 'scraped_data.xlsx'
df.to_excel(output_path, sheet_name='2018', index=False)
df.info()
