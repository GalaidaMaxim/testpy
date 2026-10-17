import psycopg2

connect = psycopg2.connect("postgresql://postgres.ctersgvolxajiscpuiho:9cQNtmZetBvJi0jM@aws-0-eu-west-1.pooler.supabase.com:5432/postgres")

cursor = connect.cursor()
cursor.execute("INSERT INTO users (name, password) VALUES ('Maxim', '12345')")

connect.commit()
cursor.close()
# 9cQNtmZetBvJi0jM