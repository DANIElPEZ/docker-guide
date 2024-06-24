import reflex as rx
from dockerweb.components.command import linecode
from dockerweb.components.head import navbar, headcontent
import dockerweb.meta as rxd
import dockerweb.components.styles as st

def linecodedocument(command:str):
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
                    rx.code_block(
                        command,
                        background='rgba(0,0,0,0)',
                        color='#fff',
                        padding='0',
                        margin='0',
                        language='docker',
                        theme='material-dark'
                    ),
                    type="auto",
                    scrollbars="horizontal",
                    padding_bottom='5px',
                    color='#ffffff'
                )
            ),
            size="2",
            background_color='rgb(12,107,165)',
            margin_y='10px'
        ),
        width='100%',
        padding_y='0'
    )

def title_or_content(text:str,style,id:str | None = None):
    return rx.box(
            rx.text(
                text,
                style=style,
                id=id
            ),
            width='100%',
            padding_y='0'
        )

def maincontent():
    return rx.center(
        rx.vstack(
            rx.text(
                'Comandos de Docker',
                style=st.bold_titles,
                width='100%',
                align="center",
                margin_top='60px',
                margin_bottom='-10px'
            ),

            title_or_content('Contenedores',st.bold_titles),

            title_or_content('Crear Contenedor',st.normal_titles,'crearcontenedor'),
            linecode(f'docker run nombre_contenedor'),

            title_or_content('Alias (nuevo nombre)',st.normal_titles,'aliascontenedor'),
            title_or_content('Se utiliza para cambiar el nombre en NAMES y no usar el CONTAINER ID.',st.text),
            linecode('docker run –name nombre_alias nombre_contenedor'),

            title_or_content('Listar contenedores',st.normal_titles,'listarcontenedor'),
            title_or_content('Con este comando ves todos los contenedores.',st.text),
            linecode('docker ps -a'),
            title_or_content('Y con este ves los contenedores que están corriendo.',st.text),
            linecode('docker ps'),

            title_or_content('Borrar contenedor',st.normal_titles,'borrarcontenedor'),
            title_or_content('Con este comando borras el contenedor con el respectivo nombre.',st.text),
            linecode('docker rm nombre_contenedor'),
            title_or_content('Con este comando borras todos los contenedores.',st.text),
            linecode('docker container prune'),

            title_or_content('Correr contenedor',st.normal_titles,'corrercontenedor'),
            title_or_content('En este caso, se está corriendo un contenedor que tiene Ubuntu.',st.text),
            linecode('docker run –d --name Linux Ubuntu'),
            title_or_content('El "-d" evita entrar en modo interactivo (entrar al contenedor o línea de comandos). Para entrar al modo interactivo, usa "-it".',st.text),
            linecode('docker exec –it nombre_contenedor bash'),

            title_or_content('Detener contenedor',st.normal_titles,'detenercontenedor'),
            title_or_content('Para detener un contenedor en windows es con.',st.text),
            linecode('docker kill nombre_contenedor'),
            title_or_content('Y en Linux puedes obtener el ID del proceso con',st.text),
            linecode('docker inspect nombre_contenedor –format ‘{{.State.Pid}}'),

            title_or_content('Exponer contenedor',st.normal_titles,'exponercontenedor'),
            title_or_content('Ahora vamos a exponer un puerto de un contenedor usando la imagen nginx. Los números son los puertos: el de la izquierda es el puerto de la máquina anfitriona y el de la derecha es el puerto del contenedor.',st.text),
            linecode('docker run –d –name proxy –p 8001:80 nginx'),

            title_or_content('Datos',st.bold_titles),

            title_or_content('Persistir datos (Bind mount)',st.normal_titles,'bindmount'),
            title_or_content('Esta forma de persistir datos es la menos recomendable ya que tiene acceso directo a la carpeta.',st.text),
            linecode('docker run –d –name db –v C:/ruta/directorio/carpeta_persistir_datos/mongo mongo'),

            title_or_content('Crear volumen',st.normal_titles,'crearvolumen'),
            title_or_content('La creación de volúmenes es la más común y segura. Para crear un volumen, se utiliza el siguiente comando.',st.text),
            linecode('docker volumen créate nombre_volumen'),
            title_or_content('Ejemplo práctico: en "dst", se especifica el directorio interno del contenedor donde se guardarán los datos.',st.text),
            linecode('docker run -d --name db --mount src=nombre_volumen,dst=/data/db mongo'),

            title_or_content('Insertar archivos',st.normal_titles,'insertararchivos'),
            title_or_content('Para insertar archivos, es importante que el contenedor esté corriendo. Puedes crear un archivo y luego pegarlo dentro del contenedor.',st.text),
            linecode('docker cp ruta_del_archivo_en_host nombre_container:/ruta/dentro/del/contenedor'),

            title_or_content('Extraer archivos',st.normal_titles,'extraerarchivos'),
            title_or_content('Ahora para extraer archivos haces lo mismo de forma opuesta con.',st.text),
            linecode('docker cp nombre_container:/ruta/dentro/del/contenedor ruta/a/guardar/computador/anfrition”'),

            title_or_content('Imágenes',st.bold_titles),

            title_or_content('Listar imagenes',st.normal_titles,'listarimagen'),
            linecode('docker image ls'),

            title_or_content('Descargar imagen',st.normal_titles,'descargarimagen'),
            title_or_content('La imagen se descarga de Docker Hub',st.text),
            linecode('docker pull nombre_imagen_docker_hub'),

            title_or_content('Crear imagen',st.normal_titles,'crearimagen'),
            title_or_content('Para crear imagen se crea un dockerfile',st.text),
            linecodedocument(
'''
#descargar imagen de docker hub
FROM ubuntu:latest
#ejecutar un comando (este se ejecuta en tiempo de construcción)
RUN touch /usr/src/holamrxd.txt
'''
            ),

            title_or_content('Construir imagen',st.normal_titles,'construirimagen'),
            title_or_content('Ahora ya que tienes el dokerfile, vas a construir la imagen con.',st.text),
            linecode('docker build –t ubuntu:tutag .'),
            title_or_content('El "." se refiere al directorio actual',st.text),

            title_or_content('Borrar imagen',st.normal_titles,'borrarimagen'),
            title_or_content('Para borrar la imagen es importante que lleve el tag.',st.text),
            linecode('docker image rm nombre_imagen:tag'),

            title_or_content('Cambiar nombre del tag',st.normal_titles,'cambiarnombredeltag'),
            title_or_content('Cambia el nombre a uno personal y poder publicarlo en docker hub.',st.text),
            linecode('docker tag ubuntu:mrxd name:tag'),

            title_or_content('Publicar imagen',st.normal_titles,'publicarimagen'),
            title_or_content('Primero haces.',st.text),
            linecode('docker login'),
            title_or_content('Y despues publicas la imagen con.',st.text),
            linecode('docker push usernamedelhub/name:tag'),

            title_or_content('Historial de una imagen',st.normal_titles,'historialimagen'),
            linecode('docker history name: tag'),

            title_or_content('Ejemplo Practico',st.normal_titles,'ejemplopractico'),
            title_or_content('Clona repositorio',st.text),
            linecode('git clone https://github.com/platzi/docker'),
            title_or_content('Modifica el dockerfile a',st.text),
            linecodedocument(
'''
# Usa una imagen base de Node.js
FROM node:14

# Copia package.json y package-lock.json al directorio /usr/src/ en el contenedor
COPY ["package.json", "package-lock.json", "/usr/src/"]

# Establece /usr/src/ como el directorio de trabajo dentro del contenedor
WORKDIR /usr/src

# Ejecuta npm install para instalar las dependencias definidas en package.json
RUN npm install

# Copia todo el contenido del directorio actual al directorio de trabajo en el contenedor
COPY [".", "/usr/src/"]

# Expone el puerto 3000 para que la aplicación sea accesible
EXPOSE 3000

# Define el comando por defecto para ejecutar la aplicación
CMD ["node", "index.js"]
'''
            ),
            title_or_content('Consturye la imagen',st.text),
            linecode('docker build -t mrnode .'),
            title_or_content('Y luego corre la imagen',st.text),
            linecode('docker run -–rm –p 3000:3000 –v C:/Users/…/docker/index.js:/usr/src/index.js mrnode'),
            title_or_content('El "--rm" elimina el contenedor cuando se detenga',st.text),

            title_or_content('Redes',st.bold_titles),

            title_or_content('Listar redes',st.normal_titles,'listarred'),
            linecode('docker network ls'),

            title_or_content('Crear una red',st.normal_titles,'crearred'),
            linecode('docker network créate –-attachable nombre_red'),
            title_or_content('Este parametro "--attachable" permite que cualquier contenedor se conecte a esta red',st.text),

            title_or_content('Conectarse a una red',st.normal_titles,'conectarseaunared'),
            title_or_content('Crea dos contenedores uno con mongo y otro con node; el de mongo lo conectas.',st.text),
            linecode('docker network connect nombre_red nombre_contenedor'),
            title_or_content('Y el contenedor de node lo conectas de esta manera.',st.text),
            linecode('docker run -d --rm --name appweb --network cable -p 3000:3000 --env MONGO_URL=mongodb://db:27017/test -v C:/…/index.js:/usr/src/index.js mrnode'),
            title_or_content('"env" es una variable de entorno.',st.text),

            title_or_content('Docker compose',st.bold_titles,'dockercompose'),

            title_or_content('Esta herramienta nos ayuda a hacer todo de forma más sencilla de forma declarativa, es importante la indentacion como en Python. Ahora crea un archivo "docker-compose.yml".',st.text),
            linecodedocument(
'''
version: "3.8"

services:
  app:
    image: mrnode
    environment:
      MONGO_URL: "mongodb://db:27017/test"
    depends_on:
      - db
    ports:
      - "3000:3000"

  db:
    image: mongo
'''
        ),
        title_or_content('Ahora ejecutas esto. Aclaracion mrnode es la "imagen" que yo cree previamente.',st.text),
        linecode('docker-compose up -d'),
        title_or_content('Para entrar en modo interactivo ejecutas.',st.text),
        linecode('docker-compose exec app bash'),
        title_or_content('"app" es el nombre del servicio de la seccion de "services" en el archivo docker compose. Ahora para destruir todo lo haces con.',st.text),
        linecode('docker-compose down'),
        title_or_content('Construir imagen con docker-compose',st.normal_titles),
        title_or_content('Ejemplo con mongoDB.',st.text),
        linecodedocument(
'''
version: "3.8"

services:
  app:
    build: .
    environment:
      MONGO_URL: "mongodb://db:27017/test"
    depends_on:
      - db
    ports:
      - "3000:3000"

  db:
    image: mongo

'''
        ),
        title_or_content('Y para construir lo hace con.',st.text),
        linecode('docker-compose build'),
        title_or_content('Entorno personal con docker-compose',st.normal_titles),
        title_or_content('Cuando necesites un entorno personal, usted puede crear el archivo "docker-compose.override.yml", el archivo “docker-compose.yml” lo deja como viene y en “docker-compose.override.yml” modifica lo que necesita.',st.text),
        linecodedocument(
'''
version: "3.8"

services:
  app:
    build: .
    environment:
      MONGO_URL: "mongodb://db:27017/test"
    depends_on:
      - db
    volumes:
      - .:/usr/src
      - /usr/src/node_modules
    command: npx nodemon index.js

  db:
    image: mongo
'''
        ),

            width=['90%','85%','80%','75%','70%']
        ),
        width='100%'
    )

