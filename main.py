import mariadb


conn = mariadb.connect(
    user="root",
    password="",
    host="127.0.0.1",
    port=3306,
    database="test_first_database"
)
cur = conn.cursor()

def select(data):
    if type(data) is int:
        cur.execute(f"SELECT * FROM `homework` WHERE id={data};")
        return cur.fetchall()
    else:
        cur.execute(f"SELECT `{data}` FROM `homework`;")
        return cur.fetchall()

def insert(data):
    cur.execute(f"INSERT INTO `homework`(`user_name`) VALUES ('{data}')")
    conn.commit()
    print(f"Update db: {data}")

def delete(id):
    cur.execute(f"DELETE FROM `homework` WHERE id={id}")
    conn.commit()
    print(f"User with id = {id} delete")

def update(last_value, new_value):
    cur.execute(f"UPDATE `homework` SET `user_name`='{new_value}' WHERE `user_name`='{last_value}'")
    print(f"Name {name} is changed in db")


while True:
    name = input("Input your name:\n")

    if name == "":
        break

    try:
        id = int(name)
        data = select(id)
        if not data:
            print("Unknown id")
            continue
        delete(id)
    except ValueError:
        db_name = select("user_name")
        flag = False
        for user_name in db_name:
            if user_name[0].lower() == name.lower():
                update(user_name[0], name)
                flag = True 
                   
        if flag:
            continue

        insert(name)

