import twitter

f=open("/home/samvit/Desktop/outputone.txt","w+")
f.close()

def analyze(handle):
  twitter_consumer_key = '1hzEEKAnhiiy6mRUvROfOHVsr'
  twitter_consumer_secret = 'Cme0jpREgjfWEz2XhwZ1h9nwfoygU2XWdvX1tkDRjtWm9rRJC9'
  twitter_access_token = '779676838020931584-tUKZ6W5Ypzw2993y8MIbv1UlvYecFb0'

  twitter_access_secret = 'VrMwoLkpiHPH32xsRgtv9CC5QWtBTYoKbTcBX1okcKfE3'

  twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

  statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

  text = ""

  with open("/home/samvit/Desktop/outputone.txt","a+") as w:
    for status in statuses:
        status = (status.text)
        w.write(str(status))
        w.write("\n")

analyze("@GodHatesFagsWBC")