def footer():
    return rx.center(
        rx.vstack(
            rx.flex(
                rx.spacer(),
                rx.vstack(
                    rx.hstack(
                        rx.link(
                            'Build with reflex',
                            style={
                                'color':'#fff',
                                'text_decoration':'none',
                                'font_size':'15px'
                            },                        is_external=True,
                            href='https://reflex.dev'
                        ),
                        rx.chakra.avatar(
                            src='/rx.png',
                            size="sm"
                        ),
                        align_items='center'
                    ),
                    rx.link(
                        'Creado por DNV',
                        style={
                            'color':'#fff',
                            'text_decoration':'none',
                            'font_size':'15px'
                        },
                        is_external=True,
                        href='https://dnvdev.reflex.run'
                    ),
                ),
                rx.spacer(),
                width='100%'
            ),
            width='100%'
        ),
        padding='20px',
        width='100%'
    )

@rx.page(
    title=rxd.title,
    image=rxd.img,
    description=rxd.description,
    meta=rxd.meta
)
def index():
    return rx.box(
        navbar(),
        headcontent(),
        maincontent(),
        footer(),
        width='100%'
    )

app = rx.App(
    style={
        'background_color':'#0c2739'
    },
    stylesheets=[
        "/styles.css",
    ]
)
app.add_page(index)
