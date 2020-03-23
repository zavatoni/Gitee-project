#!/usr/bin/python3
from error_debug import result_debug_type
from error_debug import errors_run_log
import unittest

def raises_error(*args,**kwds):
    raise ValueError('Invalid value:{}{}'.format(args,kwds))

class ExceptionTest(unittest.TestCase):
    def test_trap_locally(self):
        try:
            raises_error('a',b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see valueError')
    def test_assert_raises(self):
        self.assertRaises(ValueError,raises_error,'a',b='c')

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(),'FOO')
    def test_isUpper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_split(self):
        print("test_split")
        s="hello world"
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)
    def test_title(self):
        string='haha'
        self.assertEqual(string.title(),'Haha')
    def test_notEqual(self):
        string='haha'
        self.assertNotEqual(string,'Haha')
    def test_isUpper(self):
        char_str='hahas'
        self.assertFalse(char_str.isupper())
    def test_isLower(self):
        test_str='haha'
        self.assertTrue(test_str.islower())
    def test_list(self):
        try:
            string=[
            'haha',
            'heihei',
            'hehe'
            ]
            str='heihei'
            self.assertIn(str,string)
        except:
            errors_run_log()
            print(result_debug_type())
    def test_notIn(self):
        try:
            string=[
            'haha',
            'heihei',
            'hehe'
            ]
            str='hoho'
            self.assertNotIn(str,string)
        except:
            errors_run_log()
            print(result_debug_type())
def main():
    unittest.main()
if __name__ == "__main__":
    main()