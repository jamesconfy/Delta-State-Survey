#imports............
from app import create_app

app = create_app()

#run code................
if __name__ == '__main__':
    #create database....................
    #db.create_all()
    app.run(debug=True)