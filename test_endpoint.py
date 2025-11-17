"""
简单的测试脚本，用于验证 POST /api/test-cases 端点
"""
import sys
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

# 创建测试客户端
client = TestClient(app)

# 确保数据库表存在
Base.metadata.create_all(bind=engine)

def test_create_test_case():
    """测试创建测试用例端点"""
    
    # 测试数据
    test_data = {
        "title": "测试登录功能",
        "description": "验证用户登录流程",
        "steps": "1. 打开登录页面\n2. 输入用户名和密码\n3. 点击登录按钮",
        "expected_result": "成功登录并跳转到首页",
        "status": "active"
    }
    
    # 发送 POST 请求
    response = client.post("/api/test-cases", json=test_data)
    
    # 验证响应
    print(f"状态码: {response.status_code}")
    print(f"响应数据: {response.json()}")
    
    assert response.status_code == 201, f"期望状态码 201，实际 {response.status_code}"
    
    data = response.json()
    assert "id" in data, "响应应包含 id 字段"
    assert "created_at" in data, "响应应包含 created_at 字段"
    assert "updated_at" in data, "响应应包含 updated_at 字段"
    assert data["title"] == test_data["title"], "标题应匹配"
    assert data["description"] == test_data["description"], "描述应匹配"
    
    print("✓ 测试通过：成功创建测试用例")
    return data["id"]


def test_create_minimal_test_case():
    """测试仅使用必填字段创建测试用例"""
    
    test_data = {
        "title": "最小测试用例"
    }
    
    response = client.post("/api/test-cases", json=test_data)
    
    print(f"\n最小数据测试 - 状态码: {response.status_code}")
    print(f"响应数据: {response.json()}")
    
    assert response.status_code == 201, f"期望状态码 201，实际 {response.status_code}"
    
    data = response.json()
    assert data["title"] == test_data["title"], "标题应匹配"
    assert data["status"] == "active", "默认状态应为 active"
    
    print("✓ 测试通过：成功创建最小测试用例")


def test_create_invalid_test_case():
    """测试验证错误处理（缺少必填字段）"""
    
    test_data = {
        "description": "缺少标题字段"
    }
    
    response = client.post("/api/test-cases", json=test_data)
    
    print(f"\n验证错误测试 - 状态码: {response.status_code}")
    print(f"响应数据: {response.json()}")
    
    assert response.status_code == 422, f"期望状态码 422，实际 {response.status_code}"
    
    print("✓ 测试通过：正确处理验证错误")


def test_create_invalid_title_length():
    """测试标题长度验证"""
    
    test_data = {
        "title": ""  # 空标题
    }
    
    response = client.post("/api/test-cases", json=test_data)
    
    print(f"\n标题长度验证测试 - 状态码: {response.status_code}")
    
    assert response.status_code == 422, f"期望状态码 422，实际 {response.status_code}"
    
    print("✓ 测试通过：正确验证标题长度")


if __name__ == "__main__":
    try:
        print("=" * 60)
        print("测试 POST /api/test-cases 端点")
        print("=" * 60)
        
        test_create_test_case()
        test_create_minimal_test_case()
        test_create_invalid_test_case()
        test_create_invalid_title_length()
        
        print("\n" + "=" * 60)
        print("所有测试通过！✓")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n✗ 测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ 错误: {e}")
        sys.exit(1)
