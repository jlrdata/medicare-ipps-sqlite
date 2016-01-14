# Define functions for file I/O.

import csv

def readIPPSFile(fn):
    """Read IPPS CSV file.

    Arguments:
    fn (string) -- name of IPPS data file

    Returns:
    List of tuples (each tuple is a row of data)
    """
    allRows = []
    i = 0
    f = open(fn, 'rb')
    csvData = csv.reader(f, delimiter=',', quotechar='"')
    for row in csvData:
        # Skip first row (contains column names) and empty rows
        if i != 0 and len(row[0]) != 0:
            f0 = row[0]           # drgDefinition
            f1 = int(row[1])      # providerId
            f2 = row[2]           # providerName
            f3 = row[3]           # providerStreetAddress
            f4 = row[4]           # providerCity
            f5 = row[5]           # providerState
            f6 = int(row[6])      # providerZipCode
            f7 = row[7]           # hrrDescription
            f8 = int(row[8])      # totalDischarges
            f9 = float(row[9])    # avgCoveredCharges
            f10 = float(row[10])  # avgTotalPayments
            f11 = float(row[11])  # avgMedicarePayments
            f12 = f10-f11         # avgNonMedicarePayments
            f13 = f9-f10          # avgCoveredChargesMinusTotalPayments
            t = (f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13)
            allRows.append(t)
        i += 1
    f.close()
    return allRows

def readUSDARestaurantsFile(fn):
    """Read USDA Restaurants CSV file.

    Arguments:
    fn (string) = name of USDA restaurants data file

    Returns:
    List of tuples (each tuple is a row of data)
    """
    allRows = []
    i = 0
    f = open(fn, 'rb')
    csvData = csv.reader(f, delimiter=',', quotechar='"')
    for row in csvData:
        # Skip rows that contain any empty fields
        containsEmptyField = False
        for r in range(len(row)):
            if len(row[r]) == 0:
                containsEmptyField = True
        if containsEmptyField:
            continue
        # Skip first row (contains column names) and empty rows
        if i != 0 and len(row[0]) != 0:
            f0 = row[0]           # fips
            f1 = row[1]           # state
            f2 = row[2]           # county
            f3 = int(row[3])      # ffr07
            f4 = int(row[4])      # ffr12
            f5 = float(row[5])    # pch_ffr_07_12
            f6 = float(row[6])    # ffrpth07
            f7 = float(row[7])    # ffrpth12
            f8 = float(row[8])    # pch_ffrpth_07_12
            f9 = int(row[9])      # fsr07
            f10 = int(row[10])    # fsr12
            f11 = float(row[11])  # pch_fsr_07_12
            f12 = float(row[12])  # fsrpth07
            f13 = float(row[13])  # fsrpth12
            f14 = float(row[14])  # pch_fsrpth_07_12
            f15 = float(row[15])  # pc_ffrsales02
            f16 = float(row[16])  # pc_ffrsales07
            f17 = float(row[17])  # pc_fsrsales02
            f18 = float(row[18])  # pc_fsrsales07
            t = (f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,
                 f11, f12, f13, f14, f15, f16, f17, f18)
            allRows.append(t)
        i += 1
    f.close()
    return allRows

