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
            <li><router-link to="/visualization" class="hover:text-gray-200 font-semibold">可视化</router-link></li>
            <li><router-link to="/management" class="hover:text-gray-200">管理</router-link></li>
          </ul>
        </nav>
      </div>
    </header>

    <!-- 主内容区 -->
    <main class="container mx-auto px-4 py-8">
      <div class="bg-white rounded-lg shadow-md p-8 mb-8">
        <h2 class="text-2xl font-semibold mb-6 text-primary">可视化展示</h2>
        
        <!-- 可视化配置 -->
        <div class="mb-8">
          <h3 class="text-lg font-semibold mb-4">可视化配置</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-gray-700 mb-2">选择分析任务</label>
              <select 
                v-model="selectedTask" 
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
              >
                <option value="">请选择分析任务</option>
                <option v-for="task in tasks" :key="task.id" :value="task.id">
                  {{ task.id }} - {{ task.platform }} - {{ task.keywords }}
                </option>
              </select>
            </div>
            <div>
              <label class="block text-gray-700 mb-2">时间范围</label>
              <select 
                v-model="timeRange" 
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
              >
                <option value="day">按天</option>
                <option value="week">按周</option>
                <option value="month">按月</option>
              </select>
            </div>
          </div>
          <div class="mt-6">
            <button 
              @click="loadVisualization" 
              class="bg-primary text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition-colors"
            >
              加载可视化
            </button>
          </div>
        </div>

        <!-- 可视化结果 -->
        <div v-if="visualizationData" class="mt-8">
          <!-- 情感分布饼图 -->
          <div class="mb-8">
            <h3 class="text-lg font-semibold mb-4">情感分布</h3>
            <div class="h-80">
              <div id="sentimentChart" class="w-full h-full"></div>
            </div>
          </div>

          <!-- 舆情趋势折线图 -->
          <div class="mb-8">
            <h3 class="text-lg font-semibold mb-4">舆情趋势</h3>
            <div class="h-80">
              <div id="trendChart" class="w-full h-full"></div>
            </div>
          </div>

          <!-- 高频关键词云 -->
          <div class="mb-8">
            <h3 class="text-lg font-semibold mb-4">高频关键词</h3>
            <div class="h-80 border rounded-lg p-4">
              <div id="keywordCloud" class="w-full h-full"></div>
            </div>
          </div>

          <!-- 评论样本 -->
          <div>
            <h3 class="text-lg font-semibold mb-4">评论样本</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div v-for="(comment, index) in visualizationData.comments" :key="index" class="border rounded-lg p-4">
                <div class="flex justify-between items-start">
                  <p class="text-gray-700">{{ comment.content }}</p>
                  <span 
                    class="px-2 py-1 rounded-full text-xs"
                    :class="comment.sentiment === 'positive' ? 'bg-green-100 text-green-800' : comment.sentiment === 'negative' ? 'bg-red-100 text-red-800' : 'bg-gray-100 text-gray-800'"
                  >
                    {{ comment.sentiment === 'positive' ? '正面' : comment.sentiment === 'negative' ? '负面' : '中性' }}
                  </span>
                </div>
                <div class="mt-2 text-sm text-gray-500">
                  {{ comment.platform }} - {{ comment.created_at }}
                </div>
              </div>
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
import { ref, watch } from 'vue'
import * as echarts from 'echarts'

const selectedTask = ref('')
const timeRange = ref('day')
const visualizationData = ref<any>(null)

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

