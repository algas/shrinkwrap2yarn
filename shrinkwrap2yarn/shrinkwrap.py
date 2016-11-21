from collections import namedtuple

## Definition of YarnElement
YarnElement = namedtuple('YarnElement', 'name version resolved dependencies')


class YarnFactory:
    def _merge(self, yarn_elements):
        yarns = {}
        for yarn in yarn_elements:
            if yarn.resolved not in yarns:
                yarns[yarn.resolved] = {'names':[yarn.name], 'version':yarn.version, 'dependencies'=[]}
            else:
                yarns[yarn.resolved]['names'].append(yarn.name)
        return yarns

    def _str_yarns(self, yarns):
        for yarn in yarns:
            print ', '.joins('"{0}"'.format(n) for n in yarn.names)
            print '  version {0}'.format(yarn.version)
            print '  resolved {0}'.format(yarn.resolved)
            if yarn.dependencies and len(yarn.dependencies) > 0:
                print '  dependencies:'
                for d in yarn.dependencies:
                    print '    {0}'.format(d)


    def merge(self, yarn_elements):
        return self._str_yarns(elf._merge(yarn_elements))
