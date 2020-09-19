from main import TwitchJoinBot
from lister import Lister
from time import sleep

while True:
    bots = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    try:
        users = Lister().returnList()
    except:
        # Exceptions causing this one will be in lister or main, both of which should arleady output their errors
        exit()

    userCount = 0
    for user in users:
        bots[userCount] = TwitchJoinBot(user)
        live = bots[userCount].checkLive()
        if not live:
            bots[userCount].quit()
            userCount += 1
        else: # Other attempt failed so this one at least grants 3 views
            bots[userCount + 1] = TwitchJoinBot(user)
            bots[userCount + 2] = TwitchJoinBot(user)
            userCount += 3

    sleep(300)
