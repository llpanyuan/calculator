import pytest
import yaml

from python_code.calc import Calc


# 获取测试数据
def get_data():
    test_data = yaml.safe_load(open("data/test_data.yml"))
    return test_data


# 获取测试步骤
def get_steps():
    with open('steps/test_steps.yml', encoding="utf-8") as f:
        return yaml.safe_load(f)


# 使用 fixture 装置进行计算机器实例的初始化
@pytest.fixture(scope='module', autouse=True)
def initialization():
    print("测试开始")
    calc = Calc()
    yield calc
    print("测试结束")


# 测试类
class TestCalc:
    # # sepup初始化
    # def setup_class(self):
    #     print("Test start!")
    #     self.calc = Calc()
    #
    # # teardown 结束处理
    # def teardown_class(self):
    #     print("\nTest finished!")

    # 参数化用例，获取测试数据
    @pytest.mark.parametrize('a,b,result', get_data()["add"])
    # 获取测试步骤
    @pytest.mark.parametrize('steps', get_steps()["add"])
    # @pytest.mark.run(order=3)
    # 加法测试
    # 改造 pytest 的运行规则 ,测试用例命名以  `calc_`  开始，【加， 减 ，乘，除】分别为 calc_add, calc_sub，…
    def calc_add(self, a, b, result, steps, initialization):
        self.adding_steps(a, b, result, steps, initialization)

    # 测试步骤
    def adding_steps(self, a, b, result, steps, initialization):
        for step in steps:
            if 'add' == step:
                print(f"step is {step}")
                assert initialization.add(a, b) == result
            else:
                raise NameError

    # 参数化用例，获取测试数据
    @pytest.mark.parametrize('a,b,result', get_data()["sub"])
    # 获取测试步骤
    @pytest.mark.parametrize('steps', get_steps()['sub'])
    # @pytest.mark.run(order=-1)
    # 减法测试
    def calc_sub(self, a, b, result, steps, initialization):
        # assert initialization.sub(a, b) == result
        self.sub_steps(a, b, result, steps, initialization)

    # 测试步骤驱动测试
    def sub_steps(self, a, b, result, steps, initialization):
        for step in steps:
            if 'sub' == step:
                assert initialization.sub(a, b) == result
            else:
                raise NameError

    # 参数化用例，获取测试数据
    @pytest.mark.parametrize('a,b,result', get_data()["mul"])
    # 获取测试步骤
    @pytest.mark.parametrize('steps', get_steps()["mul"])
    # @pytest.mark.run(order=2)
    # 乘法测试
    def calc_mul(self, a, b, result, steps, initialization):
        self.mul_steps(a, b, result, steps, initialization)

    # 测试步骤驱动测试
    def mul_steps(self, a, b, result, steps, initialization):
        for step in steps:
            if 'mul' == step:
                assert initialization.mul(a, b) == result
            else:
                raise NameError

    # 参数化用例，获取测试数据
    @pytest.mark.parametrize('a,b,result', get_data()["div"])
    # 获取测试步骤
    @pytest.mark.parametrize('steps', get_steps()["div"])
    # @pytest.mark.run(order=1)
    # 除法测试
    def calc_div(self, a, b, result, steps, initialization):
        self.div_steps(a, b, result, steps, initialization)

    # 测试步骤驱动测试
    def div_steps(self, a, b, result, steps, initialization):
        for step in steps:
            if 'div' == step:
                print(f"step is {step}")
                assert initialization.div(a, b) == result
            else:
                raise NameError


# 入口函数
if __name__ == '__main__':
    pytest.main()
