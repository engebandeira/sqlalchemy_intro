from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id    = Column(Integer, primary_key=True)
    nome  = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
