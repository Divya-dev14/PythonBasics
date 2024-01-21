from kivymd.app import MDApp
from kivymd.uix.list import MDList, ThreeLineIconListItem,ThreeLineListItem, IconLeftWidget
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.screen import Screen

class iconlistdemo(MDApp):
    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list = MDList()
        
        for i in range(1,21):
            icon = IconLeftWidget(icon="account")
            item = ThreeLineIconListItem(text="Student "+str(i), 
                                         secondary_text = "Name "+str(i),
                                         tertiary_text="Age "+str(i) )
            item.add_widget(icon)
            list.add_widget(item)
        
        scroll_view.add_widget(list)
        screen.add_widget(scroll_view)
        return screen

iconlistdemo().run()












