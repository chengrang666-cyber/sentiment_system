<template>
  <div class="comments">
    <h1 class="page-title">评论浏览</h1>
    
    <!-- 搜索和筛选 -->
    <div class="comment-filter">
      <el-input v-model="searchKeyword" placeholder="搜索评论内容" style="width: 300px; margin-right: 10px;"></el-input>
      <el-select v-model="platformFilter" placeholder="选择平台" style="width: 120px; margin-right: 10px;">
        <el-option label="全部" value=""></el-option>
        <el-option label="微博" value="微博"></el-option>
        <el-option label="抖音" value="抖音"></el-option>
      </el-select>
      <el-select v-model="sentimentFilter" placeholder="情感筛选" style="width: 120px;">
        <el-option label="全部" value=""></el-option>
        <el-option label="正面" value="positive"></el-option>
        <el-option label="中性" value="neutral"></el-option>
        <el-option label="负面" value="negative"></el-option>
      </el-select>
    </div>
    
    <!-- 评论列表 -->
    <div class="comment-list">
      <el-table :data="filteredComments" style="width: 100%">
        <el-table-column prop="id" label="ID" width="80"></el-table-column>
        <el-table-column prop="content" label="评论内容"></el-table-column>
        <el-table-column prop="platform" label="平台" width="100"></el-table-column>
        <el-table-column prop="sentiment" label="情感" width="120">
          <template #default="scope">
            <span class="sentiment-tag" :class="scope.row.sentiment">{{ getSentimentText(scope.row.sentiment) }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="sentiment_score" label="情感分数" width="120"></el-table-column>
        <el-table-column prop="time" label="时间"></el-table-column>
      </el-table>
      
      <!-- 分页 -->
      <div class="pagination">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[10, 20, 50, 100]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="filteredComments.length"
        ></el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Comments',
  data() {
    return {
      searchKeyword: '',
      platformFilter: '',
      sentimentFilter: '',
      currentPage: 1,
      pageSize: 10,
      comments: [
        {
          id: 1,
          content: '这个产品非常好，服务也很周到',
          platform: '微博',
          sentiment: 'positive',
          sentiment_score: 0.8,
          time: '2023-01-01 12:00'
        },
        {
          id: 2,
          content: '价格有点贵，但是质量还可以',
          platform: '微博',
          sentiment: 'neutral',
          sentiment_score: 0.5,
          time: '2023-01-02 10:30'
        },
        {
          id: 3,
          content: '质量太差了，退款！',
          platform: '抖音',
          sentiment: 'negative',
          sentiment_score: 0.2,
          time: '2023-01-03 15:45'
        }
      ]
    }
  },
  computed: {
    filteredComments() {
      let result = this.comments
      
      // 搜索关键词
      if (this.searchKeyword) {
        result = result.filter(comment => comment.content.includes(this.searchKeyword))
      }
      
      // 平台筛选
      if (this.platformFilter) {
        result = result.filter(comment => comment.platform === this.platformFilter)
      }
      
      // 情感筛选
      if (this.sentimentFilter) {
        result = result.filter(comment => comment.sentiment === this.sentimentFilter)
      }
      
      return result
    }
  },
  methods: {
    getSentimentText(sentiment) {
      switch (sentiment) {
        case 'positive':
          return '正面'
        case 'neutral':
          return '中性'
        case 'negative':
          return '负面'
        default:
          return '未知'
      }
    },
    handleSizeChange(size) {
      this.pageSize = size
    },
    handleCurrentChange(current) {
      this.currentPage = current
    }
  }
}
</script>

<style scoped>
.comments {
  width: 100%;
  height: 100%;
}

.page-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 24px;
  color: #e2e8f0;
}

.comment-filter {
  margin-bottom: 24px;
  display: flex;
  align-items: center;
}

.comment-list {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.el-table {
  background-color: transparent;
  margin-bottom: 20px;
}

.el-table th {
  background-color: rgba(59, 130, 246, 0.1);
  color: #94a3b8;
  border-bottom: 1px solid #334155;
}

.el-table td {
  background-color: transparent;
  color: #e2e8f0;
  border-bottom: 1px solid #334155;
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

.pagination {
  display: flex;
  justify-content: flex-end;
}

.el-pagination button,
.el-pagination span {
  color: #94a3b8;
}

.el-pagination .el-pager li {
  color: #94a3b8;
}

.el-pagination .el-pager li.active {
  color: #3b82f6;
}
</style>
