import ast
import hashlib
import io
import math
from pathlib import Path
import unittest

APP = Path(__file__).resolve().parents[1] / 'app.py'
class FakeArray(list):
    pass
class NP:
    float32 = float
    @staticmethod
    def ascontiguousarray(value, dtype=None): return value
    log = staticmethod(math.log)
class Encoder:
    def encode(self, *args, **kwargs): return [[1.0]]
class Index:
    ntotal = 4
    def search(self, vector, k): return [[1.0]], [[0]]
class Page:
    def extract_text(self): return ' '.join('word'+str(i) for i in range(250))
class Reader:
    def __init__(self, data): self.pages = [Page()]

def helpers():
    tree = ast.parse(APP.read_text(encoding='utf-8'))
    names = {'retrieve', 'chunk_pdf', 'index_key'}
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    scope = dict(np=NP, load_encoder=lambda: Encoder(), hashlib=hashlib,
                 io=io, PdfReader=Reader, MODEL='test-model', CHUNK_WORDS=120,
                 OVERLAP=25)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(APP), 'exec'), scope)
    return scope

class HelpersTest(unittest.TestCase):
    def test_chunk_overlap_and_page(self):
        chunks = helpers()['chunk_pdf'](b'pdf')
        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0]['text'].split()[-25:], chunks[1]['text'].split()[:25])
        self.assertTrue(all(c['page'] == 1 for c in chunks))
    def test_cache_identity_changes(self):
        scope = helpers(); key = scope['index_key']
        self.assertEqual(key(b'a'), key(b'a'))
        self.assertNotEqual(key(b'a'), key(b'b'))
        old = key(b'a'); scope['CHUNK_WORDS'] = 121
        self.assertNotEqual(old, key(b'a'))
    def test_keyword_recovers_nonsemantic_page(self):
        chunks = [{'page':5,'text':'attention heads'},
                  {'page':5,'text':'encoder attention'},
                  {'page':7,'text':'Hardware and schedule eight GPUs'},
                  {'page':7,'text':'base training twelve hours'}]
        result = helpers()['retrieve']('What hardware and schedule?', Index(), chunks, 1)
        self.assertIn(2, [c['chunk_id'] for c in result])
        self.assertIn(3, [c['chunk_id'] for c in result])
        self.assertEqual(len(result), len({c['chunk_id'] for c in result}))
    def test_neighbor_does_not_cross_page(self):
        chunks = [{'page':1,'text':'alpha'}, {'page':2,'text':'beta'},
                  {'page':2,'text':'gamma'}, {'page':2,'text':'delta'}]
        result = helpers()['retrieve']('unmatched', Index(), chunks, 1)
        self.assertEqual([c['chunk_id'] for c in result], [0])

if __name__ == '__main__': unittest.main()
