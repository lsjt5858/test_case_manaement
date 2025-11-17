# 测试用例管理平台

一个基于 FastAPI 的轻量级测试用例管理系统，提供完整的 CRUD 功能。

## 功能特性

- ✅ 创建测试用例
- ✅ 查看测试用例列表
- ✅ 查看单个测试用例详情
- ✅ 更新测试用例
- ✅ 删除测试用例
- ✅ 自动生成 API 文档（Swagger UI 和 ReDoc）
- ✅ 简单的前端示例页面

## 技术栈

- **后端框架**: FastAPI 0.104+
- **数据库**: SQLite 3
- **ORM**: SQLAlchemy 2.0+
- **数据验证**: Pydantic 2.0+
- **前端**: 原生 HTML + JavaScript

## 环境要求

- Python 3.8+
- pip 包管理器

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动服务

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 访问应用

- **前端页面**: http://localhost:8000
- **API 文档 (Swagger UI)**: http://localhost:8000/docs
- **API 文档 (ReDoc)**: http://localhost:8000/redoc

## API 端点

| 方法 | 路径 | 功能 |
|------|------|------|
| POST | /api/test-cases | 创建测试用例 |
| GET | /api/test-cases | 获取测试用例列表 |
| GET | /api/test-cases/{id} | 获取单个测试用例 |
| PUT | /api/test-cases/{id} | 更新测试用例 |
| DELETE | /api/test-cases/{id} | 删除测试用例 |

## 项目结构

```
test-case-platform/
├── app/
│   ├── __init__.py          # 应用初始化
│   ├── main.py              # FastAPI 应用入口
│   ├── models.py            # SQLAlchemy 数据模型
│   ├── schemas.py           # Pydantic 数据模式
│   ├── database.py          # 数据库连接配置
│   └── crud.py              # CRUD 操作函数
├── static/
│   └── index.html           # 前端示例页面
├── requirements.txt         # Python 依赖
├── README.md               # 项目说明文档
└── test_cases.db           # SQLite 数据库文件（运行时生成）
```

## 使用示例

### 创建测试用例

```bash
curl -X POST "http://localhost:8000/api/test-cases" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "登录功能测试",
    "description": "测试用户登录功能",
    "steps": "1. 打开登录页面\n2. 输入用户名和密码\n3. 点击登录按钮",
    "expected_result": "成功登录并跳转到首页"
  }'
```

### 获取测试用例列表

```bash
curl -X GET "http://localhost:8000/api/test-cases"
```

## 开发说明

- 数据库文件 `test_cases.db` 会在首次运行时自动创建
- 使用 `--reload` 参数启动服务可以在代码修改后自动重启
- 所有 API 都支持 CORS，方便前端开发

## 学习资源

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/)
- [Pydantic 官方文档](https://docs.pydantic.dev/)

## 许可证

MIT License
