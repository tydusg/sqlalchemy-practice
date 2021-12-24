from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///users.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    # # Adds a user
    # kirby_user = User(name="Kirby", fullname="Luis Kirby Salva", nickname="Kirby")
    # session.add(kirby_user)
    # session.commit()

    # # Adds multiple users
    # new_users = [
    #     User(name="Marriane", fullname="Marriane Mones", nickname="Mols"),
    #     User(name="Marjorie", fullname="Marjorie Mones", nickname="Marjo"),
    #     User(name="Karen", fullname="Karen Tricia Salva", nickname="Karen"),
    # ]
    # session.add_all(new_users)
    # session.commit()

    # # Update a user
    # kirby_user = User(name="Kirby", fullname="Luis Kirby Salva", nickname="Kirby")
    # session.add(kirby_user)
    # session.new # Outputs kirby_user
    # kirby_user['nickname'] = 'new_nickname' # Update nickname
    # session.new # Will reflect the new nickname
    # session.commit() # Commit changes to db
    # session.new # Nothing, changes already commited
    # kirby_user['nickname'] = 'new_nickname_2' # Update nickname
    # session.new # Nothing, no changes here. This is only for new entries
    # session.dirty # Will reflect the new nickname
    # session.commit() # Commit changes to db

    # # Rollback changes
    # session.rollback() # Removes changes reflected in session.new and session.dirty

    # # Delete user
    # session.delete(user_to_delete) # replace user_to_delete with user object -> you can query to get hold of the user
    # session.commit() # Like creating and updating, changes must be commited before being reflected in the db
