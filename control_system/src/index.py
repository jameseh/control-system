import reflex as rx


class Sidebar(rx.Component):
    """A sidebar component for the application."""

    @staticmethod
    def layout():
        """Layout for the sidebar."""

        return rx.box(
            rx.vstack(
                rx.image(src="/favicon.ico", margin="0 auto"),
                rx.heading(
                    "Sidebar",
                    text_align="center",
                    margin_bottom="1em",
                ),
                rx.menu(...),
                width="250px",
                padding_x="2em",
                padding_y="1em",
            ),
            position="fixed",
            height="100%",
            left="0px",
            top="0px",
            z_index="500",
        )




class BottomDrawer(rx.Component):
    """A bottom drawer component for the application."""

    def layout(self):
        """Layout for the bottom drawer."""
        return rx.Container(
                children=[rx.Text("Bottom Drawer Content")],
        )


class ContentArea(rx.Component):
    """A main content area component for the application."""

    def layout(self):
        """Layout for the main content area."""
        return rx.(
                children=[rx.Text("Welcome!")],
        )


class Index(rx.App):
    """The main application class."""

    @staticmethod
    def layout():
        """Layout for the application."""
        return rx.hstack(
                children=[
                        Sidebar(),
                        rx.vstack(
                                children=[
                                        ContentArea(),
                                        BottomDrawer(),
                                ],
                        ),
                ],
        )
