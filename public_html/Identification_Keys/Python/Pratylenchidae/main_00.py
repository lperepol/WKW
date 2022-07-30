# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
import json

def label2(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    str = ""
    for i in grouped_words:
        str = str + i + "\n"
    return str

def toJSON(dot):
    json_string = dot.pipe('json').decode()
    # parse the resulting json_string
    json_dict = json.loads(json_string)

    # now, you have a JSON dictionary that has two relevant keys:
    # 'objects' for nodes and 'edges' for, well, edges.
    # you can iterate over the nodes and get the (x,y) position for each node as follows:
    for obj in json_dict['objects']:
        print(obj['name'], '\t', obj['pos'])

def draw():
    GraphTitle = 'Key to Pratylenchidae\nan adapatation from:\n\nPratylenchus (Nematoda:\nPratylenchidae): Diagnosis, Biology,\nPathpgenicity And Management\n\nPablo Castillo et al\n\n\n\n'
    g = Digraph('Pratylenchus Key', comment="FOO",filename = 'PratylenchusKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    g.graph_attr['rankdir'] = 'LR'
    g.attr(labelloc='t')
    g.attr(label=GraphTitle)

    g.node('1',label='Pratylenchus')
    g.edge('1', '2', label=label2('Labial region with two annuli'))
    g.edge('1', '28', label=label2('Labial region with three annuli'))
    g.edge('1', '65', label=label2('Labial region with four annuli'))

    g.edge('2', '3', label=label2('Males absent, spermatheca empty'))
    g.edge('2', '8', label=label2('Males generally common, spermatheca filled with sperm'))

    g.edge('3', 'P. angulatus', label=label2('Stylet length < 13 μm'))
    g.edge('3', '4', label=label2('Stylet length > 13 μm'))

    g.edge('4', 'P. acuticaudatus', label=label2('Spermatheca absent or reduced'))
    g.edge('4', '5', label=label2('Spermatheca well developed'))

    g.edge('5', 'P. crassi', label=label2('Vulva position < 75%'))
    g.edge('5', '6', label=label2('Vulva position <= 75%'))

    g.edge('6', '7', label=label2('Post-vulval uterine sac < 16 μm'))
    g.edge('6', 'P. hippeastri', label=label2('Post-vulval uterine sac 30-35 μm long'))

    g.edge('7', 'P. tenuis', label=label2('Female tail tip smooth'))
    g.edge('7', 'P. estoniensis', label=label2('Female tail tip striated'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.edge('8', 'XX', label=label2('xx'))
    g.edge('8', 'XX', label=label2('xx'))

    g.render('PratylenchusKey.gv', format='svg', view=True)
    #g.render('PratylenchusKey.gv', format='jpg', view=False)
    #g.render('PratylenchusKey.gv', format='pdf', view=False)

def main():
    # Use a breakpoint in the code line below to debug your script.
    draw()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
