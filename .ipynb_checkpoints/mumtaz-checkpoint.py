# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Zemberek: Word Analysis Example
Documentation: https://bit.ly/2MTmfr1
Java Code Example: https://bit.ly/2MV2Hmj
"""

from gensim.models import KeyedVectors

from os.path import join

from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM

word_vectors = KeyedVectors.load_word2vec_format('trmodel', binary=True)
word = word_vectors.most_similar(positive=["informatik"])
word_list = []
for i in range(len(word)):
    word_list.append(word[i][0])
for i in range(len(word_list)):
    print(word_list[i])

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join( 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()
    word: str = 'ruhbilim'
    results: morphology = morphology.analyze(JString(word))
    for result in results:
        print(result.getStem())

    shutdownJVM()