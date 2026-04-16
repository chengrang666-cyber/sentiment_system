<template>
  <div class="dashboard">
    <h1 class="dashboard-title">实时舆情监控大屏</h1>
    
    <!-- 统计卡片 -->
    <div class="stats-container">
      <div class="stat-card">
        <div class="stat-icon">📋</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.totalTasks }}</div>
          <div class="stat-label">总任务数</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">💬</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.collectedComments }}</div>
          <div class="stat-label">采集评论数</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">✅</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.analyzedComments }}</div>
          <div class="stat-label">已分析数</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">⭐</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.averageSentiment }}</div>
          <div class="stat-label">平均情感分</div>
        </div>
      </div>
    </div>
    
    <!-- 图表区域 -->
    <div class="charts-container">
      <!-- 情感分布 -->
      <div class="chart-card">
        <div class="chart-header">
          <h3>情感分布</h3>
          <div class="chart-controls">
            <button class="control-btn" :class="{ active: timeRange === 'day' }" @click="timeRange = 'day'">日</button>
            <button class="control-btn" :class="{ active: timeRange === 'week' }" @click="timeRange = 'week'">周</button>
            <button class="control-btn" :class="{ active: timeRange === 'month' }" @click="timeRange = 'month'">月</button>
          </div>
        </div>
        <div ref="sentimentChart" class="chart-content"></div>
      </div>
      
      <!-- 高频关键词云 -->
      <div class="chart-card">
        <div class="chart-header">
          <h3>高频关键词云</h3>
          <button class="refresh-btn" @click="refreshKeywords">🔄 刷新</button>
        </div>
        <div ref="keywordCloud" class="chart-content"></div>
      </div>
    </div>
    
    <!-- 舆情趋势 -->
    <div class="chart-card full-width">
      <div class="chart-header">
        <h3>舆情趋势 (近7天)</h3>
        <div class="chart-controls">
          <button class="control-btn" :class="{ active: trendType === 'sentiment' }" @click="trendType = 'sentiment'">情感趋势</button>
          <button class="control-btn" :class="{ active: trendType === 'heat' }" @click="trendType = 'heat'">热度趋势</button>
        </div>
      </div>
      <div ref="trendChart" class="chart-content"></div>
    </div>
    
    <!-- 最近评论 -->
    <div class="comments-section">
      <h3 class="section-title">最近评论</h3>
      <div class="comments-table">
        <table>
          <thead>
            <tr>
              <th>评论内容</th>
              <th>平台</th>
              <th>情感</th>
              <th>时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="comment in recentComments" :key="comment.id">
              <td>{{ comment.content }}</td>
              <td>{{ comment.platform }}</td>
              <td>
                <span class="sentiment-tag" :class="comment.sentiment">{{ comment.sentimentText }}</span>
              </td>
              <td>{{ comment.time }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <button class="view-all-btn">查看全部</button>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
import 'echarts-wordcloud'

export default {
  name: 'Dashboard',
  data() {
    return {
      stats: {
        totalTasks: 1,
        collectedComments: 5,
        analyzedComments: 5,
        averageSentiment: 3.2
      },
      timeRange: 'week',
      trendType: 'sentiment',
      recentComments: [
        {
          id: 1,
          content: '这个产品非常好，服务也很周到',
          platform: '微博',
          sentiment: 'positive',
          sentimentText: '正面',
          time: '2023-01-01 12:00'
        },
        {
          id: 2,
          content: '价格有点贵，但是质量还可以',
          platform: '微博',
          sentiment: 'neutral',
          sentimentText: '中性',
          time: '2023-01-02 10:30'
        }
      ],
      sentimentChart: null,
      keywordCloud: null,
      trendChart: null
    }
  },
  mounted() {
    this.initCharts()
  },
  methods: {
    initCharts() {
      this.initSentimentChart()
      this.initKeywordCloud()
      this.initTrendChart()
    },
    initSentimentChart() {
      const chartDom = this.$refs.sentimentChart
      this.sentimentChart = echarts.init(chartDom)
      
      const option = {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          textStyle: {
            color: '#e2e8f0'
          }
        },
        series: [
          {
            name: '情感分布',
            type: 'pie',
            radius: '70%',
            data: [
              { value: 3, name: '正面', itemStyle: { color: '#10b981' } },
              { value: 1, name: '中性', itemStyle: { color: '#f59e0b' } },
              { value: 1, name: '负面', itemStyle: { color: '#ef4444' } }
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            label: {
              color: '#e2e8f0'
            }
          }
        ]
      }
      
      this.sentimentChart.setOption(option)
    },
    initKeywordCloud() {
      const chartDom = this.$refs.keywordCloud
      this.keywordCloud = echarts.init(chartDom)
      
      const option = {
        series: [
          {
            type: 'wordCloud',
            shape: 'circle',
            left: 'center',
            top: 'center',
            width: '80%',
            height: '80%',
            right: null,
            bottom: null,
            sizeRange: [12, 50],
            rotationRange: [-45, 45],
            rotationStep: 45,
            gridSize: 8,
            drawOutOfBound: false,
            textStyle: {
              fontFamily: 'sans-serif',
              fontWeight: 'bold',
              color: function() {
                return 'rgb(' + [
                  Math.round(Math.random() * 160),
                  Math.round(Math.random() * 160),
                  Math.round(Math.random() * 255)
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
            data: [
              { name: '产品', value: 100 },
              { name: '服务', value: 80 },
              { name: '质量', value: 70 },
              { name: '价格', value: 60 },
              { name: '体验', value: 50 },
              { name: '物流', value: 40 },
              { name: '客服', value: 30 },
              { name: '包装', value: 20 }
            ]
          }
        ]
      }
      
      this.keywordCloud.setOption(option)
    },
    initTrendChart() {
      const chartDom = this.$refs.trendChart
      this.trendChart = echarts.init(chartDom)
      
      const option = {
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['正面', '中性', '负面'],
          textStyle: {
            color: '#e2e8f0'
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['12-26', '12-27', '12-28', '12-29', '12-30', '12-31', '01-01'],
          axisLabel: {
            color: '#94a3b8'
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            color: '#94a3b8'
          }
        },
        series: [
          {
            name: '正面',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210],
            lineStyle: {
              color: '#10b981'
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(16, 185, 129, 0.5)' },
                { offset: 1, color: 'rgba(16, 185, 129, 0.1)' }
              ])
            }
          },
          {
            name: '中性',
            type: 'line',
            stack: 'Total',
            data: [220, 182, 191, 234, 290, 330, 310],
            lineStyle: {
              color: '#f59e0b'
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(245, 158, 11, 0.5)' },
                { offset: 1, color: 'rgba(245, 158, 11, 0.1)' }
              ])
            }
          },
          {
            name: '负面',
            type: 'line',
            stack: 'Total',
            data: [150, 232, 201, 154, 190, 330, 410],
            lineStyle: {
              color: '#ef4444'
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(239, 68, 68, 0.5)' },
                { offset: 1, color: 'rgba(239, 68, 68, 0.1)' }
              ])
            }
          }
        ]
      }
      
      this.trendChart.setOption(option)
    },
    refreshKeywords() {
      // 模拟刷新关键词云
      this.keywordCloud.dispose()
      this.initKeywordCloud()
    }
  }
}
</script>

