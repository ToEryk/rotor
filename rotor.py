from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import socket

Builder.load_file('builder.kv')


class MyLayout(Widget):
    def prawo(self):
        if self.ids.lb1.text == "359":
            self.ids.lb1.text = "0"
        else:
            self.ids.lb1.text = str(int(self.ids.lb1.text) + 1)
        self.ids.img.stopnie = str(int(self.ids.img.stopnie) - 1)
        s = socket.socket()
        s.connect(('127.0.0.1', 2222))
        data = "prawo";
        s.send(data.encode())
        dataFromServer = s.recv(1024)
        print(dataFromServer.decode())
        s.close()

    def lewo(self):
        if self.ids.lb1.text == "0":
            self.ids.lb1.text = "359"
        else:
            self.ids.lb1.text = str(int(self.ids.lb1.text) - 1)
        self.ids.img.stopnie = str(int(self.ids.img.stopnie) + 1)
        s = socket.socket()
        s.connect(('127.0.0.1', 2222))
        data = "lewo";
        s.send(data.encode())
        dataFromServer = s.recv(1024)
        print(dataFromServer.decode())
        s.close()

class ROTOR(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    ROTOR().run()
