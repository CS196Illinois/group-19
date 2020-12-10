import TwitterScraper
import run
import json
import time

scraper = TwitterScraper.GoTime()

run.news_scrape()
print("Ran news scrape")

scraper.clear_files()
time.sleep(3)
print("Cleared tweets.json and tweetsToText.txt")

scraper.stream_command()
time.sleep(200)
print("Finished streaming 10,000 tweets")

data = open( "tweets.json", "r+" )
for line in data:
    f = json.loads( line )
    with open( "tweetsToText.txt", "a+" ) as tf:
        try:
            tf.write( f['text'] + '\n' )
        except:
            pass

print("Wrote String information to file")