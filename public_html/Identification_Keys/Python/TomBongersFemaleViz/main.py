# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
import pandas as pd

def readSpreadSheet():
    fn = ''
    excel_data_df = pandas.read_excel('records.xlsx', sheet_name='Employees')

def label2(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    str = ""
    for i in grouped_words:
        str = str + i + "\n"
    return str

def draw():
    #http://nemaplex.ucdavis.edu/Uppermnus/nematamnu.htm#Taxonomic_Keys
    #http://nemaplex.ucdavis.edu/Taxadata/Tylenchidaekey2008.htm
    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'

    GraphTitle = 'Key to the\n Genera of\n Tylenchidae'
    g.node('000', label=GraphTitle,fillcolor='red',style="filled")
    g.edge('000', '001', label2(''))

    g.node('001', '001',fillcolor='aqua',style="filled" )
    g.edge('001','002', label2('Female didelphic'))
    g.edge('001','004', label2('Female monodelphic'))

    g.node('002', '002',fillcolor='aqua',style="filled" )
    g.edge('002','Antarctenchus', label2('Cephalic framework moderately sclerotized; vulva provided with lateral vulval membranes; male cloaca provided with large hypoptygmata'))
    g.edge('002','003', label2('Cephalic framework not sclerotized; vulva without lateral vulval membranes; male without hypoptygmata'))

    g.node('003', '003',fillcolor='aqua',style="filled" )
    g.edge('003','Psilenchus', label2('Head high with distinct amphidial slit on the lateral side; median bulb usually behind middle of pharynx'))
    g.edge('003','Atetylenchus', label2('Head low with indistinct amphidial slit; median bulb anterior to middle of pharynx'))

    g.node('004', '004',fillcolor='aqua',style="filled" )
    g.edge('004','005', label2('Stylet = 76-104µm'))
    g.edge('004','Epicharinema', label2('Stylet = 38-52µm'))
    g.edge('004','006', label2('Stylet = 22-34µm'))
    g.edge('004','007', label2('Stylet less than 22µm'))

    g.node('005', '005',fillcolor='aqua',style="filled" )
    g.edge('005','Tylodorus', label2('Cephalic region continuous, not lobed; lateral field beginning near middle of pharynx'))
    g.edge('005','Arboritynchus', label2('Cephalic region offset, with four prominent lobes; lateral field beginning at base of pharynx'))

    g.node('006', '006',fillcolor='aqua',style="filled" )
    g.edge('006','Campbellenchus', label2('Cuticle with longitudinal ridges'))
    g.edge('006','Gracilancea', label2('Cuticle without longitudinal ridges except for the lateral field'))

    g.node('007', '007',fillcolor='aqua',style="filled" )
    g.edge('007','008', label2('Head provided with setae'))
    g.edge('007','009', label2('Head without setae'))

    g.node('008', '008',fillcolor='aqua',style="filled" )
    g.edge('008','Atetylenchus', label2('Vulva covered by longitudinal flap, male without caudal alae; cloaca provided with large hypoptytgmata'))
    g.edge('008','Eutylenchus', label2('Vulva with lateral vulval flaps; male with caudal alae; cloaca raised'))

    g.node('009', '009',fillcolor='aqua',style="filled" )
    g.edge('009','010', label2('Cuticle provided with longitudinal ridges'))
    g.edge('009','014', label2('Cuticle without longitudinal ridges except for the lateral field'))

    g.node('010', '010',fillcolor='aqua',style="filled" )
    g.edge('010','011', label2('Stylet conus about 1/3 of stylet length'))
    g.edge('010','013', label2('Stylet conus about 1/2 of stylet length'))

    g.node('011', '011',fillcolor='aqua',style="filled" )
    g.edge('011','Ridgellus', label2('The longitudinal ridges mask the transverse body annulations; lateral field not distinct (the mid-lateral ridge appears slightly larger than the others)'))
    g.edge('011','012', label2('The longitudinal ridges divide the transverse annulations into blocks'))

    g.node('012', '012',fillcolor='aqua',style="filled" )
    g.edge('012','Neothada', label2('Lateral field with four lines'))
    g.edge('012','Ecphyadophoriodes', label2('Lateral field with two lines, very thin animals'))

    g.node('013', '013',fillcolor='aqua',style="filled" )
    g.edge('013','Pleurotylencus', label2('Vulva covered by longitudinal flap; stylet = 17-19µm'))
    g.edge('013','Coslenchus', label2('Vulva with lateral flaps (sometimes small or absent); stylet less than 15µm (exceptionally 17-19µm'))

    g.node('014', '014',fillcolor='aqua',style="filled" )
    g.edge('014','015', label2('Stylet conus about 1/3 of stylet length'))
    g.edge('014','015', label2('Stylet conus about 1/2 stylet length'))

    g.node('015', '015',fillcolor='aqua',style="filled" )
    g.edge('015','016', label2('Boleodoridinae Head high with oblique or transverse amphidial slit on the lateral side'))
    g.edge('015','018', label2('Head variously shaped, amphidial slit longitudinally oriented or only present on the front (than not seen by light microscopy'))

    g.node('016', '016',fillcolor='aqua',style="filled" )
    g.edge('016','Boleodorus', label2('Body ventrally curved, sometimes in spiral; female reproductive system with offset spermatheca filled with small refractive sperm and ovary with oocytes in multiple rows'))
    g.edge('016','017', label2('Body straight or only slightly curved; sperm not refractive and oocytes not in multiple rows'))

    g.node('017', '017',fillcolor='aqua',style="filled" )
    g.edge('017','Neopsilenchus', label2('Anterior part of stylet not conical but with wide lumen, stylet without knobs'))
    g.edge('017','Basiria', label2('Anterior part of stylet conical with the usual very fine lumen; stylet with or without knobs'))

    g.node('018', '018',fillcolor='aqua',style="filled" )
    g.edge('018','Cucullitylenchus', label2('Head with large dome-shaped structure'))
    g.edge('018','019', label2('Head with small disc-like structure at front end'))
    g.edge('018','020', label2('Head with smooth contour'))

    g.node('019', '019',fillcolor='aqua',style="filled" )
    g.edge('019','Mitranema', label2('Very slender, (a-value=62-67); caudal alae posteriorly concave'))
    g.edge('019','Discotylenchus', label2('Not so slender; caudal alae rounded, no vulval flaps'))
    g.edge('019','Malenchus', label2('Not so slender; caudal alae rounded, distinct vulval flaps'))

    g.node('020', '020',fillcolor='aqua',style="filled" )
    g.edge('020','021', label2('Very slender body (a-value 60-180); bursa lobed'))
    g.edge('020','022', label2('Very slender body, bursa not lobed'))
    g.edge('020','023', label2('Body not extremely slender; bursa (if present) not lobed'))

    g.node('021', '021',fillcolor='aqua',style="filled" )
    g.edge('021','Ecyphyadophora', label2('Body constricted at vulva; head quadrangular (amphidial openings small pores on front, not distinct with light microscopy)'))
    g.edge('021','Tenunemellus', label2('Body not constricted at vulva; head dorso-ventrally flattened; long sinuous amphidial aperture'))

    g.node('022', '022',fillcolor='aqua',style="filled" )
    g.edge('022','Ultratenella', label2('Lateral field absent'))
    g.edge('022','Chilenchus', label2('Lateral field prominent with four lines'))

    g.node('023', '023',fillcolor='aqua',style="filled" )
    g.edge('023','024', label2('Cuticular annuli deeply incised'))
    g.edge('023','027', label2('Cuticular annuli not so deeply incised, sometimes indistinct'))

    g.node('024', '024',fillcolor='aqua',style="filled" )
    g.edge('024','Thada', label2('Stylet with minute swellings, median bulb hardly developed'))
    g.edge('024','025', label2('Stylet with small knobs, median bulb hardly or well developed'))

    g.node('025', '025',fillcolor='aqua',style="filled" )
    g.edge('025','Miculenchus', label2('Annuli zigzag in surface view; annulations continue on the head; male without caudal alae'))
    g.edge('025','026', label2('Annuli normal; male with caudal alae'))

    g.node('026', '026',fillcolor='aqua',style="filled" )
    g.edge('026','Silenchus', label2('Vulva with projecting vulval lips, male with elongated bursa'))
    g.edge('026','Malenchus', label2('Vulva sunken in body; male with rather short, ad-cloacal bursa'))

    g.node('027', '027',fillcolor='aqua',style="filled" )
    g.edge('027','Lelenchus', label2('Head dorso-ventrally flattened with longitudinal sinuous amphidial apertures; the small head contains large amphidial pouches; body usually very slender'))
    g.edge('027','028', label2('Head quadrangular with usually longitudinal (but not sinuous) amphidial apertures; amphidial pouches not distinct; relatively thicker species'))

    g.node('028', '028',fillcolor='aqua',style="filled" )
    g.edge('028','Irantylenchus', label2('Clavate stylet knobs with ventrally situated opening of pharyngeal lumen; dorsal gland has opening one half to one stylet length posterior to knobs'))
    g.edge('028','029', label2('Stylet has rounded knobs; dorsal gland opening  close to knobs'))

    g.node('029', '029',fillcolor='aqua',style="filled" )
    g.edge('029','Fraglenchus', label2('Lateral vulval membranes'))
    g.edge('029','030', label2('Lateral vulval membranes absent'))

    g.node('030', '030',fillcolor='aqua',style="filled" )
    g.edge('030','Sakia', label2('Median bulb underdeveloped, no valves'))
    g.edge('030','Filenchus', label2('Median bulb slightly or well developed, with valves'))

    g.node('031', '031',fillcolor='aqua',style="filled" )
    g.edge('031','032', label2('Vulva provided with lateral flaps'))
    g.edge('031','033', label2('Vulva without flaps'))

    g.node('032', '032',fillcolor='aqua',style="filled" )
    g.edge('032','Allotylenchus', label2('Lateral field with two lines; vagina thin; post-vulval sac short'))
    g.edge('032','Aglenchus', label2('Lateral field with three lines (but the two ridges can slightly separate so that in total four lines can sometimes be seen); vagina thickened; post-vulval sac short'))
    g.edge('032','Fraglenchus', label2('Lateral field with four lines, vagina not swollen, no post-vulval uterine sac'))
    g.edge('032','Cephalenchus', label2('Lateral field usually with six lines, sometimes four lines; vagina not thickened; post-vulval uterine sac well developed'))

    g.node('033', '033',fillcolor='aqua',style="filled" )
    g.edge('033','Tanzanius', label2('Pharynx without median bulb'))
    g.edge('033','034', label2('Pharynx with median bulb'))

    g.node('034', '034',fillcolor='aqua',style="filled" )
    g.edge('034','035', label2('Lateral field and body annulations at mid-body mostly inconspicuous'))
    g.edge('034','036', label2('Lateral field and body annulations distinct; caudal alae distinct'))

    g.node('035', '035',fillcolor='aqua',style="filled" )
    g.edge('035','Cervoannulatus', label2('A few large annuli just posterior to the head'))
    g.edge('035','Polenchus', label2('Not such large annuli'))

    g.node('036', '036',fillcolor='aqua',style="filled" )
    g.edge('036','Silenchus', label2('Vulva with projecting vulval lips, male with elongated bursa'))
    g.edge('036','Tylenchus', label2('Vulva plain, male with shorter, ad-cloacal bursa'))

    g.render('NematodaKey.gv', format='svg', view=True)
    g.render('NematodaKey.gv', format='jpg', view=False)
    g.render('NematodaKey.gv', format='pdf', view=False)


    #g.node('', '',fillcolor='aqua',style="filled" )
    #g.edge('','', label2('')
    #g.edge('','', label2('')


def main():
    # Use a breakpoint in the code line below to debug your script.
    draw()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
