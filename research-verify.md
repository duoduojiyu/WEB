---
name: research-verify
description: 帮助用户进行高效资料检索、评估信息可信度、核实AI生成内容（尤其是代码）真实性的研究助手。Use when 用户需要：(1) 搜索和筛选可靠的学习/研究资料，(2) 验证AI生成内容的真实性，(3) 评估信息来源可信度，(4) 查找原始论文或官方文档，(5) 交叉验证多个信息源，(6) 验证AI生成代码的正确性、检查API是否过时、测试代码能否运行，或任何需要确保信息准确性的场景。
---

# 资料检索与核实指南

系统化地进行资料检索、评估可信度、核实AI生成内容的方法论。

## 快速判断：何时需要核实？

当遇到以下情况时，必须进行核实：
- AI给出具体数据、统计数字、日期
- AI提到"某研究表明"、"据统计"等引用
- AI生成代码示例、API参数
- AI提及人物、公司、产品的具体信息
- 信息来源不明确或可疑
- 用于决策、写作、分享的关键信息

## 资料检索流程

### 第一步：明确检索目标

在开始搜索前，明确：
- **检索主题**：具体要解决什么问题
- **信息类型**：概念解释 / 技术文档 / 最佳实践 / 论文研究
- **时效要求**：需要最新还是经典内容
- **深度要求**：入门级 / 进阶 / 专家级

### 第二步：选择检索渠道（按优先级）

| 优先级 | 渠道类型 | 具体来源 | 适用场景 |
|-------|---------|---------|---------|
| ⭐⭐⭐ | 官方文档 | 产品官网、GitHub、官方博客 | 技术规范、API使用 |
| ⭐⭐⭐ | 学术数据库 | Google Scholar、arXiv、IEEE | 论文、研究成果 |
| ⭐⭐⭐ | 权威媒体 | 知名技术媒体、官方公众号 | 行业动态、解读 |
| ⭐⭐☆ | 社区平台 | Stack Overflow、Reddit、知乎 | 实践经验、问题排查 |
| ⭐☆☆ | 视频教程 | YouTube、B站 | 入门学习、操作演示 |

### 第三步：搜索技巧

**精确搜索：**
```
"精确短语" + 关键词 -排除词 site:domain.com filetype:pdf
```

**AI领域专用搜索：**
- `site:arxiv.org` - 学术论文
- `site:github.com` - 代码和文档
- `site:huggingface.co` - 模型和数据集
- `site:openai.com` 或 `site:anthropic.com` - 官方文档

**查找原始论文：**
- 用 Google Scholar 搜索标题
- 使用 Semantic Scholar 查看引用关系
- Papers with Code 找论文+代码

## 可信度评估框架

### 来源可信度分级

| 级别 | 特征 | 可信度 | 使用建议 |
|-----|------|--------|---------|
| A级 | 官方文档、顶级期刊、权威机构 | 95%+ | 可直接引用 |
| B级 | 知名专家、知名公司技术博客 | 80-95% | 核实后引用 |
| C级 | 社区文章、个人博客 | 60-80% | 需交叉验证 |
| D级 | 无署名、无日期、无来源 | <60% | 谨慎使用 |

### 评估检查清单

- [ ] **作者资质**：作者是该领域专家吗？
- [ ] **发布机构**：机构有公信力吗？
- [ ] **发布日期**：信息是最新的吗？
- [ ] **引用来源**：有引用原始资料吗？
- [ ] **同行评议**：经过审核或社区验证吗？
- [ ] **多方验证**：其他可靠来源有相同说法吗？

## AI幻觉识别与核实

### 常见AI幻觉类型

| 类型 | 特征 | 示例 |
|-----|------|------|
| 编造引用 | 虚构论文、人物、数据 | "根据Smith et al. (2023)的研究..." |
| 错误事实 | 张冠李戴、数据错误 | 把A公司的产品说成B公司的 |
| 过时信息 | 用旧版信息回答 | API参数已废弃 |
| 过度泛化 | 从特例推出一般结论 | "所有模型都..." |
| 逻辑漏洞 | 推理过程有问题 | 因果关系倒置 |