<style scoped>
.dashboard {
  width: 100%;
  height: 100%;
}

.dashboard-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 24px;
  color: #e2e8f0;
}

.stats-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  font-size: 24px;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(59, 130, 246, 0.1);
  border-radius: 8px;
}

.stat-info {
  flex: 1;
}

.stat-value {
  font-size: 24px;
  font-weight: bold;
  color: #e2e8f0;
}

.stat-label {
  font-size: 14px;
  color: #94a3b8;
  margin-top: 4px;
}

.charts-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 24px;
}

.chart-card {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.chart-card.full-width {
  grid-column: 1 / -1;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.chart-header h3 {
  font-size: 16px;
  font-weight: bold;
  color: #e2e8f0;
}

.chart-controls {
  display: flex;
  gap: 8px;
}

.control-btn {
  padding: 4px 12px;
  border: 1px solid #3b82f6;
  background-color: transparent;
  color: #94a3b8;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.control-btn.active {
  background-color: #3b82f6;
  color: #ffffff;
}

.refresh-btn {
  padding: 4px 12px;
  border: 1px solid #3b82f6;
  background-color: transparent;
  color: #94a3b8;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.refresh-btn:hover {
  background-color: rgba(59, 130, 246, 0.1);
}

.chart-content {
  height: 300px;
}

.comments-section {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 16px;
  font-weight: bold;
  color: #e2e8f0;
  margin-bottom: 16px;
}

.comments-table {
  margin-bottom: 16px;
  overflow-x: auto;
}

.comments-table table {
  width: 100%;
  border-collapse: collapse;
}

.comments-table th,
.comments-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #334155;
}

.comments-table th {
  font-size: 14px;
  font-weight: bold;
  color: #94a3b8;
}

.comments-table td {
  font-size: 14px;
  color: #e2e8f0;
}

.sentiment-tag {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}

.sentiment-tag.positive {
  background-color: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.sentiment-tag.neutral {
  background-color: rgba(245, 158, 11, 0.2);
  color: #f59e0b;
}

.sentiment-tag.negative {
  background-color: rgba(239, 68, 68, 0.2);
  color: #ef4444;
}

.view-all-btn {
  padding: 8px 16px;
  border: 1px solid #3b82f6;
  background-color: transparent;
  color: #3b82f6;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  float: right;
}

.view-all-btn:hover {
  background-color: rgba(59, 130, 246, 0.1);
}
</style>
