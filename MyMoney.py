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
    try:
        cur.execute(sql)
        conn.commit()
        print('\nExpense saved!\n')
    except:
        print('\nExpense not saved. Please try again and do not punctuate the category or detailed message.\n')

def view(category, date):
    conn = sqlite3.connect("spent.db")
    cur = conn.cursor()
    if category.isalpha():
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
    for expense in results:
        print(expense)
    print('\nTotal:','$' + str(total_amount))

#Welcome message
print("\nWelcome to MyMoney Expense Tracker!")
print("This app allows you to record and view your spending habits to help you become a more conscious spender!")
  
#Main loop for user input
while True:
        print("\nWhat would you like to do?")
        print("1 - Enter an expense\n2 - View expenses based on date and category\n3 - Update on spending habits\nQ - Quit")
        ans = input(":")
        print()

        if ans == "1":
            cost = input('What is the amount of the expense?\n:')
            cat = input('What is the category of the expense?\n:').title()
            msg = input('What is the expense for?\n:')
            log(cost,cat,msg)
        elif ans == "2":
            date = input('What month or day do you want to view? (yyyy-mm or yyyy-mm-dd)\n:')
            category = input('Enter what category of expenses you would like to view or press enter to view all\n:').title()
            print()
            view(category,date)
        elif ans == "3":
            compare()
        elif ans.lower() == "q":
            print('Goodbye!\n')
            break

