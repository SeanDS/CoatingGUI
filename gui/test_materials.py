#!/usr/bin/env python
# This work is licensed under the Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative
# Commons, PO Box 1866, Mountain View, CA 94042, USA.

import materials as mat
import unittest

class TestMaterials(unittest.TestCase):
    """Testing the Materials module"""

    def test_material(self):
        m = mat.Material(n=1.44)
        self.assertEqual(m.n(1), 1.44)
        m2 = mat.Material(n=3.0)
        self.assertEqual(m.n(1), 1.44)
        self.assertEqual(m2.n(1), 3.0)

    def test_material_library(self):
        m = mat.Material(name='TestMaterial', n=1.44)
        ml = mat.MaterialLibrary.Instance()
        self.assertTrue('TestMaterial' in ml.list_materials())
        self.assertEqual(ml.get_material('TestMaterial').n(1), 1.44)
        self.assertEqual(ml.get_material(3.0).n(1), 3.0)
        self.assertRaises(mat.MaterialNotDefined, ml.get_material, 'UndefinedMaterial')
        with self.assertRaises(mat.MaterialAlreadyDefined):
            m2 = mat.Material(name='TestMaterial')

if __name__ == '__main__':
    unittest.main()
