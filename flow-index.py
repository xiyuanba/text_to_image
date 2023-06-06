from jina import Flow,Document,DocumentArray
import os

f = Flow().add(
    uses='ImageReader',
    py_modules='executor1/executor.py',
    name='image_loader'
).add(
    name='image_encoder',
    uses='jinaai+docker://jina-ai/CLIPImageEncoder:latest',
    volumes='$HOME/.cache/huggingface:/root/.cache/huggingface',
    timeout_ready=600000,
    read_only=True,
    needs='image_loader'
)
docs = DocumentArray()
doc = Document(uri='/home/yingtie/PycharmProjects/text_to_image/cat.png')
docs.append(doc)
with f:
    f.index(docs)
