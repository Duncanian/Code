#! python3
import openpyxl

wb = openpyxl.load_workbook('october.xlsx', data_only=True)
sheet = wb['MAIN']

farmerData = []

for row in range(3, 965):  # upto number of farmers
    # Each row in the spreadsheet has data for one member.
    number = sheet['A' + str(row)].value
    name = sheet['B' + str(row)].value
    station = sheet['C' + str(row)].value
    farmerData.append(sheet['AI' + str(row)].value)
    rate = sheet['AJ' + str(row)].value
    farmerData.append(sheet['AK' + str(row)].value)
    farmerData.append(sheet['AL' + str(row)].value)
    farmerData.append(sheet['AO' + str(row)].value)
    farmerData.append(sheet['AP' + str(row)].value)
    farmerData.append(sheet['AQ' + str(row)].value)
    farmerData.append(sheet['AT' + str(row)].value)
    farmerData.append(sheet['AU' + str(row)].value)
    farmerData.append(sheet['AV' + str(row)].value)
    farmerData.append(sheet['AX' + str(row)].value)
    farmerData.append(sheet['AY' + str(row)].value)
    farmerData.append(sheet['AZ' + str(row)].value)
    farmerData.append(sheet['BA' + str(row)].value)
    farmerData.append(sheet['BB' + str(row)].value)
    farmerData.append(sheet['BC' + str(row)].value)
    farmerData.append(sheet['BD' + str(row)].value)
    farmerData.append(sheet['AW' + str(row)].value)
    farmerData.append(sheet['BE' + str(row)].value)
    bank = sheet['BF' + str(row)].value
    accountNumber = sheet['BG' + str(row)].value

    if not bank:
        bank = 'N/A'

    if not accountNumber:
        accountNumber = 'N/A'

    data = f"""                IMARA DAIRY FARMERS CO-OPERATIVE SOCIETY LTD\n
                TEL 0722 823 667/ 0723 688 721 / 0725 168 913\n

                MEMBER NUMBER: {number}\n
                NAME: {name}\n
                STATION: {station}\n
                TOTAL KGS: {farmerData[0]}\n
                RATE: {rate}\n
                GROSS AMOUNT: {farmerData[1]}\n
                PREVIOUS LOAN BALANCE: {farmerData[2]}\n
                MONTHLY INSTALMENT: {farmerData[3]}\n
                ACTUAL PAYMENT: {farmerData[4]}\n
                LOAN BALANCE: {farmerData[5]}\n
                STORE LOAN: {farmerData[6]}\n
                ACTUAL STORE REPAYMENT: {farmerData[7]}\n
                STORE LOAN BALANCE: {farmerData[8]}\n
                PREVIOUS SAVINGS: {farmerData[9]}\n
                MEMBER SAVINGS: {farmerData[10]}\n
                TOTAL MEMBER SAVINGS: {farmerData[11]}\n
                PREVIOUS REGISTRATION: {farmerData[12]}\n
                TOTAL REGISTRATION: {farmerData[13]}\n
                PREVIOUS SHARES: {farmerData[14]}\n
                TOTAL SHARES: {farmerData[15]}\n
                TOTAL DEDUCTIONS: {farmerData[16]}\n
                NET PAY: {farmerData[17]}\n
                BANK: {bank}\n
                ACCOUNT NUMBER: {accountNumber}\n
 """  # Do not delete the space here, it serves an important role

    with open("payslips.txt", "a") as f:
        f.write(data)

    farmerData = []  # clear the list for entry of the next farmer
