FROM ubuntu:22.04
ENV MODEL TheBloke/saiga_mistral_7b-GGUF
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /llm
RUN touch start.sh \
&& echo echo Starting LLM server >> start.sh \
&& echo llm run ${MODEL} 8000 >> start.sh \
&& echo echo LLM server running >> start.sh \
&& echo llm ps >> start.sh \
&& echo tail -f /dev/null >> start.sh \
&& chmod a+x start.sh \
&& useradd -ms /bin/bash --uid 1000 jupyter\
&& apt-get update\
&& apt-get -y upgrade \
&& apt-get install -y python3.10-dev python3.10-distutils curl git build-essential \
&& ln -s /usr/bin/python3.10 /usr/local/bin/python3\
&& ln -s /usr/bin/python3.10 /usr/local/bin/python\
&& curl https://bootstrap.pypa.io/get-pip.py | python3 \
&& git clone https://github.com/GoogleCloudPlatform/localllm \
&& cd localllm \
&& git checkout 14fa964bc4f18aaab387aee1010298138a5344c0 \
&& pip3 install --no-cache-dir --root-user-action=ignore openai \
&& cd llm-tool \
&& pip3 install --no-cache-dir --root-user-action=ignore . \
&& llm pull ${MODEL}

EXPOSE 8000

CMD ["bash","/llm/start.sh"]
