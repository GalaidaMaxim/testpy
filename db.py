import psycopg2

connect = psycopg2.connect("postgresql://postgres.ctersgvolxajiscpuiho:9cQNtmZetBvJi0jM@aws-0-eu-west-1.pooler.supabase.com:5432/postgres")


def createUser(name, password):
    cursor = connect.cursor()
    try: 
        cursor.execute(f"INSERT INTO users (name, password) VALUES ('{name}', '{password}') RETURNING id, name")
        connect.commit()
        data = cursor.fetchall()
        cursor.close()
        obj = {
            "name": data[0][1],
            "id": data[0][0]
        }
        return obj
    except:
        connect.rollback()
        cursor.close()

    


def getUserByID(id):
    cursor = connect.cursor()
    try:
        cursor.execute(f"SELECT name FROM users WHERE id = {id}")
        data = cursor.fetchall()
        cursor.close()
        obj = {
            "name": data[0][0]
        }
        return obj
    except:
        cursor.close()

def getUser(name, password):
    cursor = connect.cursor()
    try:
        cursor.execute(f"SELECT id, name FROM users WHERE name = '{name}' and password = '{password}'")
        data = cursor.fetchall()
        cursor.close()
        obj = {
            "name": data[0][1],
            "id": data[0][0]
        }
        return obj
    except NameError:
        print(NameError)
        cursor.close()
    


getUser("Galaida", 12345)
# 9cQNtmZetBvJi0jM

def createTask(text, answer, user):
    cursor = connect.cursor()
    try:
        cursor.execute('INSERT INTO task ("text", "ansver", "user") VALUES (%s, %s, %s)',(text, answer, user)
)
        connect.commit()
        cursor.close()
    except NameError:
        connect.rollback()
        cursor.close()
        print(NameError)