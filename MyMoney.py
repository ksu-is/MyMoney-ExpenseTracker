import sqlite3

def init():
    conn = sqlite3.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
        )
    '''
    cur.execute(sql)
    conn.commit()

def log(amount, category, message=""):
    from datetime import datetime
    date = str(datetime.now())
    conn = sqlite3.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    insert into expenses values (
        {},
        '{}',
        '{}',
        '{}'
          )
    '''.format(amount, category, message, date)
    cur.execute(sql)
    conn.commit()

def view(category, date):
    conn = sqlite3.connect("spent.db")
    cur = conn.cursor()
    if category.startswith('p'):
        sql = '''
        select * from expenses where category = '{}' and date like '{}%'
        '''.format(category, date)
        sql2 = '''
        select sum(amount) from expenses where category = '{}' and date like '{}%'
        '''.format(category, date)
    else:
        sql = '''
        select * from expenses where date like '{}%'
        '''.format(date)
        sql2 = '''
        select sum(amount) from expenses where date like '{}%'
        '''.format(date)
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sql2)
    total_amount = cur.fetchone()[0]

  
#Main loop for user input
while True:
        print("What would you like to do?")
        print("1 - Enter an expense\n2 - View expenses based on date and category\n3 - Update on spending habits\nQ - Quit")
        ans = input(":")

        if ans == "1":
            cost = input('What is the amount of the expense?\n:')
            cat = input('What is the category of the expense?\n:')
            msg = input('What is the expense for?\n:')
            log(cost,cat,msg)
        elif ans == "2":
            ctg = input('Enter what category of expenses you would like to view or press enter to view all\n:')
            dat = input('What month do you want to view? (yyyy-mm)\n:')
            print(view(ctg,dat))
        elif ans == "3":
            compare()
        elif ans.lower() == "q":
            break

