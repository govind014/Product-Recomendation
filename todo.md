
**TO-DO**

*custom-ner formatting*
>>entity-selection.ipynb  :   map <B-I-O> to lowercase category
                              combine similar tags
                              convert to a dict (tag : user utterance)
                              ?? remove <NUMBEROFPRODUCTS>
|
|
|
>>config.py   : update dictionaries 
|
|
|
>>database.py : create new dict
|
|
|
>>DialogueManager calls Ui --> get user Utterance 

--> DialogueManager : #16 self.nlp = NaturalLanguageProcessor() 
------> #123 userAction = nlp.GetSemanticFrame(userUtterance, agentAction)

------> #13 NaturalLanguageProcessor.py : GetSemanticFrame(userInput):
--------------->   *use custom-ner to find slots*
--------------->   GetSlots(), GetIntent()
--------------->   return SemanticFrame
|
|
|
*change gensim to custom-ner*
>>NaturalLanguageProcessor.py  : GetIntent()
                                 GetAction()
                                 GetSlots()
                                 #change to latest gensim??
|
|
|
>>agent.py    : GenerateDoneResponse(), 
                GetEntryFromDb()
|
|
|
>>UserSimulator.py  : 


