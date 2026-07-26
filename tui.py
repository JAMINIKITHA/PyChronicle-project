from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal
import sqlite3


class PyChronicleApp(App):

    CSS = """
    #code_view {
        width: 60%;
        border: solid green;
        padding: 1;
    }

    #timeline {
        width: 20%;
        border: solid yellow;
        padding: 1;
    }

    #watch {
        width: 20%;
        border: solid cyan;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:

        # Load source code
        try:
            with open("sample.py", "r") as file:
                code = file.readlines()
        except FileNotFoundError:
            code = ["sample.py not found"]

        code_text = "📄 Source Code\n\n"

        for i, line in enumerate(code, start=1):
            code_text += f"{i:3} | {line}"

        # Load database
        conn = sqlite3.connect("pychronicle.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM variable_history")
        total_frames = cursor.fetchone()[0]

        cursor.execute("""
            SELECT variable_name, variable_value
            FROM variable_history
            ORDER BY id DESC
            LIMIT 10
        """)

        variables = cursor.fetchall()
        conn.close()

        timeline_text = (
            f"⏳ Timeline\n\n"
            f"Frames : {total_frames}\n\n"
            f"Current : Latest\n\n"
            f"Status : Ready"
        )

        watch_text = "👀 Watch Variables\n\n"

        for name, value in variables:
            watch_text += f"{name} = {value}\n"

        yield Header()

        with Horizontal():
            yield Static(code_text, id="code_view")
            yield Static(timeline_text, id="timeline")
            yield Static(watch_text, id="watch")

        yield Footer()


if __name__ == "__main__":
    PyChronicleApp().run()