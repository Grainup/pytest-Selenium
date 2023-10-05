# 测试框架的运行入口

import subprocess


def main():
    """主函数"""
    steps = [

        "pytest -sv --alluredir reports/allure-results --clean-alluredir",
        "allure generate reports/allure-results -c -o reports/allure-report",
        "allure open reports/allure-report"
    ]
    for step in steps:
        subprocess.run("call " + step, shell=True)


if __name__ == "__main__":
    main()
