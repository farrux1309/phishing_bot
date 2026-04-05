SHORTENERS = ["bit.ly", "tinyurl.com", "t.co"]

def is_short_url(url):
    return any(s in url for s in SHORTENERS)