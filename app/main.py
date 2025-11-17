"""
FastAPI 应用主模块

创建 FastAPI 应用实例，配置中间件，定义 API 路由
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_redoc_html
from sqlalchemy.orm import Session
from typing import List
from app.database import engine, Base, get_db
from app.schemas import TestCaseCreate, TestCaseUpdate, TestCaseResponse
from app import crud

# 创建 FastAPI 应用实例
app = FastAPI(
    title="测试用例管理平台",
    description="基于 FastAPI 的测试用例管理系统，提供 CRUD 功能",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,  # 禁用默认 ReDoc，使用自定义版本
    swagger_ui_parameters={"defaultModelsExpandDepth": 1},
)

# 配置 CORS 中间件（开发环境）
# 允许所有源访问，支持跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源（生产环境应限制具体域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

# 挂载静态文件目录
# 将 static 目录挂载到 / 路径，用于提供前端页面
app.mount("/static", StaticFiles(directory="static"), name="static")


# 应用启动事件：创建数据库表
@app.on_event("startup")
def startup_event():
    """
    应用启动时执行的操作
    
    创建所有数据库表（如果不存在）
    需求: 6.1, 6.2, 7.1, 7.2, 7.3
    """
    Base.metadata.create_all(bind=engine)
    print("数据库表已创建")


# 自定义 ReDoc 端点（使用 CDN 资源）
@app.get("/redoc", include_in_schema=False)
async def redoc():
    """
    自定义 ReDoc 文档页面
    使用 CDN 资源加载 ReDoc
    """
    return get_redoc_html(
        title="测试用例管理平台 - API 文档",
        openapi_url=app.openapi_url,
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@latest/bundles/redoc.standalone.js",
    )


# 根路径：健康检查端点
@app.get("/")
def read_root():
    """
    根路径健康检查
    
    Returns:
        dict: 包含欢迎消息和文档链接
    """
    return {
        "message": "欢迎使用测试用例管理平台",
        "docs": "/docs",
        "redoc": "/redoc"
    }


# API 端点：创建测试用例
@app.post(
    "/api/test-cases",
    response_model=TestCaseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="创建测试用例",
    description="创建新的测试用例，返回包含 ID 和时间戳的完整数据"
)
def create_test_case(
    test_case: TestCaseCreate,
    db: Session = Depends(get_db)
):
    """
    创建新测试用例
    
    Args:
        test_case: 测试用例创建数据（自动验证）
        db: 数据库会话（依赖注入）
    
    Returns:
        TestCaseResponse: 新创建的测试用例，包含 id、created_at、updated_at
    
    Raises:
        HTTPException 422: 请求数据验证失败（由 Pydantic 自动处理）
    
    需求: 1.1, 1.2, 1.3, 1.4, 1.5
    """
    # 调用 CRUD 函数创建测试用例
    db_test_case = crud.create_test_case(db=db, test_case_data=test_case)
    
    # FastAPI 自动将 SQLAlchemy 模型转换为 Pydantic 响应模型
    return db_test_case


# API 端点：获取测试用例列表
@app.get(
    "/api/test-cases",
    response_model=List[TestCaseResponse],
    status_code=status.HTTP_200_OK,
    summary="获取测试用例列表",
    description="获取所有测试用例，按创建时间降序排序，支持分页"
)
def get_test_cases(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    获取测试用例列表
    
    Args:
        skip: 跳过的记录数，用于分页（默认 0）
        limit: 返回的最大记录数（默认 100）
        db: 数据库会话（依赖注入）
    
    Returns:
        List[TestCaseResponse]: 测试用例数组，按创建时间降序排序
        如果没有测试用例，返回空数组
    
    需求: 2.1, 2.2, 2.3, 2.4
    """
    # 调用 CRUD 函数获取测试用例列表
    test_cases = crud.get_test_cases(db=db, skip=skip, limit=limit)
    
    # FastAPI 自动将 SQLAlchemy 模型列表转换为 Pydantic 响应模型列表
    # 空列表会自动返回 []
    return test_cases


# API 端点：获取单个测试用例
@app.get(
    "/api/test-cases/{id}",
    response_model=TestCaseResponse,
    status_code=status.HTTP_200_OK,
    summary="获取单个测试用例",
    description="根据 ID 获取测试用例的详细信息"
)
def get_test_case(
    id: int,
    db: Session = Depends(get_db)
):
    """
    获取单个测试用例详情
    
    Args:
        id: 测试用例的唯一标识符
        db: 数据库会话（依赖注入）
    
    Returns:
        TestCaseResponse: 测试用例的完整信息
    
    Raises:
        HTTPException 404: 测试用例不存在
    
    需求: 3.1, 3.2, 3.3
    """
    # 调用 CRUD 函数根据 ID 查询测试用例
    db_test_case = crud.get_test_case(db=db, test_case_id=id)
    
    # 如果测试用例不存在，返回 404 错误
    if db_test_case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Test case not found"
        )
    
    # FastAPI 自动将 SQLAlchemy 模型转换为 Pydantic 响应模型
    return db_test_case


# API 端点：更新测试用例
@app.put(
    "/api/test-cases/{id}",
    response_model=TestCaseResponse,
    status_code=status.HTTP_200_OK,
    summary="更新测试用例",
    description="根据 ID 更新测试用例的信息，支持部分更新"
)
def update_test_case(
    id: int,
    test_case: TestCaseUpdate,
    db: Session = Depends(get_db)
):
    """
    更新测试用例
    
    Args:
        id: 测试用例的唯一标识符
        test_case: 测试用例更新数据（自动验证，所有字段可选）
        db: 数据库会话（依赖注入）
    
    Returns:
        TestCaseResponse: 更新后的测试用例完整信息
    
    Raises:
        HTTPException 404: 测试用例不存在
        HTTPException 422: 请求数据验证失败（由 Pydantic 自动处理）
    
    需求: 4.1, 4.2, 4.3, 4.4, 4.5
    """
    # 调用 CRUD 函数更新测试用例
    db_test_case = crud.update_test_case(db=db, test_case_id=id, test_case_data=test_case)
    
    # 如果测试用例不存在，返回 404 错误
    if db_test_case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Test case not found"
        )
    
    # FastAPI 自动将 SQLAlchemy 模型转换为 Pydantic 响应模型
    return db_test_case


# API 端点：删除测试用例
@app.delete(
    "/api/test-cases/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="删除测试用例",
    description="根据 ID 删除测试用例"
)
def delete_test_case(
    id: int,
    db: Session = Depends(get_db)
):
    """
    删除测试用例
    
    Args:
        id: 测试用例的唯一标识符
        db: 数据库会话（依赖注入）
    
    Returns:
        None: 成功删除返回 204 状态码（无内容）
    
    Raises:
        HTTPException 404: 测试用例不存在
    
    需求: 5.1, 5.2, 5.3
    """
    # 调用 CRUD 函数删除测试用例
    success = crud.delete_test_case(db=db, test_case_id=id)
    
    # 如果测试用例不存在，返回 404 错误
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Test case not found"
        )
    
    # 成功删除，返回 204 状态码（无内容）
    # FastAPI 会自动处理 204 响应，不返回任何内容
    return None
