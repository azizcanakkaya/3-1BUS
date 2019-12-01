"""
Zemberek: Word Analysis Example
Documentation: https://bit.ly/2MTmfr1
Java Code Example: https://bit.ly/2MV2Hmj
"""

from os.path import join

from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM

from gensim.models import KeyedVectors

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
    word: str = input("Alan girin: ")
    results: morphology = morphology.analyze(JString(word))
    for result in results:
        temp = result.getStem()
    
print (temp)
    
    ##shutdownJVM()


word_vectors = KeyedVectors.load_word2vec_format('trmodel', binary=True)
word = word_vectors.most_similar(positive=[wordok])
word_list = []
for i in range(len(word)):
    word_list.append(word[i][0])
    
    
    
results0: morphology = morphology.analyze(JString(word_list[0]))
results1: morphology = morphology.analyze(JString(word_list[1]))
results2: morphology = morphology.analyze(JString(word_list[2]))
results3: morphology = morphology.analyze(JString(word_list[3]))
results4: morphology = morphology.analyze(JString(word_list[4]))
results5: morphology = morphology.analyze(JString(word_list[5]))
results6: morphology = morphology.analyze(JString(word_list[6]))
results7: morphology = morphology.analyze(JString(word_list[7]))
results8: morphology = morphology.analyze(JString(word_list[8]))
results9: morphology = morphology.analyze(JString(word_list[9]))

print("Öneri 1: \n")
for result in results0:
    print('İsim: ',result.getStem()+temp)
for result in results0:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results0:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')

print("Öneri 2: \n")
for result in results1:
    print('İsim: ',result.getStem()+temp)
for result in results1:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results1:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')

print("Öneri 3: \n")
for result in results2:
    print('İsim: ',result.getStem()+temp)
for result in results2:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results2:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')
    
print("Öneri 4: \n")
for result in results3:
    print('İsim: ',result.getStem()+temp)
for result in results3:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results3:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')
    
print("Öneri 5: \n")
for result in results4:
    print('İsim: ',result.getStem()+temp)
for result in results4:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results4:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')
    
print("Öneri 6: \n")
for result in results5:
    print('İsim: ',result.getStem()+temp)
for result in results5:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results5:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')

print("Öneri 7: \n")
for result in results6:
    print('İsim: ',result.getStem()+temp)
for result in results6:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results6:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')
    
print("Öneri 8: \n")
for result in results7:
    print('İsim: ',result.getStem()+temp)
for result in results7:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results7:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')

print("Öneri 9: \n")
for result in results8:
    print('İsim: ',result.getStem()+temp)
for result in results8:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results8:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')

print("Öneri 10: \n")
for result in results9:
    print('İsim: ',result.getStem()+temp)
for result in results9:
    print('Web Site: www.',result.getStem()+temp,'.com')
for result in results9:
    print('Sosyal Medya: ',result.getStem()+temp,'\n')


shutdownJVM()    
    
    