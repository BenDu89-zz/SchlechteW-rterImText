import urllib

def read_text():
    text = open("/Users/benjamindunisch/Downloads/movie_quotes/movie_quotes.txt")
    text = text.read()
    check_text(text)




def check_text(text_to_check):
    website = "http://www.wdylike.appspot.com/?q=" + text_to_check
    t = urllib.urlopen(website)
    output = t.read()
    if output == "false":
        print "Du bist sehr freundlich"
    else:
        print "Selber Arsch"





read_text()
