from django.test import TestCase

from docxtpl import DocxTemplate
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU')
date = datetime.now()

doc = DocxTemplate("doc/act.docx")
context = {
    'name_or_fio': 'Наименование/ФИО',
    'day': date.day,
    'month': date.strftime("%B"),
    'year': date.year,
    'position': 'Должность',
    'fio': 'ФИО',
}
doc.render(context)
doc.save("doc/generated_doc.docx")
