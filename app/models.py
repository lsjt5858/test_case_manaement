"""
数据模型定义模块

定义 SQLAlchemy ORM 模型，映射到数据库表
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database import Base


class TestCase(Base):
    """
    测试用例数据模型
    
    表示一个测试用例的完整信息，包括标题、描述、步骤、预期结果等
    """
    __tablename__ = "test_cases"
    
    # 主键：唯一标识符，自动递增
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # 标题：必填字段，最大 200 字符
    title = Column(String(200), nullable=False)
    
    # 描述：可选字段，文本类型
    description = Column(Text, nullable=True)
    
    # 测试步骤：可选字段，文本类型
    steps = Column(Text, nullable=True)
    
    # 预期结果：可选字段，文本类型
    expected_result = Column(Text, nullable=True)
    
    # 状态：默认为 "active"
    status = Column(String(50), nullable=False, default="active")
    
    # 创建时间：自动生成，记录创建时间戳
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    # 更新时间：自动更新，记录最后修改时间戳
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        """字符串表示，用于调试"""
        return f"<TestCase(id={self.id}, title='{self.title}', status='{self.status}')>"
