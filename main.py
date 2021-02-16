import csv
import dataclasses

def readInput(path):
    stockRecords = list()
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) # skip header
        for row in reader:
            sequence = int(row[0])
            group = row[1]
            subCategory = row[2]
            stock = row[3]
            description = row[4]
            package = row[5]
            # onHand may be blank
            onHand = 0
            try:
                onHand = int(row[6])
            except ValueError:
                pass
            shelfLife = row[7]
            arriveDate = row[8]
            lotNumber = row[9]
            stockRecord = Stock(sequence, group, subCategory, stock, description, package, onHand, shelfLife, arriveDate, lotNumber)
            stockRecords.append(stockRecord)
    return stockRecords

def readInvoice(path):
    stockRecords = list()
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) # skip header
        for row in reader:
            sequence = 0
            group = ''
            subCategory = ''
            stock = row[0]
            description = row[1]
            package = int(row[2])
            onHand = int(row[3])
            shelfLife = row[4]
            arriveDate = row[5]
            lotNumber = row[6]
            stockRecord = Stock(sequence, group, subCategory, stock, description, package, onHand, shelfLife, arriveDate, lotNumber)
            stockRecords.append(stockRecord)
    return stockRecords

def saveRecords(records, path):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['sequence', 'group', 'subCategory', 'stock', 'description', 'package', 'onHand', 'shelfLife', 'arriveDate', 'lotNumber']
        writer.writerow(header)
        for record in records:
            row = [record.sequeuce, record.group, record.subCategory, record.stock, record.description, record.package, record.onHand, record.shelfLife, record.arriveDate, record.lotNumber]
            writer.writerow(row)

@dataclasses.dataclass
class Stock:
    sequeuce: int
    group: str
    subCategory: str
    stock: str
    description: str
    package: str
    onHand: int
    shelfLife: str
    arriveDate: str
    lotNumber: str

if __name__ == '__main__':
    records = list()
    records += readInput('data/Jointlist.csv')
    # print(len(records))
    records += readInvoice('data/invoice.csv')
    # print(len(records))
    records.sort(key=lambda st:st.stock)
    saveRecords(records, 'data/output.csv')
