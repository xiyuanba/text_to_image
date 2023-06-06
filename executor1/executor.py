from jina import Executor, requests, DocumentArray,Document


class ImageReader(Executor):
    @requests(on='/')
    def transform(self, docs: DocumentArray, **kwargs):
        print("in step ImageReader")
        for doc in docs:
            print(f'Loading image from {doc.uri}...')
            blob = doc.load_uri_to_blob()
            if isinstance(blob, bytes):
                doc.blob = blob
                print('Image loaded successfully.')
                print(f'Blob type: {type(doc.blob)}')
            else:
                doc.buffer = blob
                print('Failed to load image.')
                print(f'Buffer type: {type(doc.buffer)}')


class ReturnBlob(Executor):
    def print_embedding(self, docs: DocumentArray, **kwargs):
        print("in step ReturnBlob")
        print(docs.summary())