### 核实流程

```
AI生成内容
    ↓
标记可疑信息（数据、引用、具体事实）
    ↓
优先查官方文档（最高可信度）
    ↓
交叉验证2-3个独立来源
    ↓
确认无误后使用
    ↓
记录信息来源（便于追溯）
```

### 快速核实技巧

**核实论文/研究：**
1. 复制标题到 Google Scholar
2. 检查作者、年份、期刊是否存在
3. 阅读摘要确认内容匹配

**核实代码/API：**
1. 直接查阅官方文档
2. 在官方示例中验证
3. 实际运行测试

**核实数据/统计：**
1. 寻找原始出处（报告、数据库）
2. 检查数据年份和范围
3. 对比多个来源的数据

**核实人物/公司信息：**
1. 查看官方网站/LinkedIn
2. 查阅权威媒体报道
3. 核实时间线和关联关系

## 代码验证详解

AI生成的代码是最容易出现幻觉的领域，必须进行系统性验证。

### 常见AI代码幻觉类型

| 类型 | 特征 | 示例 |
|-----|------|------|
| 虚构API | 编造不存在的函数/方法 | `openai.ChatCompletion.create()`（旧版） |
| 错误参数 | 参数名、类型、顺序错误 | 传了`model`实际是`engine` |
| 版本过时 | 使用已废弃的语法/API | 使用PyTorch 1.x的语法 |
| 逻辑错误 | 代码能运行但结果不对 | 数据预处理顺序错误 |
| 导入错误 | 不存在的模块或路径 | `from langchain.chat_models import ChatOpenAI`（已迁移） |
| 环境假设 | 假设存在某些前置条件 | 假设已安装特定版本依赖 |

### 代码验证流程

```
AI生成代码
    ↓
静态检查（语法、API存在性）
    ↓
文档对照（官方文档验证）
    ↓
环境准备（依赖安装）
    ↓
实际运行（功能测试）
    ↓
边界测试（异常情况）
    ↓
确认可用
```

### 各语言验证要点

**Python：**
```bash
# 1. 语法检查
python -m py_compile script.py

# 2. 类型检查（如有类型注解）
mypy script.py

# 3. 依赖检查
pip show package_name  # 确认已安装
pip install -r requirements.txt  # 安装依赖

# 4. 运行测试
python script.py
```

**JavaScript/TypeScript：**
```bash
# 1. 语法检查
node --check script.js

# 2. Lint检查
eslint script.js

# 3. 类型检查（TS）
tsc --noEmit

# 4. 运行测试
node script.js
```

**其他语言：**
- **Java**：`javac`编译检查 + Maven/Gradle依赖
- **Go**：`go build` + `go vet`
- **Rust**：`cargo check` + `cargo clippy`

### API验证清单

验证任何第三方API调用时检查：

- [ ] **导入路径**：模块路径是否正确（注意版本迁移）
- [ ] **类/函数名**：名称拼写、大小写是否正确
- [ ] **参数名称**：每个参数名是否与文档一致
- [ ] **参数类型**：字符串/数字/布尔/对象类型匹配
- [ ] **必需参数**：是否漏传了必需参数
- [ ] **认证信息**：API key、token是否正确传递
- [ ] **版本兼容**：当前安装的库版本是否支持该API

### 依赖版本验证

```bash
# Python - 检查已安装版本
pip list | grep package_name
pip freeze | findstr package_name  # Windows

# 对比AI建议的版本
pip install package==version  # 指定版本安装

# 使用虚拟环境隔离
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 快速验证技巧

**1. API存在性检查（不运行）：**
```python
# Python
import openai
print(dir(openai))  # 查看可用属性和方法
print(help(openai.chat.completions))  # 查看文档
```

**2. 官方示例对比：**
- 复制AI代码中的关键API调用
- 在官方文档搜索该API
- 对比参数列表和示例用法

**3. 最小可复现测试：**
```python
# 将复杂代码简化为最小测试
# 原代码：复杂的RAG流程
# 最小测试：只测试API调用是否正常响应

