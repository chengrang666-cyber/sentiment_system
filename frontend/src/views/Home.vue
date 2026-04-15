<template>
  <div class="space-y-8">
    <!-- 实时舆情监控大屏标题 -->
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
      <h2 class="text-2xl md:text-3xl font-bold text-blue-400 mb-4 md:mb-0">
        <span class="inline-block animate-pulse mr-2">●</span>
        实时舆情监控大屏
      </h2>
      <div class="flex items-center space-x-4 w-full md:w-auto">
        <div class="relative w-full md:w-48">
          <select class="w-full bg-gray-800 text-white border border-gray-700 rounded-lg px-4 py-2 appearance-none focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
            <option>--全部任务--</option>
            <option>任务 1</option>
            <option>任务 2</option>
            <option>任务 3</option>
          </select>
          <div class="absolute right-3 top-1/2 transform -translate-y-1/2 pointer-events-none">
            <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </div>
        </div>
        <button class="bg-gray-800 text-white border border-gray-700 rounded-lg px-4 py-2 hover:bg-gray-700 transition-all duration-300 transform hover:scale-105 flex items-center">
          <svg class="w-4 h-4 mr-2 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
          </svg>
          刷新
        </button>
      </div>
    </div>

    <!-- 统计卡片 -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <!-- 总任务数 -->
      <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/10 hover:border-blue-500/30">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-sm text-gray-400 mb-1 font-medium">总任务数</h3>
            <p class="text-3xl font-bold text-white">1</p>
          </div>
          <div class="bg-blue-900/30 p-3 rounded-lg">
            <svg class="w-6 h-6 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center">
          <span class="text-green-400 text-sm font-medium flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
            </svg>
            0 任务
          </span>
        </div>
      </div>
      
      <!-- 采集评论数 -->
      <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-green-500/10 hover:border-green-500/30">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-sm text-gray-400 mb-1 font-medium">采集评论数</h3>
            <p class="text-3xl font-bold text-green-400">5</p>
          </div>
          <div class="bg-green-900/30 p-3 rounded-lg">
            <svg class="w-6 h-6 text-green-400" fill="currentColor" viewBox="0 0 20 20">
              <path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z"></path>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center">
          <span class="text-green-400 text-sm font-medium flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
            </svg>
            5 条评论
          </span>
        </div>
      </div>
      
      <!-- 已分析数 -->
      <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-red-500/10 hover:border-red-500/30">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-sm text-gray-400 mb-1 font-medium">已分析数</h3>
            <p class="text-3xl font-bold text-red-400">5</p>
          </div>
          <div class="bg-red-900/30 p-3 rounded-lg">
            <svg class="w-6 h-6 text-red-400" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center">
          <span class="text-green-400 text-sm font-medium flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
            </svg>
            100% 完成
          </span>
        </div>
      </div>
      
      <!-- 平均情感分 -->
      <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-purple-500/10 hover:border-purple-500/30">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-sm text-gray-400 mb-1 font-medium">平均情感分</h3>
            <p class="text-3xl font-bold text-purple-400">3.2</p>
          </div>
          <div class="bg-purple-900/30 p-3 rounded-lg">
            <svg class="w-6 h-6 text-purple-400" fill="currentColor" viewBox="0 0 20 20">
              <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center">
          <span class="text-yellow-400 text-sm font-medium flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
            </svg>
            中性偏正面
          </span>
        </div>
      </div>
    </div>

    <!-- 图表区域 -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- 情感分布 -->
      <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/10">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-lg font-semibold text-gray-300">情感分布</h3>
          <div class="flex space-x-2">
            <button class="bg-gray-700 text-gray-300 px-3 py-1 rounded-lg text-sm hover:bg-gray-600 transition-colors">
              日
            </button>
            <button class="bg-blue-600 text-white px-3 py-1 rounded-lg text-sm">
              周
            </button>
            <button class="bg-gray-700 text-gray-300 px-3 py-1 rounded-lg text-sm hover:bg-gray-600 transition-colors">
              月
            </button>
          </div>
        </div>
        <div class="h-80">
          <div id="sentimentChart" class="w-full h-full"></div>
        </div>
      </div>
      
      <!-- 高频关键词云 -->
      <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-purple-500/10">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-lg font-semibold text-gray-300">高频关键词云</h3>
          <button class="bg-gray-700 text-gray-300 px-3 py-1 rounded-lg text-sm hover:bg-gray-600 transition-colors flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
            </svg>
            刷新
          </button>
        </div>
        <div class="h-80">
          <div id="keywordCloud" class="w-full h-full"></div>
        </div>
      </div>
    </div>

    <!-- 舆情趋势 -->
    <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-green-500/10">
      <div class="flex justify-between items-center mb-6">
        <h3 class="text-lg font-semibold text-gray-300">舆情趋势 (近7天)</h3>
        <div class="flex space-x-2">
          <button class="bg-blue-600 text-white px-3 py-1 rounded-lg text-sm">
            情感趋势
          </button>
          <button class="bg-gray-700 text-gray-300 px-3 py-1 rounded-lg text-sm hover:bg-gray-600 transition-colors">
            热度趋势
          </button>
        </div>
      </div>
      <div class="h-80">
        <div id="trendChart" class="w-full h-full"></div>
      </div>
    </div>

    <!-- 最近评论 -->
    <div class="bg-gray-800 rounded-xl border border-gray-700 p-6 transform transition-all duration-300 hover:shadow-lg hover:shadow-gray-500/10">
      <div class="flex justify-between items-center mb-6">
        <h3 class="text-lg font-semibold text-gray-300">最近评论</h3>
        <button class="bg-gray-700 text-gray-300 px-3 py-1 rounded-lg text-sm hover:bg-gray-600 transition-colors">
          查看全部
        </button>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead>
            <tr class="border-b border-gray-700">
              <th class="text-left py-3 px-4 text-sm font-medium text-gray-400">评论内容</th>
              <th class="text-left py-3 px-4 text-sm font-medium text-gray-400">平台</th>
              <th class="text-left py-3 px-4 text-sm font-medium text-gray-400">情感</th>
              <th class="text-left py-3 px-4 text-sm font-medium text-gray-400">时间</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-b border-gray-700 hover:bg-gray-750 transition-colors">
              <td class="py-3 px-4 text-sm text-gray-300">这个产品非常好，服务也很周到</td>
              <td class="py-3 px-4 text-sm text-gray-300">微博</td>
              <td class="py-3 px-4">
                <span class="px-2 py-1 rounded-full text-xs bg-green-900/30 text-green-400">正面</span>
              </td>
              <td class="py-3 px-4 text-sm text-gray-400">2023-01-01 12:00</td>
            </tr>
            <tr class="border-b border-gray-700 hover:bg-gray-750 transition-colors">
              <td class="py-3 px-4 text-sm text-gray-300">价格有点贵，但是质量还可以</td>
              <td class="py-3 px-4 text-sm text-gray-300">微博</td>
              <td class="py-3 px-4">
                <span class="px-2 py-1 rounded-full text-xs bg-gray-900/30 text-gray-400">中性</span>
              </td>
              <td class="py-3 px-4 text-sm text-gray-400">2023-01-02 10:30</td>
            </tr>
            <tr class="border-b border-gray-700 hover:bg-gray-750 transition-colors">
              <td class="py-3 px-4 text-sm text-gray-300">体验很差，不会再买了</td>
              <td class="py-3 px-4 text-sm text-gray-300">抖音</td>
              <td class="py-3 px-4">
                <span class="px-2 py-1 rounded-full text-xs bg-red-900/30 text-red-400">负面</span>
              </td>
              <td class="py-3 px-4 text-sm text-gray-400">2023-01-03 15:20</td>
            </tr>
            <tr class="hover:bg-gray-750 transition-colors">
              <td class="py-3 px-4 text-sm text-gray-300">物流速度很快，包装也很精美</td>
              <td class="py-3 px-4 text-sm text-gray-300">抖音</td>
              <td class="py-3 px-4">
                <span class="px-2 py-1 rounded-full text-xs bg-green-900/30 text-green-400">正面</span>
              </td>
              <td class="py-3 px-4 text-sm text-gray-400">2023-01-04 09:15</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as echarts from 'echarts'

