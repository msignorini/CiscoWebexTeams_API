#import webex_teams
from webex_teams.webex_teams import *
from pprint import pprint

wt = webexTeams()
#ret = wt.get_domain_people()
#pprint(ret)

ret = wt.send_to_email("marco.signorini88@gmail.com", "hello world")
pprint(ret)

ret = wt.send_hello_to_sparky()
pprint(ret)
