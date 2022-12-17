from __future__ import unicode_literals

from sqlalchemy.schema import (
    Column,
    Index,
    ForeignKey,
    PrimaryKeyConstraint,
    UniqueConstraint,
)

from sqlalchemy.sql.schema import CheckConstraint
from sqlalchemy.types import Integer, String, Text, Enum
from sqlalchemy.dialects.postgresql import ARRAY

from xivo_dao.alchemy import enum
from xivo_dao.helpers.db_manager import Base, UUIDAsString

from ..db import Base


class RatingModel(Base):
    __tablename__ = 'plugin_rating'

    id = Column(Integer, nullable=False)
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    provider_name = Column(String(128), nullable=True)
    local = Column(String(128), nullable=True)
    national = Column(String(128), nullable=True)
    mobile = Column(String(128), nullable=True)
    international = Column(String(128), nullable=True)
    cost = Column(String(128), nullable=True)
    currency = Column(String(128), nullable=True)
    free = Column(String(128), nullable=True)
    timestamp = Column(String(50), nullable=True)
    reserved = Column(String(50), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )
