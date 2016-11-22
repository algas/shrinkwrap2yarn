from collections import namedtuple
import logging

## Definition of YarnElement
YarnElement = namedtuple('YarnElement', 'name from_ version resolved dependencies')
## Definition of YarnDependency
YarnDependency = namedtuple('YarnDependency', 'name from_')

class YarnLock:
    def __init__(self, names, version, resolved, dependencies=[]):
        self.names = names
        self.version = version
        self.resolved = resolved
        self.dependencies = dependencies

    def __repl__(self):
        strs = [
            ', '.join(self.names) + ':',
            '  version "{0}"'.format(self.version),
            '  resolved "{0}"'.format(self.resolved)
        ]
        if len(self.dependencies) > 0:
            strs.append('  dependencies:')
            strs.extend(['    "{0}" "{1}"'.format(d.name, d.from_) for d in self.dependencies])
        return '\n'.join(strs)

    def __str__(self):
        return self.__repl__()

class YarnLockFactory:
    ## Yarn Lock Factory
    def _merge(self, yarn_elements):
        def _get_name(yarn):
            if yarn.from_ is None:
                return '"{0}@{1}"'.format(yarn.name, yarn.version)
            elif yarn.from_.startswith('git:') or yarn.from_.startswith('https:'):
                return '"{0}@{1}"'.format(yarn.name, yarn.from_)
            return '"{0}"'.format(yarn.from_)
        yarns = {}
        for yarn in yarn_elements:
            if yarn.resolved not in yarns:
                yarns[yarn.resolved] = {'names':set([_get_name(yarn)]), 'version':yarn.version, 'dependencies':yarn.dependencies}
            else:
                yarns[yarn.resolved]['names'].add(_get_name(yarn))
        return yarns

    def _locks(self, yarns):
        return [YarnLock(yarn['names'], yarn['version'], resolved, yarn['dependencies']) for resolved, yarn in yarns.items()]

    def run(self, yarn_elements):
        return sorted(self._locks(self._merge(yarn_elements)), key=lambda x:repr(x.names))
