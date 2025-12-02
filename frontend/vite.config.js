import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Vite 配置
// 教程说明：Vite 是现代前端构建工具，比 webpack 更快
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    // 代理配置：将 /api 请求转发到后端
    // 这样前端开发时可以避免跨域问题
    proxy: {
      '/api': {
        target: 'http://localhost:8010',
        changeOrigin: true
      }
    }
  }
})
