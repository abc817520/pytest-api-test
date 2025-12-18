# DummyJSON 接口自动化测试框架

本项目是一个针对 [DummyJSON](https://dummyjson.com/) 的接口自动化测试框架，基于 Python + Pytest + Requests + Allure 构建。

## 📁 项目结构

```
dummyjson-api-test/
├── api/                # API 封装层
├── common/             # 公共工具类 (Requests, Token 管理等)
├── config/             # 配置文件
├── data/               # 测试数据 (YAML)
├── testcases/          # 测试用例脚本
├── report/             # Allure 测试报告 (自动生成)
├── run.py              # 启动脚本
├── pytest.ini          # Pytest 配置文件
└── requirements.txt    # 项目依赖文件
```

## 🛠 前置要求

- Python 3.x
- Java (Allure 运行需要)

## 📦 安装说明

1. 克隆仓库：
   ```bash
   git clone <repository_url>
   cd dummyjson-api-test
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ 配置

项目配置文件位于 `config/config.yaml`。您可以在此修改 `base_url` 和测试凭证。

```yaml
env: test

test:
  base_url: https://dummyjson.com
  username: emilys
  password: emilyspass
```

## 🚀 使用方法

### 运行测试

您可以使用启动脚本运行测试：

```bash
python run.py
```

该脚本将：
1. 使用 `pytest` 执行所有测试用例。
2. 生成 Allure 报告。
3. 自动在默认浏览器中打开报告。

或者，您可以直接运行 pytest：

```bash
pytest
```

### 查看报告

如果您直接使用 `pytest` 运行测试，可以使用以下命令生成并查看报告：

```bash
allure serve report
```

## 📚 接口文档

以下 API 接口封装在 `api/` 目录下：

### 认证模块 (Auth) - `api/auth_api.py`

- **登录 (Login)**
  - **方法:** `POST`
  - **端点:** `/auth/login`
  - **参数:** `username`, `password`

### 商品模块 (Product) - `api/product_api.py`

- **获取商品列表 (List Products)**
  - **方法:** `GET`
  - **端点:** `/products`

- **获取单个商品 (Get Single Product)**
  - **方法:** `GET`
  - **端点:** `/products/{id}`

### 购物车模块 (Cart) - `api/cart_api.py`

- **添加到购物车 (Add to Cart)**
  - **方法:** `POST`
  - **端点:** `/carts/add`
  - **参数:** `userId`, `products` (包含 `{id, quantity}` 的列表)

### 用户模块 (User) - `api/user_api.py`

- **获取当前用户信息 (Get Current User Info)**
  - **方法:** `GET`
  - **端点:** `/auth/me`
  - **Header:** 需要 Authorization 头 (由 `TokenManager` 自动处理)

## 🤝 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request