from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

**4. 错误信息分析：**
```
常见错误及含义：
- ImportError: No module named 'xxx' → 未安装依赖或路径错误
- AttributeError: module has no attribute 'xxx' → API不存在或版本不对
- TypeError: xxx() takes 1 positional argument but 2 were given → 参数数量/类型错误
- NameError: name 'xxx' is not defined → 变量未定义或拼写错误
```

### 代码验证工具推荐

| 工具类型 | Python | JavaScript | 用途 |
|---------|--------|-----------|------|
| 语法检查 | `py_compile` | `node --check` | 基础语法验证 |
| Linter | `pylint`/`flake8` | `eslint` | 代码规范检查 |
| 类型检查 | `mypy` | TypeScript | 类型安全验证 |
| 依赖管理 | `pipdeptree` | `npm ls` | 依赖冲突检查 |
| 交互测试 | Jupyter Notebook | Node REPL | 快速验证代码片段 |

### 代码验证记录模板

```markdown
## 代码验证记录

### 原始代码来源
- AI对话 / 教程文章 / Stack Overflow
- 链接/截图：

### 验证过程
| 检查项 | 结果 | 备注 |
|-------|------|------|
| 语法检查 | ✅/❌ | |
| 依赖安装 | ✅/❌ | 版本： |
| API存在性 | ✅/❌ | 文档链接： |
| 运行测试 | ✅/❌ | 输出： |
| 功能验证 | ✅/❌ | 预期 vs 实际： |

### 修改记录
- 原代码：
- 修改后：
- 修改原因：

### 最终验证结果
- [ ] 可直接使用
- [ ] 需要修改后使用
- [ ] 不可使用（原因：）
- 验证时间：202X-XX-XX
- 环境信息：Python x.x, package x.x.x
```

### 高风险代码警示

以下情况代码风险极高，需格外谨慎：
- 涉及文件系统操作（删除、覆盖）
- 网络请求（API调用、下载）
- 数据库操作（删改数据）
- 系统命令执行（os.system, subprocess）
- 涉及认证/密钥处理

**建议**：
1. 先在隔离环境（虚拟机/容器）测试
2. 仔细阅读每一行代码
3. 添加日志输出而不是直接执行
4. 备份重要数据

## 论文复现验证

AI/ML领域论文复现是检验知识真实性的重要环节，也是最容易出问题的环节。

### 复现前的评估

在开始复现前，评估论文的可复现性：

| 评估指标 | 高可复现性 | 低可复现性 |
|---------|-----------|-----------|
| 代码开源 | ✅ 有官方GitHub仓库 | ❌ 无代码 |
| 依赖说明 | ✅ 完整的requirements.txt | ❌ 依赖不明 |
| 数据公开 | ✅ 数据集可下载/链接提供 | ❌ 私有数据 |
| 超参完整 | ✅ 所有关键超参数列出 | ❌ 关键参数缺失 |
| 硬件说明 | ✅ 明确GPU型号/内存需求 | ❌ 硬件要求不明 |
| 随机种子 | ✅ 提供种子或可复现设置 | ❌ 随机性未控制 |

### 复现流程

```
阅读论文理解方法
    ↓
检查是否有官方代码
    ↓
环境准备（Python版本、CUDA版本）
    ↓
下载代码和数据
    ↓
安装依赖（注意版本冲突）
    ↓
运行示例/测试
    ↓
逐步验证各模块输出
    ↓
对比论文报告指标
    ↓
记录差异和问题
```

