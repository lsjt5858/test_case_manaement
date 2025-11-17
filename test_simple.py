"""简单测试 TestClient"""
import sys

try:
    # 尝试方法 1: 直接导入
    from starlette.testclient import TestClient as StarletteTestClient
    from app.main import app
    
    print("尝试使用 Starlette TestClient...")
    client = StarletteTestClient(app)
    print("✓ Starlette TestClient 成功")
except Exception as e:
    print(f"✗ Starlette TestClient 失败: {e}")
    
    try:
        # 尝试方法 2: 使用 FastAPI 的 TestClient
        from fastapi.testclient import TestClient as FastAPITestClient
        from app.main import app
        
        print("\n尝试使用 FastAPI TestClient...")
        client = FastAPITestClient(app)
        print("✓ FastAPI TestClient 成功")
    except Exception as e2:
        print(f"✗ FastAPI TestClient 也失败: {e2}")
        sys.exit(1)

# 测试一个简单的请求
response = client.get("/")
print(f"\n测试 GET / 端点:")
print(f"状态码: {response.status_code}")
print(f"响应: {response.json()}")
