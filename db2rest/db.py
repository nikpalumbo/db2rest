"""This module provide the interfaces with the dababase.

    It uses SQLAlchemy to connect and introspect a RDBMS
"""

import sqlalchemy as sql
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.engine import reflection
from sqlalchemy.types import Integer
from  sqlalchemy.schema import Column

class DBAdapter(object):
    """Responsible to adapt the database.
    """

    def __init__(self, db_engine):
        self.meta = sql.schema.MetaData()
        self.db_engine = db_engine
        self.meta.reflect(bind=db_engine)
        self.session = sessionmaker(db_engine)()
        self.conn = db_engine.connect()

    def rollback(self):
        self.session.rollback()
        self.conn = self.db_engine.connect()

    def add_row(self, table_name, values):
        """Add a row to a table
            #: table_name
            #: values
        """
        table = sql.Table(table_name, self.meta)
        if set(values).issubset(set(table.columns.keys())):
            stmt = sql.sql.expression.insert(table, values)
            res = self.conn.execute(stmt)
            return res.lastrowid

    def delete_row(self, table_name, row_id):
        """Delete row from a table
            #: table_name
            #: values
        """
        table = sql.Table(table_name, self.meta)
        stmt = sql.sql.expression.delete(table).\
                    where(table.c.id == row_id)
        res = self.conn.execute(stmt)
        self.session.commit()
        return res.rowcount

    def get_tables(self):
        """Return all the tables in the DB."""
        insp = reflection.Inspector.from_engine(self.db_engine)
        views = insp.get_view_names()
        views.extend(self.meta.tables)
        return sorted(views)

    def get_headers(self, table_name):
        """Return the column name of a given table."""
        return [x.name for x in sql.Table(table_name, self.meta).columns]

    def get_rows(self, table_name, params={}):
        """Return some or all rows in case params is not specified
           a given table.
        """
        self.rollback()
        for key in params.keys():
            if key not in self.get_headers(table_name):
              del params[key]
        res = []
        try:
            table = sql.Table(table_name, self.meta)
            if not len(table.columns.keys()):
                table = sql.Table(table_name, self.meta,
                                  Column("id", Integer, primary_key=True),
                                  autoload=True,
                                  autoload_with=self.db_engine,
                                  extend_existing=True)
            res = self.session.query(table).filter_by(**params)
        except Exception, e:
            print e
            pass
        return res

    def  get_row(self, table_name, row_id):
        """Returns a list with a row found."""
        table = sql.Table(table_name, self.meta)
        return [self.session.query(table).filter_by(id=row_id).one()]

    def update_row(self, table_name, row_id, values):
        """Update the given row_id in the given table."""
        table = sql.Table(table_name, self.meta)
        for key in values.keys():
            if key not in self.get_headers(table_name):
              del values[key]
        stmt = sql.sql.expression.update(table).\
            where(table.c.id == int(row_id)).\
            values(values)
        res = self.conn.execute(stmt)
        self.session.commit()
        return res.rowcount,\
            dict(zip(self.get_headers(table_name),
                     self.get_row(table_name, row_id)[0]))
