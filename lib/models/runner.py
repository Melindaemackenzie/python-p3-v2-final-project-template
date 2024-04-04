from __init__ import CURSOR, CONN

class Runner:

    all = {}

    def __init__(self, name, age, gender, race_id, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.race_id = race_id

    def __repr__(self):
        return f"<Runner {self.id}: {self.name}: {self.age}: {self.gender} - {self.race_id}>"
        
       

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
        if isinstance(age, int) and len(age):
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
        """ Create a new table to persist the attributes of Runner instances """
        sql = """
            CREATE TABLE IF NOT EXISTS runners (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            race_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS runners 
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO runners (name, age, gender, race_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.gender, self.race_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

