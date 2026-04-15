<template>
  <div class="app-container">
    <header class="app-header">
      <div class="logo">
        <span class="logo-text">SentimentAI</span>
        <span class="logo-subtext">/ 舆情分析系统</span>
      </div>
      <nav class="app-nav">
        <router-link to="/" class="nav-item">大屏监控</router-link>
        <router-link to="/tasks" class="nav-item">任务管理</router-link>
        <router-link to="/comments" class="nav-item">评论浏览</router-link>
        <router-link to="/chat" class="nav-item">AI对话</router-link>
      </nav>
    </header>
    <main class="app-main">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
.app-container {
  width: 100%;
  height: 100vh;
  background-color: #0f172a;
  color: #e2e8f0;
  font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
}

.app-header {
  height: 60px;
  background-color: #1e293b;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo {
  display: flex;
  align-items: center;
}

.logo-text {
  font-size: 20px;
  font-weight: bold;
  color: #3b82f6;
  margin-right: 8px;
}

.logo-subtext {
  font-size: 14px;
  color: #94a3b8;
}

.app-nav {
  display: flex;
  gap: 24px;
}

.nav-item {
  color: #94a3b8;
  text-decoration: none;
  font-size: 14px;
  padding: 8px 12px;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.nav-item:hover {
  color: #e2e8f0;
  background-color: rgba(59, 130, 246, 0.1);
}

.app-main {
  height: calc(100vh - 60px);
  overflow: auto;
  padding: 24px;
}
</style>
