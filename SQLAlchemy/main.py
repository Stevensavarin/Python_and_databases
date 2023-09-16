from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import ForeignKey

engine = create_engine("postgresql://postgres:password@localhost/pythondb")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True )
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now)
    courses = relationship("Course", backref="user")

    def __str__(self):
        return self.username
    
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=False)
    user_id = Column(ForeignKey("users.id"))
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.title

Session = sessionmaker(engine)
session = Session()

if __name__ == "__main__":
    
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    user1 = User(username="user1", email="user1@example.com")
    user2 = User(username="user2", email="user2@example.com")
    user3 = User(username="user3", email="user3@example.com")
    user4 = User(username="user4", email="user4@example.com")

    user1.courses.append(
        Course(title="Curso profesional de Base de datos", user_id=user1.id)
    )
    user1.courses.append(
        Course(title="Curso profesional de Python", user_id=user1.id)
    )
    user1.courses.append(
        Course(title="Curso profesional de Go", user_id=user1.id)
    )

    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)

    session.commit()

    # Listar en consola todos los usuarios que posean por lo menos un curso (INNER JOIN).
    # Listar en consola todos los usuarios sin cursos (LEFT JOIN)

    users = session.query(User).join(
        Course
    )

    #users = session.query(User).outerjoin(
    #    Course
    #).filter(
    #    Course.id == None
    #)

    for user in users:
        print(user)
