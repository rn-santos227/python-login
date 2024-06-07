import os

project_directory = os.path.dirname(os.path.abspath(__file__))

data_folder = os.path.join(project_directory, 'data')

database_name = "database_name"
database_path = os.path.join(data_folder, "db_logbook.accdb")

connection_string = (
  r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
  r"DBQ=" + database_name + ";"
)