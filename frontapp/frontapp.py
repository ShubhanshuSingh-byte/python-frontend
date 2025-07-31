import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""


def login_page():
    return rx.flex(
        rx.box(
            rx.vstack(
                rx.image(src="logo.png", alt="Logo"),
                rx.text("Welcome to SNSS Global Services", weight="bold", size="9", align="center"),
                rx.text("Enterprise Resource Planning System"),
                rx.button(rx.image(src="logo.png", width="20px", height="20px"), rx.text("Continue with google"),margin="3em"),
                rx.text("Application under development"),
                align="center"
            ),
            width="450px", height="539px", padding="50px"
        ),
        justify="center", margin="150em"
    )


def index():
    return login_page()

app = rx.App()
app.add_page(index)
