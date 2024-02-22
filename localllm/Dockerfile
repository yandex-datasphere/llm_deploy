FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive
RUN useradd -ms /bin/bash --uid 1000 jupyter\
&& apt update\
&& apt install -y python3.10-dev python3.10-distutils curl\
&& ln -s /usr/bin/python3.10 /usr/local/bin/python3\
&& ln -s /usr/bin/python3.10 /usr/local/bin/python\
&& curl https://bootstrap.pypa.io/get-pip.py | python3
RUN git clone https://github.com/GoogleCloudPlatform/localllm \
&& pip3 install --root-user-action=ignore openai 
COPY llm-tool llm-tool
RUN cd llm-tool && pip install --root-user-action=ignore .

ENTRYPOINT ["llm",\
            "run",\
            "TheBloke/Mistral-7B-Instruct-v0.2-GGUF",\
            "8000"]


