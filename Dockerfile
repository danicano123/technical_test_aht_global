# Usar la imagen base de Python 3.12
FROM python:3.12

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto en el que corre Flask
EXPOSE 8888

# Comando para ejecutar la aplicación
CMD ["python", "index.py"]