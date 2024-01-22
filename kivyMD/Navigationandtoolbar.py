from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size =(300,500)

screen_helper = """
Screen: 
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDTopAppBar: 
                        title: 'Demo App'
                        left_action_items :[["menu",lambda x: nav_drawer.set_state("open")]]
                        elevation:2
                    Widget:
        MDNavigationDrawer:
            id:nav_drawer
            BoxLayout:
                orientation:'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source:'pic.JPG'
                MDLabel:
                    text:'     Santa Cruz'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height:self.texture_size[1]
                MDLabel:
                    text:'     Dec 31st'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height:self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon:'account'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon:'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon:'logout'
"""

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Orange"
        screen = Builder.load_string(screen_helper)
        return screen
    
    def navigation_draw(self):
        print("Navigation")




DemoApp().run()