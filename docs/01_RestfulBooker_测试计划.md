# Restful-Booker 接口测试计划

## 一、测试对象
Restful-Booker 示例 API 服务 (https://restful-booker.herokuapp.com)

## 二、测试范围
- Auth 接口：创建 Token
- Booking 接口：查询、创建、更新、删除
- 正常功能、异常输入、鉴权校验

## 三、不测试范围
- 性能测试（仅 JMeter 简单验证）
- 安全性深入渗透测试
- 第三方集成

## 四、测试环境
- 公共测试环境（Heroku 部署）
- 或本地 Mock 环境（可选）

## 五、测试类型
- 功能测试
- 接口测试
- 异常场景测试
- 自动化回归测试

## 六、风险点
- 公共测试环境数据不稳定
- 网络超时
- 接口限流或变更

## 七、交付物
- 测试用例文档
- pytest 自动化脚本
- Allure 报告截图
- Postman 集合
- 缺陷记录样例
