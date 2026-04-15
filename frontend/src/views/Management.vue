<template>
  <div class="space-y-8">
    <!-- 管理选项卡 -->
    <div class="bg-white rounded-lg shadow-md p-8">
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
          <button class="bg-primary text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors flex items-center">
            <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clip-rule="evenodd"></path>
            </svg>
            添加用户
          </button>
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white border border-gray-200 rounded-lg">
            <thead>
              <tr class="bg-gray-50">
                <th class="py-3 px-4 border-b text-left">ID</th>
                <th class="py-3 px-4 border-b text-left">用户名</th>
                <th class="py-3 px-4 border-b text-left">角色</th>
                <th class="py-3 px-4 border-b text-left">创建时间</th>
                <th class="py-3 px-4 border-b text-left">操作</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50 transition-colors">
                <td class="py-3 px-4 border-b">{{ user.id }}</td>
                <td class="py-3 px-4 border-b">{{ user.username }}</td>
                <td class="py-3 px-4 border-b">
                  <span 
                    class="px-2 py-1 rounded-full text-xs"
                    :class="user.role === 'admin' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'"
                  >
                    {{ user.role === 'admin' ? '管理员' : '普通用户' }}
                  </span>
                </td>
                <td class="py-3 px-4 border-b">{{ user.created_at }}</td>
                <td class="py-3 px-4 border-b">
                  <button class="text-primary hover:underline mr-3 flex items-center">
                    <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" clip-rule="evenodd"></path>
                    </svg>
                    编辑
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
      </div>

      <!-- 任务管理 -->
      <div v-if="activeTab === 'tasks'">
        <div class="mb-4">
          <h3 class="text-lg font-semibold">任务列表</h3>
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white border border-gray-200 rounded-lg">
            <thead>
              <tr class="bg-gray-50">
                <th class="py-3 px-4 border-b text-left">任务ID</th>
                <th class="py-3 px-4 border-b text-left">类型</th>
                <th class="py-3 px-4 border-b text-left">状态</th>
                <th class="py-3 px-4 border-b text-left">创建时间</th>
                <th class="py-3 px-4 border-b text-left">操作</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="task in tasks" :key="task.id" class="hover:bg-gray-50 transition-colors">
                <td class="py-3 px-4 border-b">{{ task.id }}</td>
                <td class="py-3 px-4 border-b">{{ task.type === 'collection' ? '数据采集' : '情感分析' }}</td>
                <td class="py-3 px-4 border-b">
                  <span 
                    class="px-2 py-1 rounded-full text-xs"
                    :class="task.status === 'completed' ? 'bg-green-100 text-green-800' : 'bg-blue-100 text-blue-800'"
                  >
                    {{ task.status === 'completed' ? '已完成' : '进行中' }}
                  </span>
                </td>
                <td class="py-3 px-4 border-b">{{ task.created_at }}</td>
                <td class="py-3 px-4 border-b">
                  <button class="text-primary hover:underline mr-3 flex items-center">
                    <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"></path>
                    </svg>
                    查看
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
              class="bg-primary text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition-colors flex items-center"
            >
              <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
              </svg>
              保存配置
            </button>
          </div>
        </form>
      </div>
    </div>
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