import sqlite3 as db
from docopt import docopt

def init():
    conn = db.connect("budget.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses(
        amount number,
        category string,
        message string,
        date string
    )
    '''
    cur.execute(sql)
    conn.commit()

init()

def log(amount, category, message=""):
    from datetime import datetime

    date = str(datetime.now())
    conn = db.connect("budget.db")
    cur = conn.cursor()
    sql = '''
    insert into expenses values(
         {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(amount, category, message, date)
    cur.execute(sql)
    conn.commit()

#log(15, "transport", "Uber to Meijer")


def view(category=None):
    conn = db.connect("budget.db")
    cur = conn.cursor()
    if category:
        sql = '''
        select * from expenses where category = '{}'
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses
        '''.format(category)
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sql2)
    total_amount = cur.fetchone()[0]

    return total_amount, results


print(view('food'))

print(view())
