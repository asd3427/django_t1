import unittest


def add(a, b):
    a+1
    return a + b


def test_add():
    a = 1
    for b in range(6):
        result = add(a, b)
        if a + b != result:
            print(f"测试失败！函数执行有错误:a={a},b={b},result={result}")
            break
    else:
        print("测试通过")

# 用单元测试模块 做测试
class TestCase(unittest.TestCase):
    def test_add(self):
        a = 1
        for b in range(6):
            result = add(a, b)
            self.assertEqual(a + b, result)


if __name__ == "__main__":
    test_add()
    unittest.main()
