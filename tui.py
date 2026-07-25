from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Static
import sqlite3


class PyChronicleApp(App):

    def on_mount(self):
        conn = sqlite3.connect("pychronicle.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT line_number, variable_name, variable_value FROM variable_history LIMIT 10"
        )

        rows = cursor.fetchall()

        print("\n=== Variable History ===")
        for row in rows:
            print(row)

        conn.close()

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal():
            yield Static(
                "📄 Code View\n\nPython code will appear here.",
                id="code_view",
            )

            yield Static(
                "⏳ Timeline\n\nDatabase Connected",
                id="timeline",
            )

        yield Footer()


if __name__ == "__main__":
    PyChronicleApp().run()