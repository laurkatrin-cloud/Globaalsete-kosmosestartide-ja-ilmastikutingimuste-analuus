from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://praktikum:praktikum@localhost:55432/kosmos"
)

with engine.connect() as conn:
    print("Ühendus PostgreSQL-iga töötab!")
