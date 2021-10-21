from database import session
from database.models import classnames
from sqlalchemy import select, text, desc, asc


class Get:

    def __init__(self, filter):
        self.schema = filter["schemaName"]
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
            order_map = {'asc': asc, 'desc': desc}
            order_columns = self.orderBy['columns']
            updown = self.orderBy['order']

            if len(order_columns) != len(updown):
                raise ValueError("In orderBy: Attributes 'columns' and 'order' lengths do not match.")

            elif any([order not in order_map.keys() for order in updown]):
                raise ValueError("In orderBy: One or more of the items in 'orderBy.order' are not in ['asc','desc']")

            else:
                order_num = len(order_columns)

            params = [order_map[updown[i]](order_columns[i]) for i in range(order_num)]
            stmt = stmt.order_by(*params)

        if self.limit is not None:
            stmt

        print(stmt)
        res = session.execute(stmt)
        return res


soldier = Get({
    "schemaName": "public",
    "table": "soldiers",
    "columns": ["department", "id"],
    "where": "soldiers.id > 5",
    "orderBy": {
        "columns": ["department", "id"],
        "order": ["asc", "desc"]
    },
    "limit": None
}
)

# res = soldier.get_data()