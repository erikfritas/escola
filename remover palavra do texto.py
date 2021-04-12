# palavra = str(input("Digite a palavra que deseja remover: "))

# este script é bem simples: para ser usado vc insere o que está sendo pedido.

# insira a palavra a ser removida
palavra = [

]

# Exemplo de texto
# estas palavras são as fonts das do pygame, para usar vc remove o texto da variavel 'texto' e adiciona o texto que
# quiser deixando apenas a variavel texto que está no lado esquerdo da igualdade
texto = "['arial', 'batangbatangchegungsuhgungsuhche', 'couriernew', 'daunpenh', 'dokchampa', 'estrangeloedessa'," \
        " 'euphemia', 'gautami', 'vani', 'gulimgulimchedotumdotumche', 'impact', 'iskoolapota', 'kalinga', 'kartika'," \
        " 'khmerui', 'laoui', 'latha', 'lucidaconsole', 'malgungothic', 'mangal', 'meiryomeiryomeiryouimeiryouiitalic'," \
        " 'meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftyahei'," \
        " 'mingliupmingliumingliuhkscs', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti'," \
        " 'msgothicmspgothicmsuigothic', 'msminchomspmincho', 'mvboli', 'microsoftnewtailue', 'nyala'," \
        " 'microsoftphagspa', 'plantagenetcherokee', 'raavi', 'segoescript', 'segoeui', 'segoeuisemibold'," \
        " 'segoeuisymbol', 'shruti', 'simsunnsimsun', 'simsunextb', 'sylfaen', 'microsofttaile', 'timesnewroman'," \
        " 'tunga', 'vrinda', 'shonarbangla', 'microsoftyibaiti', 'tahoma', 'microsoftsansserif', 'angsananew'," \
        " 'aparajita', 'cordianew', 'ebrima', 'gisha', 'kokila', 'leelawadee', 'microsoftuighur', 'moolboran'," \
        "'symbol', 'utsaah', 'vijaya', 'wingdings', 'andalus', 'arabictypesetting', 'simplifiedarabic', " \
        "'simplifiedarabicfixed'," \
        " 'sakkalmajalla', 'traditionalarabic', 'aharoni', 'david', 'frankruehl', 'levenim', 'miriam', 'miriamfixed'," \
        " 'narkisim', 'rod', 'fangsong', 'simhei', 'kaiti', 'angsanaupc', 'browallianew', 'browalliaupc', 'cordiaupc'," \
        " 'dilleniaupc', 'eucrosiaupc', 'freesiaupc', 'irisupc', 'jasmineupc', 'kodchiangupc', 'lilyupc', 'dfkaisb'," \
        " 'lucidasans', 'arialblack', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas'" \
        ", 'constantia', 'corbel', 'franklingothicmedium', 'gabriola', 'georgia', 'palatinolinotype', 'segoeprint', " \
        "'trebuchetms', 'verdana', 'webdings', 'nirmalaui', 'nirmalauinegrito', 'bookantiquanegrito', " \
        "'bookantiquanegritoitálico', 'bookantiquaitálico', 'arialnegrito', 'arialnegritoitálico', 'arialitálico', " \
        "'arialms', 'bookantiqua', 'bookmanoldstyle', 'bookmanoldstylenegrito', 'bookmanoldstylenegritoitálico', " \
        "'bookmanoldstyleitálico', 'bookshelfsymbol7', 'century', 'gadugi', 'gaduginegrito', 'garamond', " \
        "'garamondnegrito', 'garamonditálico', 'centurygothic', 'centurygothicnegrito', 'centurygothicnegritoitálico', " \
        "'centurygothicitálico', 'microsoftjhengheimicrosoftjhengheiui', " \
        "'microsoftjhengheinegritomicrosoftjhengheiuinegrito', 'microsoftuighurnegrito', " \
        "'microsoftyaheimicrosoftyaheiui', 'microsoftyaheinegritomicrosoftyaheiuinegrito', 'monotypecorsiva', 'extra', " \
        "'msreferencesansserif', 'msreferencespecialty', 'segoeuisemilight', 'segoeuiemoji', 'wingdings2', " \
        "'wingdings3', 'unispacebold', 'lucidasanstypewriterregular', 'lucidasanstypewriter', 'lucidasansregular', " \
        "'lucidabrightregular', 'lucidabright', 'helvlightregular', 'agencyfb', 'lato']"

palen = len(palavra)
index = 0

while index != palen:
    texto = texto.replace(palavra[index], "")
    texto = texto.replace(palavra[index].capitalize(), "")
    index += 1

texto = texto.replace(',', ',\n')

print("\n\n")
print(texto)
print("\n")
print(texto.replace("\n", "\\n\\\n"))

