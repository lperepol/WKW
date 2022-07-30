# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
def draw():

    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'

    g.node('001', label='Rhabditidae',fillcolor='red',style="filled")

    g.node('A1', 'Matthesonema',fillcolor='aqua',style="filled" )
    g.edge('001','A')

    g.node('B1', 'Distolabrellus',fillcolor='aqua',style="filled" )
    g.edge('001','B')

    g.node('C1', 'Teratorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','C')

    g.node('D1', 'Cruznema',fillcolor='aqua',style="filled" )
    g.edge('001','D1')

    g.node('E1', 'Rhabpanus',fillcolor='aqua',style="filled" )
    g.edge('001','E1')

    g.node('F1', 'Mesorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','F1')

    g.node('G1', 'Parasitorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','G1')

    g.node('H1', 'Crustorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','H1')

    g.node('I1', 'Pelodera\nStrongyloid.-gr.',fillcolor='aqua',style="filled" )
    g.edge('001','I1')

    g.node('A2', 'Neorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','A2')

    g.node('B2', 'Xylorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','B2')

    g.node('C2', 'Sclerorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','C2')

    g.node('D2', 'Diploscapter',fillcolor='aqua',style="filled" )
    g.edge('001','D2')

    g.node('E2', 'Protorhabditis\nXylocla-group',fillcolor='aqua',style="filled" )
    g.edge('001','E2')

    g.node('F2', 'Protorhabditis\nOxyuruides-group',fillcolor='aqua',style="filled" )
    g.edge('001','F2')

    g.node('G2', 'Prodontorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','G2')

    g.node('H2', 'Caenorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','H2')

    g.node('I2', 'Pelodera\nCoarctata-group',fillcolor='aqua',style="filled" )
    g.edge('001','I2')

    g.node('A3', 'Pelodera\nTeres-group',fillcolor='aqua',style="filled" )
    g.edge('001','A3')

    g.node('B3', 'Reiterina',fillcolor='aqua',style="filled" )
    g.edge('001','B3')

    g.node('C3', 'Buetschlinema',fillcolor='aqua',style="filled" )
    g.edge('001','C3')

    g.node('D3', 'Pellioditis',fillcolor='aqua',style="filled" )
    g.edge('001','D3')

    g.node('E3', 'Heterorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','E3')

    g.node('F3', 'Litoditis',fillcolor='aqua',style="filled" )
    g.edge('001','F3')

    g.node('G3', 'Oscheius\nDolichura-group',fillcolor='aqua',style="filled" )
    g.edge('001','G3')

    g.node('H3', 'Oscheius\nlnsectivorus-group',fillcolor='aqua',style="filled" )
    g.edge('001','H3')

    g.node('I3', 'Metarhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','I3')

    g.node('A4', 'Himatidiophila',fillcolor='aqua',style="filled" )
    g.edge('001','A4')

    g.node('B4', 'Saprorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','B4')

    g.node('C4', 'Poikilolaimus\nOxycercus-group',fillcolor='aqua',style="filled" )
    g.edge('001','C4')

    g.node('D4', 'Poikilolaimus\nMicoletzkyi-group',fillcolor='aqua',style="filled" )
    g.edge('001','D4')

    g.node('E4', 'Noteodiplogasler',fillcolor='aqua',style="filled" )
    g.edge('001','E4')

    g.node('F4', 'Choriorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','F4')

    g.node('G4', 'Rhabditis\nBrassicae-group',fillcolor='aqua',style="filled" )
    g.edge('001','G4')

    g.node('H4', 'Rhabditis\nMaupasi-group',fillcolor='aqua',style="filled" )
    g.edge('001','H4')

    g.node('I4', 'Eudronema',fillcolor='aqua',style="filled" )
    g.edge('001','I4')

    g.node('A5', 'Stomachorhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','XX')

    g.node('B5', 'Rhabditonema',fillcolor='aqua',style="filled" )
    g.edge('001','B5')

    g.node('C5', 'Rhabditoides',fillcolor='aqua',style="filled" )
    g.edge('001','XX')

    g.node('D5', 'Haematozoon',fillcolor='aqua',style="filled" )
    g.edge('001','D5')

    g.node('E5', 'Rhomborhabditis',fillcolor='aqua',style="filled" )
    g.edge('001','E5')

    g.node('F5', 'Oryctonema',fillcolor='aqua',style="filled" )
    g.edge('001','F5')

    g.node('G5', 'Diploscapteroides',fillcolor='aqua',style="filled" )
    g.edge('001','G5')

    g.node('H5', 'Rhabditella',fillcolor='aqua',style="filled" )
    g.edge('001','H5')

    g.node('I5', 'Cephaloboides',fillcolor='aqua',style="filled" )
    g.edge('001','I5')



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
