# AI翻译助手

中文转英文翻译工具，包含后端API + Flutter前端界面。调用DeepSeek大模型API实现翻译和关键词提取。

## 项目结构

```
ai_translator/
├── backend/
│   ├── main.py              # FastAPI 后端接口
│   └── requirements.txt     # Python 依赖
├── frontend/
│   └── ai_translator_app/   # Flutter 前端项目
├── screenshots/             # AI对话截图
└── README.md
```

## 运行说明

### 1. 启动后端

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

后端运行在 http://127.0.0.1:8000 ，可访问 http://127.0.0.1:8000/docs 查看接口文档。

### 2. 启动前端（Flutter）

```bash
cd frontend/ai_translator_app
flutter pub get
flutter run -d chrome
```

### 3. 使用方式

1. 在输入框中输入中文文本
2. 点击「点击翻译」按钮
3. 页面展示英文翻译结果和关键词

## 技术栈

- **后端**：Python + FastAPI + DeepSeek API
- **前端**：Flutter (Dart)
- **AI工具**：Claude（用于辅助开发）

## 开发过程

### AI使用说明

本项目全程借助 Claude 进行辅助开发，主要包括：

1. **环境搭建**：通过与 Claude 对话，完成了 Flutter SDK、Android Studio、Android SDK 的安装配置
2. **后端代码**：FastAPI 接口代码由 Claude 生成，我根据实际运行情况进行了调试（如添加 CORS 中间件解决跨域问题）
3. **前端代码**：Flutter 界面代码由 Claude 生成，包含输入框、翻译按钮和结果展示区
4. **问题解决**：遇到 Android SDK 路径识别、跨域请求失败等问题，均通过与 Claude 对话解决

### AI生成 vs 手动修改

- **AI生成**：main.py 后端接口代码、main.dart 前端界面代码、项目结构建议
- **手动操作**：环境安装配置、项目创建、文件组织、运行调试、问题排查

详细的 AI 对话截图见 `screenshots/` 目录。

## API接口

### POST /translate

**请求：**
```json
{
  "text": "人工智能改变世界"
}
```

**返回：**
```json
{
  "translation": "Artificial intelligence changes the world",
  "keywords": ["artificial intelligence", "changes", "world"]
}
```