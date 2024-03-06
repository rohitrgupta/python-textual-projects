from textual.widgets import Button, Static
from ui.time_display import TimeDisplay
from textual.app import ComposeResult


class Stopwatch(Static):
    """Stopwatch"""

    DEFAULT_CSS = """
    Stopwatch {
        layout: horizontal;
        background: $boost;
        height: 5;
        margin: 1;
        padding: 1;
        min-width: 50;
    }
    Stopwatch Button {
        width: 16;
    }

    #start {
        dock: left;
    }

    #stop {
        dock: left;
        display: none;
    }

    #reset {
        dock: right;
    }
    Stopwatch.started {
        text-style: bold;
        background: $success;
        color: $text;
    }

    Stopwatch.started TimeDisplay {
        text-opacity: 100%;
    }

    Stopwatch.started #start {
        display: none
    }

    Stopwatch.started #stop {
        display: block
    }

    Stopwatch.started #reset {
        visibility: hidden
    }    
    """

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="primary")
        yield Button("Reset", id="reset", variant="error")
        self.time_display = TimeDisplay("00:00:00.00")
        yield self.time_display

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.time_display.start()
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")
            self.time_display.stop()
        elif event.button.id == "reset":
            self.time_display.reset()
