from sqlalchemy import Column, Integer, Text, Date

from Conjugate import db

class Classes(db.model):
    __tablename__ = "classes"
    class_id = Column(Integer, primary_key=True)
    class_name = Column(Text, nullable = False)
    class_start_time = Column(Integer, nullable = False)
    class_end_time = Column(Integer, nullable= False)
    class_building = Column(Text, nullable = False)
    class_room_number  = Column(Integer, nullable = False)

    def __init__(self, class_name, class_start_time, class_end_time, class_building, class_room_number):
        self.class_name = class_name
        self.class_start_time = class_start_time
        self.class_end_time = class_end_time
        self.class_building = class_building
        self.class_room_number = class_room_number

class Homeworks(db.model):
    __tablename__ = "homeworks"
    homeworks_id = Column(Integer, primary_key=True)
    user_name = Column(Text, nullable = False)
    class_id = Column(Integer, nullable = False)
    homework_title = Column(Integer, nullable = False)
    homework_due_date = Column(Date, nullable = False)

    def __init__(self, user_name, class_id, homework_title, homework_due_date)
        self.user_name = user_name
        self.class_id = class_id
        self.homework_title = homework_title
        self.homework_due_date = homework_due_date
    