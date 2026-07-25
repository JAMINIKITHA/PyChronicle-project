from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Static

class PyChronicleApp(App):

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal():
            yield Static("📄 Code View", id="code_view")
            yield Static("⏳ Timeline", id="timeline")

        yield Footer()

if __name__ == "__main__":
    PyChronicleApp().run()