from django.test import TestCase

from docxtpl import DocxTemplate
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU')
date = datetime.now()

doc = DocxTemplate("doc/act.docx")
context = {
    'id': 1,
    'name_or_fio': 'Наименование/ФИО',
    'day': date.day,
    'month': date.strftime("%B"),
    'year': date.year,
    'position': 'Должность',
    'fio': 'ФИО',
}
doc.render(context)
id_name = context.get('id')
doc.save(f"doc/generated_doc_{id_name}.docx")
