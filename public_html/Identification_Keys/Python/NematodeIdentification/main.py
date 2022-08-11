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

#page https://nematode.unl.edu/nemakey.htm
#Step 41  b)Male tail with setae points to Oncholaimus
#and
#page https://nematode.unl.edu/key/nemakey_pt4.htm
#Step 100 a)Stomal teeth massive points to Oncholaimus

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

    g.node('002', '002',fillcolor='green',style="filled" )
    g.edge('002','003', xlabel='Stylet\n Visible')
    g.edge('002','038', xlabel='Stylet\n Absent')

    g.node('003', '003',fillcolor='green',style="filled" )
    g.edge('003','004', label='Knobbed')
    g.edge('003','029', label='No Knobs')

    g.node('004', '004',fillcolor='green',style="filled" )
    g.edge('004','005', label='Median\nBulb  Visible')
    g.edge('004','022', label='Median\nBulb  Absent')

    g.node('005', '005',fillcolor='green',style="filled" )
    g.edge('005','006', label='Females Eel-like')
    g.edge('005','021', label='Females Swollen')

    g.node('006', '006', fillcolor='green', style="filled")
    g.edge('006', '007', label='Vulva Mid-body')
    g.edge('006', '014', label='Vulva Lower third')

    g.node('007', '007', fillcolor='green', style="filled")
    g.edge('007', '008', label='Esophagus No\noverlap')
    g.edge('007', '011', label='Esophagus Overlapping\nintestine')


    g.node('008', '008', fillcolor='green', style="filled")
    g.edge('008', '009', label='Stylet < 80 μm')
    g.node('Genus\nDolichodorus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('008', 'Genus\nDolichodorus', label='Stylet > 80 μm')

    g.node('009', '009', fillcolor='green', style="filled")
    g.node('Genus\nTetylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('009', 'Genus\nTetylenchus', label='Tail\nTerminus Pointed')
    g.edge('009', '010', label='Tail\nTerminus Not Pointed')

    g.node('010', '010', fillcolor='green', style="filled")
    g.node('Genus\nPsilenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('010', 'Genus\nPsilenchus', label='Tail terminus\n knobbed')
    g.node('Genus\nTylenchorhynchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('010', 'Genus\nTylenchorhynchus', label='Tail terminus\n never knobbed or pointed')

    g.node('011', '011', fillcolor='green', style="filled")
    g.edge('011', '012', label='Labium Offset')
    g.edge('011', '013', label='Labium Flattened\namalgamated')

    g.node('012', '012', fillcolor='green', style="filled")
    g.node('Genus\nHoplolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('012', 'Genus\nHoplolaimus', label='\nStylet\n massive 40-50 μm')
    g.node('Genus\nBelonolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('012', 'Genus\nBelonolaimus', label='\nStylet\n long thin, > 90 μm\n')

    g.node('013', '013', fillcolor='green', style="filled")
    g.node('Genus\nRadopholus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('013', 'Genus\nRadopholus', label='Body 0.5-1 mm')
    g.node('Genus\nHirschmanniella', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('013', 'Genus\nHirschmanniella', label='Body 2-3 mm')

    g.node('014', '014', fillcolor='green', style="filled")
    g.edge('014', '015', label='Cuticle Annulated')
    g.edge('014', '017', label='Cuticle Smooth')

    g.node('015', '015', fillcolor='green', style="filled")
    g.edge('015', '016', label='Cuticle\nSheath Absent')
    g.node('Genus\nHemicycliophora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('015', 'Genus\nHemicycliophora', label='Cuticle\nSheath Visible')

    g.node('016', '016', fillcolor='green', style="filled")
    g.node('Genus\nCriconema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('016', 'Genus\nCriconema', label='Annules\nSpines or Scales Visible')
    g.node('Genus\nMesocriconema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('016', 'Genus\nMesocriconema', label='Annules\nSpines or Scales Absent')

    g.node('017', '017 ', fillcolor='green', style="filled")
    g.edge('017', '018', label='Body\nDeath Position\n Straight')
    g.node('Genus\nHelicotylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('017', 'Genus\nHelicotylenchus', label='Death Position\n Spiral')

    g.node('018', '018', fillcolor='green', style="filled")
    g.edge('018', '019', label='Median Bulb\nInconspicous')
    g.node('Genus\nAphelenchoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('018', 'Genus\nAphelenchoides', label='Median Bulb\nConspicous')

    g.node('019', '019', fillcolor='green', style="filled")
    g.edge('019', '020', label='Esophagus\nOverlapping\nIntestine')
    g.node('Genus\nTylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('019', 'Genus\nTylenchus', label='Esophagus\nNo\nOverlap')

    g.node('020', '020', fillcolor='green', style="filled")
    g.node('Genus\nDitylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('020', 'Genus\nDitylenchus', label='Median Bulb\nValves Small\nStylet weak')
    g.node('Genus\nPratylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('020', 'Genus\nPratylenchus', label='Median Bulb\nValves and stylet\nwell developed,\nlabium flattened')

    g.node('021', '021', fillcolor='green', style="filled")
    g.node('Genus\nMeloidogyne', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('021', 'Genus\nMeloidogyne', label='Female Body\nWhite\nwithout eggs')
    g.node('Genus\nHeterodera', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('021', 'Genus\nHeterodera', label='Female Body\nBrown\nwith eggs')

    g.node('022', '022', fillcolor='green', style="filled")
    g.edge('022', '023', label='Stylet\n< 100 μm')
    g.node('Genus\nXiphinema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('022', 'Genus\nXiphinema', label='Stylet\n> 100 μm')

    g.node('023', '023', fillcolor='green', style="filled")
    g.edge('023', '024', label='Stylet\nComplex')
    g.edge('023', '025', label='Stylet\nSimple')

    g.node('024', '024', fillcolor='green', style="filled")
    g.node('Genus\nDiphtherophora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('024', 'Genus\nDiphtherophora', label='Stylet\nAnterior\narch-like')
    g.node('Genus\nTylencholaimellus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('024', 'Genus\nTylencholaimellus', label='Stylet\nDorsal\nthickening')

    g.node('025', '025', fillcolor='green', style="filled")
    g.edge('025', '026', label='Stylet Knobs\nElongate\nflange-like')
    g.edge('025', '027', label='Stylet Knobs\nRound')

    g.node('026', '026', fillcolor='green', style="filled")
    g.node('Genus\nAulolaimoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('026', 'Genus\nAulolaimoides', label='Tail\nFiliform')
    g.node('Genus\nEnchodelus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('026', 'Genus\nEnchodelus', label='Tail\nRound')

    g.node('027', '027', fillcolor='green', style="filled")
    g.edge('027', '028', label='Tail Round')
    g.node('Genus\nNothotylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('027', 'Genus\nNothotylenchus', label='Tail Pointed')

    g.node('028', '028', fillcolor='green', style="filled")
    g.node('Genus\nTylencholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('028', 'Genus\nTylencholaimus', label='Basal\npart Esophagus\nelongate')
    g.node('Genus\nDoryllium', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('028', 'Genus\nDoryllium', label='Basal\npart Esophagus\noval')

    g.node('029', '029',fillcolor='green',style="filled" )
    g.edge('029', '030', label='Valvate median\nesophageal bulb Absent')
    g.edge('029', '037', label='Valvate median\nesophageal bulb Visible')

    g.node('030', '030',fillcolor='green',style="filled" )
    g.edge('030', '031', label='Stomal\nwalls Not cuticularized')

    g.node('Genus\nActinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nActinolaimus', label='Stomal\nwalls Cuticularized')
    g.node('Genus\nMetactinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nMetactinolaimus', label='Stomal\nwalls Cuticularized')
    g.node('Genus\nNeoactinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nNeoactinolaimus', label='Stomal\nwalls Cuticularized')
    g.node('Genus\nParactinolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nParactinolaimus', label='Stomal\nwalls Cuticularized')
    g.node('Genus\nActinolaimoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('030', 'Genus\nActinolaimoides', label='Stomal\nwalls Cuticularized')

    g.node('031', '031',fillcolor='green',style="filled" )
    g.edge('031', '032', label='Esophagus with Basal\nexpansions')
    g.node('Genus\nOionchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('031', 'Genus\nOionchus', label='Esophagus Expanding\nuniformly')

    g.node('032', '032',fillcolor='green',style="filled" )
    g.edge('032', '033', label='Terminal fifth\n or sixth of esophagus\n an ovoid bulb')
    g.edge('032', '036', label='Posterior third\n of esophagus swollen')

    g.node('033', '033',fillcolor='green',style="filled" )
    g.edge('033', '034', label='Stylet\nAxial Positioned centrally')
    g.node('Genus\nCampydora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('033', 'Genus\nCampydora', label='Stylet\nAxial Not axial\norginating from tooth\nin stoma wall')

    g.node('034', '034',fillcolor='green',style="filled" )
    g.edge('034', '035', label='Gonads Paired\nvulva about 50%')
    g.node('Genus\nTyleptus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('034', 'Genus\nTyleptus', label='Gonads Single\nvulva > 50%')

    g.node('035', '035',fillcolor='green',style="filled" )
    g.node('Genus\nLeptonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('035', 'Genus\nLeptonchus', label='Stylet Slender')
    g.node('Genus\nDorylaimoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('035', 'Genus\nDorylaimoides', label='Stylet Thick')

    g.node('036', 'Stylet\nAxial',fillcolor='green',style="filled" )
    g.node('Genus\nDorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nDorylaimus', label=' Stylet axial,\n positioned centrally')
    g.node('Genus\nEudorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nEudorylaimus', label=' Stylet axial,\n positioned centrally')
    g.node('Genus\nLabronema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nLabronema', label='Central')
    g.node('Genus\nMesodorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nMesodorylaimus', label=' Stylet axial,\n positioned centrally')
    g.node('Genus\nThornia', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nThornia', label='Central')
    g.node('Genus\nLaimydorus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nLaimydorus', label=' Stylet axial,\n positioned centrally')
    g.node('Genus\nProdorylaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nProdorylaimus', label='Central')
    g.node('Genus\nDorylaiminae', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nDorylaiminae', label=' Stylet axial,\n positioned centrally')
    g.node('Genus\nNygolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('036', 'Genus\nNygolaimus', label='Stylet not axial,\n originating from\n tooth in stoma wall ')

    g.node('037', '037',fillcolor='green',style="filled" )
    g.node('Genus\nSeinura', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('037', 'Genus\nSeinura', label='Tail Pointed ')
    g.node('Genus\nAphelenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('037', 'Genus\nAphelenchus', label='Tail Rounded')

    g.node('038', '038',fillcolor='green',style="filled" )
    g.edge('038', '039', label='Teeth Visible')
    g.edge('038', '050', label='Teeth Absent/minute/indistinct')

    g.node('039', '039',fillcolor='green',style="filled" )
    g.edge('039', '040', label='Esophagus without mid-region\nexpansion')
    g.edge('039', '049', label='Esophagus Expanded\nat mid-region')

    g.node('040', '040',fillcolor='green',style="filled" )
    g.edge('040', '041', label='Tail Pointed\nor tapering')
    g.edge('040', '047', label='Tail Rounded')

    g.node('041', '041',fillcolor='green',style="filled" )
    g.edge('041', '042', label='Male tail\n without setae')
    g.node('Genus\nOncholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('041', 'Genus\nOncholaimus', label='Male tail\n with setae')

    g.node('042', '042 ',fillcolor='green',style="filled" )
    g.edge('042', '043', label='Stoma with Denticles')
    g.edge('042', '045', label='Stoma without Denticles')

    g.node('043', '043',fillcolor='green',style="filled" )
    g.edge('043', '044', label='Denticles Scattered\nor in longitudinal rows')
    g.node('Genus\nMylonchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('043', 'Genus\nMylonchulus', label='Denticles In\ntransverse rows')

    g.node('044', '044',fillcolor='green',style="filled" )
    g.node('Genus\nPrionchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('044', 'Genus\nPrionchulus', label='Denticles On longitudinal\nrib of stoma')
    g.node('Genus\nSporonchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('044', 'Genus\nSporonchulus', label='Denticles Scattered\non stoma wall ')

    g.node('045', '045',fillcolor='green',style="filled" )
    g.edge('045', '046', label='Tooth anteriorly directed')
    g.node('Genus\nAnatonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('045', 'Genus\nAnatonchus', label='Tooth retrorse')

    g.node('046', '046',fillcolor='green',style="filled" )
    g.node('Genus\nIotonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('046', 'Genus\nIotonchus', label='Tooth in basal\n part of stoma')
    g.node('Genus\nMononchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('046', 'Genus\nMononchus', label='Tooth in anterior\n part of stoma')

    g.node('047', '047',fillcolor='green',style="filled" )
    g.edge('047', '048', label='Stoma With prominent medial\nor apical tooth')
    g.node('Genus\nBathyodontus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('047', 'Genus\nBathyodontus', label='Stoma With small\nbasal tooth')

    g.node('048', '048',fillcolor='green',style="filled" )
    g.node('Genus\nEnoplocheilus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('048', 'Genus\nEnoplocheilus', label='Stoma With 3 teeth\nwithout small basal tooth\ncaudal glands terminal')
    g.node('Genus\nMononchulus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('048', 'Genus\nMononchulus', label='Stoma With large anterior\n& small basal tooth\ncaudal glands ventral')

    g.node('049', '049',fillcolor='green',style="filled" )
    g.node('Genus\nMononchoides', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('049', 'Genus\nMononchoides', label='Lip region with\n rib-like armature')
    g.node('Genus\nDiplogaster', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('049', 'Genus\nDiplogaster', label='Lip region without rib-like armature')

    g.node('050', '050',fillcolor='green',style="filled" )
    g.edge('050', '051', label='Esophagus With basal\nexpansions')
    g.edge('050', '060', label='Esophagus Uniformly\ncylindrical')

    g.node('051', '051',fillcolor='green',style="filled" )
    g.edge('051', '052', label='Esophagus Without\nmid-region expansion')
    g.edge('051', '055', label='Esophagus Expanded\nat mid-region')

    g.node('052', '052',fillcolor='green',style="filled" )
    g.edge('052', '053', label='Amphids Distinct')
    g.edge('052', '054', label='Amphids Indistinct')

    g.node('053', '053',fillcolor='green',style="filled" )
    g.node('Genus\nMicrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('053', 'Genus\nMicrolaimus', label='Stoma\nWalls Anteriorly inflated\nwith minute tooth')
    g.node('Genus\nLeptolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('053', 'Genus\nLeptolaimus', label='Stoma\nWalls Without tooth and\nwith straight,\ntapering sides')

    g.node('054', '054',fillcolor='green',style="filled" )
    g.node('Genus\nRhabdolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('054', 'Genus\nRhabdolaimus', label='Stoma\nRod-Like\n Thickenings')
    g.node('Genus\nMonochromadora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('054', 'Genus\nMonochromadora', label='Stoma without\n rod-like thickenings')

    g.node('055', '055',fillcolor='green',style="filled" )
    g.edge('055', '056', label='Gonads Paired')
    g.edge('055', '058', label='Gonads Single')

    g.node('056', '056',fillcolor='green',style="filled" )
    g.edge('056', '057', label='Stoma\nwalls Straight\namalgamated')
    g.node('Genus\nAlloionema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('056', 'Genus\nAlloionema', label='Stoma\nwalls Separated,\nnot straight')

    g.node('057', '057',fillcolor='green',style="filled" )
    g.node('Genus\nRhabditis', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('057', 'Genus\nRhabditis', label='Metacorpus Moderately swollen\nstoma not\nexcessively elongate')
    g.node('Genus\nCylindrocorpus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('057', 'Genus\nCylindrocorpus', label='Metacorpus Elongate\ncyclindrical metacorpus\nstoma elongate')

    g.node('058', '058',fillcolor='green',style="filled" )
    g.edge('058', '059', label='Tail with Sharp\nterminus')
    g.node('Genus\nCephalobus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('058', 'Genus\nCephalobus', label='Tail Bluntly conical')

    g.node('059', '059',fillcolor='green',style="filled" )
    g.node('Genus\nPanagrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('059', 'Genus\nPanagrolaimus', label='Anterior part\n of stoma a broad,\n open chamber')

    g.node('060', '060',fillcolor='green',style="filled" )
    g.edge('060', '061', label='Stoma Absent or\nindistinct')
    g.edge('060', '063', label='Stoma Distinct')

    g.node('061', '061',fillcolor='green',style="filled" )
    g.edge('061', '062', label=' Lip region narrow,\n tooth absent')
    g.node('Genus\nTripyla', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('061', 'Genus\nTripyla', label='Lip region broad,\n small denticle\n apparent in stomal area')

    g.node('062', '062',fillcolor='green',style="filled" )
    g.node('Genus\nAmphidelus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('062', 'Genus\nAmphidelus', label='Amphid aperture\n appearing as large slit')
    g.node('Genus\nAlaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('062', 'Genus\nAlaimus', label='Appears aperture  as minute pores')

    g.node('063', '063',fillcolor='green',style="filled" )
    g.node('Genus\nCryptonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('063', 'Genus\nCryptonchus', label='Stoma \n Narrow and long')
    g.node('Genus\nBathyonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('063', 'Genus\nBathyonchus', label='Stoma \n Wide and shallow')

    g.node('064', '064',fillcolor='green',style="filled" )
    g.edge('064', '065', label= 'Body Symmetrical ')
    g.node('Genus\nBunonema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('064', 'Genus\nBunonema', label='Asymmetrical\nbearing series of\nprotuberances on side')

    g.node('065', '065',fillcolor='green',style="filled" )
    g.edge('065', '066', label='Lip Appendages \n Not elaborate')
    g.edge('065', '068', label='Lip Appendages \n Elaborate')

    g.node('066', '066',fillcolor='green',style="filled" )
    g.node('Genus\nDiploscapter', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('066', 'Genus\nDiploscapter', label='Lateral\nLip\nAppendages Thorn-like\ndirected laterally')
    g.edge('066', '067', label='Lateral\nLip\nAppendages Not thorn-like\nor directed laterally')

    g.node('067', '067',fillcolor='green',style="filled" )
    g.node('Genus\nMacrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('067', 'Genus\nMacrolaimus', label='Papillae or\nsetae horn-like')
    g.node('Genus\nTeratocephalus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('067', 'Genus\nTeratocephalus', label='Lips flap-like\nand pointed forward')

    g.node('068', '068',fillcolor='green',style="filled" )
    g.node('Genus\nAcrobeles', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('068', 'Genus\nAcrobeles', label='Lip\nAppendages Forked and\nelaborately fringed')
    g.node('Genus\nWilsonema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('068', 'Genus\nWilsonema', label='Lip\nAppendages Membranous and wing-like')
    g.node('Genus\nTylocephalus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('068', 'Genus\nTylocephalus', label='Lip\nAppendages Membranous\nand wing-like')

    g.node('069', '069',fillcolor='green',style="filled" )
    g.edge('069', '070', label='Post-cephalic\nSetae Absent')
    g.edge('069', '092', label='Post-cephalic\nSetae Distinct')

    g.node('070', '070',fillcolor='green',style="filled" )
    g.edge('070', '071', label='Stylet Absent')
    g.edge('070', '091', label='Stylet Visible')

    g.node('071', '071',fillcolor='green',style="filled" )
    g.edge('071', '072', label='Teeth Absent\nminute\nor indistinct')
    g.edge('071', '085', label='Teeth Distinct')

    g.node('072', '072',fillcolor='green',style="filled" )
    g.edge('072', '073', label='Esophagus With basal\nexpansions')
    g.edge('072', '082', label='Esophagus Uniformaly\ncylindrical')

    g.node('073', '073',fillcolor='green',style="filled" )
    g.edge('073', '074', label='Amphids Oval\nspiral\nor stirrup-shaped')
    g.edge('073', '080', label='Amphids Circular')

    g.node('074', '074',fillcolor='green',style="filled" )
    g.edge('074', '075', label='Amphids Spiral ')
    g.edge('074', '079', label='Amphids Not Spiral')

    g.node('075', '075',fillcolor='green',style="filled" )
    g.edge('075', '076', label='Cuticular\nPunctations Absent')
    g.edge('075', '078', label='Cuticular\nPunctations Visible')

    g.node('076', '076',fillcolor='green',style="filled" )
    g.edge('076', '077', label='Esophageal bulb without valves')
    g.node('Genus\nPlectus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('076', 'Genus\nPlectus', label='Esophageal\nBulb valvate ')
    g.node('Genus\nAnaplectus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('076', 'Genus\nAnaplectus', label='Esophageal\nBulb valvate ')

    g.node('077', '077',fillcolor='green',style="filled" )
    g.node('Genus\nParaplectonema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('077', 'Genus\nParaplectonema', label='Esophageal-intestinal\nvalve Elongate ')
    g.node('Genus\nParaphanolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('077', 'Genus\nParaphanolaimus', label='Esophageal-intestinal\nvalve Valve\nshortened')

    g.node('078', '078',fillcolor='green',style="filled" )
    g.node('Genus\nEuteratocephalus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('078', 'Genus\nEuteratocephalus', label='Labial\nRegion Flap-like')
    g.node('Genus\nEthmolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('078', 'Genus\nEthmolaimus', label='Labial\nRegion Lips bluntly\nrounded')

    g.node('079', '079',fillcolor='green',style="filled" )
    g.node('Genus\nGreenenema', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('079', 'Genus\nGreenenema', label='Amphids Oval')
    g.node('Genus\nChronogaster', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('079', 'Genus\nChronogaster', label='Amphids Stirrup-shaped')

    g.node('080', '080',fillcolor='green',style="filled" )
    g.edge('080', '081', label='Esophageal-intestinal\nvalve Short')
    g.node('Genus\nDesmolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('080', 'Genus\nDesmolaimus', label='Esophageal-intestinal\nvalve Elongate ')

    g.node('081', '081',fillcolor='green',style="filled" )
    g.node('Genus\nDomorganus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('081', 'Genus\nDomorganus', label='Excretory\nPore Visible and\nlarge excretory gland present')
    g.node('Genus\nMonhystera', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('081', 'Genus\nMonhystera', label='Excretory\nPore indistinct or absent\nGland indistinct or absent')

    g.node('082', '082',fillcolor='green',style="filled" )
    g.node('Genus\nPrismatolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('082', 'Genus\nPrismatolaimus', label='Stoma Wide and shallow\nconspicuous\ntail filiform')
    g.edge('082', '083', label='Stoma Narrow, elongate, collapsed or inconspicuous')

    g.node('083', '083',fillcolor='green',style="filled" )
    g.node('Genus\nCylindrolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('083', 'Genus\nCylindrolaimus', label='Gonads Single')
    g.edge('083', '084', label='Gonads Paired')

    g.node('084', '084',fillcolor='green',style="filled" )
    g.node('Genus\nTripyla', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('084', 'Genus\nTripyla', label='Amphids Inconspicuous')
    g.node('Genus\nAphanolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('084', 'Genus\nAphanolaimus', label='Amphids Conspicuous ')

    g.node('085', '085',fillcolor='green',style="filled" )
    g.edge('085', '086', label='Esophagus Ovoid bulb\nTerminal fifth or sixth')
    g.node('Genus\nIronus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('085', 'Genus\nIronus', label='Esophagus Uniformly cylindrical\nstoma with massive teeth')

    g.node('086', '086',fillcolor='green',style="filled" )
    g.edge('086', '087', label='Cuticular\nPunctations Visible')
    g.edge('086', '089', label='Cuticular\nPunctations Absent')

    g.node('087', '087',fillcolor='green',style="filled" )
    g.edge('087', '088', label='Amphids Not Spiral')
    g.node('Genus\nAchromadora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('087', 'Genus\nAchromadora', label='Amphids Spiral')

    g.node('088', '088',fillcolor='green',style="filled" )
    g.node('Genus\nChromadora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('088', 'Genus\nChromadora', label='Longitudinal rows of\ncuticular markings Conspicous')
    g.node('Genus\nProchromadorella', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('088', 'Genus\nProchromadorella', label='No longitudinal rows of cuticular markings present ')

    g.node('089', '089',fillcolor='green',style="filled" )
    g.edge('089', '090', label='Amphids Distinct ')
    g.node('Genus\nButlerius', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('089', 'Genus\nButlerius', label='Amphids Indistinct ')

    g.node('090', '090',fillcolor='green',style="filled" )
    g.node('Genus\nAnonchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('090', 'Genus\nAnonchus', label='Female\nGonad Double\namphid hook-shaped')
    g.node('Genus\nMonhystrella', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('090', 'Genus\nMonhystrella', label='Female\nGonad Single\namphid circular')

    g.node('091', '091',fillcolor='green',style="filled" )
    g.node('Genus\nAtylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('091', 'Genus\nAtylenchus', label='Lip\nregion Annulated\nnot set off')
    g.node('Genus\nEutylenchus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('091', 'Genus\nEutylenchus', label='Lip\nregion Smooth\nset off')

    g.node('092', '092',fillcolor='green',style="filled" )
    g.edge('092', '093', label='Esophagus With basal\nexpansion')
    g.edge('092', '098', label='Esophagus Uniformly cylindrical')

    g.node('093', '093',fillcolor='green',style="filled" )
    g.edge('093', '094', label='Cuticular\npunctation Visible\namphids not circular')
    g.edge('093', '097', label='Cuticular\npunctation Absent\namphids circular')

    g.node('094', '094',fillcolor='green',style="filled" )
    g.edge('094', '095', label='Ocelli Eye spots\npresent')
    g.edge('094', '096', label='Ocelli Absent')

    g.node('095', '095',fillcolor='green',style="filled" )
    g.node('Genus\nChromadorina', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('095', 'Genus\nChromadorina', label='Stoma with Three equal-sized teeth')
    g.node('Genus\nPunctodora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('095', 'Genus\nPunctodora', label='Stoma with At least one\nlarge tooth')

    g.node('096', '096',fillcolor='green',style="filled" )
    g.node('Genus\nHypodontolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('096', 'Genus\nHypodontolaimus', label='Cuticle Lateral longitudinal\nrows of punctation')
    g.node('Genus\nChromadorita', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('096', 'Genus\nChromadorita', label='Cuticle Without lateral\ndifferentiations')

    g.node('097', '097',fillcolor='green',style="filled" )
    g.node('Genus\nProdesmodora', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('097', 'Genus\nProdesmodora', label='Esophageal\nBulb Valvate ')
    g.node('Genus\nOdontolaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('097', 'Genus\nOdontolaimus', label='Esophageal\nBulb No valves')

    g.node('098', '098',fillcolor='green',style="filled" )
    g.edge('098', '099', label='Amphid Anterior\non body')
    g.node('Genus\nBastia', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('098', 'Genus\nBastia', label='Amphid Posteroirly\nlocated')

    g.node('099', '099',fillcolor='green',style="filled" )
    g.node('Genus\nParacyatholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('099', 'Genus\nParacyatholaimus', label='Amphid Spiral')
    g.edge('099', '100', label='Amphid Cup-shaped or obscure')

    g.node('100', '100',fillcolor='green',style="filled" )
    g.node('Genus\nOncholaimus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('100', 'Genus\nOncholaimus', label='Stoma Teeth\nmassive')
    g.node('Genus\nTobrilus', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.edge('100', 'Genus\nTobrilus', label='Stoma Teeth\nsmall')

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
