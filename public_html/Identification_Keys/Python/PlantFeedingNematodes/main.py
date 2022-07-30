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
    #http://nemaplex.ucdavis.edu/Plntpara/KeyGenPltFdrsn.htm

    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6'))
    g.graph_attr['rankdir'] = 'LR'

    GraphTitle = 'Key to Genera of \nPlant-feeding Nematodes'
    g.node('000', label=GraphTitle,fillcolor='red',style="filled")
    g.edge('000', '001', label2(''))

    g.node('001', '001',fillcolor='aqua',style="filled" )
    g.edge('001','Go to alternate key\n nemaplex.ucdavis.edu/Taxadata/Famkey.htm ', label2('Stylet absent'))
    g.edge('001','002', label2('Stylet/spear present'))

    g.node('002', '002',fillcolor='aqua',style="filled" )
    g.edge('002','003', label2('Order Dorylaimida 2-part esophagus, anterior slender, posterior glandular and muscular, spear, no metacorpus with valve'))
    g.edge('002','007', label2('Sub-Order Tylenchina 3-part esophagus, metacorpus with valve, slender isthmus, glandular postcorpus, stylet usually with knobs'))

    g.node('003', '003',fillcolor='aqua',style="filled" )
    g.edge('003','004', label2('Trichodoridae Spear short and curved, body thick, anus almost terminal'))
    g.edge('003','005', label2('Longidoridae Spear long with long extension, body long and slender'))
    g.edge('003','Not a plant feeder\nGo to alternate key', label2('Spear short and straight'))

    g.node('004', '004',fillcolor='aqua',style="filled" )
    g.edge('004','Trichodorus', label2('Diovarial females, males without caudal alae'))
    g.edge('004','Paratrichodorus', label2('Diovarial females, males with caudal alae'))
    g.edge('004','Monotrichodorus', label2('Monovarial females, males without caudal alae'))
    g.edge('004','Allotrichodorus', label2('Monovarial females, males without caudal alae'))

    g.node('005', '005',fillcolor='aqua',style="filled" )
    g.edge('005','Xiphinema', label2('Spear extension with basal flanges, guiding ring near base of spear'))
    g.edge('005','006', label2('Spear extension without basal flanges, guiding ring near tip of spear'))

    g.node('006', '006',fillcolor='aqua',style="filled" )
    g.edge('006','Longidorus', label2('Amphid openings small and slit-like'))
    g.edge('006','Paralongidorus', label2('Amphid openings wide, posterior to lips'))

    g.node('007', '007',fillcolor='aqua',style="filled" )
    g.edge('007','008', label2('Superfamily Aphelenchoidea DEGO in metacorpus and difficult to see; metacorpus usually nearly as large as body diameter'))
    g.edge('007','010', label2('Superfamily Criconematoidea or Tylenchoidea DEGO in procorpus; metacorpus usually less that 75% of body width'))

    g.node('008', '008',fillcolor='aqua',style="filled" )
    g.edge('008','Bursaphelenchus', label2('Vulva with overlapping flap, vagina curved, male with small bursa at tail tip'))
    g.edge('008','009', label2('Vulva without flap, vagina not curved'))

    g.node('009', '009',fillcolor='aqua',style="filled" )
    g.edge('009','Aphelenchus', label2('Female tail bluntly rounded, lateral field with 6-15 lines, male with bursa and gubernaculum'))
    g.edge('009','Aphelenchoides', label2('Female tail usually conoid and mucronate, lateral field with 3-5 lines, male without bursa or gubernaculum'))

    g.node('010', '010',fillcolor='aqua',style="filled" )
    g.edge('010','074', label2('Head with setae, no plant feeders'))
    g.edge('010','011', label2('Head without setae, mainly plant feeders'))

    g.node('011', '011',fillcolor='aqua',style="filled" )
    g.edge('011','Nothanguina,\nNothotylenchus', label2('Metacorpus absent or reduced, no valve.'))
    g.edge('011','012', label2('Metacorpus with valve'))

    g.node('012', '012',fillcolor='aqua',style="filled" )
    g.edge('012','013', label2('Mature females greatly enlarged (pear-shaped, kidney-shaped), embedded or attached to plant roots, or free in soil as cysts'))
    g.edge('012','024', label2('Mature females vermiform, slender to slightly swollen'))

    g.node('013', '013',fillcolor='aqua',style="filled" )
    g.edge('013','014', label2('Mature female body elongate-saccate or kidney shape and not hardened into a cyst'))
    g.edge('013','019', label2('Mature female body pear-, lemon-shaped or spherical, may be hardened into a cyst'))

    g.node('014', '014',fillcolor='aqua',style="filled" )
    g.edge('014','Rotylenchulus', label2('Female diovarial'))
    g.edge('014','015', label2('Female monovarial'))

    g.node('015', '015',fillcolor='aqua',style="filled" )
    g.edge('015','016', label2('Excretory pore in esophageal region, near nerve ring'))
    g.edge('015','017', label2('Excretory pore posterior to nerve ring'))

    g.node('016', '016',fillcolor='aqua',style="filled" )
    g.edge('016','Sphaeronema', label2('Mature female subspherical, may have a protruding vulva, cuticle marked with coarse reticulate pattern'))
    g.edge('016','Trophonema', label2('Mature female a thick spiral, without protruding vulva'))

    g.node('017', '017',fillcolor='aqua',style="filled" )
    g.edge('017','Trophotylenchulus', label2('Lip region elevated in females and juveniles'))
    g.edge('017','018', label2('Lip region not elevated, continuous with body contour'))

    g.node('018', '018',fillcolor='aqua',style="filled" )
    g.edge('018','Tylenchulus', label2('Excretory pore in posterior third of body, near vulva'))
    g.edge('018','Nacobbus', label2('Excretory pore near basal region of esophagus'))

    g.node('019', '019',fillcolor='aqua',style="filled" )
    g.edge('019','Meloidogyne', label2('Females with perineal pattern, excretory pore close to level of stylet, lip region with 2 lateral lips and 4 smaller sublateral lips, weak head frame, J2 stylet < 20 µm, host roots usually galled'))
    g.edge('019','020', label2('Females without perineal pattern, excretory pore posterior to metacorpus, lip region with 2 lateral lips smaller than 4 sublateral lips, J2 stylet > 20 µm, host roots not galled'))

    g.node('020', '020',fillcolor='aqua',style="filled" )
    g.edge('020','021', label2('V > 50% but well anterior to anus, cuticle striated'))
    g.edge('020','Cryphodera', label2('Vulva terminal or subterminal, cuticle striated or lace-patterned'))

    g.node('021', '021',fillcolor='aqua',style="filled" )
    g.edge('021','Cryphodera', label2('Cuticle striated'))
    g.edge('021','022', label2('Cuticle lace-patterned'))

    g.node('022', '022',fillcolor='aqua',style="filled" )
    g.edge('022','023', label2('Female body hardens to cyst, vulva terminal or on a terminal vulval cone, anus dorsal to vulva'))
    g.edge('022','Atalodera', label2('Female body does not harden to cyst, vulva and anus on terminal prominence'))
    g.edge('022','Sarisodera', label2('Female body does not harden to cyst, vulva sunken into terminal vulval cone with anus on upper side of dorsal vulva lip, J2 stylet >38 µm'))

    g.node('023', '023',fillcolor='aqua',style="filled" )
    g.edge('023','Heterodera', label2('Cysts generally lemon-shaped, vulva on terminal vulval cone with fenestration, bullae present or absent, J2 stylet <30 µm'))
    g.edge('023','Globodera', label2('Cyst spherical or subspherical, bullae absent, J2 with 5 lines in lateral field'))

    g.node('024', '024',fillcolor='aqua',style="filled" )
    g.edge('024','025', label="c' ≥ 6, filiform with pointed or clavate terminus")
    g.edge('024','029', label="c' generally < 6, but if longer it is cylindroid rather than filiform")

    g.node('025', '025',fillcolor='aqua',style="filled" )
    g.edge('025','026', label2('Female diovarial'))
    g.edge('025','027', label2('Female monovarial'))

    g.node('026', '026',fillcolor='aqua',style="filled" )
    g.edge('026','070', label2('Stylet without knobs, no cephalic sclerotization, tail filiform, usually with clavate terminus'))
    g.edge('026','Brachydorus', label2('Stylet with knobs, heavy cephalic sclerotization, tail filiform with pointed terminus'))

    g.node('027', '027',fillcolor='aqua',style="filled" )
    g.edge('027','Caloosia', label2('Esophagus criconematoid with swollen procorpus continuous with metacorpus, cuticle thick and coarsely striated'))
    g.edge('027','028', label2('Esophagus tylenchoid, procorpus not swollen,, cuticle thin, not coarsely striated'))

    g.node('028', '028',fillcolor='aqua',style="filled" )
    g.edge('028','067', label2('Esophagus terminating in a bulb that abuts the intestine; non-overlapping'))
    g.edge('028','029', label2('Esophageal postcorpus glandular region slightly to distinctly overlapping intestine'))

    g.node('029', '029',fillcolor='aqua',style="filled" )
    g.edge('029','030', label2('Monovarial, vulva in posterior third of body'))
    g.edge('029','Trophurus', label2('Monovarial, V near 50%, lip region conical and not striated, female tail tip rounded, cuticle of tail swollen'))
    g.edge('029','045', label2('Diovarial, V near 50%'))

    g.node('030', '030',fillcolor='aqua',style="filled" )
    g.edge('030','031', label2('Procorpus not swollen and combined into metacorpus or, if swollen, offset from metacorpus by a constriction'))
    g.edge('030','038', label2('Superfamily Criconematoidea Procorpus not swollen and combined into metacorpus or, if swollen, offset from metacorpus by a constriction'))

    g.node('031', '031',fillcolor='aqua',style="filled" )
    g.edge('031','032', label2('Stylet delicate, ≤ 15 µm, tail acute or subacute'))
    g.edge('031','034', label2('Stylet strong, >15 µm, tail tapering or bluntly rounded'))

    g.node('032', '032',fillcolor='aqua',style="filled" )
    g.edge('032','033', label2('Ovary with oocytes in one or two rows, not arranged around central rachis, mature female slender to stout'))
    g.edge('032','Anguina', label2('Ovary with multiple rows of oocytes arranged around central rachis, mature female usually obese, in seed, leaf or flower galls'))

    g.node('033', '033',fillcolor='aqua',style="filled" )
    g.edge('033','Subanguina', label2('Ovary with one or two flexures, female moderately stout, in root galls of Graminae'))
    g.edge('033','Ditylenchus', label2('Ovary outstretched, female slender, in bulbs, stems, leaves, tubers'))

    g.node('034', '034',fillcolor='aqua',style="filled" )
    g.edge('034','Rotylenchoides', label="s ≥1.5, c' generally ≤1.5")
    g.edge('034','035', label="s<1.5, c' >1.5")

    g.node('035', '035',fillcolor='aqua',style="filled" )
    g.edge('035','Pratylenchus', label2('Esophagus overlaps intestine ventrally'))
    g.edge('035','036', label2('Esophagus overlaps intestine dorsally'))

    g.node('036', '036',fillcolor='aqua',style="filled" )
    g.edge('036','Radopholoides', label2('Lip region low, generally rounded, stylet knobs flattened anteriorly, sexual dimorphism'))
    g.edge('036','037', label2('Lip region high, conoid, stylet knobs sloping anteriorly or indented, males present or absent'))

    g.node('037', '037',fillcolor='aqua',style="filled" )
    g.edge('037','Acontylus', label2('Female body swollen, stylet knobs sloping anteriorly, sexual dimorphism'))
    g.edge('037','Hoplotylus', label2('Female body slender, stylet knobs tapering anteriorly to a dentate tip, males absent'))

    g.node('038', '038',fillcolor='aqua',style="filled" )
    g.edge('038','039', label2('Mature female without extra cuticle or sheath'))
    g.edge('038','041', label2('Mature female with extra cuticle or sheath'))

    g.node('039', '039',fillcolor='aqua',style="filled" )
    g.edge('039','040', label2('Cuticle with prominent retrorse striations'))
    g.edge('039','042', label2('Cuticle without prominent retrorse striations'))

    g.node('040', '040',fillcolor='aqua',style="filled" )
    g.edge('040','Criconema', label2('Cuticular striations of female with spines, scales, plates or stalks on posterior margins'))
    g.edge('040','Criconemoides', label2('Cuticular striations of female with smooth or crenate posterior margins'))

    g.node('041', '041',fillcolor='aqua',style="filled" )
    g.edge('041','Hemicriconemoides', label2('Stylet knobs rounded, sloping anteriorly, usually <200 striations on cuticle'))
    g.edge('041','Hemicycliophora', label2('Stylet knobs anchor-shaped, usually >200 striations on cuticle'))

    g.node('042', '042',fillcolor='aqua',style="filled" )
    g.edge('042','Bakernema', label2('Cuticular striations of female with membranous structures on posterior margins'))
    g.edge('042','043', label2('Cuticular striations of female without membranous structures on posterior margins'))

    g.node('043', '043',fillcolor='aqua',style="filled" )
    g.edge('043','Cacopaurus', label2('Cuticle of female with minute tubercles'))
    g.edge('043','044', label2('Cuticle of female without minute tubercles'))

    g.node('044', '044',fillcolor='aqua',style="filled" )
    g.edge('044','Paratylenchus', label2('Female stylet ≤36 µm'))
    g.edge('044','Gracilacus', label2('Female stylet 45-120 µm'))

    g.node('045', '045',fillcolor='aqua',style="filled" )
    g.edge('045','046', label2('s ≥2.5'))
    g.edge('045','050', label2('s generally <2.5'))

    g.node('046', '046',fillcolor='aqua',style="filled" )
    g.edge('046','047', label2('Esophageal glands not enclosed in a bulb, usually unequal in length, overlapping intestine'))
    g.edge('046','048', label2('Esophageal glands enclosed in a bulb, usually butting intestine'))

    g.node('047', '047',fillcolor='aqua',style="filled" )
    g.edge('047','Belonolaimus', label2('Average adult body length ≥ 1.75mm'))
    g.edge('047','049', label2('Average adult body length <1.75mm'))

    g.node('048', '048',fillcolor='aqua',style="filled" )
    g.edge('048','Macrotrophurus', label2('Lip region continuous with body contour'))
    g.edge('048','Dolichodorus', label2('Lip region offset from body contour by a constriction'))

    g.node('049', '049',fillcolor='aqua',style="filled" )
    g.edge('049','Morulaimus', label2('Lateral field with 5 lines'))
    g.edge('049','Carphodorus', label2('Lateral field with 3 lines'))

    g.node('050', '050',fillcolor='aqua',style="filled" )
    g.edge('050','Aphasmatylenchus', label2('Phasmids absent'))
    g.edge('050','051', label2('Phasmids present'))

    g.node('051', '051',fillcolor='aqua',style="filled" )
    g.edge('051','062', label="c'<1.5")
    g.edge('051','052', label="c'≥1.5")

    g.node('052', '052',fillcolor='aqua',style="filled" )
    g.edge('052','053', label2('Esophageal glands usually unequal in length, overlapping intestine dorsally or lateroventrally'))
    g.edge('052','060', label2('Esophageal glands enclosed in a bulb or equal in length, usually butting intestine'))

    g.node('053', '053',fillcolor='aqua',style="filled" )
    g.edge('053','054', label2('Weak to moderate cephalic framework, female head not low or flattened'))
    g.edge('053','057', label2('Well-developed cephalic framework, female head low , rounded or flattened'))

    g.node('054', '054',fillcolor='aqua',style="filled" )
    g.edge('054','055', label2('Well-developed stylet, lateral field with 5 lines'))
    g.edge('054','Trichotylenchus', label2('Stylet slender with diverging knobs, lateral field with 4 lines'))

    g.node('055', '055',fillcolor='aqua',style="filled" )
    g.edge('055','056', label2('Female tail cylindroid with rounded terminus'))
    g.edge('055','Telotylenchus', label2('Female tail elongate-conoid with blunt terminus'))

    g.node('056', '056',fillcolor='aqua',style="filled" )
    g.edge('056','Histotylenchus', label="Stylet cone asymmetrical, c' around 2, tail with broadly rounded terminus")
    g.edge('056','Telotylenchoides', label2('Stylet cone symmetrical, female tail with broadly rounded to bulbous terminus and strongly thickened cuticle'))

    g.node('057', '057',fillcolor='aqua',style="filled" )
    g.edge('057','058', label2('Esophagus overlapping intestine dorsally'))
    g.edge('057','059', label2('Esophagus overlapping intestine ventrally'))

    g.node('058', '058',fillcolor='aqua',style="filled" )
    g.edge('058','Pratylenchoides', label2('Short overlap, no obvious sexual dimorphism'))
    g.edge('058','Radopholus', label2('Long overlap, distinct sexual dimorphism'))

    g.node('059', '059',fillcolor='aqua',style="filled" )
    g.edge('059','Hirschmanniella', label2('Tail tip mucronate'))
    g.edge('059','Zygotylenchus', label2('Tail tip not mucronate'))

    g.node('060', '060',fillcolor='aqua',style="filled" )
    g.edge('060','061', label2('Lateral field with 4 lines, female tail not acute'))
    g.edge('060','Merlinius', label2('Lateral field with 6 lines, female tail acute or subacute'))

    g.node('061', '061',fillcolor='aqua',style="filled" )
    g.edge('061','Tylenchorhynchus', label2('Female tail conoid with terminus bluntly rounded'))
    g.edge('061','Paratrophurus', label2('Female tail cylindroid, tail with broadly rounded terminus and thick cuticle'))

    g.node('062', '062',fillcolor='aqua',style="filled" )
    g.edge('062','063', label2('Phasmids small, pore-like'))
    g.edge('062','064', label2('Phasmids enlarged'))

    g.node('063', '063',fillcolor='aqua',style="filled" )
    g.edge('063','', label2('Esophagus overlapping intestine dorsally and laterally, lip region with or without striation, DEGO <0.25 of stylet length behind knobs'))
    g.edge('063','', label2('Esophagus overlapping intestine ventrally, lip region without longitudinal striation, DEGO ≥0.25 of stylet length behind knobs'))

    g.node('064', '064',fillcolor='aqua',style="filled" )
    g.edge('064','065', label2('Both phasmids posterior to vulva'))
    g.edge('064','066', label2('One phasmid anterior and one posterior to vulva'))

    g.node('065', '065',fillcolor='aqua',style="filled" )
    g.edge('065','Scutellonema', label2('Phasmids nearly opposite each other in region of anus, lip region with transverse striations'))
    g.edge('065','Peltamigratus', label2('Phasmids anterior to anus, not opposite each other, lip region without striations'))

    g.node('066', '066',fillcolor='aqua',style="filled" )
    g.edge('066','Hoplolaimus', label2('Stylet knobs with anterior projections, <5 lines in lateral field, lateral field areolated throughout length'))
    g.edge('066','Aorolaimus', label2('Stylet knobs rounded and without anterior projections, 5 lines in lateral field, lateral field areolated at phasmids and in anterior'))

    g.node('067', '067',fillcolor='aqua',style="filled" )
    g.edge('067','068', label2('Females diovarial'))
    g.edge('067','071', label2('Females monovarial'))

    g.node('068', '068',fillcolor='aqua',style="filled" )
    g.edge('068','Macrotrophurus', label2('Tail short, subcylindrical, rounded; stylet very long (90-110 µm)'))
    g.edge('068','069', label2('Tail elongate, attenuated; stylet < 20 µm'))

    g.node('069', '069',fillcolor='aqua',style="filled" )
    g.edge('069','Antarctenchus', label2('Cephalic framework sclerotized; vulva with lateral membranes; male cloaca with hypoptygma'))
    g.edge('069','070', label2('Cephalic framework not sclerotized; vulva withithout lateral membranes; male cloaca without hypoptygma'))

    g.node('070', '070',fillcolor='aqua',style="filled" )
    g.edge('070','Psilenchus', label2('Head high, amphidial slit obvious; metacorpus posterior to middle of esophagus'))
    g.edge('070','Atetylenchus', label2('Head low, amphidial slit indistinct; metacorpus anterior to middle of esophagus'))

    g.node('071', '071',fillcolor='aqua',style="filled" )
    g.edge('071','Tylodorus', label2('Stylet very long (76-104 µm)'))
    g.edge('071','Epicharinema', label2('Stylet long (38-52 µm)'))
    g.edge('071','072', label2('Stylet moderate (22-34 µm)'))
    g.edge('071','073', label2('Stylet short (<22 µm)'))

    g.node('072', '072',fillcolor='aqua',style="filled" )
    g.edge('072','Campbellenchus', label2('Cuticle with longitudinal ridges'))
    g.edge('072','Gracilancea', label2('Cuticle without longitudinal ridges'))

    g.node('073', '073',fillcolor='aqua',style="filled" )
    g.edge('073','074', label2('Head with setae'))
    g.edge('073','075', label2('Head without setae'))

    g.node('074', '074',fillcolor='aqua',style="filled" )
    g.edge('074','Atylenchus', label2('Vulva covered by longitudinal flap; male without caudal alae; male cloaca with hypoptygma'))
    g.edge('074','Eutylenchus', label2('Vulva with lateral flaps; male with caudal alae; male cloaca raised'))

    g.node('075', '075',fillcolor='aqua',style="filled" )
    g.edge('075','076', label2('Cuticle with longitudinal ridges'))
    g.edge('075','080', label2('Cuticle without longitudinal ridges'))

    g.node('076', '076',fillcolor='aqua',style="filled" )
    g.edge('076','077', label2('Cone about 1/3 of stylet length'))
    g.edge('076','079', label2('Cone almost 1/2 of stylet length'))

    g.node('077', '077',fillcolor='aqua',style="filled" )
    g.edge('077','Basirienchus', label2('Transverse striations not visible through longitudinal ridges'))
    g.edge('077','078', label2('Transverse striations and longitudinal ridges form block (tessellate) pattern; lateral field with 4 lines'))

    g.node('078', '078',fillcolor='aqua',style="filled" )
    g.edge('078','Neothada', label2('Lip region with 2-3 striations, stylet without knobs'))
    g.edge('078','Basirienchus', label2('Lip region with 6-7 striations, stylet without knobs'))

    g.node('079', '079',fillcolor='aqua',style="filled" )
    g.edge('079','Pleurotylenchus', label2('Vulva covered by longitudinal flap; stylet 17-19 µm'))
    g.edge('079','Coslenchus', label2('Vulva with lateral flaps; stylet < 15 µm'))

    g.node('080', '080',fillcolor='aqua',style="filled" )
    g.edge('080','081', label2('Cone about 1/3 of stylet length'))
    g.edge('080','094', label2('Cone almost 1/2 of stylet length'))

    g.node('081', '081',fillcolor='aqua',style="filled" )
    g.edge('081','082', label2('Head high, with distinct lateral amphid slits'))
    g.edge('081','085', label2('Head variously shaped, amphid slit longitudinal'))

    g.node('082', '082',fillcolor='aqua',style="filled" )
    g.edge('082','Boleodorus', label2('Female body ventrally curved or spiral; female with offset spermatheca and oocytes in multiple rows'))
    g.edge('082','083', label2('Female body straight; oocytes not in multiple rows'))

    g.node('083', '083',fillcolor='aqua',style="filled" )
    g.edge('083','Basirienchus', label2('Tail bent or hook-shaped near tip'))
    g.edge('083','084', label2('Tail more or less straight'))

    g.node('084', '084',fillcolor='aqua',style="filled" )
    g.edge('084','Neopsilenchus', label2('Stylet without knobs, anterior part with wide lumen'))
    g.edge('084','Basiria', label2('Stylet with or without knobs, anterior conical with narrow lumen'))

    g.node('085', '085',fillcolor='aqua',style="filled" )
    g.edge('085','086', label2('Head with disc-like structure'))
    g.edge('085','088', label2('Head with smooth contour'))

    g.node('086', '086',fillcolor='aqua',style="filled" )
    g.edge('086','087', label2('Head with small disc'))
    g.edge('086','Cucullitylenchus', label2('Head with large dome-shaped structure'))

    g.node('087', '087',fillcolor='aqua',style="filled" )
    g.edge('087','Mitranema', label2('Very slender (a=62-76); caudal alae concave posteriorly'))
    g.edge('087','Filenchus', label2('Less slender; caudal alae rounded'))

    g.node('088', '088',fillcolor='aqua',style="filled" )
    g.edge('088','089', label2('Very slender (a=60-180); caudal alae lobed'))
    g.edge('088','090', label2('Body width variable; caudal alae rounded if present'))

    g.node('089', '089',fillcolor='aqua',style="filled" )
    g.edge('089','Ecphyadophora', label2('Head quadrangular; pore-like amphid apertures; body constricted after vulva'))
    g.edge('089','Ecphyadophoroides', label2('Head flattened; long amphid apertures; body not constricted after vulva'))

    g.node('090', '090',fillcolor='aqua',style="filled" )
    g.edge('090','091', label2('Cuticle deeply incised'))
    g.edge('090','092', label2('Cuticle not deeply incised'))

    g.node('091', '091',fillcolor='aqua',style="filled" )
    g.edge('091','Miculenchus', label2('Head quadrangular; body striations with zigzag pattern; male without caudal alae'))
    g.edge('091','Malenchus', label2('Head flattened; male with caudal alae'))

    g.node('092', '092',fillcolor='aqua',style="filled" )
    g.edge('092','Lelenchus', label2('Very slender; indistinct striation; head very flat; long, sinuous amphid aperture'))
    g.edge('092','093', label2('Larger body diameter; distinct striation; head quadrangular; aperture not sinuous'))

    g.node('093', '093',fillcolor='aqua',style="filled" )
    g.edge('093','Irantylenchus', label2('Head high with longitudinal amphid apertures lateral; clavate stylet knobs; DEGO > 1/2 stylet length behind knobs'))
    g.edge('093','Filenchus', label2('Head quadrangular; distinct striation; round stylet knobs; DEGO < 1/2 stylet length behind knobs'))

    g.node('094', '094',fillcolor='aqua',style="filled" )
    g.edge('094','095', label2('Vulva with lateral flaps'))
    g.edge('094','096', label2('Vulva without flaps'))

    g.node('095', '095',fillcolor='aqua',style="filled" )
    g.edge('095','Allotylenchus', label2('Lateral field with 2 lines; vagina thin; post-vulval sac short'))
    g.edge('095','Aglenchus', label2('Lateral field with 3 lines; vagina thickened; post-vulval sac short'))
    g.edge('095','Cephalenchus', label2('Lateral field with 4-6 lines; vagina not thickened; post-vulval sac long'))

    g.node('096', '096',fillcolor='aqua',style="filled" )
    g.edge('096','Polenchus', label2('Lateral field and striations inconspicuous; caudal alae very small'))
    g.edge('096','Tylenchus', label2('Lateral field and striations distinct; caudal alae distinct'))

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
