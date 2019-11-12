#! python3
import openpyxl

wb = openpyxl.load_workbook('october.xlsx', data_only=True)
sheet = wb['MAIN']

farmerData = []

for row in range(3, 965):  # upto number of farmers
    # Each row in the spreadsheet has data for one member.
    number = sheet['A' + str(row)].value  # number
    name = sheet['B' + str(row)].value  # name
    station = sheet['C' + str(row)].value  # station
    farmerData.append(sheet['AI' + str(row)].value)  # 0 totalKgs
    rate = sheet['AJ' + str(row)].value  # rate
    farmerData.append(sheet['AK' + str(row)].value)  # 1 grossAmount
    farmerData.append(sheet['AL' + str(row)].value)  # 2 previousLoanBalance
    farmerData.append(sheet['AO' + str(row)].value)  # 3 monthlyInstalment
    farmerData.append(sheet['AP' + str(row)].value)  # 4 actualPayment
    farmerData.append(sheet['AQ' + str(row)].value)  # 5 loanBalance
    farmerData.append(sheet['AT' + str(row)].value)  # 6 storeLoan
    farmerData.append(sheet['AU' + str(row)].value)  # 7 actualStoreRepayment
    farmerData.append(sheet['AV' + str(row)].value)  # 8 storeLoanBalance
    farmerData.append(sheet['AX' + str(row)].value)  # 9 previousSavings
    farmerData.append(sheet['AY' + str(row)].value)  # 10 memberSavings
    farmerData.append(sheet['AZ' + str(row)].value)  # 11 TotalMemberSavings
    farmerData.append(sheet['BA' + str(row)].value)  # 12 previouRegistration
    farmerData.append(sheet['BB' + str(row)].value)  # 13 totalRegistration
    farmerData.append(sheet['BC' + str(row)].value)  # 14 previousShares
    farmerData.append(sheet['BD' + str(row)].value)  # 15 totalShares
    farmerData.append(sheet['AW' + str(row)].value)  # 16 totalDeductions
    farmerData.append(sheet['BE' + str(row)].value)  # 17 netPay
    bank = sheet['BF' + str(row)].value
    accountNumber = sheet['BG' + str(row)].value

    if not bank:
        bank = 'N/A'

    if not accountNumber:
        accountNumber = 'N/A'

    data = f"""
                                      IMARA DAIRY FARMERS CO-OPERATIVE SOCIETY LTD  *  TEL: 0722 823 667 / 0723 688 721 / 0725 168 913\n

            MEMBER NUMBER: {number}   *    NAME: {name}   *    STATION: {station}   *    TOTAL KGS: {farmerData[0]}   *    RATE: {rate}   *    GROSS AMOUNT: {farmerData[1]}\n
            PREVIOUS LOAN BALANCE: {farmerData[2]}   *    MONTHLY INSTALMENT: {farmerData[3]}   *    ACTUAL PAYMENT: {farmerData[4]}   *    LOAN BALANCE: {farmerData[5]}\n
            STORE LOAN: {farmerData[6]}   *    ACTUAL STORE REPAYMENT: {farmerData[7]}   *    STORE LOAN BALANCE: {farmerData[8]}   *    PREVIOUS SAVINGS: {farmerData[9]}\n
            MEMBER SAVINGS: {farmerData[10]}   *    TOTAL MEMBER SAVINGS: {farmerData[11]}   *    PREVIOUS REGISTRATION: {farmerData[12]}   *    TOTAL REGISTRATION: {farmerData[13]}\n
            PREVIOUS SHARES: {farmerData[14]}   *    TOTAL SHARES: {farmerData[15]}   *    TOTAL DEDUCTIONS: {farmerData[16]}   *    NET PAY: {farmerData[17]}\n
            BANK: {bank} |  ACCOUNT NUMBER: {accountNumber}\n

 """  # noqa # Do not delete the space here, it serves an important role

    with open("payslips.txt", "a") as f:
        f.write(data)

    farmerData = []  # clear the list for entry of the next farmer
