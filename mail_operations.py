class MailOperations:
    def __init__(self):
        pass

    def send(self):
        print('send')

    def read(self):
        print('read')

    def delete(self):
        print('delete')


mail_operations = MailOperations()

mail_operations.send()
mail_operations.read()
mail_operations.delete()