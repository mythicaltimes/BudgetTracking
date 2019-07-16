usage = '''

Expense Tracker CLI.

Usage:
    spent_driver.py init
    spent_driver.py view [<view_category>]
    spent_driver.py <amount> <category> [<message>]
'''

from docopt import docopt
from Budget import *
args = docopt(usage)

if args['init']:
    init()
    print("User Profile Created")

if args['view']:
    category = args['view_category>']
    view(category)
    amount, results = view(category)
    print(amount)
    print(results)

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        log(amount, args['category'], args['message'])
    except:
        print(usage)
