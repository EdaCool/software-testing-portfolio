# OpenCart Web 自动化回归测试计划

## 一、测试对象
OpenCart 电商系统（本地 Docker 部署，http://localhost失败 opencart官方demo也失败 改成TutorialsNinjaOpencart Demo）

## 二、测试范围
- 首页加载
- 商品搜索与结果校验
- 商品详情页信息展示
- 加入购物车功能
- 购物车页面商品校验

## 三、不测试范围
- 用户注册/登录功能（若未启用）
- 后台管理功能
- 支付流程

## 四、测试环境
- Windows 10 + WSL2 + Docker Desktop
- TutorialsNinjaOpencart Demo(https://tutorialsninja.com/demo/)
- 浏览器：Chrome（最新稳定版）
- Selenium + pytest

## 五、测试类型
- 功能测试
- Web UI 回归测试
- 异常场景测试（元素缺失等）
- 自动化回归测试

## 六、风险点
- UI 元素变化导致定位失败
- 网络延迟影响等待时间
- 测试数据污染
- Docker 容器不稳定

## 七、交付物
- 测试用例文档
- Selenium + Page Object 自动化脚本
- Allure 报告截图
- 缺陷记录样例
