/**
 * API 服务层
 * 
 * 教程说明：
 * - 将所有 API 调用集中管理，便于维护
 * - 使用 axios 进行 HTTP 请求
 * - 前后端分离的核心：前端通过 HTTP API 与后端通信
 */
import axios from 'axios'

// 创建 axios 实例，配置基础 URL
// 开发环境通过 Vite 代理转发，生产环境需要配置实际后端地址
const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

/**
 * 测试用例 API
 */
export const testCaseApi = {
  /**
   * 获取所有测试用例
   * GET /api/test-cases
   */
  getAll: async (skip = 0, limit = 100) => {
    const response = await api.get(`/test-cases?skip=${skip}&limit=${limit}`)
    return response.data
  },

  /**
   * 获取单个测试用例
   * GET /api/test-cases/:id
   */
  getById: async (id) => {
    const response = await api.get(`/test-cases/${id}`)
    return response.data
  },

  /**
   * 创建测试用例
   * POST /api/test-cases
   */
  create: async (testCase) => {
    const response = await api.post('/test-cases', testCase)
    return response.data
  },

  /**
   * 更新测试用例
   * PUT /api/test-cases/:id
   */
  update: async (id, testCase) => {
    const response = await api.put(`/test-cases/${id}`, testCase)
    return response.data
  },

  /**
   * 删除测试用例
   * DELETE /api/test-cases/:id
   */
  delete: async (id) => {
    await api.delete(`/test-cases/${id}`)
  }
}

export default api
