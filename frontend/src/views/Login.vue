<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50">
    <div class="bg-white rounded-lg shadow-md p-8 w-full max-w-md">
      <h2 class="text-2xl font-semibold mb-6 text-center text-primary">登录系统</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label for="username" class="block text-gray-700 mb-2">用户名</label>
          <input 
            type="text" 
            id="username" 
            v-model="form.username" 
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
            placeholder="请输入用户名"
            required
          >
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700 mb-2">密码</label>
          <input 
            type="password" 
            id="password" 
            v-model="form.password" 
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
            placeholder="请输入密码"
            required
          >
        </div>
        <button 
          type="submit" 
          class="w-full bg-primary text-white py-2 rounded-lg hover:bg-blue-600 transition-colors"
        >
          登录
        </button>
        <div class="mt-4 text-center">
          <p class="text-gray-600">默认管理员账号: admin / admin</p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  username: '',
  password: ''
})

const login = () => {
  // 模拟登录验证
  if (form.value.username === 'admin' && form.value.password === 'admin') {
    // 登录成功，跳转到首页
    router.push('/')
  } else {
    alert('用户名或密码错误')
  }
}
</script>

<style scoped>
/* Login page styles */
</style>