# OpenCart 本地 Docker 环境搭建记录

## 环境

- Windows + WSL2
- Docker Desktop
- OpenCart
- MariaDB
- Apache / PHP-FPM

## 问题 1：Docker 端口发布失败

最初执行 `make up` 时，MySQL 容器启动失败，错误为：

`ports are not available: exposing port TCP 0.0.0.0:3306`

排查后判断是 Windows / WSL2 环境下 Docker Desktop 端口转发异常或宿主机端口冲突。处理方式是：

1. 将 MySQL 宿主机暴露端口从 3306 改为 3307；
2. 将 Web 服务端口改为 8081；
3. 只暴露 Apache 端口，MySQL 和 PHP-FPM 保留在 Docker 内部网络中。

## 问题 2：数据库表未初始化

容器启动成功后，访问 `http://127.0.0.1:8081/` 出现：

`Table 'opencart.oc_store' doesn't exist`

排查后发现：

1. Apache、PHP、MySQL 容器均正常启动；
2. PHP 可以连接 MySQL；
3. 但 OpenCart 数据库表未创建；
4. 手动执行 `install/cli_install.php` 后，数据库初始化成功，生成 168 张表，并出现 `oc_store` 表。

## 问题 3：模板加载异常

数据库初始化成功后，访问前台页面出现：

`Unable to find template "catalog/view/template/common/footer.twig"`

排查后判断：Docker、端口、数据库连接、数据库初始化均已通过，问题发生在 OpenCart 当前代码分支的应用模板加载逻辑。

## 问题 4：切换 release 分支后缺少 Makefile

尝试切换到 OpenCart 4.1.0.3 release 后，执行 `make init` 出现：

`make: *** No rule to make target 'init'. Stop.`

说明该 release tag 下没有 master 分支中的本地 Docker Makefile 脚手架。

## 处理决策

本项目目标是完成 Web UI 自动化测试实践，而不是修复 OpenCart 本地部署问题。因此，在记录完整环境排查过程后，Web 自动化测试切换为 OpenCart 官方 Demo 环境执行。

该决策保证了测试项目可以继续推进，同时保留了环境问题定位过程，便于面试时说明测试环境搭建、问题定位和风险取舍能力。

