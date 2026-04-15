<template>
  <div class="space-y-8">
    <!-- 数据采集卡片 -->
    <div class="bg-white rounded-lg shadow-md p-8">
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
              class="bg-primary text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition-colors flex items-center"
            >
              <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
              </svg>
              开始采集
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- 数据管理卡片 -->
    <div class="bg-white rounded-lg shadow-md p-8">
      <h3 class="text-lg font-semibold mb-4">数据管理</h3>
      <div class="overflow-x-auto">
        <table class="min-w-full bg-white border border-gray-200 rounded-lg">
          <thead>
            <tr class="bg-gray-50">
              <th class="py-3 px-4 border-b text-left">任务ID</th>
              <th class="py-3 px-4 border-b text-left">平台</th>
              <th class="py-3 px-4 border-b text-left">关键词</th>
              <th class="py-3 px-4 border-b text-left">采集数量</th>
              <th class="py-3 px-4 border-b text-left">状态</th>
              <th class="py-3 px-4 border-b text-left">操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="task in tasks" :key="task.id" class="hover:bg-gray-50 transition-colors">
              <td class="py-3 px-4 border-b">{{ task.id }}</td>
              <td class="py-3 px-4 border-b">{{ task.platform }}</td>
              <td class="py-3 px-4 border-b">{{ task.keywords }}</td>
              <td class="py-3 px-4 border-b">{{ task.count }}</td>
              <td class="py-3 px-4 border-b">
                <span 
                  class="px-2 py-1 rounded-full text-xs"
                  :class="task.status === 'completed' ? 'bg-green-100 text-green-800' : 'bg-blue-100 text-blue-800'"
                >
                  {{ task.status === 'completed' ? '已完成' : '进行中' }}
                </span>
              </td>
              <td class="py-3 px-4 border-b">
                <button class="text-primary hover:underline mr-3 flex items-center">
                  <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"></path>
                  </svg>
                  查看
                </button>
                <button class="text-primary hover:underline mr-3 flex items-center">
                  <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                  </svg>
                  导出
                </button>
                <button class="text-red-500 hover:underline flex items-center">
                  <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" clip-rule="evenodd"></path>
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 011.414 0L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path>
                  </svg>
                  删除
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="mt-4 flex justify-between items-center">
        <p class="text-gray-600">共 {{ tasks.length }} 条记录</p>
        <div class="flex space-x-2">
          <button class="px-3 py-1 border border-gray-300 rounded hover:bg-gray-50 transition-colors">上一页</button>
          <button class="px-3 py-1 border border-gray-300 rounded bg-primary text-white">1</button>
          <button class="px-3 py-1 border border-gray-300 rounded hover:bg-gray-50 transition-colors">下一页</button>
        </div>
      </div>
    </div>
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