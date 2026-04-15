<template>
  <div class="min-h-screen bg-gray-50">
    <!-- 顶部导航栏 -->
    <header class="bg-primary text-white shadow-md">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <h1 class="text-xl font-bold">社交媒体评论情感分析系统</h1>
        <nav>
          <ul class="flex space-x-6">
            <li><router-link to="/" class="hover:text-gray-200">首页</router-link></li>
            <li><router-link to="/collection" class="hover:text-gray-200">数据采集</router-link></li>
            <li><router-link to="/analysis" class="hover:text-gray-200">分析</router-link></li>
            <li><router-link to="/visualization" class="hover:text-gray-200">可视化</router-link></li>
            <li><router-link to="/management" class="hover:text-gray-200 font-semibold">管理</router-link></li>
          </ul>
        </nav>
      </div>
    </header>

    <!-- 主内容区 -->
    <main class="container mx-auto px-4 py-8">
      <div class="bg-white rounded-lg shadow-md p-8 mb-8">
        <h2 class="text-2xl font-semibold mb-6 text-primary">后台管理</h2>
        
        <!-- 管理选项卡 -->
        <div class="mb-8">
          <div class="border-b border-gray-200">
            <ul class="flex flex-wrap -mb-px text-sm font-medium text-center" id="management-tabs" role="tablist">
              <li class="mr-2" role="presentation">
                <button 
                  @click="activeTab = 'users'" 
                  class="inline-block p-4 border-b-2 rounded-t-lg"
                  :class="activeTab === 'users' ? 'border-primary text-primary' : 'border-transparent hover:border-gray-300 hover:text-gray-600'"
                >
                  用户管理
                </button>
              </li>
              <li class="mr-2" role="presentation">
                <button 
                  @click="activeTab = 'tasks'" 
                  class="inline-block p-4 border-b-2 rounded-t-lg"
                  :class="activeTab === 'tasks' ? 'border-primary text-primary' : 'border-transparent hover:border-gray-300 hover:text-gray-600'"
                >
                  任务管理
                </button>
              </li>
              <li role="presentation">
                <button 
                  @click="activeTab = 'config'" 
                  class="inline-block p-4 border-b-2 rounded-t-lg"
                  :class="activeTab === 'config' ? 'border-primary text-primary' : 'border-transparent hover:border-gray-300 hover:text-gray-600'"
                >
                  系统配置
                </button>
              </li>
            </ul>
          </div>
        </div>

        <!-- 用户管理 -->
        <div v-if="activeTab === 'users'">
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-lg font-semibold">用户列表</h3>
            <button class="bg-primary text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors">
              添加用户
            </button>
          </div>
          <div class="overflow-x-auto">
            <table class="min-w-full bg-white border border-gray-200">
              <thead>
                <tr>
                  <th class="py-2 px-4 border-b bg-gray-50">ID</th>
                  <th class="py-2 px-4 border-b bg-gray-50">用户名</th>
                  <th class="py-2 px-4 border-b bg-gray-50">角色</th>
                  <th class="py-2 px-4 border-b bg-gray-50">创建时间</th>
                  <th class="py-2 px-4 border-b bg-gray-50">操作</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in users" :key="user.id">
                  <td class="py-2 px-4 border-b">{{ user.id }}</td>
                  <td class="py-2 px-4 border-b">{{ user.username }}</td>
                  <td class="py-2 px-4 border-b">
                    <span 
                      class="px-2 py-1 rounded-full text-xs"
                      :class="user.role === 'admin' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'"
                    >
                      {{ user.role === 'admin' ? '管理员' : '普通用户' }}
                    </span>
                  </td>
                  <td class="py-2 px-4 border-b">{{ user.created_at }}</td>
                  <td class="py-2 px-4 border-b">
                    <button class="text-primary hover:underline mr-2">编辑</button>
                    <button class="text-red-500 hover:underline">删除</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 任务管理 -->
        <div v-if="activeTab === 'tasks'">
          <div class="mb-4">
            <h3 class="text-lg font-semibold">任务列表</h3>
          </div>
          <div class="overflow-x-auto">
            <table class="min-w-full bg-white border border-gray-200">
              <thead>
                <tr>
                  <th class="py-2 px-4 border-b bg-gray-50">任务ID</th>
                  <th class="py-2 px-4 border-b bg-gray-50">类型</th>
                  <th class="py-2 px-4 border-b bg-gray-50">状态</th>
                  <th class="py-2 px-4 border-b bg-gray-50">创建时间</th>
                  <th class="py-2 px-4 border-b bg-gray-50">操作</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="task in tasks" :key="task.id">
                  <td class="py-2 px-4 border-b">{{ task.id }}</td>
                  <td class="py-2 px-4 border-b">{{ task.type === 'collection' ? '数据采集' : '情感分析' }}</td>
                  <td class="py-2 px-4 border-b">
                    <span 
                      class="px-2 py-1 rounded-full text-xs"
                      :class="task.status === 'completed' ? 'bg-green-100 text-green-800' : 'bg-blue-100 text-blue-800'"
                    >
                      {{ task.status === 'completed' ? '已完成' : '进行中' }}
                    </span>
                  </td>
                  <td class="py-2 px-4 border-b">{{ task.created_at }}</td>
                  <td class="py-2 px-4 border-b">
                    <button class="text-primary hover:underline mr-2">查看</button>
                    <button class="text-red-500 hover:underline">删除</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 系统配置 -->
        <div v-if="activeTab === 'config'">
          <div class="mb-4">
            <h3 class="text-lg font-semibold">系统配置</h3>
          </div>
          <form @submit.prevent="saveConfig">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-gray-700 mb-2">模型名称</label>
                <input 
                  type="text" 
                  v-model="config.model_name" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="请输入模型名称"
                >
              </div>
              <div>
                <label class="block text-gray-700 mb-2">API密钥</label>
                <input 
                  type="text" 
                  v-model="config.api_key" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="请输入API密钥"
                >
              </div>
              <div>
                <label class="block text-gray-700 mb-2">最大 tokens</label>
                <input 
                  type="number" 
                  v-model="config.max_tokens" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="请输入最大 tokens"
                >
              </div>
              <div>
                <label class="block text-gray-700 mb-2">超时时间 (秒)</label>
                <input 
                  type="number" 
                  v-model="config.timeout" 
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="请输入超时时间"
                >
              </div>
            </div>
            <div class="mt-6">
              <button 
                type="submit" 
                class="bg-primary text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition-colors"
              >
                保存配置
              </button>
            </div>
          </form>
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

const activeTab = ref('users')

const users = ref([
  {
    id: 1,
    username: 'admin',
    role: 'admin',
    created_at: '2023-01-01 00:00:00'
  },
  {
    id: 2,
    username: 'user1',
    role: 'user',
    created_at: '2023-01-02 00:00:00'
  }
])

const tasks = ref([
  {
    id: 'task_123',
    type: 'collection',
    status: 'completed',
    created_at: '2023-01-01 12:00:00'
  },
  {
    id: 'task_456',
    type: 'analysis',
    status: 'completed',
    created_at: '2023-01-02 10:30:00'
  }
])

const config = ref({
  model_name: 'llama2',
  api_key: '...',
  max_tokens: 1000,
  timeout: 30
})

const saveConfig = () => {
  // 模拟保存配置
  alert('配置已保存')
}
</script>

<style scoped>
/* Management page styles */
</style>