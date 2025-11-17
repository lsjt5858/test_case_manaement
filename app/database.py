"""
数据库配置和连接管理模块

提供 SQLAlchemy 数据库连接、会话管理和依赖注入功能
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 数据库连接字符串
# check_same_thread=False 允许多线程访问（SQLite 默认限制）
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_cases.db"

# 创建 SQLAlchemy 引擎
# connect_args 仅用于 SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# 创建会话工厂
# autocommit=False: 需要显式提交事务
# autoflush=False: 需要显式刷新
# bind=engine: 绑定到数据库引擎
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建声明式基类
# 所有数据模型将继承此基类
Base = declarative_base()


# 依赖注入函数：提供数据库会话
def get_db():
    """
    FastAPI 依赖注入函数，用于获取数据库会话
    
    使用方式:
        @app.get("/items")
        def read_items(db: Session = Depends(get_db)):
            ...
    
    Yields:
        Session: 数据库会话对象
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
