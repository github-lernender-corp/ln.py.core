def repr_toString(cls):
    def __str__(self):
        return '%s\n\t%s\n' % (
            type(self).__name__,
            '\n\t'.join('[%s]: %s' % item for item in vars(self).items())
        )
    cls.__str__ = __str__
    return cls
