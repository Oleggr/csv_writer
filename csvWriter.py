import csv
from datetime import datetime, timedelta


class csvWriter:

    debts_filename = 'debts.csv'
    payments_filename = 'payments.csv'

    def writePayment(self, name, tg_id, amount):
        with open(self.payments_filename, 'a', newline='') as file:
            payment = [
                name,
                tg_id,
                int(datetime.now().timestamp()),
                amount
            ]
            writer = csv.writer(file)
            writer.writerow(payment)

    def getPaymentsCount(self, tg_id):
        with open(self.payments_filename, newline='') as file:
            reader = csv.reader(file)
            return len(list(filter(lambda x: x[1] == str(tg_id), reader)))

    def writeDebt(self, name, tg_id, amount):
        with open(self.debts_filename, 'a', newline='') as file:
            debt = [
                name,
                tg_id,
                int(datetime.now().timestamp()),
                amount
            ]
            writer = csv.writer(file)
            writer.writerow(debt)

    def getTotalMonthsPayments(self):
        payments_total = 0

        with open(self.payments_filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[2]) < (datetime.now() - timedelta(days=30)).timestamp():
                    payments_total += row[3]

        return payments_total