### 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 结果远低于论文 | 实现细节差异、超参不对 | 检查代码Issue、对比官方实现 |
| 无法运行 | 依赖版本不兼容、缺少文件 | 查看README、检查依赖版本 |
| 显存不足 | 批次大小、模型尺寸 | 减小batch_size、使用梯度累积 |
| 数据加载失败 | 路径问题、数据格式 | 检查数据目录结构、文件格式 |
| 随机性导致结果波动 | 种子未固定 | 设置numpy/pytorch/tensorflow种子 |

### 复现检查清单

- [ ] **环境一致**：Python、CUDA、库版本与论文一致
- [ ] **数据一致**：数据集版本、预处理流程一致
- [ ] **模型一致**：架构、参数量与论文描述一致
- [ ] **训练一致**：优化器、学习率、批次大小一致
- [ ] **评估一致**：评估指标、测试集划分一致
- [ ] **结果对比**：在合理误差范围内（通常±1-2%）

### 复现验证工具

- **Docker**：创建与论文一致的环境
- **Pipreqs/Pigar**：自动生成依赖清单
- **Weights & Biases/TensorBoard**：训练过程可视化对比
- **Papers with Code**：查看社区复现结果和讨论

### 无法复现时的处理

1. **查看GitHub Issues**：其他人可能遇到相同问题
2. **联系作者**：通过邮件礼貌询问实现细节
3. **社区求助**：Reddit r/MachineLearning、Stack Overflow
4. **部分复现**：验证核心模块而非完整流程
5. **接受差异**：记录差异并分析可能原因

## 数据集验证

AI生成的数据集信息同样需要核实，错误的数据集会导致错误的结论。

### 数据集验证维度

| 维度 | 验证内容 | 验证方法 |
|-----|---------|---------|
| **存在性** | 数据集是否真实存在 | 搜索Kaggle/HuggingFace/UCI |
| **可获取性** | 是否能下载/访问 | 尝试下载链接 |
| **版本** | 使用哪个版本 | 查看版本历史、发布日期 |
| **规模** | 样本数、特征数 | 读取数据shape、描述统计 |
| **质量** | 缺失值、异常值 | 数据探索性分析(EDA) |
| **许可** | 使用许可协议 | 查看LICENSE文件 |

### 常用数据集官方来源

| 数据集 | 官方来源 | 验证链接 |
|-------|---------|---------|
| ImageNet | 斯坦福 | image-net.org |
| COCO | 微软 | cocodataset.org |
| MNIST | LeCun个人页 | yann.leCun.com/exdb/mnist |
| CIFAR-10/100 | 多伦多大学 | cs.toronto.edu/~kriz/cifar.html |
| GLUE/SuperGLUE | 纽约大学 | gluebenchmark.com |
| Kaggle数据集 | Kaggle | kaggle.com/datasets |
| HuggingFace数据集 | HF Hub | huggingface.co/datasets |

### 数据集验证流程

```python
# 1. 加载数据集
import pandas as pd
df = pd.read_csv('dataset.csv')

# 2. 基础信息验证
print(f"Shape: {df.shape}")  # 样本数、特征数
print(f"Columns: {df.columns.tolist()}")  # 特征名
print(df.info())  # 数据类型

# 3. 统计信息验证
print(df.describe())  # 描述统计
print(df.isnull().sum())  # 缺失值

# 4. 标签分布验证
print(df['label'].value_counts())  # 类别分布

# 5. 与论文描述对比
# 检查样本数、特征数、类别数是否与论文一致
```

### 合成数据识别

AI可能生成不存在的合成数据，识别特征：
- 特征名过于通用（feature_1, feature_2）
- 数值分布过于均匀或规律
- 时间戳格式不自然
- 类别标签命名异常

**验证方法**：
- 要求提供数据来源链接
- 检查数据是否有现实世界的特征（噪声、缺失、异常值）
- 使用统计检验检测合成数据

### 数据预处理验证

确保预处理流程与论文一致：

