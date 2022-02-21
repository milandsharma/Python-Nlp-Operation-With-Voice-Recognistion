# modules
import speech_recognition as s
import pyttsx3
import nltk
import nltk.corpus
nltk.download('averaged_perceptron_tagger')

# function for operation such as tokenization pos tagging 

def token():
    Army = "i will join indian army as a luitenent ,if i am not selected then i will start youtube channel like colin furze or hacksmith "
    tokenize = nltk.word_tokenize(Army)
    print(tokenize)
def gram():
    data = "machine cant understand human language so far , machine read a natural language as read a word only one time is konwn as unigram, machine read two at same time is known as bigram and unigram, machine read three word at  same time is known as trigram"
    data_tokenize = nltk.word_tokenize(data)
    print()
    print("this is bigram :")
    print(list(nltk.bigrams(data_tokenize)))
    print()
    print("this is trigram : ")
    print(list(nltk.trigrams(data_tokenize)))
    print()
    print("this is ngram : ")
    print(list(nltk.ngrams(data_tokenize, 5)))
def pos():
    hello = "this is dog , from another planet and i am going to kill this dog or maybe call it alein which has differnt biology is compare to earth animal or plants"
    hello_tokenize = nltk.word_tokenize(hello)
    for i in hello_tokenize:
      print(nltk.pos_tag([i]))
    from nltk import ne_chunk
    hello_tag = nltk.pos_tag(hello_tokenize)
    print("this is hello tags  = ", hello_tag)
    hello_ne = ne_chunk(hello_tag)
    print("this is hello ne chunks = ", hello_ne)
def chunk():
    from nltk.corpus import names
    sample = " Vishnu is one of the members in the trimurti in Hinduism. Vishnu is the God of Preservation"
    sampleTokenize = nltk.word_tokenize(sample)
    pos_sample = nltk.pos_tag(sampleTokenize)
    grammer = (r"""
        NP :{<DT>?<JJ>*<NN.*>}
            """)
    chunk = nltk.RegexpParser(grammer)
    tree = chunk.parse(pos_sample)
    tree.draw()
    sample = "Vishnu is one of the members in the trimurti in Hinduism. Vishnu is the God of Preservation"
    token_pos = nltk.pos_tag(nltk.word_tokenize(sample))
    print(token_pos)
    chunkParser = nltk.RegexpParser(grammer)
    tree = chunkParser.parse(pos_sample)
    tree.draw()
# ......................................................................................................................



#                                                HELLO BY SPEECH RECOGNITION 


text_speech = pyttsx3.init()
sr = s.Recognizer()
while True:
    with s.Microphone() as source:
        text_speech.say("hello abhishek kushwah")
        text_speech.runAndWait()
        text_speech.say("hello charan mam")
        text_speech.runAndWait()
        text_speech.say("speak Anything")
        print("speak Anything wait for 2 sec after voice")
        text_speech.runAndWait()
        audio = sr.listen(source)
    try:
        text = sr.recognize_google(audio,language = "en-In")
        print("You said : {}".format(text))
        text_speech.say(str(text))
        text_speech.runAndWait()
        break
    except:
        print("Sorry could not recognize what you said")
        text_speech.say("Sorry could not recognize what you said")
        text_speech.runAndWait()
    
    
# ..........................................................................................



#                                                      OPTION

print("option 1 for Word_tokenize")
text_speech.say("option 1 for Word_tokenize")
text_speech.runAndWait()
print("...............................................................................................................")

print("option you for Ngrams ")
text_speech.say("option you for Ngrams")
text_speech.runAndWait()
print("...............................................................................................................")

print("option free for part of speech")
text_speech.say("option free for part of speech")
text_speech.runAndWait()
print("...............................................................................................................")

print("option chunk for chunking and chinking")
text_speech.say("option chunk for part of speech")
text_speech.runAndWait()
print("...............................................................................................................")




while True:
    option = text_speech.say("please select option")
    text_speech.runAndWait()
    print(option)


    with s.Microphone() as source:
        print("speak Anything wait for 2 sec after voice")
        text_speech.runAndWait()
        audio = sr.listen(source)


    try:
        option = sr.recognize_google(audio, language="en-In")
        print("You said : {}".format(option))
        text_speech.say(str(option))
        text_speech.runAndWait()
    except:
        print("Sorry could not recognize what you said")
        text_speech.say("Sorry could not recognize what you said")
        text_speech.runAndWait()
    
    
    
    this = str(option)
    if this == "1":
     print(token())
    if this == "you":
     print(gram())
    elif this == "free":
     print(pos())
    elif this == "Jung":
     print(chunk())





