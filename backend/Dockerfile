FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код (включая alembic)
COPY . .

# Создаём папки для статики и логов
RUN mkdir -p static logs

EXPOSE 8000

# Запуск с миграциями
CMD alembic upgrade head && \
    uvicorn main:app --host 0.0.0.0 --port 8000