| 预处理步骤 | 验证点 | 常见问题 |
|-----------|-------|---------|
| 归一化/标准化 | 使用train集的统计量 | 数据泄露（用全量数据计算） |
| 数据划分 | 划分比例、随机种子 | 划分方式不同导致结果不可比 |
| 缺失值处理 | 填充方法 | 不同方法影响模型性能 |
| 特征工程 | 特征构造逻辑 | 实现细节差异 |
| 数据增强 | 增强策略参数 | 增强过度或不足 |

## 交叉验证方法

### 三角验证法

同一信息至少通过3个独立来源验证：
- 来源A（官方文档）
- 来源B（权威媒体/学术文章）
- 来源C（社区实践/案例验证）

### 反向验证

当找到疑似原始来源时：
1. 阅读原文，确认AI的理解是否正确
2. 检查上下文，确认没有断章取义
3. 查看是否有更新的信息覆盖

## 实用工具推荐

### 检索工具
- **Google Scholar**：学术论文搜索
- **Semantic Scholar**：AI论文专用，带引用关系
- **Wayback Machine**：查看网页历史版本
- **Wikiwand/Wikipedia**：快速概念核查（但需二次验证）

### 核实工具
- **Crossref**：验证DOI和论文信息
- **Retraction Watch**：查看论文是否被撤稿
- **Snopes/FactCheck**：事实核查网站
- **Perplexity AI**：带引用的AI搜索（需核实引用）

### 管理工具
- **Zotero**：文献管理和引用
- **Notion/Obsidian**：整理核实后的知识
- **Diigo**：网页标注和存档

## 资料整理模板

核实后的资料按以下格式整理：

```markdown
## 主题：XXX

### 核心结论
- 结论1（来源A）
- 结论2（来源B）

### 信息来源
| 信息点 | 来源 | 可信度 | 最后核实时间 |
|-------|------|--------|-------------|
| XXX | [链接] | A级 | 202X-XX-XX |

### 存疑信息
- XXX（需进一步核实）

### 相关资源
- [官方文档](链接)
- [论文原文](链接)
- [实践案例](链接)
```

## 常见误区提醒

1. **盲目信任权威**：即使是权威来源也要看时效性
2. **忽视版本差异**：软件/框架不同版本可能有差异
3. **中文二手资料**：尽量查阅英文原始资料
4. **忽视更新日期**：技术领域信息过期很快
5. **不记录来源**：核实后不复查，无法追溯

## 实战示例

**场景**：AI说"GPT-4在2023年的MMLU测试中达到86.4%的准确率"

**核实步骤**：
1. 标记关键信息：GPT-4、MMLU、86.4%、2023年
2. 搜索："GPT-4 MMLU score official"
3. 查OpenAI官方发布的技术报告
4. 在arXiv找相关论文验证
5. 对比多个报道确认数据一致
6. 记录：OpenAI GPT-4 Technical Report, 2023

**场景**：AI给了一段Python代码使用某个库的API

**核实步骤**：
1. 标记关键信息：库名、函数名、参数
2. 查阅库的官方文档确认API存在
3. 检查参数名和类型是否匹配
4. 查看官方示例代码对比
5. 实际运行测试（如果环境允许）

---

**场景**：AI提供了OpenAI API调用的代码

**代码验证步骤**：
```python
# AI生成的代码（可能存在幻觉）
import openai

openai.api_key = "your-key"
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)
```

**验证过程**：
1. **静态检查**：`python -m py_compile script.py` → 语法正确
2. **API文档对照**：查OpenAI官方文档 → 发现API已更新！
   - 旧版：`openai.ChatCompletion.create()`
   - 新版：`client.chat.completions.create()`
3. **依赖检查**：`pip show openai` → 已安装v1.x（新版）
4. **修正代码**：
```python
from openai import OpenAI
client = OpenAI(api_key="your-key")
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)
```
5. **运行测试**：执行代码 → 成功获取响应
6. **记录**：OpenAI Python SDK v1.0+ 迁移指南，2023年11月发布
