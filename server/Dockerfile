FROM ubuntu:focal

# обновляем репозитории и пакеты
RUN apt update && apt upgrade -y 

# копируем все содержимое в папку
COPY . /app

# рабочая директория по дефолту
WORKDIR /app

# ставим необходимые пакеты
RUN bash config.sh

# ставим питоновские пакеты
RUN poetry install 
