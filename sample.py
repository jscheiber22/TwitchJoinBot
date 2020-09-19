from main import TwitchJoinBot
from lister import Lister

try:
    users = Lister().returnList()
except:
    # Exceptions causing this one will be in lister or main, both of which should arleady output their errors
    exit()

for user in users:
    bot = TwitchJoinBot(user)
    live = bot.checkLive()

# Attempt to allocate up to 10 views per streamer

    # if live:
    #     for allocation in range(1, 1 + round((len(users)/10))):
    #         bot = TwitchJoinBot(user)
    #         live = bot.checkLive()

#
# # bot = TwitchJoinBot("ryan")
# bot = TwitchJoinBot("onlinedude")
# bot.checkLive()
#
# bot2 = TwitchJoinBot("ryan")
# bot2.checkLive()
