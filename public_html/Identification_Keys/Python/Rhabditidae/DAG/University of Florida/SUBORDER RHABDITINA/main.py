# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
def draw():

    # https://entnemdept.ufl.edu/nguyen/morph/rhabdi/rhabkey.HTM#ALOIONEMA
    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'

    g.node('000', label='SUBORDER RHABDITINA',fillcolor='red',style="filled")

    g.node('003', 'Aloionematoidea ',fillcolor='aqua',style="filled" )
    g.edge('000','003',label='Stoma short,\n with weakly cuticularized rhabdions;\n bursa absent')
    g.node('002', ' ',fillcolor='aqua',style="filled" )
    g.edge('000','002',label='Stoma cylindrical,\n well cuticularized;\nbursa present supported by ribs,\nsometimes reduced ')

    g.node('002', '002',fillcolor='aqua',style="filled" )
    g.node('004', 'Bunonematoidea',fillcolor='aqua',style="filled" )
    g.edge('002','004',label='Body asymetrical,\n left side with longitudinal ridges,\n right side with various structures\n such as network pattern,\n tubercles, warts, fins\n (Fig. 4)')
    g.edge('002','011',label=' Body symetrical;\n various structures such as network pattern,\n tubercles, warts,fins absent ')

    g.node('003', 'SUPERFAMILY\nALLOIONEMATOIDEA',fillcolor='aqua',style="filled" )
    g.node('Alloionematidae', 'Alloionematidae',fillcolor='aqua',style="filled" )
    g.edge('003','Alloionematidae',label='One family')
    g.node('Alloionema', 'Alloionema',fillcolor='aqua',style="filled" )
    g.edge('003','Alloionema',label='Labial region with 6 fused lips;\ndorsal metarhabdion with numerous denticles')
    g.node('Rhabditophanes', 'Rhabditophanes',fillcolor='aqua',style="filled" )
    g.edge('003','Rhabditophanes',label='Labial region with 4 lips;\nmetastom without denticles;\nesophagus with a slight swelling\n anterior to median bulb')

    g.node('004', 'SUPERFAMILY\nBUNONEMATOIDEA',fillcolor='aqua',style="filled" )
    g.node('005', 'Bunonematidae',fillcolor='aqua',style="filled" )
    g.edge('004','005',label='Right side of body with hexagonal network,\n tubercles or warts,\n left side with 5 longitudinal\n  ridges (Fig. 4-10 )')
    g.node('Pterygonematidae', 'Pterygonematidae',fillcolor='aqua',style="filled" )
    g.edge('004','Pterygonematidae',label='Right side of body without network,\n tubercles or warts but with rows of rhomboidal structures,\n left side with longitudinal ridges ')
    g.node('Pterygonematinae', 'Pterygonematinae',fillcolor='aqua',style="filled" )
    g.edge('004','Pterygonematinae',label='Only one subfamily')
    g.node('Pterygorhabditis', 'Pterygorhabditis',fillcolor='aqua',style="filled" )
    g.edge('004','Pterygorhabditis',label='Only one genus\n  (Fig. 3) ')

    g.node('005', '005',fillcolor='aqua',style="filled" )
    g.edge('005','006',label='Right side of body with warts,\n papillae or longitudinal ridges (Fig. 4-7)')
    g.node('009', 'Craspedonematinae.',fillcolor='aqua',style="filled" )
    g.edge('005','009',label='Right side with large shield-like structures\n or with crust-like swellings (Fig. 8-10)')

    g.node('006', 'Bunonematinae',fillcolor='aqua',style="filled" )
    g.node('Bunonema', 'Bunonema',fillcolor='aqua',style="filled" )
    g.edge('006','Bunonema',label='Dorsal and ventral menbranes\n forming collar on right side of body;\n warts paired,\n supported  by internal rods\n  (Fig. 4) .')
    g.edge('006','007',label='No collar forming on right side of body;\n warts without internal rods,\n paired, unpaired or lacking\n (Fig. 5)...')

    g.node('007', '007',fillcolor='aqua',style="filled" )
    g.node('Rhodonema', 'Rhodonema',fillcolor='aqua',style="filled" )
    g.edge('007','Rhodonema',label='Warts or papillae absent,\n right side with striated ridges\n  (Fig. 5')
    g.edge('007','008',label='Warts  or papillae present,\n striated ridges on right side absent\n (Fig. 6,7).')

    g.node('008', '008',fillcolor='aqua',style="filled" )
    g.node('Serronema', 'Serronema',fillcolor='aqua',style="filled" )
    g.edge('008','Serronema',label='Right side of body ornamented with single row of rod-like warts(Fig. 6)')
    g.node('Rhodolaimus', 'Rhodolaimus',fillcolor='aqua',style="filled" )
    g.edge('008','Rhodolaimus',label='Two or more warts joined to form\n paired or unpaired fins,\n or continuous rows\n  (Fig. 7) ')

    g.node('009', '009',fillcolor='aqua',style="filled" )
    g.node('Craspedonema', 'Craspedonema',fillcolor='aqua',style="filled" )
    g.edge('009','Craspedonema',label='Right side without warts\n but with several shields\n or crust-like swellings (Fig. 8)')
    g.edge('009','010',label='Right side with warts and shields (Fig. 9, 10)')

    g.node('010', '010',fillcolor='aqua',style="filled" )
    g.node('Aspidonema', 'Aspidonema',fillcolor='aqua',style="filled" )
    g.edge('010','Aspidonema',label='Warts paired, in two longitudinal rows  (Fig. 9) ..')
    g.node('Sachsium', 'Sachsium',fillcolor='aqua',style="filled" )
    g.edge('010','Sachsium',label='Warts unpaired,\n in single row alternating with large\n shields or crust-like structures\n (Fig. 10)')

    g.node('011', 'SUPERFAMILY\nRHABDITOIDEA',fillcolor='aqua',style="filled" )
    g.node('Diploscapteridae', 'Diploscapteridae',fillcolor='aqua',style="filled" )
    g.edge('011','Diploscapteridae',label='Dorsal and ventral lips\n transformed into\n cuticularized fossors\n (Fig. 11) ')
    g.node('Diploscapterinae', 'Diploscapterinae',fillcolor='aqua',style="filled" )
    g.edge('011','Diploscapterinae',label='Only one subfamily')
    g.node('Diploscapter', 'Diploscapter',fillcolor='aqua',style="filled" )
    g.edge('011','Diploscapter',label='Only one genus\n  (Fig. 11) ')
    g.edge('011','012',label='Dorsal and ventral lips normal ')

    g.node('012', '012',fillcolor='aqua',style="filled" )
    g.edge('012','014',label='Stoma long with large,\ntransverse dorsal tooth\n (Fig. 12, 13)')
    g.edge('012','013',label='Stoma long with parallel walls,\n without tooth\n (Fig. 14, 15).')

    g.node('013', '013',fillcolor='aqua',style="filled" )
    g.edge('013','015',label='Stoma about twice as long as wide;\n esophageal corpus cylindrical;\n bursa absent.')
    g.node('016', 'Rhabditidae',fillcolor='aqua',style="filled" )
    g.edge('013','016',label='Stoma more than 3 times\n as long as wide\n (except in Amphidirhabditinae,\n then amphids large);\n bursa generally\n well developed,\n if rudimentary, \nthen esophageal corpus\n distinctly swollen.')

    g.node('014', 'Odontorhabditidae',fillcolor='aqua',style="filled" )
    g.node('Diploscapteroides', 'Diploscapteroides',fillcolor='aqua',style="filled" )
    g.edge('014','Diploscapteroides',label='Cheilorhabdion\nstrongly cuticularized,\n female tail long,\n tapering gradually')
    g.node('Cephaloboides', 'Cephaloboides',fillcolor='aqua',style="filled" )
    g.edge('014','Cephaloboides',label='Cheilorhabdion\nslightly cuticularized,\nfemale tail narrowing suddenly\n to form spike\n(Fig. 13) ')

    g.node('015', 'Rhabditonematidae',fillcolor='aqua',style="filled" )
    g.node('Rhabditonema', 'Rhabditonema',fillcolor='aqua',style="filled" )
    g.edge('015','Rhabditonema',label='Metarhabdion\n with small denticles,\n female tail long,\n about 1/8 of body length\n (Fig. 14)')
    g.node('Saprorhabditis', 'Saprorhabditis',fillcolor='aqua',style="filled" )
    g.edge('015','Saprorhabditis',label='Metarhabdion\n without denticles;\n female tail short,\n about 1/50 of body length\n (Fig. 15).')

    g.node('016', '016',fillcolor='aqua',style="filled" )
    g.node('Stomachorhabditinae', 'Stomachorhabditinae',fillcolor='aqua',style="filled" )
    g.edge('016','Stomachorhabditinae',label='Anterior end of intestinal\n wall folded\n (Fig. 16);\n bursa absent')
    g.node('Stomachorhabditis', 'Stomachorhabditis',fillcolor='aqua',style="filled" )
    g.edge('016','Stomachorhabditis',label='Only one genus\n (Fig. 16)')
    g.edge('016','017',label='Anterior end of intestinal\n wall not folded,\n bursa present')

    g.node('017', '017',fillcolor='aqua',style="filled" )
    g.node('Amphidirhabditinae', 'Amphidirhabditinae',fillcolor='aqua',style="filled" )
    g.edge('017','Amphidirhabditinae',label='Stoma short,\n amphids large,\n at about mid-stoma;\n cheilorhabdion long,\n curved, well cuticularized\n (Fig.17) .')
    g.node('Amphidirhabditis', 'Amphidirhabditis',fillcolor='aqua',style="filled" )
    g.edge('017','Amphidirhabditis',label='Only one genus  (Fig. 17)')
    g.edge('017','018',label='Stoma longer,\n amphids very small,\n on lateral lips;\n cheilorhabdion simple,\n not well cuticularized')

    g.node('018', '018',fillcolor='aqua',style="filled" )
    g.edge('018','022',label='Stoma usually long and narrow;\n glotoid apparatus and denticles absent')
    g.edge('018','019',label='Stoma typical rhabditoid;\n glotoid apparatus and denticles present ')

    g.node('019', '019',fillcolor='aqua',style="filled" )
    g.edge('019','025',label='Female usually small,\n gonad single;\n vulva close to anus')
    g.edge('019','020',label='Female gonads\n usually paired,\n vulva at mid-body')

    g.node('020', '020',fillcolor='aqua',style="filled" )
    g.edge('020','032',label='Bursa\npeloderan')
    g.edge('020','021',label='Bursa\nleptoderan')

    g.node('021', '021',fillcolor='aqua',style="filled" )
    g.edge('021','039',label='Lips with numerous cilliae,\n anterior part of esophagus\n covering more than half of stoma(Fig. 38-39) ')
    g.edge('021','040',label=' Lips without cilliae,\n anterior part of esophagus\n usually covering less\n than half of stoma ')

    g.node('022', 'Subfamily\nProtorhabditinae',fillcolor='aqua',style="filled" )
    g.node('Parasitorhabditis', 'Parasitorhabditis',fillcolor='aqua',style="filled" )
    g.edge('022','Parasitorhabditis',label=' Female gonad single;\n spicules fused (Fig. 18)')
    g.edge('022','023',label='Female gonads paired;\n spicules not fused.')

    g.node('023', '023',fillcolor='aqua',style="filled" )
    g.node('Paradoxorhabditis', 'Paradoxorhabditis',fillcolor='aqua',style="filled" )
    g.edge('023','Paradoxorhabditis',label='Bursa pseudopeloderan;\n corpus of esophagus cylindrical,\n isthmus very weak\n  (Fig. 19) .')
    g.edge('023','024',label='Bursa peloderan;\n esophagus with distinct\n corpus and isthmus')

    g.node('024', '024',fillcolor='aqua',style="filled" )
    g.node('Prodontorhabditis', 'Prodontorhabditis',fillcolor='aqua',style="filled" )
    g.edge('024','Prodontorhabditis',label='Anterior end of prorhabdion\n with three small teeth;\n bursa closed  (Fig. 20)')
    g.node('Protorhabditis', 'Protorhabditis',fillcolor='aqua',style="filled" )
    g.edge('024','Protorhabditis',label='Prorhabdion without small teeth;\n bursa usually open (Fig. 21)')

    g.node('025', 'Subfamily\nMesorhabditinae',fillcolor='aqua',style="filled" )
    g.edge('025','026',label='Cheilorhabdion\n cuticularized\n (Fig. 22-24).')
    g.edge('025','028',label='Cheilorhabdion\n not cuticularized')

    g.node('026', '026',fillcolor='aqua',style="filled" )
    g.node('Teratorhabditis', 'Teratorhabditis',fillcolor='aqua',style="filled" )
    g.edge('026','Teratorhabditis',label='Labial edges strongly cuticularized (Fig. 22).')
    g.edge('026','027',label='Labial edges not strongly cuticularized ')

    g.node('027', '027',fillcolor='aqua',style="filled" )
    g.node('Rhabpanus', 'Rhabpanus',fillcolor='aqua',style="filled" )
    g.edge('027','Rhabpanus',label='Bursa pseudopeloderan  (Fig. 23)')
    g.node('Cruznema', 'Cruznema',fillcolor='aqua',style="filled" )
    g.edge('027','Cruznema',label='Bursa peloderan  (Fig. 24)')

    g.node('028', '028',fillcolor='aqua',style="filled" )
    g.edge('028','029',label='Female tail very short,\n broadly rounded or narrowing\n suddenly with spine at terminus  (Fig. 25,26) ')
    g.edge('028','030',label='Female tail elongate, conical with pointed terminus ')

    g.node('029', '029',fillcolor='aqua',style="filled" )
    g.node('Operculorhabditis', 'Operculorhabditis',fillcolor='aqua',style="filled" )
    g.edge('029','Operculorhabditis',label='Female tail\n with spine\n  (Fig. 25) ')
    g.node('Marispelodera', 'Marispelodera',fillcolor='aqua',style="filled" )
    g.edge('029','Marispelodera',label='Female tail with broadly\n rounded terminus,\n without spine (Fig. 26)')

    g.node('030', '030',fillcolor='aqua',style="filled" )
    g.node('Bursilla', 'Bursilla',fillcolor='aqua',style="filled" )
    g.edge('030','Bursilla',label='Bursa very narrow;\n spicules shorter than tail\n and fused at tip (Fig. 27).')
    g.edge('030','031',label='Bursa well developed;\nspicules longer than tail and\n fused at least to one third\n of their length.')

    g.node('031', '031',fillcolor='aqua',style="filled" )
    g.node('Crustorhabditis', 'Crustorhabditis',fillcolor='aqua',style="filled" )
    g.edge('031','Crustorhabditis',label='Spicules\n fused to two third of their length;\n bursa crenate in its anterior half\n (Fig. 28)')
    g.node('Mesorhabditis', 'Mesorhabditis',fillcolor='aqua',style="filled" )
    g.edge('031','Mesorhabditis',label='Spicules\n fused to one third,\n sometimes one half of their length;\n bursa smooth (Fig. 29).')

    g.node('032', 'Subfamily\nPeloderinae',fillcolor='aqua',style="filled" )
    g.edge('032','033',label=' Bursa\n closed anteriorly\n (Fig. 30, 31) ')
    g.edge('032','034',label='Bursa\n not closed anteriorly')

    g.node('033', '033',fillcolor='aqua',style="filled" )
    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('033','',label='Female tail\n tapering gradually;\n spicules not fused;\n bursa with nine\n pairs of ribs\n (Fig. 30)')
    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('033','',label='Female tail\n narrowing suddenly\n with or without spike on terminus;\n spicules fused;\n bursa with ten\n pairs of ribs  (Fig. 31) ....')

    g.node('034', '034',fillcolor='aqua',style="filled" )
    g.node('Phasmarhabditis', 'Phasmarhabditis',fillcolor='aqua',style="filled" )
    g.edge('034','Phasmarhabditis',label='Stomal\n tube short,\n about once or twice as long as wide;\n cheilorhabdion cuticularized;\n phasmids dot-like,\nvery prominent   (Fig. 32) .')
    g.edge('034','035',label='Stomal\n tube normal,\n at least 4 times as long as wide,\n cheilorhabdion usually not cuticularized;\n phasmids point-like,\n small ')

    g.node('035', '035',fillcolor='aqua',style="filled" )
    g.edge('035','036',label='Spicules\n fused;\n bursa with ten pairs\n of ribs\n (Fig. 33,34) .')
    g.edge('035','037',label='Spicules\n not fused;\n bursa with nine pairs\n of ribs\n (Fig. 35, 37) ')

    g.node('036', '036',fillcolor='aqua',style="filled" )
    g.node('Rhomborhabditis', 'Rhomborhabditis',fillcolor='aqua',style="filled" )
    g.edge('036','Rhomborhabditis',label=' Two first pairs of ribs not on bursa;\n female tail rounded (Fig. 33).')
    g.node('Pelodera', 'Pelodera',fillcolor='aqua',style="filled" )
    g.edge('036','Pelodera',label='All ribs on bursa;\n female tail spicate  (Fig. 34)')

    g.node('037', '037',fillcolor='aqua',style="filled" )
    g.node('Pellioditis', 'Pellioditis',fillcolor='aqua',style="filled" )
    g.edge('037','Pellioditis',label='Metarhabdion\n each with 3 or 5\n minute warts\n   (Fig. 35) .')
    g.edge('037','038',label='Metarhabdion\n each with 2 to 3\n bristle-like denticles\n (Fig. 36, 37) ')

    g.node('038', '',fillcolor='aqua',style="filled" )
    g.node('Xylorhabditis', 'Xylorhabditis',fillcolor='aqua',style="filled" )
    g.edge('038','Xylorhabditis',label='Cheilorhabdion\n cuticularized;\n corpus swollen  (Fig. 36) ')
    g.node('Dolichorhabditis', 'Dolichorhabditis',fillcolor='aqua',style="filled" )
    g.edge('038','Dolichorhabditis',label='Cheilorhabdion\n not cuticularized;\n corpus cylindrical')

    g.node('039', 'Subfamily\nAblechroiulinae',fillcolor='aqua',style="filled" )
    g.node('Rhabditoides', 'Rhabditoides',fillcolor='aqua',style="filled" )
    g.edge('039','Rhabditoides',label='Bursa\n rudimentary\n with 10 pairs of ribs\n (Fig. 38).')
    g.node('Ablechroiulus', 'Ablechroiulus',fillcolor='aqua',style="filled" )
    g.edge('039','Ablechroiulus',label='Bursa\n narrow,\n but well visible,\n with nine pairs of ribs\n (Fig. 39)')

    g.node('040', 'Subfamily\nRhabditinae',fillcolor='aqua',style="filled" )
    g.node('Colporhabditis', 'Colporhabditis',fillcolor='aqua',style="filled" )
    g.edge('040','Colporhabditis',label='Labial edges strongly cuticularized (Fig. 40)..')
    g.edge('040','041',label='Labial edges not cuticularized.')

    g.node('041', '041',fillcolor='aqua',style="filled" )
    g.node('Oscheius', 'Oscheius',fillcolor='aqua',style="filled" )
    g.edge('041','Oscheius',label='Stoma\n very short,\n protostom as long as or \nslightly longer than wide\n (Fig. 41)')
    g.edge('041','042',label='Stoma\n much longer')

    g.node('042', '042',fillcolor='aqua',style="filled" )
    g.edge('042','043',label='Bursa rudimentary (Fig. 42-46')
    g.edge('042','047',label='Bursa normal (Fig. 47, 48) ')

    g.node('043', '043',fillcolor='aqua',style="filled" )
    g.edge('043','044',label='Each spicule\n with long dorsal thorn\n (Fig. 42-43);\n metarhabdion\n with minute warts')
    g.edge('043','045',label='Spicules\n without dorsal thorn;\n metarhabdion with\n setose denticles\n (Fig.44, 46)')

    g.node('044', '044',fillcolor='aqua',style="filled" )
    g.node('Curviditis', 'Curviditis',fillcolor='aqua',style="filled" )
    g.edge('044','Curviditis',label='Female tail\n narrowing suddenlly\n to form spike;\n bursa with ten pairs of ribs')
    g.node('Rhabditella', 'Rhabditella',fillcolor='aqua',style="filled" )
    g.edge('044','Rhabditella',label='Female tail\n tapering gradually\n to form long,\n finely pointed tail (Fig. 43).')

    g.node('045', '045',fillcolor='aqua',style="filled" )
    g.node('Poikilolaimus', 'Poikilolaimus',fillcolor='aqua',style="filled" )
    g.edge('045','Poikilolaimus',label='Amphids\n relatively large,\n behind labial region;\n bursa with 7 pairs of ribs\n  (Fig. 44)')
    g.edge('045','046',label=' Amphids\n very small,\n on lateral lip;\n bursa with nine pairs of ribs.')

    g.node('046', '046',fillcolor='aqua',style="filled" )
    g.node('Cuticularia', 'Cuticularia',fillcolor='aqua',style="filled" )
    g.edge('046','Cuticularia',label='Nematode\n with cuticular sheath;\n female tail short,\n spikate  (Fig. 45)')
    g.node('Rhittis', 'Rhittis',fillcolor='aqua',style="filled" )
    g.edge('046','Rhittis',label='Nematode\n with normal cuticle;\n female tail tapering gradually  (Fig. 46) ')

    g.node('047', '047',fillcolor='aqua',style="filled" )
    g.node('Discoditis', 'Discoditis',fillcolor='aqua',style="filled" )
    g.edge('047','Discoditis',label='Bursa closed anteriorly (Fig. 47)')
    g.node('Rhabditis', 'Rhabditis',fillcolor='aqua',style="filled" )
    g.edge('047','Rhabditis',label=' Bursa open anteriorly  (Fig. 48)')

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
