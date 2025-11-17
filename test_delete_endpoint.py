"""
测试删除测试用例 API 端点
"""
import sys
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

# 创建测试客户端
client = TestClient(app)

# 确保数据库表存在
Base.metadata.create_all(bind=engine)

# 测试 1: 创建一个测试用例用于删除
print("测试 1: 创建测试用例...")
create_response = client.post(
    "/api/test-cases",
    json={
        "title": "待删除的测试用例",
        "description": "这个测试用例将被删除",
        "status": "active"
    }
)
print(f"创建响应状态码: {create_response.status_code}")
assert create_response.status_code == 201, "创建失败"
created_test_case = create_response.json()
test_case_id = created_test_case["id"]
print(f"创建成功，ID: {test_case_id}")
print(f"创建的测试用例: {created_test_case}")

# 测试 2: 删除存在的测试用例
print("\n测试 2: 删除存在的测试用例...")
delete_response = client.delete(f"/api/test-cases/{test_case_id}")
print(f"删除响应状态码: {delete_response.status_code}")
assert delete_response.status_code == 204, f"删除失败，状态码: {delete_response.status_code}"
print("✓ 成功删除测试用例（返回 204 状态码）")

# 测试 3: 验证测试用例已被删除
print("\n测试 3: 验证测试用例已被删除...")
get_response = client.get(f"/api/test-cases/{test_case_id}")
print(f"获取已删除测试用例的响应状态码: {get_response.status_code}")
assert get_response.status_code == 404, "应该返回 404，因为测试用例已被删除"
print("✓ 确认测试用例已被删除")

# 测试 4: 删除不存在的测试用例
print("\n测试 4: 删除不存在的测试用例...")
not_found_response = client.delete("/api/test-cases/99999")
print(f"删除不存在测试用例的响应状态码: {not_found_response.status_code}")
assert not_found_response.status_code == 404, "应该返回 404"
error_detail = not_found_response.json()
print(f"错误详情: {error_detail}")
assert "not found" in error_detail["detail"].lower(), "错误消息不正确"
print("✓ 正确处理不存在的测试用例")

print("\n所有测试通过！✓")
