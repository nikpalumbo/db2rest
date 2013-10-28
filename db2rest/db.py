import sqlalchemy as sql
from sqlalchemy.orm.session import sessionmaker


class DBAdapter(object):

    def __init__(self, db_engine):
        self.meta = sql.schema.MetaData()
        self.db_engine = db_engine
        self.meta.reflect(bind=db_engine)
        self.session = sessionmaker(db_engine)()
        self.conn = db_engine.connect()

    def add_row(self, table_name, values):
        table = sql.Table(table_name, self.meta)
        params = dict(values.items())
        if set(params).issubset(set(table.columns.keys())):
            stmt = sql.sql.expression.insert(table, params)
            res = self.conn.execute(stmt)
            return res.lastrowid

    def get_tables(self):
        return [x.name for x in reversed(self.meta.sorted_tables)]

    def get_headers(self, table_name):
        return [x.name for x in sql.Table(table_name, self.meta).columns]

    def get_rows(self, table_name):
        table = sql.Table(table_name, self.meta)
        return self.session.query(table).all()
