from models.__init__ import CURSOR, CONN


class Race:

    all = {}

    def __init__(self, name, race_type, distance,  id=None):
        self.id = id
        self.name = name
        self.race_type = race_type
        self.distance = distance
   

    def __repr__(self):
        return f'<Race {self.id}: {self.name}, {self.race_type}, {self.distance}>'


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def race_type(self):
        return self._race_type
    
    @race_type.setter
    def race_type(self, race_type):
        if isinstance(race_type, str) and race_type.lower() in {"run", "bike", "swim"}:
            self._race_type = race_type.lower()
        else:
            raise ValueError(
                "Race type must be a string and one of 'run', 'bike', 'swim' "
            )
        
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, distance):
        if isinstance(distance, (int, float)) and distance > 0:
            self._distance = distance
        else:
            raise ValueError(
                "Distance must be a postiive integer or float in miles"
            )
        
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

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the race instance to the database """
        if self.id is None:
            # Insert a new row into the races table
            sql = """
                INSERT INTO races (name, race_type, distance)
                VALUES (?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.race_type, self.distance))
            CONN.commit()
            # Update the instance with the assigned ID
            self.id = CURSOR.lastrowid
        else:
            # Update an existing row in the races table
            sql = """
                UPDATE races
                SET name = ?, race_type = ?, distance = ?
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

        CURSOR.execute (sql, (self.name, self.race_type, self.distance, self.id))
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
    def find_by_name(cls, name):
        """Find a race by its name."""
        sql = """
            SELECT *
            FROM races
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if row:

            return cls.instance_from_db(row) 
        else:
            return None
    
    @classmethod
    def find_by_race_type(cls, race_type):
        sql = """
            SELECT *
            FROM races
            WHERE race_type = ?
        """

        rows = CURSOR.execute(sql, (race_type,)).fetchall()

        races = []
        for row in rows:
            races.append(cls.instance_from_db(row))
        return races 
    
    
    
    def athletes(self):
        from models.athlete import Athlete
        sql = '''
            SELECT * FROM athletes
            WHERE race_id = ?
        '''

        rows = CURSOR.execute(sql, (self.id, )).fetchall()

        return [Athlete.instance_from_db(row) for row in rows]