const visualizationData = ref<any>(null)

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
    const myChart = echarts.init(chartDom, 'dark')
    const option = {
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)',
        backgroundColor: 'rgba(30, 30, 46, 0.9)',
        borderColor: '#444',
        textStyle: {
          color: '#fff'
        }
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: ['正面', '负面', '中性'],
        textStyle: {
          color: '#ccc'
        },
        itemWidth: 12,
        itemHeight: 12
      },
      series: [
        {
          name: '情感分布',
          type: 'pie',
          radius: ['40%', '70%'],
          center: ['60%', '50%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 10,
            borderColor: '#1f2937',
            borderWidth: 2
          },
          label: {
            show: false,
            position: 'center'
          },
          emphasis: {
            label: {
              show: true,
              fontSize: 20,
              fontWeight: 'bold',
              color: '#fff'
            },
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          },
          labelLine: {
            show: false
          },
          data: [
            { value: visualizationData.value.sentiment.positive, name: '正面', itemStyle: { color: '#00B42A' } },
            { value: visualizationData.value.sentiment.negative, name: '负面', itemStyle: { color: '#F53F3F' } },
            { value: visualizationData.value.sentiment.neutral, name: '中性', itemStyle: { color: '#86909C' } }
          ]
        }
      ],
      backgroundColor: 'transparent'
    }
    myChart.setOption(option)
    
    // 响应式调整
    window.addEventListener('resize', () => {
      myChart.resize()
    })
  }
}

