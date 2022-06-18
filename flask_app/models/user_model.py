
from flask_app.config.mysqlconnection import connectToMySQL



class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_one_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email) "
        query += "VALUES(%(first_name)s,%(last_name)s,%(email)s);"

        return connectToMySQL("users_schema").query_db(query, data)


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL("users_schema").query_db(query)
        print(result)

        all_users = []

        for row in result:
            all_users.append(cls(row))
        return all_users

    @classmethod
    def get_one_user(cls,data):

        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL("users_schema").query_db(query,data)
        print(result)
        return cls(result[0])


    @classmethod
    def edit_one_user(cls,data):
        query = "UPDATE users "
        query += "SET first_name =%(first_name)s, last_name =%(last_name)s, email =%(email)s  WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )
    

    @classmethod
    def delete_one_user(cls,data):
        query = "DELETE FROM users "
        query += "WHERE id= %(id)s "
        return connectToMySQL('users_schema').query_db( query, data )

