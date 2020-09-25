from nltk import word_tokenize,pos_tag
from py2neo import Graph,Node,Relationship

graph = Graph(password="123")
def create_graph(node,rel):
    node1 = Node("Catagory", name=node[0])
    node2 = Node("Catagory", name=node[1])
    relation = Relationship.type(rel)
    graph.merge(relation(node1, node2), "category", "name")

sen = input("enter sen")

tokens = word_tokenize(sen)
print(tokens)
list = pos_tag(tokens)
print(list)
node = []
rel = ""
for x in list:
    if(x[0] == "son"):
        rel = "is_son_of"
    elif (x[0] == "sits"):
        rel = "sits_in_a"
    elif (x[1] == "NNP" or x[1] == "NN" or x[1] == "NNS" or x[1] == "NNPS" or x[1] == "JJ"):
        node.append(x[0])

    elif (x[1] == "VB" or x[1] == "VBD" or x[1] == "VBG" or x[1] == "VBN" or x[1] == "VBP" or x[1] == "VBZ"):
        rel = x[0]

    if len(node) == 2 and rel != "":
        print("nouns are: ", node)
        print("rel is: ", rel)
        create_graph(node, rel)
        node = []
        rel = ""
    if (x[0] == "," or x[0] == "."):
        node = []
        rel = ""