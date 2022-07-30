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

    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'

    g.node('000', label='Diagnostic Key\nto Nematoda Orders',fillcolor='red',style="filled")
    g.edge('000','001', label='')

    g.node('001', '001\nEsophagus',fillcolor='aqua',style="filled" )
    g.edge('001','002', label='Cylindrical or bottle-shaped\namphids usually post-labial\nexcretory system single-cell hypodermal glands\nmale with 2 testes\ncaudal alae rare\nphasmids absent')
    g.edge('001','008', label='Subdivided into bulbs\namphid apertures on lips\noften difficult to see\nor posterior to lips and obvious - round or coiled\ngonads single or paired in both male and female')

    g.node('002', '002\nAnterior sensillae',fillcolor='aqua',style="filled" )
    g.edge('002','003', label='3 whorls of inner labial papillae\nouter labial setae and cephalic setae\nmetanemes (filamentous structures in lateral chors) present\ncaudal glands present\nesophageal glands open in or\nnear stoma')
    g.edge('002','004', label='Rarely setiform\nstoma with teeth or odontostyle\nesophagus cylindrical\nbottle-shaped or a stichosome\ncaudal glands usually absent\nesophageal glands open in posterior region of esophagus')

    g.node('003', '003\nSpicule ',fillcolor='aqua',style="filled" )
    g.edge('003','010', label='Muscles attached to proximal enlargement\nmetanemes present\nmarine and fresh water')
    g.edge('003','011', label='Muscles form a pouch around spicules\nprotrusible tooth in some forms')


    g.node('004', '004\nEsophagus',fillcolor='aqua',style="filled" )
    g.edge('004','012', label='Bottle-shaped\nMovable hollow spear\n')
    g.edge('004','015', label='Glandular\nStichosome\nIntestinal trophosome\nParasites of invertebrates')
    g.edge('004','017', label='Vestigial\nParasites of vertebrates')
    g.edge('004','005', label='Cylindrical')

    g.node('005', '005\nParasites?',fillcolor='aqua',style="filled" )
    g.edge('005','019', label='Juveniles are parasites of invertebrates;\nadults free-living	')
    g.edge('005','006', label='All stages parasitic\nadults are vertebrate parasites\njuveniles with or without intermediate hosts')
    g.edge('005','007', label='All stages\nfree-living')

    g.node('006', '006',fillcolor='aqua',style="filled" )
    g.edge('006','016', label='Posterior esophagus a stichosome\nonchiostyle present\nmonovarial\nanphids pore-like')
    g.edge('006','018', label='Anterior end has a sucker\nmales with bell-shaped bursa')

    g.node('007', '007',fillcolor='aqua',style="filled" )
    g.edge('007','013', label='Strong, large\ncuticularized stoma with prominent dorsal tooth\npredators of nematodes')
    g.edge('007','014', label='Long and slender\ntubular stoma without teeth\nstoma without lips\nsoil inhabitants')

    g.node('008', '008\nAmphids',fillcolor='aqua',style="filled" )
    g.edge('008','026', label='Amphids Pore-like, on lips\ncephalic sensillae on lip region\nphasmids present\ncaudal glands absent\nterrestrial\ninclude free-living\nanimal parasites\nplant parsites')
    g.edge('008','009', label='Amphids Post-labial, varied shapes\nphasmids absent; somatic seta common\nfree-living\naquatic organisms')

    g.node('009', '009',fillcolor='aqua',style="filled" )
    g.edge('009','020', label='Anterior sensillae in three whorls\ninner labial\nouter labial and cephalic\namphids var from circular to complex spirals\npost-labial and usually posterior to cephalic setae\nstoma funnel-shaped with a dorsal tooth\nand two smaller subventral teeth\nesophagus cylindrical with posetrior bulb\nfemales diovarial\nmarine')
    g.edge('009','021', label='Brownish cuticle\nanterior sensillae in three whorls,\ninner labial, outer labial and cephalic\namphids spiral, posterior to cephalic setae\ndorsal and smaller subventral teeth\nesophagus cylindrical with enlarged end bulb')
    g.edge('009','023', label='Anterior sensillae in three whorls,\ninner labial, outer labial and cephalic,\n cephalic setae on peduncles\n amphids large, on head\n ocelli may be present\n small stoma with small teeth\n esophagus cylindrical\n females diovarial\n mainly marine')
    g.edge('009','022', label='Small, slender nematodes with a slender tail region\n three whorls of anterior sensilla\n amphids round\n both sexes with one or two gonads\n  Mainly aquatic and wet soil environments')
    g.edge('009','024', label='Anterior sensillae in three whorls,\ninner labial, outer labial and cephalic\nstoma with 3 to 6 teeth on anterior edge\namphids loop-shaped\nocelli may be present\nesophagus cylindrical with no posterior enlargemen')
    g.edge('009','025', label='Labial sensilla papilliform,\ncephalic sensilla usually setiform\nqamphids circular or simple spiral\n esophagus cylindrical, with or without basal bulb\n females usually diovarial')

    g.node('010', '010',fillcolor='aqua',style="filled" )
    g.edge('010','Enoplina', label='Enoplida\n amphids pocket-shaped; esophagus cylindrical\n 3 esophageal glands opening in or near stoma\n excretory canal present\n marine and freshwater')
    g.edge('010','Ironina', label='Enoplida\n amphids pocket-shaped\n stoma elongated, without teeth or with 3-5 moveable teeth\n esophagus cylindrical\n excretory canal present\n mainly marine but also freshwater')
    g.edge('010','Oncholaimina', label='Enoplida\n amphids pocket-shaped\n stoma large, refractive, with 3 teeth\n esophagus cylindrical\n excretory canal present\n mainly marine but also freshwater')
    g.edge('010','Tripyloidina', label='Enoplida\n amphids spiral\n stoma with 1 or more teeth\n esophagus cylindrical\n females diovarial\n mainly marine')
    g.edge('010','Campydorina', label='Enoplida\n amphids pocket-shaped\n stoma with dorsal tooth\n esophagus cylindrical with terminal bulb\n excretory canal present\n females diovarial\n soil and freshwater inhabitant')
    g.edge('010','Alaimina', label='Enoplida\n amphids pore or pocket-shaped\n stoma vestigial, without teeth\n esophagus slender, cylindrical, enlarged posteriorly\n soil and freshwater inhabitants')
    g.edge('010','Trefusiina', label='Enoplida\n amphids spiral\n stoma with teeth\n esophagus cylindrical\n females diovarial\n mainly marine, some freshwater')

    g.node('011', '011',fillcolor='aqua',style="filled" )
    g.edge('011','Diphtherophorina', label='Triplonchida\nstoma with curved or complex spear\n sensilla papilliform\n esophagus with elongate prosterior bulb')
    g.edge('011','Tobrilina', label='Triplonchida\n stoma wide and refractive or funnel-shaped\n usually with teeth\n spinneret at tail tip')
    g.edge('011','Tripylina', label='Triplonchida\n  stoma narrow with a dirsal and two small subventral teeth\n well-developed caudal glands opening at terminal spinneret ')

    g.node('012', '012',fillcolor='aqua',style="filled" )
    g.edge('012','Dorylaimina', label='	Dorylaimida\nstoma with axial odontostyle')
    g.edge('012','Nygolaimina', label='Dorylaimida\nstoma with grooved subventral mural tooth')

    g.node('013', '013',fillcolor='aqua',style="filled" )
    g.edge('013','Mononchina', label='Mononchida\nstoma large, wide with 1 to 3 teeth and/or rows of denticles')
    g.edge('013','Bathyodontina', label='Mononchida\nStoma narrow with a single subventral tooth')

    g.node('014', '014',fillcolor='aqua',style="filled" )
    g.edge('014','Isolaimiina', label='Isolaimiida')

    g.node('015', '015',fillcolor='aqua',style="filled" )
    g.edge('015','Mermithina', label='Mermithida')

    g.node('016', '016',fillcolor='aqua',style="filled" )
    g.edge('016','Trichinellina', label='Trichinellida')

    g.node('017', '017',fillcolor='aqua',style="filled" )
    g.edge('017','Muscipeicina', label='Muscipeicida;')

    g.node('018', '018',fillcolor='aqua',style="filled" )
    g.edge('018','Dioctophymatina', label='Dioctophymatida;')

    g.node('019', '019',fillcolor='aqua',style="filled" )
    g.edge('019','Marimermithina', label='Marimermithida')

    g.node('020', '020',fillcolor='aqua',style="filled" )
    g.edge('020','Chromadorina', label='Chromadorida')

    g.node('021', '021',fillcolor='aqua',style="filled" )
    g.edge('021','Desmodorina', label='Desmodorida')

    g.node('022', '022',fillcolor='aqua',style="filled" )
    g.edge('022','Monhysterina', label='Monhysterida')
    g.edge('022','Linhomoeina', label='Monhysterida')

    g.node('023', '023',fillcolor='aqua',style="filled" )
    g.edge('023','Desmoscolecina', label='Desmoscolecida;')

    g.node('024', '024',fillcolor='aqua',style="filled" )
    g.edge('024','Araeolaimina', label='Araeolaimida')

    g.node('025', '025',fillcolor='aqua',style="filled" )
    g.edge('025','Plectina', label='Plectida')

    g.node('026', '026',fillcolor='aqua',style="filled" )
    g.edge('026','Tylenchina\nTylenchomorpha', label='Rhabditida\nstoma with a protrusible stomatostyle\n lip region simple\n posterior esophageal region\neither a bulb without valve or overlapping glands')
    g.edge('026','Tylenchina\nPanagrolaimorpha', label='Rhabditida\nstoma without teeth or with denticles\nlip region simple\nesophageal corpus without bulb\nposterior bulb with valve')
    g.edge('026','Tylenchina\nCephalobomorpha', label='Rhabditida\nstoma without teeth or with denticles\nlip region with probolae\nesophageal corpus without bulb\nposterior bulb with valve')
    g.edge('026','Rhabditina\nDiplogasteromorpha', label='Rhabditida\nstoma with teeth\nlip region simple\ncorpus with muscular metacorpus\nno valve in posterior bulb')
    g.edge('026','Rhabditina\nRhabditomorpha', label='Rhabditida\nstoma without teeth or with denticles\nlip region simple\ncorpus with metacorpus\nposterior bulb with valve')
    g.edge('026','Spirurina', label='Rhabditida\njuveniles with cephalic hooks\nmultinucleate esophageal glands\nparasites of animals')


    g.render('NematodaKey.gv', format='svg', view=True)
    g.render('NematodaKey.gv', format='jpg', view=False)
    g.render('NematodaKey.gv', format='pdf', view=False)

def main():
    # Use a breakpoint in the code line below to debug your script.
    draw()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