const renderTrendChart = () => {
  const chartDom = document.getElementById('trendChart')
  if (chartDom) {
    const myChart = echarts.init(chartDom, 'dark')
    const option = {
      tooltip: {
        trigger: 'axis',
        backgroundColor: 'rgba(30, 30, 46, 0.9)',
        borderColor: '#444',
        textStyle: {
          color: '#fff'
        }
      },
      legend: {
        data: ['正面', '负面', '中性'],
        textStyle: {
          color: '#ccc'
        },
        top: 0
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
        data: visualizationData.value.trends.map((item: any) => item.date),
        axisLabel: {
          color: '#ccc'
        },
        axisLine: {
          lineStyle: {
            color: '#444'
          }
        },
        splitLine: {
          show: false
        }
      },
      yAxis: {
        type: 'value',
        min: 0,
        max: 1,
        axisLabel: {
          color: '#ccc'
        },
        axisLine: {
          lineStyle: {
            color: '#444'
          }
        },
        splitLine: {
          lineStyle: {
            color: '#333'
          }
        }
      },
      series: [
        {
          name: '正面',
          type: 'line',
          stack: 'Total',
          data: visualizationData.value.trends.map((item: any) => item.positive),
          itemStyle: {
            color: '#00B42A'
          },
          lineStyle: {
            width: 3
          },
          symbol: 'circle',
          symbolSize: 8,
          emphasis: {
            focus: 'series',
            itemStyle: {
              shadowBlur: 10,
              shadowColor: '#00B42A'
            }
          }
        },
        {
          name: '负面',
          type: 'line',
          stack: 'Total',
          data: visualizationData.value.trends.map((item: any) => item.negative),
          itemStyle: {
            color: '#F53F3F'
          },
          lineStyle: {
            width: 3
          },
          symbol: 'circle',
          symbolSize: 8,
          emphasis: {
            focus: 'series',
            itemStyle: {
              shadowBlur: 10,
              shadowColor: '#F53F3F'
            }
          }
        },
        {
          name: '中性',
          type: 'line',
          stack: 'Total',
          data: visualizationData.value.trends.map((item: any) => item.neutral),
          itemStyle: {
            color: '#86909C'
          },
          lineStyle: {
            width: 3
          },
          symbol: 'circle',
          symbolSize: 8,
          emphasis: {
            focus: 'series',
            itemStyle: {
              shadowBlur: 10,
              shadowColor: '#86909C'
            }
          }
        }
      ],
      backgroundColor: 'transparent'
    }
    myChart.setOption(option)
    
    // 响应式调整
    window.addEventListener('resize', () => {
      myChart.resize()
    })
  }
}

const renderKeywordCloud = () => {
  const chartDom = document.getElementById('keywordCloud')
  if (chartDom) {
    const myChart = echarts.init(chartDom, 'dark')
    const option = {
      tooltip: {
        backgroundColor: 'rgba(30, 30, 46, 0.9)',
        borderColor: '#444',
        textStyle: {
          color: '#fff'
        }
      },
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
              const colors = ['#00B42A', '#F53F3F', '#86909C', '#722ED1', '#13C2C2', '#FAAD14']
              return colors[Math.floor(Math.random() * colors.length)]
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
      ],
      backgroundColor: 'transparent'
    }
    myChart.setOption(option)
    
    // 响应式调整
    window.addEventListener('resize', () => {
      myChart.resize()
    })
  }
}

// 页面加载时自动加载数据
onMounted(() => {
  loadVisualization()
})

// 监听数据变化
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
/* 自定义滚动条 */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #1f2937;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: #374151;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #4b5563;
}

/* 动画效果 */
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
</style>