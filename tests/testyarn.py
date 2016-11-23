import unittest
from shrinkwrap2yarn.yarn import YarnLock

class TestStringMethods(unittest.TestCase):
    def test_elements_with_resolved(self):
        names = ['package-example']
        version = '0.0.1'
        resolved = 'https://registry.npmjs.org/package-example/-/package-example-0.0.1.tgz'
        dependencies = []
        yarnLock = YarnLock(names, version, resolved, dependencies)
        self.assertEqual(yarnLock.names, names)
        self.assertEqual(yarnLock.version, version)
        self.assertEqual(yarnLock.resolved, 'https://registry.yarnpkg.com/package-example/-/package-example-0.0.1.tgz')
        self.assertEqual(yarnLock.dependencies, dependencies)


if __name__ == '__main__':
    unittest.main()
