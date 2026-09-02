# Instrucciones de configuración para Isabel y Ana

Sigue exactamente estos pasos para dejar el proyecto funcionando y trabajar en tus ramas:

1) Clonar el repositorio

Abre la terminal en la carpeta donde guardas tus proyectos y ejecuta:

```bash
git clone URL_DE_TU_REPOSITORIO.git
cd inventario_django
```

2) Crear y activar tu entorno virtual

- En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

- En Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Nota: la carpeta `venv/` no debe subirse a Git.

3) Instalar dependencias

Con el entorno virtual activado, ejecuta:

```bash
pip install -r requirements.txt
```

4) Crear la base de datos en MariaDB local

Abre tu cliente de MariaDB/MySQL (HeidiSQL, DBeaver o la consola) y ejecuta:

```sql
CREATE DATABASE inventariodb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

5) Configurar el archivo `.env`

Por seguridad el archivo `.env` no se sube a Git. Duplica o renombra el archivo `.env.example` y llámalo exactamente `.env`.

Edita el `.env` y coloca la contraseña de tu MariaDB local, por ejemplo:

```
DB_NAME=inventariodb
DB_USER=root
DB_PASSWORD=TU_CONTRASEÑA_LOCAL
DB_HOST=127.0.0.1
DB_PORT=3306
```

6) Aplicar migraciones

Para crear las tablas necesarias ejecuta:

```bash
python manage.py migrate
```

7) (Opcional) Crear y cambiar a tu rama de trabajo

Cada una debe trabajar en su propia rama. Por ejemplo:

```bash
git checkout -b feature/nombre-tu-rama
# trabajar, commitear, luego:
git push -u origin feature/nombre-tu-rama
```

8) Ejecutar el servidor local (comprobación)

```bash
python manage.py runserver
```

Notas finales

- No subas `venv/` ni `.env` al repositorio.
- Si no existe `.env.example`, dímelo y lo creo con un ejemplo mínimo.
- ¿Quieres que cree este `README.md` en el repositorio y haga un commit y push? Si sí, indícame la rama destino para el commit.
