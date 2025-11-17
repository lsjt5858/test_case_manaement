"""
手动测试更新 API - 使用 requests 库
运行前请先启动服务器: uvicorn app.main:app --reload
"""
import requests
import json

BASE_URL = "http://localhost:8000"

print("=" * 60)
print("测试 PUT /api/test-cases/{id} 端点")
print("=" * 60)

# 测试 1: 创建一个测试用例
print("\n测试 1: 创建测试用例...")
create_data = {
    "title": "原始标题",
    "description": "原始描述",
    "steps": "原始步骤",
    "expected_result": "原始预期结果",
    "status": "active"
}
response = requests.post(f"{BASE_URL}/api/test-cases", json=create_data)
print(f"状态码: {response.status_code}")
if response.status_code == 201:
    created = response.json()
    test_case_id = created["id"]
    print(f"✓ 创建成功，ID: {test_case_id}")
    print(f"创建的数据: {json.dumps(created, indent=2, ensure_ascii=False)}")
else:
    print(f"✗ 创建失败: {response.text}")
    exit(1)

# 测试 2: 更新所有字段
print("\n测试 2: 更新所有字段...")
update_data = {
    "title": "更新后的标题",
    "description": "更新后的描述",
    "steps": "更新后的步骤",
    "expected_result": "更新后的预期结果",
    "status": "inactive"
}
response = requests.put(f"{BASE_URL}/api/test-cases/{test_case_id}", json=update_data)
print(f"状态码: {response.status_code}")
if response.status_code == 200:
    updated = response.json()
    print(f"✓ 更新成功")
    print(f"更新后的数据: {json.dumps(updated, indent=2, ensure_ascii=False)}")
    assert updated["title"] == "更新后的标题", "标题未更新"
    assert updated["status"] == "inactive", "状态未更新"
    print("✓ 数据验证通过")
else:
    print(f"✗ 更新失败: {response.text}")

# 测试 3: 部分更新
print("\n测试 3: 部分更新（仅更新标题）...")
partial_data = {"title": "部分更新的标题"}
response = requests.put(f"{BASE_URL}/api/test-cases/{test_case_id}", json=partial_data)
print(f"状态码: {response.status_code}")
if response.status_code == 200:
    partial_updated = response.json()
    print(f"✓ 部分更新成功")
    print(f"更新后的标题: {partial_updated['title']}")
    assert partial_updated["title"] == "部分更新的标题", "标题未更新"
    assert partial_updated["description"] == "更新后的描述", "描述不应改变"
    print("✓ 部分更新验证通过")
else:
    print(f"✗ 部分更新失败: {response.text}")

# 测试 4: 更新不存在的测试用例
print("\n测试 4: 更新不存在的测试用例...")
response = requests.put(f"{BASE_URL}/api/test-cases/99999", json={"title": "不存在"})
print(f"状态码: {response.status_code}")
if response.status_code == 404:
    print(f"✓ 正确返回 404")
    print(f"错误信息: {response.json()}")
else:
    print(f"✗ 应该返回 404，实际: {response.status_code}")

# 测试 5: 验证错误（空标题）
print("\n测试 5: 验证错误（空标题）...")
response = requests.put(f"{BASE_URL}/api/test-cases/{test_case_id}", json={"title": ""})
print(f"状态码: {response.status_code}")
if response.status_code == 422:
    print(f"✓ 正确返回 422 验证错误")
    print(f"错误信息: {response.json()}")
else:
    print(f"✗ 应该返回 422，实际: {response.status_code}")

print("\n" + "=" * 60)
print("所有测试完成！")
print("=" * 60)
