from main import TwitchJoinBot
#from lazylister import Lister
from time import sleep

while True:
    # Up to three bots represents Twitch's maximum counted views per IP adress
    bots = ["one", "two"]

    try:
        f = open('list.txt', 'r+')
        users = f.readlines()
        f.close()
        #users = Lister(filePath = "list.txt").returnList()
    except:
        # Exceptions causing this one will be in lister or main, both of which should arleady output their errors
        exit()

    userCount = 0
    for user in users:
        bots[userCount] = TwitchJoinBot(user)
        live = bots[userCount].checkLive()
        if not live:
            bots[userCount].quit()
        else: # Other attempt failed so this one at least grants 2 :( views
            bots[userCount + 1] = TwitchJoinBot(user)
            userCount += 2

        if userCount >= 2:
            break

    # Waits 30 minutes to check for live again
    # This is accomplished by closing all windows and reoping them
    print('No sessions found. Waiting for 60 minutes.')
    sleep(30 * 60) # (Minutes * 60 seconds for easy calculations)

    # Quits and resets all 10 variables, doesn't actually reset for some reason though
    for bot in bots:
        if not isinstance(bot, str):
            bot.quit()
            bot = None
