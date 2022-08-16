from graphviz import Digraph
# import JSON parser
import json

def labelNodes(g):
    #g.node('Aporcelaimidae_002', label='002')
    return g


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
    #http://nemaplex.ucdavis.edu/Uppermnus/nematamnu.htm#Taxonomic_Keys
    #http://nemaplex.ucdavis.edu/Taxadata/Dorylaimida%20Andrassy%202009.html
    GraphTitle = 'Keys from\nDorylaimda\n Free-living, Predaceous and\n Plant-parasitic Nematodes\n\n M. Shamim Jairajpuri\n and Wasim Ahmad (1992).'
    g = Digraph('GraphTitle', comment="FOO",filename = 'NematodaKey.gv') #, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    g= labelNodes(g)
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'
    g.attr(labelloc='t')
    g.attr(label=GraphTitle)


    tableLabelWithLink = '''<
        <table border="0">
           <tr><td href="http://google.com">Google</td></tr> 
           <tr><td align="text">This td is left aligned<br align="left" /></td></tr> 
           <tr><td align="text">this one centered<br align="center" /></td></tr> 
           <tr><td align="text">and this one right aligned<br align="right" /><br align="right"/></td></tr> 
           <tr><td align="text">The value of a closing<br align="left"/>&lt;br/&gt; tag<br align="center"/>refers to the preceeding text<br align="right"/></td></tr> 
        </table>
      >'''
    #g.node('Dorylaimida', label=label2('Dorylaimida'), fillcolor='aqua', style="filled", shape='doubleoctagon')
    #g.node('Sectonematinae', label=label2('Sectonematinae'), fillcolor='aqua', style="filled", shape='doubleoctagon')
    #g.node('Dorylaimina', label=label2('Dorylaimina'), fillcolor='aqua', style="filled", shape='doubleoctagon')

    # Order Dorylaimida Pearse, 1936
    g.edge('COMMON GENERA', 'Tl', label=label2('Terrestrial nematodes with stylet and median bulb'))

    g.edge('COMMON GENERA', 'T2', label=label2('Terrestrial nematodes with spear, median bulb absent'))
    g.edge('COMMON GENERA', 'T3', label=label2('Terrestrial nematodes without stylet or spear'))
    g.edge('COMMON GENERA', 'Zl', label=label2('Freshwater nematodes with stylet and median bulb'))
    g.edge('COMMON GENERA', 'Z2', label=label2('Freshwater nematodes with spear, median bulb absent'))
    g.edge('COMMON GENERA', 'Z3', label=label2('Freshwater nematodes without stylet or spear'))


    g.edge(label2('Tl'), label2('Oesophagal glands overlapping'), label=label2(''))
    g.edge(label2('Oesophagal glands overlapping'), label2('Two gonads'), label=label2(''))
    g.edge(label2('Two gonads'), label2('Hoplolaimidae; head frame strongly developed, body Spiral-shaped'), label=label2(''))
    g.edge(label2('Two gonads'), label2('Helicotylenchus; tail often with little tip, ventrally overlapping'), label=label2(''))
    g.edge(label2('Two gonads'), label2('Rotylenchus; tail without tip, dorsal overlap'), label=label2(''))

    g.node(label2('One gonad1'), label=label2('One gonad'))
    g.edge(label2('Oesophagal glands overlapping'), label2('One gonad1'), label=label2(''))
    g.edge(label2('One gonad1'), label2('Pratylenchidae; short stylet strongly developed, tail blunt'), label=label2(''))

    g.edge(label2('Pratylenchidae; short stylet strongly developed, tail blunt'), label2('Pratylenchus; lip region flattened'), label=label2(''))
    g.edge(label2('One gonad1'), label2('Anguinidae; stylet weak, tail conical'), label=label2(''))
    g.edge(label2('Anguinidae; stylet weak, tail conical'), label2('Pseudhalenchus; median bulb weakly developed'), label=label2(''))
    g.edge(label2('One gonad1'), label2('Aphelenchoididae; median bulb light-refracting, stylet weak'), label=label2(''))
    g.edge(label2('Aphelenchoididae; median bulb light-refracting, stylet weak'), label2('Aphelenchoides; tail conical, often with mucro'), label=label2(''))
    g.edge(label2('Aphelenchoididae; median bulb light-refracting, stylet weak'), label2('Aphelenchus; tail bluntly rounded'), label=label2(''))

    g.edge(label2('Tl'), label2('Oesophagal glands not overlapping'), label=label2(''))

    g.node(label2('Two gonads1'), label=label2('Two gonads'))
    g.edge(label2('Oesophagal glands not overlapping'), label2('Two gonads1'), label=label2(''))
    g.edge(label2('Two gonads1'), label2('Dolichodoridae; tail bluntly rounded'), label=label2(''))
    g.edge(label2('Dolichodoridae; tail bluntly rounded'), label2('Dolichorynchus; with longitudinal grooves'), label=label2(''))
    g.edge(label2('Dolichodoridae; tail bluntly rounded'), label2('Merlinius lateral field with six lines'), label=label2(''))
    g.edge(label2('Dolichodoridae; tail bluntly rounded'), label2('Tylenchorynchus and Bitylenchus; four lines'), label=label2(''))
    g.edge(label2('Oesophagal glands not overlapping'), label2('One gonad'), label=label2(''))
    g.edge(label2('One gonad'), label2('tail long, acute'), label=label2(''))
    g.edge(label2('tail long, acute'), label2('XX'), label=label2(''))
    g.edge(label2('xxx'), label2('XX'), label=label2(''))
    g.edge(label2('xxx'), label2('XX'), label=label2(''))
    g.edge(label2('xxx'), label2('XX'), label=label2(''))
    g.node(label2('One gonad3'), label=label2('One gonad'))
    g.edge(label2('One gonad3'), label2('body with conspicuously broad annules, little, plump nematodes'), label=label2(''))
    g.edge(label2('One gonad3'), label2('double, annulated cuticle'), label=label2(''))
    g.edge(label2('One gonad3'), label2('little C-shaped nematodes, procorpus gently widens into median bulb'), label=label2(''))

    g.node(label2('One gonad2'), label=label2('Two gonads'))
    g.node(label2('Two gonads2'), label=label2('Two gonads'))
    g.edge(label2('One gonad2'), label2('double, annulated cuticle'), label=label2(''))

    g.edge(label2('One gonad'), label2('little C-shaped nematodes, procorpus gently widens into median bulb'), label=label2(''))


    g.render('NematodaKey.gv', format='svg', view=True)
    g.render('NematodaKey.gv', format='jpg', view=False)
    g.render('NematodaKey.gv', format='pdf', view=False)

    #g.node('', '',fillcolor='aqua',style="filled" )
    #g.edge('','', label='')
    #g.edge('','', label='')

    return g



def main():
    # Use a breakpoint in the code line below to debug your script.
    g = draw()
    toJSON(g)

if __name__ == '__main__':
    main()

