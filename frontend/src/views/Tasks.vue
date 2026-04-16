<template>
  <div class="tasks">
    <h1 class="page-title">任务管理</h1>
    
    <!-- 任务创建表单 -->
    <div class="task-form">
      <h3>创建新任务</h3>
      <el-form :model="newTask" label-width="100px">
        <el-form-item label="关键词">
          <el-input v-model="newTask.keyword" placeholder="请输入关键词"></el-input>
        </el-form-item>
        <el-form-item label="平台">
          <el-select v-model="newTask.platform" placeholder="请选择平台">
            <el-option label="微博" value="微博"></el-option>
            <el-option label="抖音" value="抖音"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="开始日期">
          <el-date-picker v-model="newTask.startDate" type="datetime" placeholder="选择开始日期"></el-date-picker>
        </el-form-item>
        <el-form-item label="结束日期">
          <el-date-picker v-model="newTask.endDate" type="datetime" placeholder="选择结束日期"></el-date-picker>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="createTask">创建任务</el-button>
        </el-form-item>
      </el-form>
    </div>
    
    <!-- 任务列表 -->
    <div class="task-list">
      <h3>任务列表</h3>
      <el-table :data="tasks" style="width: 100%">
        <el-table-column prop="id" label="任务ID" width="80"></el-table-column>
        <el-table-column prop="keyword" label="关键词"></el-table-column>
        <el-table-column prop="platform" label="平台" width="100"></el-table-column>
        <el-table-column prop="status" label="状态" width="120">
          <template #default="scope">
            <el-tag :type="getTagType(scope.row.status)">{{ scope.row.status }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="collected_count" label="采集数" width="100"></el-table-column>
        <el-table-column prop="analyzed_count" label="分析数" width="100"></el-table-column>
        <el-table-column label="操作" width="180">
          <template #default="scope">
            <el-button size="small" @click="startTask(scope.row.id)">开始</el-button>
            <el-button size="small" @click="pauseTask(scope.row.id)">暂停</el-button>
            <el-button size="small" @click="viewTask(scope.row.id)">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tasks',
  data() {
    return {
      newTask: {
        keyword: '',
        platform: '',
        startDate: '',
        endDate: ''
      },
      tasks: [
        {
          id: 1,
          keyword: '产品质量',
          platform: '微博',
          status: 'completed',
          collected_count: 5,
          analyzed_count: 5
        }
      ]
    }
  },
  methods: {
    createTask() {
      const task = {
        id: this.tasks.length + 1,
        keyword: this.newTask.keyword,
        platform: this.newTask.platform,
        status: 'pending',
        collected_count: 0,
        analyzed_count: 0
      }
      this.tasks.push(task)
      this.newTask = {
        keyword: '',
        platform: '',
        startDate: '',
        endDate: ''
      }
    },
    startTask(id) {
      const task = this.tasks.find(t => t.id === id)
      if (task) {
        task.status = 'running'
      }
    },
    pauseTask(id) {
      const task = this.tasks.find(t => t.id === id)
      if (task) {
        task.status = 'paused'
      }
    },
    viewTask(id) {
      // 跳转到任务详情页
      console.log('查看任务', id)
    },
    getTagType(status) {
      switch (status) {
        case 'completed':
          return 'success'
        case 'running':
          return 'warning'
        case 'pending':
          return 'info'
        case 'paused':
          return 'danger'
        default:
          return 'info'
      }
    }
  }
}
</script>

<style scoped>
.tasks {
  width: 100%;
  height: 100%;
}

.page-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 24px;
  color: #e2e8f0;
}

.task-form {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.task-form h3 {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #e2e8f0;
}

.task-list {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.task-list h3 {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #e2e8f0;
}

.el-table {
  background-color: transparent;
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
</style>
