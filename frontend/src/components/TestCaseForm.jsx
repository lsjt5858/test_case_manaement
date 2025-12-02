/**
 * 测试用例表单组件
 * 
 * 教程说明：
 * - 这是一个"受控组件"，表单数据由 React state 管理
 * - 可复用于创建和编辑场景
 * - props 是父组件传递给子组件的数据
 */
import { useState, useEffect } from 'react'

/**
 * @param {Object} props
 * @param {Object} props.initialData - 初始数据（编辑时使用）
 * @param {Function} props.onSubmit - 提交回调
 * @param {Function} props.onCancel - 取消回调
 * @param {boolean} props.isEdit - 是否为编辑模式
 */
function TestCaseForm({ initialData, onSubmit, onCancel, isEdit = false }) {
  // 表单状态：使用 useState Hook 管理
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    steps: '',
    expected_result: '',
    status: 'active'
  })

  // 加载状态
  const [loading, setLoading] = useState(false)

  // 当 initialData 变化时，更新表单数据
  // useEffect 是 React 的副作用 Hook
  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        description: initialData.description || '',
        steps: initialData.steps || '',
        expected_result: initialData.expected_result || '',
        status: initialData.status || 'active'
      })
    }
  }, [initialData])

  // 处理输入变化
  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  // 处理表单提交
  const handleSubmit = async (e) => {
    e.preventDefault() // 阻止表单默认提交行为
    
    if (!formData.title.trim()) {
      alert('请输入测试用例标题')
      return
    }

    setLoading(true)
    try {
      await onSubmit(formData)
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="card">
      <h3>{isEdit ? '编辑测试用例' : '创建测试用例'}</h3>
      
      {/* 标题输入 */}
      <div className="form-group">
        <label htmlFor="title">标题 *</label>
        <input
          type="text"
          id="title"
          name="title"
          value={formData.title}
          onChange={handleChange}
          placeholder="请输入测试用例标题"
          maxLength={200}
          required
        />
      </div>

      {/* 描述输入 */}
      <div className="form-group">
        <label htmlFor="description">描述</label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
          placeholder="请输入测试用例描述"
          rows={3}
        />
      </div>

      {/* 测试步骤 */}
      <div className="form-group">
        <label htmlFor="steps">测试步骤</label>
        <textarea
          id="steps"
          name="steps"
          value={formData.steps}
          onChange={handleChange}
          placeholder="请输入测试步骤"
          rows={4}
        />
      </div>

      {/* 预期结果 */}
      <div className="form-group">
        <label htmlFor="expected_result">预期结果</label>
        <textarea
          id="expected_result"
          name="expected_result"
          value={formData.expected_result}
          onChange={handleChange}
          placeholder="请输入预期结果"
          rows={3}
        />
      </div>

      {/* 状态选择 */}
      <div className="form-group">
        <label htmlFor="status">状态</label>
        <select
          id="status"
          name="status"
          value={formData.status}
          onChange={handleChange}
        >
          <option value="active">待执行</option>
          <option value="passed">通过</option>
          <option value="failed">失败</option>
        </select>
      </div>

      {/* 按钮组 */}
      <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? '提交中...' : (isEdit ? '保存修改' : '创建')}
        </button>
        <button type="button" className="btn btn-secondary" onClick={onCancel}>
          取消
        </button>
      </div>
    </form>
  )
}

export default TestCaseForm
