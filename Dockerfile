# Establece la imagen base como Python 3.10
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias definidas en requirements.txt
RUN pip install -r requirements.txt

# Copia el contenido del directorio "app" al directorio de trabajo
COPY app .

# Expone el puerto 5000 para la app flask
EXPOSE 5000

# Variable de entorno para Flask
ENV FLASK_APP=calc.py

# Comando que se ejecutará cuando se inicie el contenedor
CMD ["flask", "run", "--host=0.0.0.0"]