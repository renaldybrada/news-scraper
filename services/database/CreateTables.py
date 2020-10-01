from services.database.Connector import DBConnector

class ColumnStructure():
    def __init__(self, columnName, columnType, nullable=True, isPrimary=False):
        self.name = columnName
        self.type = columnType
        self.nullable = nullable
        self.isPrimary = isPrimary

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

            conj = ", "
            if i == (len(table.columns) - 1):
                conj = ""
            columnQuery = columnQuery + temp + conj 

        query = "CREATE TABLE %s (%s)" % (table.name, columnQuery)
        print(query)
        # self.connection.execute(query)

class MigrateTable():
    tables = [
        TableStructure("channels", [
            ColumnStructure("id", "INT", False, True),
            ColumnStructure("name", "VARCHAR(255)"),
            ColumnStructure("status", "VARCHAR(255)")
        ]),
        TableStructure("headlines", [
            ColumnStructure("id", "INT", False, True),
            ColumnStructure("channel_name", "VARCHAR(255)"),
            ColumnStructure("original_link", "VARCHAR(255)"),
            ColumnStructure("title", "VARCHAR(255)"),
            ColumnStructure("image", "VARCHAR(255)"),
            ColumnStructure("created_at", "DATE()"),
        ]),
        TableStructure("analytic_common_words", [
            ColumnStructure("id", "INT", False, True),
            ColumnStructure("content", "TEXT", False),
            ColumnStructure("created_at", "DATE()"),
        ])
    ]

    def migrate(self):
        exec = CreateTables()
        for table in self.tables:
            exec.createTable(table)

        return 0
