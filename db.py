import psycopg2


data_base = psycopg2.connect(
    host='abul.db.elephantsql.com',
    user='zwjbkucy',
    database='zwjbkucy',
    password='eOEKzbEyk0n21qcPRs9i3YbSp__32BVc'
)
cursor = data_base.cursor()

def insert_data(laptop_name, laptop_image, laptop_price, credit_price):
    cursor.execute(f"""
        INSERT INTO bots(image, name, month_price, year_price)
        VALUES
        ('{laptop_image}', '{laptop_name}', '{laptop_price}', '{credit_price}')
    """)

    data_base.commit()


cursor.execute("""
    SELECT image, name, month_price, year_price
    FROM bots
""")


data = cursor.fetchall()
for product in data:
    product_image = product[0]
    product_name = product[1]
    product_price = product[2]
    product_kredit = product[3]

