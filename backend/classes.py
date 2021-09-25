class Get:

    def __init__(self, filter):
        self.tablename = filter.tablename
        self.where = filter.where
        self.order_by = filter.order_by
