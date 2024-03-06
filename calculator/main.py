from textual.app import App, ComposeResult
from textual.widgets import Button, Digits
from textual.containers import Grid

class CalculatorApp(App):
    """Calculator App"""
    CSS_PATH = "main.tcss"

    def compose(self) -> ComposeResult:
        yield Digits("0", id="display")
        with Grid() as grid:
            yield Button("AC", classes="top-button")
            yield Button("+/-", classes="top-button")
            yield Button("%", classes="top-button")
            yield Button.warning("/")
            yield Button("7")
            yield Button("8")
            yield Button("9")
            yield Button.warning("*")
            yield Button("4")
            yield Button("5")
            yield Button("6")
            yield Button.warning("-")
            yield Button("1")
            yield Button("2")
            yield Button("3")
            yield Button.warning("+")
            yield Button("0", id="number-0")
            yield Button(".")
            yield Button.warning("=")



if __name__ == '__main__':
    app = CalculatorApp()
    app.run()