import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class childapp(GridLayout):
    def __init__(self,**kwargs):
        super(childapp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Student Name"))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Age"))
        self.age = TextInput()
        self.add_widget(self.age)

        self.add_widget(Label(text="Student Marks"))
        self.marks = TextInput()
        self.add_widget(self.marks)

        self.btn = Button(text="Submit")
        self.btn.bind(on_press=self.submit)
        self.add_widget(self.btn)

    def submit(self,instance):
        print("Student Name is",self.s_name.text)
        print("Student Age is",self.age.text)
        print("Student Marks :",self.marks.text)


class parentapp(App):
    def build(self):
        return childapp()

if __name__ == "__main__":
    parentapp().run()

    




    