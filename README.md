# 测试用例管理平台 🚀

一个基于 FastAPI 的现代化测试用例管理系统，提供完整的 CRUD 功能和友好的 Web 界面。

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-orange.svg)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 快速导航

| 角色 | 推荐阅读 |
|------|--------|
| 🟢 **初学者** | [快速开始](#快速开始) → [基础概念](#基础概念) → [简单示例](#简单示例) |
| 🟡 **中级开发者** | [API 文档](#api-文档) → [项目结构](#项目结构) → [开发指南](#开发指南) |
| 🔴 **高级开发者** | [技术架构](#技术架构) → [代码详解](#代码详解) → [扩展建议](#扩展建议) |

---

## ✨ 功能特性

### 核心功能
- ✅ **完整的 CRUD 操作** - 创建、读取、更新、删除测试用例
- ✅ **RESTful API** - 符合 REST 规范的 API 设计
- ✅ **自动数据验证** - 使用 Pydantic 进行请求数据验证
- ✅ **交互式 API 文档** - 自动生成 Swagger UI 和 ReDoc 文档
- ✅ **Web 前端界面** - 简洁易用的测试用例管理界面
- ✅ **时间戳管理** - 自动记录创建和更新时间
- ✅ **错误处理** - 完善的 HTTP 状态码和错误信息
- ✅ **CORS 支持** - 支持跨域请求，方便前后端分离开发

### 适用场景
- 📝 软件测试团队的测试用例管理
- 🎓 学习 FastAPI 和 RESTful API 开发
- 🔧 快速搭建测试管理系统原型
- 📚 作为 Web 开发教学示例

---

## 🏗️ 技术架构

### 后端技术栈

| 组件 | 技术 | 版本 | 说明 |
|------|------|------|------|
| **Web 框架** | FastAPI | 0.104+ | 高性能 Python Web 框架，自动生成 API 文档 |
| **数据库** | SQLite | 3 | 轻量级关系型数据库，无需额外配置 |
| **ORM** | SQLAlchemy | 2.0+ | Python ORM 框架，提供数据库抽象层 |
| **数据验证** | Pydantic | 2.0+ | 数据验证和序列化库，自动类型检查 |
| **服务器** | Uvicorn | 0.24+ | ASGI 服务器，支持异步处理 |

### 前端技术栈（React 版本）
- **React 18** - 现代化前端框架
- **Vite** - 快速构建工具
- **Axios** - HTTP 请求库

### 前端技术栈（原生版本）
- **HTML5** - 页面结构
- **CSS3** - 样式美化
- **JavaScript (原生)** - 交互逻辑，无需框架依赖

### 架构图

```
┌─────────────────────────────────────────────────────────┐
│                    浏览器 (前端)                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  HTML + CSS + JavaScript                         │  │
│  │  - 创建/编辑/删除测试用例表单                      │  │
│  │  - 测试用例列表展示                               │  │
│  │  - 实时交互和验证                                 │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↕ HTTP/REST
┌─────────────────────────────────────────────────────────┐
│                  FastAPI 服务器 (后端)                   │
│  ┌──────────────────────────────────────────────────┐  │
│  │  路由层 (main.py)                                │  │
│  │  - POST /api/test-cases (创建)                   │  │
│  │  - GET /api/test-cases (列表)                    │  │
│  │  - GET /api/test-cases/{id} (详情)               │  │
│  │  - PUT /api/test-cases/{id} (更新)               │  │
│  │  - DELETE /api/test-cases/{id} (删除)            │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  业务逻辑层 (crud.py)                            │  │
│  │  - 数据库操作封装                                 │  │
│  │  - 业务规则实现                                   │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  数据验证层 (schemas.py)                         │  │
│  │  - Pydantic 模型定义                             │  │
│  │  - 自动数据验证和转换                             │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  数据模型层 (models.py)                          │  │
│  │  - SQLAlchemy ORM 模型                           │  │
│  │  - 数据库表定义                                   │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↕ SQL
┌─────────────────────────────────────────────────────────┐
│                   SQLite 数据库                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  test_cases 表                                   │  │
│  │  - id (主键)                                     │  │
│  │  - title (标题)                                  │  │
│  │  - description (描述)                            │  │
│  │  - steps (步骤)                                  │  │
│  │  - expected_result (预期结果)                    │  │
│  │  - status (状态)                                 │  │
│  │  - created_at (创建时间)                         │  │
│  │  - updated_at (更新时间)                         │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 快速开始

### 环境要求

- **Python 3.8+** - [下载 Python](https://www.python.org/downloads/)
- **pip** - Python 包管理器（通常随 Python 一起安装）
- **Git** (可选) - 版本控制工具

### 第一步：克隆或下载项目

```bash
# 使用 Git 克隆
git clone <项目地址>
cd test-case-platform

# 或者直接下载 ZIP 文件并解压
```

### 第二步：创建虚拟环境（推荐）

虚拟环境可以隔离项目依赖，避免与系统其他项目冲突。

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 第三步：安装依赖

```bash
pip install -r requirements.txt
```

### 第四步：启动服务

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8010
```

你会看到类似的输出：
```
INFO:     Uvicorn running on http://0.0.0.0:8010
INFO:     Application startup complete
```

### 第五步：访问应用

打开浏览器访问以下地址：

| 功能 | 地址 |
|------|------|
| 🌐 **前端页面（原生）** | http://localhost:8010/static/index.html |
| 📚 **API 文档 (Swagger)** | http://localhost:8010/docs |
| 📖 **API 文档 (ReDoc)** | http://localhost:8010/redoc |
| ✅ **健康检查** | http://localhost:8010/ |

---

## 🎯 前后端分离开发（React）

### 启动 React 前端

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端运行在 http://localhost:3000，通过 Vite 代理自动转发 API 请求到后端。

### 前后端分离架构说明

```
┌─────────────────────────────────────────────────────────┐
│              React 前端 (localhost:3000)                 │
│  ┌──────────────────────────────────────────────────┐  │
│  │  App.jsx          - 主应用组件，状态管理          │  │
│  │  TestCaseList.jsx - 列表展示组件                 │  │
│  │  TestCaseForm.jsx - 表单组件（创建/编辑）        │  │
│  │  api.js           - API 服务层                   │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↕ HTTP/REST (Vite 代理)
┌─────────────────────────────────────────────────────────┐
│              FastAPI 后端 (localhost:8010)               │
│  ┌──────────────────────────────────────────────────┐  │
│  │  /api/test-cases - RESTful API 端点              │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### React 核心概念（教程）

1. **组件化** - UI 拆分为可复用的组件
2. **useState** - 状态管理 Hook
3. **useEffect** - 副作用 Hook（数据获取）
4. **Props** - 父子组件通信
5. **受控组件** - 表单数据由 React 管理

---

## 📚 基础概念

### 什么是 REST API？

REST (Representational State Transfer) 是一种 Web 服务设计风格。简单来说：

- **资源** - 数据对象（这里是"测试用例"）
- **操作** - 通过 HTTP 方法表示（GET、POST、PUT、DELETE）
- **URL** - 资源的地址

### HTTP 方法说明

| 方法 | 用途 | 例子 |
|------|------|------|
| **GET** | 获取数据 | 获取所有测试用例 |
| **POST** | 创建数据 | 创建新的测试用例 |
| **PUT** | 更新数据 | 更新现有测试用例 |
| **DELETE** | 删除数据 | 删除测试用例 |

### HTTP 状态码说明

| 状态码 | 含义 | 例子 |
|--------|------|------|
| **200** | 成功 | 成功获取数据 |
| **201** | 创建成功 | 成功创建测试用例 |
| **204** | 删除成功 | 成功删除测试用例 |
| **400** | 请求错误 | 请求数据格式不正确 |
| **404** | 未找到 | 测试用例不存在 |
| **422** | 验证失败 | 数据验证不通过 |
| **500** | 服务器错误 | 服务器内部错误 |

---

## 💡 简单示例

### 示例 1：使用 curl 创建测试用例（初学者）

```bash
curl -X POST "http://localhost:8010/api/test-cases" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "登录功能测试",
    "description": "验证用户登录功能",
    "steps": "1. 打开登录页面\n2. 输入用户名和密码\n3. 点击登录按钮",
    "expected_result": "成功登录并跳转到首页"
  }'
```

**响应示例：**
```json
{
  "id": 1,
  "title": "登录功能测试",
  "description": "验证用户登录功能",
  "steps": "1. 打开登录页面\n2. 输入用户名和密码\n3. 点击登录按钮",
  "expected_result": "成功登录并跳转到首页",
  "status": "active",
  "created_at": "2024-11-17T10:30:00",
  "updated_at": "2024-11-17T10:30:00"
}
```

### 示例 2：使用 Python 获取测试用例列表（中级）

```python
import requests

# 获取所有测试用例
response = requests.get("http://localhost:8010/api/test-cases")

if response.status_code == 200:
    test_cases = response.json()
    for tc in test_cases:
        print(f"ID: {tc['id']}, 标题: {tc['title']}")
else:
    print(f"错误: {response.status_code}")
```

### 示例 3：使用 JavaScript 更新测试用例（中级）

```javascript
// 更新测试用例
const testCaseId = 1;
const updateData = {
  title: "登录功能测试 - 已更新",
  status: "completed"
};

fetch(`http://localhost:8010/api/test-cases/${testCaseId}`, {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(updateData)
})
.then(response => response.json())
.then(data => console.log('更新成功:', data))
.catch(error => console.error('错误:', error));
```

---

## 📖 API 文档

### 完整 API 端点列表

#### 1. 创建测试用例

```
POST /api/test-cases
```

**请求体：**
```json
{
  "title": "测试用例标题",
  "description": "详细描述（可选）",
  "steps": "测试步骤（可选）",
  "expected_result": "预期结果（可选）",
  "status": "active"
}
```

**响应 (201 Created)：**
```json
{
  "id": 1,
  "title": "测试用例标题",
  "description": "详细描述",
  "steps": "测试步骤",
  "expected_result": "预期结果",
  "status": "active",
  "created_at": "2024-11-17T10:30:00",
  "updated_at": "2024-11-17T10:30:00"
}
```

**字段说明：**
- `title` (必填) - 测试用例标题，1-200 字符
- `description` (可选) - 详细描述
- `steps` (可选) - 测试步骤
- `expected_result` (可选) - 预期结果
- `status` (可选) - 状态，默认为 "active"

**错误响应：**
- `422` - 数据验证失败（如标题为空或超过 200 字符）

---

#### 2. 获取测试用例列表

```
GET /api/test-cases?skip=0&limit=100
```

**查询参数：**
- `skip` - 跳过的记录数，用于分页（默认 0）
- `limit` - 返回的最大记录数（默认 100）

**响应 (200 OK)：**
```json
[
  {
    "id": 1,
    "title": "测试用例 1",
    "description": "描述 1",
    "steps": "步骤 1",
    "expected_result": "预期结果 1",
    "status": "active",
    "created_at": "2024-11-17T10:30:00",
    "updated_at": "2024-11-17T10:30:00"
  },
  {
    "id": 2,
    "title": "测试用例 2",
    "description": "描述 2",
    "steps": "步骤 2",
    "expected_result": "预期结果 2",
    "status": "active",
    "created_at": "2024-11-17T10:35:00",
    "updated_at": "2024-11-17T10:35:00"
  }
]
```

**说明：**
- 返回按创建时间降序排序的测试用例列表
- 如果没有测试用例，返回空数组 `[]`

---

#### 3. 获取单个测试用例

```
GET /api/test-cases/{id}
```

**路径参数：**
- `id` - 测试用例的唯一标识符

**响应 (200 OK)：**
```json
{
  "id": 1,
  "title": "测试用例标题",
  "description": "详细描述",
  "steps": "测试步骤",
  "expected_result": "预期结果",
  "status": "active",
  "created_at": "2024-11-17T10:30:00",
  "updated_at": "2024-11-17T10:30:00"
}
```

**错误响应：**
- `404` - 测试用例不存在

---

#### 4. 更新测试用例

```
PUT /api/test-cases/{id}
```

**路径参数：**
- `id` - 测试用例的唯一标识符

**请求体（所有字段可选）：**
```json
{
  "title": "更新后的标题",
  "description": "更新后的描述",
  "steps": "更新后的步骤",
  "expected_result": "更新后的预期结果",
  "status": "completed"
}
```

**响应 (200 OK)：**
```json
{
  "id": 1,
  "title": "更新后的标题",
  "description": "更新后的描述",
  "steps": "更新后的步骤",
  "expected_result": "更新后的预期结果",
  "status": "completed",
  "created_at": "2024-11-17T10:30:00",
  "updated_at": "2024-11-17T10:40:00"
}
```

**说明：**
- 支持部分更新（只更新提供的字段）
- `updated_at` 会自动更新为当前时间

**错误响应：**
- `404` - 测试用例不存在
- `422` - 数据验证失败

---

#### 5. 删除测试用例

```
DELETE /api/test-cases/{id}
```

**路径参数：**
- `id` - 测试用例的唯一标识符

**响应 (204 No Content)：**
```
(无响应体)
```

**说明：**
- 成功删除返回 204 状态码
- 删除后无法再获取该测试用例

**错误响应：**
- `404` - 测试用例不存在

---

## 📁 项目结构

```
test-case-platform/
│
├── app/                          # 应用主目录
│   ├── __init__.py              # Python 包初始化文件
│   ├── main.py                  # FastAPI 应用入口，定义所有 API 路由
│   ├── models.py                # SQLAlchemy ORM 模型，定义数据库表结构
│   ├── schemas.py               # Pydantic 数据验证模型，定义请求/响应格式
│   ├── database.py              # 数据库连接配置和会话管理
│   └── crud.py                  # CRUD 操作函数，数据库业务逻辑
│
├── static/                       # 前端静态文件
│   └── index.html               # Web 前端页面
│
├── requirements.txt             # Python 依赖列表
├── README.md                    # 项目说明文档（本文件）
├── test_cases.db                # SQLite 数据库文件（运行时生成）
└── .gitignore                   # Git 忽略文件配置
```

### 文件详解

**app/main.py** - FastAPI 应用主文件
- 创建 FastAPI 应用实例
- 配置 CORS 中间件
- 定义所有 API 路由
- 处理应用启动事件

**app/models.py** - 数据库模型
- 定义 `TestCase` SQLAlchemy 模型
- 映射到 `test_cases` 数据库表
- 定义表字段和约束

**app/schemas.py** - 数据验证模型
- `TestCaseBase` - 基础模型
- `TestCaseCreate` - 创建请求模型
- `TestCaseUpdate` - 更新请求模型
- `TestCaseResponse` - 响应模型

**app/database.py** - 数据库配置
- SQLite 数据库连接
- SQLAlchemy 引擎和会话工厂
- 依赖注入函数

**app/crud.py** - 数据库操作
- `create_test_case()` - 创建测试用例
- `get_test_cases()` - 获取列表
- `get_test_case()` - 获取单个
- `update_test_case()` - 更新
- `delete_test_case()` - 删除

---

## 🔧 开发指南

### 本地开发环境设置

#### 1. 安装开发依赖

```bash
# 安装基础依赖
pip install -r requirements.txt

# 安装开发工具（可选）
pip install pytest pytest-cov  # 测试框架
pip install black flake8       # 代码格式化和检查
pip install mypy               # 类型检查
```

#### 2. 启动开发服务器

```bash
# 使用 --reload 参数，代码修改后自动重启
uvicorn app.main:app --reload --host 0.0.0.0 --port 8010
```

#### 3. 查看 API 文档

- Swagger UI: http://localhost:8010/docs
- ReDoc: http://localhost:8010/redoc

### 代码详解

#### 创建测试用例的完整流程

```python
# 1. 前端发送 POST 请求
POST /api/test-cases
{
  "title": "登录测试",
  "description": "测试登录功能"
}

# 2. FastAPI 接收请求并验证数据
@app.post("/api/test-cases")
def create_test_case(test_case: TestCaseCreate, db: Session = Depends(get_db)):
    # test_case 已由 Pydantic 自动验证

# 3. 调用 CRUD 函数
db_test_case = crud.create_test_case(db=db, test_case_data=test_case)

# 4. CRUD 函数创建数据库记录
def create_test_case(db: Session, test_case_data: TestCaseCreate):
    db_test_case = TestCase(**test_case_data.dict())
    db.add(db_test_case)
    db.commit()
    db.refresh(db_test_case)
    return db_test_case

# 5. FastAPI 自动转换为 JSON 响应
{
  "id": 1,
  "title": "登录测试",
  "description": "测试登录功能",
  "created_at": "2024-11-17T10:30:00",
  "updated_at": "2024-11-17T10:30:00"
}
```

#### 数据验证流程

```python
# Pydantic 自动验证以下规则：
class TestCaseCreate(TestCaseBase):
    title: str = Field(..., min_length=1, max_length=200)
    # ✓ 必填字段
    # ✓ 最少 1 个字符
    # ✓ 最多 200 个字符
    
    description: Optional[str] = None
    # ✓ 可选字段
    # ✓ 可以为 None
```

### 扩展建议

#### 1. 添加搜索功能

```python
@app.get("/api/test-cases/search")
def search_test_cases(keyword: str, db: Session = Depends(get_db)):
    return db.query(TestCase).filter(
        TestCase.title.contains(keyword)
    ).all()
```

#### 2. 添加分类功能

```python
# 在 models.py 中添加
category = Column(String(50), nullable=True)

# 在 schemas.py 中添加
category: Optional[str] = None
```

#### 3. 添加用户认证

```python
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/api/test-cases")
def create_test_case(
    test_case: TestCaseCreate,
    credentials: HTTPAuthCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # 验证用户身份
    pass
```

#### 4. 使用 PostgreSQL 替代 SQLite

```python
# 在 database.py 中修改
DATABASE_URL = "postgresql://user:password@localhost/testdb"
```

---

## ❓ 常见问题

### Q1: 如何重置数据库？

```bash
# 删除数据库文件
rm test_cases.db

# 重启服务，会自动创建新的数据库
uvicorn app.main:app --reload
```

### Q2: 如何修改端口号？

```bash
# 使用 --port 参数
uvicorn app.main:app --port 8080
```

### Q3: 如何在生产环境部署？

```bash
# 使用 Gunicorn + Uvicorn
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Q4: 如何处理 CORS 错误？

CORS 错误通常是因为前端和后端不在同一域名。本项目已配置允许所有源，如需限制：

```python
# 在 main.py 中修改
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 只允许特定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Q5: 如何添加日志记录？

```python
import logging

logger = logging.getLogger(__name__)

@app.post("/api/test-cases")
def create_test_case(test_case: TestCaseCreate, db: Session = Depends(get_db)):
    logger.info(f"创建测试用例: {test_case.title}")
    return crud.create_test_case(db=db, test_case_data=test_case)
```

### Q6: 数据库文件在哪里？

```
test_cases.db  # 项目根目录
```

### Q7: 如何导出数据？

```python
import json

# 导出为 JSON
test_cases = db.query(TestCase).all()
data = [tc.__dict__ for tc in test_cases]
with open('export.json', 'w') as f:
    json.dump(data, f, default=str)
```

---

## 📚 学习资源

### 官方文档
- [FastAPI 官方文档](https://fastapi.tiangolo.com/) - 完整的 FastAPI 教程
- [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/) - ORM 框架文档
- [Pydantic 官方文档](https://docs.pydantic.dev/) - 数据验证库文档

### 推荐教程
- [FastAPI 中文教程](https://fastapi.tiangolo.com/zh/) - 中文版本
- [Python Web 开发入门](https://www.python.org/) - Python 官方网站
- [RESTful API 设计指南](https://restfulapi.net/) - REST 最佳实践

### 相关技术
- [HTTP 状态码详解](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [JSON 格式说明](https://www.json.org/)
- [SQL 基础教程](https://www.w3schools.com/sql/)

---

## 📝 许可证

MIT License - 可自由使用、修改和分发

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📞 联系方式

如有问题或建议，欢迎通过以下方式联系：
- 提交 GitHub Issue
- 发送邮件
- 提交 Pull Request

---

**最后更新**: 2024 年 11 月 17 日  
**版本**: 1.0.0
