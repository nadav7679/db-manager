from database import session
from database.models import classnames
from sqlalchemy import select, text, desc, asc


class Get:

    def __init__(self, filter):
        self.schema = filter["schema"]
        self.table = filter["table"]
        self.columns = filter["columns"]
        self.where = filter["where"]
        self.orderBy = filter["orderBy"]
        self.limit = filter["limit"]

    def get_data(self):

        table = classnames[self.table]
        if self.columns is None:
            select_stmt = select(table)

        else:
            attr = [getattr(table, column) for column in self.columns]
            select_stmt = select(*attr)

        if self.where is not None:
            stmt = select_stmt.where(text(self.where))

        if self.orderBy is not None:
            stmt = stmt.order_by()

        if self.limit is not None:
            stmt

        print(stmt)
        res = session.execute(stmt)
        print(res.fetchall())


soldier = Get({
    "schema": "public",
    "table": "departments",
    "columns": ["id", "name"],
    "where": "departments.id > 5",
    "orderBy": None,
    "limit": None
}
)

soldier.get_data()
