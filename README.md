# Запуск открытых LLM в облаке Yandex Cloud

Данный репозиторий содержит несколько примеров того, как можно развернуть открытые большие языковые модели (LLM) в своём облаке Yandex Cloud.

Вы можете запустить LLM на ресурсах с CPU или с GPU, выбрав один из приведённых ниже способов деплоймента.

CPU/GPU | Библиотека | Инструкции | Комментарии 
--------|------------|------------|------------
CPU | Google [localllm](https://github.com/GoogleCloudPlatform/localllm) | [Читать](localllm/README.md) | Используем квантизированные модели для ускорения работы
GPU | [vLLM](https://github.com/vllm-project/vllm) | [Читать](vLLM/README.md) | Работает только на GPU
CPU/GPU | [FastAPI](https://github.com/fastapi/fastapi) | [Читать](fastapi/Dockerfile) | NOT OAI compatible, 1 parallel request max
CPU | [Ollama](https://github.com/ollama/ollama) | [Читать](ollama/README.md) | NOT OAI compatible, >1 parallel requests, [Как?](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-does-ollama-handle-concurrent-requests)

Описанные выше способы предоставляют OpenAI-совместимое API, что позволяет использовать развёрнутые таким образом модели из большинства популярных фреймворков. Пример использования моделей из LangChain содержится в [examples/langchain_demo.py](examples/langchain_demo.py).

Ollama не поддерживает OpenAI-совместимое API, но его также можно использовать с langchain через библиотеку langchain-ollama.
