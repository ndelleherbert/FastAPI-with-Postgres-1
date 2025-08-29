from database import Base, engine


print("creating database...")

Base.metadata.create_all(engine)