import reflex as rx
import dockerweb.components.styles as st

def linktopic(txt:str):
    return rx.chakra.menu_item(
        rx.link(
            rx.text(
                txt,
                style={
                    'font_size':'18px',
                    'color':'#fff',
                    'width':'100%',
                    'padding':'0',
                    'margin':'0',
                    'text_align':'center'
                }
            ),
            width='100%',
            href=f'#{txt.lower().replace(" ", "")}'
        )
    )

def navbar():
    return rx.hstack(
        rx.flex(
            rx.hstack(
                    rx.link(
                        rx.heading(
                        'Guia de Docker',
                        size='5',
                        color='#ffffff'
                    ),
                    href='https://www.docker.com/',
                    text_decoration='none',
                    is_external=True
                )
            ),
            rx.spacer(),
            rx.chakra.menu(
                rx.chakra.menu_button(
                    rx.chakra.icon(
                        tag="hamburger",
                        width='30px',
                        height='30px',
                        color='#ffffff',
                        _hover={
                            'cursor':'pointer'
                        }
                    )
                ),
                rx.chakra.menu_list(
                    rx.scroll_area(
                        linktopic('Crear contenedor'),
                        linktopic('Alias contenedor'),
                        linktopic('Listar contenedor'),
                        linktopic('Borar contenedor'),
                        linktopic('Correr contenedor'),
                        linktopic('Detener contenedor'),
                        linktopic('Exponer contenedor'),
                        linktopic('Bind mount'),
                        linktopic('Crear volumen'),
                        linktopic('Insertar archivos'),
                        linktopic('Extraer archivos'),
                        linktopic('Listar imagen'),
                        linktopic('Descargar imagen'),
                        linktopic('Crear imagen'),
                        linktopic('Construir imagen'),
                        linktopic('Borrar imagen'),
                        linktopic('Cambiar nombre Del Tag'),
                        linktopic('Publicar imagen'),
                        linktopic('Historial imagen'),
                        linktopic('Ejemplo practico'),
                        linktopic('Listar red'),
                        linktopic('Crear red'),
                        linktopic('Conectarse a una red'),
                        linktopic('Docker compose'),
                        type="hover",
                        scrollbars="vertical",
                        style={
                            "height": '200px',
                            "background_color":"#2475ab"
                        },
                    )
                )
            ),
            width="100%"
        ),
        position="fixed",
        top='0',
        padding="1em",
        width="100%",
        z_index="10",
        bg='#20a0cc'
    )

def conponentconcept(title, concept):
    return rx.box(
        rx.text(
            title,
            style=st.normal_titles
        ),
        rx.text(
            concept,
            style=st.text
        ),
    )

def headcontent():
    concepts=[
        (
            'Imagen',
            '''
            Es la que contiene las dependencias, bibliotecas, etc. 
            Básicamente es una plantilla o (modelo) que solo tiene lo necesario para ejecutar la aplicación.
            '''
        ),
        (
            'Contenedor',
            '''
            Son instancias o (objetos como en POO), 
            el cual crea la instancia de una imagen.'''
        ),
        (
            'Dockerfile',
            '''
            Es la configuración para la creación de la imagen, 
            acá se define que va a llevar, las instrucciones, dependencias, 
            y configuración del entorno.
            '''
        ),
        (
            'Red',
            '''
            La red virtual la
            permite comunicación entre contenedores, esto es usado en aplicaciones grandes que van a tener varios servicios, 
            es decir se crear varios contenedores de los cuales lleva el micro-servició que va a realizar (backend o la lógica del negocio).
            '''
        ),
        (
            'Volumen',
            '''
            Es donde se guarda los datos generados y usados por los contenedores.
            '''
        )
    ]
    return rx.center(
        rx.vstack(
            rx.box(
                rx.image(
                    src='/dockerlogo.png',
                    width='250px',
                    margin='auto',
                    margin_top='4.5em',
                    align='center'
                ),
                width='100%'
            ),
            rx.text(
                'Conceptos de Docker',
                style=st.bold_titles
            ),
            *[
                conponentconcept(title, concept)
                for title, concept in concepts
            ],
            rx.text(
                'Notas:',
                style=st.normal_titles
            ),
            rx.list.unordered(
                rx.list.item(
                    'Cree una cuenta de ',
                    rx.link(
                        rx.text(
                            'docker hub',
                            color='#ffffff',
                            display='contents'
                        ),
                        href='https://hub.docker.com/',
                        is_external=True,
                        style={
                            'color': '#ffffff',
                            'text_decoration':'underline',
                            'text_decoration_color':'#ffffff'
                        }
                    ),
                    style=st.text
                ),
                rx.list.item(
                    'Algunos comandos como por ejemplo build, compose requieren que estes en el directorio donde creaste los archivos, para que funcionen.',
                    style=st.text
                )
            ),
            width=['90%','85%','80%','75%','70%']
        ),
        width='100%'
    )