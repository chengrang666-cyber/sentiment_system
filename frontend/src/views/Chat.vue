<template>
  <div class="chat">
    <h1 class="page-title">AI对话</h1>
    
    <div class="chat-container">
      <!-- 聊天记录 -->
      <div class="chat-messages">
        <div class="message ai-message">
          <div class="message-content">
            <p>您好！我是 SentimentAI 智能助手，有什么可以帮助您的吗？</p>
          </div>
        </div>
        <div v-for="(msg, index) in messages" :key="index" class="message" :class="msg.type">
          <div class="message-content">
            <p>{{ msg.content }}</p>
          </div>
        </div>
      </div>
      
      <!-- 输入框 -->
      <div class="chat-input">
        <el-input
          v-model="inputMessage"
          placeholder="请输入您的问题..."
          @keyup.enter="sendMessage"
          type="textarea"
          :rows="2"
        ></el-input>
        <el-button type="primary" @click="sendMessage">发送</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Chat',
  data() {
    return {
      inputMessage: '',
      messages: []
    }
  },
  methods: {
    sendMessage() {
      if (!this.inputMessage.trim()) return
      
      // 添加用户消息
      this.messages.push({
        type: 'user-message',
        content: this.inputMessage
      })
      
      // 模拟AI回复
      setTimeout(() => {
        this.messages.push({
          type: 'ai-message',
          content: '这是一条模拟的AI回复，实际项目中会调用真实的大模型API。'
        })
      }, 1000)
      
      this.inputMessage = ''
    }
  }
}
</script>

<style scoped>
.chat {
  width: 100%;
  height: 100%;
}

.page-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 24px;
  color: #e2e8f0;
}

.chat-container {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 20px;
  height: calc(100vh - 180px);
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 20px;
}

.message {
  margin-bottom: 16px;
  max-width: 80%;
}

.user-message {
  align-self: flex-end;
  margin-left: auto;
}

.ai-message {
  align-self: flex-start;
  margin-right: auto;
}

.message-content {
  padding: 12px 16px;
  border-radius: 8px;
}

.user-message .message-content {
  background-color: #3b82f6;
  color: white;
  border-bottom-right-radius: 2px;
}

.ai-message .message-content {
  background-color: #334155;
  color: #e2e8f0;
  border-bottom-left-radius: 2px;
}

.chat-input {
  display: flex;
  gap: 10px;
}

.chat-input .el-input {
  flex: 1;
}

.chat-input .el-textarea__inner {
  background-color: #334155;
  border: 1px solid #475569;
  color: #e2e8f0;
  resize: none;
}

.chat-input .el-textarea__inner:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
}
</style>
