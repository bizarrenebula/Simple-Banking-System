class Bank:

    name = 'International Bank'
    clients = []

    def update_db(self, client):
        self.clients.append(client)

    def verification(self, name, acc_num):
        for i in range(len(self.clients)):
            if name == self.clients[i].name and acc_num == self.clients[i].acc_number:
                return self.clients[i]
