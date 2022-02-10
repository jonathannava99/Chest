#! /usr/bin/envs python3
# coding: utf-8

from model.connection import Connection


class RequestsTemplate(Connection):

    def read(self, sql: str, message: str) -> tuple:
        """Read a list of items from the database

        Attrs:
        - sql (str): SQL request for read items
        - message (str): Warning message if can't read items

        Returns:
        - A list with the items
        """
        read_entity = None
        connect = self.getConnection()
        connection = connect.cursor()

        sql = sql

        try:
            connection.execute(sql)
            read_entity = connection.fetchall()

        except NameError:
            print("{},{}".format(message, NameError))

        finally:
            connection.close()
            return read_entity

    def create(self, value: tuple, sql_script: str, message: str) -> None:
        """Insert item into database

        Attrs:
        - sql (str): SQL request for create item
        - value (tuple): Item's infos
        - message (str) : Warning if can't create item
        """
        connect = self.getConnection()
        connection = connect.cursor()

        try:
            connection.execute(sql_script, value)
            connect.commit()

        except NameError:
            print("{}, {}".format(message, NameError))

        finally:
            connection.close()

    def update(self, sql: str, message: str) -> None:
        """Update item from database

        Attrs:
        - sql (str): SQL request for update item
        - message (str) : Warning if can't update item
        """
        connect = self.getConnection()
        connection = connect.cursor()

        sql = sql

        try:
            connection.execute(sql)
            connect.commit()

        except NameError:
            print("{},{}".format(message, NameError))

        finally:
            connection.close()

    def delete(self, table: str, table_id: str, id_entity: int, message: str) -> None:
        """Delete item from database

        Attrs:
        - table (str): SQL request for update item
        - table_id (str) : name item's Identifier
        - id_entity(int): item's Identifier
        - message(str): warning if can't delete
        """
        connect = self.getConnection()
        connection = connect.cursor()

        sql = "DELETE FROM {} WHERE {} ={}".format(table, table_id, id_entity)

        try:
            connection.execute(sql)
            connect.commit()

        except NameError:
            print("{},{}".format(message, NameError))

        finally:
            connection.close()
