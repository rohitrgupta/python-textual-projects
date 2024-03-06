from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import ScrollableContainer
from ui.stopwatch import Stopwatch


class StopwatchApp(App):

    BINDINGS = [("ctrl+q", "quit", "Quit"),
                ("ctrl+d", "toggle_dark", "Toggle Dark Mode"),
                ("a", "add_stopwatch", "Add"),
                ("r", "remove_stopwatch", "Remove"),]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        self.stopwatch_container = ScrollableContainer(
            Stopwatch(), Stopwatch(), Stopwatch(), Stopwatch())
        yield self.stopwatch_container

    def action_add_stopwatch(self) -> None:
        new_stopwatch = Stopwatch()
        self.stopwatch_container.mount(new_stopwatch)
        new_stopwatch.scroll_visible()

    def action_remove_stopwatch(self) -> None:
        timers = self.query("Stopwatch")
        if timers:
            timers.last().remove()


if __name__ == '__main__':
    app = StopwatchApp()
    app.run()
