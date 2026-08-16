import os
from urllib.parse import quote

user = quote(os.environ["MYSQL_USER"], safe="")
password = quote(os.environ["MYSQL_PASSWORD"], safe="")
port = os.environ["MYSQL_HOST_PORT"]
database = quote(os.environ["MYSQL_DATABASE"], safe="")

print(
    f"mysql://{user}:{password}@127.0.0.1:{port}/{database}",
    end=""
)
