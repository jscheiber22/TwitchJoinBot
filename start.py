from main import TwitchJoinBot
from lister import Lister
from time import sleep

while True:
    # Up to ten bots represents Twitch's maximum counted views per IP adress
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
            userCount += 2
        if userCount >= 2:
            break

    # Waits 30 minutes to check for live again
    # This is accomplished by closing all windows and reoping them
    sleep(30 * 60) # (Minutes * 60 seconds for easy calculations)

    # Quits and resets all 10 variables, doesn't actually reset for some reason though
    for bot in bots:
        if not isinstance(bot, str):
            bot.quit()
            bot = None
