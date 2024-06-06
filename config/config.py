import os

project_directory = os.path.dirname(os.path.abspath(__file__))

files_folder = os.path.join(project_directory, 'data')

database_name = "db_logbook.accdb"

connection_string = (
  r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
  r"DBQ=" + database_name + ";"
)