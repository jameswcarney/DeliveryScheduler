#  Package class describes a package to be delivered
class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes, status):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.weight, self.notes, self.status)


class Truck:
    def __init__(self):
        self.packages = None

    def add_package(self, package):
        if self.packages is None:
            self.packages = []
        self.packages.append(package)

    def nearest_neighbor(self, packages):
        pass

