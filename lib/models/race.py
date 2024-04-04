from models.__init__ import CURSOR, CONN

class Race:

    all = {}

    def __init__(self, name, location, date, distance, id=None):
        self.id = id
        self.name = name
        self.location = location
        self.date = date
        self.distance = distance

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Race instances """
        sql = """
            CREATE TABLE IF NOT EXISTS races (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            date DATE,
            distance REAL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the race instance to the database """
        if self.id is None:
            # Insert a new row into the races table
            sql = """
                INSERT INTO races (name, location, date, distance)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.location, self.date, self.distance))
            CONN.commit()
            # Update the instance with the assigned ID
            self.id = CURSOR.lastrowid
        else:
            # Update an existing row in the races table
            sql = """
                UPDATE races
                SET name = ?, location = ?, date = ?, distance = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.location, self.date, self.distance, self.id))
            CONN.commit()

    def delete(self):
        """ Delete the race instance from the database """
        if self.id is not None:
            sql = "DELETE FROM races WHERE id = ?"
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            self.id = None
