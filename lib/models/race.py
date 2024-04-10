from models.__init__ import CURSOR, CONN

class Race:

    all = {}

    def __init__(self, name, race_type, distance, id=None):
        self.id = id
        self.name = name
        self.race_type = race_type
        self.distance = distance

    def __repr__(self):
        return f'<Race {self.id}: {self.name}, {self.race_type}, {self.distance}>'

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Race instances """
        sql = """
            CREATE TABLE IF NOT EXISTS races (
            id INTEGER PRIMARY KEY,
            name TEXT,
            race_type TEXT,
            distance REAL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS races
        """

        CURSOR.execut(sql)
        CONN.commit()

    def save(self):
        """ Save the race instance to the database """
        if self.id is None:
            # Insert a new row into the races table
            sql = """
                INSERT INTO races (name, race_type, distance)
                VALUES (?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.race_id, self.distance))
            CONN.commit()
            # Update the instance with the assigned ID
            self.id = CURSOR.lastrowid
        else:
            # Update an existing row in the races table
            sql = """
                UPDATE races
                SET name = ?, race_id = ?, distance = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.race_type, self.distance, self.id))
            CONN.commit()



    @classmethod
    def create(cls, name, race_type, distance):
        race = cls(name, race_type, distance)
        race.save()
        return race
    
    def update(self):
        sql = """
            UPDATE races
            SET name = ?, race_type = ?, distance = ?
            WHERE id = ?
        """

        CURSOR.execute (sql, (self.name, self.race_type, self.distance))
        CONN.commit()


    def delete(self):
        """ Delete the race instance from the database """
        if self.id is not None:
            sql = "DELETE FROM races WHERE id = ?"
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            self.id = None

    @classmethod
    def instance_from_db(cls, row):
        race = cls.all.get(row[0])
        if race:
            race.name = row[1]
            race.race_type = row[2]
            race.distance = row[3]
        else:
            race = cls(row[1], row[2], row[3])
            race.id = row[0]
            cls.all[race.id] = race
        return race
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM races
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM races
            WHERE id =?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_race_type(cls, race_type):
        sql = """
            SELECT *
            FROM races
            WHERE race_type = ?
        """

        row = CURSOR.execute(sql, (race_type,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def athletes(self):
        pass

