#imports............
from app import create_app, db

app = create_app()

#run code................
if __name__ == '__main__':
    #create database....................
    db.create_all(app=create_app())
    app.run(debug=True)