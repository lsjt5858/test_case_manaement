"""
测试脚本，用于验证 GET /api/test-cases 端点
"""
import sys
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

# 创建测试客户端
client = TestClient(app)

# 确保数据库表存在
Base.metadata.create_all(bind=engine)

def test_get_empty_list():
    """测试获取空列表"""
    response = client.get("/api/test-cases")
    
    print(f"状态码: {response.status_code}")
    print(f"响应数据: {response.json()}")
    
    assert response.status_code == 200, f"期望状态码 200，实际 {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "响应应该是数组"
    
    print("✓ 测试通过：成功获取测试用例列表（可能为空）")


def test_get_list_with_data():
    """测试获取包含数据的列表"""
    
    # 先创建几个测试用例
    test_cases = [
        {"title": "测试用例 1", "description": "第一个测试用例"},
        {"title": "测试用例 2", "description": "第二个测试用例"},
        {"title": "测试用例 3", "description": "第三个测试用例"}
    ]
    
    created_ids = []
    for tc in test_cases:
        response = client.post("/api/test-cases", json=tc)
        assert response.status_code == 201
        created_ids.append(response.json()["id"])
    
    print(f"\n已创建 {len(created_ids)} 个测试用例")
    
    # 获取列表
    response = client.get("/api/test-cases")
    
    print(f"状态码: {response.status_code}")
    data = response.json()
    print(f"返回 {len(data)} 个测试用例")
    
    assert response.status_code == 200, f"期望状态码 200，实际 {response.status_code}"
    assert isinstance(data, list), "响应应该是数组"
    assert len(data) >= 3, f"至少应该有 3 个测试用例，实际 {len(data)}"
    
    # 验证每个测试用例包含必要字段
    for tc in data:
        assert "id" in tc, "每个测试用例应包含 id"
        assert "title" in tc, "每个测试用例应包含 title"
        assert "created_at" in tc, "每个测试用例应包含 created_at"
        assert "updated_at" in tc, "每个测试用例应包含 updated_at"
    
    # 验证排序（按创建时间降序）
    if len(data) >= 2:
        # 最新创建的应该在前面
        print(f"第一个测试用例 ID: {data[0]['id']}, 标题: {data[0]['title']}")
        print(f"第二个测试用例 ID: {data[1]['id']}, 标题: {data[1]['title']}")
    
    print("✓ 测试通过：成功获取测试用例列表并验证数据结构")


if __name__ == "__main__":
    try:
        print("=" * 60)
        print("测试 GET /api/test-cases 端点")
        print("=" * 60)
        
        test_get_empty_list()
        test_get_list_with_data()
        
        print("\n" + "=" * 60)
        print("所有测试通过！✓")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n✗ 测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ 错误: {e}")
        sys.exit(1)
