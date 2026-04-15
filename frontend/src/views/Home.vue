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
            <li><router-link to="/management" class="hover:text-gray-200">管理</router-link></li>
          </ul>
        </nav>
      </div>
    </header>

    <!-- 主内容区 -->
    <main class="container mx-auto px-4 py-8">
      <div class="bg-white rounded-lg shadow-md p-8 mb-8">
        <h2 class="text-2xl font-semibold mb-4 text-primary">系统介绍</h2>
        <p class="text-gray-700 mb-4">
          社交媒体评论情感分析系统是一个基于大模型智能体的分析工具，用于采集和分析微博、抖音等平台的用户评论数据。
          通过情感极性识别与强度分析，为舆情监测、品牌口碑分析提供技术支撑。
        </p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
          <div class="bg-blue-50 p-6 rounded-lg border border-blue-100">
            <h3 class="text-lg font-semibold mb-2 text-primary">数据采集</h3>
            <p class="text-gray-600">支持多平台评论采集，数据清洗与预处理</p>
          </div>
          <div class="bg-blue-50 p-6 rounded-lg border border-blue-100">
            <h3 class="text-lg font-semibold mb-2 text-primary">情感分析</h3>
            <p class="text-gray-600">基于大模型智能体的情感极性识别与强度分析</p>
          </div>
          <div class="bg-blue-50 p-6 rounded-lg border border-blue-100">
            <h3 class="text-lg font-semibold mb-2 text-primary">可视化展示</h3>
            <p class="text-gray-600">情感分布、舆情趋势、关键词云等多维度展示</p>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-md p-8">
        <h2 class="text-2xl font-semibold mb-4 text-primary">使用流程</h2>
        <div class="flex flex-col md:flex-row gap-4">
          <div class="flex-1 bg-gray-50 p-4 rounded-lg">
            <div class="flex items-center mb-2">
              <div class="w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center mr-2">1</div>
              <h3 class="font-semibold">数据采集</h3>
            </div>
            <p class="text-gray-600 pl-10">配置采集参数，选择平台和关键词，开始采集数据</p>
          </div>
          <div class="flex-1 bg-gray-50 p-4 rounded-lg">
            <div class="flex items-center mb-2">
              <div class="w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center mr-2">2</div>
              <h3 class="font-semibold">情感分析</h3>
            </div>
            <p class="text-gray-600 pl-10">系统使用大模型智能体对数据进行分析，包括情感分析、关键词提取和舆情追踪</p>
          </div>
          <div class="flex-1 bg-gray-50 p-4 rounded-lg">
            <div class="flex items-center mb-2">
              <div class="w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center mr-2">3</div>
              <h3 class="font-semibold">结果展示</h3>
            </div>
            <p class="text-gray-600 pl-10">查看可视化分析结果，导出报告</p>
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
// Home page component
</script>

<style scoped>
/* Home page styles */
</style>