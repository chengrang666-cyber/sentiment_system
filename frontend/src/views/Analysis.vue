<template>
  <div class="space-y-8">
    <!-- 分析配置卡片 -->
    <div class="bg-white rounded-lg shadow-md p-8">
      <h2 class="text-2xl font-semibold mb-6 text-primary">情感分析</h2>
      
      <!-- 分析配置 -->
      <div class="mb-8">
        <h3 class="text-lg font-semibold mb-4">分析配置</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-gray-700 mb-2">选择采集任务</label>
            <select 
              v-model="selectedTask" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
            >
              <option value="">请选择采集任务</option>
              <option v-for="task in tasks" :key="task.id" :value="task.id">
                {{ task.id }} - {{ task.platform }} - {{ task.keywords }}
              </option>
            </select>
          </div>
          <div>
            <label class="block text-gray-700 mb-2">分析类型</label>
            <div class="flex flex-wrap gap-4">
              <label class="flex items-center">
                <input 
                  type="radio" 
                  v-model="analysisType" 
                  value="sentiment" 
                  class="mr-2"
                >
                情感分析
              </label>
              <label class="flex items-center">
                <input 
                  type="radio" 
                  v-model="analysisType" 
                  value="keywords" 
                  class="mr-2"
                >
                关键词提取
              </label>
              <label class="flex items-center">
                <input 
                  type="radio" 
                  v-model="analysisType" 
                  value="trend" 
                  class="mr-2"
                >
                舆情趋势
              </label>
            </div>
          </div>
        </div>
        <div class="mt-6">
          <button 
            @click="startAnalysis" 
            class="bg-primary text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition-colors flex items-center"
          >
            <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
            开始分析
          </button>
        </div>
      </div>
    </div>

    <!-- 分析结果卡片 -->
    <div v-if="analysisResults" class="bg-white rounded-lg shadow-md p-8">
      <h3 class="text-lg font-semibold mb-4">分析结果</h3>
      
      <!-- 情感分析结果 -->
      <div v-if="analysisType === 'sentiment'">
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white border border-gray-200 rounded-lg">
            <thead>
              <tr class="bg-gray-50">
                <th class="py-3 px-4 border-b text-left">评论内容</th>
                <th class="py-3 px-4 border-b text-left">情感极性</th>
                <th class="py-3 px-4 border-b text-left">情感强度</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(result, index) in analysisResults" :key="index" class="hover:bg-gray-50 transition-colors">
                <td class="py-3 px-4 border-b">{{ result.content }}</td>
                <td class="py-3 px-4 border-b">
                  <span 
                    class="px-2 py-1 rounded-full text-xs"
                    :class="result.sentiment === 'positive' ? 'bg-green-100 text-green-800' : result.sentiment === 'negative' ? 'bg-red-100 text-red-800' : 'bg-gray-100 text-gray-800'"
                  >
                    {{ result.sentiment === 'positive' ? '正面' : result.sentiment === 'negative' ? '负面' : '中性' }}
                  </span>
                </td>
                <td class="py-3 px-4 border-b">{{ result.score.toFixed(2) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 关键词提取结果 -->
      <div v-else-if="analysisType === 'keywords'">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="(keyword, index) in analysisResults" :key="index" class="border rounded-lg p-4 hover:shadow-md transition-shadow">
            <div class="flex justify-between items-center">
              <h4 class="font-semibold">{{ keyword.word }}</h4>
              <span class="px-2 py-1 rounded-full text-xs bg-blue-100 text-blue-800">
                频率: {{ keyword.frequency }}
              </span>
            </div>
            <div class="mt-2">
              <span 
                class="px-2 py-1 rounded-full text-xs"
                :class="keyword.sentiment === 'positive' ? 'bg-green-100 text-green-800' : keyword.sentiment === 'negative' ? 'bg-red-100 text-red-800' : 'bg-gray-100 text-gray-800'"
              >
                {{ keyword.sentiment === 'positive' ? '正面' : keyword.sentiment === 'negative' ? '负面' : '中性' }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- 舆情趋势结果 -->
      <div v-else-if="analysisType === 'trend'">
        <div class="h-80 border rounded-lg p-4">
          <!-- 这里应该使用ECharts绘制趋势图 -->
          <div id="trendChart" class="w-full h-full"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import * as echarts from 'echarts'

const selectedTask = ref('')
const analysisType = ref('sentiment')
const analysisResults = ref<any>(null)

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

const startAnalysis = () => {
  // 模拟分析结果
  if (analysisType.value === 'sentiment') {
    analysisResults.value = [
      { content: '这个产品非常好，服务也很周到', sentiment: 'positive', score: 0.9 },
      { content: '价格有点贵，但是质量还可以', sentiment: 'neutral', score: 0.5 },
      { content: '体验很差，不会再买了', sentiment: 'negative', score: 0.8 },
      { content: '物流速度很快，包装也很精美', sentiment: 'positive', score: 0.85 },
      { content: '一般般，没有特别的惊喜', sentiment: 'neutral', score: 0.5 }
    ]
  } else if (analysisType.value === 'keywords') {
    analysisResults.value = [
      { word: '产品', frequency: 10, sentiment: 'positive' },
      { word: '服务', frequency: 8, sentiment: 'positive' },
      { word: '价格', frequency: 6, sentiment: 'negative' },
      { word: '质量', frequency: 5, sentiment: 'positive' },
      { word: '物流', frequency: 4, sentiment: 'positive' }
    ]
  } else if (analysisType.value === 'trend') {
    analysisResults.value = [
      { date: '2023-01-01', positive: 0.6, negative: 0.2, neutral: 0.2 },
      { date: '2023-01-02', positive: 0.62, negative: 0.19, neutral: 0.19 },
      { date: '2023-01-03', positive: 0.64, negative: 0.18, neutral: 0.18 },
      { date: '2023-01-04', positive: 0.66, negative: 0.17, neutral: 0.17 },
      { date: '2023-01-05', positive: 0.68, negative: 0.16, neutral: 0.16 },
      { date: '2023-01-06', positive: 0.70, negative: 0.15, neutral: 0.15 },
      { date: '2023-01-07', positive: 0.72, negative: 0.14, neutral: 0.14 }
    ]
    setTimeout(() => {
      renderTrendChart()
    }, 100)
  }
}

const renderTrendChart = () => {
  const chartDom = document.getElementById('trendChart')
  if (chartDom) {
    const myChart = echarts.init(chartDom)
    const option = {
      title: {
        text: '舆情趋势分析'
      },
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        data: ['正面', '负面', '中性']
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: analysisResults.value.map((item: any) => item.date)
      },
      yAxis: {
        type: 'value',
        min: 0,
        max: 1
      },
      series: [
        {
          name: '正面',
          type: 'line',
          stack: 'Total',
          data: analysisResults.value.map((item: any) => item.positive),
          itemStyle: {
            color: '#00B42A'
          }
        },
        {
          name: '负面',
          type: 'line',
          stack: 'Total',
          data: analysisResults.value.map((item: any) => item.negative),
          itemStyle: {
            color: '#F53F3F'
          }
        },
        {
          name: '中性',
          type: 'line',
          stack: 'Total',
          data: analysisResults.value.map((item: any) => item.neutral),
          itemStyle: {
            color: '#86909C'
          }
        }
      ]
    }
    myChart.setOption(option)
  }
}

watch(analysisResults, (newVal) => {
  if (newVal && analysisType.value === 'trend') {
    setTimeout(() => {
      renderTrendChart()
    }, 100)
  }
})
</script>

<style scoped>
/* Analysis page styles */
</style>