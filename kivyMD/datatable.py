from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class datatabledemo(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(pos_hint = {'center_x':0.5,'center_y':0.5},
                            size_hint = (0.9,0.6),
                            check=True,
                            column_data=[("No",dp(18)),("Place",dp(20)),("Area (sqft)", dp(20))],
                            row_data = [("1","Miami","1500"),("2","Orlando","2000"),("3","Seattle","4000"),
                                        ("4","Cali","5000"),("5","NC","4000"),("6","Utah","3500")])
        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)
        screen.add_widget(table)
        return screen
    
    def check_press(self,table_obj,current_row):
        print(table_obj,current_row)


    def row_press(self,table_obj,instance_row):
        print(table_obj,instance_row)

    

datatabledemo().run()
