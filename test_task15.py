#!/usr/bin/env python3
"""
测试任务15：前端更新和删除功能的后端API验证
"""
import requests
import json

BASE_URL = "http://localhost:8000/api/test-cases"

def test_update_and_delete():
    print("=" * 60)
    print("测试任务15：更新和删除功能")
    print("=" * 60)
    
    # 1. 创建一个测试用例
    print("\n1. 创建测试用例...")
    create_data = {
        "title": "测试更新和删除功能",
        "description": "这是一个用于测试的测试用例",
        "steps": "步骤1\n步骤2\n步骤3",
        "expected_result": "预期结果",
        "status": "active"
    }
    
    response = requests.post(BASE_URL, json=create_data)
    assert response.status_code == 201, f"创建失败: {response.status_code}"
    created = response.json()
    test_id = created['id']
    print(f"✓ 创建成功，ID: {test_id}")
    print(f"  标题: {created['title']}")
    
    # 2. 获取单个测试用例（用于编辑前获取数据）
    print(f"\n2. 获取测试用例 ID={test_id}...")
    response = requests.get(f"{BASE_URL}/{test_id}")
    assert response.status_code == 200, f"获取失败: {response.status_code}"
    fetched = response.json()
    print(f"✓ 获取成功")
    print(f"  标题: {fetched['title']}")
    print(f"  描述: {fetched['description']}")
    
    # 3. 更新测试用例
    print(f"\n3. 更新测试用例 ID={test_id}...")
    update_data = {
        "title": "已更新的测试用例标题",
        "description": "已更新的描述",
        "steps": "更新后的步骤1\n更新后的步骤2",
        "expected_result": "更新后的预期结果",
        "status": "active"
    }
    
    response = requests.put(f"{BASE_URL}/{test_id}", json=update_data)
    assert response.status_code == 200, f"更新失败: {response.status_code}"
    updated = response.json()
    print(f"✓ 更新成功")
    print(f"  新标题: {updated['title']}")
    print(f"  新描述: {updated['description']}")
    assert updated['title'] == update_data['title'], "标题未正确更新"
    assert updated['description'] == update_data['description'], "描述未正确更新"
    
    # 4. 验证 updated_at 时间戳已更新
    print(f"\n4. 验证时间戳...")
    print(f"  创建时间: {created['created_at']}")
    print(f"  更新时间: {updated['updated_at']}")
    assert updated['updated_at'] != created['created_at'], "更新时间戳未改变"
    print(f"✓ 时间戳已正确更新")
    
    # 5. 测试更新不存在的测试用例（应返回404）
    print(f"\n5. 测试更新不存在的测试用例...")
    response = requests.put(f"{BASE_URL}/99999", json=update_data)
    assert response.status_code == 404, f"应返回404，实际: {response.status_code}"
    print(f"✓ 正确返回404错误")
    
    # 6. 删除测试用例
    print(f"\n6. 删除测试用例 ID={test_id}...")
    response = requests.delete(f"{BASE_URL}/{test_id}")
    assert response.status_code == 204, f"删除失败: {response.status_code}"
    print(f"✓ 删除成功（返回204）")
    
    # 7. 验证测试用例已被删除
    print(f"\n7. 验证测试用例已被删除...")
    response = requests.get(f"{BASE_URL}/{test_id}")
    assert response.status_code == 404, f"应返回404，实际: {response.status_code}"
    print(f"✓ 测试用例已不存在（返回404）")
    
    # 8. 测试删除不存在的测试用例（应返回404）
    print(f"\n8. 测试删除不存在的测试用例...")
    response = requests.delete(f"{BASE_URL}/99999")
    assert response.status_code == 404, f"应返回404，实际: {response.status_code}"
    print(f"✓ 正确返回404错误")
    
    print("\n" + "=" * 60)
    print("✓ 所有测试通过！")
    print("=" * 60)
    print("\n前端功能说明：")
    print("1. 点击'编辑'按钮会填充表单数据")
    print("2. 表单标题变为'编辑测试用例'，按钮变为'更新测试用例'")
    print("3. 显示'取消编辑'按钮")
    print("4. 提交表单会调用 PUT API 更新数据")
    print("5. 点击'删除'按钮会显示确认对话框")
    print("6. 确认后调用 DELETE API 删除数据")
    print("7. 更新或删除后自动刷新列表")
    print("\n请访问 http://localhost:8000 测试前端功能")

if __name__ == "__main__":
    try:
        test_update_and_delete()
    except AssertionError as e:
        print(f"\n✗ 测试失败: {e}")
        exit(1)
    except requests.exceptions.ConnectionError:
        print("\n✗ 无法连接到服务器，请确保服务器正在运行")
        print("  运行命令: uvicorn app.main:app --reload")
        exit(1)
    except Exception as e:
        print(f"\n✗ 发生错误: {e}")
        exit(1)
