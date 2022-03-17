from sqlite3 import *
from config import DATABASE


class DBApi(object):

    def __init__(self) -> None:
        self.__conn: Connection = connect(DATABASE)
        self.__cur: Cursor = self.__conn.cursor()

    def create_users_table(self) -> None:
        """CREATE USER TABLES"""
        self.__cur.execute('''
            CREATE TABLE IF NOT EXISTS
            users(
                user_id INTEGER PRIMARY KEY,
                role TEXT NOT NULL,
                FOREIGN KEY (role) REFERENCES roles(role)
            )
        ''')
        self.__conn.commit()

    def technical_efficiency(self):
        result = "SELECT * FROM technical_efficiency"
        return self.__cur.execute(result).fetchall()

    def select_basic_formula(self, E= 0, C1: str = '', C2 = 0, C3 = 0):
        try:
            self.__cur.execute('''
                        INSERT INTO basic_formula(
                            E,
                            C1,
                            C2,
                            C3
                        )
                        VALUES(?,?,?,?)
                    ''', (E, C1, C2, C3))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True


    def create_all_database(self) -> None:
        """CREATE DATABASE"""
        self.create_users_table()