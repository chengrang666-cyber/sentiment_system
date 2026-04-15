<template>
  <div class="space-y-8">
    <!-- 英雄区域 -->
    <div class="bg-gradient-to-r from-primary to-blue-600 rounded-xl shadow-lg p-8 md:p-12 text-white">
      <h1 class="text-3xl md:text-4xl font-bold mb-4">社交媒体评论情感分析系统</h1>
      <p class="text-lg md:text-xl opacity-90 max-w-3xl">
        基于大模型智能体的情感分析平台，通过采集微博、抖音等平台的用户评论数据，
        对评论文本进行情感极性识别与强度分析，并通过可视化界面展示情感分布、舆情趋势等结果。
      </p>
      <div class="mt-8 flex flex-wrap gap-4">
        <router-link to="/collection" class="bg-white text-primary px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors flex items-center">
          <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z"></path>
          </svg>
          开始采集
        </router-link>
        <router-link to="/visualization" class="bg-white/20 text-white border border-white/40 px-6 py-3 rounded-lg font-semibold hover:bg-white/30 transition-colors flex items-center">
          <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"></path>
          </svg>
          查看可视化
        </router-link>
      </div>
    </div>

    <!-- 核心功能 -->
    <div class="bg-white rounded-lg shadow-md p-8">
      <h2 class="text-2xl font-semibold mb-8 text-center text-primary">核心功能</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-blue-50 rounded-lg p-6 border border-blue-100 hover:shadow-md transition-shadow">
          <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z"></path>
            </svg>
          </div>
          <h3 class="text-lg font-semibold mb-4 text-primary">数据采集</h3>
          <p class="text-gray-700">支持微博、抖音等平台的评论定向采集，可设置采集关键词、时间范围、平台类型等筛选条件。</p>
        </div>
        <div class="bg-green-50 rounded-lg p-6 border border-green-100 hover:shadow-md transition-shadow">
          <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
          </div>
          <h3 class="text-lg font-semibold mb-4 text-primary">情感分析</h3>
          <p class="text-gray-700">基于大模型智能体对评论进行情感极性识别与强度分析，提取关键词并追踪舆情趋势。</p>
        </div>
        <div class="bg-purple-50 rounded-lg p-6 border border-purple-100 hover:shadow-md transition-shadow">
          <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"></path>
            </svg>
          </div>
          <h3 class="text-lg font-semibold mb-4 text-primary">可视化展示</h3>
          <p class="text-gray-700">通过Web界面直观展示分析结果，包含情感分布饼图、舆情趋势折线图、高频关键词云等。</p>
        </div>
      </div>
    </div>

    <!-- 使用流程 -->
    <div class="bg-white rounded-lg shadow-md p-8">
      <h2 class="text-2xl font-semibold mb-8 text-center text-primary">使用流程</h2>
      <div class="space-y-8">
        <div class="flex flex-col md:flex-row items-start md:items-center gap-6">
          <div class="bg-primary text-white rounded-full w-12 h-12 flex items-center justify-center flex-shrink-0">1</div>
          <div class="flex-grow">
            <h3 class="text-lg font-semibold mb-2 text-primary">数据采集</h3>
            <p class="text-gray-700">在数据采集页面选择平台，输入关键词和采集数量，点击开始采集按钮。系统将自动爬取指定平台的评论数据。</p>
          </div>
        </div>
        <div class="flex flex-col md:flex-row items-start md:items-center gap-6">
          <div class="bg-primary text-white rounded-full w-12 h-12 flex items-center justify-center flex-shrink-0">2</div>
          <div class="flex-grow">
            <h3 class="text-lg font-semibold mb-2 text-primary">情感分析</h3>
            <p class="text-gray-700">在分析页面选择采集任务，点击开始分析按钮。系统将对采集的评论进行情感分析、关键词提取和舆情追踪。</p>
          </div>
        </div>
        <div class="flex flex-col md:flex-row items-start md:items-center gap-6">
          <div class="bg-primary text-white rounded-full w-12 h-12 flex items-center justify-center flex-shrink-0">3</div>
          <div class="flex-grow">
            <h3 class="text-lg font-semibold mb-2 text-primary">结果展示</h3>
            <p class="text-gray-700">在可视化页面查看情感分布、舆情趋势和关键词云等分析结果。系统支持多维度筛选和结果导出。</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 系统特点 -->
    <div class="bg-white rounded-lg shadow-md p-8">
      <h2 class="text-2xl font-semibold mb-8 text-center text-primary">系统特点</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="flex items-start gap-4">
          <div class="bg-green-100 text-green-600 rounded-full p-2 flex-shrink-0">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
            </svg>
          </div>
          <div>
            <h3 class="font-semibold mb-1 text-gray-800">高效采集</h3>
            <p class="text-gray-600">支持多平台评论定向采集，可设置多种筛选条件，快速获取目标数据。</p>
          </div>
        </div>
        <div class="flex items-start gap-4">
          <div class="bg-blue-100 text-blue-600 rounded-full p-2 flex-shrink-0">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" clip-rule="evenodd"></path>
            </svg>
          </div>
          <div>
            <h3 class="font-semibold mb-1 text-gray-800">智能分析</h3>
            <p class="text-gray-600">基于大模型智能体进行情感分析，提供准确的情感极性识别与强度分析。</p>
          </div>
        </div>
        <div class="flex items-start gap-4">
          <div class="bg-purple-100 text-purple-600 rounded-full p-2 flex-shrink-0">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"></path>
            </svg>
          </div>
          <div>
            <h3 class="font-semibold mb-1 text-gray-800">直观可视化</h3>
            <p class="text-gray-600">通过丰富的图表展示分析结果，包括情感分布饼图、舆情趋势折线图和关键词云。</p>
          </div>
        </div>
        <div class="flex items-start gap-4">
          <div class="bg-amber-100 text-amber-600 rounded-full p-2 flex-shrink-0">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"></path>
            </svg>
          </div>
          <div>
            <h3 class="font-semibold mb-1 text-gray-800">易于管理</h3>
            <p class="text-gray-600">提供完善的后台管理功能，支持用户管理、任务管理和系统配置。</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Home page component
</script>

<style scoped>
/* Home page styles */
</style>