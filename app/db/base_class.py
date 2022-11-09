from __future__ import annotations

import typing as t

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr

class_registry: t.Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: t.Any
    __name__: str

    # This is a hack to get the table name from the class name

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
