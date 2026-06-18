# OpenCart 电商系统 Web 自动化回归测试

## 一、项目简介

本项目基于 OpenCart 官方 Demo 前台，完成 Web UI 自动化回归测试实践。

项目目标是展示软件测试工程师 / 测试开发工程师岗位所需的基础能力，包括：

- Web 功能测试分析
- 测试用例设计
- Selenium 自动化脚本编写
- pytest 测试执行
- Page Object 模式封装
- Allure 测试报告生成
- 失败截图与问题定位
- Git / GitHub SSH 项目管理

## 二、技术栈

- Python
- Selenium
- pytest
- Page Object
- Allure
- YAML
- Git
- GitHub SSH

## 三、运行环境

- Windows WSL2
- Ubuntu
- Linux Google Chrome Headless

## 四、测试范围

本项目覆盖以下功能：

1. 首页访问
2. 登录页表单校验
3. 错误账号登录校验
4. 商品搜索
5. 商品详情页校验
6. 加入购物车
7. 购物车页面校验

其中，购物车用例依赖公开 Demo 环境的 session 和页面状态，因此标记为 optional。

## 五、项目结构

```text
opencart-web-ui-tests/
├── config/
├── pages/
├── tests/
├── docs/
├── reports/
├── screenshots/
├── images/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

## 六、如何运行
### 1. 创建虚拟环境

```bash
python3 -m venv .venv
```

### 2. 激活虚拟环境

```bash
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行核心测试

```bash
pytest -m "not optional"
```

### 5. 生成 Allure 测试结果

```bash
pytest -m "not optional" --alluredir=reports/allure-results
```

### 6. 生成 Allure HTML 报告

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

### 7. 本地查看 Allure 报告

```bash
cd reports/allure-report
python3 -m http.server 8000
```

然后在 Windows 浏览器访问：

```text
http://127.0.0.1:8000

## 七、测试文档
docs/01_测试计划.md
    
- docs/02_测试用例.md
    
- docs/03_缺陷记录样例.md
    
- docs/04_环境搭建记录.md
    
- docs/05_面试讲解稿.md

## 八、项目说明
本项目最初尝试使用 Windows WSL2 + Docker Desktop 本地部署 OpenCart，但遇到端口映射、数据库初始化和模板加载问题。为保证项目目标聚焦于 Web 自动化测试实践，最终使用 TutorialsNinja Opencart Demo环境作为被测系统。。

该处理方式体现了测试工作中的问题定位、风险记录和优先级取舍。 
