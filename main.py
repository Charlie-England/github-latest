import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    url = "https://api.github.com/users/" + username + "/events/public"
    response = requests.get(url)
    print(response.json()[0]["created_at"])
    


