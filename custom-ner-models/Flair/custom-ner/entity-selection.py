from flair.data import Sentence
from flair.models import SequenceTagger

model = SequenceTagger.load('H:\\Product-Recomendation\\custom-ner-models\\Flair\\custom-ner\\best-model-2.pt')

tags = ["<B-PRICING>","<I-PRICING>", "<O-PRICING>",
        "<B-PRODUCTNAME>", "<I-PRODUCTNAME>", "<O-PRODUCTNAME>",
        "<B-CATEGORY>", "<I-CATEGORY>", "<O-CATEGORY>",
        "<B-CITY>", "<I-CITY>", "<O-CITY>",
        "<B-NUMBEROFPRODUCTS>", "<I-NUMBEROFPRODUCTS>", "<O-NUMBEROFPRODUCTS>",
        "<B-TIME>", "<I-TIME>", "<O-TIME>"]

def entitySelection(input_):
    """ Get user input -> find NER from it -> return dictionary of found entities"""

    sentence = Sentence(input_)
    model.predict(sentence)
    #print(sentence.to_tagged_string())
    out = sentence.to_tagged_string()

    slot_key = []
    slot_value = []
    outList = out.split()
    for i in range(len(outList)):
        for tag in tags:
            #print(tag, outList)
            if outList[i] == tag:
                #print(outList[i-1], tag)
                slot_key.append(outList[i][3:-1].lower())
                slot_value.append(outList[i-1])

    slot_dict = {}
    for i in range(len(slot_key)):
        slot_dict.setdefault(slot_key[i], [])
        if slot_key[i] in slot_dict.keys():
            slot_dict[slot_key[i]].append(slot_value[i])
    print(slot_dict)



if __name__ == "__main__":
    print("Start")
    inp  = str(input("Enter query : "))
    entitySelection(inp)