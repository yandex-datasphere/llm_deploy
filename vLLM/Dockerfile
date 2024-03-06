FROM vllm/vllm-openai
ENTRYPOINT []

# use --dtype=half to make it work on V-100 in DataSphere
# awq quantization is not supported on V-100
CMD [ \
    "python3",\
    "-m", "vllm.entrypoints.openai.api_server",\
    "--model","IlyaGusev/saiga_mistral_7b_merged",\
    "--dtype=half" \
    ]