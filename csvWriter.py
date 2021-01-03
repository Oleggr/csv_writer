import csv
from datetime import datetime, timedelta


class CsvWriter:

    payments_filename = 'payments.csv'
    events_log = 'events.log'
    messages_log = 'messages.log'

    def writePayment(self, name, tg_id, amount):
        with open(self.payments_filename, 'a', newline='') as file:
            payment = [
                name,
                tg_id,
                CsvWriter.getCurrTimestamp(),
                amount
            ]
            writer = csv.writer(file)
            writer.writerow(payment)
            self.writeLog(payment, self.events_log)

    def getPaymentsCount(self, tg_id):
        with open(self.payments_filename, newline='') as file:
            reader = csv.reader(file)
            return len(list(filter(lambda x: x[1] == str(tg_id), reader)))

    def getTotalMonthsPayments(self):
        payments_total = 0

        with open(self.payments_filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[2]) > (datetime.now() - timedelta(days=30)).timestamp():
                    payments_total += int(row[3])

        return payments_total

    def writeLog(self, event, filename):
        with open(filename, 'a', encoding='utf-8') as file:
            message = str(datetime.fromtimestamp(event[2])) \
                    + ' :: ' \
                    + str(event[0]) \
                    + ' (' \
                    + str(event[1]) \
                    + ') | ' \
                    + str(event[3])
            file.write(message + '\n')

    @staticmethod
    def getCurrTimestamp():
        return int(datetime.now().timestamp())
