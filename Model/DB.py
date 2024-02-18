import mysql.connector as m


class MySql:

    @staticmethod
    def Connect():
        connection = m.connect(
            host="localhost",
            user="root",
            password="",
            database="pythonMVC"

        )