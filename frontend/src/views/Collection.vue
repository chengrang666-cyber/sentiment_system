<template>
  <div class="min-h-screen bg-gray-50">
    <!-- 顶部导航栏 -->
    <header class="bg-primary text-white shadow-md">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <h1 class="text-xl font-bold">社交媒体评论情感分析系统</h1>
        <nav>
          <ul class="flex space-x-6">
            <li><router-link to="/" class="hover:text-gray-200">首页</router-link></li>
            <li><router-link to="/collection" class="hover:text-gray-200 font-semibold">数据采集</router-link></li>
            <li><router-link to="/analysis" class="hover:text-gray-200">分析</router-link></li>
            <li><router-link to="/visualization" class="hover:text-gray-200">可视化</router-link></li>
            <li><router-link to="/management" class="hover:text-gray-200">管理</router-link></li>
          </ul>
        </nav>
      </div>
    </header>

    <!-- 主内容区 -->
    <main class="container mx-auto px-4 py-8">
      <div class="bg-white rounded-lg shadow-md p-8 mb-8">
        <h2 class="text-2xl font-semibold mb-6 text-primary">数据采集</h2>
        
        <!-- 平台选择 -->
        <div class="mb-8">
          <h3 class="text-lg font-semibold mb-4">平台选择</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div 
              class="border rounded-lg p-4 cursor-pointer transition-all hover:shadow-md"
              :class="selectedPlatform === 'weibo' ? 'border-primary bg-blue-50' : 'border-gray-300'"
              @click="selectedPlatform = 'weibo'"
            >
              <div class="flex items-center">
                <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                  <span class="text-primary font-bold text-xl">微博</span>
                </div>
                <div>
                  <h4 class="font-semibold">微博</h4>
                  <p class="text-sm text-gray-600">采集微博平台的用户评论</p>
                </div>
              </div>
            </div>
            <div 
              class="border rounded-lg p-4 cursor-pointer transition-all hover:shadow-md"
              :class="selectedPlatform === 'douyin' ? 'border-primary bg-blue-50' : 'border-gray-300'"
              @click="selectedPlatform = 'douyin'"
            >
              <div class="flex items-center">
                <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                  <span class="text-primary font-bold text-xl">抖音</span>
                </div>
                <div>
                  <h4 class="font-semibold">抖音</h4>
                  <p class="text-sm text-gray-600">采集抖音平台的用户评论</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 采集配置 -->
        <div class="mb-8">
          <h3 class="text-lg font-semibold mb-4">采集配置</h3>
          <form @submit.prevent="startCollection">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-gray-700 mb-2">关键词</label>
                <input 
                  type="text" 
                  v-model="collectionConfig.keywords" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="请输入关键词，多个关键词用逗号分隔"
                >
              </div>
              <div>
                <label class="block text-gray-700 mb-2">采集数量</label>
                <input 
                  type="number" 
                  v-model="collectionConfig.limit" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="请输入采集数量"
                  min="1"
                  max="1000"
                >
              </div>
              <div>
                <label class="block text-gray-700 mb-2">开始日期</label>
                <input 
                  type="date" 
                  v-model="collectionConfig.startDate" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                >
              </div>
              <div>
                <label class="block text-gray-700 mb-2">结束日期</label>
                <input 
                  type="date" 
                  v-model="collectionConfig.endDate" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                >
              </div>
            </div>
            <div class="mt-6">
              <button 
                type="submit" 
                class="bg-primary text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition-colors"
              >
                开始采集
              </button>
            </div>
          </form>
        </div>

        <!-- 数据管理 -->
        <div>
          <h3 class="text-lg font-semibold mb-4">数据管理</h3>
          <div class="overflow-x-auto">
            <table class="min-w-full bg-white border border-gray-200">
              <thead>
                <tr>
                  <th class="py-2 px-4 border-b bg-gray-50">任务ID</th>
                  <th class="py-2 px-4 border-b bg-gray-50">平台</th>
                  <th class="py-2 px-4 border-b bg-gray-50">关键词</th>
                  <th class="py-2 px-4 border-b bg-gray-50">采集数量</th>
                  <th class="py-2 px-4 border-b bg-gray-50">状态</th>
                  <th class="py-2 px-4 border-b bg-gray-50">操作</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="task in tasks" :key="task.id">
                  <td class="py-2 px-4 border-b">{{ task.id }}</td>
                  <td class="py-2 px-4 border-b">{{ task.platform }}</td>
                  <td class="py-2 px-4 border-b">{{ task.keywords }}</td>
                  <td class="py-2 px-4 border-b">{{ task.count }}</td>
                  <td class="py-2 px-4 border-b">
                    <span 
                      class="px-2 py-1 rounded-full text-xs"
                      :class="task.status === 'completed' ? 'bg-green-100 text-green-800' : 'bg-blue-100 text-blue-800'"
                    >
                      {{ task.status === 'completed' ? '已完成' : '进行中' }}
                    </span>
                  </td>
                  <td class="py-2 px-4 border-b">
                    <button class="text-primary hover:underline mr-2">查看</button>
                    <button class="text-primary hover:underline mr-2">导出</button>
                    <button class="text-red-500 hover:underline">删除</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="mt-4 flex justify-between items-center">
            <p class="text-gray-600">共 {{ tasks.length }} 条记录</p>
            <div class="flex space-x-2">
              <button class="px-3 py-1 border border-gray-300 rounded hover:bg-gray-50">上一页</button>
              <button class="px-3 py-1 border border-gray-300 rounded hover:bg-gray-50 bg-gray-100">1</button>
              <button class="px-3 py-1 border border-gray-300 rounded hover:bg-gray-50">下一页</button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 页脚 -->
    <footer class="bg-gray-800 text-white py-6 mt-8">
      <div class="container mx-auto px-4 text-center">
        <p>© 2026 社交媒体评论情感分析系统</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const selectedPlatform = ref('weibo')

const collectionConfig = ref({
  keywords: '',
  limit: 100,
  startDate: new Date().toISOString().split('T')[0],
  endDate: new Date().toISOString().split('T')[0]
})

const tasks = ref([
  {
    id: 'task_123',
    platform: '微博',
    keywords: '产品,服务',
    count: 100,
    status: 'completed'
  },
  {
    id: 'task_456',
    platform: '抖音',
    keywords: '价格,质量',
    count: 50,
    status: 'completed'
  }
])

const startCollection = () => {
  // 模拟开始采集
  alert('采集任务已开始')
  // 这里应该调用后端API开始采集
}
</script>

<style scoped>
/* Collection page styles */
</style>