from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal
import sqlite3


class PyChronicleApp(App):

    CSS = """
    #code_view {
        width: 70%;
        border: solid green;
    }

    #timeline {
        width: 30%;
        border: solid yellow;
    }
    """

    def compose(self) -> ComposeResult:

        conn = sqlite3.connect("pychronicle.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT line_number, variable_name, variable_value
            FROM variable_history
            ORDER BY id DESC
            LIMIT 15
        """)

        rows = cursor.fetchall()
        conn.close()

        code_text = "📄 Recent Execution\n\n"

        for line, var, value in rows:
            code_text += f"Line {line}: {var} = {value}\n"

        timeline_text = f"⏳ Timeline\n\nFrames Loaded: {len(rows)}"

        yield Header()

        with Horizontal():
            yield Static(code_text, id="code_view")
            yield Static(timeline_text, id="timeline")

        yield Footer()


if __name__ == "__main__":
    PyChronicleApp().run()