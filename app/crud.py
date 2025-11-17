"""
CRUD 操作模块

封装所有数据库操作逻辑，提供创建、读取、更新、删除测试用例的函数
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import TestCase
from app.schemas import TestCaseCreate, TestCaseUpdate


def create_test_case(db: Session, test_case_data: TestCaseCreate) -> TestCase:
    """
    创建新测试用例
    
    Args:
        db: 数据库会话
        test_case_data: 测试用例创建数据（Pydantic 模式）
    
    Returns:
        TestCase: 新创建的测试用例对象，包含数据库生成的 id 和时间戳
    
    需求: 1.1, 1.5
    """
    # 将 Pydantic 模型转换为字典
    test_case_dict = test_case_data.model_dump()
    
    # 创建 TestCase 实例，自动设置 created_at 和 updated_at
    db_test_case = TestCase(**test_case_dict)
    
    # 添加到会话
    db.add(db_test_case)
    
    # 提交事务到数据库
    db.commit()
    
    # 刷新实例以获取数据库生成的字段（id, created_at, updated_at）
    db.refresh(db_test_case)
    
    return db_test_case


def get_test_cases(db: Session, skip: int = 0, limit: int = 100) -> List[TestCase]:
    """
    获取测试用例列表
    
    Args:
        db: 数据库会话
        skip: 跳过的记录数，用于分页（默认 0）
        limit: 返回的最大记录数（默认 100）
    
    Returns:
        List[TestCase]: 测试用例列表，按创建时间降序排序
    
    需求: 2.1, 2.4
    """
    return (
        db.query(TestCase)
        .order_by(TestCase.created_at.desc())  # 按创建时间降序排序
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_test_case(db: Session, test_case_id: int) -> Optional[TestCase]:
    """
    根据 ID 获取单个测试用例
    
    Args:
        db: 数据库会话
        test_case_id: 测试用例 ID
    
    Returns:
        TestCase | None: 测试用例对象，如果不存在则返回 None
    
    需求: 3.1
    """
    return db.query(TestCase).filter(TestCase.id == test_case_id).first()


def update_test_case(
    db: Session, 
    test_case_id: int, 
    test_case_data: TestCaseUpdate
) -> Optional[TestCase]:
    """
    更新测试用例
    
    Args:
        db: 数据库会话
        test_case_id: 测试用例 ID
        test_case_data: 更新数据（Pydantic 模式）
    
    Returns:
        TestCase | None: 更新后的测试用例对象，如果不存在则返回 None
    
    需求: 4.1, 4.4
    """
    # 查询测试用例
    db_test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    
    if db_test_case is None:
        return None
    
    # 获取更新数据，排除未设置的字段
    update_data = test_case_data.model_dump(exclude_unset=True)
    
    # 更新字段
    for field, value in update_data.items():
        setattr(db_test_case, field, value)
    
    # 手动更新 updated_at 时间戳
    db_test_case.updated_at = datetime.utcnow()
    
    # 提交事务
    db.commit()
    
    # 刷新实例
    db.refresh(db_test_case)
    
    return db_test_case


def delete_test_case(db: Session, test_case_id: int) -> bool:
    """
    删除测试用例
    
    Args:
        db: 数据库会话
        test_case_id: 测试用例 ID
    
    Returns:
        bool: 成功删除返回 True，测试用例不存在返回 False
    
    需求: 5.1
    """
    # 查询测试用例
    db_test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    
    if db_test_case is None:
        return False
    
    # 删除记录
    db.delete(db_test_case)
    
    # 提交事务
    db.commit()
    
    return True
