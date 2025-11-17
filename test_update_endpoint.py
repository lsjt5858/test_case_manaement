"""
测试更新测试用例 API 端点
"""
import sys
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

# 创建测试客户端
client = TestClient(app)

# 确保数据库表存在
Base.metadata.create_all(bind=engine)

# 测试 1: 创建一个测试用例用于后续更新
print("测试 1: 创建测试用例...")
create_response = client.post(
    "/api/test-cases",
    json={
        "title": "原始标题",
        "description": "原始描述",
        "steps": "原始步骤",
        "expected_result": "原始预期结果",
        "status": "active"
    }
)
print(f"创建响应状态码: {create_response.status_code}")
assert create_response.status_code == 201, "创建失败"
created_test_case = create_response.json()
test_case_id = created_test_case["id"]
original_created_at = created_test_case["created_at"]
print(f"创建成功，ID: {test_case_id}")
print(f"创建的测试用例: {created_test_case}")

# 测试 2: 更新所有字段
print("\n测试 2: 更新所有字段...")
update_response = client.put(
    f"/api/test-cases/{test_case_id}",
    json={
        "title": "更新后的标题",
        "description": "更新后的描述",
        "steps": "更新后的步骤",
        "expected_result": "更新后的预期结果",
        "status": "inactive"
    }
)
print(f"更新响应状态码: {update_response.status_code}")
assert update_response.status_code == 200, f"更新失败，状态码: {update_response.status_code}"
updated_test_case = update_response.json()
print(f"更新后的测试用例: {updated_test_case}")
assert updated_test_case["id"] == test_case_id, "ID 不应改变"
assert updated_test_case["title"] == "更新后的标题", "标题未更新"
assert updated_test_case["description"] == "更新后的描述", "描述未更新"
assert updated_test_case["status"] == "inactive", "状态未更新"
assert updated_test_case["created_at"] == original_created_at, "创建时间不应改变"
assert updated_test_case["updated_at"] != created_test_case["updated_at"], "更新时间应该改变"
print("✓ 成功更新所有字段")

# 测试 3: 部分更新（仅更新标题）
print("\n测试 3: 部分更新（仅更新标题）...")
partial_update_response = client.put(
    f"/api/test-cases/{test_case_id}",
    json={
        "title": "部分更新的标题"
    }
)
print(f"部分更新响应状态码: {partial_update_response.status_code}")
assert partial_update_response.status_code == 200, "部分更新失败"
partial_updated = partial_update_response.json()
print(f"部分更新后的测试用例: {partial_updated}")
assert partial_updated["title"] == "部分更新的标题", "标题未更新"
assert partial_updated["description"] == "更新后的描述", "描述不应改变"
assert partial_updated["status"] == "inactive", "状态不应改变"
print("✓ 成功进行部分更新")

# 测试 4: 更新不存在的测试用例
print("\n测试 4: 更新不存在的测试用例...")
not_found_response = client.put(
    "/api/test-cases/99999",
    json={"title": "不存在的测试用例"}
)
print(f"更新不存在测试用例的响应状态码: {not_found_response.status_code}")
assert not_found_response.status_code == 404, "应该返回 404"
error_detail = not_found_response.json()
print(f"错误详情: {error_detail}")
assert "not found" in error_detail["detail"].lower(), "错误消息不正确"
print("✓ 正确处理不存在的测试用例")

# 测试 5: 验证错误（标题为空字符串）
print("\n测试 5: 验证错误（标题为空字符串）...")
validation_error_response = client.put(
    f"/api/test-cases/{test_case_id}",
    json={"title": ""}
)
print(f"验证错误响应状态码: {validation_error_response.status_code}")
assert validation_error_response.status_code == 422, "应该返回 422"
validation_error = validation_error_response.json()
print(f"验证错误详情: {validation_error}")
print("✓ 正确处理验证错误")

# 测试 6: 验证 updated_at 自动更新
print("\n测试 6: 验证 updated_at 自动更新...")
import time
time.sleep(1)  # 等待 1 秒确保时间戳不同
final_update_response = client.put(
    f"/api/test-cases/{test_case_id}",
    json={"description": "最终更新"}
)
assert final_update_response.status_code == 200
final_updated = final_update_response.json()
print(f"最终 updated_at: {final_updated['updated_at']}")
print(f"之前 updated_at: {partial_updated['updated_at']}")
assert final_updated["updated_at"] != partial_updated["updated_at"], "updated_at 应该自动更新"
print("✓ updated_at 自动更新正常")

print("\n所有测试通过！✓")
