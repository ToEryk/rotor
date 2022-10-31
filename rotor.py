import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.lang import Builder
import socket
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label



class MyApp(App):
    def build(self):

        def prawo(self):
            if lb1.text == "359":
                lb1.text = "0"
            else:
                lb1.text = str(int(lb1.text)+1)

                s = socket.socket()
                s.connect(('127.0.0.1', 2222))
                data = "prawo";
                s.send(data.encode())
                dataFromServer = s.recv(1024)
                print(dataFromServer.decode())
                s.close()



        def lewo(self):
            if lb1.text == "0":
                lb1.text = "359"
            else:
                lb1.text = str(int(lb1.text)-1)
            s = socket.socket()
            s.connect(('127.0.0.1', 2222))
            data = "lewo";
            s.send(data.encode())
            dataFromServer = s.recv(1024)
            print(dataFromServer.decode())
            s.close()


        superBox = BoxLayout(orientation='vertical')
        VB = BoxLayout(orientation='vertical')
        HB = BoxLayout(orientation='horizontal')
        btn1 = Button(text="Lewo")
        btn1.bind(on_press=lewo)
        btn2 = Button(text="Prawo")
        btn2.bind(on_press=prawo)
        lb1 = Label(text="0")
        HB.add_widget(btn1)
        HB.add_widget(btn2)
        VB.add_widget(lb1)
        superBox.add_widget(VB)
        superBox.add_widget(HB)
        return superBox


if __name__ == '__main__':
    MyApp().run()