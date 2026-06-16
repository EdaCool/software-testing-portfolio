| 模块         | 用例                 | 预期                        |
| ---------- | ------------------ | ------------------------- |
| Auth       | 正确用户名密码获取 token    | 返回 200，包含 token           |
| Auth       | 错误密码获取 token       | 返回 Bad credentials        |
| Booking 查询 | 获取 booking id 列表   | 返回数组                      |
| Booking 查询 | 根据有效 id 查询详情       | 返回 firstname、lastname 等字段 |
| Booking 查询 | 查询不存在 id           | 返回 404                    |
| Booking 创建 | 合法参数创建 booking     | 返回 200，包含 bookingid       |
| Booking 创建 | 缺少 firstname       | 记录实际返回，判断是否为缺陷或接口约束       |
| Booking 更新 | 有 token 更新 booking | 返回 200，字段更新成功             |
| Booking 更新 | 无 token 更新 booking | 返回 403                    |
| Booking 删除 | 有 token 删除 booking | 删除后再次查询返回 404             |

