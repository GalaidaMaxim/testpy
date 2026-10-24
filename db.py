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
    cursor.execute(f"SELECT name FROM users WHERE id = {id}")
    data = cursor.fetchall()
    cursor.close()
    obj = {
        "name": data[0][0]
    }
    return obj

def getUser(name, password):
    cursor = connect.cursor()
    cursor.execute(f"SELECT id, name FROM users WHERE name = '{name}' and password = '{password}'")
    data = cursor.fetchall()
    cursor.close()
    obj = {
        "name": data[0][1],
        "id": data[0][0]
    }
    return obj


def createTask(text, answer, userID):
    cursor = connect.cursor()
    try:
        cursor.execute('INSERT INTO quessions ("text", "answer", "user") VALUES (%s, %s, %s)', (text, answer, userID))
        connect.commit()
        cursor.close()
        return True
    except NameError:
        print(NameError)
        connect.rollback()
        cursor.close()

def getTasksById(id):
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM quessions WHERE "user" = %s', (id,))
    data = cursor.fetchall()
    cursor.close()
    arr=[]
    for item in data:
        arr.append({"text": item[1], "answer": item[2]})
    return arr
    