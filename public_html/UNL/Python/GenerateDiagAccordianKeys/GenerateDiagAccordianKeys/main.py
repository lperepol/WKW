
def readTemplate():
    accordian = ""
    fn = '../AccordianKey.txt'
    with open(fn) as f:
        accordian = f.read()
    return accordian

def write_key(htmltemplate):
    accordian = ""
    key = 1
    htmltemplate = str(htmltemplate)
    with open('AccordianKeys.html',"w") as f:
        while key < 150 :
            keystr = str(key).zfill(3)
            tempTemplate = htmltemplate.replace('KeyNumber', keystr)
            sub = 'collapseOne' + keystr
            tempTemplate = tempTemplate.replace('collapseOne002', sub)
            sub = 'collapseTwo' + keystr
            tempTemplate = tempTemplate.replace('collapseTwo002', sub)
            sub = 'collapseThree' + keystr
            tempTemplate = tempTemplate.replace('collapseThree003', sub)
            sub = 'accordionid' + keystr
            tempTemplate = tempTemplate.replace('accordionid', sub)
            sub = '<h3>' + keystr + '</h3>'
            tempTemplate = tempTemplate.replace('<h3>002</h3>', sub)

            sub = '<article class="my-3" id="accordion' + keystr + '">'
            tempTemplate = tempTemplate.replace('<article class="my-3" id="accordion">', sub)

            f.write(tempTemplate)
            key = key + 1

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

def main():
    htmltemplate = readTemplate()
    write_key(htmltemplate)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")




