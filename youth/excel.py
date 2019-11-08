#! python3
from datetime import date
import json

import pandas
import openpyxl

wb = openpyxl.load_workbook('raw_youth.xlsx')
sheet = wb['Form Responses 1']
youthData = []

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one member.
    email = sheet['B' + str(row)].value
    name = sheet['C' + str(row)].value
    dob = sheet['D' + str(row)].value
    sex = sheet['E' + str(row)].value
    locality = sheet['F' + str(row)].value
    jumuiya = sheet['G' + str(row)].value
    phone = sheet['H' + str(row)].value
    nationalId = sheet['I' + str(row)].value
    pendingSacraments = sheet['K' + str(row)].value
    activities = sheet['L' + str(row)].value
    studentOrCareer = sheet['M' + str(row)].value
    occupation = sheet['N' + str(row)].value
    kin1Name = sheet['O' + str(row)].value
    kin1Phone = sheet['P' + str(row)].value
    kin1Relationship = sheet['Q' + str(row)].value
    kin2Name = sheet['R' + str(row)].value
    kin2Phone = sheet['S' + str(row)].value
    kin2Relationship = sheet['T' + str(row)].value
    syokimauResident = sheet['U' + str(row)].value

    # data manipulation
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) # noqa E501

    if not pendingSacraments:
        pendingSacraments = ' N/A '

    if not syokimauResident:
        syokimauResident = ' N/A '

    if not jumuiya:
        jumuiya = ' N/A '

    if not nationalId or isinstance(nationalId, str):
        nationalId = 'N/A'

    if isinstance(nationalId, float):
        nationalId = int(nationalId)

    data = {
        'NAME': name.upper(),
        'JUMUIYA': jumuiya.upper(),
        'PHONE NUMBER': phone,
        'EMAIL': email,
        'ID NUMBER': nationalId,
        'SEX': sex,
        'DATE OF BIRTH': str(dob),
        'AGE': age,
        'SYOKIMAU RESIDENT': syokimauResident,
        'LOCALITY': locality.upper(),
        'PENDING SACRAMENT': pendingSacraments,
        'ACTIVITIES INTERSTED IN': activities,
        'STUDENT OR CAREER': studentOrCareer,
        'OCCUPATION': occupation.upper(),
        'NEXT OF KIN 1 RELATIONSHIP': kin1Relationship.upper(),
        'NEXT OF KIN 1 NAME': kin1Name.upper(),
        'NEXT OF KIN 1 PHONE NUMBER': kin1Phone,
        'NEXT OF KIN 2 RELATIONSHIP': kin2Relationship.upper(),
        'NEXT OF KIN 2 NAME': kin2Name.upper(),
        'NEXT OF KIN 2 PHONE': kin2Phone,
    }

    youthData.append(data)


with open('youth.json', 'w', encoding='utf-8') as file:
    json.dump(youthData, file, ensure_ascii=False, indent=4)

pandas.read_json("youth.json").to_excel("youth.xlsx")
