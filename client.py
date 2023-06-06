from jina import Client, DocumentArray,Document


if __name__ == '__main__':
    c = Client(host='http://172.66.1.189', port=54322)
    d = Document(uri='/home/yingtie/PycharmProjects/text_to_image/cat.png', mime_type='image/png', modality='image')
    input_da = DocumentArray()
    input_da.append(d)
    print(f'd.uri:',d.uri)
    input_da.summary()
    da = c.post('/', inputs=input_da, show_progress=True, timeout=3600)
    da.summary()
    print('=======>>')
    print(f'embedding:', da.embeddings)


