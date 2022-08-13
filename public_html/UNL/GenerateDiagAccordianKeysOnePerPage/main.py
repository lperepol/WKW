
def readTemplate():
    accordian = ""
    fn = '/0program/var/www/WKW/public_html/UNL/Keys/Key_002.html'
    with open(fn) as f:
        htmltemplate = f.read()
    return htmltemplate

def write_key(htmltemplate):
    accordian = ""
    key = 1
    htmltemplate = str(htmltemplate)
    while key < 102:
        keystr = str(key).zfill(3)
        fn = '/0program/var/www/WKW/public_html/UNL/Keys/newKeys/' + "Key_" + keystr + ".html"
        with open(fn,"w") as f:
            str1 = 'Key' + keystr
            str1 = '<title>Key_Template</title>'.replace('Key_Template', str1)
            tempTemplate = htmltemplate.replace('<title>Key_Template</title>', str1)

            str1 = '<h1>002</h1>'.replace('002', keystr)
            tempTemplate = tempTemplate.replace('<h1>002</h1>', str1)

            str1 = "displayImages('accordioncollapseOne002-image-target', this)".replace('002', keystr)
            tempTemplate = tempTemplate.replace("displayImages('accordioncollapseOne002-image-target', this)", str1)


            str1 = '<a href="/UNL/Keys/Key_001.html">001</a>'.replace('001', 'XXX')
            tempTemplate = tempTemplate.replace('<a href="/UNL/Keys/Key_001.html">001</a>', str1)


            str1 = '<a href="/UNL/Keys/Key_001.html">001</a>'.replace('001', 'XXX')
            tempTemplate = tempTemplate.replace('<a href="/UNL/Keys/Key_001.html">001</a>', str1)

            str1 = '<div id="accordioncollapseOne002-image-target">'.replace('002', keystr)
            tempTemplate = tempTemplate.replace('<div id="accordioncollapseOne002-image-target">', str1)


            #str1 = ''.replace('', keystr)
            #tempTemplate = tempTemplate.replace('', str1)

            str1 = "displayImages('accordioncollapseTwo002-image-target', this)".replace('002', keystr)
            tempTemplate = tempTemplate.replace("displayImages('accordioncollapseTwo002-image-target', this)", str1)

            str1 = '<a href="/UNL/Keys/Key_001.html">001</a>'.replace('001', 'XXX')
            tempTemplate = tempTemplate.replace('<a href="/UNL/Keys/Key_001.html">001</a>', str1)

            str1 = '<a href="/UNL/Keys/Key_001.html">003 </a>'.replace('001', 'XXX')
            tempTemplate = tempTemplate.replace('<a href="/UNL/Keys/Key_001.html">003 </a>', str1)

            str1 = '<div id="accordioncollapseTwo002-image-target">'.replace('002', keystr)
            tempTemplate = tempTemplate.replace('<div id="accordioncollapseTwo002-image-target">', str1)

            tempTemplate = tempTemplate.replace('Stylet present', 'XXXX')
            tempTemplate = tempTemplate.replace('Stylet absent', 'XXXX')



            f.write(tempTemplate)
        key = key + 1


def main():
    htmltemplate = readTemplate()
    write_key(htmltemplate)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")




