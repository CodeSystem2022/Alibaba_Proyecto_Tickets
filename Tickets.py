class Tickets:

    def __init__(self, id_ticket=None, ticket=None, vendido=None, verificado=None):
        self._id_ticket = id_ticket
        self._ticket = ticket
        self._vendido = vendido
        self._verificado = verificado

    def __str__(self):
        return f'Ticket: {self._id_ticket} {self._ticket} {self._vendido} {self._verificado}'

    @property
    def id_ticket(self):
        return self._id_ticket

    @id_ticket.setter
    def id_ticket(self, id_ticket):
        self._id_ticket = id_ticket

    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        self._ticket = ticket

    @property
    def vendido(self):
        return self._vendido
    @vendido.setter
    def vendido(self, vendido):
        self._vendido = vendido

    @property
    def verificado(self):
        return self._verificado

    @verificado.setter
    def verificado(self, verificado):
        self._verificado = verificado
