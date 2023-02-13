import psycopg2



# Функция удаления таблицы
def drop_table(cur, table):    
    cur.execute(table)
     
      
# Функция создания таблицы
def create_table(cur, query_table):
    cur.execute(query_table)

# Функция добавления записи о клиенте
def add_person(cur, firstname, lastname, email, phone=None):
    cur.execute("""
                INSERT INTO person(firstname, lastname, email)
                VALUES (%s, %s, %s)
                RETURNING person_id;
                """, (firstname, lastname, email))
    person_id = cur.fetchone()
    if phone:
        cur.execute("""
                    INSERT INTO phone_person(person_id, phone)
                    VALUES (%s, %s)
                    """, (person_id, phone))            

# Функция добавления номера телефона клиента
def add_phone(cur, person_id, phone):
    cur.execute("""
                INSERT INTO phone_person(person_id, phone)
                VALUES (%s, %s)
                """, (person_id, phone))

# Функция изменения данных клиента
def change_person(cur, person_id, firstname=None, lastname=None, email=None, phone=None):
    if phone != None:
        cur.execute("""
            UPDATE phone_person
            SET phone_person = %s
            WHERE person_id = %s
            """, (phone, person_id))

    if email != None:
        cur.execute("""
            UPDATE person
            SET email = %s
            WHERE person_id = %s
            """, (email, person_id))

    if lastname != None:
        cur.execute("""
            UPDATE person
            SET lastname = %s
            WHERE person_id = %s
            """, (lastname, person_id))

    if firstname != None:
        cur.execute("""
            UPDATE person
            SET firstname = %s
            WHERE person_id = %s
            """, (firstname, person_id))

# Функция удаления номера телефона клиента
def delete_phone(cur, phone=None, person_id=None):
    cur.execute("""DELETE FROM phone_person WHERE person_id=%s or phone=%s;""", (person_id, phone))

# Функция удаления записи о клиенте
def delete_person(cur, person_id):   
    delete_phone(cur, None, person_id)
    cur.execute("""DELETE FROM person WHERE person_id=%s; """, (person_id))
   

# Функция поиска клиента
def search_person(cur, firstname=None, lastname=None, email=None, phone=None): 
    data_person = {}
    if firstname:
        data_person['firstname'] = firstname
    if lastname:
        data_person['lastname'] = lastname
    if email:
        data_person['email'] = email
    if phone:
        data_person['phone'] = phone

    query = """SELECT firstname, lastname, email, p.phone FROM person  
        JOIN phone_person AS p USING(person_id) 
        WHERE """ + ' and '.join(f"{k} LIKE '{v}'" for k, v in data_person.items())
    cur.execute(query)
    item_search = cur.fetchall()
    print(item_search)



with psycopg2.connect(user='postgres', password='6814',  database='hw_notebook') as conn:
    with conn.cursor() as cur:
               
        # Удаляем таблицы
        tables = """DROP TABLE phone_person;
                    DROP TABLE person;"""
        drop_table(cur, tables)
        
        # Создаем таблицы
        create_query_tables = """CREATE TABLE IF NOT EXISTS person (person_id SERIAL PRIMARY KEY, 
                                                                     firstname VARCHAR(64) NOT NULL, 
                                                                     lastname VARCHAR(64) NOT NULL,
                                                                     email VARCHAR(64) NOT NULL);
                                CREATE TABLE IF NOT EXISTS phone_person (phone_id SERIAL PRIMARY KEY, 
                                                                            phone VARCHAR(32) , 
                                                                            person_id int REFERENCES person(person_id)) ;"""
        
        create_table(cur, create_query_tables )
        
        # Создаем запись о клиенте
        add_person(cur, 'Anna', 'Annova', 'Anna@neto.ru','+70000000005')
        add_person(cur, 'Ivan', 'Ivanov', 'Ivan@neto.ru', '+70000000000')
        add_person(cur, 'Petr', 'Petrov', 'Petr@neto.ru')
        add_person(cur, 'Egor', 'Eorov', 'Egor@neto.ru', '+70000350000')
        # Добавляем номер телефона
        add_phone(cur, 3, '+78889999999' )
        add_phone(cur, 3, '+78889999998' )
       
        # Изменяем запись о клиенте
        change_person(cur, 1,  firstname=None, lastname='Petrova', email=None, phone=None)
        
        # Удаляем номер телефона
        delete_phone(cur, '+78889999999')
 
        # Ищем по данным запись о клиенте
        person = search_person(cur, firstname='Petr')
        
          # Удаляем запись о клиенте
        delete_person(cur, '4')
        
        conn.commit() 
       
    conn.close()           

