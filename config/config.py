import os

documents_directory = os.path.join(os.path.expanduser('~'), 'Documents')

database_path = os.path.join(documents_directory, "db_logbook.mdb")

connection_string = (
  r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
  r"DBQ=" + database_path + ";"
)