import json
from shrinkwrap2yarn import yarn

class ShrinkwrapParser:
    def __init__(self):
        self.factory = yarn.YarnLockFactory()

    def parse(self, file_path):
        with open(file_path) as fp:
            data = json.load(fp)
            return self._parse(data)

    def _parse(self, data, yarns=[]):
        name = data.get('name', None)
        from_ = data.get('from', None)
        version = data.get('version', None)
        resolved = data.get('resolved', None)
        dependencies, yarns = self._dependencies(data, yarns)
        yarns.append(yarn.YarnElement(name, from_, version, resolved, dependencies))
        return yarns

    def _dependencies(self, data, yarns):
        def _from(val):
            return val.get('from', val.get('version', None))
        dependencies = []
        if 'dependencies' in data and len(data['dependencies']) > 0:
            for k, v in data['dependencies'].items():
                v['name'] = k
                yarns = self._parse(v, yarns)
                dependencies.append(yarn.YarnDependency(k, _from(v), v.get('version', None)))
        return dependencies, yarns

    def print_yarn(self, parsed):
        [print(m) for m in self.factory.run(parsed)]
