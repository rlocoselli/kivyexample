from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
import requests

response = requests.get('https://stark-ridge-59896.herokuapp.com/typebeers')
data = response.json()

print(data)

dropdown = DropDown()
for item in data:
    btn = Button(text=str(item["name"]), size_hint_y=None, height=44)
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)

mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
runTouchApp(mainbutton)