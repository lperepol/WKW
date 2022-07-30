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
    #http://nemaplex.ucdavis.edu/Plntpara/Criconematoidea%20and%20Criconematidae.html
    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv ') #, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6 '))
    g.graph_attr['rankdir'] = 'LR'

    g.node('C000', label=label2('Key to Families  of the Superfamily Criconematoidea '),fillcolor='red',style="filled")
    g.edge('C000', 'C001', label='')
    g.node('C001', 'C001',fillcolor='aqua',style="filled" )
    g.edge('C001','C002', label=label2('Cuticle thick,coarsely annulated,  often with extensions,  isthmus broad amalgamated  with basal bulb'))
    g.edge('C001','C003', label=label2('Cuticle thin,  finely annulated,  without extensions,  isthmus slender,  not amalgamated  with basal bulb'))

    g.node('C002', 'C002',fillcolor='aqua',style="filled" )
    g.edge('C002','Criconematidae', label=label2('Females and juveniles cigar-shaped;  cuticular annules retrorse,  often with extensions;  male tail short,  bursa small or absent'))
    g.edge('C002','Hemicycliophoridae', label=label2('Females and juveniles slender, vermiform;  cuticular annules rounded;  male tail long,  bursa large'))

    g.node('C003', 'C003',fillcolor='aqua',style="filled" )
    g.edge('C003','Paratylenchidae', label=label2('Mature female vermiform to elongate-obese;  procorpus of esophagus wide;  stylet may be long'))
    g.edge('C003','C004', label=label2('Mature female saccate or spherical;  procorpus of esophagus slender;  stylet short'))

    g.node('C004', 'C004',fillcolor='aqua',style="filled" )
    g.edge('C004','Sphaeronematidae', label=label2('Mature female spherical,  vulva terminal;  excretory pore in anterior  25% of body'))
    g.edge('C004','Tylenchulidae', label=label2('Mature female elongate-obese;  vulva not terminal;  excretory pore at >50% of body length'))

    g.node('Criconematidae', 'Criconematidae',fillcolor='aqua',style="filled" )
    g.edge('Criconematidae','Hemicriconemoides', label=label2('Female with a cuticular sheath of rounded annules'))
    g.edge('Criconematidae','002', label=label2('Female without cuticular sheath'))

    g.node('002', '002',fillcolor='aqua',style="filled" )
    g.edge('002','003', label=label2('Cuticular annules in females and juveniles with scales, spines or other extensions'))
    g.edge('002','009', label=label2('Cuticular annules in females smooth, occasionally with extensions in juveniles'))

    g.node('003', '003',fillcolor='aqua',style="filled" )
    g.edge('003','Blandicephalonema', label=label2('Cephalic region small, knob-like'))
    g.edge('003','004', label=label2('Cephalic region not knob-like, usually with two annules'))

    g.node('004', '004',fillcolor='aqua',style="filled" )
    g.edge('004','Crossonema', label=label2('Each cuticular annule with continuous fringe of spines'))
    g.edge('004','005', label=label2('Extensions of cuticular annules separated, not fringe-like'))

    g.node('005', '005',fillcolor='aqua',style="filled" )
    g.edge('005','Croserinema', label=label2('Cuticular extensions in alternating rows'))
    g.edge('005','006', label=label2('Cuticular extensions not alternating, arranged in longitudinal rows'))

    g.node('006', '006',fillcolor='aqua',style="filled" )
    g.edge('006','Paterocephalonema', label=label2('One large saucer-shaped cephalic annule'))
    g.edge('006','007', label=label2('Two, sometimes three, moderately-sized cephalic annules'))

    g.node('007', '007',fillcolor='aqua',style="filled" )
    g.edge('007','Bakernema', label=label2('Cuticular extensions transparent, membranous'))
    g.edge('007','008', label=label2('Cuticular extensions not membranous'))

    g.node('008', '008',fillcolor='aqua',style="filled" )
    g.edge('008','Orphreyus', label=label2('Shape and size of cuticular extensions differ on dorsal and ventral sides'))
    g.edge('008','Ogma', label=label2('Shape and size of cuticular extensions similar on dorsal and ventral sides'))

    g.node('009', '009',fillcolor='aqua',style="filled" )
    g.edge('009','010', label=label2('Annules of juveniles with longitudinal rows of scales or spines; females with smmoth annules, except in tail region'))
    g.edge('009','013', label=label2('Annules of both juveniles and females without scales or spines'))

    g.node('010', '010',fillcolor='aqua',style="filled" )
    g.edge('010','Neolobocriconema', label=label2('Scales and spines present on annules in posterior region of females'))
    g.edge('010','011', label=label2('Scales and spines not present on annules in posterior region of females'))

    g.node('011', '011',fillcolor='aqua',style="filled" )
    g.edge('011','Lobocriconema', label=label2('Cephalic region with submedial lobes'))
    g.edge('011','012', label=label2('Cephalic region without submedial lobes'))

    g.node('012', '012',fillcolor='aqua',style="filled" )
    g.edge('012','Amphisbaenema', label=label2('Head with one dome-shaped annule; annules with encrustations'))
    g.edge('012','Criconema', label=label2('Head with two ring-like annules; annules without encrustations'))

    g.node('013', '013',fillcolor='aqua',style="filled" )
    g.edge('013','Mesocriconema', label=label2('Vulva open; cephalic region with submedial lobes'))
    g.edge('013','014', label=label2('Vulva closed; cephalic region without submedial lobes'))

    g.node('014', '014',fillcolor='aqua',style="filled" )
    g.edge('014','Discocriconemella', label=label2('Anterior cephalic annule disc-like, offset by a collar'))
    g.edge('014','015', label=label2('Anterior cephalic annule not disc-like, not offset'))

    g.node('015', '015',fillcolor='aqua',style="filled" )
    g.edge('015','Xenocriconemella', label=label2('Stylet exceedingly long, flexible'))
    g.edge('015','016', label=label2('Stylet not exceedingly long, not flexible'))

    g.node('016', '016',fillcolor='aqua',style="filled" )
    g.edge('016','Nothocriconemoides', label=label2('Anterior lip of vulva overhanging aperture '))
    g.edge('016','Criconemoides', label=label2('Anterior lip of vulva not overhanging aperture '))

    #http://nemaplex.ucdavis.edu/Taxadata/G058.aspx
    g.node('Hemicriconemoides', 'Hemicriconemoides',fillcolor='aqua',style="filled" )
    g.edge('Hemicriconemoides','H. obtusus', label=label2('Lip region strongly offset '))
    g.edge('Hemicriconemoides','H002', label=label2('Lip region slightly offset or not offset '))


    g.node('H002', 'H002',fillcolor='aqua',style="filled" )
    g.edge('H002','H. strictathecatus', label=label2('Stylet knobs rounded without forward processes '))
    g.edge('H002','H003', label=label2('Stylet knobs anchor shaped with prominent forward processes '))

    g.node('H003', 'H003',fillcolor='aqua',style="filled" )
    g.edge('H003','H. brevicaudatus', label=label2('Vulva on 2nd annule from tail tip, fewer than 56 annules in sheath, sheath annules rounded '))
    g.edge('H003','H004', label=label2('Vulva on 7th to 21st annule from tail tip, more than 75 annules in sheath, sheath annules flattened '))

    g.node('H004', 'H004',fillcolor='aqua',style="filled" )
    g.edge('H004','H005', label=label2('Stylet < 46 µm '))
    g.edge('H004','H006', label=label2('Stylet > 46 µm '))

    g.node('H005', 'H005',fillcolor='aqua',style="filled" )
    g.edge('H005','H006', label=label2('Vulval sheath present '))
    g.edge('H005','H010', label=label2('Vulval sheath absent '))

    g.node('H006', 'H006',fillcolor='aqua',style="filled" )
    g.edge('H006','H007', label=label2('Fewer than 98 annules in sheath '))
    g.edge('H006','H009', label=label2('More than 98 annules in sheath '))

    g.node('H007', 'H007',fillcolor='aqua',style="filled" )
    g.edge('H007','H. minutus', label=label2('Stylet > 71 µm '))
    g.edge('H007','H008', label=label2('Stylet < 60 µm '))

    g.node('H008', 'H008',fillcolor='aqua',style="filled" )
    g.edge('H008','H. wessoni', label=label2('Tail narrows abruptly after anus '))
    g.edge('H008','H. intermedius', label=label2('Tail regularly conoid after anus '))

    g.node('H009', 'H009',fillcolor='aqua',style="filled" )
    g.edge('H009','H. brachyurus', label=label2('Lip region rounded, no amphidial plate, tail rounded '))
    g.edge('H009','H. cocophilus', label=label2('Lip region truncate, no amphidial plate, tail tapered '))

    g.node('H010', 'H010',fillcolor='aqua',style="filled" )
    g.edge('H010','H. kanayaensis', label=label2('Lip region conoid, vulva on 16th to 21st annule from tail tip '))
    g.edge('H010','H011', label=label2('Lip region rounded to truncate, vulva on 7th to 17th annule from tail tip '))

    g.node('H011', 'H011',fillcolor='aqua',style="filled" )
    g.edge('H011','H. insignis', label=label2('Lip region with a conspicuously large annule '))
    g.edge('H011','H012', label=label2('Lip region with 2 distinct annules '))

    g.node('H012', 'H012',fillcolor='aqua',style="filled" )
    g.edge('H012','H. parvus', label=label2('Length = 0.29-0.38 mm '))
    g.edge('H012','H013', label=label2('Length = 0.41-0.61 mm '))

    g.node('H013', 'H013',fillcolor='aqua',style="filled" )
    g.edge('H013','H. pseudobrachyurum', label=label2('Fewer than 104 annules in sheath, stylet < 60 µm '))
    g.edge('H013','H014', label=label2('More than 104 annules in sheath, stylet > 60 µm '))

    g.node('H014', 'H014',fillcolor='aqua',style="filled" )
    g.edge('H014','H. mangiferae', label=label2('Tail rounded or convex to conoid '))
    g.edge('H014','H015', label=label2('Tail conoid, tapering to an angular tip '))

    g.node('H015', 'H015',fillcolor='aqua',style="filled" )
    g.edge('H015','H. gaddi', label=label2('Lip region rounded, not offset, first annule rounded, second annule as large or larger than first '))
    g.edge('H015','H. chitwoodi', label=label2('Lip region truncate, slightly offset, first annule angular, second annule smaller than first '))


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
