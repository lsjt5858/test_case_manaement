/**
 * 主应用组件
 * 
 * 教程说明：
 * - App 是 React 应用的根组件
 * - 管理全局状态和页面逻辑
 * - useState: 状态管理 Hook
 * - useEffect: 副作用 Hook，用于数据获取等
 */
import { useState, useEffect } from 'react'
import TestCaseList from './components/TestCaseList'
import TestCaseForm from './components/TestCaseForm'
import { testCaseApi } from './services/api'

function App() {
  // ========== 状态定义 ==========
  // 测试用例列表
  const [testCases, setTestCases] = useState([])
  // 加载状态
  const [loading, setLoading] = useState(true)
  // 当前视图：'list' | 'create' | 'edit'
  const [view, setView] = useState('list')
  // 当前编辑的测试用例
  const [editingTestCase, setEditingTestCase] = useState(null)
  // 错误信息
  const [error, setError] = useState(null)

  // ========== 数据获取 ==========
  // 组件挂载时获取测试用例列表
  // useEffect 的第二个参数是依赖数组，空数组表示只在挂载时执行一次
  useEffect(() => {
    fetchTestCases()
  }, [])

  // 获取测试用例列表
  const fetchTestCases = async () => {
    setLoading(true)
    setError(null)
    try {
      const data = await testCaseApi.getAll()
      setTestCases(data)
    } catch (err) {
      console.error('获取测试用例失败:', err)
      setError('获取测试用例失败，请检查后端服务是否启动')
    } finally {
      setLoading(false)
    }
  }

  // ========== 事件处理 ==========
  // 创建测试用例
  const handleCreate = async (formData) => {
    try {
      await testCaseApi.create(formData)
      setView('list')
      fetchTestCases() // 刷新列表
    } catch (err) {
      console.error('创建失败:', err)
      alert('创建失败: ' + (err.response?.data?.detail || err.message))
    }
  }

  // 更新测试用例
  const handleUpdate = async (formData) => {
    try {
      await testCaseApi.update(editingTestCase.id, formData)
      setView('list')
      setEditingTestCase(null)
      fetchTestCases() // 刷新列表
    } catch (err) {
      console.error('更新失败:', err)
      alert('更新失败: ' + (err.response?.data?.detail || err.message))
    }
  }

  // 删除测试用例
  const handleDelete = async (id) => {
    try {
      await testCaseApi.delete(id)
      fetchTestCases() // 刷新列表
    } catch (err) {
      console.error('删除失败:', err)
      alert('删除失败: ' + (err.response?.data?.detail || err.message))
    }
  }

  // 进入编辑模式
  const handleEdit = (testCase) => {
    setEditingTestCase(testCase)
    setView('edit')
  }

  // 取消操作，返回列表
  const handleCancel = () => {
    setView('list')
    setEditingTestCase(null)
  }

  // ========== 渲染 ==========
  return (
    <div className="container">
      {/* 页面标题 */}
      <header style={{ marginBottom: '24px' }}>
        <h1>🧪 测试用例管理平台</h1>
        <p style={{ color: '#666' }}>基于 React + FastAPI 的前后端分离项目</p>
      </header>

      {/* 错误提示 */}
      {error && (
        <div style={{ 
          background: '#fff2f0', 
          border: '1px solid #ffccc7', 
          padding: '12px', 
          borderRadius: '4px',
          marginBottom: '16px',
          color: '#ff4d4f'
        }}>
          {error}
        </div>
      )}

      {/* 条件渲染：根据 view 状态显示不同内容 */}
      {view === 'list' && (
        <>
          {/* 操作栏 */}
          <div style={{ marginBottom: '16px' }}>
            <button 
              className="btn btn-primary" 
              onClick={() => setView('create')}
            >
              + 新建测试用例
            </button>
            <button 
              className="btn btn-secondary" 
              onClick={fetchTestCases}
              style={{ marginLeft: '10px' }}
            >
              刷新
            </button>
          </div>

          {/* 测试用例列表 */}
          <TestCaseList
            testCases={testCases}
            loading={loading}
            onEdit={handleEdit}
            onDelete={handleDelete}
          />
        </>
      )}

      {view === 'create' && (
        <TestCaseForm
          onSubmit={handleCreate}
          onCancel={handleCancel}
          isEdit={false}
        />
      )}

      {view === 'edit' && (
        <TestCaseForm
          initialData={editingTestCase}
          onSubmit={handleUpdate}
          onCancel={handleCancel}
          isEdit={true}
        />
      )}
    </div>
  )
}

export default App
