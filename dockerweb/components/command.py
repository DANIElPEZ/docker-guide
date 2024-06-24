import reflex as rx

def linecode(command:str):
    return rx.box(
        rx.card(
            rx.hstack(
                rx.chakra.icon(
                    tag='copy',
                    _hover={
                        'cursor':'pointer'
                    },
                    on_click=[
                        rx.set_clipboard(command),
                        rx.window_alert('Comando copiado')
                        ],
                    color='#ffffff'
                ),
                rx.scroll_area(
                    rx.text(
                        command,
                        style={
                            'background':'#00000000',
                            'background_color':'#00000000',
                            'color':"#fff",
                        }
                    ),
                    type="auto",
                    scrollbars="horizontal",
                    padding_bottom='5px'
                )
            ),
            size="2",
            background_color='rgb(12,107,165)',
            margin_y='10px'
        ),
        width='100%',
        padding_y='0'
    )