import docx

document = docx.Document("doc/act_primer.docx")

table = document.tables[1]
for row in table.rows:
    string = ''
    for cell in row.cells:
        string = string + cell.text + ' '
    print(string)
