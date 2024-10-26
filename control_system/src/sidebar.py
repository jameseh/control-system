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


import reflex as rx
from webui import styles
from webui.state import State

# Helper Components for Organization
def NavbarBrand():
    return rx.link(
        rx.box(
            rx.image(src="favicon.ico", width=30, height="auto"),
            p="1",
            border_radius="6",
            bg="#F0F0F0",
            mr="2",
        ),
        href="/",
    )

def NavbarActions(): 
    return rx.hstack(
        rx.button(
            "+ New chat",
            bg=styles.accent_color,
            px="4",
            py="2",
            h="auto",
            on_click=State.toggle_modal,
        ),
        rx.menu(
            rx.menu_button(
                rx.avatar(name="User", size="md"),
                rx.box(),
            ),
            rx.menu_list(
                rx.menu_item("Help"),
                rx.menu_divider(),
                rx.menu_item("Settings"),
            ),
        ),
        spacing="8", 
    )

# Main NavBar Function
def navbar():
    return rx.box(
        rx.hstack(  # Main horizontal layout for entire navbar
            rx.hstack(  # Left Section
                rx.icon(
                    tag="hamburger",
                    mr=4,
                    on_click=State.toggle_drawer,
                    cursor="pointer",
                ),
                NavbarBrand(),
                rx.breadcrumb(
                    rx.breadcrumb_item(
                        rx.heading("ReflexGPT", size="sm"),
                    ),
                    rx.breadcrumb_item(
                        rx.text(State.current_chat, size="sm", font_weight="normal"),
                    ),
                ),
            ),
            NavbarActions(),  # Right Section
            justify="space-between",
        ),
        bg=styles.bg_dark_color,
        backdrop_filter="auto",
        backdrop_blur="lg",
        p="4",
        border_bottom=f"1px solid {styles.border_color}",
        position="sticky",
        top="0",
        z_index="100",
    )
