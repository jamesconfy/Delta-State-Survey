#imports............
from app import create_app, db

app = create_app()

#run code................
if __name__ == '__main__':
    #create database....................
    # db.create_all(app=create_app())
    # @app.before_app_first_request
    # def create_tables():
    #     db.create_all()
        
    app.run(debug=True)