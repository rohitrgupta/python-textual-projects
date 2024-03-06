from textual.widgets import Static
from time import monotonic
from textual.reactive import Reactive


class TimeDisplay(Static):
    """Display time"""
    DEFAULT_CSS = """
    TimeDisplay {
        content-align: center middle;
        text-opacity: 60%;
        height: 3;
    }"""

    start_time = Reactive(monotonic)
    current_time = Reactive(0.0)
    total_time = Reactive(0.0)

    def on_mount(self) -> None:
        self.update_timer = self.set_interval(
            1/60, self.update_time, pause=True)

    def update_time(self) -> None:
        self.current_time = self.total_time + monotonic() - self.start_time

    def watch_current_time(self, time: float) -> None:
        minutes, seconds = divmod(time, 60)
        hours, minutes, = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        self.start_time = monotonic()
        self.update_timer.resume()
        self.watch_current_time(self.current_time)

    def stop(self) -> None:
        self.update_timer.pause()
        self.total_time += monotonic() - self.start_time

    def reset(self) -> None:
        self.total_time = 0.0
        self.current_time = 0.0
