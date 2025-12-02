/**
 * React 应用入口文件
 * 
 * 教程说明：
 * - React 18 使用 createRoot 替代了旧的 ReactDOM.render
 * - StrictMode 帮助发现潜在问题（仅开发环境生效）
 */
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

// 获取 DOM 挂载点并创建 React 根节点
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
