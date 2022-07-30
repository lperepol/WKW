# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
# import JSON parser
import json

def labelNodes(g):
    g.node('Aporcelaimidae_002', label='002')
    g.node('Aporcelaiminae_002', label='002')
    g.node('Actinolaimoidinae_002', label='002')
    g.node('Actinolaimoidea_002', label='002')
    g.node('Actinolaimidae_002', label='002')
    g.node('Actinca_002', label='002')
    g.node('Axonchium_002', label='002')
    g.node('Aulolaimoididae_002', label='002')
    g.node('Belondiridae_002', label='002')
    g.node('Belondirinae_002', label='002')
    g.node('Belonenchinae_002', label='002')
    g.node('Basirotyleptus_002', label='002')
    g.node('Carcharolaiminae_002', label='002')
    g.node('Calolaiminae_002', label='002')
    g.node('Dorylaimoidea_002', label='002')
    g.node('Dorylaimidae_002', label='002')
    g.node('Discolaiminae_002', label='002')
    g.node('Dorylaimellus_002', label='002')
    g.node('Dorylaimoides_002', label='002')
    g.node('Enchodelus_002', label='002')
    g.node('Laimydorinae_002', label='002')
    g.node('Lordellonematinae_002', label='002')
    g.node('Longidoridae_002', label='002')
    g.node('Leptonchidae_002', label='002')
    g.node('Leptonchinae_002', label='002')
    g.node('Mydonominae_002', label='002')
    g.node('Nordiidae_002', label='002')
    g.node('Neoactinolaiminae_002', label='002')
    g.node('Nygolaimoidea_002', label='002')
    g.node('Nygolaiminae_002', label='002')
    g.node('Nygolaimellinae_002', label='002')
    g.node('Pungentiinae_002', label='002')
    g.node('Paractinolaiminae_002', label='002')
    g.node('Qudsianematidae_002', label='002')
    g.node('Qudsianematinae_002', label='002')
    g.node('Swangeriinae_002', label='002')
    g.node('Solididentinae_002', label='002')
    g.node('Thornenematinae_002', label='002')
    g.node('Thorniinae_002', label='002')
    g.node('Tylencholaimoidea_002', label='002')
    g.node('Tylencholaimidae_002', label='002')
    g.node('Tylencholaiminae_002', label='002')
    g.node('Tylencholaimus_002', label='002')
    g.node('Tyleptinae_002', label='002')
    g.node('Tylencholaimellinae_002', label='002')
    g.node('Vanderlindiinae_002', label='002')
    g.node('Xiphinemellinae_002', label='002')
    g.node('Aporcelaiminae_003', label='003')
    g.node('Actinolaimoidinae_003', label='003')
    g.node('Actinolaimidae_003', label='003')
    g.node('Axonchium_003', label='003')
    g.node('Belondirinae_003', label='003')
    g.node('Belonenchinae_003', label='003')
    g.node('Basirotyleptus_003', label='003')
    g.node('Carcharolaiminae_003', label='003')
    g.node('Dorylaimoidea_003', label='003')
    g.node('Dorylaimidae_003', label='003')
    g.node('Discolaiminae_003', label='003')
    g.node('Dorylaimellus_003', label='003')
    g.node('Dorylaimoides_003', label='003')
    g.node('Enchodelus_003', label='003')
    g.node('Laimydorinae_003', label='003')
    g.node('Lordellonematinae_003', label='003')
    g.node('Leptonchidae_003', label='003')
    g.node('Leptonchinae_003', label='003')
    g.node('Nordiidae_003', label='003')
    g.node('Neoactinolaiminae_003', label='003')
    g.node('Nygolaimoidea_003', label='003')
    g.node('Nygolaiminae_003', label='003')
    g.node('Pungentiinae_003', label='003')
    g.node('Paractinolaiminae_003', label='003')
    g.node('Qudsianematidae_003', label='003')
    g.node('Qudsianematinae_003', label='003')
    g.node('Swangeriinae_003', label='003')
    g.node('Thornenematinae_003', label='003')
    g.node('Tylencholaimoidea_003', label='003')
    g.node('Tylencholaimidae_003', label='003')
    g.node('Tylencholaiminae_003', label='003')
    g.node('Tylencholaimus_003', label='003')
    g.node('Tylencholaimellinae_003', label='003')
    g.node('Vanderlindiinae_003', label='003')
    g.node('Xiphinemellinae_003', label='003')
    g.node('Aporcelaiminae_004', label='004')
    g.node('Actinolaimoidinae_004', label='004')
    g.node('Axonchium_004', label='004')
    g.node('Belondirinae_004', label='004')
    g.node('Belonenchinae_004', label='004')
    g.node('Basirotyleptus_004', label='004')
    g.node('Carcharolaiminae_004', label='004')
    g.node('Discolaiminae_004', label='004')
    g.node('Dorylaimellus_004', label='004')
    g.node('Dorylaimoides_004', label='004')
    g.node('Enchodelus_004', label='004')
    g.node('Laimydorinae_004', label='004')
    g.node('Leptonchidae_004', label='004')
    g.node('Leptonchinae_004', label='004')
    g.node('Nordiidae_004', label='004')
    g.node('Nygolaiminae_004', label='004')
    g.node('Pungentiinae_004', label='004')
    g.node('Qudsianematidae_004', label='004')
    g.node('Qudsianematinae_004', label='004')
    g.node('Swangeriinae_004', label='004')
    g.node('Thornenematinae_004', label='004')
    g.node('Tylencholaiminae_004', label='004')
    g.node('Tylencholaimus_004', label='004')
    g.node('Tylencholaimellinae_004', label='004')
    g.node('Aporcelaiminae_005', label='005')
    g.node('Axonchium_005', label='005')
    g.node('Belondirinae_005', label='005')
    g.node('Carcharolaiminae_005', label='005')
    g.node('Dorylaimellus_005', label='005')
    g.node('Dorylaimoides_005', label='005')
    g.node('Laimydorinae_005', label='005')
    g.node('Leptonchidae_005', label='005')
    g.node('Leptonchinae_005', label='005')
    g.node('Nygolaiminae_005', label='005')
    g.node('Pungentiinae_005', label='005')
    g.node('Qudsianematidae_005', label='005')
    g.node('Qudsianematinae_005', label='005')
    g.node('Swangeriinae_005', label='005')
    g.node('Thornenematinae_005', label='005')
    g.node('Tylencholaiminae_005', label='005')
    g.node('Tylencholaimus_005', label='005')
    g.node('Tylencholaimellinae_005', label='005')
    g.node('Aporcelaiminae_006', label='006')
    g.node('Axonchium_006', label='006')
    g.node('Belondirinae_006', label='006')
    g.node('Dorylaimellus_006', label='006')
    g.node('Laimydorinae_006', label='006')
    g.node('Leptonchinae_006', label='006')
    g.node('Nygolaiminae_006', label='006')
    g.node('Pungentiinae_006', label='006')
    g.node('Qudsianematidae_006', label='006')
    g.node('Qudsianematinae_006', label='006')
    g.node('Swangeriinae_006', label='006')
    g.node('Thornenematinae_006', label='006')
    g.node('Tylencholaiminae_006', label='006')
    g.node('Tylencholaimus_006', label='006')
    g.node('Tylencholaimellinae_006', label='006')
    g.node('Aporcelaiminae_007', label='007')
    g.node('Axonchium_007', label='007')
    g.node('Belondirinae_007', label='007')
    g.node('Dorylaimellus_007', label='007')
    g.node('Laimydorinae_007', label='007')
    g.node('Qudsianematinae_007', label='007')
    g.node('Swangeriinae_007', label='007')
    g.node('Thornenematinae_007', label='007')
    g.node('Tylencholaiminae_007', label='007')
    g.node('Tylencholaimellinae_007', label='007')
    g.node('Aporcelaiminae_008', label='008')
    g.node('Belondirinae_008', label='008')
    g.node('Dorylaimellus_008', label='008')
    g.node('Laimydorinae_008', label='008')
    g.node('Qudsianematinae_008', label='008')
    g.node('Thornenematinae_008', label='008')
    g.node('Belondirinae_009', label='009')
    g.node('Dorylaimellus_009', label='009')
    g.node('Laimydorinae_009', label='009')
    g.node('Qudsianematinae_009', label='009')
    g.node('Thornenematinae_009', label='009')
    g.node('Dorylaimellus_010', label='010')
    g.node('Laimydorinae_010', label='010')
    g.node('Qudsianematinae_010', label='010')
    g.node('Dorylaimellus_011', label='011')
    g.node('Laimydorinae_011', label='011')
    g.node('Qudsianematinae_011', label='011')
    g.node('Dorylaimellus_012', label='012')
    g.node('Qudsianematinae_012', label='012')
    g.node('Dorylaimellus_013', label='013')
    g.node('Qudsianematinae_013', label='013')
    g.node('Qudsianematinae_014', label='014')
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
    g.edge('Dorylaimida', 'Dorylaimina', label=label2('Odontostyle feeding apparatus'))
    g.edge('Dorylaimida', 'Dorylaimida 002', label=label2('Mural-tooth feeding apparatus'))

    g.edge('Dorylaimida 002', 'Campydorina', label=label2('Mural tooth located on subdorsal wall of buccal cavity; basal part of esophagus small with a strongly-developed triquetrous chamber'))
    g.edge('Dorylaimida 002', 'Nygolaimina', label=label2('Mural tooth located on subventral wall of buccal cavity; basal part of esophagus fairly long and without triquetrous chamber'))

    #Suborder Dorylaimina Pearse, 1936
    g.edge('Dorylaimina', 'Actinolaimoidea', label=label2('Cheilostom strongly sclerotized, with plate- or basket-like structures, frequently with large onchia, with or without denticles'))
    g.edge('Dorylaimina', 'Dorylaimina 002',  label=label2('Cheilostom usually thin-walled, without onchia or denticles'))

    g.edge('Dorylaimina 002', 'Longidoroidea',  label=label2('Odontostyle long, attenuated; esophagus with three glands'))
    g.edge('Dorylaimina 002', 'Dorylaimina 003',  label=label2('Odontostyle comparatively small; esophagus with five glands'))

    g.edge('Dorylaimina 003', 'Belondiroidea',  label=label2('Expanded part of esophagus enclosed in a spiral muscular sheath'))
    g.edge('Dorylaimina 003', 'Dorylaimina 004',  label=label2('Expanded part of esophagus not enclosed in a spiral muscular sheath'))

    g.edge('Dorylaimina 004', 'Tylencholaimoidea',  label=label2('Subcuticle coarsely striated, with abundant radial striae; expanded part of esophagus usually a small basal bulb'))
    g.edge('Dorylaimina 004', 'Dorylaimoidea',  label=label2('Subcuticle not striated, few if any radial striae; expanded part of esophagus usually about 50% of total esophagus length'))

    #Superfamily Dorylaimoidea de Man, 1876
    g.edge('Dorylaimoidea', 'Aporcelaimidae',  label=label2('Odontostyle aperture wide, usually more than half odontostyle length; guiding ring plicated, not sclerotized'))
    g.edge('Dorylaimoidea', 'Dorylaimoidea_002',  label=label2('Odontostyle with smaller aperture, usually < 33% of odontostyle length; guiding ring sclerotized'))

    g.edge('Dorylaimoidea_002', 'Nordiidae',  label=label2('Odontostyle attenuated, usually longer than lip region width'))
    g.edge('Dorylaimoidea_002', 'Dorylaimoidea_003',  label=label2('Odontostyle not attenuated, usually about as long as lip region width'))

    g.edge('Dorylaimoidea_003', 'Dorylaimidae',  label=label2('Large, stout nematodes, usually with long, filiform tail which exhibits sexual dimorphism'))
    g.edge('Dorylaimoidea_003', 'Qudsianematidae',  label=label2('Medium-sized nematodes with short tails which are similar in both sexes'))


    #Family Dorylaimidae de Man, 1876
    g.edge('Dorylaimidae', 'Dorylaimidae_002',  label=label2('Cuticle with longitudinal ridges'))
    g.edge('Dorylaimidae', 'Dorylaimidae_003',  label=label2('Cuticle without longitudinal ridges'))

    g.edge('Dorylaimidae_002', 'Arctidorylaiminae',  label=label2('Tail elongate-conoid, similar in both sexes'))
    g.edge('Dorylaimidae_002', 'Dorylaiminae',  label=label2('Tail elongate-conoid to filiform in females, short and bluntly rounded in males'))


    #g.node('Thornenematinae', label=label2('Thornenematinae'), fillcolor='aqua', style="filled",shape='septagon')
    g.edge('Dorylaimidae_003', 'Thornenematinae',  label=label2('Cheilostom (between guiding ring and oral aperture) with minute to well-developed sclerotized plates; S2N (nuclei of second pair of ventro-sublateral glands) well anterior to base of esophagus'))
    g.edge('Dorylaimidae_003', 'Laimydorinae',  label=label2('Cheilostom without sclerotized plates; S2N close to base of esophagus'))

    #Subfamily Dorylaiminae de Man, 1876
    g.edge('Dorylaiminae', 'Dorylaimus',  label=label2('Ventromedian supplements in a contiguous series of 25-55'))
    g.edge('Dorylaiminae', 'Ischiodorylaimus',  label=label2('Ventromedian supplements in 2-3 groups (fascicles)'))

    #Subfamily Laimydorinae Andrassy, 1969
    g.edge('Laimydorinae', 'Laimydorinae_002',  label=label2('Tails similar in both sexes'))
    g.edge('Laimydorinae', 'Laimydorinae_004',  label=label2('Tails dissimilar in males and females'))

    g.edge('Laimydorinae_002', 'Amphidorylaimus',  label=label2('Lip region offset; spicules narrow and "non-dorylaimoid"'))
    g.edge('Laimydorinae_002', 'Laimydorinae_003',  label=label2('Lip region continuous; spicules broad and dorylaimoid'))

    g.edge('Laimydorinae_003', 'Prodorylaimus',  label=label2('Ventromedian supplements numerous, contiguous'))
    g.edge('Laimydorinae_003', 'Prodorylaimium',  label=label2('Ventromedian supplements few, spaced'))

    g.edge('Laimydorinae_004', 'Laimydorinae_005',  label=label2('Guiding ring sclerotized, appearing double; male prerectum long, beginning anterior to supplements'))
    g.edge('Laimydorinae_004', 'Laimydorinae_006',  label=label2('Guiding ring not sclerotized, appearing single or weakly double; male prerectum short, beginning within range of supplements'))

    g.edge('Laimydorinae_005', 'Idiodorylaimus',  label=label2('Subcuticle with coarse striations'))
    g.edge('Laimydorinae_005', 'Laimydorus',  label=label2('Subcuticle without coarse striations'))

    g.edge('Laimydorinae_006', 'Laimydorinae_007',  label=label2('Male tail with rounded terminus'))
    g.edge('Laimydorinae_006', 'Afrodorylaimus',  label=label2('Male tail with pointed terminus'))

    g.edge('Laimydorinae_007', 'Drepanodorylaimus',  label=label2('Odontostyle asymmetrical; two parts of esophagus not clearly demarcated'))
    g.edge('Laimydorinae_007', 'Laimydorinae_008',  label=label2('Odontostyle symmetrical; two parts of esophagus clearly demarcated'))

    g.edge('Laimydorinae_008', 'Minidorylaimus',  label=label2('Odontophore slightly swollen at base'))
    g.edge('Laimydorinae_008', 'Laimydorinae_009',  label=label2('Odontophore rod like'))

    g.edge('Laimydorinae_009', 'Laimydorinae_010',  label=label2('Ventromedian supplements contiguous or uniformly spaced'))
    g.edge('Laimydorinae_009', 'Calodorylaimus',  label=label2('Ventromedian supplements in two groups (fascicles)'))

    g.edge('Laimydorinae_010', 'Miodorylaimus',  label=label2('Cuticle thin, vulva not sclerotized; spicules comparatively weak; prerectum extending much beyond range of supplements'))
    g.edge('Laimydorinae_010', 'Laimydorinae_011',  label=label2('Cuticle thick, vulva sclerotized; spicules well developed; prerectum beginning at anterior end or within range of supplements'))

    g.edge('Laimydorinae_011', 'Calcaridorylaimus',  label=label2('Spicules large, with double contour on dorsal side and spur near tip; supplements very small'))
    g.edge('Laimydorinae_011', 'Mesodorylaimus',  label=label2('Spicules without double contour on dorsal side and without spur near tip; supplements well developed'))

    #Subfamily Thornenematinae Siddiqi, 1969
    g.edge('Thornenematinae', 'Thornenematinae_002',  label=label2('Female reproductive system monovarial, opisthodelphic'))
    g.edge('Thornenematinae', 'Thornenematinae_006',  label=label2('Female reproductive system diovarial, amphidelphic'))

    g.edge('Thornenematinae_002', 'Thornenematinae_003',  label=label2('Female tail short, rounded'))
    g.edge('Thornenematinae_002', 'Thornenematinae_004',  label=label2('Female tail elongate-conoid to long, filiform'))

    g.edge('Thornenematinae_003', 'Sclerolabia',  label=label2('No labial or postlabial sclerotization'))
    g.edge('Thornenematinae_003', 'Willinema',  label=label2('Tail elongate-conoid, similar in both sexes'))

    g.edge('Thornenematinae_004', 'Indiodorylaimus',  label=label2('Tail elongate-conoid, similar in both sexes'))
    g.edge('Thornenematinae_004', 'Thornenematinae_005',  label=label2('Tail elongate-conoid to long, filiform in females and short-conoid in males'))

    g.edge('Thornenematinae_005', 'Opisthodorylaimus',  label=label2('Odontostyle broad, with wide lumen and aperture; no labial sclerotization'))
    g.edge('Thornenematinae_005', 'Thornenema',  label=label2('Odontostyle narrow, labial sclerotization'))

    g.edge('Thornenematinae_006', 'Coomansinema',  label=label2('Odontostyle broad, with wide lumen and aperture; no labial sclerotization'))
    g.edge('Thornenematinae_006', 'Thornenematinae_007',  label=label2('Odontostyle relatively narrow, labial sclerotization'))

    g.edge('Thornenematinae_007', 'Thornenematinae_008',  label=label2('Cheilorhabdions  strongly sclerotized, forming chamber-like structure'))
    g.edge('Thornenematinae_007', 'Thornenematinae_009',  label=label2('Cheilorhabdions  sclerotized, but not forming chamber-like structure'))

    g.edge('Thornenematinae_008', 'Silvallis',  label=label2('Guiding ring single, plicated; tail short, bluntly rounded'))
    g.edge('Thornenematinae_008', 'Fuscheila',  label=label2('Guiding ring appears double; tail long, filiform'))

    g.edge('Thornenematinae_009', 'Timminema',  label=label2('Female tail short and rounded'))
    g.edge('Thornenematinae_009', 'Sicaguttur',  label=label2('Female tail long and filiform'))

    #Subfamily Arctidorylaiminae Mulvey and Anderson, 1979
    g.edge('Arctidorylaiminae', 'Arctidorylaimus')


    #Family Aporcelaimidae Heyns, 1965
    g.edge('Aporcelaimidae', 'Paraxonchiinae',  label=label2('Body sharply tapering towards anterior end'))
    g.edge('Aporcelaimidae', 'Aporcelaimidae_002',  label=label2('Body not sharply tapering towards anterior end'))

    g.edge('Aporcelaimidae_002', 'Aporcelaiminae',  label=label2('Odontostyle axial with wide aperture'))
    g.edge('Aporcelaimidae_002', 'Sectonematinae',  label=label2('Odontostyle a mural tooth'))

    #Subfamily Aporcelaiminae Heyns, 1965
    g.edge('Aporcelaiminae', 'Aporcelaiminae_002',  label=label2('Cuticular layers inconspicuous; no criss-cross lines or punctations'))
    g.edge('Aporcelaiminae', 'Aporcelaiminae_003',  label=label2('Cuticular layers conspicuous; transverse of criss-cross lines or punctations'))

    g.edge('Aporcelaiminae_002', 'Aporcedorus',  label=label2('Female tail long, filiform'))
    g.edge('Aporcelaiminae_002', 'Aporcelaimium',  label=label2('Female tail short, conoid'))

    g.edge('Aporcelaiminae_003', 'Makatinus',  label=label2('Lip region offset by slight depression; vulva longitudinal'))
    g.edge('Aporcelaiminae_003', 'Aporcelaiminae_004',  label=label2('Lip region offset by deep constriction; vulva lips a transverse slit or pore-like'))

    g.edge('Aporcelaiminae_004', 'Akrotonus',  label=label2('Lip region rounded, labial papillae not projecting above contour; two ventromedian supplements'))
    g.edge('Aporcelaiminae_004', 'Aporcelaiminae_005',  label=label2('Lip region angular, labial papillae projecting above contour; >2 ventromedian supplements'))

    g.edge('Aporcelaiminae_005', 'Tubixaba',  label=label2('Body very long (9-11 mm); aperture of odontostyle 1/3 its length'))
    g.edge('Aporcelaiminae_005', 'Aporcelaiminae_006',  label=label2('Body <6mm; odontostyle aperture about Ã‚Â½ its length or greater'))

    g.edge('Aporcelaiminae_006', 'Aporcelaiminae_007',  label=label2('Cuticle with faint longitudinal markings or criss-cross lines'))
    g.edge('Aporcelaiminae_006', 'Aporcelaiminae_008',  label=label2('Cuticle with transverse striations'))

    g.edge('Aporcelaiminae_007', 'Torumanawa',  label=label2('Body relatively small; three cardia glands at esophago-intestinal junction'))
    g.edge('Aporcelaiminae_007', 'Aporcelaimus',  label=label2('Body large; cardia glands absent'))

    g.edge('Aporcelaiminae_008', 'Takamangi',  label=label2('Oral aperture circular'))
    g.edge('Aporcelaiminae_008', 'Aporcelaimellus',  label=label2('Oral aperture hexagonal'))

    #Subfamily Sectonematinae Siddiqi, 1969
    g.edge('Sectonematinae', 'Sectonema')

    #Subfamily Paraxonchiinae Dhanachand and Jairajpuri, 1981
    g.edge('Paraxonchiinae', 'Gopalus',  label=label2('Odontostyle long, straight, attenuated, with small aperture; cardia glands poorly developed'))
    g.edge('Paraxonchiinae', 'Paraxonchium',  label=label2('Odontostyle smaller, wide, a little bent, with larger aperture; cardia glands well-developed'))


    #Family Qudsianematidae  Jairajpuri, 1965
    g.edge('Qudsianematidae', 'Qudsianematidae_002',  label=label2('Cuticle with coarse transverse striations'))
    g.edge('Qudsianematidae', 'Qudsianematidae_003',  label=label2('Cuticle with fine transverse striations'))

    g.edge('Qudsianematidae_002', 'Crateronematinae',  label=label2('Body slender; body pores indistinct; odontostyle attenuated'))
    g.edge('Qudsianematidae_002', 'Lordellonematinae',  label=label2('Body not slender; body pores distinct; odontostyle not attenuated'))

    g.edge('Qudsianematidae_003', 'Discolaiminae',  label=label2('Lip region discoid; well-developed hypodermal glands'))
    g.edge('Qudsianematidae_003', 'Qudsianematidae_004',  label=label2('Lip region not discoid; hypodermal glands absent or poorly developed'))

    g.edge('Qudsianematidae_004', 'Qudsianematidae_005',  label=label2('Lip region continuous with body contour; lips amalgamated'))
    g.edge('Qudsianematidae_004', 'Qudsianematidae_006',  label=label2('Lip region offset; lips usually separated'))

    g.edge('Qudsianematidae_005', 'Thorniinae',  label=label2('Tail short and hemispherical in both sexes; only one adanal pair of supplements present (rarely a single ventromedian)'))
    g.edge('Qudsianematidae_005', 'Chrysonematinae',  label=label2('Tail elongate conoid in both sexes; adanal pair and a series of ventromedian supplements present'))

    g.edge('Qudsianematidae_006', 'Qudsianematinae',  label=label2('Dorsal esophageal gland nucleus near anterior of esophageal enlargement; female tail short, hemispherical to elongate conoid'))
    g.edge('Qudsianematidae_006', 'Hulqinae',  label=label2('Dorsal esophageal gland nucleus two or more body widths behind anterior of esophageal enlargement; female tail long, filiform'))


    #Subfamily Qudsianematinae Jairajpuri, 1965
    g.edge('Qudsianematinae', 'Qudsianematinae_002',  label=label2('Female reproductive system monovarial, opisthodelphic'))
    g.edge('Qudsianematinae', 'Qudsianematinae_003',  label=label2('Female reproductive system diovarial, amphidelphic'))

    g.edge('Qudsianematinae_002', 'Indokochinema',  label=label2('Amphids labial'))
    g.edge('Qudsianematinae_002', 'Ecumenicus',  label=label2('Amphids post-labial'))

    g.edge('Qudsianematinae_003', 'Qudsianematinae_004',  label=label2('Odontophore simple, rod-like'))
    g.edge('Qudsianematinae_003', 'Qudsianematinae_013',  label=label2('Odontophore flanged or with basal knobs'))

    g.edge('Qudsianematinae_004', 'Qudsianematinae_005',  label=label2('Odontostyle large; guiding ring appears double'))
    g.edge('Qudsianematinae_004', 'Qudsianematinae_006',  label=label2('Odontostyle small; guiding ring appears single'))

    g.edge('Qudsianematinae_005', 'Labronemella',  label=label2('Lip region with deeply sunken circumoral area and distinct inner liplets'))
    g.edge('Qudsianematinae_005', 'Labronema',  label=label2('Lip region without deeply sunken circumoral area; inner liplets not well separated; odontostyle slender'))

    g.edge('Qudsianematinae_006', 'Baqriella',  label=label2('Outer margin of lips forming flap over oral area; inner margin of lips sunken'))
    g.edge('Qudsianematinae_006', 'Qudsianematinae_007',  label=label2('Outer margin of lips not forming flap over oral area; inner margin of lips not sunken'))

    g.edge('Qudsianematinae_007', 'Skibbernema',  label=label2('Constriction between slender and expanded parts of esophagus; expanded part bipartite'))
    g.edge('Qudsianematinae_007', 'Qudsianematinae_008',  label=label2('No constriction between slender and expanded parts of esophagus; expanded part not bipartite'))

    g.edge('Qudsianematinae_008', 'Crassolabium',  label=label2('Lips with cuticularized pieces'))
    g.edge('Qudsianematinae_008', 'Qudsianematinae_009',  label=label2('Lips without cuticularized pieces'))

    g.edge('Qudsianematinae_009', 'Thonus',  label=label2('Cardia disk present'))
    g.edge('Qudsianematinae_009', 'Qudsianematinae_010',  label=label2('Cardia disk absent'))

    g.edge('Qudsianematinae_010', 'Epidorylaimus',  label=label2('Tail elongate conoid, 3.5-8.0 x anal body diameter.'))
    g.edge('Qudsianematinae_010', 'Qudsianematinae_011',  label=label2('Tail short-conoid, 1-3 x anal body diameter'))

    g.edge('Qudsianematinae_011', 'Microdorylaimus',  label=label2('Body small (<1mm); esophagus long, almost 1/3 body length'))
    g.edge('Qudsianematinae_011', 'Qudsianematinae_012',  label=label2('Body long (>1mm); esophagus short'))

    g.edge('Qudsianematinae_012', 'Eudorylaimus',  label=label2('Precloacal space present'))
    g.edge('Qudsianematinae_012', 'Allodorylaimus',  label=label2('Precloacal space absent'))

    g.edge('Qudsianematinae_013', 'Qudsianematinae_014',  label=label2('Odontophore flanged'))
    g.edge('Qudsianematinae_013', 'Tylenchodorus',  label=label2('Odontophore with three prominent knobs'))

    g.edge('Qudsianematinae_014', 'Pachydorylaimus',  label=label2('Odontostyle thick-walled'))
    g.edge('Qudsianematinae_014', 'Qudsianema',  label=label2('Odontostyle thin-walled'))

    #Subfamily Thorniinae De Coninck, 1965
    g.edge('Thorniinae', 'Nygolaimoides',  label=label2('Males with large ventromedian supplements and small gubernaculum'))
    g.edge('Thorniinae', 'Thorniinae_002',  label=label2('Males without ventromedian supplements or gubernaculum'))

    g.edge('Thorniinae_002', 'Thornia',  label=label2('Amphids stirrup-shaped, aperture as wide as fovea; spicules not dorylaimoid, lateral guiding pieces absent'))
    g.edge('Thorniinae_002', 'Thorneella',  label=label2('Amphids oval, aperture smaller than fovea; spicules  dorylaimoid with lateral guiding pieces'))

    #Subfamily Crateronematinae Siddiqi, 1969
    g.edge('Crateronematinae', 'Crateronema')

    #Subfamily Chrysonematinae Siddiqi, 1969
    g.edge('Chrysonematinae', 'Chrysonema',  label=label2('Lips rounded; female tail long, conoid; male tail short, convex-conoid'))
    g.edge('Chrysonematinae', 'Chrysonemoides',  label=label2('Lips knob-like; tail in both sexes elongate-conoid, ventrally-curved'))


    #Subfamily Discolaiminae Siddiqi, 1969
    g.edge('Discolaiminae', 'Mylodiscus',  label=label2('Lip region with cuticularized, shallow, bowl-like plates'))
    g.edge('Discolaiminae', 'Discolaiminae_002',  label=label2('Lip region without cuticularized plates'))

    g.edge('Discolaiminae_002', 'Discolaimus',  label=label2('Lip region discoid'))
    g.edge('Discolaiminae_002', 'Discolaiminae_003',  label=label2('Lip region not discoid'))

    g.edge('Discolaiminae_003', 'Discolaimoides',  label=label2('Lip region offset by an expansion'))
    g.edge('Discolaiminae_003', 'Discolaiminae_004',  label=label2('Lip region offset by a constriction'))

    g.edge('Discolaiminae_004', 'Discolaimium',  label=label2('Female reproductive system diovarial, amphidelphic'))
    g.edge('Discolaiminae_004', 'Latocephalus',  label=label2('Female reproductive system monovarial, opisthodelphic'))

    #Subfamily Lordellonematinae Siddiqi, 1969
    g.edge('Lordellonematinae', 'Sicorinema',  label=label2('Body pores indistinct; female reproductive system monovarial, opisthodelphic'))
    g.edge('Lordellonematinae', 'Lordellonematinae_002',  label=label2('Body pores distinct; female reproductive system monovarial, prodelphic'))

    g.edge('Lordellonematinae_002', 'Poronemella',  label=label2('Ventral body pores only in esophageal region; tail elongate-conoid, bent dorsally'))
    g.edge('Lordellonematinae_002', 'Lordellonematinae_003',  label=label2('Ventral body pores along entire body; tail short-conoid, or subdigitate'))

    g.edge('Lordellonematinae_003', 'Moshajia',  label=label2('Odontostyle aperture > 1/2 its length; spicules non-dorylaimoid'))
    g.edge('Lordellonematinae_003', 'Lordellonema',  label=label2('Odontostyle aperture < 1/2 its length; spicules dorylaimoid'))

    #Subfamily Hulqinae Siddiqi, 1982
    g.edge('Hulqinae', 'Hulqus',  label=label2('Female reproductive system monovarial, opisthodelphic'))
    g.edge('Hulqinae', 'Mitoaxonchium',  label=label2('Female reproductive system diovarial, amphidelphic'))

    #Family Nordiidae Jairajpuri and Siddiqi, 1964
    g.edge('Nordiidae', 'Nordiidae_002',  label=label2('Labial papillae rising above lip contour'))
    g.edge('Nordiidae', 'Nordiidae_003',  label=label2('Labial papillae not enlarged'))

    g.edge('Nordiidae_002', 'Helmabiinae',  label=label2('Cuticle with longitudinal and horizontal lamelliform striations'))
    g.edge('Nordiidae_002', 'Cephalodorylaiminae',  label=label2('Cuticle smooth, striations absent'))

    g.edge('Nordiidae_003', 'Pungentiinae',  label=label2('Odontophore usually flanged'))
    g.edge('Nordiidae_003', 'Nordiidae_004',  label=label2('Odontophore not flanged'))

    g.edge('Nordiidae_004', 'Nordiinae',  label=label2('Body usually robust; odontostyle length 3-5 x lip region width'))
    g.edge('Nordiidae_004', 'Actinolaimoidinae',  label=label2('Body usually slender; odontostyle length < 2 x lip region width'))

    #Subfamily Nordiinae Jairajpuri and Siddiqi, 1964
    g.edge('Nordiinae', 'Longidorella\nSaevadorella',  label=label2('Body robust; odontostyle length 3-5 x lip region width'))
    g.edge('Nordiinae', 'Thornedia',  label=label2('Body slender; odontostyle length < 2 x lip region width'))

    #Subfamily Cephalodorylaiminae Jairajpuri, 1967
    g.edge('Cephalodorylaiminae', 'Cephalodorylaimus',  label=label2('Inner labial papillae setiform; female reproductive system diovarial, amphidelphic'))
    g.edge('Cephalodorylaiminae', 'Acephalodorylaimus',  label=label2('Inner labial papillae barely raised; female reproductive system monovarial, prodelphic'))

    #Subfamily Pungentiinae Siddiqi, 1969
    g.edge('Pungentiinae', 'Pungentiinae_002',  label=label2('Tail short to elongate-conoid'))
    g.edge('Pungentiinae', 'Pungentiinae_006',  label=label2('Tail long, filiform'))

    g.edge('Pungentiinae_002', 'Californidorus',  label=label2('Odontostyle very long, > 50 µm'))
    g.edge('Pungentiinae_002', 'Pungentiinae_003',  label=label2('Odontostyle shorter, < 50 µm'))

    g.edge('Pungentiinae_003', 'Kochinema',  label=label2('Amphids labial'))
    g.edge('Pungentiinae_003', 'Pungentiinae_004',  label=label2('Amphids post-labial'))

    g.edge('Pungentiinae_004', 'Rhyssocolpus',  label=label2('Cuticle near vulva coarsely striated'))
    g.edge('Pungentiinae_004', 'Pungentiinae_005',  label=label2('Cuticle near vulva not striated'))

    g.edge('Pungentiinae_005', 'Pungentus',  label=label2('Cuticularized platelets around stoma'))
    g.edge('Pungentiinae_005', 'Enchodelus',  label=label2('No cuticularized platelets around stoma'))

    g.edge('Pungentiinae_006', 'Enchodorus',  label=label2('Odontostyle  < 10 µm; ventromedian supplements few and spaced'))
    g.edge('Pungentiinae_006', 'Lenonchium',  label=label2('Odontostyle  > 15 µm; ventromedian supplements numerous and contiguous'))

    #Subgenera of Enchodelus Thorne, 1939
    g.edge('Enchodelus', 'Enchodelus_002',  label=label2('Tail hemispherical or bluntly conoid'))
    g.edge('Enchodelus', 'Enchodelus_003',  label=label2('Tail short-conoid or elongate-conoid'))

    g.edge('Enchodelus_002', 'Enchodelus',  label=label2('Odontostyle fairly long; odontophore with broad basal flanges'))
    g.edge('Enchodelus_002', 'Rotundus',  label=label2('Odontostyle short; odontophore without basal flanges'))

    g.edge('Enchodelus_003', 'Heterodorus',  label=label2('Lip region not offset from body contour; female gonads with ovoid chamber'))
    g.edge('Enchodelus_003', 'Enchodelus_004',  label=label2('Lip region distinctly offset from body contour; female gonads without ovoid chamber'))

    g.edge('Enchodelus_004', 'Nepalus',  label=label2('Odontostyle>50µm; odontophore with moderate basal flanges'))
    g.edge('Enchodelus_004', 'Paraenchodelus',  label=label2('Odontostyle<50µm; odontophore rod-like'))

    #Subfamily Helmabiinae Siddiqi, 1971
    g.edge('Helmabiinae', 'Helmabia')

    #Subfamily Actinolaimoidinae Jairajpuri and Ahmad, 1992
    g.edge('Actinolaimoidinae', 'Actinolaimoidinae_002',  label=label2('Odontostyle very narrow; aperture indistinct'))
    g.edge('Actinolaimoidinae', 'Actinolaimoidinae_003',  label=label2('Odontostyle narrow; aperture distinct'))

    g.edge('Actinolaimoidinae_002', 'Malekus',  label=label2('Labial papillae prominent; projecting above lip contour'))
    g.edge('Actinolaimoidinae_002', 'Oonaguntus',  label=label2('Labial papillae indistinct; not projecting above lip contour'))

    g.edge('Actinolaimoidinae_003', 'Actinolaimoides',  label=label2('Lip region continuous; first pair of ventro-sub-lateral esophageal glands close together'))
    g.edge('Actinolaimoidinae_003', 'Actinolaimoidinae_004',  label=label2('Lip region offset; first pair of ventro-sub-lateral esophageal glands widely separated'))

    g.edge('Actinolaimoidinae_004', 'Oriverutus',  label=label2('Odontostyle usually < 2 lip widths long; well-developed glands at esophago-intestinal junction'))
    g.edge('Actinolaimoidinae_004', 'Pararoriverutus',  label=label2('Odontostyle usually 3 lip widths long; no glands at esophago-intestinal junction'))


    #Superfamily Actinolaimoidea Thorne, 1939
    g.edge('Actinolaimoidea', 'Carcharolaimidae',  label=label2('Female tail < 2x abd, conical or rounded; vestibule with basket-like structures'))
    g.edge('Actinolaimoidea', 'Actinolaimoidea_002',  label=label2('Female tail >4x abd; vestibule without basket-like structures'))

    g.edge('Actinolaimoidea_002', 'Actinolaimidae',  label=label2('Vestibule with four massive onchia, with or without denticles'))
    g.edge('Actinolaimoidea_002', 'Trachypleurosidae',  label=label2('Vestibule without onchia but with corrugated ring and tranverse rows of mural denticles'))

    #Family Actinolaimidae Thorne, 1939
    g.edge('Actinolaimidae', 'Actinolaimidae_002',  label=label2('Cuticle with longitudinal striations'))
    g.edge('Actinolaimidae', 'Actinolaimidae_003',  label=label2('Cuticle without longitudinal striations'))

    g.edge('Actinolaimidae_002', 'Actinolaiminae',  label=label2('Odontostyle massive, robust, aperture 1/2 its length'))
    g.edge('Actinolaimidae_002', 'Brittonematinae',  label=label2('Odontostyle slender, 2-3 lip widths long; aperture about 1/3 its length'))

    g.edge('Actinolaimidae_003', 'Paractinolaiminae',  label=label2('Vestibule with minute denticles'))
    g.edge('Actinolaimidae_003', 'Neoactinolaiminae',  label=label2('Vestibule without denticles'))

    #Subfamily Actinolaiminae Thorne, 1939
    g.edge('Actinolaiminae', 'Actinolaimus')

    #Subfamily Neoactinolaiminae Thorne, 1967
    g.edge('Neoactinolaiminae', 'Neoactinolaiminae_002', label=label2('Vestibule with four onchia'))
    g.edge('Neoactinolaiminae', 'Hexactinolaimus',  label=label2('Vestibule with six onchia'))

    g.edge('Neoactinolaiminae_002', 'Metactinolaimus',  label=label2('Onchia fused into a strong second spear guide'))
    g.edge('Neoactinolaiminae_002', 'Neoactinolaiminae_003',  label=label2('Onchia not fused'))

    g.edge('Neoactinolaiminae_003', 'Neoactinolaimus',  label=label2('Ventromedian supplements in 2-3 fascicles'))
    g.edge('Neoactinolaiminae_003', 'Egtitus',  label=label2('Ventromedian supplements arranged in series'))

    #Subfamily Paractinolaiminae Thorne, 1967
    g.edge('Paractinolaiminae', 'Paractinolaiminae_002',  label=label2('Vestibule with four onchia'))
    g.edge('Paractinolaiminae', 'Paractinolaiminae_003',  label=label2('Vestibule with six onchia'))

    g.edge('Paractinolaiminae_002', 'Metactinolaimus',  label=label2('Onchia fused into a strong second spear guide'))
    g.edge('Paractinolaiminae_002', 'Paractinolaiminae_003',  label=label2('Onchia not fused'))

    g.edge('Paractinolaiminae_003', 'Neoactinolaimus',  label=label2('Ventromedian supplements in 2-3 fascicles'))
    g.edge('Paractinolaiminae_003', 'Egtitus',  label=label2('Ventromedian supplements arranged in series'))

    #Subfamily Brittonematinae Thorne, 1967
    g.edge('Brittonematinae', 'Actinca',  label=label2('Lip region almost continuous with body; female tail long, filiform; male tail short, rounded'))
    g.edge('Brittonematinae', 'Paractinocephalus',  label=label2('Lip region expanded; tail long, filiform in both sexes'))

    #Subgenera of Actinca Andrassy, 1964
    g.edge('Actinca', 'Actinca',  label=label2('Lip region narrow and high; vestibule ring weak'))
    g.edge('Actinca', 'Actinca_002',  label=label2('Lip region wide and low; vestibule ring well developed'))

    g.edge('Actinca_002', 'Stomachoglossa',  label=label2('Body < 3 mm, odontostyle slender'))
    g.edge('Actinca_002', 'Parastomachoglossa',  label=label2('Body > 3 mm, odontostyle robust'))

    # Family Trachypleurosidae Thorne, 1967
    g.edge('Trachypleurosidae', 'Trachypleurosum')

    # Family Carcharolaimidae Thorne, 1967
    g.edge('Carcharolaimidae', 'Carcharolaiminae',  label=label2('Stoma narrowing behind guiding ring'))
    g.edge('Carcharolaimidae', 'Caribenematinae',  label=label2('Stoma not narrowing behind guiding ring'))

    # Subfamily Carcharolaiminae Thorne, 1967
    g.edge('Carcharolaiminae', 'Carcharolaiminae_002',  label=label2('Lip region offset; tail conoid; curved ventrally'))
    g.edge('Carcharolaiminae', 'Brasilaimus',  label=label2('Lip region continuous; tail elongate, straight'))

    g.edge('Carcharolaiminae_002', 'Antholaimus',  label=label2('Lips angular, petaloid, bearing rods and plates'))
    g.edge('Carcharolaiminae_002', 'Carcharolaiminae_003',  label=label2('Lips not angular, without rods and plates'))

    g.edge('Carcharolaiminae_003', 'Carcharolaiminae_004',  label=label2('Cephalic framework basket-like'))
    g.edge('Carcharolaiminae_003', 'Mylodiscoides',  label=label2('Cephalic framework with two plates, posterior one shallow, bowl-like, anterior small'))

    g.edge('Carcharolaiminae_004', 'Carcharolaiminae_005',  label=label2('Cephalic framework with strong onchia'))
    g.edge('Carcharolaiminae_004', 'Carcharolaimus',  label=label2('Cephalic framework with ribs, denticles or small teeth'))

    g.edge('Carcharolaiminae_005', 'Carcharoides',  label=label2('Six onchia'))
    g.edge('Carcharolaiminae_005', 'Caryboca',  label=label2('Four onchia'))

    # Subfamily Caribenematinae Thorne, 1967
    g.edge('Caribenematinae', 'Caribenema')

    # Superfamily Longidoroidea Thorne, 1935
    g.edge('Longidoroidea', 'Xiphinematidae',  label=label2('Guiding ring double; odontophore flanged'))
    g.edge('Longidoroidea', 'Longidoridae',  label=label2('Guiding ring single; odontophore not flanged'))

    # Family Longidoridae Thorne, 1935
    g.edge('Longidoridae', 'Paralongidorus',  label=label2('Amphids with stirrup-shaped fovea'))
    g.edge('Longidoridae', 'Longidoridae_002',  label=label2('Amphids with pouch-like fovea'))

    g.edge('Longidoridae_002', 'Longidorus',  label=label2('Amphid apertures pore-like, inconspicuous'))
    g.edge('Longidoridae_002', 'Longidoroides',  label=label2('Amphid apertures slit-like'))

    # Family Xiphinematidae Dalmasso, 1969
    g.edge('Xiphinematidae', 'Xiphinematinae',  label=label2('Amphids stirrup-shaped with slit-like apertures; dorsal gland nucleus at same level as dorsal gland opening'))
    g.edge('Xiphinematidae', 'Xiphidorinae',  label=label2('Amphids pouch-like with pore-like apertures; dorsal gland nucleus far behind dorsal gland opening'))

    # Subfamily Xiphinematinae Dalmasso, 1969
    g.edge('Xiphinematinae', 'Xiphinema')

    # Subfamily Xiphidorinae Khan, Chawla and Saha, 1978
    g.edge('Xiphidorinae', 'Xiphidorus')

    # Superfamily Belondiroidea Thorne, 1939
    g.edge('Belondiroidea', 'Belondiridae')

    # Family Belondiridae Thorne, 1939
    g.edge('Belondiridae', 'Dorylaimellinae',  label=label2('Cuticularized pieces around oral aperture; odontophore flanged'))
    g.edge('Belondiridae', 'Belondiridae_002',  label=label2('Cuticularized pieces absent around oral aperture; odontophore rod-like'))

    g.edge('Belondiridae_002', 'Belondirinae',  label=label2('Female tail short; digitate, conoid or rounded'))
    g.edge('Belondiridae_002', 'Swangeriinae',  label=label2('Female tail long, filiform'))

    # Subfamily Belondirinae Thorne, 1939
    g.edge('Belondirinae', 'Belondirinae_002',  label=label2('Female reproductive system diovarial, amphidelphic'))
    g.edge('Belondirinae', 'Belondirinae_004',  label=label2('Female reproductive system monovarial, opisthodelphic'))

    g.edge('Belondirinae_002', 'Anchobelondira',  label=label2('Anterior of esophagus set off by constriction'))
    g.edge('Belondirinae_002', 'Belondirinae_003',  label=label2('Anterior of esophagus not set off by constriction'))

    g.edge('Belondirinae_003', 'Belondirella',  label=label2('Lip region with 6 liplets; 2 ventromedian supplements'))
    g.edge('Belondirinae_003', 'Amphibelondira',  label=label2('Lip region without liplets, no ventromedian supplements'))

    g.edge('Belondirinae_004', 'Nimigula',  label=label2('Esophagus > 1/2  body length; vulva anterior to esophago-intestinal junction'))
    g.edge('Belondirinae_004', 'Belondirinae_005',  label=label2('Esophagus < Â½ body length; vulva posterior to esophago-intestinal junction'))

    g.edge('Belondirinae_005', 'Belondirinae_006',  label=label2('Anterior of esophagus set off by constriction or isthmus'))
    g.edge('Belondirinae_005', 'Belondira',  label=label2('Anterior part of esophagus continuous'))

    g.edge('Belondirinae_006', 'Dactyluraxonchium',  label=label2('Tail apically digitate'))
    g.edge('Belondirinae_006', 'Belondirinae_007',  label=label2('Tail apically hemispherical'))

    g.edge('Belondirinae_007', 'Phallaxonchium',  label=label2('Spicules very long, narrow, alate, without median pieces'))
    g.edge('Belondirinae_007', 'Belondirinae_008',  label=label2('Spicules massive, non-alate, with median pieces'))

    g.edge('Belondirinae_008', 'Heynsaxonchium',  label=label2('Odontostyle narrow, > 2 lip widths long'))
    g.edge('Belondirinae_008', 'Belondirinae_009',  label=label2('Odontostyle fusiform to cylindroid, < 2 lip widths long'))

    g.edge('Belondirinae_009', 'Axonchoides',  label=label2('Labial framework semi-sclerotized, cephalic papillae mammiform, anterior of esophagus non-muscular'))
    g.edge('Belondirinae_009', 'Axonchium',  label=label2('Labial framework not sclerotized, cephalic papillae not mammiform, anterior of esophagus muscular'))

    # Subgenera of Axonchium Cobb, 1920
    g.edge('Axonchium', 'Syncheilaxonchium',  label=label2('Lip region not offset, bluntly conoid to hemispherical, lips amalgamated'))
    g.edge('Axonchium', 'Axonchium_002',  label=label2('Lip region offset'))

    g.edge('Axonchium_002', 'Poraxonchium',  label=label2('>100 lateral body pores, > 50 ventral body pores; 5-7 caudal pores in female, 7-10 in male; spiral muscle sheath encircling posterior part of esophagus'))
    g.edge('Axonchium_002', 'Axonchium_003',  label=label2('Fewer lateral and ventral body pores; 1-2 caudal pores in female, up to 6 in male; muscle sheath with straight bundles encircling posterior part of esophagus'))

    g.edge('Axonchium_003', 'Axonchium_004',  label=label2('Vagina sclerotized'))
    g.edge('Axonchium_003', 'Axonchium_007',  label=label2('Vagina not sclerotized'))

    g.edge('Axonchium_004', 'Discaxonchium',  label=label2('Disk-like structure between body cuticle and vaginal sclerotization; males with many contiguous supplements'))
    g.edge('Axonchium_004', 'Axonchium_005',  label=label2('No disk-like structure between body cuticle and vaginal scerotization; males with spaced supplements'))

    g.edge('Axonchium_005', 'Axonchium_006',  label=label2('Anterior part of esophagus separated by an isthmus; spicules arcuate; ventromedian supplements regularly spaced'))
    g.edge('Axonchium_005', 'Spiculaxonchium',  label=label2('Anterior part of esophagus not separated by an isthmus; spicules plow-shaped; ventromedian supplements poorly developed, in two groups'))

    g.edge('Axonchium_006', 'Epaxonchium',  label=label2('Anterior part of esophagus slender, with fusiform section; male spicules > 2x anal body diameter long'))
    g.edge('Axonchium_006', 'Metaxonchium',  label=label2('Anterior part of esophagus muscular, without fusiform section; male spicules smaller'))

    g.edge('Axonchium_007', 'Hypaxonchium',  label=label2('Vulva broad, longitudinally oval, vagina lumen wide'))
    g.edge('Axonchium_007', 'Axonchium',  label=label2('Vulva a transverse slit, vagina lumen narrow'))

    # Subfamily Dorylaimellinae Jairajpuri, 1964
    g.edge('Dorylaimellinae', 'Dorylaimellus')

    # Subgenera of Dorylaimellus Cobb, 1913
    g.edge('Dorylaimellus', 'Dorylaimellus_002',  label=label2('Female reproductive system monovarial'))
    g.edge('Dorylaimellus', 'Dorylaimellus_006',  label=label2('Female reproductive system diovarial, amphidelphic'))

    g.edge('Dorylaimellus_002', 'Dorylaimellus_003',  label=label2('Female reproductive system monovarial, prodelphic'))
    g.edge('Dorylaimellus_002', 'Dorylaimellus_004',  label=label2('Female reproductive system monovarial, opisthodelphic'))

    g.edge('Dorylaimellus_003', 'Mesodorylaimellus',  label=label2('Vulva a transverse slit'))
    g.edge('Dorylaimellus_003', 'Ibadanus',  label=label2('Vulva a longitudinal slit'))

    g.edge('Dorylaimellus_004', 'Sindellus',  label=label2('Peri-oral disk present, odontostyle attenuated'))
    g.edge('Dorylaimellus_004', 'Dorylaimellus_005',  label=label2('Peri-oral disk absent, odontostyle lumen distinct'))

    g.edge('Dorylaimellus_005', 'Metadorylaimellus',  label=label2('Tail hemispherical or conoid'))
    g.edge('Dorylaimellus_005', 'Amazonema',  label=label2('Tail long, attenuated'))

    g.edge('Dorylaimellus_006', 'Capitellus',  label=label2('Lip region continuous with body contour'))
    g.edge('Dorylaimellus_006', 'Dorylaimellus_007',  label=label2('Lip region offset'))

    g.edge('Dorylaimellus_007', 'Dorylaimellus_008',  label=label2('Peri-oral disk present'))
    g.edge('Dorylaimellus_007', 'Dorylaimellus_010',  label=label2('Peri-oral disk absent'))

    g.edge('Dorylaimellus_008', 'Axodorylaimellus',  label=label2('Vulva transverse'))
    g.edge('Dorylaimellus_008', 'Dorylaimellus_009',  label=label2('Vulva pore-like or longitudinal'))

    g.edge('Dorylaimellus_009', 'Belondorylaimellus',  label=label2('Vulva longitudinal; tail cylindroid or sub-cylindroid'))
    g.edge('Dorylaimellus_009', 'Jamilius',  label=label2('Vulva pore-like; tail elongate, attenuated'))

    g.edge('Dorylaimellus_010', 'Rashidanema',  label=label2('Vulva transverse'))
    g.edge('Dorylaimellus_010', 'Dorylaimellus_011',  label=label2('Vulva longitudinal'))

    g.edge('Dorylaimellus_011', 'Clavidorylaimellus',  label=label2('Tail terminus clavate'))
    g.edge('Dorylaimellus_011', 'Dorylaimellus_012',  label=label2('Tail terminus not clavate'))

    g.edge('Dorylaimellus_012', 'Dorylaimellus',  label=label2('Tail digitate or subdigitate'))
    g.edge('Dorylaimellus_012', 'Dorylaimellus_013',  label=label2('Tail elongate-conoid to filiform'))

    g.edge('Dorylaimellus_013', 'Elongidorylaimellus',  label=label2('Tail very long (c=8-16); spicules with abrupt ventral angle; ventromedian supplements in pairs'))
    g.edge('Dorylaimellus_013', 'Filidorylaimellus',  label=label2('Tail long (c=4-5); spicules dorylaimoid; ventromedian supplements in pairs'))

    # Subfamily Swangeriinae Jairajpuri, 1964
    g.edge('Swangeriinae', 'Swangeriinae_002',  label=label2('Tail similar in both sexes'))
    g.edge('Swangeriinae', 'Swangeriinae_007',  label=label2('Tail dissimilar in both sexes'))

    g.edge('Swangeriinae_002', 'Swangeria',  label=label2('Basket-like structure around oral aperture'))
    g.edge('Swangeriinae_002', 'Swangeriinae_003',  label=label2('No basket-like structure around oral aperture'))

    g.edge('Swangeriinae_003', 'Oxybelondira',  label=label2('Cephalic sclerotization'))
    g.edge('Swangeriinae_003', 'Swangeriinae_004',  label=label2('No cephalic sclerotization'))

    g.edge('Swangeriinae_004', 'Swangeriinae_005',  label=label2('Odontostyle straight'))
    g.edge('Swangeriinae_004', 'Swangeriinae_006',  label=label2('Odontostyle asymmetrical'))

    g.edge('Swangeriinae_005', 'Falcihasta',  label=label2('Body length < 2mm; female tail with lateral expansions; few ventromedian supplements'))
    g.edge('Swangeriinae_005', 'Paraoxydirus',  label=label2('Body length > 3mm; female tail without lateral expansions; numerous ventromedian supplements'))

    g.edge('Swangeriinae_006', 'Qudsiella',  label=label2('Odontostyle long, attenuated'))
    g.edge('Swangeriinae_006', 'Oxydirus',  label=label2('Odontostyle short, not attenuated'))

    g.edge('Swangeriinae_007', 'Lindseyus',  label=label2('Odontostyle narrow; weak labial basket present'))
    g.edge('Swangeriinae_007', 'Roqueus',  label=label2('Odontostyle fusiform; labial basket absent'))

    # Superfamily Tylencholaimoidea Filipjev, 1934
    g.edge('Tylencholaimoidea', 'Aulolaimoididae',  label=label2('Esophagus with 3 sections'))
    g.edge('Tylencholaimoidea', 'Tylencholaimoidea_002',  label=label2('Esophagus with 2 sections'))

    g.edge('Tylencholaimoidea_002', 'Tylencholaimidae',  label=label2('Odontostyle usually well developed; expanded part of esophagus about 1/2 esophagus length'))
    g.edge('Tylencholaimoidea_002', 'Tylencholaimoidea_003',  label=label2('Odontostyle slender; expanded part of esophagus short, cylindroid or pyriform'))

    g.edge('Tylencholaimoidea_003', 'Mydonomidae',  label=label2('Odontostyle asymmetrical, aperture distinct; esophageal bulb cylindroid'))
    g.edge('Tylencholaimoidea_003', 'Leptonchidae',  label=label2('Odontostyle symmetrical, attenuated, often solid, needle-like; esophageal bulb usually pyriform'))

    # Family Tylencholaimidae Filipjev, 1934
    g.edge('Tylencholaimidae', 'Mumtaziinae',  label=label2('Amphids small, pouch-shaped, with oval aperture; odontostyle asymmetrical'))
    g.edge('Tylencholaimidae', 'Tylencholaimidae_002',  label=label2('Amphids stirrup-shaped, with slit-like aperture; odontostyle symmetrical'))

    g.edge('Tylencholaimidae_002', 'Vanderlindiinae',  label=label2('Odontostyle massive with very thick walls'))
    g.edge('Tylencholaimidae_002', 'Tylencholaimidae_003',  label=label2('Odontostyle not massive, walls not thick'))

    g.edge('Tylencholaimidae_003', 'Xiphinemellinae',  label=label2('Odontostyle long, attenuated with narrow lumen and aperture'))
    g.edge('Tylencholaimidae_003', 'Tylencholaiminae',  label=label2('Odontostyle generally small, with distinct lumen and aperture; odontophore usually knobbed'))

    # Subfamily Tylencholaiminae Filipjev, 1934
    g.edge('Tylencholaiminae', 'Tantunema',  label=label2('Amphid aperture small, pore-like'))
    g.edge('Tylencholaiminae', 'Tylencholaiminae_002',  label=label2('Amphid aperture slit-like'))

    g.edge('Tylencholaiminae_002', 'Tylencholaiminae_003',  label=label2('Odontophore with distinct basal knobs'))
    g.edge('Tylencholaiminae_002', 'Tylencholaiminae_004',  label=label2('Odontophore without basal knobs'))

    g.edge('Tylencholaiminae_003', 'Tylencholaimus',  label=label2('Tail short-conoid or elongate-conoid'))
    g.edge('Tylencholaiminae_003', 'Discomyctus',  label=label2('ail long, filiform'))

    g.edge('Tylencholaiminae_004', 'Tylencholaiminae_005',  label=label2('Odontostyle 2 lip-region widths long'))
    g.edge('Tylencholaiminae_004', 'Tylencholaiminae_007',  label=label2('Odontostyle 1 lip-region width long'))

    g.edge('Tylencholaiminae_005', 'Tylencholaiminae_006',  label=label2('Body length < 1 mm; odontostyle long and very thin; vulva transverse'))
    g.edge('Tylencholaiminae_005', 'Chitwoodius',  label=label2('Body length  about 2 mm; odontostyle long and robust; vulva longitudinal'))

    g.edge('Tylencholaiminae_006', 'Meylonema',  label=label2('Female reproductive system monovarial, prodelphic'))
    g.edge('Tylencholaiminae_006', 'Utahnema',  label=label2('Female reproductive system diovarial, amphidelphic'))

    g.edge('Tylencholaiminae_007', 'Sclerolaimus',  label=label2('Six sclerotized pieces around oral opening; labial disk absent; female reproductive system diovarial, amphidelphic'))
    g.edge('Tylencholaiminae_007', 'Capilonchus',  label=label2('Sclerotized pieces absent around oral opening; labial disk present; female reproductive system monovarial, prodelphic'))

    # Subgenera of Tylencholaimus De Man, 1876
    g.edge('Tylencholaimus', 'Disctylencholaimus',  label=label2('Labial disk present'))
    g.edge('Tylencholaimus', 'Tylencholaimus_002',  label=label2('Labial disk absent'))

    g.edge('Tylencholaimus_002', 'Tylencholaimus_003',  label=label2('Female reproductive system monovaria'))
    g.edge('Tylencholaimus_002', 'Tylencholaimus_006',  label=label2('Female reproductive system diovarial, amphidelphic'))

    g.edge('Tylencholaimus_003', 'Tylencholaimus_004',  label=label2('Female reproductive system prodelphic'))
    g.edge('Tylencholaimus_003', 'Opisthotylencholaimus',  label=label2('Female reproductive system opisthodelphic'))

    g.edge('Tylencholaimus_004', 'Tylencholaimus_005',  label=label2('Lip region offset by deep constriction; odontophore with distinct basal knobs'))
    g.edge('Tylencholaimus_004', 'Protylencholaimus',  label=label2('Lip region offset by shallow depression; odontophore with very small basal knobs'))

    g.edge('Tylencholaimus_005', 'Tylencholaimus',  label=label2('Tail short-conoid'))
    g.edge('Tylencholaimus_005', 'Leptotylencholaimus',  label=label2('Tail elongate-conoid'))

    g.edge('Tylencholaimus_006', 'Pseudotylencholaimus',  label=label2('Odontostyle long, strongly cuticularized, small aperture'))
    g.edge('Tylencholaimus_006', 'Amphitylencholaimus',  label=label2('Odontostyle short, slender, with aperture 1/3 its length'))

    # Subfamily Xiphinemellinae Jairajpuri, 1964
    g.edge('Xiphinemellinae', 'Loncharionema',  label=label2('Female reproductive system monovarial prodelphic; tail long, filiform'))
    g.edge('Xiphinemellinae', 'Xiphinemellinae_002',  label=label2('Female reproductive system diovarial, amphidelphic; tail short, conoid'))

    g.edge('Xiphinemellinae_002', 'Xiphinemella',  label=label2('Labial disk present'))
    g.edge('Xiphinemellinae_002', 'Xiphinemellinae_003',  label=label2('Labial disk absent'))

    g.edge('Xiphinemellinae_003', 'Zalophidera',  label=label2('Stoma sclerotized; odontophore flanged; vulva transverse'))
    g.edge('Xiphinemellinae_003', 'Kantbhala',  label=label2('Stoma not sclerotized; odontophore without knobs or flanges; vulva pore-like'))

    # Subfamily Vanderlindiinae Siddiqi, 1969
    g.edge('Vanderlindiinae', 'Vanderlindiinae_002',  label=label2('Odontostyle ventrally curved'))
    g.edge('Vanderlindiinae', 'Vanderlindiinae_003',  label=label2('Odontostyle straight'))

    g.edge('Vanderlindiinae_002', 'Curvidorylaimus',  label=label2('Odontostyle base furcate, two distinct parts of esophagus; vulva transverse'))
    g.edge('Vanderlindiinae_002', 'Vanderlindia',  label=label2('Odontostyle base not furcate, parts of esophagus not distinctly demarcated; vulva circular'))

    g.edge('Vanderlindiinae_003', 'Metadorylaimus',  label=label2('Odontostyle aperture small; vulva transverse'))
    g.edge('Vanderlindiinae_003', 'Neometadorylaimus',  label=label2('Odontostyle aperture large; vulva longitudinal'))

    # Subfamily Mumtaziinae Andrassy, 1976
    g.edge('Mumtaziinae', 'Promumtazium',  label=label2('Female reproductive system diovarial, amphidelphic; tail short, conoid'))
    g.edge('Mumtaziinae', 'Mumtazium',  label=label2('Female reproductive system monovarial, opisthodelphic; tail long, filiform'))

    # Family Leptonchidae Thorne, 1935
    g.edge('Leptonchidae', 'Encholaiminae',  label=label2('Cuticle heavily striated, both transversely and longitudinally forming a lamelliform pattern; cephalic setae present'))
    g.edge('Leptonchidae', 'Leptonchidae_002',  label=label2('Cuticle finely striated; no longitudinal straie or cephalic setae'))

    g.edge('Leptonchidae_002', 'Athernematinae',  label=label2('Odontostyle asymmetrical; amphids strongly sclerotized'))
    g.edge('Leptonchidae_002', 'Leptonchidae_003',  label=label2('Odontostyle symmetrical; amphids not sclerotized'))

    g.edge('Leptonchidae_003', 'Belonenchinae',  label=label2('Odontostyle solid, needle like, without distinct lumen'))
    g.edge('Leptonchidae_003', 'Leptonchidae_004',  label=label2('Odontostyle not solid, with distinct lumen'))

    g.edge('Leptonchidae_004', 'Tylencholaimellinae',  label=label2('Odontophore with distinct knobs or flanges'))
    g.edge('Leptonchidae_004', 'Leptonchidae_005',  label=label2('Odontophore without distinct knobs, rarely flanged'))

    g.edge('Leptonchidae_005', 'Leptonchinae',  label=label2('Odontostyle slender; inner cuticle lining of esophageal bulb not thickened'))
    g.edge('Leptonchidae_005', 'Tyleptinae',  label=label2('Odontostyle robust; inner cuticle lining of esophageal bulb distinctly thickened'))

    # Subfamily Leptonchinae Thorne, 1935
    g.edge('Leptonchinae', 'Leptonchinae_002',  label=label2('Esophageal bulb offset by Constriction'))
    g.edge('Leptonchinae', 'Leptonchinae_004',  label=label2('Esophageal bulb not offset by constriction'))

    g.edge('Leptonchinae_002', 'Meylis',  label=label2('Lip region distinctly offset; labial disk present; female reproductive system diovarial; amphidelphic'))
    g.edge('Leptonchinae_002', 'Leptonchinae_003',  label=label2('Lip region slightly offset; labial disk absent; female reproductive system monovarial; prodelphic'))

    g.edge('Leptonchinae_003', 'Proleptonchoides',  label=label2('Odontophore flanged; tail digitate-spicate'))
    g.edge('Leptonchinae_003', 'Proleptonchus',  label=label2('Odontophore not flanged; tail hemispherical or bluntly conoid'))

    g.edge('Leptonchinae_004', 'Funaria',  label=label2('Vulva longitudinal; esophageal bulb cylindroid'))
    g.edge('Leptonchinae_004', 'Leptonchinae_005',  label=label2('Vulva transverse or pore-like; esophageal bulb pyriform'))

    g.edge('Leptonchinae_005', 'Bertzuckermania',  label=label2('Lip region continuous with body contour; stomal ring present'))
    g.edge('Leptonchinae_005', 'Leptonchinae_006',  label=label2('Lip region offset; stomal ring absent'))

    g.edge('Leptonchinae_006', 'Leptonchus',  label=label2('Odontophore sclerotized, arcuate; vulva transverse'))
    g.edge('Leptonchinae_006', 'Apoleptonchus',  label=label2('Odontophore sclerotized only at base, straight; vulva pore-like'))

    # Subfamily Tyleptinae Jairajpuri, 1964
    g.edge('Tyleptinae', 'Caveonchus',  label=label2('Labial disk present; odontostyle attenuated, with narrow lumen and aperture'))
    g.edge('Tyleptinae', 'Tyleptinae_002',  label=label2('Labial disk absent; odontostyle robust, with wide lumen and aperture'))

    g.edge('Tyleptinae_002', 'Tyleptus',  label=label2('Inner liplets around oral aperture; valvular chamber in esophageal bulb distinctly thickened'))
    g.edge('Tyleptinae_002', 'Gymnotyleptus',  label=label2('Inner liplets absent around oral aperture; valvular chamber in esophageal bulb indistinct'))

    # Subfamily Belonenchinae Jairajpuri, 1964
    g.edge('Belonenchinae', 'Punctoleptus',  label=label2('Cuticle with punctations over entire body'))
    g.edge('Belonenchinae', 'Belonenchinae_002',  label=label2('Cuticle without punctations'))

    g.edge('Belonenchinae_002', 'Belonenchinae_003',  label=label2('Basal esophageal bulb pyriform with distinct, valvular thickenings'))
    g.edge('Belonenchinae_002', 'Belonenchinae_004',  label=label2('Basal esophageal bulb cylindrical, without valvular thickenings'))

    g.edge('Belonenchinae_003', 'Sclerostylus',  label=label2('Stoma heavily sclerotized at base; odontostyle long; odontophore conspicuously flanged'))
    g.edge('Belonenchinae_003', 'Basirotyleptus',  label=label2('Stoma weakly sclerotized at base; odontostyle short; odontophore simple, rod-like or weakly flanged'))

    g.edge('Belonenchinae_004', 'Glochidorella',  label=label2('Labial disk present; odontophore with basal knobs'))
    g.edge('Belonenchinae_004', 'Zetalaimus',  label=label2('Labial disk absent; odontophore flanged'))

    # Subgenera of Basirotyleptus Jairajpuri, 1964
    g.edge('Basirotyleptus', 'Coronatyleptus',  label=label2('Labial disk present'))
    g.edge('Basirotyleptus', 'Basirotyleptus_002',  label=label2('Labial disk absent'))

    g.edge('Basirotyleptus_002', 'Aculonchus',  label=label2('Female reproductive system diovarial, amphidelphic'))
    g.edge('Basirotyleptus_002', 'Basirotyleptus_003',  label=label2('Female reproductive system monovarial'))

    g.edge('Basirotyleptus_003', 'Trichonchium',  label=label2('Female reproductive system monovarial, prodelphic'))
    g.edge('Basirotyleptus_003', 'Basirotyleptus_004',  label=label2('Female reproductive system monovarial; opisthodelphic'))

    g.edge('Basirotyleptus_004', 'Opisthotyleptus',  label=label2('Odontophore flanged'))
    g.edge('Basirotyleptus_004', 'Basirotyleptus',  label=label2('Odontophore not flanged'))

    # Subfamily Encholaiminae Golden and Murphy, 1967
    g.edge('Encholaiminae', 'Encholaimus')

    # Subfamily Tylencholaimellinae Jairajpuri, 1964
    g.edge('Tylencholaimellinae', 'Tylencholaimellinae_002',  label=label2('Esophageal bulb not offset by constriction'))
    g.edge('Tylencholaimellinae', 'Tylencholaimellinae_004',  label=label2('Esophageal bulb offset by constriction'))

    g.edge('Tylencholaimellinae_002', 'Oostebrinkella',  label=label2('Tail long, filiform'))
    g.edge('Tylencholaimellinae_002', 'Tylencholaimellinae_003',  label=label2('Tail short, rounded'))

    g.edge('Tylencholaimellinae_003', 'Gerthus',  label=label2('Odontophore with basal knobs, female reproductive system monovarial, opisthodelphic'))
    g.edge('Tylencholaimellinae_003', 'Goferus',  label=label2('Odontophore without basal knobs, female reproductive system diovarial, amphidelphic'))

    g.edge('Tylencholaimellinae_004', 'Tylencholaimellinae_005',  label=label2('Odontostyle with accessory stiffening piece'))
    g.edge('Tylencholaimellinae_004', 'Tylencholaimellinae_006',  label=label2('Odontostyle without accessory stiffening piece'))

    g.edge('Tylencholaimellinae_005', 'Tylencholaimellus',  label=label2('Accessory stiffening piece on dorsal side of odontostyle; female reproductive system monovarial, opisthodelphic'))
    g.edge('Tylencholaimellinae_005', 'Dorella',  label=label2('Accessory stiffening piece on ventral side of odontostyle; female reproductive system monovarial, prodelphic'))

    g.edge('Tylencholaimellinae_006', 'Agmodorus',  label=label2('Tail elongate'))
    g.edge('Tylencholaimellinae_006', 'Tylencholaimellinae_007',  label=label2('Tail short and rounded'))

    g.edge('Tylencholaimellinae_007', 'Doryllium',  label=label2('Sclerotized pieces absent around oral aperture; female reproductive system monovarial, opisthodelphic'))
    g.edge('Tylencholaimellinae_007', 'Phellonema',  label=label2('Sclerotized pieces present around oral aperture; female reproductive system diovarial, amphidelphic'))

    # Subgenera of Tylencholaimellus Cobb, 1915
    g.edge('Tylencholaimellus', 'Coronatylencholaimellus',  label=label2('Labial disk present'))
    g.edge('Tylencholaimellus', 'Tylencholaimellus',  label=label2('Labial disk absent'))

    # Family Mydonomidae Thorne, 1964
    g.edge('Mydonomidae', 'Calolaiminae',  label=label2('Odontophore straight, rod-like; guiding ring thick'))
    g.edge('Mydonomidae', 'Mydonominae',  label=label2('Odontophore angular; guiding ring not thick'))

    # Subamily Mydonominae Thorne, 1964
    g.edge('Mydonominae', 'Mydonomus',  label=label2('Esophageal bulb enclosed in muscular sheath'))
    g.edge('Mydonominae', 'Mydonominae_002',  label=label2('Esophageal bulb not enclosed in muscular sheath'))

    g.edge('Mydonominae_002', 'Dorylaimoides',  label=label2('Tail similar in both sexes'))
    g.edge('Mydonominae_002', 'Morasia',  label=label2('Tail dissimilar in both sexes'))

    # Subgenera of Dorylaimoides Thorne and Swanger, 1936
    g.edge('Dorylaimoides', 'Dorylaimoides_002',  label=label2('Female reproductive system diovarial, amphidelphic'))
    g.edge('Dorylaimoides', 'Dorylaimoides_004',  label=label2('Female reproductive system monovarial, opisthodelphic'))

    g.edge('Dorylaimoides_002', 'Longidorylaimoides',  label=label2('Tail long, filiform'))
    g.edge('Dorylaimoides_002', 'Dorylaimoides_003',  label=label2('Tail not long and filiform'))

    g.edge('Dorylaimoides_003', 'Dorylaimoides',  label=label2('Tail short, conoid to hemispheroid'))
    g.edge('Dorylaimoides_003', 'Digidorylaimoides',  label=label2('Tail subdigtate or bent dorsally'))

    g.edge('Dorylaimoides_004', 'Shamimonema',  label=label2('Tail short, conoid or digitate'))
    g.edge('Dorylaimoides_004', 'Dorylaimoides_005',  label=label2('Tail elongate, conoid or long, filiform'))

    g.edge('Dorylaimoides_005', 'Arcidorylaimoides',  label=label2('Tail elongate, conoid, ventrally arcuate'))
    g.edge('Dorylaimoides_005', 'Tarjania',  label=label2('Tail elongate, conoid, bent dorsally or long, filiform'))


    # Subamily Calolaiminae Goseco, Ferris and Ferris, 1976
    g.edge('Calolaiminae', 'Miranema',  label=label2('Tail dissimilar in both sexes; odontophore strongly sclerotized'))
    g.edge('Calolaiminae', 'Calolaiminae_002',  label=label2('Tail similar in both sexes; odontophore not strongly sclerotized'))

    g.edge('Calolaiminae_002', 'Calolaimus',  label=label2('Odontostyle and guiding ring very thick; esophageal bulb long, cylindroid'))
    g.edge('Calolaiminae_002', 'Timmus',  label=label2('Odontostyle and guiding ring not very thick; esophageal bulb short, pyriform'))

    # Family Aulolaimoididae Jairajpuri, 1964
    g.edge('Aulolaimoididae', 'Aulolaimoides',  label=label2('Tail long and filiform'))
    g.edge('Aulolaimoididae', 'Aulolaimoididae_002',  label=label2('Tail short and rounded'))

    g.edge('Aulolaimoididae_002', 'Adenolaimus',  label=label2('Pharyngeal structures present; female reproductive system monovarial, opisthodelphic'))
    g.edge('Aulolaimoididae_002', 'Oostenbrinckia',  label=label2('Pharyngeal structures absent; female reproductive system diovarial, amphidelphic'))

    # Suborder Nygolaimina Ahmad and Jairajpuri, 1979
    g.edge('Nygolaimina', 'Nygolaimoidea')

    # Superfamily Nygolaimoidea Thorne, 1935
    g.edge('Nygolaimoidea', 'Nygellidae',  label=label2('Basal expanded part of esophagus enclosed in a thick sheath of spiral muscles; female reproductive system monovarial, opisthodelphic'))
    g.edge('Nygolaimoidea', 'Nygolaimoidea_002',  label=label2('Basal part of esophagus not enclosed in muscle sheath; female reproductive system diovarial, amphidelphic'))

    g.edge('Nygolaimoidea_002', 'Aetholaimidae',  label=label2('Stoma sclerotized'))
    g.edge('Nygolaimoidea_002', 'Nygolaimoidea_003',  label=label2('Stoma not sclerotized'))

    g.edge('Nygolaimoidea_003', 'Nygolaimidae',  label=label2('Basal expanded part of esophagus about 1/2 esophagus length; cardiac glands present'))
    g.edge('Nygolaimoidea_003', 'Nygolaimellidae',  label=label2('Basal expanded part of esophagus about 2/3 esophagus length, bibulbar; cardiac disk present'))

    # Family Nygolaimidae Thorne, 1935
    g.edge('Nygolaimidae', 'Nygolaiminae',  label=label2('Mural tooth deltoid to linear or dorylaimoid'))
    g.edge('Nygolaimidae', 'Solididentinae',  label=label2('Mural tooth solid or acicular'))

    # Subfamily Nygolaiminae Thorne, 1935
    g.edge('Nygolaiminae', 'Paravulvus',  label=label2('Vulva longitudinal; paravulvae usually present'))
    g.edge('Nygolaiminae', 'Nygolaiminae_002',  label=label2('Vulva transverse; paravulvae absent'))

    g.edge('Nygolaiminae_002', 'Afronygus',  label=label2('Tail elongate, conoid, ventrally arcuate'))
    g.edge('Nygolaiminae_002', 'Nygolaiminae_003',  label=label2('Tail short, convex-conoid, ventrally arcuate, hemispheroid or clavate'))

    g.edge('Nygolaiminae_003', 'Laevides',  label=label2('Tooth dorylaimoid'))
    g.edge('Nygolaiminae_003', 'Nygolaiminae_004',  label=label2('Tooth deltoid or linear'))

    g.edge('Nygolaiminae_004', 'Nygolaiminae_005',  label=label2('Lip region offset by constriction'))
    g.edge('Nygolaiminae_004', 'Nygolaiminae_006',  label=label2('Lip region usually continuous with body contour'))

    g.edge('Nygolaiminae_005', 'Nygolaimus',  label=label2('Males without gubernaculum and with weakly-developed ventromedian supplements'))
    g.edge('Nygolaiminae_005', 'Paranygolaimus',  label=label2('Males with gubernaculum and with well-developed ventromedian supplements'))

    g.edge('Nygolaiminae_006', 'Aquatides',  label=label2('Tooth linear; body usually straight; tail convex-conoid to hemispherical'))
    g.edge('Nygolaiminae_006', 'Clavicaudoides',  label=label2('Tooth deltoid to linear; body ventrally curved; tail hemispherical to clavate'))

    # Subfamily Solididentinae Ahmad and Jairajpuri, 1982
    g.edge('Solididentinae', 'Solididens',  label=label2('Body C- or S-shaped; lip region offset by constriction'))
    g.edge('Solididentinae', 'Solididentinae_002',  label=label2('Body almost straight; lip region continuous with body contour'))

    g.edge('Solididentinae_002', 'Feroxides',  label=label2('Tail short, bluntly rounded'))
    g.edge('Solididentinae_002', 'Clavicauda',  label=label2('Tail long with clavate terminus'))

    # Family Nygellidae Andrassy, 1958
    g.edge('Nygellidae', 'Nygellinae')

    # Family Aetholaimidae Jairajpuri, 1965
    g.edge('Aetholaimidae', 'Aetholaiminae')

    # Subfamily Aetholaiminae Jairajpuri, 1965
    g.edge('Aetholaiminae', 'Aetholaimus')

    # Family Nygolaimellidae Clark, 1961
    g.edge('Nygolaimellidae', 'Nygolaimiinae',  label=label2('Pharynx with rasp-like area of minute denticles'))
    g.edge('Nygolaimellidae', 'Nygolaimellinae',  label=label2('Pharynx without rasp-like area'))

    # Subfamily Nygolaimellinae Clark, 1961
    g.edge('Nygolaimellinae', 'Nygolaimellus',  label=label2('Basal expanded part of esophagus bibulbular; cardiac disk present'))
    g.edge('Nygolaimellinae', 'Nygolaimellinae_002',  label=label2('Basal expanded part of esophagus simple; cardiac disk absent'))

    g.edge('Nygolaimellinae_002', 'Aporcelaimoides',  label=label2('Mural tooth dorylaimoid, long, with dorsal aperture'))
    g.edge('Nygolaimellinae_002', 'Scapidens',  label=label2('Mural tooth small without dorsal aperture'))

    # Subfamily Nygolaimiinae Andrássy, 1976
    g.edge('Nygolaimiinae', 'Nygolaimium')

    # Suborder Campydorina Jairajpuri, 1983
    g.edge('Campydorina', 'Campydoroidea')

    # Superfamily Campydoroidea Thorne, 1935
    g.edge('Campydoroidea', 'Campydora')


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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
