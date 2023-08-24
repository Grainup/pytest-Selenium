# 测试框架的运行入口

import sys
import subprocess

# WIN = sys.platform.startswith('win')


def main():
    """主函数"""
    steps = [
        # "venv\\Script\\activate" if WIN else "source venv/bin/activate",
        "pytest -sv --alluredir reports/allure-results --clean-alluredir",
        "allure generate reports/allure-results -c -o reports/allure-report",
        "allure open reports/allure-report"
    ]
    for step in steps:
        subprocess.run("call " + step, shell=True)


if __name__ == "__main__":
    main()
