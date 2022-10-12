# Formulario CRUD con Django-REST y Sqlite 

Este proyecto esta hecho con el Framework Django-Rest, estructurando una api REST CRUD que guarda los datos en una base de datos sqlite

* Back: Python (Django-rest)

Sistemas operativos usados:

* Windows 10 Pro
* Linux Debian 11

Python version: 3.10.7

# Introduccion

* 1. Creando un entorno virtual

* i.i Instalando requerimientos
* i.ii Iniciar el servidor

## 1. Creando un entorno virtual

Primero debemos asegurarnos de tener instalado Python y Git. 

En Linux, debemos instalar python3-venv despues de tener Python3

En una consola de Debian corremos lo siguiente:

```cmd
sudo apt install python3-venv
```
En una consola de windows ('cmd.exe') o Linux (konsole), correr el siguiente comando:

* Crear un entorno virtual en el directorio actual llamado 'myvenv'
```cmd
python -m venv myvenv
```
* Activar el entorno virtual que esta ubicado en myvenv/

- Linux
```cmd
source myvenv/bin/activate
```
- Windows
```cmd
myvenv\Scripts\activate
```
* Actualizar pip (Linux y Windows)
```cmd
python -m pip install --upgrade pip
```
* Clonar este repositorio (Linux y Windows)
```cmd
git clone https://github.com/OscarRPi/Django-Form.git
```

```cmd
cd Django-Form
```

### 1.1 Instalando requerimientos (Linux y Windows)

```cmd
pip install -r requirements.txt
```

### 1.2 Iniciar el servidor de Back (Linux y Windows)

```cmd
python manage.py runserver
```
En la consola aparecera la direccion y el puerto que debemos abrir (http://127.0.0.0.1:8000)

Copiar esta direccion y en un navegador buscar esta url

Este end-point responderá a las peticiones GET/PUT/POST/DELETE
