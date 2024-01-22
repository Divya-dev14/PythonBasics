username_helper = """
MDTextField:
    hint_text:"Enter username"
    helper_text:"Forget password"
    helper_text_mode:"on_focus"
    icon_right:"android"
    icon_right_color:app.theme_cls.primary_color
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:500
"""



screen_helper="""
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name:'menu'
    MDLabel:
        text:'Welcome User!'
        halign:'center'
    MDRectangleFlatButton:
        text:'Profile'
        pos_hint : {'center_x':0.5,'center_y':0.4}
        on_press:root.manager.current='profile'
    MDRectangleFlatButton:
        text:'Upload'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        on_press:root.manager.current='upload'

<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:'Your profile is up to date'
        halign:'center'
    MDRectangleFlatButton:
        text:'back'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        on_press:root.manager.current='menu'

<UploadScreen>:
    name:'upload'
    MDLabel:
        text:'Already uploaded enough files'
        halign:'center'
    MDRectangleFlatButton:
        text:'back'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        on_press:root.manager.current='menu'



"""
