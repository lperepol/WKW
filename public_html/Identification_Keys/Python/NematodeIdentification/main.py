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

    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')
    #, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'
    g.graph_attr['tooltip'] = " "



    g.node('000', label='UNL Nematology Lab\nInteractive Diagnostic Key \nto Plant Parasitic, \nFreeliving and Predaceous Nematodes',tooltip=" ",fillcolor='red',style="filled")
    g.edge('000','001',tooltip="tooltip 000->00")
    g.edge('001','002', xlabel='Cephalic setae\n indistinct or absent',tooltip="000tooltip 001->0")
    g.edge('001','064', xlabel='Cephalic setae\n absent \nbut setae-like head appendages present',tooltip="  tooltip 001->0")
    g.edge('001','069', label='Cephalic setae\n present',tooltip="  tooltip 001->0")

    g.node('002', '002',fillcolor='aqua',style="filled" )
    g.edge('002','003', xlabel='Stylet\n Visible')
    g.edge('002','038', xlabel='Stylet\n Absent')

    g.node('003', '003',fillcolor='aqua',style="filled" )
    g.edge('003','004', label='Knobbed')
    g.edge('003','029', label='No Knobs')

    g.node('004', '004',fillcolor='aqua',style="filled" )
    g.edge('004','005', label='Median\nBulb  Visible')
    g.edge('004','022', label='Median\nBulb  Absent')

    g.node('005', '005',fillcolor='aqua',style="filled" )
    g.edge('005','006', label='Females Eel-like')
    g.edge('005','021', label='Females Swollen')

    g.node('006', '006', fillcolor='aqua', style="filled")
    g.edge('006', '007', label='Vulva Mid-body')
    g.edge('006', '014', label='Vulva Lower third')

    g.node('007', '007', fillcolor='aqua', style="filled")
    g.edge('007', '008', label='Esophagus No\noverlap')
    g.edge('007', '011', label='Esophagus Overlapping\nintestine')


    g.node('008', '008', fillcolor='aqua', style="filled")
    g.edge('008', '009', label='Stylet < 80 μm')
    g.node('Genus\nDolichodorus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('008', 'Genus\nDolichodorus', label='Stylet > 80 μm')

    g.node('009', '009', fillcolor='aqua', style="filled")
    g.node('Genus\nTetylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('009', 'Tail\nTerminus Genus\nTetylenchus', label='Pointed')
    g.edge('009', '010', label='Tail\nTerminus Round')

    g.node('010', 'Tail\nTerminus', fillcolor='aqua', style="filled")
    g.node('Genus\nPsilenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('010', 'Genus\nPsilenchus', label='Knobbed')
    g.node('Genus\nTylenchorhynchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('010', 'Genus\nTylenchorhynchus', label='Round')

    g.node('011', 'Labium', fillcolor='aqua', style="filled")
    g.edge('011', '012', label='Offset')
    g.edge('011', '013', label='Flattened\namalgamated')

    g.node('012', 'Stylet', fillcolor='aqua', style="filled")
    g.node('Genus\nHoplolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('012', 'Genus\nHoplolaimus', label='40-50 μm\nfat')
    g.node('Genus\nBelonolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('012', 'Genus\nBelonolaimus', label='> 90 μm\n')

    g.node('013', 'Body', fillcolor='aqua', style="filled")
    g.node('Genus\nRadopholus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('013', 'Genus\nRadopholus', label='0.5-1 mm')
    g.node('Genus\nHirschmanniella', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('013', 'Genus\nHirschmanniella', label='2-3 mm')

    g.node('014', 'Cuticle', fillcolor='aqua', style="filled")
    g.edge('014', '015', label='Annulated')
    g.edge('014', '017', label='Smooth')

    g.node('015', 'Cuticle\nSheath', fillcolor='aqua', style="filled")
    g.edge('015', '016', label='Absent')
    g.node('Genus\nHemicycliophora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('015', 'Genus\nHemicycliophora', label='Visible')

    g.node('016', 'Annules\nSpines or Scales', fillcolor='aqua', style="filled")
    g.node('Genus\nCriconema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('016', 'Genus\nCriconema', label='Visible')
    g.node('Genus\nMesocriconema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('016', 'Genus\nMesocriconema', label='Absent')

    g.node('017', 'Body\nDeath Position ', fillcolor='aqua', style="filled")
    g.edge('017', '018', label='Straight')
    g.node('Genus\nHelicotylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('017', 'Genus\nHelicotylenchus', label='Spiral')

    g.node('018', 'Median/Bulb', fillcolor='aqua', style="filled")
    g.edge('018', '019', label='Inconspicous')
    g.node('Genus\nAphelenchoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('018', 'Genus\nAphelenchoides', label='Conspicous')

    g.node('019', 'Esophagus', fillcolor='aqua', style="filled")
    g.edge('019', '020', label='Overlapping\nIntestine')
    g.node('Genus\nTylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('019', 'Genus\nTylenchus', label='No\nOverlap')

    g.node('020', 'Median/Bulb', fillcolor='aqua', style="filled")
    g.node('Genus\nDitylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('020', 'Genus\nDitylenchus', label='Valves Small\nStylet weak')
    g.node('Genus\nPratylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('020', 'Genus\nPratylenchus', label='Valves and stylet\nwell developed,\nlabium flattened')

    g.node('021', 'Female Body', fillcolor='aqua', style="filled")
    g.node('Genus\nMeloidogyne', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('021', 'Genus\nMeloidogyne', label='White\nwithout eggs')
    g.node('Genus\nHeterodera', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('021', 'Genus\nHeterodera', label='Brown\nwith eggs')

    g.node('022', 'Stylet', fillcolor='aqua', style="filled")
    g.edge('022', '023', label='< 100 μm')
    g.node('Genus\nXiphinema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('022', 'Genus\nXiphinema', label='> 100 μm')

    g.node('023', 'Stylet', fillcolor='aqua', style="filled")
    g.edge('023', '024', label='Complex')
    g.edge('023', '025', label='Simple')

    g.node('024', 'Stylet', fillcolor='aqua', style="filled")
    g.node('Genus\nDiphtherophora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('024', 'Genus\nDiphtherophora', label='Anterior\narch-like')
    g.node('Genus\nTylencholaimellus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('024', 'Genus\nTylencholaimellus', label='Dorsal\nthickening')

    g.node('025', 'Stylet Knobs', fillcolor='aqua', style="filled")
    g.edge('025', '026', label='Elongate\nflange-like')
    g.edge('025', '027', label='Round')

    g.node('026', 'Tail', fillcolor='aqua', style="filled")
    g.node('Genus\nAulolaimoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('026', 'Genus\nAulolaimoides', label='Filiform')
    g.node('Genus\nEnchodelus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('026', 'Genus\nEnchodelus', label='Round')

    g.node('027', 'Tail', fillcolor='aqua', style="filled")
    g.edge('027', '028', label='Round')
    g.node('Genus\nNothotylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('027', 'Genus\nNothotylenchus', label='Pointed')

    g.node('028', 'Basal\npart', fillcolor='aqua', style="filled")
    g.node('Genus\nTylencholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('028', 'Genus\nTylencholaimus', label='Esophagus\nelongate')
    g.node('Genus\nDoryllium', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('028', 'Genus\nDoryllium', label='Esophagus\noval')

    g.node('029', 'Valvate median\nesophageal bulb',fillcolor='aqua',style="filled" )
    g.edge('029', '030', label='Absent')
    g.edge('029', '037', label='Visible')

    g.node('030', 'Stomal\nwalls',fillcolor='aqua',style="filled" )
    g.edge('030', '031', label='Not cuticularized')
    g.node('Genus\nActinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nActinolaimus', label='Cuticularized')
    g.node('Genus\nMetactinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nMetactinolaimus', label='Cuticularized')
    g.node('Genus\nNeoactinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nNeoactinolaimus', label='Cuticularized')
    g.node('Genus\nParactinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nParactinolaimus', label='Cuticularized')
    g.node('Genus\nActinolaimoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nActinolaimoides', label='Cuticularized')

    g.node('031', 'Esophagus',fillcolor='aqua',style="filled" )
    g.edge('031', '032', label='Basal\nexpansions')
    g.node('Genus\nOionchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('031', 'Genus\nOionchus', label='Expanding\nuniformly')

    g.node('032', 'Esophagus',fillcolor='aqua',style="filled" )
    g.edge('032', '033', label='Ovoid bulb\nat terminal fifth or sixth')
    g.edge('032', '036', label='Posterior\nthird swollen')

    g.node('033', 'Stylet\nAxial',fillcolor='aqua',style="filled" )
    g.edge('033', '034', label='Positioned centrally')
    g.node('Genus\nCampydora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('033', 'Genus\nCampydora', label='Not axial\norginating from tooth\nin stoma wall')

    g.node('034', 'Gonads',fillcolor='aqua',style="filled" )
    g.edge('034', '035', label='Paired\nvulva about 50%')
    g.node('Genus\nTyleptus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('034', 'Genus\nTyleptus', label='Single\nvulva > 50%')

    g.node('035', 'Stylet',fillcolor='aqua',style="filled" )
    g.node('Genus\nLeptonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('035', 'Genus\nLeptonchus', label='Slender')
    g.node('Genus\nDorylaimoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('035', 'Genus\nDorylaimoides', label='Thick')

    g.node('036', 'Stylet\nAxial',fillcolor='aqua',style="filled" )
    g.node('Genus\nDorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nDorylaimus', label='Central')
    g.node('Genus\nEudorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nEudorylaimus', label='Central')
    g.node('Genus\nLabronema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nLabronema', label='Central')
    g.node('Genus\nMesodorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nMesodorylaimus', label='Central')
    g.node('Genus\nThornia', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nThornia', label='Central')
    g.node('Genus\nLaimydorus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nLaimydorus', label='Central')
    g.node('Genus\nProdorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nProdorylaimus', label='Central')
    g.node('Genus\nDorylaiminae', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nDorylaiminae', label='Central')
    g.node('Genus\nNygolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nNygolaimus', label='Not axial\noriginating from\ntooth in stoma wall')

    g.node('037', 'Tail',fillcolor='aqua',style="filled" )
    g.node('Genus\nSeinura', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('037', 'Genus\nSeinura', label='Pointed ')
    g.node('Genus\nAphelenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('037', 'Genus\nAphelenchus', label='Rounded')

    g.node('038', 'Teeth',fillcolor='aqua',style="filled" )
    g.edge('038', '039', label='Visible')
    g.edge('038', '050', label='Absent/minute/indistinct')

    g.node('039', 'Esophagus',fillcolor='aqua',style="filled" )
    g.edge('039', '040', label='No mid-region\nexpansion')
    g.edge('039', '049', label='Expanded\nat mid-region')

    g.node('040', 'Tail',fillcolor='aqua',style="filled" )
    g.edge('040', '041', label='Pointed\nor tapering')
    g.edge('040', '047', label='Rounded')

    g.node('041', 'Male Tail\nSetae',fillcolor='aqua',style="filled" )
    g.edge('041', '042', label='None')
    g.node('Genus\nOncholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('041', 'Genus\nOncholaimus', label='Visible')

    g.node('042', 'Stoma\nDenticles ',fillcolor='aqua',style="filled" )
    g.edge('042', '043', label='Visible')
    g.edge('042', '045', label='Absent')

    g.node('043', 'Denticles',fillcolor='aqua',style="filled" )
    g.edge('043', '044', label='Scattered\nor in longitudinal rows')
    g.node('Genus\nMylonchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('043', 'Genus\nMylonchulus', label='In\ntransverse rows')

    g.node('044', 'Denticles',fillcolor='aqua',style="filled" )
    g.node('Genus\nPrionchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('044', 'Genus\nPrionchulus', label='On longitudinal\nrib of stoma')
    g.node('Genus\nSporonchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('044', 'Genus\nSporonchulus', label='Scattered\non stoma wall ')

    g.node('045', 'Tooth',fillcolor='aqua',style="filled" )
    g.edge('045', '046', label='Pointing\nforward')
    g.node('Genus\nAnatonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('045', 'Genus\nAnatonchus', label='Turned or\npointing backward')

    g.node('046', 'Tooth\nPosition',fillcolor='aqua',style="filled" )
    g.node('Genus\nIotonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('046', 'Genus\nIotonchus', label='In botton part of stoma')
    g.node('Genus\nMononchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('046', 'Genus\nMononchus', label='In top\npart of stoma')

    g.node('047', 'Stoma',fillcolor='aqua',style="filled" )
    g.edge('047', '048', label='With prominent medial\nor apical tooth')
    g.node('Genus\nBathyodontus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('047', 'Genus\nBathyodontus', label='With small\nbasal tooth')

    g.node('048', 'Stoma',fillcolor='aqua',style="filled" )
    g.node('Genus\nEnoplocheilus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('048', 'Genus\nEnoplocheilus', label='With 3 teeth\nwithout small basal tooth\ncaudal glands terminal')
    g.node('Genus\nMononchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('048', 'Genus\nMononchulus', label='With large anterior\n& small basal tooth\ncaudal glands ventral')

    g.node('049', 'Lip Region\nRib-Like Armature',fillcolor='aqua',style="filled" )
    g.node('Genus\nMononchoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('049', 'Genus\nMononchoides', label='Distinct')
    g.node('Genus\nDiplogaster', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('049', 'Genus\nDiplogaster', label='Absent')

    g.node('050', 'Esophagus',fillcolor='aqua',style="filled" )
    g.edge('050', '051', label='With basal\nexpansions')
    g.edge('050', '060', label='Uniformly\ncylindrical')

    g.node('051', 'Esophagus',fillcolor='aqua',style="filled" )
    g.edge('051', '052', label='Without\nmid-region expansion')
    g.edge('051', '055', label='Expanded\nat mid-region')

    g.node('052', 'Amphids',fillcolor='aqua',style="filled" )
    g.edge('052', '053', label='Distinct')
    g.edge('052', '054', label='Indistinct')

    g.node('053', 'Stoma\nWalls',fillcolor='aqua',style="filled" )
    g.node('Genus\nMicrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('053', 'Genus\nMicrolaimus', label='Anteriorly inflated\nwith minute tooth')
    g.node('Genus\nLeptolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('053', 'Genus\nLeptolaimus', label='Without tooth and\nwith straight,\ntapering sides')

    g.node('054', 'Stoma\nRod-Like Thickenings ',fillcolor='aqua',style="filled" )
    g.node('Genus\nRhabdolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('054', 'Genus\nRhabdolaimus', label='Distinct')
    g.node('Genus\nMonochromadora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('054', 'Genus\nMonochromadora', label='Indistinct')

    g.node('055', 'Gonads',fillcolor='aqua',style="filled" )
    g.edge('055', '056', label='Paired')
    g.edge('055', '058', label='Single')

    g.node('056', 'Stoma\nwalls',fillcolor='aqua',style="filled" )
    g.edge('056', '057', label='Straight\namalgamated')
    g.node('Genus\nAlloionema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('056', 'Genus\nAlloionema', label='Separated,\nnot straight')

    g.node('057', 'Metacorpus',fillcolor='aqua',style="filled" )
    g.node('Genus\nRhabditis', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('057', 'Genus\nRhabditis', label='Moderately swollen\nstoma not\nexcessively elongate')
    g.node('Genus\nCylindrocorpus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('057', 'Genus\nCylindrocorpus', label='Elongate\ncyclindrical metacorpus\nstoma elongate')

    g.node('058', 'Tail',fillcolor='aqua',style="filled" )
    g.edge('058', '059', label='Sharp\nterminus')
    g.node('Genus\nCephalobus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('058', 'Genus\nCephalobus', label='Bluntly conical')

    g.node('059', 'Stoma\nAnterior part',fillcolor='aqua',style="filled" )
    g.node('Genus\nPanagrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('059', 'Genus\nPanagrolaimus', label='Broad\nopen chamber')

    g.node('060', 'Stoma',fillcolor='aqua',style="filled" )
    g.edge('060', '061', label='Absent or\nindistinct')
    g.edge('060', '063', label='Distinct')

    g.node('061', 'Lip\nregion',fillcolor='aqua',style="filled" )
    g.edge('061', '062', label='Narrow\ntooth absent')
    g.node('Genus\nTripyla', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('061', 'Genus\nTripyla', label='Broad\nsmall denticle\napparent in stomal area')

    g.node('062', 'Amphid\nAperture',fillcolor='aqua',style="filled" )
    g.node('Genus\nAmphidelus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('062', 'Genus\nAmphidelus', label='Appears as\nlarge slit')
    g.node('Genus\nAlaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('062', 'Genus\nAlaimus', label='Appears as minute pores')

    g.node('063', 'Stoma',fillcolor='aqua',style="filled" )
    g.node('Genus\nCryptonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('063', 'Genus\nCryptonchus', label='Narrow and long')
    g.node('Genus\nBathyonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('063', 'Genus\nBathyonchus', label='Wide and shallow')

    g.node('064', 'Body',fillcolor='aqua',style="filled" )
    g.edge('064', '065', label='Symmetrical ')
    g.node('Genus\nBunonema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('064', 'Genus\nBunonema', label='Asymmetrical\nbearing series of\nprotuberances on side')

    g.node('065', 'Lip\nAppendages',fillcolor='aqua',style="filled" )
    g.edge('065', '066', label='Not elaborate')
    g.edge('065', '068', label='Elaborate')

    g.node('066', 'Lateral\nLip\nAppendages',fillcolor='aqua',style="filled" )
    g.node('Genus\nDiploscapter', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('066', 'Genus\nDiploscapter', label='Thorn-like\ndirected laterally')
    g.edge('066', '067', label='Not thorn-like\nor directed laterally')

    g.node('067', 'Head',fillcolor='aqua',style="filled" )
    g.node('Genus\nMacrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('067', 'Genus\nMacrolaimus', label='Papillae or\nsetae horn-like')
    g.node('Genus\nTeratocephalus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('067', 'Genus\nTeratocephalus', label='Lips flap-like\nand pointed forward')

    g.node('068', 'Lip\nAppendages',fillcolor='aqua',style="filled" )
    g.node('Genus\nAcrobeles', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('068', 'Genus\nAcrobeles', label='Forked and\nelaborately fringed')
    g.node('Genus\nWilsonema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('068', 'Genus\nWilsonema', label='Membranous and wing-like')
    g.node('Genus\nTylocephalus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('068', 'Genus\nTylocephalus', label='Membranous\nand wing-like')

    g.node('069', 'Post-cephalic\nSetae',fillcolor='aqua',style="filled" )
    g.edge('069', '070', label='Absent')
    g.edge('069', '092', label='Distinct')

    g.node('070', 'Stylet',fillcolor='aqua',style="filled" )
    g.edge('070', '071', label='Absent')
    g.edge('070', '091', label='Visible')

    g.node('071', 'Teeth',fillcolor='aqua',style="filled" )
    g.edge('071', '072', label='Absent\nminute\nor indistinct')
    g.edge('071', '085', label='Distinct')

    g.node('072', 'Esophagus',fillcolor='aqua',style="filled" )
    g.edge('072', '073', label='With basal\nexpansions')
    g.edge('072', '082', label='Uniformaly\ncylindrical')

    g.node('073', 'Amphids',fillcolor='aqua',style="filled" )
    g.edge('073', '074', label='Oval\nspiral\nor stirrup-shaped')
    g.edge('073', '080', label='Circular')

    g.node('074', 'Amphids',fillcolor='aqua',style="filled" )
    g.edge('074', '075', label='Spiral ')
    g.edge('074', '079', label='Not Spiral')

    g.node('075', 'Cuticular\nPunctations',fillcolor='aqua',style="filled" )
    g.edge('075', '076', label='Absent')
    g.edge('075', '078', label='Visible')

    g.node('076', 'Esophageal\nBulb',fillcolor='aqua',style="filled" )
    g.edge('076', '077', label='No valves')
    g.node('Genus\nPlectus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('076', 'Genus\nPlectus', label='valvate ')
    g.node('Genus\nAnaplectus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('076', 'Genus\nAnaplectus', label='valvate ')

    g.node('077', 'Esophageal-intestinal\nvalve',fillcolor='aqua',style="filled" )
    g.node('Genus\nParaplectonema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('077', 'Genus\nParaplectonema', label='Elongate ')
    g.node('Genus\nParaphanolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('077', 'Genus\nParaphanolaimus', label='Valve\nshortened')

    g.node('078', 'Labial\nRegion',fillcolor='aqua',style="filled" )
    g.node('Genus\nEuteratocephalus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('078', 'Genus\nEuteratocephalus', label='Flap-like')
    g.node('Genus\nEthmolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('078', 'Genus\nEthmolaimus', label='Lips bluntly\nrounded')

    g.node('079', 'Amphids',fillcolor='aqua',style="filled" )
    g.node('Genus\nGreenenema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('079', 'Genus\nGreenenema', label='Oval')
    g.node('Genus\nChronogaster', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('079', 'Genus\nChronogaster', label='Stirrup-shaped')

    g.node('080', 'Esophageal-intestinal\nvalve',fillcolor='aqua',style="filled" )
    g.edge('080', '081', label='Short')
    g.node('Genus\nDesmolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('080', 'Genus\nDesmolaimus', label='Elongate ')

    g.node('081', 'Excretory\nPore',fillcolor='aqua',style="filled" )
    g.node('Genus\nDomorganus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('081', 'Genus\nDomorganus', label='Visible and\nlarge excretory gland present')
    g.node('Genus\nMonhystera', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('081', 'Genus\nMonhystera', label='Pore indistinct or absent\nGland indistinct or absent')

    g.node('082', 'Stoma',fillcolor='aqua',style="filled" )
    g.node('Genus\nPrismatolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('082', 'Genus\nPrismatolaimus', label='Wide and shallow\nconspicuous\ntail filiform')
    g.edge('082', '083', label='Narrow, elongate, collapsed or inconspicuous')

    g.node('083', 'Gonads',fillcolor='aqua',style="filled" )
    g.node('Genus\nCylindrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('083', 'Genus\nCylindrolaimus', label='Single')
    g.edge('083', '084', label='Paired')

    g.node('084', 'Amphids',fillcolor='aqua',style="filled" )
    g.node('Genus\nTripyla', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('084', 'Genus\nTripyla', label='Inconspicuous')
    g.node('Genus\nAphanolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('084', 'Genus\nAphanolaimus', label='Conspicuous ')

    g.node('085', 'Esophagus ',fillcolor='aqua',style="filled" )
    g.edge('085', '086', label='Ovoid bulb\nTerminal fifth or sixth')
    g.node('Genus\nIronus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('085', 'Genus\nIronus', label='Uniformly cylindrical\nstoma with massive teeth')

    g.node('086', 'Cuticular\nPunctations',fillcolor='aqua',style="filled" )
    g.edge('086', '087', label='Visible')
    g.edge('086', '089', label='Absent')

    g.node('087', 'Amphids',fillcolor='aqua',style="filled" )
    g.edge('087', '088', label='Not Spiral')
    g.node('Genus\nAchromadora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('087', 'Genus\nAchromadora', label='Spiral')

    g.node('088', 'Longitudinal rows of\ncuticular markings',fillcolor='aqua',style="filled" )
    g.node('Genus\nChromadora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('088', 'Genus\nChromadora', label='Conspicous')
    g.node('Genus\nProchromadorella', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('088', 'Genus\nProchromadorella', label='None')

    g.node('089', 'Amphids',fillcolor='aqua',style="filled" )
    g.edge('089', '090', label='Distinct ')
    g.node('Genus\nButlerius', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('089', 'Genus\nButlerius', label='Indistinct ')

    g.node('090', 'Female\nGonad',fillcolor='aqua',style="filled" )
    g.node('Genus\nAnonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('090', 'Genus\nAnonchus', label='Double\namphid hook-shaped')
    g.node('Genus\nMonhystrella', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('090', 'Genus\nMonhystrella', label='Single\namphid circular')

    g.node('091', 'Lip\nregion',fillcolor='aqua',style="filled" )
    g.node('Genus\nAtylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('091', 'Genus\nAtylenchus', label='Annulated\nnot set off')
    g.node('Genus\nEutylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('091', 'Genus\nEutylenchus', label='Smooth\nset off')

    g.node('092', 'Esophagus',fillcolor='aqua',style="filled" )
    g.edge('092', '093', label='With basal\nexpansion')
    g.edge('092', '098', label='Uniformly cylindrical')

    g.node('093', 'Cuticular\npunctation',fillcolor='aqua',style="filled" )
    g.edge('093', '094', label='Visible\namphids not circular')
    g.edge('093', '097', label='Absent\namphids circular')

    g.node('094', 'Ocelli',fillcolor='aqua',style="filled" )
    g.edge('094', '095', label='Eye spots\npresent')
    g.edge('094', '096', label='Absent')

    g.node('095', 'Stoma',fillcolor='aqua',style="filled" )
    g.node('Genus\nChromadorina', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('095', 'Genus\nChromadorina', label='Three equal-sized teeth')
    g.node('Genus\nPunctodora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('095', 'Genus\nPunctodora', label='At least one\nlarge tooth')

    g.node('096', 'Cuticle',fillcolor='aqua',style="filled" )
    g.node('Genus\nHypodontolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('096', 'Genus\nHypodontolaimus', label='Lateral longitudinal\nrows of punctation')
    g.node('Genus\nChromadorita', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('096', 'Genus\nChromadorita', label='Without lateral\ndifferentiations')

    g.node('097', 'Esophageal\nBulb',fillcolor='aqua',style="filled" )
    g.node('Genus\nProdesmodora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('097', 'Genus\nProdesmodora', label='Valvate ')
    g.node('Genus\nOdontolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('097', 'Genus\nOdontolaimus', label='No valves')

    g.node('098', 'Amphid',fillcolor='aqua',style="filled" )
    g.edge('098', '099', label='Anterior\non body')
    g.node('Genus\nBastia', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('098', 'Genus\nBastia', label='Posteroirly\nlocated')

    g.node('099', 'Amphid',fillcolor='aqua',style="filled" )
    g.node('Genus\nParacyatholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('099', 'Genus\nParacyatholaimus', label='Spiral')
    g.edge('099', '100', label='Cup-shaped or obscure')

    g.node('100', 'Stoma',fillcolor='aqua',style="filled" )
    g.node('Genus\nOncholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('100', 'Genus\nOncholaimus', label='Teeth\nmassive')
    g.node('Genus\nTobrilus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('100', 'Genus\nTobrilus', label='Teeth\nsmall')

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
