import requests # this can be used to request information on a webpage

r = requests.get("https://www.google.com")

#this gets data from the home page of google

r.status_code # this will tell us the availability of the page
    #200 is ok
    #403 is forbidden, password or otherwise protected
    #404 not found, page moved or deleted but it no longer exists

r.headers

#this brings all of the different categories of info found with the request

r.headers["Date"]

# brings up the date of the request

r.text

#this is all of the text that makes up the front page, will be a lot
