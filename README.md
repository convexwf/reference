# reference

`reference` 集中维护多个上游仓库的完整 Markdown 版本；上游仓库保持只读，不再承载复制的生成脚本或生成文件。

目前覆盖：

- `ai-agent-book` 的简体中文完整教程
- `ai-infra-book` 的简体中文 AI Infra 教程
- `easy-rl` 的中文完整教程
- `hello-agents` 的中文主教程
- `lianglianglee-architecture` 的《从 0 开始学架构》专栏
- `lianglianglee-continuous-delivery` 的《持续交付36讲》专栏
- `lianglianglee-distributed-finance` 的《分布式金融架构课》专栏
- `lianglianglee-linux-performance` 的《Linux性能优化实战》专栏
- `lianglianglee-mysql` 的《MySQL实战45讲》专栏
- `lianglianglee-instant-messaging` 的《即时消息技术剖析与实战》专栏
- `lianglianglee-high-concurrency` 的《高并发系统设计40问》专栏
- `lianglianglee-kafka` 的《Kafka核心技术与实战》专栏
- `lianglianglee-ai-tech-insider` 的《AI技术内参》专栏
- `lianglianglee-flutter` 的《Flutter核心技术与实战》专栏
- `lianglianglee-left-ear` 的《左耳听风》专栏
- `lianglianglee-recommendation-system` 的《推荐系统三十六式》专栏
- `lianglianglee-http` 的《透视HTTP协议》专栏

生成结果位于 `markdown/`，具体路径由各清单的 `output` 决定；GeekTime 专栏位于 `markdown/geektime/`。`sources.lock.json` 锁定每份结果对应的上游提交、清单摘要和适配器版本，因此可以在任何时间重建同一版本。

本地使用：

```bash
python -m tools.update --all
python -m tools.check --all
```

离线开发时，可明确指定清洁的同级源码目录；该模式只读取源码，不会写入源码仓库：

```bash
python -m tools.update --all --source-root .. --dry-run
```

GitHub Actions 每周日 10:20（北京时间）检查上游；有变化时仅提交 `sources.lock.json` 与 `markdown/`，通过受保护分支的 `validate` 检查后自动合并。仓库管理员需要配置 GitHub App 机密 `REFERENCE_SYNC_APP_ID` 和 `REFERENCE_SYNC_APP_PRIVATE_KEY`，并把 `validate` 设为默认分支的必需检查。

技术设计见 [doc/multi-repository-markdown-integration-and-auto-update-design.md](doc/multi-repository-markdown-integration-and-auto-update-design.md)。