const loadVisualization = () => {
  // 模拟可视化数据
  visualizationData.value = {
    sentiment: {
      positive: 60,
      negative: 20,
      neutral: 20
    },
    trends: [
      { date: '2023-01-01', positive: 0.6, negative: 0.2, neutral: 0.2 },
      { date: '2023-01-02', positive: 0.62, negative: 0.19, neutral: 0.19 },
      { date: '2023-01-03', positive: 0.64, negative: 0.18, neutral: 0.18 },
      { date: '2023-01-04', positive: 0.66, negative: 0.17, neutral: 0.17 },
      { date: '2023-01-05', positive: 0.68, negative: 0.16, neutral: 0.16 },
      { date: '2023-01-06', positive: 0.70, negative: 0.15, neutral: 0.15 },
      { date: '2023-01-07', positive: 0.72, negative: 0.14, neutral: 0.14 }
    ],
    keywords: [
      { name: '产品', value: 10, sentiment: 'positive' },
      { name: '服务', value: 8, sentiment: 'positive' },
      { name: '价格', value: 6, sentiment: 'negative' },
      { name: '质量', value: 5, sentiment: 'positive' },
      { name: '物流', value: 4, sentiment: 'positive' },
      { name: '包装', value: 3, sentiment: 'positive' },
      { name: '体验', value: 3, sentiment: 'negative' },
      { name: '速度', value: 2, sentiment: 'positive' },
      { name: '客服', value: 2, sentiment: 'positive' },
      { name: '性价比', value: 2, sentiment: 'neutral' }
    ],
    comments: [
      { content: '这个产品非常好，服务也很周到', sentiment: 'positive', platform: '微博', created_at: '2023-01-01 12:00:00' },
      { content: '价格有点贵，但是质量还可以', sentiment: 'neutral', platform: '微博', created_at: '2023-01-02 10:30:00' },
      { content: '体验很差，不会再买了', sentiment: 'negative', platform: '抖音', created_at: '2023-01-03 15:20:00' },
      { content: '物流速度很快，包装也很精美', sentiment: 'positive', platform: '抖音', created_at: '2023-01-04 09:15:00' }
    ]
  }
  
  setTimeout(() => {
    renderSentimentChart()
    renderTrendChart()
    renderKeywordCloud()
  }, 100)
}

const renderSentimentChart = () => {
  const chartDom = document.getElementById('sentimentChart')
  if (chartDom) {
    const myChart = echarts.init(chartDom)
    const option = {
      title: {
        text: '情感分布',
        left: 'center'
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: ['正面', '负面', '中性']
      },
      series: [
        {
          name: '情感分布',
          type: 'pie',
          radius: '50%',
          data: [
            { value: visualizationData.value.sentiment.positive, name: '正面', itemStyle: { color: '#00B42A' } },
            { value: visualizationData.value.sentiment.negative, name: '负面', itemStyle: { color: '#F53F3F' } },
            { value: visualizationData.value.sentiment.neutral, name: '中性', itemStyle: { color: '#86909C' } }
          ],
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }
      ]
    }
    myChart.setOption(option)
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
        data: visualizationData.value.trends.map((item: any) => item.date)
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
          data: visualizationData.value.trends.map((item: any) => item.positive),
          itemStyle: {
            color: '#00B42A'
          }
        },
        {
          name: '负面',
          type: 'line',
          stack: 'Total',
          data: visualizationData.value.trends.map((item: any) => item.negative),
          itemStyle: {
            color: '#F53F3F'
          }
        },
        {
          name: '中性',
          type: 'line',
          stack: 'Total',
          data: visualizationData.value.trends.map((item: any) => item.neutral),
          itemStyle: {
            color: '#86909C'
          }
        }
      ]
    }
    myChart.setOption(option)
  }
}

const renderKeywordCloud = () => {
  const chartDom = document.getElementById('keywordCloud')
  if (chartDom) {
    const myChart = echarts.init(chartDom)
    const option = {
      title: {
        text: '高频关键词',
        left: 'center'
      },
      tooltip: {},
      series: [
        {
          type: 'wordCloud',
          shape: 'circle',
          left: 'center',
          top: 'center',
          width: '90%',
          height: '90%',
          right: null,
          bottom: null,
          sizeRange: [12, 60],
          rotationRange: [-90, 90],
          rotationStep: 45,
          gridSize: 8,
          drawOutOfBound: false,
          textStyle: {
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            color: function () {
              return 'rgb(' + [
                Math.round(Math.random() * 160),
                Math.round(Math.random() * 160),
                Math.round(Math.random() * 160)
              ].join(',') + ')'
            }
          },
          emphasis: {
            focus: 'self',
            textStyle: {
              shadowBlur: 10,
              shadowColor: '#333'
            }
          },
          data: visualizationData.value.keywords.map((item: any) => ({
            name: item.name,
            value: item.value
          }))
        }
      ]
    }
    myChart.setOption(option)
  }
}

watch(visualizationData, (newVal) => {
  if (newVal) {
    setTimeout(() => {
      renderSentimentChart()
      renderTrendChart()
      renderKeywordCloud()
    }, 100)
  }
})
</script>

<style scoped>
/* Visualization page styles */
</style>