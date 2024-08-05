# Используем официальный образ Ubuntu 22.04
FROM ubuntu:22.04

# Устанавливаем рабочую директорию
WORKDIR /root/.ollama

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y curl

# Копируем скрипт в контейнер
COPY entrypoint.sh /root/.ollama/entrypoint.sh

# Делаем скрипт исполняемым
RUN chmod +x /root/.ollama/entrypoint.sh

# Устанавливаем ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Открываем порт 11434 для доступа к модели
EXPOSE 11434

# Устанавливаем скрипт в качестве точки входа
ENTRYPOINT ["/root/.ollama/entrypoint.sh"]
