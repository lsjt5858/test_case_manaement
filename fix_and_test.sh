#!/bin/bash

echo "=========================================="
echo "修复 httpx 版本兼容性问题"
echo "=========================================="

# 降级 httpx 到兼容版本
echo "正在降级 httpx 到 0.24.1..."
pip install httpx==0.24.1 -q

if [ $? -eq 0 ]; then
    echo "✓ httpx 降级成功"
else
    echo "✗ httpx 降级失败，尝试升级 fastapi 和 starlette..."
    pip install --upgrade fastapi starlette -q
fi

echo ""
echo "=========================================="
echo "运行所有测试"
echo "=========================================="

# 运行所有测试文件
for test_file in test_endpoint.py test_get_endpoint.py test_get_single_endpoint.py test_update_endpoint.py; do
    if [ -f "$test_file" ]; then
        echo ""
        echo "运行 $test_file..."
        echo "------------------------------------------"
        python "$test_file"
        if [ $? -eq 0 ]; then
            echo "✓ $test_file 通过"
        else
            echo "✗ $test_file 失败"
        fi
    fi
done

echo ""
echo "=========================================="
echo "测试完成"
echo "=========================================="
