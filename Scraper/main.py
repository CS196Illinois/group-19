import TwitterScraper
import json
import time

scraper = TwitterScraper.GoTime()

scraper.clear_files()
time.sleep(3)
print("Cleared file")

scraper.stream_command()
time.sleep(200)
print("Finished streaming")

data = open( "tweets.json", "r+" )
for line in data:
    f = json.loads( line )
    with open( "writeTo.txt", "a+" ) as tf:
        try:
            tf.write( f['text'] + '\n' )
        except:
            pass

print("Wrote String information to file")