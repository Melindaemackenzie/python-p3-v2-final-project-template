from models.__init__ import CURSOR, CONN

class Athlete:

    all = {}

    def __init__(self, name, age, gender, race_id, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.race_id = race_id

    def __repr__(self):
        return f"<Athlete {self.id}: {self.name}: {self.age}: {self.gender} - {self.race_id}>"
        
       

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
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age is not None:
            self._age = age
        else:
            raise ValueError(
                "Age must be an integer"
            )
        
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and gender in ["M", "F"]:
            self._gender = gender
        else:
            raise ValueError(
                "Gender must be 'M' or F"
            )
        
    @property
    def race_id(self):
        return self._race_id
    
    @race_id.setter
    def race_id(self, race_id):
        if isinstance(race_id, int):
            self._race_id = race_id
        else:
            raise ValueError(
                'Race must be a number'
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Athlete instances """
        sql = """
            CREATE TABLE IF NOT EXISTS athletes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            race_id INTEGER,
            FOREIGN KEY (race_id) REFERENCES races(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def rename_table(cls, new_name):
        """ Rename the athletes table """
        sql = f"""
            ALTER TABLE runners RENAME TO {new_name}
        """
        CURSOR.execute(sql)
        CONN.commit()

        

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS athletes 
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO athletes (name, age, gender, race_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.gender, self.race_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Athlete.all[self.id] = self

    @classmethod
    def create(cls, name, age, gender, race_id):
        athlete = cls(name, age, gender, race_id)
        athlete.save()
        return athlete
    
    def update(self):
        sql = """
            UPDATE athletes
            SET name = ?, age = ?, gender = ?, race_id =?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.age, self.gender, self.race_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM athletes
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del Athlete.all[self.id]
        self.id =  None
        
    @classmethod
    def instance_from_db(cls,row):
        athlete = cls.all.get(row[0])

        if athlete:
            athlete.name = row[1]
            athlete.age = row[2]
            athlete.gender = row[3]
            athlete.race_id = row[4]
        else:
            athlete = cls(row [1], row[2], row[3], row[4])
            athlete.id = row[0]
            cls.all[athlete.id] = athlete
        return athlete
    
    @classmethod
    def get_all(cls, race_id):
        sql = """
            SELECT * FROM athletes
            WHERE race_id = ?
        """

        rows = CURSOR.execute(sql, (race_id)).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM athletes
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
        

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM athletes
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()

        return cls.instance_from_db(row) if row else None

