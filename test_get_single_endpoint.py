"""
测试获取单个测试用例 API 端点
"""
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, get_db
from sqlalchemy.orm import Session

# 创建测试客户端
client = TestClient(app)

# 确保数据库表存在
Base.metadata.create_all(bind=engine)

# 测试 1: 创建一个测试用例
print("测试 1: 创建测试用例...")
create_response = client.post(
    "/api/test-cases",
    json={
        "title": "测试用例标题",
        "description": "这是一个测试描述",
        "steps": "步骤1\n步骤2\n步骤3",
        "expected_result": "预期结果",
        "status": "active"
    }
)
print(f"创建响应状态码: {create_response.status_code}")
assert create_response.status_code == 201, "创建失败"
created_test_case = create_response.json()
test_case_id = created_test_case["id"]
print(f"创建成功，ID: {test_case_id}")
print(f"创建的测试用例: {created_test_case}")

# 测试 2: 获取存在的测试用例
print("\n测试 2: 获取存在的测试用例...")
get_response = client.get(f"/api/test-cases/{test_case_id}")
print(f"获取响应状态码: {get_response.status_code}")
assert get_response.status_code == 200, "获取失败"
retrieved_test_case = get_response.json()
print(f"获取的测试用例: {retrieved_test_case}")
assert retrieved_test_case["id"] == test_case_id, "ID 不匹配"
assert retrieved_test_case["title"] == "测试用例标题", "标题不匹配"
print("✓ 成功获取存在的测试用例")

# 测试 3: 获取不存在的测试用例
print("\n测试 3: 获取不存在的测试用例...")
not_found_response = client.get("/api/test-cases/99999")
print(f"获取不存在测试用例的响应状态码: {not_found_response.status_code}")
assert not_found_response.status_code == 404, "应该返回 404"
error_detail = not_found_response.json()
print(f"错误详情: {error_detail}")
assert "not found" in error_detail["detail"].lower(), "错误消息不正确"
print("✓ 正确处理不存在的测试用例")

print("\n所有测试通过！✓")
