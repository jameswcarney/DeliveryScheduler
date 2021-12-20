"""
A class representing packages that will be delivered
"""
class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes, delivery_time, location, status):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.delivery_time = None
        self.location = ''
        self.status = 'Hub'

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                           self.deadline, self.weight, self.notes,
                                                           self.delivery_time, self.status)
