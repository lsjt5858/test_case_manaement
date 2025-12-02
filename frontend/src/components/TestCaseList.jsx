/**
 * 测试用例列表组件
 * 
 * 教程说明：
 * - 展示测试用例列表
 * - 使用 map 方法渲染列表，每个元素需要唯一的 key
 * - 条件渲染：根据数据状态显示不同内容
 */

/**
 * @param {Object} props
 * @param {Array} props.testCases - 测试用例数组
 * @param {Function} props.onEdit - 编辑回调
 * @param {Function} props.onDelete - 删除回调
 * @param {boolean} props.loading - 加载状态
 */
function TestCaseList({ testCases, onEdit, onDelete, loading }) {
  // 获取状态对应的样式类名
  const getStatusClass = (status) => {
    const statusMap = {
      active: 'status-active',
      passed: 'status-passed',
      failed: 'status-failed'
    }
    return statusMap[status] || 'status-active'
  }

  // 获取状态的中文显示
  const getStatusText = (status) => {
    const textMap = {
      active: '待执行',
      passed: '通过',
      failed: '失败'
    }
    return textMap[status] || status
  }

  // 格式化日期
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleString('zh-CN')
  }

  // 加载中状态
  if (loading) {
    return <div className="card">加载中...</div>
  }

  // 空数据状态
  if (!testCases || testCases.length === 0) {
    return (
      <div className="card" style={{ textAlign: 'center', color: '#999' }}>
        暂无测试用例，点击上方按钮创建第一个吧！
      </div>
    )
  }

  return (
    <div className="test-case-list">
      {/* 使用 map 遍历数组渲染列表 */}
      {testCases.map(testCase => (
        <div key={testCase.id} className="card test-case-item">
          {/* 头部：标题和状态 */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
            <h4 style={{ margin: 0 }}>{testCase.title}</h4>
            <span className={`status-tag ${getStatusClass(testCase.status)}`}>
              {getStatusText(testCase.status)}
            </span>
          </div>

          {/* 描述 */}
          {testCase.description && (
            <p style={{ color: '#666', marginBottom: '12px' }}>
              {testCase.description}
            </p>
          )}

          {/* 测试步骤 */}
          {testCase.steps && (
            <div style={{ marginBottom: '12px' }}>
              <strong>测试步骤：</strong>
              <pre style={{ 
                background: '#f5f5f5', 
                padding: '10px', 
                borderRadius: '4px',
                whiteSpace: 'pre-wrap',
                fontSize: '13px'
              }}>
                {testCase.steps}
              </pre>
            </div>
          )}

          {/* 预期结果 */}
          {testCase.expected_result && (
            <div style={{ marginBottom: '12px' }}>
              <strong>预期结果：</strong>
              <p style={{ margin: '5px 0', color: '#666' }}>{testCase.expected_result}</p>
            </div>
          )}

          {/* 时间信息 */}
          <div style={{ fontSize: '12px', color: '#999', marginBottom: '12px' }}>
            创建时间：{formatDate(testCase.created_at)} | 
            更新时间：{formatDate(testCase.updated_at)}
          </div>

          {/* 操作按钮 */}
          <div style={{ display: 'flex', gap: '10px' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => onEdit(testCase)}
            >
              编辑
            </button>
            <button 
              className="btn btn-danger" 
              onClick={() => {
                if (window.confirm('确定要删除这个测试用例吗？')) {
                  onDelete(testCase.id)
                }
              }}
            >
              删除
            </button>
          </div>
        </div>
      ))}
    </div>
  )
}

export default TestCaseList
