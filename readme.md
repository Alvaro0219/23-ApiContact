# API de Contactos con Flask y SQLAlchemy

## Descripción

Esta es una API REST simple creada con Flask y SQLAlchemy para gestionar una lista de contactos. Puedes realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la lista de contactos.

## Cómo usar la API

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/Alvaro0219/23-ApiContact.git
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta la aplicación:

    ```bash
    flask --app app --debug run
    ```

La aplicación estará disponible en: `http://127.0.0.1:5000`

## Endpoints

### 1. Obtener todos los contactos

- **URL:** `GET /contacts`
- **Descripción:** Obtiene la lista completa de contactos.
- **Cómo realizar la solicitud en Postman:**
  - Método: `GET`
  - URL: `http://127.0.0.1:5000/contacts`

### 2. Crear un nuevo contacto

- **URL:** `POST /contacts`
- **Descripción:** Crea un nuevo contacto.
- **Cómo realizar la solicitud en Postman:**
  - Método: `POST`
  - URL: `http://127.0.0.1:5000/contacts`
  - Cuerpo (raw JSON):
    ```json
    {
      "name": "Nombre del contacto",
      "email": "correo@example.com",
      "phone": "123456789"
    }
    ```

### 3. Obtener un contacto por ID

- **URL:** `GET /contacts/{id}`
- **Descripción:** Obtiene un contacto específico por su ID.
- **Cómo realizar la solicitud en Postman:**
  - Método: `GET`
  - URL: `http://127.0.0.1:5000/contacts/{id}` (reemplaza `{id}` con el ID del contacto deseado)

### 4. Actualizar un contacto por ID

- **URL:** `PUT /contacts/{id}` o `PATCH /contacts/{id}`
- **Descripción:** Actualiza un contacto específico por su ID.
- **Cómo realizar la solicitud en Postman:**
  - Método: `PUT` o `PATCH`
  - URL: `http://127.0.0.1:5000/contacts/{id}` (reemplaza `{id}` con el ID del contacto deseado)
  - Cuerpo (raw JSON):
    ```json
    {
      "name": "Nuevo nombre",
      "email": "nuevo_correo@example.com",
      "phone": "987654321"
    }
    ```

### 5. Eliminar un contacto por ID

- **URL:** `DELETE /contacts/{id}`
- **Descripción:** Elimina un contacto específico por su ID.
- **Cómo realizar la solicitud en Postman:**
  - Método: `DELETE`
  - URL: `http://127.0.0.1:5000/contacts/{id}` (reemplaza `{id}` con el ID del contacto deseado)
