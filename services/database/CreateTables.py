import mysql.connector
from services.database.Connector import DBConnector

class ColumnStructure():
    def __init__(self, columnName, columnType, nullable=True, isPrimary=False, isUnique=False):
        self.name = columnName
        self.type = columnType
        self.nullable = nullable
        self.isPrimary = isPrimary
        self.isUnique = isUnique

class TableStructure():
    def __init__(self, tableName, tableColumns):
        self.name = tableName
        self.columns = tableColumns

class CreateTables(DBConnector):
    def createTable(self, table):
        columnQuery = ""
        for i, column in enumerate(table.columns):
            temp = column.name + " " + column.type
            if column.nullable == False :
                temp = temp + " NOT NULL"

            if column.isPrimary:
                temp = temp + " PRIMARY KEY"
                if column.type == "INT":
                    temp = temp + " AUTO_INCREMENT"

            if column.isUnique :
                temp = temp + " UNIQUE"

            conj = ", "
            if i == (len(table.columns) - 1):
                conj = ""
            columnQuery = columnQuery + temp + conj 

        query = "CREATE TABLE %s (%s)" % (table.name, columnQuery)
        # print(query)
        try :
            self.connection.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)

        self.closeConnection()

class MigrateTable():
    tables = [
        TableStructure("headlines", [
            ColumnStructure("id", "INT", False, True),
            ColumnStructure("channel_name", "VARCHAR(255)"),
            ColumnStructure("original_link", "VARCHAR(255)", False, False, True),
            ColumnStructure("title", "VARCHAR(255)"),
            ColumnStructure("image", "VARCHAR(255)"),
            ColumnStructure("author", "VARCHAR(255)"),
            ColumnStructure("editor", "VARCHAR(255)"),
            ColumnStructure("content", "TEXT"),
            ColumnStructure("publish_date", "VARCHAR(255)"),
            ColumnStructure("created_at", "DATETIME"),
        ]),
        TableStructure("analytic_common_words", [
            ColumnStructure("id", "INT", False, True),
            ColumnStructure("content", "TEXT", False),
            ColumnStructure("created_at", "DATETIME"),
        ])
    ]

    def migrate(self):
        for table in self.tables:
            exec = CreateTables()
            exec.createTable(table)

        return 0
