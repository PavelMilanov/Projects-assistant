from docxtpl import DocxTemplate

# в документе сделать {{director}}
doc = DocxTemplate('template.docx')
context = { 'director' : 'И.И.Иванов'}
doc.render(context)
doc.save('report.docx')
