# 实施计划

## 任务清单

- [x] 1. 创建项目基础结构和配置文件
  - 创建项目目录结构（app/, static/）
  - 创建 requirements.txt 文件，包含 FastAPI、SQLAlchemy、uvicorn 等依赖
  - 创建 README.md 文件，包含项目说明和启动步骤
  - 创建 app/__init__.py 空文件
  - _需求: 6.1, 6.2, 6.3, 6.4_

- [x] 2. 实现数据库配置和连接管理
  - 在 app/database.py 中配置 SQLite 数据库连接字符串
  - 创建 SQLAlchemy engine 和 SessionLocal 会话工厂
  - 实现 get_db() 依赖注入函数，用于提供数据库会话
  - 创建 Base 声明式基类
  - _需求: 1.1, 1.4_

- [x] 3. 定义测试用例数据模型
  - 在 app/models.py 中创建 TestCase 模型类
  - 定义所有字段：id（主键）、title、description、steps、expected_result、status
  - 添加时间戳字段：created_at、updated_at，设置自动更新
  - 配置表名为 "test_cases"
  - _需求: 1.1, 1.4, 1.5, 4.4_

- [x] 4. 创建 Pydantic 数据验证模式
  - 在 app/schemas.py 中创建 TestCaseBase 基础模式
  - 实现 TestCaseCreate 模式，用于创建请求，包含必填字段验证（title 1-200 字符）
  - 实现 TestCaseUpdate 模式，用于更新请求，所有字段可选
  - 实现 TestCaseResponse 模式，用于响应，包含 id 和时间戳字段
  - _需求: 1.2, 4.5_

- [x] 5. 实现 CRUD 数据库操作函数
  - 在 app/crud.py 中实现 create_test_case() 函数，创建新测试用例并设置时间戳
  - 实现 get_test_cases() 函数，获取测试用例列表，按创建时间降序排序，支持分页
  - 实现 get_test_case() 函数，根据 ID 获取单个测试用例
  - 实现 update_test_case() 函数，更新测试用例并自动更新 updated_at
  - 实现 delete_test_case() 函数，删除测试用例
  - _需求: 1.1, 1.5, 2.1, 2.4, 3.1, 4.1, 4.4, 5.1_

- [x] 6. 创建 FastAPI 应用和配置中间件
  - 在 app/main.py 中创建 FastAPI 应用实例
  - 配置 CORS 中间件，允许所有源访问（开发环境）
  - 挂载静态文件目录 /static
  - 在应用启动时创建数据库表
  - _需求: 6.1, 6.2, 7.1, 7.2, 7.3_

- [x] 7. 实现创建测试用例 API 端点
  - 在 app/main.py 中实现 POST /api/test-cases 端点
  - 使用 TestCaseCreate 模式验证请求数据
  - 调用 create_test_case() 创建记录
  - 返回 201 状态码和新创建的测试用例数据
  - 处理验证错误，返回 422 状态码
  - _需求: 1.1, 1.2, 1.3, 1.4, 1.5_

- [x] 8. 实现获取测试用例列表 API 端点
  - 在 app/main.py 中实现 GET /api/test-cases 端点
  - 调用 get_test_cases() 获取所有测试用例
  - 返回 200 状态码和测试用例数组
  - 处理空列表情况
  - _需求: 2.1, 2.2, 2.3, 2.4_

- [x] 9. 实现获取单个测试用例 API 端点
  - 在 app/main.py 中实现 GET /api/test-cases/{id} 端点
  - 调用 get_test_case() 根据 ID 查询
  - 返回 200 状态码和测试用例详情
  - 处理不存在的情况，返回 404 状态码和错误消息
  - _需求: 3.1, 3.2, 3.3_

- [x] 10. 实现更新测试用例 API 端点
  - 在 app/main.py 中实现 PUT /api/test-cases/{id} 端点
  - 使用 TestCaseUpdate 模式验证请求数据
  - 调用 update_test_case() 更新记录
  - 返回 200 状态码和更新后的数据
  - 处理不存在的情况，返回 404 状态码
  - 处理验证错误，返回 422 状态码
  - _需求: 4.1, 4.2, 4.3, 4.4, 4.5_

- [x] 11. 实现删除测试用例 API 端点
  - 在 app/main.py 中实现 DELETE /api/test-cases/{id} 端点
  - 调用 delete_test_case() 删除记录
  - 返回 204 状态码（无内容）
  - 处理不存在的情况，返回 404 状态码和错误消息
  - _需求: 5.1, 5.2, 5.3_

- [x] 12. 创建前端示例页面
  - 在 static/index.html 中创建 HTML 页面结构
  - 添加创建测试用例的表单（标题、描述、步骤、预期结果）
  - 添加测试用例列表展示区域
  - 实现基本的 CSS 样式，使页面美观易用
  - _需求: 8.1_

- [x] 13. 实现前端创建测试用例功能
  - 在 static/index.html 中使用 Fetch API 调用 POST /api/test-cases
  - 获取表单数据并构造 JSON 请求体
  - 处理成功响应，清空表单并刷新列表
  - 处理错误响应，显示错误提示
  - _需求: 8.2_

- [x] 14. 实现前端列表和显示功能
  - 在 static/index.html 中使用 Fetch API 调用 GET /api/test-cases
  - 动态渲染测试用例列表到页面
  - 显示每个测试用例的所有字段信息
  - 为每个测试用例添加编辑和删除按钮
  - _需求: 8.3_

- [x] 15. 实现前端更新和删除功能
  - 实现编辑按钮点击事件，填充表单数据
  - 使用 Fetch API 调用 PUT /api/test-cases/{id} 更新测试用例
  - 实现删除按钮点击事件，添加确认提示
  - 使用 Fetch API 调用 DELETE /api/test-cases/{id} 删除测试用例
  - 更新或删除后刷新列表
  - _需求: 8.4_

- [x] 16. 验证和测试完整功能
  - 启动 FastAPI 服务器（uvicorn app.main:app --reload）
  - 访问 Swagger UI 文档（http://localhost:8000/docs）测试所有 API 端点
  - 访问前端页面（http://localhost:8000/static/index.html）测试完整用户流程
  - 验证所有 CRUD 操作正常工作
  - 验证错误处理（404、422 等）
  - 使用浏览器开发者工具检查网络请求和响应
  - _需求: 1.1, 1.2, 1.3, 2.1, 2.3, 3.1, 3.2, 4.1, 4.2, 4.5, 5.1, 5.2, 6.1, 6.2, 6.3, 6.4_
