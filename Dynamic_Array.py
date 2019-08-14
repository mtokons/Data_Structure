class M(object):
    def public(self):
        print('use tab to see me')

    def _private(self):
        print('you can\'t see me by tab')

m = M()
m.public()
m._private()