# JS 基础练习 & GitHub Push Skill 学习记录

**日期**: 2026-04-15  
**仓库**: [duoduojiyu/WEB](https://github.com/duoduojiyu/WEB)

---

## 1. GitHub Push Skill

为了快速将任何内容推送到 GitHub 仓库，创建了一个 `github-push` skill。

**skill 核心文件**:
- `SKILL.md` — 使用说明（API vs Git CLI）
- `scripts/push_to_github.py` — GitHub Contents API 推送脚本

**特点**:
- 无需本地配置 git，只需 GitHub Token 即可单文件秒推
- 自动检测文件是否存在，更新时携带 SHA
- 支持自定义 commit message 和分支

---

## 2. JS 基础知识练习页面

编写了一个交互式 HTML 页面 `js-basic-practice.html`，涵盖五大核心知识点：

### 模块一览

| 模块 | 知识点 | 练习内容 |
|------|--------|---------|
| 变量的定义 | `var` / `let` / `const` | 创建变量、let vs const 重新赋值对比 |
| 变量类型 | 动态类型、`typeof`、类型转换 | 类型侦探、显式转换 `Number/String/Boolean` |
| 表达式 | 算术/比较/逻辑/字符串表达式 | 计算器、严格相等 `===`、模板字符串 |
| 流程控制 | `if/else`、`for`、`while` | 成绩评级、九九乘法表、猜数字游戏 |
| 函数 | 声明/表达式/箭头函数、闭包 | 计算器函数、作用域链、自定义代码运行区 |

### 页面亮点
- 每个知识点都配有 **输入控件 + 运行按钮 + 实时输出**
- 底部内置 **代码编辑器**，可手写 JS 并立即执行（支持 `console.log` 捕获）
- 响应式卡片布局，直接在浏览器打开即可练习

---

## 3. 本次推送文件清单

```
study/
  ├── js-basic-practice.html
  └── notes/
        └── 2026-04-15-js-github-skill-learning.md
skills/
  └── github-push/
        ├── SKILL.md
        └── scripts/
              └── push_to_github.py
```

---

## 4. 学习心得

- **变量**: 默认用 `const`，需要重新赋值时用 `let`，避免 `var` 的作用域问题。
- **类型**: `typeof null === "object"` 是 JS 的历史 bug；严格相等 `===` 比 `==` 更安全。
- **表达式**: 模板字符串 `` `Hello ${name}` `` 比字符串拼接更清晰。
- **流程控制**: `for` 适合已知次数的循环，`while` 适合条件驱动的循环。
- **函数**: 箭头函数简洁但无自身 `this`；闭包让内部函数记住外部变量，常用于计数器、缓存等场景。
