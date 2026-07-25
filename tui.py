from textual.app import App
from textual.widgets import Header, Footer, Static

class PyChronicleApp(App):
    def compose(self):
        yield Header()
        yield Static("Code View Pane")
        yield Static("Timeline Slider (Coming Soon)")
        yield Footer()

if __name__ == "__main__":
    PyChronicleApp().run()