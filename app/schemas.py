"""
Pydantic 数据验证模式模块

定义 API 请求和响应的数据结构，提供自动数据验证和序列化
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class TestCaseBase(BaseModel):
    """
    测试用例基础模式
    
    包含测试用例的所有业务字段，作为其他模式的基类
    """
    title: str = Field(..., min_length=1, max_length=200, description="测试用例标题，必填，1-200 字符")
    description: Optional[str] = Field(None, description="测试用例详细描述，可选")
    steps: Optional[str] = Field(None, description="测试步骤，可选")
    expected_result: Optional[str] = Field(None, description="预期结果，可选")
    status: str = Field(default="active", description="测试用例状态，默认为 active")


class TestCaseCreate(TestCaseBase):
    """
    创建测试用例请求模式
    
    用于 POST /api/test-cases 端点
    继承 TestCaseBase 的所有字段和验证规则
    """
    pass


class TestCaseUpdate(BaseModel):
    """
    更新测试用例请求模式
    
    用于 PUT /api/test-cases/{id} 端点
    所有字段都是可选的，允许部分更新
    """
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="测试用例标题，可选，1-200 字符")
    description: Optional[str] = Field(None, description="测试用例详细描述，可选")
    steps: Optional[str] = Field(None, description="测试步骤，可选")
    expected_result: Optional[str] = Field(None, description="预期结果，可选")
    status: Optional[str] = Field(None, description="测试用例状态，可选")


class TestCaseResponse(TestCaseBase):
    """
    测试用例响应模式
    
    用于所有返回测试用例数据的 API 响应
    包含数据库生成的字段：id、created_at、updated_at
    """
    id: int = Field(..., description="测试用例唯一标识符")
    created_at: datetime = Field(..., description="创建时间戳")
    updated_at: datetime = Field(..., description="最后更新时间戳")
    
    # Pydantic v2 配置
    model_config = ConfigDict(from_attributes=True)
