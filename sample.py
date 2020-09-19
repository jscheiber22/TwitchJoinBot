from main import TwitchJoinBot
from lister import Lister
from time import sleep

try:
    users = Lister().returnList()
except:
    # Exceptions causing this one will be in lister or main, both of which should arleady output their errors
    exit()

for user in users:
    bot = TwitchJoinBot(user)
    live = bot.checkLive()
    if not live:
        bot.quit()
    else: # Other attempt failed so this one at least grants 3 views
        bot = TwitchJoinBot(user)
        bot = TwitchJoinBot(user)

sleep(5)

# Attempt to allocate up to 10 views per streamer that does not work

    # if live:
    #     for allocation in range(1, 1 + round((len(users)/10))):
    #         bot = TwitchJoinBot(user)
    #         live = bot.checkLive()
