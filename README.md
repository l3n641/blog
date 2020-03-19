
---
### 安装
- 创建虚拟环境 `python3 -m venv venv`
- 进入虚拟环境 `source venv/bin/activate`
- 安装包 `pip install -r requirements.txt`
- 复制配置文件 `cp .env.example .env`
- 编辑env文件
- 数据库迁移 `flask db upgrade`
- 启动http服务 `flask run`
