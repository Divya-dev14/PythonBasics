from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from helpers import username_helper


class demoapp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette="Purple"
        self.button = MDRectangleFlatButton(text="Login",pos_hint={'center_x':0.5,'center_y':0.4},
                                       on_release = self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(self.button)
        return screen
    
    def show_data(self,obj):
        if self.username.text is "":
            check_user = "Enter Username"
        else :
            check_user = "you entered "+self.username.text
        closebutton = MDFlatButton(text="Close",on_release = self.close_dialog)
        self.morebutton = MDFlatButton(text="More", on_release = self.more_dialog)
        self.dialog = MDDialog(title='Username', text=check_user,
                          size_hint=(0.7,1),buttons=[closebutton,self.morebutton])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()
    
    def more_dialog(self,obj1):
        label = MDLabel(text="You are Succesfully Validated!", pos_hint={'center_x':0.9,'center_y':0.1})
        self.dialog.add_widget(label)
        
        


    

demoapp().run()