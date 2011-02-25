import dumbo
from collections import defaultdict

def mapper(key, value):
    for trans in value.split():
        yield trans.split("::")

def reducer(key, values):
    translation_counts = defaultdict(int)
    for value in values:
        translation_counts[value] += 1
    
    total_translations = float(sum(translation_counts.values()))
    for word in translation_counts:
        yield (key, word, translation_counts[word]/total_translations)

if __name__ == '__main__':
    dumbo.run(mapper, reducer)