# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph

def label2(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    str = ""
    for i in grouped_words:
        str = str + i + "\n"
    return str


def draw():
    #http://nemaplex.ucdavis.edu/Uppermnus/nematamnu.htm#Taxonomic_Keys
    #http://nemaplex.ucdavis.edu/Taxadata/Dorylaimida%20Andrassy%202009.html
    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'

    GraphTitle = 'Key to the Families\nand Genera of the\nOrder Dorylaimida\n Andrassy 2009'
    g.node('000', label=GraphTitle,fillcolor='red',style="filled")
    g.edge('000', '001', label2(''))

    g.node('001', '001',fillcolor='aqua',style="filled" )
    g.edge('001','002', label2('Nygolaimina Stoma with subventral mural tooth, stoma wide, cardia with 3 gland cells'))
    g.edge('001','017', label2('Dorylaimina Stoma with axial odontostyle, stoma narrow, cardia small, without gland cells'))

    g.node('002', '002\nNygolaimina\nNygolaimoidea',fillcolor='aqua',style="filled" )
    g.edge('002','004', label2('Nygellidae Female reproductive system monovarial, opisthodelphic; basal part of esophagus with a sheath of spiral muscles'))
    g.edge('002','003', label2('Female reproductive system diovarial, amphidelphic; basal part of esophagus with a thin muscle sheath which is difficult to discern'))

    g.node('003', '003',fillcolor='aqua',style="filled" )
    g.edge('003','005', label2('Aetholaimidae Anterior part of stoma bowl-shaped and sclerotized'))
    g.edge('003','006', label2('Nygolaimidae Anterior part of stoma simple, without sclerotization'))

    g.node('004', '004\nNygellidae\nNygelliinae',fillcolor='aqua',style="filled" )
    g.edge('004','Nygellus', label2('Body length < 1.4 mm; cuticle thin with fine transverse striations; lip region continuous with body contour'))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))

    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label2(''))
    g.edge('','', label2(''))


    g.render('NematodaKey.gv', format='svg', view=True)
    g.render('NematodaKey.gv', format='jpg', view=False)
    g.render('NematodaKey.gv', format='pdf', view=False)

    #g.node('', '',fillcolor='aqua',style="filled" )
    #g.edge('','', label2(''))
    #g.edge('','', label2(''))


def main():
    # Use a breakpoint in the code line below to debug your script.
    draw()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
