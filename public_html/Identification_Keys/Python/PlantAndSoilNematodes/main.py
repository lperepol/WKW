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
    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6'))
    g.graph_attr['rankdir'] = 'LR'

    GraphTitle = 'Key to Families\n(and Subfamilies) of\n Plant and Soil Nematodes'
    g.node('000', label=GraphTitle,fillcolor='red',style="filled")
    g.edge('000', '001', label2(''))

    g.node('001', '001',fillcolor='aqua',style="filled" )
    g.edge('001','002', label2('Nematodes with a protrusible stylet (stomatostyle) or spear (odontostyle)'))
    g.edge('001','024', label2('Nematodes without protrusible stylet or spear'))

    g.node('002', '002',fillcolor='aqua',style="filled" )
    g.edge('002','003', label2('Stylet and three-part esophagus with median bulb (metacorpus), males with or without bursa'))
    g.edge('002','016', label2('Spear and two-part esophagus with posterior swollen (postcorpus), males usually without bursa but with supplements  '))

    g.node('003', '003',fillcolor='aqua',style="filled" )
    g.edge('003','004', label2('Median bulb large with refractive valve, flattened against body wall, stylet knobs absent or small'))
    g.edge('003','005', label2('Median bulb not refractive, stylet knobs obvious'))

    g.node('004', '004',fillcolor='aqua',style="filled" )
    g.edge('004','Aphelenchidae', label2('Stylet without knobs, tail rounded, male with bursa'))
    g.edge('004','Aphelenchoididae', label2('Stylet with small knobs, tail pointed, male usually without bursa'))

    g.node('005','005',fillcolor='aqua',style="filled" )
    g.edge('005','006', label2('Esophageal glands overlap intestine'))
    g.edge('005','011', label2('Esophageal glands enclosed in bulb that abuts intestine'))

    g.node('006', '006',fillcolor='aqua',style="filled" )
    g.edge('006','007', label2('Cephalic framework well-developed, lip-region high; females with two gonads'))
    g.edge('006','010', label2('Posterior gonad reduced to a post-uterine sac, vulva at 70-90%, lip-region flattened or cephalic framework absent '))

    g.node('007', '007',fillcolor='aqua',style="filled" )
    g.edge('007','008', label2('Tail tip, anus and vulva in close proximity on posterior of swollen female, male body twisted, male without bursa'))
    g.edge('007','009', label2('Anus and vulva anterior to tail tip even when female swollen, male body not twisted, male with bursa'))

    g.node('008', '008',fillcolor='aqua',style="filled" )
    g.edge('008','Heteroderidae', label2('Juvenile and female stages are sedentary endoparasites, female greatly swollen; male without bursa, body twisted, migratory in soil Body of dead female forms cyst and retains some or all eggs – subfam. Heteroderinae'))
    g.edge('008','Heteroderidae', label2('Juvenile and female stages are sedentary endoparasites, female greatly swollen; male without bursa, body twisted, migratory in soil Female body does not form cyst, eggs deposited in matrix – subfam. Meloidogyninae'))
    g.edge('008','Heteroderidae', label2('Adult females sedentary endoparasites, greatly swollen; pre-adults vermiform; male without bursa, body twisted, migratory in soil Female body does not form cyst, eggs deposited in matrix – subfam. Nacobboderinae'))

    g.node('009', '009',fillcolor='aqua',style="filled" )
    g.edge('009','Hoplolaimidae', label2('Stylet 2-3 x stylet body diameter, tail < 2 x anal body diameter, body spiral when heat-killed, vulva around 60% Mature female remains vermiform – subfam. Hoplolaiminae '))
    g.edge('009','Hoplolaimidae', label2('Stylet 2-3 x stylet body diameter, tail < 2 x anal body diameter, body spiral when heat-killed, vulva around 60% Mature female saccate sedentary semi-endoparasite – subfam. Rotylenchulinae'))
    g.edge('009','Dolichodoridae', label2('Tail > 2.5 x anal body diameter, phasmids on tail region  Long nematodes, stylet > 3 x stylet body diameter – subfam. Belonolaiminae'))
    g.edge('009','Dolichodoridae', label2('Tail > 2.5 x anal body diameter, phasmids on tail region Stylet < 1.5 x stylet body diameter – subfam. Telotylenchinae'))

    g.node('010', '010',fillcolor='aqua',style="filled" )
    g.edge('010','Pratylenchidae', label2('Lip-region flattened but cephalic framework well-developed Female remains vermiform – subfam. Pratylenchinae  '))
    g.edge('010','Pratylenchidae', label2('Lip-region flattened but cephalic framework well-developed Female a saccate endoparasite – subfam. Nacobbinae'))
    g.edge('010','Anguinidae', label2('Cephalic-framework weak or absent'))

    g.node('011', '011',fillcolor='aqua',style="filled" )
    g.edge('011','Dolichodoridae', label2('Females with two gonads, males with caudal bursa '))
    g.edge('011','012', label2('Posterior female gonad reduced to a post-uterine sac, males with adanal bursa (if present)'))

    g.node('012', '012',fillcolor='aqua',style="filled" )
    g.edge('012','013', label2('Stylet short (< stylet body diameter), tail pointed to filiform'))
    g.edge('012','014', label2('Stylet long so that knobs are close to median bulb valve, procorpus swollen and fused with metacorpus'))

    g.node('013', '013',fillcolor='aqua',style="filled" )
    g.edge('013','Tylenchidae', label2('Tail long and filiform (>5 x anal body diameter)'))
    g.edge('013','Anguinidae', label2('Tail pointed (<5 x anal body diameter), cephalic framework absent '))

    g.node('014', '014',fillcolor='aqua',style="filled" )
    g.edge('014','015', label2('Thick cuticle with coarse striations'))
    g.edge('014','Tylenchulidae', label2('Female swollen, excretory pore posterior on body, female a saccate sedentary semi-endoparasite – subfam. Tylenchulinae'))
    g.edge('014','Tylenchulidae', label2('Cuticle with fine striations, male often without stylet, body C-shaped – subfam. Paratylenchinae'))

    g.node('015', '015',fillcolor='aqua',style="filled" )
    g.edge('015','Criconematidae', label2('Large body diameter, sausage shape, slow moving, anchor-shaped stylet knobs – subfam. Criconematinae '))
    g.edge('015','Criconematidae', label2('Extra cuticular sheath, pointed tail, rounded stylet knobs – subfam. Hemicycliophorinae'))

    g.node('016', '016',fillcolor='aqua',style="filled" )
    g.edge('016','Diphtherophoridae', label2('Spear with complex configuration, loose-fitting cuticle'))
    g.edge('016','017', label2('Spear simple, cuticle not loose but may be swollen'))

    g.node('017', '017',fillcolor='aqua',style="filled" )
    g.edge('017','Trichodoridae', label2('Spear dorsally curved, anus almost terminal'))
    g.edge('017','018', label2('Spear straight, anus not terminal - tail present'))

    g.node('018', '018',fillcolor='aqua',style="filled" )
    g.edge('018','Longidoridae', label2('Long, slender nematodes (1-12 mm), spear > 50 µm, long spear extension (odontophore)'))
    g.edge('018','019', label2('Short spear'))

    g.node('019', '019',fillcolor='aqua',style="filled" )
    g.edge('019','Belondiridae', label2('Postcorpus of esophagus with muscular sheath'))
    g.edge('019','020', label2('No muscular sheath around esophagus'))

    g.node('020', '020',fillcolor='aqua',style="filled" )
    g.edge('020','Leptonchidae', label2('Spear extension (odontophore) thick and curved '))
    g.edge('020','021', label2('Spear extension not curved '))

    g.node('021', '021',fillcolor='aqua',style="filled" )
    g.edge('021','022', label2('Plump nematodes, tail rounded, with or without point'))
    g.edge('021','023', label2('Slender nematodes, tail conoid to filiform'))

    g.node('022', '022',fillcolor='aqua',style="filled" )
    g.edge('022','Nordiidae', label2('Spear slightly curved, small opening'))
    g.edge('022','Aporcelaimidae', label2('Spear with large opening, cuticle appears layered at tail'))

    g.node('023', '023',fillcolor='aqua',style="filled" )
    g.edge('023','Thornenematidae', label2('Large nematodes (>2 mm), tail filiform (may be rounded in male)'))
    g.edge('023','Qudsianematidae', label2('Medium size (1-2 mm), tail conoid, body generally curved'))

    g.node('024', '024',fillcolor='aqua',style="filled" )
    g.edge('024','Bunonematidae', label2('Body asymmetrical, caterpillar-like'))
    g.edge('024','025', label2('Body symmetrical'))

    g.node('025', '025',fillcolor='aqua',style="filled" )
    g.edge('025','Diplogastridae', label2('Median bulb present, tail filiform'))
    g.edge('025','026', label2('Median bulb absent'))

    g.node('026', '026',fillcolor='aqua',style="filled" )
    g.edge('026','027', label2('Esophagus with terminal bulb or swelling'))
    g.edge('026','037', label2('Esophagus cylindrical, no swellings'))

    g.node('027', '027',fillcolor='aqua',style="filled" )
    g.edge('027','028', label2('Terminal bulb without valves'))
    g.edge('027','029', label2('Terminal bulb with valves'))

    g.node('028', '028',fillcolor='aqua',style="filled" )
    g.edge('028','Monhysteridae', label2('Cuticle not striated'))
    g.edge('028','Bastianiidae', label2('Cuticle clearly striated '))

    g.node('029', '029',fillcolor='aqua',style="filled" )
    g.edge('029','Chromadoridae', label2('Aquatic forms;  cuticle striated and punctated '))
    g.edge('029','030', label2('Cuticle without punctations'))

    g.node('030', '030',fillcolor='aqua',style="filled" )
    g.edge('030','Diplogastridae', label2('Stoma cavity with teeth, tail filiform'))
    g.edge('030','031', label2('Stoma cavity without teeth'))

    g.node('031', '031',fillcolor='aqua',style="filled" )
    g.edge('031','032', label2('Head with labial extensions or crown'))
    g.edge('031','032', label2('Head without extensions'))

    g.node('032', '032',fillcolor='aqua',style="filled" )
    g.edge('032','Plectidae', label2('Head with lateral cuticular extensions'))
    g.edge('032','033', label2('Head with anterior extensions only'))

    g.node('033', '033',fillcolor='aqua',style="filled" )
    g.edge('033','Teratocephalidae', label2('Labial extensions crown-shaped'))
    g.edge('033','Cephalobidae', label2('Labial-extensions thorn- or antler-shaped'))

    g.node('034', '034',fillcolor='aqua',style="filled" )
    g.edge('034','Plectidae', label2('Tail tip with spinneret, amphids easily visible, males with tubular supplements'))
    g.edge('034','035', label2('Tail tip without spinneret'))

    g.node('035', '035',fillcolor='aqua',style="filled" )
    g.edge('035','Rhabditidae', label2('Stoma cavity cylindrical, cuticular walls, males with bursa'))
    g.edge('035','036', label2('Stoma cavity funnel-shaped, walls not cuticular, posterior female gonad reduced, anterior gonad reflexed and extending beyond vulva'))

    g.node('036', '036',fillcolor='aqua',style="filled" )
    g.edge('036','Panagrolaimidae', label2('Stoma cavity clearly present, anteriorly cylindrical'))
    g.edge('036','Cephalobidae', label2('Stoma cavity difficult to see, only anterior section open'))

    g.node('037', '037',fillcolor='aqua',style="filled" )
    g.edge('037','Bastianiidae', label2('Cuticle striated'))
    g.edge('037','038', label2('Cuticle smooth '))

    g.node('038', '038',fillcolor='aqua',style="filled" )
    g.edge('038','Alaimidae', label2('Slender nematodes, no obvious stoma cavity or setae'))
    g.edge('038','039', label2('Clear stoma cavity or setae'))

    g.node('039', '039',fillcolor='aqua',style="filled" )
    g.edge('039','Monhysteridae', label2('Amphids round, clearly visible'))
    g.edge('039','040', label2('Amphids difficult to see, not round'))

    g.node('040', '040',fillcolor='aqua',style="filled" )
    g.edge('040','041', label2('Stoma cavity large, walls cuticular walls'))
    g.edge('040','042', label2('Stoma cavity funnel-shaped or closed anteriorly, walls not cuticular'))

    g.node('041', '041',fillcolor='aqua',style="filled" )
    g.edge('041','Prismatolaimidae', label2('Tail filiform, setae present '))
    g.edge('041','Mononchidae', label2('Tail not filiform, large stoma cavity with teeth '))

    g.node('042', '042',fillcolor='aqua',style="filled" )
    g.edge('042','Tobrilidae', label2('Funnel-shaped stoma with small teeth'))
    g.edge('042','Tripylidae', label2('Stoma closed anteriorly, one tooth and two tiny denticles in lumen'))


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
