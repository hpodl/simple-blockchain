from app import create_app
from uuid import uuid4

app = create_app()

with open("key.txt", "w+") as fh:
    app.secret_key = fh.readline()
    if not app.secret_key:
        key = str(uuid4()).replace('-', '')
        app.secret_key = key
        
        fh.truncate(0)
        fh.write(key)



if __name__ == '__main__':
    app.run(debug=True)