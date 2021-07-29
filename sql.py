import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.engine import Inspector

engine = sqlalchemy.create_engine('postgresql://basic:basic1@localhost:5432/basic_db')

connection = engine.connect()
# print(engine.table_names())

# inspector = inspect(engine)
# print(inspector.get_table_names())

req = connection.execute("""


SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name iLIKE '%%gen%%'
ORDER BY first_name
LIMIT 2
;


""").fetchmany(5)
print(req)
