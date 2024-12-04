import pandas as pd   # FOR EXCEL
from pyparsing import originalTextFor


class ExcelCRUD():
    def __init__(self, file_name:str):
        self.file_name = file_name

    def create_excel(self):

        initial_data = {
            "Name": ['Botakoz','Forest','Dante','Jerry'],
            'Age': [18, 30, 22, 26],
            'Grade':['A', 'C', 'A+', 'D'],
            'Salary': [750, 900, 300, 100]
        }

        original_dataframe = pd.DataFrame(initial_data)
        print(original_dataframe)

        original_dataframe.to_excel (excel_writer=self.file_name, index = False)
        return original_dataframe

    def read_excel(self):
        read_excel_dataframe = pd.read_excel (io = self.file_name)
        print(read_excel_dataframe)


    def update_excel(self):
        original_dataframe = pd.read_excel(io=self.file_name)
        original_dataframe['Experience'] = original_dataframe ['Age'] - 16

        print(original_dataframe)
        original_dataframe.to_excel(excel_writer=self.file_name, index = False)

    def delete_excel(self, df):
        df.drop()
        print(df)







excel_crud_obj = ExcelCRUD(file_name='students.xlsx')
excel_crud_obj.create_excel()
excel_crud_obj.read_excel()
excel_crud_obj.update_excel()


