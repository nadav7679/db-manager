import sqlalchemy.exc
from sqlalchemy import select, text, desc, asc

from database import session, models, pydantic_model
from database.models import classnames


class Get:

    def __init__(self, filter):
        self.database = filter["database"]
        self.schema = filter["schemaName"]
        self.table = filter["table"]
        self.columns = filter["columns"]
        self.where = filter["where"]
        self.orderBy = filter["orderBy"]
        self.limit = filter["limit"]

    def get_data(self):

        table = classnames[self.table]
        if self.columns is None:
            stmt = select(table)

        else:
            attr = [getattr(table, column) for column in self.columns]
            stmt = select(*attr)

        if self.where is not None:
            stmt = stmt.where(text(self.where))

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
            stmt = stmt.limit(self.limit)

        print(stmt)
        try:
            res = session.execute(stmt)
        except sqlalchemy.exc.InternalError as e:
            session.rollback()
        return res


class Post:

    def __init__(self, filter):
        self.database = filter["database"]
        self.schema = filter["schemaName"]
        self.table = filter["table"]
        self.rowsCount = filter["rowsCount"]
        self.data = filter["data"]

    def post_data(self):
        model_meta = pydantic_model.meta[self.table]
        model = model_meta(**self.data)
        row = model.create()

        session.add(row)
        try:
            session.commit()
        except sqlalchemy.exc.InternalError as e:
            session.rollback()
        return row

soldier = Get({
    "database": "postgres",
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

post_sold = Post({
    "database": "postgres",
    "schemaName": "public",
    "table": "soldiers",
    "rowsCount": 1,
    "data": {
        "name": "whaeverrr",
        "department": "Wind Dragons",
        "commander": "William Rogers",
        "favorite_anime": "Banana Fish"
    },
})

post_dept = Post({
    "database": "db-manager",
    "schemaName": "public",
    "table": "departments",
    "rowsCount": 1,
    "data": {
        "name": "TikTok",
        "king": "whaeverrr",
    },
})

# post_dept.post_data()
# res = soldier.get_data()