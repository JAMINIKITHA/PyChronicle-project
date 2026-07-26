from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal
import sqlite3


class PyChronicleApp(App):

    CSS = """
    #code_view {
        width: 70%;
        border: solid green;
        padding: 1;
    }

    #timeline {
        width: 30%;
        border: solid yellow;
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

        # Load database info
        conn = sqlite3.connect("pychronicle.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM variable_history")
        total_frames = cursor.fetchone()[0]

        conn.close()

        timeline_text = (
            "⏳ Timeline\n\n"
            f"Total Frames : {total_frames}\n\n"
            "Current Frame : 1\n\n"
            "Status : Ready"
        )

        yield Header()

        with Horizontal():
            yield Static(code_text, id="code_view")
            yield Static(timeline_text, id="timeline")

        yield Footer()


if __name__ == "__main__":
    PyChronicleApp().run()