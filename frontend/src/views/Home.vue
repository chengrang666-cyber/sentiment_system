<template>
  <div class="space-y-6">
    <!-- 实时舆情监控大屏标题 -->
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold text-blue-400">实时舆情监控大屏</h2>
      <div class="flex items-center space-x-4">
        <select class="bg-gray-800 text-white border border-gray-700 rounded px-3 py-1">
          <option>--全部任务--</option>
        </select>
        <button class="bg-gray-800 text-white border border-gray-700 rounded px-3 py-1 hover:bg-gray-700 transition-colors">
          刷新
        </button>
      </div>
    </div>

    <!-- 统计卡片 -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 总任务数 -->
      <div class="bg-gray-800 rounded-lg border border-gray-700 p-4">
        <h3 class="text-sm text-gray-400 mb-1">总任务数</h3>
        <p class="text-2xl font-bold text-white">1</p>
      </div>
      <!-- 采集评论数 -->
      <div class="bg-gray-800 rounded-lg border border-gray-700 p-4">
        <h3 class="text-sm text-gray-400 mb-1">采集评论数</h3>
        <p class="text-2xl font-bold text-green-400">5</p>
      </div>
      <!-- 已分析数 -->
      <div class="bg-gray-800 rounded-lg border border-gray-700 p-4">
        <h3 class="text-sm text-gray-400 mb-1">已分析数</h3>
        <p class="text-2xl font-bold text-red-400">5</p>
      </div>
      <!-- 平均情感分 -->
      <div class="bg-gray-800 rounded-lg border border-gray-700 p-4">
        <h3 class="text-sm text-gray-400 mb-1">平均情感分</h3>
        <p class="text-2xl font-bold text-purple-400">3.2</p>
      </div>
    </div>

    <!-- 图表区域 -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- 情感分布 -->
      <div class="bg-gray-800 rounded-lg border border-gray-700 p-4">
        <h3 class="text-sm text-gray-400 mb-4">情感分布</h3>
        <div class="h-80">
          <div id="sentimentChart" class="w-full h-full"></div>
        </div>
      </div>
      <!-- 高频关键词云 -->
      <div class="bg-gray-800 rounded-lg border border-gray-700 p-4">
        <h3 class="text-sm text-gray-400 mb-4">高频关键词云</h3>
        <div class="h-80">
          <div id="keywordCloud" class="w-full h-full"></div>
        </div>
      </div>
    </div>

    <!-- 舆情趋势 -->
    <div class="bg-gray-800 rounded-lg border border-gray-700 p-4">
      <h3 class="text-sm text-gray-400 mb-4">舆情趋势 (近7天)</h3>
      <div class="h-80">
        <div id="trendChart" class="w-full h-full"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
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
    const myChart = echarts.init(chartDom)
    const option = {
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: ['正面', '负面', '中性'],
        textStyle: {
          color: '#ccc'
        }
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
      ],
      backgroundColor: 'transparent'
    }
    myChart.setOption(option)
  }
}

const renderTrendChart = () => {
  const chartDom = document.getElementById('trendChart')
  if (chartDom) {
    const myChart = echarts.init(chartDom)
    const option = {
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        data: ['正面', '负面', '中性'],
        textStyle: {
          color: '#ccc'
        }
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
      ],
      backgroundColor: 'transparent'
    }
    myChart.setOption(option)
  }
}

const renderKeywordCloud = () => {
  const chartDom = document.getElementById('keywordCloud')
  if (chartDom) {
    const myChart = echarts.init(chartDom)
    const option = {
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
      ],
      backgroundColor: 'transparent'
    }
    myChart.setOption(option)
  }
}

// 页面加载时自动加载数据
onMounted(() => {
  loadVisualization()
})
</script>