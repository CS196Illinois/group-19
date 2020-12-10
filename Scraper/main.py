import TwitterScraper
import run
import json
import time

# # # # Runs News Scrapers # # # #
run.news_scrape()
print("Ran news scrape")

# # # # Creates instance of TwitterScraper.GoTime() Class # # # #
scraper = TwitterScraper.GoTime()

# # # # # Clears tweets and tweetsToText files # # # # 
scraper.clear_files()
time.sleep(3)

# # # # # Starts twitter stream # # # # 
scraper.stream_command()
time.sleep(200)
print("Finished streaming 10,000 tweets")

# # # # # Writes JSON file to text format, keeping only tweet text # # # # 
data = open( "tweets.json", "r+" )
for line in data:
    f = json.loads( line )
    with open( "tweetsToText.txt", "a+" ) as tf:
        try:
            tf.write( f['text'] + '\n' )
        except:
            pass

print("Wrote String information to file")

# # # # Twitter Polarity Score # # # #
a = open("tweetsToText.txt", "r")
twitter_polarity = run.polarityCheck(a.read(), 1)
a.close()

run.twitterScrape(twitter_polarity)
run.endScrape()