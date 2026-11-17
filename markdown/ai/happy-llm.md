---
title: "Happy-LLM：从零开始构建大模型"
authors:
  - "Datawhale Happy-LLM 项目组"
language: "zh-CN"
tags:
  - "llm"
  - "transformer"
  - "pretraining"
  - "fine-tuning"
  - "rag"
  - "agent"
published_at: "2024-05-28"
updated_at: "2026-08-09"
---

# Happy-LLM：从零开始构建大模型

## 文档信息

| 项目 | 内容 |
| --- | --- |
| 文档标题 | Happy-LLM：从零开始构建大模型 |
| 文档类型 | zh-CN 整合 Markdown |
| 上游仓库 | [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) |
| 锁定提交 | [1e0b3a1e6f89](https://github.com/datawhalechina/happy-llm/commit/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96) |
| 提交时间 | 2026-08-09T01:17:26+08:00 |
| 生成器版本 | `generic@1;engine@9` |

> 本文件由 reference 仓库自动生成。请修改上游源文件或本仓库的清单/适配器后重新生成，不要直接编辑此文件。

## 阅读说明

本文档按清单中的阅读顺序合并上游 Markdown。图片被改写为锁定提交的 GitHub Raw 链接，章节内有效的本地文档链接被改写为同一提交的 GitHub 源文件链接。

## 目录

- [导读](#导读)
  - [项目概览](#项目概览)
  - [学习与环境准备](#学习与环境准备)
  - [前言](#前言)
- [基础原理](#基础原理)
  - [第一章 NLP 基础概念](#第一章-nlp-基础概念)
  - [第二章 Transformer 架构](#第二章-transformer-架构)
  - [第三章 预训练语言模型](#第三章-预训练语言模型)
  - [第四章 大语言模型](#第四章-大语言模型)
- [训练与应用实践](#训练与应用实践)
  - [第五章 动手搭建大模型](#第五章-动手搭建大模型)
  - [第六章 大模型训练实践](#第六章-大模型训练实践)
  - [第六章实践说明](#第六章实践说明)
  - [第七章 大模型应用](#第七章-大模型应用)
  - [第八章 大模型强化学习](#第八章-大模型强化学习)
  - [GRPO](#grpo)
  - [OPD](#opd)
  - [Search-R1](#search-r1)
  - [ReTool](#retool)
- [扩展章节](#扩展章节)
  - [扩展章节说明](#扩展章节说明)
  - [微调小模型的意义](#微调小模型的意义)
  - [Transformer 整体模块设计解读](#transformer-整体模块设计解读)
  - [文本数据处理详解](#文本数据处理详解)
  - [超小中文多模态模型的拼接微调](#超小中文多模态模型的拼接微调)
  - [S1：使用 vLLM 管理思考预算](#s1使用-vllm-管理思考预算)
  - [CDDRS：细粒度语义信息增强 RAG 检索](#cddrs细粒度语义信息增强-rag-检索)
  - [大模型生成 Token 的方式](#大模型生成-token-的方式)

---

## 导读

### 项目概览

![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/head.jpg)
    <h1>Happy-LLM</h1>



![GitHub stars](https://img.shields.io/github/stars/datawhalechina/happy-llm?style=flat&logo=github)
![GitHub forks](https://img.shields.io/github/forks/datawhalechina/happy-llm?style=flat&logo=github)
![Language](https://img.shields.io/badge/language-Chinese-brightgreen?style=flat)
<a href="https://github.com/datawhalechina/happy-llm">![GitHub Project](https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github)</a>
<a href="https://swanlab.cn/@kmno4/Happy-LLM/overview">![SwanLab](https://raw.githubusercontent.com/SwanHubX/assets/main/badge1.svg)</a>



<a href="https://trendshift.io/repositories/14175" target="_blank">![datawhalechina%2Fhappy-llm | Trendshift](https://trendshift.io/api/badge/repositories/14175)</a>



  <h3>📚 从零开始构建大模型</h3>
*深入理解 LLM 核心原理，动手实现你的第一个大模型*


---

#### 🎯 项目介绍

> &emsp;&emsp;*很多小伙伴在看完 Datawhale开源项目： [self-llm 开源大模型食用指南](https://github.com/datawhalechina/self-llm) 后，感觉意犹未尽，想要深入了解大语言模型的原理和训练过程。于是我们（Datawhale）决定推出《Happy-LLM》项目，旨在帮助大家深入理解大语言模型的原理和训练过程。*

&emsp;&emsp;本项目是一个**系统性的 LLM 学习教程**，将从 NLP 的基本研究方法出发，根据 LLM 的思路及原理逐层深入，依次为读者剖析 LLM 的架构基础和训练过程。同时，我们会结合目前 LLM 领域最主流的代码框架，演练如何亲手搭建、训练一个 LLM，期以实现授之以鱼，更授之以渔。希望大家能从这本书开始走入 LLM 的浩瀚世界，探索 LLM 的无尽可能。

##### ✨ 你将收获什么？

- 📚 **Datawhale 开源免费** 完全免费的学习本项目所有内容
- 🔍 **深入理解** Transformer 架构和注意力机制
- 📚 **掌握** 预训练语言模型的基本原理
- 🧠 **了解** 现有大模型的基本结构
- 🏗️ **动手实现** 一个完整的 LLaMA2 模型
- ⚙️ **掌握训练** 从预训练到微调的全流程
- 🚀 **实战应用** RAG、Agent 等前沿技术

#### 📖 内容导航

| 章节 | 关键内容 | 状态 |
| --- | --- | --- |
| [学习与环境准备](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/%E5%AD%A6%E4%B9%A0%E4%B8%8E%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87.md) | 分章依赖、硬件建议与实践入口 | ✅ |
| [前言](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/%E5%89%8D%E8%A8%80.md) | 本项目的缘起、背景及读者建议 | ✅ |
| [第一章 NLP 基础概念](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter1/%E7%AC%AC%E4%B8%80%E7%AB%A0%20NLP%E5%9F%BA%E7%A1%80%E6%A6%82%E5%BF%B5.md) | 什么是 NLP、发展历程、任务分类、文本表示演进 | ✅ |
| [第二章 Transformer 架构](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter2/%E7%AC%AC%E4%BA%8C%E7%AB%A0%20Transformer%E6%9E%B6%E6%9E%84.md) | 注意力机制、Encoder-Decoder、手把手搭建 Transformer | ✅ |
| [第三章 预训练语言模型](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter3/%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E9%A2%84%E8%AE%AD%E7%BB%83%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B.md) | Encoder-only、Encoder-Decoder、Decoder-Only 模型对比 | ✅ |
| [第四章 大语言模型](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B.md) | LLM 定义、训练策略、涌现能力分析 | ✅ |
| [第五章 动手搭建大模型](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter5/%E7%AC%AC%E4%BA%94%E7%AB%A0%20%E5%8A%A8%E6%89%8B%E6%90%AD%E5%BB%BA%E5%A4%A7%E6%A8%A1%E5%9E%8B.md) | 实现 LLaMA2、训练 Tokenizer、预训练小型 LLM | ✅ |
| [第六章 大模型训练实践](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/%E7%AC%AC%E5%85%AD%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83%E6%B5%81%E7%A8%8B%E5%AE%9E%E8%B7%B5.md) | 预训练、有监督微调、LoRA/QLoRA 高效微调 | ✅ |
| [第七章 大模型应用](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BA%94%E7%94%A8.md) | 模型评测、RAG 检索增强、Agent 智能体 | ✅ |
| [第八章 大模型强化学习](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0.md) | GRPO、OPD、Search-R1、ReTool 与 PyTRIO 实践 | ✅ |

> 第六章正文已覆盖 Pretrain、SFT 与 PEFT 等核心训练流程，建议结合 [第六章实践说明](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/readme.md) 与 [学习与环境准备](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/%E5%AD%A6%E4%B9%A0%E4%B8%8E%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87.md) 一起阅读；偏好对齐可以继续参考 [第六章补充专题](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/6.4%5BWIP%5D%20%E5%81%8F%E5%A5%BD%E5%AF%B9%E9%BD%90.md)。

##### 模型下载

| 模型名称 | 下载地址 |
| --- | --- |
| Happy-LLM-Chapter5-Base-215M | [🤖 ModelScope](https://www.modelscope.cn/models/kmno4zx/happy-llm-215M-base) |
| Happy-LLM-Chapter5-SFT-215M | [🤖 ModelScope](https://www.modelscope.cn/models/kmno4zx/happy-llm-215M-sft) |

> *ModelScope 创空间体验地址：[🤖 创空间](https://www.modelscope.cn/studios/kmno4zx/happy_llm_215M_sft)*

##### PDF 版本下载

&emsp;&emsp;***本 Happy-LLM PDF 教程完全开源免费。为防止各类营销号加水印后贩卖给大模型初学者，我们特地在 PDF 文件中预先添加了不影响阅读的 Datawhale 开源标志水印，敬请谅解～***

> *Happy-LLM PDF : https://github.com/datawhalechina/happy-llm/releases/tag/PDF*
> *Happy-LLM PDF 国内下载地址 : https://www.datawhale.cn/learn/summary/179*

#### 💡 如何学习

&emsp;&emsp;本项目适合大学生、研究人员、LLM 爱好者。在学习本项目之前，建议具备一定的编程经验，尤其是要对 Python 编程语言有一定的了解。最好具备深度学习的相关知识，并了解 NLP 领域的相关概念和术语，以便更轻松地学习本项目。

&emsp;&emsp;如果你计划复现章节代码，建议先阅读 [学习与环境准备](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/%E5%AD%A6%E4%B9%A0%E4%B8%8E%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87.md)。仓库按章节拆分依赖，不同章节建议使用独立的 Python 环境，以减少版本冲突。

&emsp;&emsp;本项目分为两部分——基础知识与实战应用。第1章～第4章是基础知识部分，从浅入深介绍 LLM 的基本原理。其中，第1章简单介绍 NLP 的基本任务和发展，为非 NLP 领域研究者提供参考；第2章介绍 LLM 的基本架构——Transformer，包括原理介绍及代码实现，作为 LLM 最重要的理论基础；第3章整体介绍经典的 PLM，包括 Encoder-Only、Encoder-Decoder 和 Decoder-Only 三种架构，也同时介绍了当前一些主流 LLM 的架构和思想；第4章则正式进入 LLM 部分，详细介绍 LLM 的特点、能力和整体训练过程。第5章～第8章是实战应用部分，将逐步带领大家深入 LLM 的底层细节。其中，第5章将带领大家基于 PyTorch 亲手搭建一个 LLM，并实现预训练、有监督微调的全流程；第6章将引入目前业界主流的 LLM 训练框架 Transformers，带领学习者基于该框架快速、高效地实现 LLM 训练过程；第7章介绍 LLM 的评测、检索增强生成（Retrieval-Augmented Generation，RAG）和智能体（Agent）；第8章进一步介绍 GRPO、OPD，以及 Search-R1 与 ReTool 两类 Agentic RL 实践。你可以根据个人兴趣和需求，选择性地阅读相关章节。

&emsp;&emsp;在阅读本书的过程中，建议你将理论和实际相结合。LLM 是一个快速发展、注重实践的领域，我们建议你多投入实战，复现本书提供的各种代码，同时积极参加 LLM 相关的项目与比赛，真正投入到 LLM 开发的浪潮中。我们鼓励你关注 Datawhale 及其他 LLM 相关开源社区，当遇到问题时，你可以随时在本项目的 issue 区提问。

&emsp;&emsp;最后，欢迎每一位读者在学习完本项目后加入到 LLM 开发者的行列。作为国内 AI 开源社区，我们希望充分聚集共创者，一起丰富这个开源 LLM 的世界，打造更多、更全面特色 LLM 的教程。星火点点，汇聚成海。我们希望成为 LLM 与普罗大众的阶梯，以自由、平等的开源精神，拥抱更恢弘而辽阔的 LLM 世界。

#### 🤝 如何贡献

我们欢迎任何形式的贡献！

- 🐛 **报告 Bug** - 发现问题请提交 Issue
- 💡 **功能建议** - 有好想法就告诉我们
- 📝 **内容完善** - 帮助改进教程内容
- 🔧 **代码优化** - 提交 Pull Request

#### 🙏 致谢

##### 核心贡献者
- [宋志学-项目负责人](https://github.com/KMnO4-zx) (Datawhale成员-中国矿业大学(北京))
- [邹雨衡-项目负责人](https://github.com/logan-zou) (Datawhale成员-对外经济贸易大学)
- [朱信忠-指导专家](https://xinzhongzhu.github.io/)（Datawhale首席科学家-浙江师范大学杭州人工智能研究院教授）

##### 特别感谢
- 感谢 [@Sm1les](https://github.com/Sm1les) 对本项目的帮助与支持
- 感谢所有为本项目做出贡献的开发者们 ❤️

<div align=center style="margin-top: 30px;">
  <a href="https://github.com/datawhalechina/happy-llm/graphs/contributors">
![image](https://contrib.rocks/image?repo=datawhalechina/happy-llm)
  </a>
</div>

#### Star History


![Datawhale](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/star-history-20251017.png)



⭐ 如果这个项目对你有帮助，请给我们一个 Star！


#### 关于 Datawhale


![Datawhale](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/datawhale.png)
扫描二维码关注 Datawhale 公众号，获取更多优质开源内容


---

#### 📜 开源协议

本作品采用[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/)进行许可。

### 学习与环境准备

Happy-LLM 以教程阅读为主、代码实践为辅。为了降低环境冲突，建议读者按照章节分别准备依赖，而不是在同一个环境中安装全部依赖。

第八章使用 PyTRIO 完成远端模型采样、前向反向传播和参数更新，本地程序负责数据处理、搜索环境、代码执行环境与训练调度。因此，第八章可以在可联网的 CPU 设备上学习和试跑，但需要 TRIO 账号、稳定的网络连接与可用额度。

#### 1. 阅读与实践建议

- 第 1 章到第 4 章以原理学习为主，推荐先完整阅读正文，再选择性复现代码。
- 第 5 章到第 8 章以实践为主，建议结合章节正文、代码目录和对应依赖一起学习。
- 如果你的设备资源有限，建议优先复现第 5 章的手写实现，以及第 6 章中的数据处理与单卡调试流程。
- 学习第 8 章时，建议先运行 GRPO 与 OPD 的同步版，再进入 Search-R1 和 ReTool 的多文件 Agentic RL 工程。

#### 2. 分章环境说明

| 章节 | 主要内容 | 依赖文件 | 硬件建议 |
| --- | --- | --- | --- |
| [第二章 Transformer 架构](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter2/%E7%AC%AC%E4%BA%8C%E7%AB%A0%20Transformer%E6%9E%B6%E6%9E%84.md) | Transformer 手写实现 | [`./chapter2/code/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter2/code/requirements.txt) | CPU 或单卡 GPU |
| [第五章 动手搭建大模型](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter5/%E7%AC%AC%E4%BA%94%E7%AB%A0%20%E5%8A%A8%E6%89%8B%E6%90%AD%E5%BB%BA%E5%A4%A7%E6%A8%A1%E5%9E%8B.md) | 手写 LLaMA2、Tokenizer、预训练与 SFT | [`./chapter5/code/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter5/code/requirements.txt) | 单卡 GPU，部分步骤可先在 CPU 调试 |
| [第六章 大模型训练流程实践](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/%E7%AC%AC%E5%85%AD%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83%E6%B5%81%E7%A8%8B%E5%AE%9E%E8%B7%B5.md) | Transformers、DeepSpeed、PEFT 训练实践 | [`./chapter6/code/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/requirements.txt) | 建议多卡 GPU，最小可从小样本和单卡调试开始 |
| [第七章 大模型应用 - RAG](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BA%94%E7%94%A8.md) | 检索增强生成 | [`./chapter7/RAG/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/RAG/requirements.txt) | CPU 可体验，向量检索建议预留更多内存 |
| [第七章 大模型应用 - Agent](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BA%94%E7%94%A8.md) | 智能体与工具调用 | [`./chapter7/Agent/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/Agent/requirements.txt) | CPU 可体验，联网能力按具体工具配置 |
| [第八章 Agentic-RL](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0.md) | GRPO、OPD、Search-R1、ReTool | [`./chapter8/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/requirements.txt) | 本地 CPU 与稳定网络即可；需要 TRIO 账号，ReTool 需隔离执行环境 |

#### 3. 通用准备步骤

第 2 章到第 7 章建议优先使用 Python 3.10 或 3.11；第 8 章配套代码使用 Python 3.13，并通过 [`./chapter8/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/requirements.txt) 固定 PyTRIO 等依赖。请为不同章节创建独立虚拟环境。以第六章为例，可以按如下方式准备：

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r ./docs/chapter6/code/requirements.txt
```

如果你需要复现其他章节，请将最后一行中的依赖文件替换为该章节对应的 `requirements.txt`。

#### 4. 第六章快速开始

第六章正文聚焦 Pretrain、SFT 和高效微调三条主线，建议和 [`./chapter6/readme.md`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/readme.md) 一起阅读。代码目录位于 [`./chapter6/code`](https://github.com/datawhalechina/happy-llm/tree/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code)。

推荐按以下顺序实践：

1. 先阅读 [`./chapter6/readme.md`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/readme.md)，明确模型、数据和脚本入口。
2. 使用 [`./chapter6/code/download_model.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/download_model.py) 下载基座模型。
3. 使用 [`./chapter6/code/download_dataset.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/download_dataset.py) 下载或准备训练数据。
4. 先用小样本调试 [`./chapter6/code/pretrain.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/pretrain.py) 或 [`./chapter6/code/finetune.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/finetune.py)。
5. 最后再结合 [`./chapter6/code/pretrain.sh`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/pretrain.sh) 与 [`./chapter6/code/finetune.sh`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/finetune.sh) 进行完整训练。

需要注意的是，脚本中的 `autodl-tmp` 路径、显卡编号和 DeepSpeed 参数都是示例配置，正式运行前请根据本地环境自行调整。

#### 5. 第八章快速开始

第八章正文位于 [`./chapter8/第八章 大模型强化学习.md`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0.md)，公共依赖位于 [`./chapter8/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/requirements.txt)。以下命令均应从 Happy-LLM 仓库根目录执行。

> **费用提示：** PyTRIO 会在远端执行模型采样与训练，并按照实际使用量产生费用。第一次运行请保留各示例 README 中的单步、小 batch 和短轨迹配置，确认完整链路后再扩大实验规模。

> **安全提示：** ReTool 会在本地执行模型生成的 Python 代码。配套 `sandbox.py` 只能限制部分资源，无法提供可信隔离。请使用一次性容器、低权限虚拟机或专用沙箱服务，并移除环境中的 API Key、SSH 配置和云服务凭证。

##### 5.1 创建独立环境

推荐为第八章单独创建 Python 3.13 环境：

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r docs/chapter8/requirements.txt
```

如果尚未安装 uv，可以先执行 `python -m pip install --upgrade uv`。Windows PowerShell 使用 `.\.venv\Scripts\Activate.ps1` 激活环境。安装完成后，可以确认本章锁定的 PyTRIO 版本：

```bash
python -c "from importlib.metadata import version; print(version('pytrio'))"
```

##### 5.2 登录并验证连接

登录 TRIO 后，读取当前服务支持的模型列表：

```bash
trio login
python -c "import pytrio as trio; print(trio.ServiceClient().get_supported_models())"
```

能够正常打印模型列表，说明 PyTRIO 安装、账号认证和网络连接均已就绪。只有需要在线记录实验时才需要额外执行 `swanlab login`；使用示例中的 `--swanlab-mode disabled` 可以先关闭远端实验记录。安装或登录遇到问题时，可以参考 [PyTRIO 官方快速开始](https://docs.pytrio.com/docs/quick-start)。

##### 5.3 推荐实践顺序

| 模块 | 建议入口 | 额外准备 |
| --- | --- | --- |
| GRPO | [`./chapter8/grpo/README.md`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/grpo/README.md) | 先运行同步版一步试验；GSM8K 会在首次运行时下载 |
| OPD | [`./chapter8/opd/README.md`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/opd/README.md) | 先使用一个 DeepMath 分片，并确认 Student 与 Teacher 模型当前可用 |
| Search-R1 | [`./chapter8/search-r1/README.md`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/search-r1/README.md) | 先准备数据并使用无需 API Key 的 Wikipedia 后端验证多轮搜索链路 |
| ReTool | [`./chapter8/retool/README.md`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter8/retool/README.md) | 先准备数据和隔离执行环境，再运行一步 PPO 训练 |

正文重点讲解 GRPO 与 OPD 的同步版，异步版保留相同算法和数据对齐方式；Search-R1 与 ReTool 按数据、协议、环境、rollout、训练和评测拆成多文件工程。想继续学习更多 Agentic RL 算法与实验，可以阅读作者持续维护的 [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab)；该仓库更新更快，并会持续补充新的训练代码与实践记录。

#### 6. 常见问题

##### 6.1 为什么不提供统一的根目录依赖？

本项目覆盖从原理实现到训练框架、再到 RAG 与 Agent 应用的完整链路，不同章节的依赖差异较大。按章节拆分依赖，能够减少版本冲突，也更符合教程式学习场景。

##### 6.2 没有多卡 GPU 是否还能学习第六章？

可以。建议先阅读正文理解训练流程，再使用小样本、较小 batch size 或单卡环境调试数据处理和训练脚本。即便无法完整复现多卡训练，也不影响掌握整体思路。

##### 6.3 第八章是否需要本地 GPU？

不需要。第八章的模型采样、logprob 计算、LoRA 前向反向传播和参数更新由 PyTRIO 远端完成。本地设备需要运行数据处理与环境交互，其中 Search-R1 依赖联网搜索，ReTool 还需要安全隔离的代码执行环境。

##### 6.4 从哪一章开始动手最合适？

如果你偏向理解底层实现，建议从第 5 章开始；如果你更关注工业界常用训练框架，建议先完成第 1 章到第 4 章的基础阅读，再进入第 6 章和第 7 章。学习 Agentic RL 时，可以在完成强化学习与 Agent 基础后进入第 8 章，按照 GRPO、OPD、Search-R1、ReTool 的顺序实践。

### 前言

2022年底，ChatGPT 的横空出世改变了人们对人工智能的认知，也给自然语言处理（Natural Language Process，NLP）领域带来了阶段性的变革，以 GPT 系列模型为代表的大语言模型（Large Language Model，LLM）成为 NLP 乃至人工智能领域的研究主流。自 2023年至今，LLM 始终是人工智能领域的核心话题，引发了一轮又一轮的科技浪潮。

LLM 其实是 NLP 领域经典研究方法预训练语言模型（Pretrain Language Model，PLM）的一种衍生成果。NLP 领域聚焦于人类书写的自然语言文本的处理、理解和生成，从诞生至今经历了符号主义阶段、统计学习阶段、深度学习阶段、预训练模型阶段到而今大模型阶段的多次变革。以 GPT、BERT 为代表的 PLM 是上一阶段 NLP 领域的核心研究成果，以注意力机制为模型架构，通过预训练-微调的阶段思想通过在海量无监督文本上进行自监督预训练，实现了强大的自然语言理解能力。但是，传统的 PLM 仍然依赖于一定量有监督数据进行下游任务微调，且在自然语言生成任务上性能还不尽如人意，NLP 系统的性能距离人们所期待的通用人工智能还有不小的差距。

LLM 是在 PLM 的基础上，通过大量扩大模型参数、预训练数据规模，并引入指令微调、人类反馈强化学习等手段实现的突破性成果。相较于传统 PLM，LLM 具备涌现能力，具有强大的上下文学习能力、指令理解能力和文本生成能力。在大模型阶段，NLP 研究者可以一定程度抛弃大量的监督数据标注工作，通过提供少量监督示例，LLM 即能在指定下游任务上达到媲美大规模微调 PLM 的性能。同时，强大的指令理解能力与文本生成能力使 LLM 能够直接、高效、准确地响应用户指令，从而真正向通用人工智能的目标逼近。

LLM 的突破性进展激发了 NLP 领域乃至整个人工智能领域的研究热度，海内外高校、研究院、大厂乃至众多传统领域企业都投入到 LLM 研究的浪潮中。自 2023年至今，LLM 阶段性成果层出不穷，模型性能不断刷新上限，从一开始的 ChatGPT，到 GPT-4，再到以 DeepSeek-R1 为代表的推理大模型、以 Qwen-VL 为代表的多模态大模型等更强大、更定制化的模型，LLM 应用也不断涌现出能够提升实际生产力、赋能用户实际生活的创新应用，从”百模大战“到”Agent 元年“，LLM 基座研究或许已趋向稳定的格局，LLM 的研究始终方兴未艾。可以肯定的是，在并不遥远的未来，LLM 及以 LLM 为基础的应用一定会成为人们生活中的基础设施，与每个人的生活、学习、工作密不可分。

在这样的背景下，深入理解、掌握 LLM 原理，能够动手应用、训练任意一个 LLM 的能力，对每一位 NLP 研究者乃至其他领域的 AI 研究者至关重要。我们在 2023年底分别创建了 self-llm（开源大模型食用指南：https://github.com/datawhalechina/self-llm ）、llm-universe（动手学大模型应用开发：https://github.com/datawhalechina/llm-universe ）两个原创开源大模型教程，前者旨在为开发者提供一站式开源 LLM 部署、推理、微调的使用教程，后者旨在指导开发者从零开始搭建自己的 LLM 应用。两个教程都帮助到了广泛的国内外开发者，也获得了众多开发者的支持和认可，在学习者的反馈中，我们发现目前还缺乏一个从零开始讲解 LLM 原理、并引导学习者亲手搭建、训练 LLM 的完整教程。

鉴于此，我们编写了这本结合 LLM 原理及实战的教程。本书将从 NLP 的基本研究方法出发，根据 LLM 的思路及原理逐层深入，依次为读者剖析 LLM 的架构基础和训练过程。同时，我们会结合目前 LLM 领域最主流的代码框架，演练如何亲手搭建、训练一个 LLM，期以实现授之以鱼，更授之以渔。希望读者能从这本书开始走入 LLM 的浩瀚世界，探索 LLM 的无尽可能。

#### 写给读者的建议

本书包含 LLM 的理论基础、原理介绍和项目实战，全书包括 LLM 及 NLP 的核心思路剖析、公式解析与代码实战，旨在帮助开发者深入理解并掌握 LLM 的基本原理与应用。因此，本书适合大学生、研究人员、LLM 爱好者阅读。在阅读本书之前，你需要具备一定的编程经验，尤其是要对 Python 编程语言有一定的了解。同时，你最好具备深度学习的相关知识，并了解 NLP 领域的相关概念和术语，以便更轻松地阅读本书。

本书分为两部分——基础知识与实战应用。第1章～第4章是基础知识部分，从浅入深介绍 LLM 的基本原理。其中，第1章简单介绍 NLP 的基本任务和发展，为非 NLP 领域研究者提供参考；第2章介绍 LLM 的基本架构——Transformer，包括原理介绍及代码实现，作为 LLM 最重要的理论基础；第3章整体介绍经典的 PLM，包括 Encoder-Only、Encoder-Decoder 和 Decoder-Only 三种架构，也同时介绍了当前一些主流 LLM 的架构和思想；第4章则正式进入 LLM 部分，详细介绍 LLM 的特点、能力和整体训练过程。第5章～第7章是实战应用部分，将逐步带领读者深入 LLM 的底层细节。其中，第5章将带领读者基于 PyTorch 层亲手搭建一个 LLM，并实现预训练、有监督微调的全流程；第6章将引入目前业界主流的 LLM 训练框架 Transformers，带领读者基于该框架快速、高效地实现 LLM 训练过程；第7章则将介绍 基于 LLM 的各种应用，补全读者对 LLM 体系的认知，包括 LLM 的评测、检索增强生成（Retrieval-Augmented Generation，RAG）、智能体（Agent）的思想和简单实现。你可以根据个人兴趣和需求，选择性地阅读相关章节。

在阅读本书的过程中，建议你将理论和实际相结合。LLM 是一个快速发展、注重实践的领域，我们建议你多投入实战，复现本书提供的各种代码，同时积极参加 LLM 相关的项目与比赛，真正投入到 LLM 开发的浪潮中。我们鼓励你关注 Datawhale 及其他 LLM 相关开源社区，当遇到问题时，你可以随时在 Datawhale 社区提问。Datawhale 也会始终跟进 LLM 及其他人工智能技术的发展，欢迎你关注或加入到 Datawhale 社区的共建中。

最后，欢迎每一位读者在阅读完本书后加入到 LLM 开发者的行列。作为国内 AI 开源社区，我们希望充分聚集共创者，一起丰富这个开源 LLM 的世界，打造更多、更全面特色 LLM 的教程。星火点点，汇聚成海。我们希望成为 LLM 与普罗大众的阶梯，以自由、平等的开源精神，拥抱更恢弘而辽阔的 LLM 世界。

感谢你选择本书，祝你阅读愉快！

## 基础原理

### 第一章 NLP 基础概念

自然语言处理（Natural Language Processing，NLP）作为人工智能领域的一个重要分支，旨在使计算机能够理解和处理人类语言，实现人机之间的自然交流。随着信息技术的飞速发展，文本数据已成为我们日常生活中不可或缺的一部分，NLP技术的进步为我们从海量文本中提取有用信息、理解语言的深层含义提供了强有力的工具。从早期的基于规则的方法，到后来的统计学习方法，再到当前深度学习技术的广泛应用，NLP领域经历了多次技术革新，文本表示作为NLP的核心技术之一，其研究和进步对于提升NLP系统的性能具有决定性的作用。

欢迎大家来到 NLP 基础概念的学习，本章节将为大家介绍 NLP 的基础概念，帮助大家更好地理解和回顾 NLP 的相关知识。

#### 1.1 什么是 NLP

NLP 是 一种让计算机理解、解释和生成人类语言的技术。它是人工智能领域中一个极为活跃和重要的研究方向，其核心任务是通过计算机程序来模拟人类对语言的认知和使用过程。NLP 结合了计算机科学、人工智能、语言学和心理学等多个学科的知识和技术，旨在打破人类语言和计算机语言之间的障碍，实现无缝的交流与互动。

NLP技术使得计算机能够执行各种复杂的语言处理任务，如中文分词、子词切分、词性标注、文本分类、实体识别、关系抽取、文本摘要、机器翻译、自动问答等。这些任务不仅要求计算机能够识别和处理语言的表层结构，更重要的是可以理解语言背后的深层含义，包括语义、语境、情感和文化等方面的复杂因素。

随着深度学习等现代技术的发展，NLP 已经取得了显著的进步。通过训练大量的数据，深度学习模型能够学习到语言的复杂模式和结构，从而在多个 NLP 任务上取得了接近甚至超越人类水平的性能。然而，尽管如此，NLP 仍然面临着诸多挑战，如处理歧义性、理解抽象概念、处理隐喻和讽刺等。研究人员正致力于通过更加先进的算法、更大规模的数据集和更精细的语言模型来解决这些问题，以推动NLP技术不断发展。

#### 1.2 NLP 发展历程

NLP 的发展历程是从早期的规则基础方法，到统计方法，再到现在的机器学习和深度学习方法的演变过程。每一次技术变革都极大地推动了 NLP 技术的发展，使其在机器翻译、情感分析、实体识别和文本摘要等任务上取得了显著成就。随着计算能力的不断增强和算法的不断优化，NLP的未来将更加光明，能够在更多领域发挥更加重要的作用。

##### 早期探索（1940年代 - 1960年代）

NLP 的早期探索始于二战后，当时人们认识到将一种语言自动翻译为另一种语言的重要性。1950年，艾伦·图灵提出了图灵测试。

> 他说，如果一台机器可以通过使用打字机成为对话的一部分，并且能够完全模仿人类，没有明显的差异，那么机器可以被认为是能够思考的。

这是判断机器是否能够展现出与人类不可区分的智能行为的测试。这一时期，诺姆·乔姆斯基提出了生成语法理论，这对理解机器翻译的工作方式产生了重要影响。然而，这一时期的机器翻译系统非常简单，主要依赖字典查找和基本的词序规则来进行翻译，效果并不理想。

##### 符号主义与统计方法（1970年代 - 1990年代）

1970年代以后，NLP 研究者开始探索新的领域，包括逻辑基础的范式和自然语言理解。这一时期，研究者分为符号主义（或规则基础）和统计方法两大阵营。符号主义研究者关注于形式语言和生成语法，而统计方法的研究者更加关注于统计和概率方法。1980年代，随着计算能力的提升和机器学习算法的引入，NLP领域出现了革命性的变化，统计模型开始取代复杂的“手写”规则。

##### 机器学习与深度学习（2000年代至今）

2000年代以后，随着深度学习技术的发展，NLP 领域取得了显著的进步。深度学习模型如循环神经网络（Recurrent Neural Network，RNN）、长短时记忆网络（Long Short-Term Memory，LSTM）和注意力机制等技术被广泛应用于 NLP 任务中，取得了令人瞩目的成果。2013年，Word2Vec模型的提出开创了词向量表示的新时代，为NLP任务提供了更加有效的文本表示方法。2018年，BERT模型的问世引领了预训练语言模型的新浪潮，为NLP技术的发展带来了新的机遇和挑战。近年来，基于Transformer的模型，如GPT-3，通过训练巨大参数的模型，能够生成高质量的文本，甚至在某些情况下可以与人类写作相媲美。


#### 1.3 NLP 任务

在NLP的广阔研究领域中，有几个核心任务构成了NLP领域的基础，它们涵盖了从文本的基本处理到复杂的语义理解和生成的各个方面。这些任务包括但不限于中文分词、子词切分、词性标注、文本分类、实体识别、关系抽取、文本摘要、机器翻译以及自动问答系统的开发。每一项任务都有其特定的挑战和应用场景，它们共同推动了语言技术的发展，为处理和分析日益增长的文本数据提供了强大的工具。

##### 1.3.1 中文分词

中文分词（Chinese Word Segmentation, CWS）是 NLP 领域中的一个基础任务。在处理中文文本时，由于中文语言的特点，词与词之间没有像英文那样的明显分隔（如空格），所以无法直接通过空格来确定词的边界。因此，中文分词成为了中文文本处理的首要步骤，其目的是将连续的中文文本切分成有意义的词汇序列。

```
英文输入：The cat sits on the mat.
英文切割输出：[The | cat | sits | on | the | mat]
中文输入：今天天气真好，适合出去游玩.
中文切割输出：["今天", "天气", "真", "好", "，", "适合", "出去", "游玩", "。"]
```

正确的分词结果对于后续的词性标注、实体识别、句法分析等任务至关重要。如果分词不准确，将直接影响到整个文本处理流程的效果。

```
输入：雍和宫的荷花开的很好。

正确切割：雍和宫 | 的 | 荷花 | 开 | 的 | 很 | 好 | 。
错误切割 1：雍 | 和 | 宫的 | 荷花 | 开的 | 很好 | 。 （地名被拆散）
错误切割 2：雍和 | 宫 | 的荷 | 花开 | 的很 | 好。 （词汇边界混乱）
```

正确的分词结果对于后续的词性标注、实体识别、句法分析等任务至关重要。如果分词不准确，将直接影响到整个文本处理流程的效果。

##### 1.3.2 子词切分

子词切分（Subword Segmentation）是 NLP 领域中的一种常见的文本预处理技术，旨在将词汇进一步分解为更小的单位，即子词。子词切分特别适用于处理词汇稀疏问题，即当遇到罕见词或未见过的新词时，能够通过已知的子词单位来理解或生成这些词汇。子词切分在处理那些拼写复杂、合成词多的语言（如德语）或者在预训练语言模型（如BERT、GPT系列）中尤为重要。

子词切分的方法有很多种，常见的有Byte Pair Encoding (BPE)、WordPiece、Unigram、SentencePiece等。这些方法的基本思想是将单词分解成更小的、频繁出现的片段，这些片段可以是单个字符、字符组合或者词根和词缀。

```
输入：unhappiness

不使用子词切分：整个单词作为一个单位，输出：“unhappiness”
使用子词切分（假设BPE算法）：单词被分割为：“un”、“happi”、“ness”
```

在这个例子中，通过子词切分，“unhappiness”这个词被分解成了三个部分：前缀“un”表示否定，“happi”是“happy”的词根变体，表示幸福，“ness”是名词后缀，表示状态。即使模型从未见过“unhappiness”这个完整的单词，它也可以通过这些已知的子词来理解其大致意思为“不幸福的状态”。

##### 1.3.3 词性标注

词性标注（Part-of-Speech Tagging，POS Tagging）是 NLP 领域中的一项基础任务，它的目标是为文本中的每个单词分配一个词性标签，如名词、动词、形容词等。这个过程通常基于预先定义的词性标签集，如英语中的常见标签有名词（Noun，N）、动词（Verb，V）、形容词（Adjective，Adj）等。词性标注对于理解句子结构、进行句法分析、语义角色标注等高级NLP任务至关重要。通过词性标注，计算机可以更好地理解文本的含义，进而进行信息提取、情感分析、机器翻译等更复杂的处理。

假设我们有一个英文句子：She is playing the guitar in the park.

词性标注的结果如下：

- She (代词，Pronoun，PRP)
- is (动词，Verb，VBZ)
- playing (动词的现在分词，Verb，VBG)
- the (限定词，Determiner，DT)
- guitar (名词，Noun，NN)
- in (介词，Preposition，IN)
- the (限定词，Determiner，DT)
- park (名词，Noun，NN)
- . (标点，Punctuation，.)

词性标注通常依赖于机器学习模型，如隐马尔可夫模型（Hidden Markov Model，HMM）、条件随机场（Conditional Random Field，CRF）或者基于深度学习的循环神经网络 RNN 和长短时记忆网络 LSTM 等。这些模型通过学习大量的标注数据来预测新句子中每个单词的词性。

##### 1.3.4 文本分类

文本分类（Text Classification）是 NLP 领域的一项核心任务，涉及到将给定的文本自动分配到一个或多个预定义的类别中。这项技术广泛应用于各种场景，包括但不限于情感分析、垃圾邮件检测、新闻分类、主题识别等。文本分类的关键在于理解文本的含义和上下文，并基于此将文本映射到特定的类别。

假设有一个文本分类任务，目的是将新闻文章分类为“体育”、“政治”或“科技”三个类别之一。

```
文本：“NBA季后赛将于下周开始，湖人和勇士将在首轮对决。”
类别：“体育”

文本：“美国总统宣布将提高关税，引发国际贸易争端。”
类别：“政治”

文本：“苹果公司发布了新款 Macbook，配备了最新的m3芯片。”
类别：“科技”
```

文本分类任务的成功关键在于选择合适的特征表示和分类算法，以及拥有高质量的训练数据。随着深度学习技术的发展，使用神经网络进行文本分类已经成为一种趋势，它们能够捕捉到文本数据中的复杂模式和语义信息，从而在许多任务中取得了显著的性能提升。

##### 1.3.5 实体识别

实体识别（Named Entity Recognition, NER），也称为命名实体识别，是 NLP 领域的一个关键任务，旨在自动识别文本中具有特定意义的实体，并将它们分类为预定义的类别，如人名、地点、组织、日期、时间等。实体识别任务对于信息提取、知识图谱构建、问答系统、内容推荐等应用很重要，它能够帮助系统理解文本中的关键元素及其属性。

假设有一个实体识别任务，目的是从文本中识别出人名、地名和组织名等实体。

```
输入：李雷和韩梅梅是北京市海淀区的居民，他们计划在2024年4月7日去上海旅行。

输出：[("李雷", "人名"), ("韩梅梅", "人名"), ("北京市海淀区", "地名"), ("2024年4月7日", "日期"), ("上海", "地名")]
```

通过实体识别任务，我们不仅能识别出文本中的实体，还能了解它们的类别，为深入理解文本内容和上下文提供了重要信息。随着NLP技术的发展，实体识别的精度和效率不断提高，可以为各种NLP应用提供强大的支持。

##### 1.3.6 关系抽取

关系抽取（Relation Extraction）是 NLP 领域中的一项关键任务，它的目标是从文本中识别实体之间的语义关系。这些关系可以是因果关系、拥有关系、亲属关系、地理位置关系等，关系抽取对于理解文本内容、构建知识图谱、提升机器理解语言的能力等方面具有重要意义。

假设我们有以下句子：

```
输入：比尔·盖茨是微软公司的创始人。

输出：[("比尔·盖茨", "创始人", "微软公司")]
```

在这个例子中，关系抽取任务的目标是从文本中识别出“比尔·盖茨”和“微软公司”之间的“创始人”关系。通过关系抽取，我们可以从文本中提取出有用的信息，帮助计算机更好地理解文本内容，为后续的知识图谱构建、问答系统等任务提供支持。

##### 1.3.7 文本摘要

文本摘要（Text Summarization）是 NLP 中的一个重要任务，目的是生成一段简洁准确的摘要，来概括原文的主要内容。根据生成方式的不同，文本摘要可以分为两大类：抽取式摘要（Extractive Summarization）和生成式摘要（Abstractive Summarization）。

- 抽取式摘要：抽取式摘要通过直接从原文中选取关键句子或短语来组成摘要。优点是摘要中的信息完全来自原文，因此准确性较高。然而，由于仅仅是原文中句子的拼接，有时候生成的摘要可能不够流畅。
- 生成式摘要：与抽取式摘要不同，生成式摘要不仅涉及选择文本片段，还需要对这些片段进行重新组织和改写，并生成新的内容。生成式摘要更具挑战性，因为它需要理解文本的深层含义，并能够以新的方式表达相同的信息。生成式摘要通常需要更复杂的模型，如基于注意力机制的序列到序列模型（Seq2Seq）。

假设我们有以下新闻报道：

```
2021年5月22日，国家航天局宣布，我国自主研发的火星探测器“天问一号”成功在火星表面着陆。此次任务的成功，标志着我国在深空探测领域迈出了重要一步。“天问一号”搭载了多种科学仪器，将在火星表面进行为期90个火星日的科学探测工作，旨在研究火星地质结构、气候条件以及寻找生命存在的可能性。
```

抽取式摘要：

```
我国自主研发的火星探测器“天问一号”成功在火星表面着陆，标志着我国在深空探测领域迈出了重要一步。
```

生成式摘要：

```
“天问一号”探测器成功实现火星着陆，代表我国在宇宙探索中取得重大进展。
```

文本摘要任务在信息检索、新闻推送、报告生成等领域有着广泛的应用。通过自动摘要，用户可以快速获取文本的核心信息，节省阅读时间，提高信息处理效率。

##### 1.3.8 机器翻译

机器翻译（Machine Translation, MT）是 NLP 领域的一项核心任务，指使用计算机程序将一种自然语言（源语言）自动翻译成另一种自然语言（目标语言）的过程。机器翻译不仅涉及到词汇的直接转换，更重要的是要准确传达源语言文本的语义、风格和文化背景等，使得翻译结果在目标语言中自然、准确、流畅，以便跨越语言障碍，促进不同语言使用者之间的交流与理解。

假设我们有一句中文：“今天天气很好。”，我们想要将其翻译成英文。

```
源语言：今天天气很好。

目标语言：The weather is very nice today.
```

在这个简单的例子中，机器翻译能够准确地将中文句子转换成英文，保持了原句的意义和结构。然而，在处理更长、更复杂的文本时，机器翻译面临的挑战也会相应增加。为了提高机器翻译的质量，研究者不断探索新的方法和技术，如基于神经网络的Seq2Seq模型、Transformer模型等，这些模型能够学习到源语言和目标语言之间的复杂映射关系，从而实现更加准确和流畅的翻译。

##### 1.3.9 自动问答

自动问答（Automatic Question Answering, QA）是 NLP 领域中的一个高级任务，旨在使计算机能够理解自然语言提出的问题，并根据给定的数据源自动提供准确的答案。自动问答任务模拟了人类理解和回答问题的能力，涵盖了从简单的事实查询到复杂的推理和解释。自动问答系统的构建涉及多个NLP子任务，如信息检索、文本理解、知识表示和推理等。

自动问答大致可分为三类：检索式问答（Retrieval-based QA）、知识库问答（Knowledge-based QA）和社区问答（Community-based QA）。检索式问答通过搜索引擎等方式从大量文本中检索答案；知识库问答通过结构化的知识库来回答问题；社区问答则依赖于用户生成的问答数据，如问答社区、论坛等。

自动问答系统的开发和优化是一个持续的过程，随着技术的进步和算法的改进，这些系统在准确性、理解能力和应用范围上都有显著的提升。通过结合不同类型的数据源和技术方法，自动问答系统正变得越来越智能，越来越能够处理复杂和多样化的问题。

#### 1.4 文本表示的发展历程

文本表示的目的是将人类语言的自然形式转化为计算机可以处理的形式，也就是将文本数据数字化，使计算机能够对文本进行有效的分析和处理。文本表示是 NLP 领域中的一项基础性和必要性工作，它直接影响甚至决定着 NLP 系统的质量和性能。

在 NLP 中，文本表示涉及到将文本中的语言单位（如字、词、短语、句子等）以及它们之间的关系和结构信息转换为计算机能够理解和操作的形式，例如向量、矩阵或其他数据结构。这样的表示不仅需要保留足够的语义信息，以便于后续的 NLP 任务，如文本分类、情感分析、机器翻译等，还需要考虑计算效率和存储效率。

文本表示的发展历程经历了多个阶段，从早期的基于规则的方法，到统计学习方法，再到当前的深度学习技术，文本表示技术不断演进，为 NLP 的发展提供了强大的支持。

##### 1.4.1 词向量

向量空间模型（Vector Space Model, VSM）是 NLP 领域中一个基础且强大的文本表示方法，最早由哈佛大学Salton提出。向量空间模型通过将文本（包括单词、句子、段落或整个文档）转换为高维空间中的向量来实现文本的数学化表示。在这个模型中，每个维度代表一个特征项（例如，字、词、词组或短语），而向量中的每个元素值代表该特征项在文本中的权重，这种权重通过特定的计算公式（如词频TF、逆文档频率TF-IDF等）来确定，反映了特征项在文本中的重要程度。

向量空间模型的应用极其广泛，包括但不限于文本相似度计算、文本分类、信息检索等自然语言处理任务。它将复杂的文本数据转换为易于计算和分析的数学形式，使得文本的相似度计算和模式识别成为可能。此外，通过矩阵运算如特征值计算、奇异值分解（singular value decomposition, SVD）等方法，可以优化文本向量表示，进一步提升处理效率和效果。

然而，向量空间模型也存在很多问题。其中最主要的是数据稀疏性和维数灾难问题，因为特征项数量庞大导致向量维度极高，同时多数元素值为零。此外，由于模型基于特征项之间的独立性假设，忽略了文本中的结构信息，如词序和上下文信息，限制了模型的表现力。特征项的选择和权重计算方法的不足也是向量空间模型需要解决的问题。

VSM 方法词向量：

```python
# "雍和宫的荷花很美"
# 词汇表大小：16384，句子包含词汇：["雍和宫", "的", "荷花", "很", "美"] = 5个词

vector = [0, 0, ..., 1, 0, ..., 1, 0, ..., 1, 0, ..., 1, 0, ..., 1, 0, ...]
#                    ↑          ↑          ↑          ↑          ↑
#      16384维中只有5个位置为1，其余16379个位置为0
# 实际有效维度：仅5维（非零维度）
# 稀疏率：(16384-5)/16384 ≈ 99.97%
```
> 词汇表是一个包含所有可能出现的词语的集合。在向量空间模型中，每个词对应词汇表中的一个位置，通过这种方式可以将词语转换为向量表示。例如，如果词汇表大小为 16384 ，那么每个词都会被表示为一个 16384 维的向量，其中只有该词对应的位置为 1，其他位置都为 0。

为了解决这些问题，研究者们对向量空间模型的研究主要集中在两个方面：一是改进特征表示方法，如借助图方法、主题方法等进行关键词抽取；二是改进和优化特征项权重的计算方法，可以在现有方法的基础上进行融合计算或提出新的计算方法.

##### 1.4.2 语言模型

N-gram 模型是 NLP 领域中一种基于统计的语言模型，广泛应用于语音识别、手写识别、拼写纠错、机器翻译和搜索引擎等众多任务。N-gram模型的核心思想是基于马尔可夫假设，即一个词的出现概率仅依赖于它前面的N-1个词。这里的N代表连续出现单词的数量，可以是任意正整数。例如，当N=1时，模型称为unigram，仅考虑单个词的概率；当N=2时，称为bigram，考虑前一个词来估计当前词的概率；当N=3时，称为trigram，考虑前两个词来估计第三个词的概率，以此类推N-gram。

N-gram模型通过条件概率链式规则来估计整个句子的概率。具体而言，对于给定的一个句子，模型会计算每个N-gram出现的条件概率，并将这些概率相乘以得到整个句子的概率。例如，对于句子“The quick brown fox”，作为trigram模型，我们会计算 $P("brown" | "The", "quick")$、$P("fox" | "quick", "brown")$等概率，并将它们相乘。

N-gram的优点是实现简单、容易理解，在许多任务中效果不错。但当N较大时，会出现数据稀疏性问题。模型的参数空间会急剧增大，相同的N-gram序列出现的概率变得非常低，导致模型无法有效学习，模型泛化能力下降。此外，N-gram模型忽略了词之间的范围依赖关系，无法捕捉到句子中的复杂结构和语义信息。

尽管存在局限性，N-gram模型由于其简单性和实用性，在许多 NLP 任务中仍然被广泛使用。在某些应用中，结合N-gram模型和其他技术（如深度学习模型）可以获得更好的性能。

##### 1.4.3 Word2Vec

Word2Vec是一种流行的词嵌入（Word Embedding）技术，由Tomas Mikolov等人在2013年提出。它是一种基于神经网络NNLM的语言模型，旨在通过学习词与词之间的上下文关系来生成词的密集向量表示。Word2Vec的核心思想是利用词在文本中的上下文信息来捕捉词之间的语义关系，从而使得语义相似或相关的词在向量空间中距离较近。

Word2Vec模型主要有两种架构：连续词袋模型CBOW(Continuous Bag of Words)是根据目标词上下文中的词对应的词向量, 计算并输出目标词的向量表示；Skip-Gram模型与CBOW模型相反, 是利用目标词的向量表示计算上下文中的词向量. 实践验证CBOW适用于小型数据集, 而Skip-Gram在大型语料中表现更好。

相比于传统的高维稀疏表示（如One-Hot编码），Word2Vec生成的是低维（通常几百维）的密集向量，有助于减少计算复杂度和存储需求。Word2Vec模型能够捕捉到词与词之间的语义关系，比如”国王“和“王后”在向量空间中的位置会比较接近，因为在大量文本中，它们通常会出现在相似的上下文中。Word2Vec模型也可以很好的泛化到未见过的词，因为它是基于上下文信息学习的，而不是基于词典。但由于CBOW/Skip-Gram模型是基于局部上下文的，无法捕捉到长距离的依赖关系，缺乏整体的词与词之间的关系，因此在一些复杂的语义任务上表现不佳。

##### 1.4.4 ELMo

ELMo（Embeddings from Language Models）实现了一词多义、静态词向量到动态词向量的跨越式转变。首先在大型语料库上训练语言模型，得到词向量模型，然后在特定任务上对模型进行微调，得到更适合该任务的词向量，ELMo首次将预训练思想引入到词向量的生成中，使用双向LSTM结构，能够捕捉到词汇的上下文信息，生成更加丰富和准确的词向量表示。

ELMo采用典型的两阶段过程: 第1个阶段是利用语言模型进行预训练; 第2个阶段是在做特定任务时, 从预训练网络中提取对应单词的词向量作为新特征补充到下游任务中。基于RNN的LSTM模型训练时间长, 特征提取是ELMo模型优化和提升的关键。

ELMo模型的主要优势在于其能够捕捉到词汇的多义性和上下文信息，生成的词向量更加丰富和准确，适用于多种 NLP 任务。然而，ELMo模型也存在一些问题，如模型复杂度高、训练时间长、计算资源消耗大等。

#### 参考文献

[1] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, Jeffrey Dean. (2013). *Distributed Representations of Words and Phrases and their Compositionality.* arXiv preprint arXiv:1310.4546.

[2] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805.

[3] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin. (2023). *Attention Is All You Need.* arXiv preprint arXiv:1706.03762.

[4] Malek Hajjem, Chiraz Latiri. (2017). *Combining IR and LDA Topic Modeling for Filtering Microblogs.* Procedia Computer Science, 112, 761–770. https://doi.org/10.1016/j.procs.2017.08.166.

[5] Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer. (2018). *Deep contextualized word representations.* arXiv preprint arXiv:1802.05365.

[6] Salton, G., Wong, A., Yang, C. S. (1975). *A vector space model for automatic indexing.* Communications of the ACM, 18(11), 613–620. https://doi.org/10.1145/361219.361220.

[7] 赵京胜,宋梦雪,高祥,等.自然语言处理中的文本表示研究[J].软件学报,2022,33(01):102-128.DOI:10.13328/j.cnki.jos.006304.

[8] 中文信息处理发展报告（2016）前言[C]//中文信息处理发展报告（2016）.中国中文信息学会;,2016:2-3.DOI:10.26914/c.cnkihy.2016.003326.

### 第二章 Transformer 架构

#### 2.1 注意力机制

##### 2.1.1 什么是注意力机制

随着 NLP 从统计机器学习向深度学习迈进，作为 NLP 核心问题的文本表示方法也逐渐从统计学习向深度学习迈进。正如我们在第一章所介绍的，文本表示从最初的通过统计学习模型进行计算的向量空间模型、语言模型，通过 Word2Vec 的单层神经网络进入到通过神经网络学习文本表示的时代。但是，从 计算机视觉（Computer Vision，CV）为起源发展起来的神经网络，其核心架构有三种：

- 前馈神经网络（Feedforward Neural Network，FNN），即数据从输入层单向流动到输出层，无循环结构，各层之间通过全连接或特定方式传递信息，其中多层感知机（Multi-Layer Perceptron，MLP）是最常见的形式，每一层的神经元都和上下两层的每一个神经元完全连接，如图2.1所示:


![图2.1 全连接神经网络](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/2-figures/1-0.png)
图2.1 全连接神经网络


- 卷积神经网络（Convolutional Neural Network，CNN），即训练参数量远小于全连接神经网络的卷积层来进行特征提取和学习，如图2.2所示:


![图2.2 卷积神经网络](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/2-figures/1-1.png)
图2.2 卷积神经网络


- 循环神经网络（Recurrent Neural Network，RNN），能够使用历史信息作为输入、包含环和自重复的网络，如图2.3所示:


![图2.3 循环神经网络](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/2-figures/1-2.png)
图2.3 循环神经网络


由于 NLP 任务所需要处理的文本往往是序列，因此专用于处理序列、时序数据的 RNN 往往能够在 NLP 任务上取得最优的效果。事实上，在注意力机制横空出世之前，RNN 以及 RNN 的衍生架构 LSTM 是 NLP 领域当之无愧的霸主。例如，我们在第一章讲到过的开创了预训练思想的文本表示模型 ELMo，就是使用的双向 LSTM 作为网络架构。

但 RNN 及 LSTM 虽然具有捕捉时序信息、适合序列生成的优点，却有两个难以弥补的缺陷：

1. 序列依序计算的模式能够很好地模拟时序信息，但限制了计算机并行计算的能力。由于序列需要依次输入、依序计算，图形处理器（Graphics Processing Unit，GPU）并行计算的能力受到了极大限制，导致 RNN 为基础架构的模型虽然参数量不算特别大，但计算时间成本却很高；

2. RNN 难以捕捉长序列的相关关系。在 RNN 架构中，距离越远的输入之间的关系就越难被捕捉，同时 RNN 需要将整个序列读入内存依次计算，也限制了序列的长度。虽然 LSTM 中通过门机制对此进行了一定优化，但对于较远距离相关关系的捕捉，RNN 依旧是不如人意的。

针对这样的问题，Vaswani 等学者参考了在 CV 领域被提出、被经常融入到 RNN 中使用的注意力机制（Attention）（注意，虽然注意力机制在 NLP 被发扬光大，但其确实是在 CV 领域被提出的），创新性地搭建了完全由注意力机制构成的神经网络——Transformer，也就是大语言模型（Large Language Model，LLM）的鼻祖及核心架构，从而让注意力机制一跃成为深度学习最核心的架构之一。

那么，究竟什么是注意力机制？

注意力机制最先源于计算机视觉领域，其核心思想为当我们关注一张图片，我们往往无需看清楚全部内容而仅将注意力集中在重点部分即可。而在自然语言处理领域，我们往往也可以通过将重点注意力集中在一个或几个 token，从而取得更高效高质的计算效果。

注意力机制有三个核心变量：**Query**（查询值）、**Key**（键值）和 **Value**（真值）。我们可以通过一个案例来理解每一个变量所代表的含义。例如，当我们有一篇新闻报道，我们想要找到这个报道的时间，那么，我们的 Query 可以是类似于“时间”、“日期”一类的向量（为了便于理解，此处使用文本来表示，但其实际是稠密的向量），Key 和 Value 会是整个文本。通过对 Query 和 Key 进行运算我们可以得到一个权重，这个权重其实反映了从 Query 出发，对文本每一个 token 应该分布的注意力相对大小。通过把权重和 Value 进行运算，得到的最后结果就是从 Query 出发计算整个文本注意力得到的结果。

​具体而言，注意力机制的特点是通过计算 **Query** 与**Key**的相关性为真值加权求和，从而拟合序列中每个词同其他词的相关关系。

##### 2.1.2 深入理解注意力机制

刚刚我们说到，注意力机制有三个核心变量：查询值 Query，键值 Key 和 真值 Value。接下来我们以字典为例，逐步分析注意力机制的计算公式是如何得到的，从而帮助读者深入理解注意力机制。首先，我们有这样一个字典：

```json
{
    "apple":10,
    "banana":5,
    "chair":2
}
```

此时，字典的键就是注意力机制中的键值 Key，而字典的值就是真值 Value。字典支持我们进行精确的字符串匹配，例如，如果我们想要查找的值也就是查询值 Query 为“apple”，那么我们可以直接通过将 Query 与 Key 做匹配来得到对应的 Value。

但是，如果我们想要匹配的 Query 是一个包含多个 Key 的概念呢？例如，我们想要查找“fruit”，此时，我们应该将 apple 和 banana 都匹配到，但不能匹配到 chair。因此，我们往往会选择将 Key 对应的 Value 进行组合得到最终的 Value。

例如，当我们的 Query 为“fruit”，我们可以分别给三个 Key 赋予如下的权重：

```json
{
    "apple":0.6,
    "banana":0.4,
    "chair":0
}
```

那么，我们最终查询到的值应该是：

$$
value = 0.6 * 10 + 0.4 * 5 + 0 * 2 = 8
$$

给不同 Key 所赋予的不同权重，就是我们所说的注意力分数，也就是为了查询到 Query，我们应该赋予给每一个 Key 多少注意力。但是，如何针对每一个 Query，计算出对应的注意力分数呢？从直观上讲，我们可以认为 Key 与 Query 相关性越高，则其所应该赋予的注意力权重就越大。但是，我们如何能够找到一个合理的、能够计算出正确的注意力分数的方法呢？

在第一章中，我们有提到词向量的概念。通过合理的训练拟合，词向量能够表征语义信息，从而让语义相近的词在向量空间中距离更近，语义较远的词在向量空间中距离更远。我们往往用欧式距离来衡量词向量的相似性，但我们同样也可以用点积来进行度量：

$$
v·w = \sum_{i}v_iw_i
$$

根据词向量的定义，语义相似的两个词对应的词向量的点积应该大于0，而语义不相似的词向量点积应该小于0。

那么，我们就可以用点积来计算词之间的相似度。假设我们的 Query 为“fruit”，对应的词向量为 $q$ ；我们的 Key 对应的词向量为 $k = [v_{apple} v_{banana} v_{chair}]$ ,则我们可以计算 Query 和每一个键的相似程度：

$$
x = qK^T
$$

此处的 K 即为将所有 Key 对应的词向量堆叠形成的矩阵。基于矩阵乘法的定义，x 即为 q 与每一个 k 值的点积。现在我们得到的 x 即反映了 Query 和每一个 Key 的相似程度，我们再通过一个 Softmax 层将其转化为和为 1 的权重：

$$
\text{softmax}(x)_i = \frac{e^{xi}}{\sum_{j}e^{x_j}}
$$

这样，得到的向量就能够反映 Query 和每一个 Key 的相似程度，同时又相加权重为 1，也就是我们的注意力分数了。最后，我们再将得到的注意力分数和值向量做对应乘积即可。根据上述过程，我们就可以得到注意力机制计算的基本公式：

$$
attention(Q,K,V) = softmax(qK^T)v
$$

不过，此时的值还是一个标量，同时，我们此次只查询了一个 Query。我们可以将值转化为维度为 $d_v$ 的向量，同时一次性查询多个 Query，同样将多个 Query 对应的词向量堆叠在一起形成矩阵 Q，得到公式：

$$
attention(Q,K,V) = softmax(QK^T)V
$$

目前，我们离标准的注意力机制公式还差最后一步。在上一个公式中，如果 Q 和 K 对应的维度 $d_k$ 比较大，softmax 放缩时就非常容易受影响，使不同值之间的差异较大，从而影响梯度的稳定性。因此，我们要将 Q 和 K 乘积的结果做一个放缩：

$$
attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})V
$$

这也就是注意力机制的核心计算公式了。

##### 2.1.3 注意力机制的实现

基于上文，我们可以很简单地使用 Pytorch 来实现注意力机制的代码：

```python
'''注意力计算函数'''
def attention(query, key, value, dropout=None):
    '''
    args:
    query: 查询值矩阵
    key: 键值矩阵
    value: 真值矩阵
    '''
    # 获取键向量的维度，键向量的维度和值向量的维度相同
    d_k = query.size(-1)
    # 计算Q与K的内积并除以根号dk
    # transpose——相当于转置
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    # Softmax
    p_attn = scores.softmax(dim=-1)
    if dropout is not None:
        p_attn = dropout(p_attn)
        # 采样
     # 根据计算结果对value进行加权求和
    return torch.matmul(p_attn, value), p_attn

```

注意，在上文代码中，我们假设输入的 q、k、v 是已经经过转化的词向量矩阵，也就是公式中的 Q、K、V。我们仅需要通过上述几行代码，就可以实现核心的注意力机制计算。

##### 2.1.4 自注意力

根据上文的分析，我们可以发现，注意力机制的本质是对两段序列的元素依次进行相似度计算，寻找出一个序列的每个元素对另一个序列的每个元素的相关度，然后基于相关度进行加权，即分配注意力。而这两段序列即是我们计算过程中 Q、K、V 的来源。

但是，在我们的实际应用中，我们往往只需要计算 Query 和 Key 之间的注意力结果，很少存在额外的真值 Value。也就是说，我们其实只需要拟合两个文本序列。​在经典的 注意力机制中，Q 往往来自于一个序列，K 与 V 来自于另一个序列，都通过参数矩阵计算得到，从而可以拟合这两个序列之间的关系。例如在 Transformer 的 Decoder 结构中，Q 来自于 Decoder 的输入，K 与 V 来自于 Encoder 的输出，从而拟合了编码信息与历史信息之间的关系，便于综合这两种信息实现未来的预测。

​但在 Transformer 的 Encoder 结构中，使用的是 注意力机制的变种 —— 自注意力（self-attention，自注意力）机制。所谓自注意力，即是计算本身序列中每个元素对其他元素的注意力分布，即在计算过程中，Q、K、V 都由同一个输入通过不同的参数矩阵计算得到。在 Encoder 中，Q、K、V 分别是输入对参数矩阵 $W_q、W_k、W_v$ 做积得到，从而拟合输入语句中每一个 token 对其他所有 token 的关系。

通过自注意力机制，我们可以找到一段文本中每一个 token 与其他所有 token 的相关关系大小，从而建模文本之间的依赖关系。​在代码中的实现，self-attention 机制其实是通过给 Q、K、V 的输入传入同一个参数实现的：

```python
# attention 为上文定义的注意力计算函数
attention(x, x, x)
```

##### 2.1.5 掩码自注意力

掩码自注意力，即 Mask Self-Attention，是指使用注意力掩码的自注意力机制。掩码的作用是遮蔽一些特定位置的 token，模型在学习的过程中，会忽略掉被遮蔽的 token。

使用注意力掩码的核心动机是让模型只能使用历史信息进行预测而不能看到未来信息。使用注意力机制的 Transformer 模型也是通过类似于 n-gram 的语言模型任务来学习的，也就是对一个文本序列，不断根据之前的 token 来预测下一个 token，直到将整个文本序列补全。

例如，如果待学习的文本序列是 【BOS】I like you【EOS】，那么，模型会按如下顺序进行预测和学习：

    Step 1：输入 【BOS】，输出 I
    Step 2：输入 【BOS】I，输出 like
    Step 3：输入 【BOS】I like，输出 you
    Step 4：输入 【BOS】I like you，输出 【EOS】

理论上来说，只要学习的语料足够多，通过上述的过程，模型可以学会任意一种文本序列的建模方式，也就是可以对任意的文本进行补全。

但是，我们可以发现，上述过程是一个串行的过程，也就是需要先完成 Step 1，才能做 Step 2，接下来逐步完成整个序列的补全。我们在一开始就说过，Transformer 相对于 RNN 的核心优势之一即在于其可以并行计算，具有更高的计算效率。如果对于每一个训练语料，模型都需要串行完成上述过程才能完成学习，那么很明显没有做到并行计算，计算效率很低。

针对这个问题，Transformer 就提出了掩码自注意力的方法。掩码自注意力会生成一串掩码，来遮蔽未来信息。例如，我们待学习的文本序列仍然是 【BOS】I like you【EOS】，我们使用的注意力掩码是【MASK】，那么模型的输入为：

    <BOS> 【MASK】【MASK】【MASK】【MASK】
    <BOS>    I   【MASK】 【MASK】【MASK】
    <BOS>    I     like  【MASK】【MASK】
    <BOS>    I     like    you  【MASK】
    <BOS>    I     like    you   </EOS>

在每一行输入中，模型仍然是只看到前面的 token，预测下一个 token。但是注意，上述输入不再是串行的过程，而可以一起并行地输入到模型中，模型只需要每一个样本根据未被遮蔽的 token 来预测下一个 token 即可，从而实现了并行的语言模型。

观察上述的掩码，我们可以发现其实则是一个和文本序列等长的上三角矩阵。我们可以简单地通过创建一个和输入同等长度的上三角矩阵作为注意力掩码，再使用掩码来遮蔽掉输入即可。也就是说，当输入维度为 （batch_size, seq_len, hidden_size）时，我们的 Mask 矩阵维度一般为 (1, seq_len, seq_len)（通过广播实现同一个 batch 中不同样本的计算）。

在具体实现中，我们通过以下代码生成 Mask 矩阵：

```python
# 创建一个上三角矩阵，用于遮蔽未来信息。
# 先通过 full 函数创建一个 1 * seq_len * seq_len 的矩阵
mask = torch.full((1, args.max_seq_len, args.max_seq_len), float("-inf"))
# triu 函数的功能是创建一个上三角矩阵
mask = torch.triu(mask, diagonal=1)
```

生成的 Mask 矩阵会是一个上三角矩阵，上三角位置的元素均为 -inf，其他位置的元素置为0。

在注意力计算时，我们会将计算得到的注意力分数与这个掩码做和，再进行 Softmax 操作：

```python
# 此处的 scores 为计算得到的注意力分数，mask 为上文生成的掩码矩阵
scores = scores + mask[:, :seqlen, :seqlen]
scores = F.softmax(scores.float(), dim=-1).type_as(xq)
```

通过做求和，上三角区域（也就是应该被遮蔽的 token 对应的位置）的注意力分数结果都变成了 `-inf`，而下三角区域的分数不变。再做 Softmax 操作，`-inf` 的值在经过 Softmax 之后会被置为 0，从而忽略了上三角区域计算的注意力分数，从而实现了注意力遮蔽。

##### 2.1.6 多头注意力

注意力机制可以实现并行化与长期依赖关系拟合，但一次注意力计算只能拟合一种相关关系，单一的注意力机制很难全面拟合语句序列里的相关关系。因此 Transformer 使用了多头注意力机制（Multi-Head Attention），即同时对一个语料进行多次注意力计算，每次注意力计算都能拟合不同的关系，将最后的多次结果拼接起来作为最后的输出，即可更全面深入地拟合语言信息。

在原论文中，作者也通过实验证实，多头注意力计算中，每个不同的注意力头能够拟合语句中的不同信息，如图2.4所示：


![图2.4 多头注意力机制](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/2-figures/1-3.jpeg)
图2.4 多头注意力机制


​上层与下层分别是两个注意力头对同一段语句序列进行自注意力计算的结果，可以看到，对于不同的注意力头，能够拟合不同层次的相关信息。通过多个注意力头同时计算，能够更全面地拟合语句关系。

事实上，所谓的多头注意力机制其实就是将原始的输入序列进行多组的自注意力处理；然后再将每一组得到的自注意力结果拼接起来，再通过一个线性层进行处理，得到最终的输出。我们用公式可以表示为：

$$
\mathrm{MultiHead}(Q, K, V) = \mathrm{Concat}(\mathrm{head_1}, ...,
\mathrm{head_h})W^O    \\
    \text{where}~\mathrm{head_i} = \mathrm{Attention}(QW^Q_i, KW^K_i, VW^V_i)
$$

其最直观的代码实现并不复杂，即 n 个头就有 n 组3个参数矩阵，每一组进行同样的注意力计算，但由于是不同的参数矩阵从而通过反向传播实现了不同的注意力结果，然后将 n 个结果拼接起来输出即可。

但上述实现时空复杂度均较高，我们可以通过矩阵运算巧妙地实现并行的多头计算，其核心逻辑在于使用三个组合矩阵来代替了n个参数矩阵的组合，也就是矩阵内积再拼接其实等同于拼接矩阵再内积。具体实现可以参考下列代码：

```python
import torch.nn as nn
import torch

'''多头自注意力计算模块'''
class MultiHeadAttention(nn.Module):

    def __init__(self, args: ModelArgs, is_causal=False):
        # 构造函数
        # args: 配置对象
        super().__init__()
        # 隐藏层维度必须是头数的整数倍，因为后面我们会将输入拆成头数个矩阵
        assert args.dim % args.n_heads == 0
        # 每个头的维度，等于模型维度除以头的总数。
        self.head_dim = args.dim // args.n_heads
        self.n_heads = args.n_heads

        # Wq, Wk, Wv 参数矩阵，每个参数矩阵为 n_embd x dim
        # 这里通过三个组合矩阵来代替了n个参数矩阵的组合，其逻辑在于矩阵内积再拼接其实等同于拼接矩阵再内积，
        # 不理解的读者可以自行模拟一下，每一个线性层其实相当于n个参数矩阵的拼接
        self.wq = nn.Linear(args.n_embd, self.n_heads * self.head_dim, bias=False)
        self.wk = nn.Linear(args.n_embd, self.n_heads * self.head_dim, bias=False)
        self.wv = nn.Linear(args.n_embd, self.n_heads * self.head_dim, bias=False)
        # 输出权重矩阵，维度为 dim x dim（head_dim = dim / n_heads）
        self.wo = nn.Linear(self.n_heads * self.head_dim, args.dim, bias=False)
        # 注意力的 dropout
        self.attn_dropout = nn.Dropout(args.dropout)
        # 残差连接的 dropout
        self.resid_dropout = nn.Dropout(args.dropout)
        self.is_causal = is_causal

        # 创建一个上三角矩阵，用于遮蔽未来信息
        # 注意，因为是多头注意力，Mask 矩阵比之前我们定义的多一个维度
        if is_causal:
            mask = torch.full((1, 1, args.max_seq_len, args.max_seq_len), float("-inf"))
            mask = torch.triu(mask, diagonal=1)
            # 注册为模型的缓冲区
            self.register_buffer("mask", mask)

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):

        # 获取批次大小和序列长度，[batch_size, seq_len, dim]
        bsz, seqlen, _ = q.shape

        # 计算查询（Q）、键（K）、值（V）,输入通过参数矩阵层，维度为 (B, T, n_embed) x (n_embed, dim) -> (B, T, dim)
        xq, xk, xv = self.wq(q), self.wk(k), self.wv(v)

        # 将 Q、K、V 拆分成多头，维度为 (B, T, n_head, dim // n_head)，然后交换维度，变成 (B, n_head, T, dim // n_head)
        # 因为在注意力计算中我们是取了后两个维度参与计算
        # 为什么要先按B*T*n_head*C//n_head展开再互换1、2维度而不是直接按注意力输入展开，是因为view的展开方式是直接把输入全部排开，
        # 然后按要求构造，可以发现只有上述操作能够实现我们将每个头对应部分取出来的目标
        xq = xq.view(bsz, seqlen, self.n_heads, self.head_dim)
        xk = xk.view(bsz, seqlen, self.n_heads, self.head_dim)
        xv = xv.view(bsz, seqlen, self.n_heads, self.head_dim)
        xq = xq.transpose(1, 2)
        xk = xk.transpose(1, 2)
        xv = xv.transpose(1, 2)

        # 注意力计算
        # 计算 QK^T / sqrt(d_k)，维度为 (B, nh, T, hs) x (B, nh, hs, T) -> (B, nh, T, T)
        scores = torch.matmul(xq, xk.transpose(2, 3)) / math.sqrt(self.head_dim)
        # 掩码自注意力必须有注意力掩码
        if self.is_causal:
            assert hasattr(self, 'mask')
            # 这里截取到序列长度，因为有些序列可能比 max_seq_len 短
            scores = scores + self.mask[:, :, :seqlen, :seqlen]
        # 计算 softmax，维度为 (B, nh, T, T)
        scores = F.softmax(scores.float(), dim=-1).type_as(xq)
        # 做 Dropout
        scores = self.attn_dropout(scores)
        # V * Score，维度为(B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
        output = torch.matmul(scores, xv)

        # 恢复时间维度并合并头。
        # 将多头的结果拼接起来, 先交换维度为 (B, T, n_head, dim // n_head)，再拼接成 (B, T, n_head * dim // n_head)
        # contiguous 函数用于重新开辟一块新内存存储，因为Pytorch设置先transpose再view会报错，
        # 因为view直接基于底层存储得到，然而transpose并不会改变底层存储，因此需要额外存储
        output = output.transpose(1, 2).contiguous().view(bsz, seqlen, -1)

        # 最终投影回残差流。
        output = self.wo(output)
        output = self.resid_dropout(output)
        return output
```

#### 2.2 Encoder-Decoder

在上一节，我们详细介绍了 Transformer 的核心——注意力机制。在《Attention is All You Need》一文中，作者通过仅使用注意力机制而抛弃传统的 RNN、CNN 架构搭建出 Transformer 模型，从而带来了 NLP 领域的大变革。在 Transformer 中，使用注意力机制的是其两个核心组件——Encoder（编码器）和 Decoder（解码器）。事实上，后续基于 Transformer 架构而来的预训练语言模型基本都是对 Encoder-Decoder 部分进行改进来构建新的模型架构，例如只使用 Encoder 的 BERT、只使用 Decoder 的 GPT 等。

在本节中，我们将以上一节所介绍的 注意力机制为基础，从 Transformer 所针对的 Seq2Seq 任务出发，解析 Transformer 的 Encoder-Decoder 结构。

##### 2.2.1 Seq2Seq 模型

Seq2Seq，即序列到序列，是一种经典 NLP 任务。具体而言，是指模型输入的是一个自然语言序列 $input = (x_1, x_2, x_3...x_n)$ ，输出的是一个可能不等长的自然语言序列 $output = (y_1, y_2, y_3...y_m)$ 。事实上，Seq2Seq 是 NLP 最经典的任务，几乎所有的 NLP 任务都可以视为 Seq2Seq 任务。例如文本分类任务，可以视为输出长度为 1 的目标序列（如在上式中 $m$ = 1）；词性标注任务，可以视为输出与输入序列等长的目标序列（如在上式中 $m$ = $n$ ）。

机器翻译任务即是一个经典的 Seq2Seq 任务，例如，我们的输入可能是“今天天气真好”，输出是“Today is a good day.”。Transformer 是一个经典的 Seq2Seq 模型，即模型的输入为文本序列，输出为另一个文本序列。事实上，Transformer 一开始正是应用在机器翻译任务上的。

对于 Seq2Seq 任务，一般的思路是对自然语言序列进行编码再解码。所谓编码，就是将输入的自然语言序列通过隐藏层编码成能够表征语义的向量（或矩阵），可以简单理解为更复杂的词向量表示。而解码，就是对输入的自然语言序列编码得到的向量或矩阵通过隐藏层输出，再解码成对应的自然语言目标序列。通过编码再解码，就可以实现 Seq2Seq 任务。

Transformer 中的 Encoder，就是用于上述的编码过程；Decoder 则用于上述的解码过程。Transformer 结构，如图2.5所示：


![图2.5 编码器-解码器结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/2-figures/2-0.jpg)
图2.5 编码器-解码器结构


Transformer 由 Encoder 和 Decoder 组成，每一个 Encoder（Decoder）又由 6个 Encoder（Decoder）Layer 组成。输入源序列会进入 Encoder 进行编码，到 Encoder Layer 的最顶层再将编码结果输出给 Decoder Layer 的每一层，通过 Decoder 解码后就可以得到输出目标序列了。

接下来，我们将首先介绍 Encoder 和 Decoder 内部传统神经网络的经典结构——前馈神经网络（FNN）、层归一化（Layer Norm）和残差连接（Residual Connection），然后进一步分析 Encoder 和 Decoder 的内部结构。

##### 2.2.2 前馈神经网络

前馈神经网络（Feed Forward Neural Network，下简称 FNN），也就是我们在上一节提过的每一层的神经元都和上下两层的每一个神经元完全连接的网络结构。每一个 Encoder Layer 都包含一个上文讲的注意力机制和一个前馈神经网络。前馈神经网络的实现是较为简单的：

```python
class MLP(nn.Module):
    '''前馈神经网络'''
    def __init__(self, dim: int, hidden_dim: int, dropout: float):
        super().__init__()
        # 定义第一层线性变换，从输入维度到隐藏维度
        self.w1 = nn.Linear(dim, hidden_dim, bias=False)
        # 定义第二层线性变换，从隐藏维度到输入维度
        self.w2 = nn.Linear(hidden_dim, dim, bias=False)
        # 定义dropout层，用于防止过拟合
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        # 前向传播函数
        # 首先，输入x通过第一层线性变换和RELU激活函数
        # 最后，通过第二层线性变换和dropout层
        return self.dropout(self.w2(F.relu(self.w1(x))))

```

注意，Transformer 的前馈神经网络是由两个线性层中间加一个 RELU 激活函数组成的，以及前馈神经网络还加入了一个 Dropout 层来防止过拟合。Dropout 层只在训练时开启，推理/测试阶段关闭，所以许多Transformer结构示意图中不会画出该层。

##### 2.2.3 层归一化

层归一化，也就是 Layer Norm，是深度学习中经典的归一化操作。神经网络主流的归一化一般有两种，批归一化（Batch Norm）和层归一化（Layer Norm）。

归一化核心是为了让不同层输入的取值范围或者分布能够比较一致。由于深度神经网络中每一层的输入都是上一层的输出，因此多层传递下，对网络中较高的层，之前的所有神经层的参数变化会导致其输入的分布发生较大的改变。也就是说，随着神经网络参数的更新，各层的输出分布是不相同的，且差异会随着网络深度的增大而增大。但是，需要预测的条件分布始终是相同的，从而也就造成了预测的误差。

因此，在深度神经网络中，往往需要归一化操作，将每一层的输入都归一化成标准正态分布。批归一化是指在一个 mini-batch 上进行归一化，相当于对一个 batch 对样本拆分出来一部分，首先计算样本的均值：

$$
\mu_j = \frac{1}{m}\sum^{m}_{i=1}Z_j^{i}
$$

其中， $Z_j^{i}$ 是样本 i 在第 j 个维度上的值，m 就是 mini-batch 的大小。

再计算样本的方差：

$$
\sigma^2 = \frac{1}{m}\sum^{m}_{i=1}(Z_j^i - \mu_j)^2
$$

最后，对每个样本的值减去均值再除以标准差来将这一个 mini-batch 的样本的分布转化为标准正态分布：

$$
\widetilde{Z_j} = \frac{Z_j - \mu_j}{\sqrt{\sigma^2 + \epsilon}}
$$

此处加上 $\epsilon$ 这一极小量是为了避免分母为0。

但是，批归一化存在一些缺陷，例如：

- 当显存有限，mini-batch 较小时，Batch Norm 取的样本的均值和方差不能反映全局的统计分布信息，从而导致效果变差；
- 对于在时间维度展开的 RNN，不同句子的同一分布大概率不同，所以 Batch Norm 的归一化会失去意义；
- 在训练时，Batch Norm 需要保存每个 step 的统计信息（均值和方差）。在测试时，由于变长句子的特性，测试集可能出现比训练集更长的句子，所以对于后面位置的 step，是没有训练的统计量使用的；
- 应用 Batch Norm，每个 step 都需要去保存和计算 batch 统计量，耗时又耗力

因此，出现了在深度神经网络中更常用、效果更好的层归一化（Layer Norm）。相较于 Batch Norm 在每一层统计所有样本的均值和方差，Layer Norm 在每个样本上计算其所有层的均值和方差，从而使每个样本的分布达到稳定。Layer Norm 的归一化方式其实和 Batch Norm 是完全一样的，只是统计统计量的维度不同。

基于上述进行归一化的公式，我们可以简单地实现一个 Layer Norm 层：

```python
class LayerNorm(nn.Module):
    ''' Layer Norm 层'''
    def __init__(self, features, eps=1e-6):
        super().__init__()
        # 线性矩阵做映射
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        # 在统计每个样本所有维度的值，求均值和方差
        mean = x.mean(-1, keepdim=True) # mean: [bsz, max_len, 1]
        std = x.std(-1, keepdim=True) # std: [bsz, max_len, 1]
        # 注意这里也在最后一个维度发生了广播
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2
```
注意，在我们上文实现的 Layer Norm 层中，有两个线性矩阵进行映射。

##### 2.2.4 残差连接

由于 Transformer 模型结构较复杂、层数较深，​为了避免模型退化，Transformer 采用了残差连接的思想来连接每一个子层。残差连接，即下一层的输入不仅是上一层的输出，还包括上一层的输入。残差连接允许最底层信息直接传到最高层，让高层专注于残差的学习。

​例如，在 Encoder 中，在第一个子层，输入会先进行层归一化（Layer Norm），然后进入多头自注意力层，其输出会与原输入相加。在第二个子层也是一样。即：

$$
x = x + MultiHeadSelfAttention(LayerNorm(x))
$$

$$
output = x + FNN(LayerNorm(x))
$$

我们在代码实现中，通过在层的 forward 计算中加上原值来实现残差连接：

```python
# 注意力计算
h = x + self.attention.forward(self.attention_norm(x))
# 经过前馈神经网络
out = h + self.feed_forward.forward(self.fnn_norm(h))
```

在上文代码中，self.attention_norm 和 self.fnn_norm 都是 LayerNorm 层，self.attn 是注意力层，而 self.feed_forward 是前馈神经网络。

##### 2.2.5 Encoder


在实现上述组件之后，我们可以搭建起 Transformer 的 Encoder。Encoder 由 N 个 Encoder Layer 组成，每一个 Encoder Layer 包括一个注意力层和一个前馈神经网络。因此，我们可以首先实现一个 Encoder Layer：

```python
class EncoderLayer(nn.Module):
  '''Encoder层'''
    def __init__(self, args):
        super().__init__()
        # 一个 Layer 中有两个 LayerNorm，分别在 Attention 之前和 MLP 之前
        self.attention_norm = LayerNorm(args.n_embd)
        # Encoder 不需要掩码，传入 is_causal=False
        self.attention = MultiHeadAttention(args, is_causal=False)
        self.fnn_norm = LayerNorm(args.n_embd)
        self.feed_forward = MLP(args.dim, args.dim, args.dropout)

    def forward(self, x):
        # Layer Norm
        norm_x = self.attention_norm(x)
        # 自注意力
        h = x + self.attention.forward(norm_x, norm_x, norm_x)
        # 经过前馈神经网络
        out = h + self.feed_forward.forward(self.fnn_norm(h))
        return out
```

然后我们搭建一个 Encoder，由 N 个 Encoder Layer 组成，在最后会加入一个 Layer Norm 实现规范化：

```python
class Encoder(nn.Module):
    '''Encoder 块'''
    def __init__(self, args):
        super(Encoder, self).__init__()
        # 一个 Encoder 由 N 个 Encoder Layer 组成
        self.layers = nn.ModuleList([EncoderLayer(args) for _ in range(args.n_layer)])
        self.norm = LayerNorm(args.n_embd)

    def forward(self, x):
        "分别通过 N 层 Encoder Layer"
        for layer in self.layers:
            x = layer(x)
        return self.norm(x)
```

通过 Encoder 的输出，就是输入编码之后的结果。

##### 2.2.6 Decoder

类似的，我们也可以先搭建 Decoder Layer，再将 N 个 Decoder Layer 组装为 Decoder。但是和 Encoder 不同的是，Decoder 由两个注意力层和一个前馈神经网络组成。第一个注意力层是一个掩码自注意力层，即使用 Mask 的注意力计算，保证每一个 token 只能使用该 token 之前的注意力分数；第二个注意力层是一个多头注意力层，该层将使用第一个注意力层的输出作为 query，使用 Encoder 的输出作为 key 和 value，来计算注意力分数。最后，再经过前馈神经网络：

```python
class DecoderLayer(nn.Module):
  '''解码层'''
    def __init__(self, args):
        super().__init__()
        # 一个 Layer 中有三个 LayerNorm，分别在 Mask Attention 之前、Self Attention 之前和 MLP 之前
        self.attention_norm_1 = LayerNorm(args.n_embd)
        # Decoder 的第一个部分是 Mask Attention，传入 is_causal=True
        self.mask_attention = MultiHeadAttention(args, is_causal=True)
        self.attention_norm_2 = LayerNorm(args.n_embd)
        # Decoder 的第二个部分是 类似于 Encoder 的 Attention，传入 is_causal=False
        self.attention = MultiHeadAttention(args, is_causal=False)
        self.ffn_norm = LayerNorm(args.n_embd)
        # 第三个部分是 MLP
        self.feed_forward = MLP(args.dim, args.dim, args.dropout)

    def forward(self, x, enc_out):
        # Layer Norm
        norm_x = self.attention_norm_1(x)
        # 掩码自注意力
        x = x + self.mask_attention.forward(norm_x, norm_x, norm_x)
        # 多头注意力
        norm_x = self.attention_norm_2(x)
        h = x + self.attention.forward(norm_x, enc_out, enc_out)
        # 经过前馈神经网络
        out = h + self.feed_forward.forward(self.ffn_norm(h))
        return out
```

然后同样的，我们搭建一个 Decoder 块：

```python
class Decoder(nn.Module):
    '''解码器'''
    def __init__(self, args):
        super(Decoder, self).__init__()
        # 一个 Decoder 由 N 个 Decoder Layer 组成
        self.layers = nn.ModuleList([DecoderLayer(args) for _ in range(args.n_layer)])
        self.norm = LayerNorm(args.n_embd)

    def forward(self, x, enc_out):
        "Pass the input (and mask) through each layer in turn."
        for layer in self.layers:
            x = layer(x, enc_out)
        return self.norm(x)
```

完成上述 Encoder、Decoder 的搭建，就完成了 Transformer 的核心部分，接下来将 Encoder、Decoder 拼接起来再加入 Embedding 层就可以搭建出完整的 Transformer 模型啦。

#### 2.3 搭建一个 Transformer

在前两章，我们分别深入剖析了 Attention 机制和 Transformer 的核心——Encoder、Decoder 结构，接下来，我们就可以基于上一章实现的组件，搭建起一个完整的 Transformer 模型。

##### 2.3.1 Embedding 层

正如我们在第一章所讲过的，在 NLP 任务中，我们往往需要将自然语言的输入转化为机器可以处理的向量。在深度学习中，承担这个任务的组件就是 Embedding 层。

Embedding 层其实是一个存储固定大小的词典的嵌入向量查找表。也就是说，在输入神经网络之前，我们往往会先让自然语言输入通过分词器 tokenizer，分词器的作用是把自然语言输入切分成 token 并转化成一个固定的 index。例如，如果我们将词表大小设为 4，输入“我喜欢你”，那么，分词器可以将输入转化成：

```
input: 我
output: 0

input: 喜欢
output: 1

input：你
output: 2
```

当然，在实际情况下，tokenizer 的工作会比这更复杂。例如，分词有多种不同的方式，可以切分成词、切分成子词、切分成字符等，而词表大小则往往高达数万数十万。此处我们不赘述 tokenizer 的详细情况，在后文会详细介绍大模型的 tokenizer 是如何运行和训练的。

因此，Embedding 层的输入往往是一个形状为 （batch_size，seq_len，1）的矩阵，第一个维度是一次批处理的数量，第二个维度是自然语言序列的长度，第三个维度则是 token 经过 tokenizer 转化成的 index 值。例如，对上述输入，Embedding 层的输入会是：

```
[[[0],[1],[2]]]
```

其 batch_size 为1，seq_len 为3，转化出来的 index 如上。

而 Embedding 内部其实是一个可训练的（Vocab_size，embedding_dim）的权重矩阵，词表里的每一个值，都对应一行维度为 embedding_dim 的向量。对于输入的值，会对应到这个词向量，然后拼接成（batch_size，seq_len，embedding_dim）的矩阵输出。

上述实现并不复杂，我们可以直接使用 torch 中的 Embedding 层：

```python
self.tok_embeddings = nn.Embedding(args.vocab_size, args.dim)
```

##### 2.3.2 位置编码

注意力机制可以实现良好的并行计算，但同时，其注意力计算的方式也导致序列中相对位置的丢失。在 RNN、LSTM 中，输入序列会沿着语句本身的顺序被依次递归处理，因此输入序列的顺序提供了极其重要的信息，这也和自然语言的本身特性非常吻合。

但从上文对注意力机制的分析我们可以发现，在注意力机制的计算过程中，对于序列中的每一个 token，其他各个位置对其来说都是平等的，即“我喜欢你”和“你喜欢我”在注意力机制看来是完全相同的，但无疑这是注意力机制存在的一个巨大问题。因此，为使用序列顺序信息，保留序列中的相对位置信息，Transformer 采用了位置编码机制，该机制也在之后被多种模型沿用。

​位置编码，即根据序列中 token 的相对位置对其进行编码，再将位置编码加入词向量编码中。位置编码的方式有很多，Transformer 使用了正余弦函数来进行位置编码（绝对位置编码Sinusoidal），其编码方式为：

$$
PE(pos, 2i) = sin(pos/10000^{2i/d_{model}})\\
PE(pos, 2i+1) = cos(pos/10000^{2i/d_{model}})
$$

上式中，pos 为 token 在句子中的位置，2i 和 2i+1 则指示了位置编码向量的维度索引是奇数还是偶数，从上式中我们可以看出对于奇数维度和偶数维度，Transformer 采用了不同的函数进行编码。

我们以一个简单的例子来说明位置编码的计算过程：假如我们输入的是一个长度为 4 的句子"I like to code"，我们可以得到下面的词向量矩阵 $\rm x$ ，其中每一行代表的就是一个词向量， $\rm x_0=[0.1,0.2,0.3,0.4]$ 对应的就是“I”的词向量，它的pos就是为0，以此类推，第二行代表的是“like”的词向量，它的pos就是1：

$$
\rm x = \begin{bmatrix}
0.1 & 0.2 & 0.3 & 0.4 \\
0.2 & 0.3 & 0.4 & 0.5 \\
0.3 & 0.4 & 0.5 & 0.6 \\
0.4 & 0.5 & 0.6 & 0.7
\end{bmatrix}
$$

​则经过位置编码后的词向量为：

$$
\rm x_{PE} = \begin{bmatrix}
0.1 & 0.2 & 0.3 & 0.4 \\
0.2 & 0.3 & 0.4 & 0.5 \\
0.3 & 0.4 & 0.5 & 0.6 \\
0.4 & 0.5 & 0.6 & 0.7
\end{bmatrix} + \begin{bmatrix}
\sin(\frac{0}{10000^0}) & \cos(\frac{0}{10000^0}) & \sin(\frac{0}{10000^{2/4}}) & \cos(\frac{0}{10000^{2/4}}) \\
\sin(\frac{1}{10000^0}) & \cos(\frac{1}{10000^0}) & \sin(\frac{1}{10000^{2/4}}) & \cos(\frac{1}{10000^{2/4}}) \\
\sin(\frac{2}{10000^0}) & \cos(\frac{2}{10000^0}) & \sin(\frac{2}{10000^{2/4}}) & \cos(\frac{2}{10000^{2/4}}) \\
\sin(\frac{3}{10000^0}) & \cos(\frac{3}{10000^0}) & \sin(\frac{3}{10000^{2/4}}) & \cos(\frac{3}{10000^{2/4}})
\end{bmatrix} = \begin{bmatrix}
0.1 & 1.2 & 0.3 & 1.4 \\
1.041 & 0.84 & 0.41 & 1.49 \\
1.209 & -0.016 & 0.52 & 1.59 \\
0.541 & -0.489 & 0.895 & 1.655
\end{bmatrix}
$$

我们可以使用如下的代码来获取上述例子的位置编码：
```python
import numpy as np
import matplotlib.pyplot as plt
def PositionEncoding(seq_len, d_model, n=10000):
    P = np.zeros((seq_len, d_model))
    for k in range(seq_len):
        for i in np.arange(int(d_model/2)):
            denominator = np.power(n, 2*i/d_model)
            P[k, 2*i] = np.sin(k/denominator)
            P[k, 2*i+1] = np.cos(k/denominator)
    return P

P = PositionEncoding(seq_len=4, d_model=4, n=100)
print(P)
```

```python
[[ 0.          1.          0.          1.        ]
 [ 0.84147098  0.54030231  0.09983342  0.99500417]
 [ 0.90929743 -0.41614684  0.19866933  0.98006658]
 [ 0.14112001 -0.9899925   0.29552021  0.95533649]]
```

这样的位置编码主要有两个好处：

1. 使 PE 能够适应比训练集里面所有句子更长的句子，假设训练集里面最长的句子是有 20 个单词，突然来了一个长度为 21 的句子，则使用公式计算的方法可以计算出第 21 位的 Embedding。
2. 可以让模型容易地计算出相对位置，对于固定长度的间距 k，PE(pos+k) 可以用 PE(pos) 计算得到。因为 Sin(A+B) = Sin(A)Cos(B) + Cos(A)Sin(B), Cos(A+B) = Cos(A)Cos(B) - Sin(A)Sin(B)。

我们也可以通过严谨的数学推导证明该编码方式的优越性。原始的 Transformer Embedding 可以表示为：

$$
\begin{equation}f(\cdots,\boldsymbol{x}_m,\cdots,\boldsymbol{x}_n,\cdots)=f(\cdots,\boldsymbol{x}_n,\cdots,\boldsymbol{x}_m,\cdots)\end{equation}
$$

很明显，这样的函数是不具有不对称性的，也就是无法表征相对位置信息。我们想要得到这样一种编码方式：

$$
\begin{equation}\tilde{f}(\cdots,\boldsymbol{x}_m,\cdots,\boldsymbol{x}_n,\cdots)=f(\cdots,\boldsymbol{x}_m + \boldsymbol{p}_m,\cdots,\boldsymbol{x}_n + \boldsymbol{p}_n,\cdots)\end{equation}
$$

这里加上的 $p_m$， $p_n$ 就是位置编码。接下来我们将 $f(...,x_m+p_m,...,x_n+p_n)$ 在 m,n 两个位置上做泰勒展开：

$$
\begin{equation}\tilde{f}\approx f + \boldsymbol{p}_m^{\top} \frac{\partial f}{\partial \boldsymbol{x}_m} + \boldsymbol{p}_n^{\top} \frac{\partial f}{\partial \boldsymbol{x}_n} + \frac{1}{2}\boldsymbol{p}_m^{\top} \frac{\partial^2 f}{\partial \boldsymbol{x}_m^2}\boldsymbol{p}_m + \frac{1}{2}\boldsymbol{p}_n^{\top} \frac{\partial^2 f}{\partial \boldsymbol{x}_n^2}\boldsymbol{p}_n + \underbrace{\boldsymbol{p}_m^{\top} \frac{\partial^2 f}{\partial \boldsymbol{x}_m \partial \boldsymbol{x}_n}\boldsymbol{p}_n}_{\boldsymbol{p}_m^{\top} \boldsymbol{\mathcal{H}} \boldsymbol{p}_n}\end{equation}
$$

可以看到第1项与位置无关，2～5项仅依赖单一位置，第6项（f 分别对 m、n 求偏导）与两个位置有关，所以我们希望第六项（ $p_m^THp_n$ ）表达相对位置信息，即求一个函数 g 使得:

$$
p_m^THp_n = g(m-n)
$$

我们假设 $H$ 是一个单位矩阵，则：

$$
p_m^THp_n = p_m^Tp_n = \langle\boldsymbol{p}_m, \boldsymbol{p}_n\rangle = g(m-n)
$$

通过将向量 [x,y] 视为复数 x+yi，基于复数的运算法则构建方程:

$$
\begin{equation}\langle\boldsymbol{p}_m, \boldsymbol{p}_n\rangle = \text{Re}[\boldsymbol{p}_m \boldsymbol{p}_n^*]\end{equation}
$$

再假设存在复数 $q_{m-n}$ 使得：

$$
\begin{equation}\boldsymbol{p}_m \boldsymbol{p}_n^* = \boldsymbol{q}_{m-n}\end{equation}
$$

使用复数的指数形式求解这个方程，得到二维情形下位置编码的解：

$$
\begin{equation}\boldsymbol{p}_m = e^{\text{i}m\theta}\quad\Leftrightarrow\quad \boldsymbol{p}_m=\begin{pmatrix}\cos m\theta \\ \sin m\theta\end{pmatrix}\end{equation}
$$

由于内积满足线性叠加性，所以更高维的偶数维位置编码，我们可以表示为多个二维位置编码的组合：

$$
\begin{equation}\boldsymbol{p}_m = \begin{pmatrix}e^{\text{i}m\theta_0} \\ e^{\text{i}m\theta_1} \\ \vdots \\ e^{\text{i}m\theta_{d/2-1}}\end{pmatrix}\quad\Leftrightarrow\quad \boldsymbol{p}_m=\begin{pmatrix}\cos m\theta_0 \\ \sin m\theta_0 \\ \cos m\theta_1 \\ \sin m\theta_1 \\ \vdots \\ \cos m\theta_{d/2-1} \\ \sin m\theta_{d/2-1}  \end{pmatrix}\end{equation}
$$

再取 $\theta_i = 10000^{-2i/d}$（该形式可以使得随着|m−n|的增大，⟨pm,pn⟩有着趋于零的趋势，这一点可以通过对位置编码做积分来证明，而 base 取为 10000 是实验结果），就得到了上文的编码方式。

当 $H$ 不是一个单位矩阵时，因为模型的 Embedding 层所形成的 d 维向量之间任意两个维度的相关性比较小，满足一定的解耦性，我们可以将其视作对角矩阵，那么使用上述编码：

$$
\begin{equation}\boldsymbol{p}_m^{\top} \boldsymbol{\mathcal{H}} \boldsymbol{p}_n=\sum_{i=1}^{d/2} \boldsymbol{\mathcal{H}}_{2i,2i} \cos m\theta_i \cos n\theta_i + \boldsymbol{\mathcal{H}}_{2i+1,2i+1} \sin m\theta_i \sin n\theta_i\end{equation}
$$

通过积化和差：

$$
\begin{equation}\sum_{i=1}^{d/2} \frac{1}{2}\left(\boldsymbol{\mathcal{H}}_{2i,2i} + \boldsymbol{\mathcal{H}}_{2i+1,2i+1}\right) \cos (m-n)\theta_i + \frac{1}{2}\left(\boldsymbol{\mathcal{H}}_{2i,2i} - \boldsymbol{\mathcal{H}}_{2i+1,2i+1}\right) \cos (m+n)\theta_i \end{equation}
$$

说明该编码仍然可以表示相对位置。

上述​编码结果，如图2.6所示：


![图2.6 编码结果](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/2-figures/3-0.png)
图2.6 编码结果



基于上述原理，我们实现一个​位置编码层：

```python

class PositionalEncoding(nn.Module):
    '''位置编码模块'''

    def __init__(self, args):
        super(PositionalEncoding, self).__init__()
        # Dropout 层
        # self.dropout = nn.Dropout(p=args.dropout)

        # block size 是序列的最大长度
        pe = torch.zeros(args.block_size, args.n_embd)
        position = torch.arange(0, args.block_size).unsqueeze(1)
        # 计算 theta
        div_term = torch.exp(
            torch.arange(0, args.n_embd, 2) * -(math.log(10000.0) / args.n_embd)
        )
        # 分别计算 sin、cos 结果
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer("pe", pe)

    def forward(self, x):
        # 将位置编码加到 Embedding 结果上
        x = x + self.pe[:, : x.size(1)].requires_grad_(False)
        return x
```

##### 2.3.3 一个完整的 Transformer

上述所有组件，再按照下图的 Tranfromer 结构拼接起来就是一个完整的 Transformer 模型了，如图2.7所示：


![图2.7 Transformer 模型结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/2-figures/3-1.png)
图2.7 Transformer 模型结构


但需要注意的是，上图是原论文《Attention is all you need》配图，LayerNorm 层放在了 Attention 层后面，也就是“Post-Norm”结构，但在其发布的源代码中，LayerNorm 层是放在 Attention 层前面的，也就是“Pre Norm”结构。考虑到目前 LLM 一般采用“Pre-Norm”结构（可以使 loss 更稳定），本文在实现时采用“Pre-Norm”结构。

如图，经过 tokenizer 映射后的输出先经过 Embedding 层和 Positional Embedding 层编码，然后进入上一节讲过的 N 个 Encoder 和 N 个 Decoder（在 Transformer 原模型中，N 取为6），最后经过一个线性层和一个 Softmax 层就得到了最终输出。

基于之前所实现过的组件，我们实现完整的 Transformer 模型：

```python
class Transformer(nn.Module):
   '''整体模型'''
    def __init__(self, args):
        super().__init__()
        # 必须输入词表大小和 block size
        assert args.vocab_size is not None
        assert args.block_size is not None
        self.args = args
        self.transformer = nn.ModuleDict(dict(
            wte = nn.Embedding(args.vocab_size, args.n_embd),
            wpe = PositionalEncoding(args),
            drop = nn.Dropout(args.dropout),
            encoder = Encoder(args),
            decoder = Decoder(args),
        ))
        # 最后的线性层，输入是 n_embd，输出是词表大小
        self.lm_head = nn.Linear(args.n_embd, args.vocab_size, bias=False)

        # 初始化所有的权重
        self.apply(self._init_weights)

        # 查看所有参数的数量
        print("number of parameters: %.2fM" % (self.get_num_params()/1e6,))

    '''统计所有参数的数量'''
    def get_num_params(self, non_embedding=False):
        # non_embedding: 是否统计 embedding 的参数
        n_params = sum(p.numel() for p in self.parameters())
        # 如果不统计 embedding 的参数，就减去
        if non_embedding:
            n_params -= self.transformer.wte.weight.numel()
        return n_params

    '''初始化权重'''
    def _init_weights(self, module):
        # 线性层和 Embedding 层初始化为正则分布
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

    '''前向计算函数'''
    def forward(self, idx, targets=None):
        # 输入为 idx，维度为 (batch size, sequence length, 1)；targets 为目标序列，用于计算 loss
        device = idx.device
        b, t = idx.size()
        assert t <= self.args.block_size, f"不能计算该序列，该序列长度为 {t}, 最大序列长度只有 {self.args.block_size}"

        # 通过 self.transformer
        # 首先将输入 idx 通过 Embedding 层，得到维度为 (batch size, sequence length, n_embd)
        print("idx",idx.size())
        # 通过 Embedding 层
        tok_emb = self.transformer.wte(idx)
        print("tok_emb",tok_emb.size())
        # 然后通过位置编码
        pos_emb = self.transformer.wpe(tok_emb)
        # 再进行 Dropout
        x = self.transformer.drop(pos_emb)
        # 然后通过 Encoder
        print("x after wpe:",x.size())
        enc_out = self.transformer.encoder(x)
        print("enc_out:",enc_out.size())
        # 再通过 Decoder
        x = self.transformer.decoder(x, enc_out)
        print("x after decoder:",x.size())

        if targets is not None:
            # 训练阶段，如果我们给了 targets，就计算 loss
            # 先通过最后的 Linear 层，得到维度为 (batch size, sequence length, vocab size)
            logits = self.lm_head(x)
            # 再跟 targets 计算交叉熵
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-1)
        else:
            # 推理阶段，我们只需要 logits，loss 为 None
            # 取 -1 是只取序列中的最后一个作为输出
            logits = self.lm_head(x[:, [-1], :]) # note: using list [-1] to preserve the time dim
            loss = None

        return logits, loss
```

注意，上述代码除去搭建了整个 Transformer 结构外，我们还额外实现了三个函数：

- get_num_params：用于统计模型的参数量
- _init_weights：用于对模型所有参数进行随机初始化
- forward：前向计算函数

另外，在前向计算函数中，我们对模型使用 pytorch 的交叉熵函数来计算损失，对于不同的损失函数，读者可以查阅 Pytorch 的官方文档，此处就不再赘述了。

经过上述步骤，我们就可以从零“手搓”一个完整的、可计算的 Transformer 模型。限于本书主要聚焦在 LLM，在本章，我们就不再详细讲述如何训练 Transformer 模型了；在后文中，我们将类似地从零“手搓”一个 LLaMA 模型，并手把手带大家训练一个属于自己的 Tiny LLaMA。

**参考文献**

[1] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin. (2023). *Attention Is All You Need.* arXiv preprint arXiv:1706.03762.

[2] Jay Mody 的文章 “An Intuition for Attention”. 来源：https://jaykmody.com/blog/attention-intuition/

### 第三章 预训练语言模型

#### 3.1 Encoder-only PLM

在上一章，我们详细讲解了给 NLP 领域带来巨大变革注意力机制以及使用注意力机制搭建的模型 Transformer，NLP 模型的里程碑式转变也就自此而始。在上文对 Transformer 的讲解中我们可以看到，Transformer 结构主要由 Encoder、Decoder 两个部分组成，两个部分分别具有不一样的结构和输入输出。

针对 Encoder、Decoder 的特点，引入 ELMo 的预训练思路，开始出现不同的、对 Transformer 进行优化的思路。例如，Google 仅选择了 Encoder 层，通过将 Encoder 层进行堆叠，再提出不同的预训练任务-掩码语言模型（Masked Language Model，MLM），打造了一统自然语言理解（Natural Language Understanding，NLU）任务的代表模型——BERT。而 OpenAI 则选择了 Decoder 层，使用原有的语言模型（Language Model，LM）任务，通过不断增加模型参数和预训练语料，打造了在 NLG（Natural Language Generation，自然语言生成）任务上优势明显的 GPT 系列模型，也是现今大火的 LLM 的基座模型。当然，还有一种思路是同时保留 Encoder 与 Decoder，打造预训练的 Transformer 模型，例如由 Google 发布的 T5模型。

在本章中，我们将以 Encoder-Only、Encoder-Decoder、Decoder-Only 的顺序来依次介绍 Transformer 时代的各个主流预训练模型，分别介绍三种核心的模型架构、每种主流模型选择的预训练任务及其独特优势，这也是目前所有主流 LLM 的模型基础。

##### 3.1.1 BERT

BERT，全名为 Bidirectional Encoder Representations from Transformers，是由 Google 团队在 2018年发布的预训练语言模型。该模型发布于论文《BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding》，实现了包括 GLUE、MultiNLI 等七个自然语言处理评测任务的最优性能（State Of The Art，SOTA），堪称里程碑式的成果。自 BERT 推出以来，预训练+微调的模式开始成为自然语言处理任务的主流，不仅 BERT 自身在不断更新迭代提升模型性能，也出现了如 MacBERT、BART 等基于 BERT 进行优化提升的模型。可以说，BERT 是自然语言处理的一个阶段性成果，标志着各种自然语言处理任务的重大进展以及预训练模型的统治地位建立，一直到 LLM 的诞生，NLP 领域的主导地位才从 BERT 系模型进行迁移。即使在 LLM 时代，要深入理解 LLM 与 NLP，BERT 也是无法绕过的一环。

###### （1）思想沿承

BERT 是一个统一了多种思想的预训练模型。其所沿承的核心思想包括：

- Transformer 架构。正如我们在上一章所介绍的，在 2017年发表的《Attention is All You Need》论文提出了完全使用 注意力机制而抛弃 RNN、LSTM 结构的 Transformer 模型，带来了新的模型架构。BERT 正沿承了 Transformer 的思想，在 Transformer 的模型基座上进行优化，通过将 Encoder 结构进行堆叠，扩大模型参数，打造了在 NLU 任务上独居天分的模型架构；
- 预训练+微调范式。同样在 2018年，ELMo 的诞生标志着预训练+微调范式的诞生。ELMo 模型基于双向 LSTM 架构，在训练数据上基于语言模型进行预训练，再针对下游任务进行微调，表现出了更加优越的性能，将 NLP 领域导向预训练+微调的研究思路。而 BERT 也采用了该范式，并通过将模型架构调整为 Transformer，引入更适合文本理解、能捕捉深层双向语义关系的预训练任务 MLM，将预训练-微调范式推向了高潮。

接下来，我们将从模型架构、预训练任务以及下游任务微调三个方面深入剖析 BERT，分析 BERT 的核心思路及优势，帮助大家理解 BERT 为何能够具备远超之前模型的性能，也从而更加深刻地理解 LLM 如何能够战胜 BERT 揭开新时代的大幕。

###### （2）模型架构——Encoder Only

BERT 的模型架构是取了 Transformer 的 Encoder 部分堆叠而成，其主要结构如图3.1所示：


![图3.1 BERT 模型结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/1-0.png)
图3.1 BERT 模型结构


BERT 是针对于 NLU 任务打造的预训练模型，其输入一般是文本序列，而输出一般是 Label，例如情感分类的积极、消极 Label。但是，正如 Transformer 是一个 Seq2Seq 模型，使用 Encoder 堆叠而成的 BERT 本质上也是一个 Seq2Seq 模型，只是没有加入对特定任务的 Decoder，因此，为适配各种 NLU 任务，在模型的最顶层加入了一个分类头 prediction_heads，用于将多维度的隐藏状态通过线性层转换到分类维度（例如，如果一共有两个类别，prediction_heads 输出的就是两维向量）。

模型整体既是由 Embedding、Encoder 加上 prediction_heads 组成：


![图3.2 BERT 模型简略结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/1-1.png)
图3.2 BERT 模型简略结构


输入的文本序列会首先通过 tokenizer（分词器） 转化成 input_ids（基本每一个模型在 tokenizer 的操作都类似，可以参考 Transformer 的 tokenizer 机制，后文不再赘述），然后进入 Embedding 层转化为特定维度的 hidden_states，再经过 Encoder 块。Encoder 块中是堆叠起来的 N 层 Encoder Layer，BERT 有两种规模的模型，分别是 base 版本（12层 Encoder Layer，768 的隐藏层维度，总参数量 110M），large 版本（24层 Encoder Layer，1024 的隐藏层维度，总参数量 340M）。通过Encoder 编码之后的最顶层 hidden_states 最后经过 prediction_heads 就得到了最后的类别概率，经过 Softmax 计算就可以计算出模型预测的类别。


> BERT 采用 WordPiece 作为分词方法。WordPiece 是一种基于统计的子词切分算法，其核心在于将单词拆解为子词（例如，"playing" -> ["play", "##ing"]）。其合并操作的依据是最大化语言模型的似然度。对于中文等非空格分隔的语言，通常将单个汉字作为原子分词单位（token）处理。

prediction_heads 其实就是线性层加上激活函数，一般而言，最后一个线性层的输出维度和任务的类别数相等，如图3.3所示：


![图3.3 prediction_heads 结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/1-5.png)
图3.3 prediction_heads 结构


而每一层 Encoder Layer 都是和 Transformer 中的 Encoder Layer 结构类似的层，如图3.4所示：


![图3.4 Encoder Layer 结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/1-2.png)
图3.4 Encoder Layer 结构


如图3.5所示，已经通过 Embedding 层映射的 hidden_states 进入核心的 attention 机制，然后通过残差连接的机制和原输入相加，再经过一层 Intermediate 层得到最终输出。Intermediate 层是 BERT 的特殊称呼，其实就是一个线性层加上激活函数：


![图3.5 Intermediate 结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/1-3.png)
图3.5 Intermediate 结构


注意，BERT 所使用的激活函数是 GELU 函数，全名为高斯误差线性单元激活函数，这也是自 BERT 才开始被普遍关注的激活函数。GELU 的计算方式为：

$$GELU(x) = 0.5x(1 + tanh(\sqrt{\frac{2}{\pi}})(x + 0.044715x^3))$$

GELU 的核心思路为将随机正则的思想引入激活函数，通过输入自身的概率分布，来决定抛弃还是保留自身的神经元。关于 GELU 的原理与核心思路，此处不再赘述，有兴趣的读者可以自行学习。

BERT 的 注意力机制和 Transformer 中 Encoder 的 自注意力机制几乎完全一致，但是 BERT 将相对位置编码融合在了注意力机制中，将相对位置编码同样视为可训练的权重参数，如图3.6所示：


![图3.6 BERT 注意力机制结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/1-4.png)
图3.6 BERT 注意力机制结构


如图，BERT 的注意力计算过程和 Transformer 的唯一差异在于，在完成注意力分数的计算之后，先通过 Position Embedding 层来融入相对位置信息。这里的 Position Embedding 层，其实就是一层线性矩阵。通过可训练的参数来拟合相对位置，相对而言比 Transformer 使用的绝对位置编码 Sinusoidal 能够拟合更丰富的相对位置信息，但是，这样也增加了不少模型参数，同时完全无法处理超过模型训练长度的输入（例如，对 BERT 而言能处理的最大上下文长度是 512 个 token）。

注：原始 BERT（即论文提出）使用和 Transformer 一致的绝对位置编码，后续改进（包括 BERT 的各种变体）使用了上述相对位置编码，为帮助读者了解更全面的模型结构设计，此处选择了改进版 BERT。

可以看出，BERT 的模型架构既是建立在 Transformer 的 Encoder 之上的，这也是为什么说 BERT 沿承了 Transformer 的思想。

###### （3）预训练任务——MLM + NSP

相较于基本沿承 Transformer 的模型架构，BERT 更大的创新点在于其提出的两个新的预训练任务上——MLM 和 NSP（Next Sentence Prediction，下一句预测）。预训练-微调范式的核心优势在于，通过将预训练和微调分离，完成一次预训练的模型可以仅通过微调应用在几乎所有下游任务上，只要微调的成本较低，即使预训练成本是之前的数倍甚至数十倍，模型仍然有更大的应用价值。因此，可以进一步扩大模型参数和预训练数据量，使用海量的预训练语料来让模型拟合潜在语义与底层知识，从而让模型通过长时间、大规模的预训练获得强大的语言理解和生成能力。

因此，预训练数据的核心要求即是需要极大的数据规模（数亿 token）。毫无疑问，通过人工标注产出的全监督数据很难达到这个规模。因此，预训练数据一定是从无监督的语料中获取。这也是为什么传统的预训练任务都是 LM 的原因——LM 使用上文预测下文的方式可以直接应用到任何文本中，对于任意文本，我们只需要将下文遮蔽将上文输入模型要求其预测就可以实现 LM 训练，因此互联网上所有文本语料都可以被用于预训练。

但是，LM 预训练任务的一大缺陷在于，其直接拟合从左到右的语义关系，但忽略了双向的语义关系。虽然 Transformer 中通过位置编码表征了文本序列中的位置信息，但这和直接拟合双向语义关系还是有本质区别。例如，BiLSTM（双向 LSTM 模型）在语义表征上就往往优于 LSTM 模型，就是因为 BiLSTM 通过双向的 LSTM 拟合了双向语义关系。因此，有没有一种预训练任务，能够既利用海量无监督语料，又能够训练模型拟合双向语义关系的能力？

基于这一思想，Jacob 等学者提出了 MLM，也就是掩码语言模型作为新的预训练任务。相较于模拟人类写作的 LM，MLM 模拟的是“完形填空”。MLM 的思路也很简单，在一个文本序列中随机遮蔽部分 token，然后将所有未被遮蔽的 token 输入模型，要求模型根据输入预测被遮蔽的 token。例如，输入和输出可以是：

    输入：I <MASK> you because you are <MASK>
    输出：<MASK> - love; <MASK> - wonderful

由于模型可以利用被遮蔽的 token 的上文和下文一起理解语义来预测被遮蔽的 token，因此通过这样的任务，模型可以拟合双向语义，也就能够更好地实现文本的理解。同样，MLM 任务无需对文本进行任何人为的标注，只需要对文本进行随机遮蔽即可，因此也可以利用互联网所有文本语料实现预训练。例如，BERT 的预训练就使用了足足 3300M 单词的语料。

不过，MLM 也存在其固有缺陷。LM 任务模拟了人自然创作的过程，其训练和下游任务是完全一致的，也就是说，训练时是根据上文预测下文，下游任务微调和推理时也同样如此。但是 MLM 不同，在下游任务微调和推理时，其实是不存在我们人工加入的 `<MASK>` 的，我们会直接通过原文本得到对应的隐藏状态再根据下游任务进入分类器或其他组件。预训练和微调的不一致，会极大程度影响模型在下游任务微调的性能。针对这一问题，作者对 MLM 的策略进行了改进。

在具体进行 MLM 训练时，会随机选择训练语料中 15% 的 token 用于遮蔽。但是这 15% 的 token 并非全部被遮蔽为 `<MASK>`，而是有 80% 的概率被遮蔽，10% 的概率被替换为任意一个 token，还有 10% 的概率保持不变。其中 10% 保持不变就是为了消除预训练和微调的不一致，而 10% 的随机替换核心意义在于迫使模型保持对上下文信息的学习。因为如果全部遮蔽的话，模型仅需要处理被遮蔽的位置，从而仅学习要预测的 token 而丢失了对上下文的学习。通过引入部分随机 token，模型无法确定需要预测的 token，从而被迫保持每一个 token 的上下文表征分布，从而具备了对句子的特征表示能力。且由于随机 token 的概率很低，其并不会影响模型实质的语言理解能力。

除去 MLM，BERT 还提出了另外一个预训练任务——NSP，即下一个句子预测。NSP 的核心思想是针对句级的 NLU 任务，例如问答匹配、自然语言推理等。问答匹配是指，输入一个问题和若干个回答，要求模型找出问题的真正回答；自然语言推理是指，输入一个前提和一个推理，判断推理是否是符合前提的。这样的任务都需要模型在句级去拟合关系，判断两个句子之间的关系，而不仅是 MLM 在 token 级拟合的语义关系。因此，BERT 提出了 NSP 任务来训练模型在句级的语义关系拟合。

NSP 任务的核心思路是要求模型判断一个句对的两个句子是否是连续的上下文。例如，输入和输入可以是：

    输入：
        Sentence A：I love you.
        Sentence B: Because you are wonderful.
    输出：
        1（是连续上下文）

    输入：
        Sentence A：I love you.
        Sentence B: Because today's dinner is so nice.
    输出：
        0（不是连续上下文）

通过要求模型判断句对关系，从而迫使模型拟合句子之间的关系，来适配句级的 NLU 任务。同样，由于 NSP 的正样本可以从无监督语料中随机抽取任意连续的句子，而负样本可以对句子打乱后随机抽取（只需要保证不要抽取到原本就连续的句子就行），因此也可以具有几乎无限量的训练数据。

在具体预训练时，BERT 使用了 800M 的 BooksCorpus 语料和 2500M 的英文维基百科语料，90% 的数据使用 128 的上下文长度训练，剩余 10% 的数据使用 512 作为上下文长度进行预训练，总共约训练了 3.3B token。其训练的超参数也是值得关注的，BERT 的训练语料共有 13GB 大小，其在 256 的 batch size 上训练了 1M 步（40 个 Epoch）。而相较而言，LLM 一般都只会训练一个 Epoch，且使用远大于 256 的 batch size。

可以看到，相比于传统的非预训练模型，其训练的数据量有指数级增长。当然，更海量的训练数据需要更大成本的算力，BERT 的 Base 版本和 Large 版本分别使用了 16块 TPU 和 64块 TPU 训练了 4天才完成。

###### （4）下游任务微调

作为 NLP 领域里程碑式的成果，BERT 的一个重大意义就是正式确立了预训练-微调的两阶段思想，即在海量无监督语料上进行预训练来获得通用的文本理解与生成能力，再在对应的下游任务上进行微调。该种思想的一个重点在于，预训练得到的强大能力能否通过低成本的微调快速迁移到对应的下游任务上。

针对这一点，BERT 设计了更通用的输入和输出层来适配多任务下的迁移学习。对每一个输入的文本序列，BERT 会在其首部加入一个特殊 token `<CLS>`。在后续编码中，该 token 代表的即是整句的状态，也就是句级的语义表征。在进行 NSP 预训练时，就使用了该 token 对应的特征向量来作为最后分类器的输入。

在完成预训练后，针对每一个下游任务，只需要使用一定量的全监督人工标注数据，对预训练的 BERT 在该任务上进行微调即可。所谓微调，其实和训练时更新模型参数的策略一致，只不过在特定的任务、更少的训练数据、更小的 batch_size 上进行训练，更新参数的幅度更小。对于绝大部分下游任务，都可以直接使用 BERT 的输出。例如，对于文本分类任务，可以直接修改模型结构中的 prediction_heads 最后的分类头即可。对于序列标注等任务，可以集成 BERT 多层的隐含层向量再输出最后的标注结果。对于文本生成任务，也同样可以取 Encoder 的输出直接解码得到最终生成结果。因此，BERT 可以非常高效地应用于多种 NLP 任务。

BERT 一经提出，直接在 NLP 11个赛道上取得 SOTA 效果，成为 NLU 方向上当之无愧的霸主，后续若干在 NLU 任务上取得更好效果的模型都是在 BERT 基础上改进得到的。直至 LLM 时代，BERT 也仍然能在很多标注数据丰富的 NLU 任务上达到最优效果，事实上，对于某些特定、训练数据丰富且强调高吞吐的任务，BERT 比 LLM 更具有可用性。

##### 3.1.2 RoBERTa

BERT 作为 NLP 划时代的杰作，同时在多个榜单上取得 SOTA 效果，也带动整个 NLP 领域向预训练模型方向迁移。以 BERT 为基础，在多个方向上进行优化，还涌现了一大批效果优异的 Encoder-Only 预训练模型。它们大都有和 BERT 类似或完全一致的模型结构，在训练数据、预训练任务、训练参数等方面上进行了优化，以取得能力更强大、在下游任务上表现更亮眼的预训练模型。其中之一即是同样由 Facebook 发布的 RoBERTa。

前面我们说过，预训练-微调的一个核心优势在于可以使用远大于之前训练数据的海量无监督语料进行预训练。因为在传统的深度学习范式中，对每一个任务，我们需要从零训练一个模型，那么就无法使用太大的模型参数，否则需要极大规模的有监督数据才能让模型较好地拟合，成本太大。但在预训练-微调范式，我们在预训练阶段可以使用尽可能大量的训练数据，只需要一次预训练好的模型，后续在每一个下游任务上通过少量有监督数据微调即可。而 BERT 就使用了 13GB（3.3B token）的数据进行预训练，这相较于传统 NLP 来说是一个极其巨大的数据规模了。

但是，13GB 的预训练数据是否让 BERT 达到了充分的拟合呢？如果我们使用更多预训练语料，是否可以进一步增强模型性能？更多的，BERT 所选用的预训练任务、训练超参数是否是最优的？RoBERTa 应运而生。

###### （1）优化一：去掉 NSP 预训练任务

RoBERTa 的模型架构与 BERT 完全一致，也就是使用了 BERT-large（24层 Encoder Layer，1024 的隐藏层维度，总参数量 340M）的模型参数。在预训练任务上，有学者质疑 NSP 任务并不能提高模型性能，因为其太过简单，加入到预训练中并不能使下游任务微调时明显受益，甚至会带来负面效果。RoBERTa 设置了四个实验组：

    1. 段落构建的 MLM + NSP：BERT 原始预训练任务，输入是一对片段，每个片段包括多个句子，来构造 NSP 任务；
    2. 文档对构建的 MLM + NSP：一个输入构建一对句子，通过增大 batch 来和原始输入达到 token 等同；
    3. 跨越文档的 MLM：去掉 NSP 任务，一个输入为从一个或多个文档中连续采样的完整句子，为使输入达到最大长度（512），可能一个输入会包括多个文档；
    4. 单文档的 MLM：去掉 NSP 任务，且限制一个输入只能从一个文档中采样，同样通过增大 batch 来和原始输入达到 token 等同

实验结果证明，后两组显著优于前两组，且单文档的 MLM 组在下游任务上微调时性能最佳。因此，RoBERTa 在预训练中去掉了 NSP，只使用 MLM 任务。

同时，RoBERTa 对 MLM 任务本身也做出了改进。在 BERT 中，Mask 的操作是在数据处理的阶段完成的，因此后期预训练时同一个 sample 待预测的 `<MASK>` 总是一致的。由于 BERT 共训练了 40 个 Epoch，为使模型的训练数据更加广泛，BERT 将数据进行了四次随机 Mask，也就是每 10个 Epoch 模型训练的数据是完全一致的。而 RoBERTa 将 Mask 操作放到了训练阶段，也就是动态遮蔽策略，从而让每一个 Epoch 的训练数据 Mask 的位置都不一致。在实验中，动态遮蔽仅有很微弱的优势优于静态遮蔽，但由于动态遮蔽更高效、易于实现，后续 MLM 任务基本都使用了动态遮蔽。

###### （2）优化二：更大规模的预训练数据和预训练步长

RoBERTa 使用了更大量的无监督语料进行预训练，除去 BERT 所使用的 BookCorpus 和英文维基百科外，还使用了 CC-NEWS（CommonCrawl 数据集新闻领域的英文部分）、OPENWEBTEXT（英文网页）、STORIES（CommonCrawl 数据集故事风格子集），共计 160GB 的数据，十倍于 BERT。

同时，RoBERTa 认为更大的 batch size 既可以提高优化速度，也可以提高任务结束性能。因此，实验在 8K 的 batch size（对比 BERT 的 batch size 为 256）下训练 31K Step，也就是总训练 token 数和 BERT 一样是 3.3B 时，模型性能更好，从而证明了大 batch size 的意义。在此基础上，RoBERTa 一共训练了 500K Step（约合 66个 Epoch）。同时，RoBERTa 不再采用 BERT 在 256 长度上进行大部分训练再在 512 长度上完成训练的策略，而是全部在 512 长度上进行训练。

当然，更大的预训练数据、更长的序列长度和更多的训练 Epoch，需要预训练阶段更多的算力资源。训练一个 RoBERTa，Meta 使用了 1024 块 V100（32GB 显存）训练了一天。

###### （3）优化三：更大的 bpe 词表

与 BERT 使用的 WordPiece 算法不同，RoBERTa 使用了 BPE 作为 Tokenizer 的编码策略。BPE，即 Byte Pair Encoding，字节对编码，是指以子词对作为分词的单位。例如，对“Hello World”这句话，可能会切分为“Hel，lo，Wor，ld”四个子词对。而对于以字为基本单位的中文，一般会按照字节编码进行切分。例如，在 UTF-8 编码中，“我”会被编码为“E68891”，那么在 BPE 中可能就会切分成“E68”，“891”两个字词对。

一般来说，BPE 编码的词典越大，编码效果越好。当然，由于 Embedding 层就是把 token 从词典空间映射到隐藏空间（也就是说 Embedding 的形状为 (vocab_size, hidden_size)，越大的词表也会带来模型参数的增加。

BERT 原始的 BPE 词表大小为 30K，RoBERTa 选择了 50K 大小的词表来优化模型的编码能力。

通过上述三个部分的优化，RoBERTa 成功地在 BERT 架构的基础上刷新了多个下游任务的 SOTA，也一度成为 BERT 系模型最热门的预训练模型。同时，RoBERTa 的成功也证明了更大的预训练数据、更大的预训练步长的重要意义，这也是 LLM 诞生的基础之一。

##### 3.1.3 ALBERT

在 BERT 的基础上，RoBERTa 进一步探究了更大规模预训练的作用。同样是基于 BERT 架构进行优化的 ALBERT 模型，则从是否能够减小模型参数保持模型能力的角度展开了探究。通过对模型结构进行优化并对 NSP 预训练任务进行改进，ALBERT 成功地以更小规模的参数实现了超越 BERT 的能力。虽然 ALBERT 所提出的一些改进思想并没有在后续研究中被广泛采用，但其降低模型参数的方法及提出的新预训练任务 SOP 仍然对 NLP 领域提供了重要的参考意义。

###### （1）优化一：将 Embedding 参数进行分解

BERT 等预训练模型具有远超传统神经网络的参数量，如前所述，BERT-large 具有 24层 Encoder Layer，1024 的隐藏层维度，总共参数量达 340M。而这其中，Embedding 层的参数矩阵维度为 $V*H$，此处的 V 为词表大小 30K，H 即为隐藏层大小 1024，也就是 Embedding 层参数达到了 30M。而这样的设置还会带来一个更大的问题，即 Google 探索尝试搭建更宽（也就是隐藏层维度更大）的模型时发现，隐藏层维度的增加会带来 Embedding 层参数的巨大上升，如果把隐藏层维度增加到 2048，Embedding 层参数就会膨胀到 61M，这无疑是极大增加了模型的计算开销。

而从另一个角度看，Embedding 层输出的向量是我们对文本 token 的稠密向量表示，从 Word2Vec 的成功经验来看，这种词向量并不需要很大的维度，Word2Vec 仅使用了 100维大小就取得了很好的效果。因此，Embedding 层的输出也许不需要和隐藏层大小一致。

因此，ALBERT 对 Embedding 层的参数矩阵进行了分解，让 Embedding 层的输出维度和隐藏层维度解绑，也就是在 Embedding 层的后面加入一个线性矩阵进行维度变换。ALBERT 设置了 Embedding 层的输出为 128，因此在 Embedding 层后面加入了一个 $128*1024$ 的线性矩阵来将 Embedding 层的输出再升维到隐藏层大小。也就是说，Embedding 层的参数从 $V*H$ 降低到了 $V*E + E*H$，当 E 的大小远小于 H 时，该方法对 Embedding 层参数的优化就会很明显。

###### （2）优化二：跨层进行参数共享

通过对 BERT 的参数进行分析，ALBERT 发现各个 Encoder 层的参数出现高度一致的情况。由于 24个 Encoder 层带来了巨大的模型参数，因此，ALBERT 提出，可以让各个 Encoder 层共享模型参数，来减少模型的参数量。

在具体实现上，其实就是 ALBERT 仅初始化了一个 Encoder 层。在计算过程中，仍然会进行 24次计算，但是每一次计算都是经过这一个 Encoder 层。因此，虽然是 24个 Encoder 计算的模型，但只有一层 Encoder 参数，从而大大降低了模型参数量。在这样的情况下，就可以极大程度地扩大隐藏层维度，实现一个更宽但参数量更小的模型。ALBERT 通过实验证明，相较于 334M 的 BERT，同样是 24层 Encoder 但将隐藏层维度设为 2048 的 ALBERT（xlarge 版本）仅有 59M 的参数量，但在具体效果上还要更优于 BERT。

但是，上述优化虽然极大程度减小了模型参数量并且还提高了模型效果，却也存在着明显的不足。虽然 ALBERT 的参数量远小于 BERT，但训练效率却只略微优于 BERT，因为在模型的设置中，虽然各层共享权重，但计算时仍然要通过 24次 Encoder Layer 的计算，也就是说训练和推理时的速度相较 BERT 还会更慢。这也是 ALBERT 最终没能取代 BERT 的一个重要原因。

###### （3）优化三：提出 SOP 预训练任务

类似于 RoBERTa，ALBERT 也同样认为 NSP 任务过于简单，在预训练中无法对模型效果的提升带来显著影响。但是不同于 RoBERTa 选择直接去掉 NSP，ALBERT 选择改进 NSP，增加其难度，来优化模型的预训练。

在传统的 NSP 任务中，正例是由两个连续句子组成的句对，而负例则是从任意两篇文档中抽取出的句对，模型可以较容易地判断正负例，并不能很好地学习深度语义。而 SOP 任务提出的改进是，正例同样由两个连续句子组成，但负例是将这两个的顺序反过来。也就是说，模型不仅要拟合两个句子之间的关系，更要学习其顺序关系，这样就大大提升了预训练的难度。例如，相较于我们在上文中提出的 NSP 任务的示例，SOP 任务的示例形如：

    输入：
        Sentence A：I love you.
        Sentence B: Because you are wonderful.
    输出：
        1（正样本）

    输入：
        Sentence A：Because you are wonderful.
        Sentence B: I love you.
    输出：
        0（负样本）

ALBERT 通过实验证明，SOP 预训练任务对模型效果有显著提升。使用 MLM + SOP 预训练的模型效果优于仅使用 MLM 预训练的模型更优于使用 MLM + NSP 预训练的模型。

通过上述三点优化，ALBERT 成功地以更小的参数实现了更强的性能，虽然由于其架构带来的训练、推理效率降低限制了模型的进一步发展，但打造更宽的模型这一思路仍然为众多更强大的模型提供了参考价值。

作为预训练时代的 NLP 王者，BERT 及 BERT 系模型在多个 NLP 任务上扮演了极其重要的角色。除去上文介绍过的 RoBERTa、ALBERT 外，还有许多从其他更高角度对 BERT 进行优化的后起之秀，包括进一步改进了预训练任务的 ERNIE、对 BERT 进行蒸馏的小模型 DistilBERT、主打多语言任务的 XLM 等，本文就不再一一赘述。以 BERT 为代表的 Encoder-Only 架构并非 Transformer 的唯一变种，接下来，我们将介绍 Transformer 的另一种主流架构，与原始 Transformer 更相似、以 T5 为代表的 Encoder-Decoder 架构。

#### 3.2 Encoder-Decoder PLM

在上一节，我们学习了 Encoder-Only 结构的模型，主要介绍了 BERT 的模型架构、预训练任务和下游任务微调。BERT 是一个基于 Transformer 的 Encoder-Only 模型，通过预训练任务 MLM 和 NSP 来学习文本的双向语义关系，从而在下游任务中取得了优异的性能。但是，BERT 也存在一些问题，例如 MLM 任务和下游任务微调的不一致性，以及无法处理超过模型训练长度的输入等问题。为了解决这些问题，研究者们提出了 Encoder-Decoder 模型，通过引入 Decoder 部分来解决这些问题，同时也为 NLP 领域带来了新的思路和方法。

在本节中，我们将学习 Encoder-Decoder 结构的模型，主要介绍 T5 的模型架构和预训练任务，以及 T5 模型首次提出的 NLP 大一统思想。

##### 3.2.1 T5

T5（Text-To-Text Transfer Transformer）是由 Google 提出的一种预训练语言模型，通过将所有 NLP 任务统一表示为文本到文本的转换问题，大大简化了模型设计和任务处理。T5 基于 Transformer 架构，包含编码器和解码器两个部分，使用自注意力机制和多头注意力捕捉全局依赖关系，利用相对位置编码处理长序列中的位置信息，并在每层中包含前馈神经网络进一步处理特征。

T5 的大一统思想将不同的 NLP 任务如文本分类、问答、翻译等统一表示为输入文本到输出文本的转换，这种方法简化了模型设计、参数共享和训练过程，提高了模型的泛化能力和效率。通过这种统一处理方式，T5不仅减少了任务特定的模型调试工作，还能够使用相同的数据处理和训练框架，极大地提升了多任务学习的性能和应用的便捷性。接下来我们将会从模型结构、预训练任务和大一统思想三个方面来介绍 T5 模型。

###### （1）模型结构：Encoder-Decoder

BERT 采用了 Encoder-Only 结构，只包含编码器部分；而 GPT 采用了 Decoder-Only 结构，只包含解码器部分。T5 则采用了 Encoder-Decoder 结构，其中编码器和解码器都是基于 Transformer 架构设计。编码器用于处理输入文本，解码器用于生成输出文本。编码器和解码器之间通过注意力机制进行信息交互，从而实现输入文本到输出文本的转换。其主要结构如图3.7所示：


![图3.7 T5 模型详细结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/2-1.png)
图3.7 T5 模型详细结构


如图3.8所示，从整体来看 T5 的模型结构包括 Tokenizer 部分和 Transformer 部分。Tokenizer 部分主要负责将输入文本转换为模型可接受的输入格式，包括分词、编码等操作。Transformer 部分又分为 EncoderLayers 和 DecoderLayers 两部分，他们分别由一个个小的 Block组成，每个 Block 包含了多头注意力机制、前馈神经网络和 Norm 层。Block 的设计可以使模型更加灵活，像乐高一样可以根据任务的复杂程度和数据集的大小来调整 Block 的数量和层数。


![图3.8 T5 模型整体结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/2-2.png)
图3.8 T5 模型整体结构


T5 模型的 Encoder 和 Decoder 部分都是基于 Transformer 架构设计的，主要包括 Self-Attention 和前馈神经网络两种结构。Self-Attention 用于捕捉输入序列中的全局依赖关系，前馈神经网络用于处理特征的非线性变换。

和 Encoder 不一样的是，在 Decoder 中还包含了 Encoder-Decoder Attention 结构，用于捕捉输入和输出序列之间的依赖关系。这两种 Attention 结构几乎完全一致，只有在位置编码和 Mask 机制上有所不同。如图3.9所示，Encoder 和 Decoder 的结构如下：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/2-3.png)
图3.9 Encoder 和 Decoder


T5 的 Self-Attention 机制和 BERT 的 Attention 机制是一样的，都是基于 Self-Attention 机制设计的。Self-Attention 机制是一种全局依赖关系建模方法，通过计算 Query、Key 和 Value 之间的相似度来捕捉输入序列中的全局依赖关系。Encoder-Decoder Attention 仅仅在位置编码和 Mask 机制上有所不同，主要是为了区分输入和输出序列。如图3.10所示，Self-Attention 结构如下：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/2-4.png)
图3.10 Self-Attention 结构


与原始 Transformer 模型不同，T5 模型的LayerNorm 采用了 RMSNorm，通过计算每个神经元的均方根（Root Mean Square）来归一化每个隐藏层的激活值。RMSNorm 的参数设置与Layer Normalization 相比更简单，只有一个可学参数，可以更好地适应不同的任务和数据集。RMSNorm函数可以用以下数学公式表示：

$$
\text{RMSNorm}(x) = \frac{x}{\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2 + \epsilon}} \cdot \gamma
$$

其中：
- $x_i$ 是输入向量的第 $i$ 个元素
- $\gamma$ 是可学习的缩放参数
- $n$ 是输入向量的维度数量
- $\epsilon$ 是一个小常数，用于数值稳定性（以避免除以零的情况）

这种归一化有助于通过确保权重的规模不会变得过大或过小来稳定学习过程，这在具有许多层的深度学习模型中特别有用。

###### （2）预训练任务

T5 模型的预训练任务是一个关键的组成部分，它能使模型能够学习到丰富的语言表示，语言表示能力可以在后续的微调过程中被迁移到各种下游任务。训练所使用的数据集是一个大规模的文本数据集，包含了各种各样的文本数据，如维基百科、新闻、书籍等等。对数据经过细致的处理后，生成了用于训练的750GB 的数据集 C4，且已在 TensorflowData 中开源。

我们可以简单概括一下 T5 的预训练任务，主要包括以下几个部分：

- 预训练任务: T5模型的预训练任务是 MLM，也称为BERT-style目标。具体来说，就是在输入文本中随机遮蔽15%的token，然后让模型预测这些被遮蔽的token。这个过程不需要标签，可以在大量未标注的文本上进行。
- 输入格式: 预训练时，T5将输入文本转换为"文本到文本"的格式。对于一个给定的文本序列，随机选择一些token进行遮蔽，并用特殊的占位符(token)替换。然后将被遮蔽的token序列作为模型的输出目标。
- 预训练数据集: T5 使用了自己创建的大规模数据集"Colossal Clean Crawled Corpus"(C4)，该数据集从Common Crawl中提取了大量干净的英语文本。C4数据集经过了一定的清洗，去除了无意义的文本、重复文本等。
- 多任务预训练: T5 还尝试了将多个任务混合在一起进行预训练，而不仅仅是单独的MLM任务。这有助于模型学习更通用的语言表示。
- 预训练到微调的转换: 预训练完成后，T5模型会在下游任务上进行微调。微调时，模型在任务特定的数据集上进行训练，并根据任务调整解码策略。

通过大规模预训练，T5模型能够学习到丰富的语言知识，并获得强大的语言表示能力，在多个NLP任务上取得了优异的性能，预训练是T5成功的关键因素之一。

###### （3）大一统思想

T5模型的一个核心理念是“大一统思想”，即所有的 NLP 任务都可以统一为文本到文本的任务，这一思想在自然语言处理领域具有深远的影响。其设计理念是将所有不同类型的NLP任务（如文本分类、翻译、文本生成、问答等）转换为一个统一的格式：输入和输出都是纯文本。

例如：
- 对于文本分类任务，输入可以是“classify: 这是一个很好的产品”，输出是“正面”；
- 对于翻译任务，输入可以是“translate English to French: How are you?”, 输出是“Comment ça va?”。

T5通过大规模的文本数据进行预训练，然后在具体任务上进行微调。这一过程与BERT、GPT等模型类似，但T5将预训练和微调阶段的任务统一为文本到文本的形式，使其在各种任务上的适应性更强。

我们可以通过图3.11，更加直观地理解 T5 的大一统思想：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/2-0.png)
图3.11 T5 的大一统思想


对于不同的NLP任务，每次输入前都会加上一个任务描述前缀，明确指定当前任务的类型。这不仅帮助模型在预训练阶段学习到不同任务之间的通用特征，也便于在微调阶段迅速适应具体任务。例如，任务前缀可以是“summarize: ”用于摘要任务，或“translate English to German: ”用于翻译任务。

T5的大一统思想通过将所有NLP任务统一为文本到文本的形式，简化了任务处理流程，增强了模型的通用性和适应性。这一思想不仅推动了自然语言处理技术的发展，也为实际应用提供了更为便捷和高效的解决方案。

#### 3.3 Decoder-Only PLM

在前两节中，我们分别讲解了由 Transformer 发展而来的两种模型架构——以 BERT 为代表的 Encoder-Only 模型和以 T5 为代表的 Encoder-Decoder 模型。那么，很自然可以想见，除了上述两种架构，还可以有一种模型架构——Decoder-Only，即只使用 Decoder 堆叠而成的模型。

事实上，Decoder-Only 就是目前大火的 LLM 的基础架构，目前所有的 LLM 基本都是 Decoder-Only 模型（RWKV、Mamba 等非 Transformer 架构除外）。而引发 LLM 热潮的 ChatGPT，正是 Decoder-Only 系列的代表模型 GPT 系列模型的大成之作。而目前作为开源 LLM 基本架构的 LLaMA 模型，也正是在 GPT 的模型架构基础上优化发展而来。因此，在本节中，我们不但会详细分析 Decoder-Only 代表模型 GPT 的原理、架构和特点，还会深入到目前的主流开源 LLM，分析它们的结构、特点，结合之前对 Transformer 系列其他模型的分析，帮助大家深入理解当下被寄予厚望、被认为是 AGI 必经之路的 LLM 是如何一步步从传统 PLM 中发展而来的。

首先，让我们学习打开 LLM 世界大门的代表模型——由 OpenAI 发布的 GPT。

##### 3.3.1 GPT

GPT，即 Generative Pre-Training Language Model，是由 OpenAI 团队于 2018年发布的预训练语言模型。虽然学界普遍认可 BERT 作为预训练语言模型时代的代表，但首先明确提出预训练-微调思想的模型其实是 GPT。GPT 提出了通用预训练的概念，也就是在海量无监督语料上预训练，进而在每个特定任务上进行微调，从而实现这些任务的巨大收益。虽然在发布之初，由于性能略输于不久后发布的 BERT，没能取得轰动性成果，也没能让 GPT 所使用的 Decoder-Only 架构成为学界研究的主流，但 OpenAI 团队坚定地选择了不断扩大预训练数据、增加模型参数，在 GPT 架构上不断优化，最终在 2020年发布的 GPT-3 成就了 LLM 时代的基础，并以 GPT-3 为基座模型的 ChatGPT 成功打开新时代的大门，成为 LLM 时代的最强竞争者也是目前的最大赢家。

本节将以 GPT 为例，分别从模型架构、预训练任务、GPT 系列模型的发展历程等三个方面深入分析 GPT 及其代表的 Decoder-Only 模型，并进一步引出当前的主流 LLM 架构——LLaMA。

###### （1） 模型架构——Decoder Only


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/3-0.png)
图3.12 GPT 模型结构


如图3.12可以看到，GPT 的整体结构和 BERT 是有一些类似的，只是相较于 BERT 的 Encoder，选择使用了 Decoder 来进行模型结构的堆叠。由于 Decoder-Only 结构也天生适用于文本生成任务，所以相较于更贴合 NLU 任务设计的 BERT，GPT 和 T5 的模型设计更契合于 NLG 任务和 Seq2Seq 任务。同样，对于一个自然语言文本的输入，先通过 tokenizer 进行分词并转化为对应词典序号的 input_ids。

输入的 input_ids 首先通过 Embedding 层，再经过 Positional Embedding 进行位置编码。不同于 BERT 选择了可训练的全连接层作为位置编码，GPT 沿用了 Transformer 的经典 Sinusoidal 位置编码，即通过三角函数进行绝对位置编码，此处就不再赘述，感兴趣的读者可以参考第二章 Transformer 模型细节的解析。

通过 Embedding 层和 Positional Embedding 层编码成 hidden_states 之后，就可以进入到解码器（Decoder），第一代 GPT 模型和原始 Transformer 模型类似，选择了 12层解码器层，但是在解码器层的内部，相较于 Transformer 原始 Decoder 层的双注意力层设计，GPT 的 Decoder 层反而更像 Encoder 层一点。由于不再有 Encoder 的编码输入，Decoder 层仅保留了一个带掩码的注意力层，并且将 LayerNorm 层从 Transformer 的注意力层之后提到了注意力层之前。hidden_states 输入 Decoder 层之后，会先进行 LayerNorm，再进行掩码注意力计算，然后经过残差连接和再一次 LayerNorm 进入到 MLP 中并得到最后输出。

由于不存在 Encoder 的编码结果，Decoder 层中的掩码注意力也是自注意力计算。也就是对一个输入的 hidden_states，会通过三个参数矩阵来生成 query、key 和 value，而不再是像 Transformer 中的 Decoder 那样由 Encoder 输出作为 key 和 value。后续的注意力计算过程则和 BERT 类似，只是在计算得到注意力权重之后，通过掩码矩阵来遮蔽了未来 token 的注意力权重，从而限制每一个 token 只能关注到它之前 token 的注意力，来实现掩码自注意力的计算。

另外一个结构上的区别在于，GPT 的 MLP 层没有选择线性矩阵来进行特征提取，而是选择了两个一维卷积核来提取，不过，从效果上说这两者是没有太大区别的。通过 N 个 Decoder 层后的 hidden_states 最后经过线性矩阵映射到词表维度，就可以转化成自然语言的 token，从而生成我们的目标序列。

###### （2）预训练任务——CLM

Decoder-Only 的模型结构往往更适合于文本生成任务，因此，Decoder-Only 模型往往选择了最传统也最直接的预训练任务——因果语言模型，Causal Language Model，下简称 CLM。

CLM 可以看作 N-gram 语言模型的一个直接扩展。N-gram 语言模型是基于前 N 个 token 来预测下一个 token，CLM 则是基于一个自然语言序列的前面所有 token 来预测下一个 token，通过不断重复该过程来实现目标文本序列的生成。也就是说，CLM 是一个经典的补全形式。例如，CLM 的输入和输出可以是：

    input: 今天天气
    output: 今天天气很

    input: 今天天气很
    output：今天天气很好

因此，对于一个输入目标序列长度为 256，期待输出序列长度为 256 的任务，模型会不断根据前 256 个 token、257个 token（输入+预测出来的第一个 token）...... 进行 256 次计算，最后生成一个序列长度为 512 的输出文本，这个输出文本前 256 个 token 为输入，后 256 个 token 就是我们期待的模型输出。

在前面我们说过，BERT 之所以可以采用预训练+微调的范式取得重大突破，正是因为其选择的 MLM、NSP 可以在海量无监督语料上直接训练——而很明显，CLM 是更直接的预训练任务，其天生和人类书写自然语言文本的习惯相契合，也和下游任务直接匹配，相对于 MLM 任务更加直接，可以在任何自然语言文本上直接应用。因此，CLM 也可以使用海量的自然语言语料进行大规模的预训练。

###### （3）GPT 系列模型的发展

自 GPT-1 推出开始，OpenAI 一直坚信 Decoder-Only 的模型结构和“体量即正义”的优化思路，不断扩大预训练数据集、模型体量并对模型做出一些小的优化和修正，来不断探索更强大的预训练模型。从被 BERT 压制的 GPT-1，到没有引起足够关注的 GPT-2，再到激发了涌现能力、带来大模型时代的 GPT-3，最后带来了跨时代的 ChatGPT，OpenAI 通过数十年的努力证明了其思路的正确性。

下表总结了从 GPT-1 到 GPT-3 的模型结构、预训练语料大小的变化：

模型 | Decoder Layer | Hidden_size | 注意力头数 | 注意力维度 | 总参数量 | 预训练语料
---- | --------------|------------|------------|----------|----------|----------
GPT-1|12|3072|12|768|0.12B|5GB
GPT-2|48|6400|25|1600|1.5B|40GB
GPT-3|96|49152|96|12288|175B|570GB

GPT-1 是 GPT 系列的开山之作，也是第一个使用 Decoder-Only 的预训练模型。但是，GPT-1 的模型体量和预训练数据都较少，沿承了传统 Transformer 的模型结构，使用了 12层 Decoder Block 和 768 的隐藏层维度，模型参数量仅有 1.17亿（0.12B），在大小为 5GB 的 BooksCorpus 数据集上预训练得到。可以看到，GPT-1 的参数规模与预训练规模和 BERT-base 是大致相当的，但其表现相较于 BERT-base 却有所不如，这也是 GPT 系列模型没能成为预训练语言模型时代的代表的原因。

GPT-2 则是 OpenAI 在 GPT-1 的基础上进一步探究预训练语言模型多任务学习能力的产物。GPT-2 的模型结构和 GPT-1 大致相当，只是扩大了模型参数规模、将 Post-Norm 改为了 Pre-Norm（也就是先进行 LayerNorm 计算，再进入注意力层计算）。这些改动的核心原因在于，由于模型层数增加、体量增大，梯度消失和爆炸的风险也不断增加，为了使模型梯度更稳定对上述结构进行了优化。

GPT-2 的核心改进是大幅增加了预训练数据集和模型体量。GPT-2 的 Decoder Block 层数达到了48（注意，GPT-2 共发布了四种规格的模型，此处我们仅指规格最大的 GPT-2 模型），隐藏层维度达到了 1600，模型整体参数量达 15亿（1.5B），使用了自己抓取的 40GB 大小的 WebText 数据集进行预训练，不管是模型结构还是预训练大小都超过了 1代一个数量级。

GPT-2 的另一个重大突破是以 zero-shot（零样本学习）为主要目标，也就是不对模型进行微调，直接要求模型解决任务。例如，在传统的预训练-微调范式中，我们要解决一个问题，一般需要收集几百上千的训练样本，在这些训练样本上微调预训练语言模型来实现该问题的解决。而 zero-shot 则强调不使用任何训练样本，直接通过向预训练语言模型描述问题来去解决该问题。zero-shot 的思路自然是比预训练-微调范式更进一步、更高效的自然语言范式，但是在 GPT-2 的时代，模型能力还不足够支撑较好的 zero-shot 效果，在大模型时代，zero-shot 及其延伸出的 few-shot（少样本学习）才开始逐渐成为主流。

GPT-3 则是更进一步展示了 OpenAI“力大砖飞”的核心思路，也是 LLM 的开创之作。在 GPT-2 的基础上，OpenAI 进一步增大了模型体量和预训练数据量，整体参数量达 175B，是当之无愧的“大型语言模型”。在模型结构上，基本没有大的改进，只是由于巨大的模型体量使用了稀疏注意力机制来取代传统的注意力机制。在预训练数据上，则是分别从 CC、WebText、维基百科等大型语料集中采样，共采样了 45T、清洗后 570GB 的数据。根据推算，GPT-3 需要在 1024张 A100（80GB 显存）的分布式训练集群上训练 1个月。

之所以说 GPT-3 是 LLM 的开创之作，除去其巨大的体量带来了涌现能力的凸显外，还在于其提出了 few-shot 的重要思想。few-shot 是在 zero-shot 上的改进，研究者发现即使是 175B 大小的 GPT-3，想要在 zero-shot 上取得较好的表现仍然是一件较为困难的事情。而 few-shot 是对 zero-shot 的一个折中，旨在提供给模型少样的示例来教会它完成任务。few-shot 一般会在 prompt（也就是模型的输入）中增加 3~5个示例，来帮助模型理解。例如，对于情感分类任务：

    zero-shot：请你判断‘这真是一个绝佳的机会’的情感是正向还是负向，如果是正向，输出1；否则输出0

    few-shot：请你判断‘这真是一个绝佳的机会’的情感是正向还是负向，如果是正向，输出1；否则输出0。你可以参考以下示例来判断：‘你的表现非常好’——1；‘太糟糕了’——0；‘真是一个好主意’——1。

通过给模型提供少量示例，模型可以取得远好于 zero-shot 的良好表现。few-shot 也被称为上下文学习（In-context Learning），即让模型从提供的上下文中的示例里学习问题的解决方法。GPT-3 在 few-shot 上展现的强大能力，为 NLP 的突破带来了重要进展。如果对于绝大部分任务都可以通过人为构造 3~5个示例就能让模型解决，其效率将远高于传统的预训练-微调范式，意味着 NLP 的进一步落地应用成为可能——而这，也正是 LLM 的核心优势。

在 GPT 系列模型的基础上，通过引入预训练-指令微调-人类反馈强化学习的三阶段训练，OpenAI 发布了跨时代的 ChatGPT，引发了大模型的热潮。也正是在 GPT-3 及 ChatGPT 的基础上，LLaMA、ChatGLM 等模型的发布进一步揭示了 LLM 的无尽潜力。在下一节，我们将深入剖析目前 LLM 的普适架构——LLaMA。

##### 3.3.2 LLaMA

LLaMA模型是由Meta（前Facebook）开发的一系列大型预训练语言模型。从LLaMA-1到LLaMA-3，LLaMA系列模型展示了大规模预训练语言模型的演进及其在实际应用中的显著潜力。

###### （1） 模型架构——Decoder Only

与GPT系列模型一样，LLaMA模型也是基于Decoder-Only架构的预训练语言模型。LLaMA模型的整体结构与GPT系列模型类似，只是在模型规模和预训练数据集上有所不同。如图3.13是LLaMA模型的架构示意图：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/3-1.png)
图3.13 LLaMA-3 模型结构


与GPT类似，LLaMA模型的处理流程也始于将输入文本通过tokenizer进行编码，转化为一系列的input_ids。这些input_ids是模型能够理解和处理的数据格式。接下来，这些input_ids会经过embedding层的转换，这里每个input_id会被映射到一个高维空间中的向量，即词向量。同时，输入文本的位置信息也会通过positional embedding层被编码，以确保模型能够理解词序上下文信息。

这样，input_ids经过embedding层和positional embedding层的结合，形成了hidden_states。hidden_states包含了输入文本的语义和位置信息，是模型进行后续处理的基础，hidden_states随后被输入到模型的decoder层。

在decoder层中，hidden_states会经历一系列的处理，这些处理由多个decoder block组成。每个decoder block都是模型的核心组成部分，它们负责对hidden_states进行深入的分析和转换。在每个decoder block内部，首先是一个masked self-attention层。在这个层中，模型会分别计算query、key和value这三个向量。这些向量是通过hidden_states线性变换得到的，它们是计算注意力权重的基础。然后使用softmax函数计算attention score，这个分数反映了不同位置之间的关联强度。通过attention score，模型能够确定在生成当前词时，应该给予不同位置的hidden_states多大的关注。然后，模型将value向量与attention score相乘，得到加权后的value，这就是attention的结果。

在完成masked self-attention层之后，hidden_states会进入MLP层。在这个多层感知机层中，模型通过两个全连接层对hidden_states进行进一步的特征提取。第一个全连接层将hidden_states映射到一个中间维度，然后通过激活函数进行非线性变换，增加模型的非线性能力。第二个全连接层则将特征再次映射回原始的hidden_states维度。

最后，经过多个decoder block的处理，hidden_states会通过一个线性层进行最终的映射，这个线性层的输出维度与词表维度相同。这样，模型就可以根据hidden_states生成目标序列的概率分布，进而通过采样或贪婪解码等方法，生成最终的输出序列。这一过程体现了LLaMA模型强大的序列生成能力。

###### （2） LLaMA模型的发展历程

**LLaMA-1 系列**：

- Meta于2023年2月发布了LLaMA-1，包括7B、13B、30B和65B四个参数量版本。
- 这些模型在超过1T token的语料上进行了预训练，其中最大的65B参数模型在2,048张A100 80G GPU上训练了近21天。
- LLaMA-1因其开源性和优异性能迅速成为开源社区中最受欢迎的大模型之一。

**LLaMA-2 系列**：

- 2023年7月，Meta发布了LLaMA-2，包含7B、13B、34B和70B四个参数量版本，除了34B模型外，其他均已开源。
- LLaMA-2将预训练的语料扩充到了2T token，并将模型的上下文长度从2,048翻倍到了4,096。
- 引入了分组查询注意力机制（Grouped-Query Attention, GQA）等技术。

**LLaMA-3 系列**：

- 2024年4月，Meta发布了LLaMA-3，包括8B和70B两个参数量版本，同时透露400B的LLaMA-3还在训练中。
- LLaMA-3支持8K长文本，并采用了编码效率更高的tokenizer，词表大小为128K。
- 使用了超过15T token的预训练语料，是LLaMA-2的7倍多。

LLaMA模型以其技术创新、多参数版本、大规模预训练和高效架构设计而著称。模型支持从70亿到数百亿不等的参数量，适应不同规模的应用需求。LLaMA-1以其开源性和优异性能迅速受到社区欢迎，而LLaMA-2和LLaMA-3进一步通过引入分组查询注意力机制和支持更长文本输入，显著提升了模型性能和应用范围。特别是LLaMA-3，通过采用128K词表大小的高效tokenizer和15T token的庞大训练数据，实现了在多语言和多任务处理上的重大进步。Meta对模型安全性和社区支持的持续关注，预示着LLaMA将继续作为AI技术发展的重要推动力，促进全球范围内的技术应用和创新。

##### 3.3.3 GLM

GLM 系列模型是由智谱开发的主流中文 LLM 之一，包括 ChatGLM1、2、3及 GLM-4 系列模型，覆盖了指令理解、代码生成等多种应用场景，曾在多种中文评估集上达到 SOTA 性能。

ChatGLM-6B 是 GLM 系列的开山之作，也是 2023年国内最早的开源中文 LLM，也是最早提出不同于 GPT、LLaMA 的独特模型架构的 LLM。在整个中文 LLM 的发展历程中，GLM 具有独特且重大的技术意义。本节将简要叙述 GLM 系列的发展，并介绍其不同于 GPT、LLaMA 系列模型的独特技术思路。

###### （1）模型架构-相对于 GPT 的略微修正

GLM 最初是由清华计算机系推出的一种通用语言模型基座，其核心思路是在传统 CLM 预训练任务基础上，加入 MLM 思想，从而构建一个在 NLG 和 NLU 任务上都具有良好表现的统一模型。

在整体模型结构上，GLM 和 GPT 大致类似，均是 Decoder-Only 的结构，仅有三点细微差异：

1. 使用 Post Norm 而非 Pre Norm。Post Norm 是指在进行残差连接计算时，先完成残差计算，再进行 LayerNorm 计算；而类似于 GPT、LLaMA 等模型都使用了 Pre Norm，也就是先进行 LayerNorm 计算，再进行残差的计算。相对而言，Post Norm 由于在残差之后做归一化，对参数正则化的效果更强，进而模型的鲁棒性也会更好；Pre Norm相对于因为有一部分参数直接加在了后面，不需要对这部分参数进行正则化，正好可以防止模型的梯度爆炸或者梯度消失。因此，对于更大体量的模型来说，一般认为 Pre Norm 效果会更好。但 GLM 论文提出，使用 Post Norm 可以避免 LLM 的数值错误（虽然主流 LLM 仍然使用了 Pre Norm）；

2. 使用单个线性层实现最终 token 的预测，而不是使用 MLP；这样的结构更加简单也更加鲁棒，即减少了最终输出的参数量，将更大的参数量放在了模型本身；

3. 激活函数从 ReLU 换成了 GeLUs。ReLU 是传统的激活函数，其核心计算逻辑为去除小于 0的传播，保留大于 0的传播；GeLUs 核心是对接近于 0的正向传播，做了一个非线性映射，保证了激活函数后的非线性输出，具有一定的连续性。

###### （2）预训练任务-GLM

GLM 的核心创新点主要在于其提出的 GLM（General Language Model，通用语言模型）任务，这也是 GLM 的名字由来。GLM 是一种结合了自编码思想和自回归思想的预训练方法。所谓自编码思想，其实也就是 MLM 的任务学习思路，在输入文本中随机删除连续的 tokens，要求模型学习被删除的 tokens；所谓自回归思想，其实就是传统的 CLM 任务学习思路，也就是要求模型按顺序重建连续 tokens。

GLM 通过优化一个自回归空白填充任务来实现 MLM 与 CLM 思想的结合。其核心思想是，对于一个输入序列，会类似于 MLM 一样进行随机的掩码，但遮蔽的不是和 MLM 一样的单个 token，而是每次遮蔽一连串 token；模型在学习时，既需要使用遮蔽部分的上下文预测遮蔽部分，在遮蔽部分内部又需要以 CLM 的方式完成被遮蔽的 tokens 的预测。例如，输入和输出可能是：

    输入：I <MASK> because you <MASK>
    输出：<MASK> - love you; <MASK> - are a wonderful person

通过将 MLM 与 CLM 思想相结合，既适配逐个 token 生成的生成类任务，也迫使模型从前后两个方向学习输入文本的隐含关系从而适配了理解类任务。使用 GLM 预训练任务产出的 GLM 模型，在一定程度上展现了其超出同体量 BERT 系模型的优越性能：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/3-2.png)
图3.14 alt text


不过，GLM 预训练任务更多的优势还是展现在预训练模型时代，迈入 LLM 时代后，针对于超大规模、体量的预训练，CLM 展现出远超 MLM 的优势。通过将模型体量加大、预训练规模扩大，CLM 预训练得到的生成模型在文本理解上也能具有超出 MLM 训练的理解模型的能力，因此，ChatGLM 系列模型也仅在第一代模型使用了 GLM 的预训练思想，从 ChatGLM2 开始，还是回归了传统的 CLM 建模。虽然从 LLM 的整体发展路径来看，GLM 预训练任务似乎是一个失败的尝试，但通过精巧的设计将 CLM 与 MLM 融合，并第一时间产出了中文开源的原生 LLM，其思路仍然存在较大的借鉴意义。

###### （3）GLM 家族的发展

在 GLM 模型（即使用原生 GLM 架构及预训练任务的早期预训练模型）的基础上，参考 ChatGPT 的技术思路进行 SFT 和 RLHF，智谱于 23年 3月发布了第一个中文开源 LLM ChatGLM-6B，成为了众多中文 LLM 研究者的起点。ChatGLM-6B 在 1T 语料上进行预训练，支持 2K 的上下文长度。

在 23年 6月，智谱就开源了 ChatGLM2-6B。相对于一代，ChatGLM2 将上下文长度扩展到了 32K，通过更大的预训练规模实现了模型性能的大幅度突破。不过，在 ChatGLM2 中，模型架构就基本回归了 LLaMA 架构，引入 MQA 的注意力机制，预训练任务也回归经典的 CLM，放弃了 GLM 的失败尝试。

ChatGLM3-6B 发布于 23年 10月，相对于二代在语义、数学、推理、代码和知识方面都达到了当时的 SOTA 性能，但是官方给出的技术报告说明 ChatGLM3 在模型架构上相对二代没有变化，最主要的优化来源是更多样化的训练数据集、更充足的训练步骤和更优化的训练策略。ChatGLM3 的另一个重要改进在于其开始支持函数调用与代码解释器，开发者可以直接使用开源的 ChatGLM3 来实现 Agent 开发，具有更广泛的应用价值。

2024年 1月，智谱发布了支持 128K 上下文，包括多种类型的 GLM-4 系列模型，评估其在英文基准上达到了 GPT-4 的水平。不过，智谱并未直接开源 GLM-4，而是开源了其轻量级版本 GLM-4-9B 模型，其在 1T token 的多语言语料库上进行预训练，上下文长度为 8K，并使用与 GLM-4 相同的管道和数据进行后训练。在训练计算量较少的情况下，其超越了 Llama-3-8B，并支持 GLM-4 中所有工具的功能。

图3.15展示了 GLM 系列模型在基准集上的表现演进：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/3-figures/3-3.png)
图3.15 alt text


**参考资料**

[1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* arXiv preprint arXiv:1810.04805.

[2] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov. (2019). *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* arXiv preprint arXiv:1907.11692.

[3] Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut. (2020). *ALBERT: A Lite BERT for Self-supervised Learning of Language Representations.* arXiv preprint arXiv:1909.11942.

[4] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu. (2023). *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.* arXiv preprint arXiv:1910.10683.

[5] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu. (2020). *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.* Journal of Machine Learning Research, 21(140), 1–67.

[6] Alec Radford, Karthik Narasimhan. (2018). *Improving Language Understanding by Generative Pre-Training*. Retrieved from https://api.semanticscholar.org/CorpusID:49313245

[7] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei. (2020). *Language Models are Few-Shot Learners.* arXiv preprint arXiv:2005.14165.

[8] 张帆, 陈安东的文章“万字长文带你梳理Llama开源家族：从Llama-1到Llama-3”，来源：https://mp.weixin.qq.com/s/5_VnzP3JmOB0D5geV5HRFg

[9] Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Dan Zhang, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang, Jing Zhang, Jingyu Sun, Juanzi Li, Lei Zhao, Lindong Wu, Lucen Zhong, Mingdao Liu, Minlie Huang, Peng Zhang, Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang, Shulin Cao, Shuxun Yang, Weng Lam Tam, Wenyi Zhao, Xiao Liu, Xiao Xia, Xiaohan Zhang, Xiaotao Gu, Xin Lv, Xinghan Liu, Xinyi Liu, Xinyue Yang, Xixuan Song, Xunkai Zhang, Yifan An, Yifan Xu, Yilin Niu, Yuantao Yang, Yueyan Li, Yushi Bai, Yuxiao Dong, Zehan Qi, Zhaoyu Wang, Zhen Yang, Zhengxiao Du, Zhenyu Hou, and Zihan Wang. (2024). *ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools.* arXiv preprint arXiv:2406.12793.

[10] Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang 和 Jie Tang. (2022). *GLM: General Language Model Pretraining with Autoregressive Blank Infilling.* arXiv preprint arXiv:2103.10360.

### 第四章 大语言模型

#### 4.1 什么是 LLM

在前三章，我们从 NLP 的定义与主要任务出发，介绍了引发 NLP 领域重大变革的核心思想——注意力机制与 Transformer 架构。随着 Transformer 架构的横空出世，NLP 领域逐步进入预训练-微调范式，以 Transformer 为基础的、通过预训练获得强大文本表示能力的预训练语言模型层出不穷，将 NLP 的各种经典任务都推进到了一个新的高度。

随着2022年底 ChatGPT 再一次刷新 NLP 的能力上限，大语言模型（Large Language Model，LLM）开始接替传统的预训练语言模型（Pre-trained Language Model，PLM） 成为 NLP 的主流方向，基于 LLM 的全新研究范式也正在刷新被 BERT 发扬光大的预训练-微调范式，NLP 由此迎来又一次翻天覆地的变化。从2022年底至今，LLM 能力上限不断刷新，通用基座大模型数量指数级上升，基于 LLM 的概念、应用也是日新月异，预示着大模型时代的到来。

在第三章，我们从模型架构的角度出发，分别分析了 Encoder-Only、Encoder-Decoder 和 Decoder-Only 三种架构下的经典模型及其训练过程。这些模型有的是 LLM 时代之前堪称时代主角的里程碑（如 BERT），有的则是 LLM 时代的舞台主角，是通用人工智能（Artificial General Intelligence，AGI） 的有力竞争者。那么，究竟什么是 LLM，LLM 和传统的 PLM 的核心差异在哪里，又是什么令研究者们对 LLM 抱有如此高的热情与期待呢？

在本章中，我们将结合上文的模型架构讲解，深入分析 LLM 的定义、特点及其能力，为读者揭示 LLM 与传统深度学习模型的核心差异，并在此基础上，展示 LLM 的实际三阶段训练过程，帮助读者从概念上梳理清楚 LLM 是如何获得这样的独特能力的，从而为进一步实践 LLM 完整训练提供理论基础。

##### 4.1.1 LLM 的定义

LLM，即 Large Language Model，中文名为大语言模型或大型语言模型，是一种相较传统语言模型参数量更多、在更大规模语料上进行预训练的语言模型。

在第一章中，我们已经介绍了语言模型的概念，即通过预测下一个 token 任务来训练的 NLP 模型。LLM 使用与传统预训练语言模型相似的架构与预训练任务（如 Decoder-Only 架构与 CLM 预训练任务），但拥有更庞大的参数、在更海量的语料上进行预训练，也从而展现出与传统预训练语言模型截然不同的能力。

一般来说，LLM 指包含**数百亿（或更多）参数的语言模型**，它们往往在**数 T token 语料上**通过多卡分布式集群进行预训练，具备远超出传统预训练模型的文本理解与生成能力。不过，随着 LLM 研究的不断深入，多种参数尺寸的 LLM 逐渐丰富，广义的 LLM 一般覆盖了从**十亿参数**（如 Qwen-1.5B）到**千亿参数**（如 Grok-314B）的所有大型语言模型。只要模型展现出**涌现能力**，即在一系列复杂任务上表现出远超传统预训练模型（如 BERT、T5）的能力与潜力，都可以称之为 LLM。

一般认为，GPT-3（1750亿参数）是 LLM 的开端，基于 GPT-3 通过 预训练（Pretraining）、监督微调（Supervised Fine-Tuning，SFT）、强化学习与人类反馈（Reinforcement Learning with Human Feedback，RLHF）三阶段训练得到的 ChatGPT 更是主导了 LLM 时代的到来。自2022年11月 OpenAI 发布 ChatGPT 至今不到2年时间里，已涌现出了上百个各具特色、能力不一的 LLM。下表列举了自 2022年11月至2023年11月国内外发布的部分大模型：

时间     | 开源 LLM                                       | 闭源 LLM
-------- | -----                                         | --------
2022.11  | 无                                            | OpenAI-ChatGPT
2023.02  | Meta-LLaMA；复旦-MOSS                         | 无
2023.03  | 斯坦福-Alpaca、Vicuna；智谱-ChatGLM|OpenAI-GPT4；百度-文心一言；Anthropic-Claude；Google-Bard
2023.04  | 阿里-通义千问；Stability AI-StableLM|商汤-日日新
2023.05  | 微软-Pi；Tll-Falcon|讯飞-星火大模型；Google-PaLM2
2023.06  | 智谱-ChatGLM2；上海 AI Lab-书生浦语；百川-BaiChuan；虎博-TigerBot|360-智脑大模型
2023.07  | Meta-LLaMA2|Anthropic-Claude2；华为-盘古大模型3
2023.08  | 无|字节-豆包
2023.09  | 百川-BaiChuan2|Google-Gemini；腾讯-混元大模型
2023.11  | 零一万物-Yi；幻方-DeepSeek|xAI-Grok

目前，国内外企业、研究院正不断推出性能更强大的 LLM，探索通往 AGI 的道路。

##### 4.1.2 LLM 的能力

###### （1）涌现能力（Emergent Abilities）

区分 LLM 与传统 PLM 最显著的特征即是 LLM 具备 `涌现能力` 。涌现能力是指同样的模型架构与预训练任务下，某些能力在小型模型中不明显，但在大型模型中特别突出。可以类比到物理学中的相变现象，涌现能力的显现就像是模型性能随着规模增大而迅速提升，超过了随机水平，也就是我们常说的量变引起了质变。

具体来说，涌现能力可以定义为与某些复杂任务相关的能力。但一般而言，NLP 更关注的是它们具备的通用能力，也就是能够应用于解决各种 NLP 任务的能力。涌现能力是目前业界和学界对 LLM 保持较高的热情和关注的核心所在，即虽然 LLM 目前的能力、所能解决的任务与人类最终所期待的通用人工智能还存在不小的差距，但在涌现能力的作用下，我们相信随着研究的不断深入、高质量数据的不断涌现和更高效的模型架构及训练框架的出现，LLM 终能具备通用人工智能所需要具备的能力，从而给人类生活带来质变。

###### （2）上下文学习（In-context Learning）

上下文学习能力是由 GPT-3 首次引入的。具体而言，上下文学习是指允许语言模型在提供自然语言指令或多个任务示例的情况下，通过理解上下文并生成相应输出的方式来执行任务，而无需额外的训练或参数更新。

对传统 PLM，在经过高成本的预训练之后，往往还需要对指定的下游任务进行有监督微调。虽然传统 PLM 体量较小，对算力要求较低，但例如 BERT 类模型（0.5B 参数），进行有监督微调一般还是需要 10G 以上显存，有一定的算力成本。而同时，有监督微调的训练数据的成本更高。针对下游任务难度的不同，需要的训练样本数往往在 1k~数十k 不等，均需要进行人工标注，数据获取上有不小的成本。而具备上下文学习能力的 LLM 往往无需进行高成本的额外训练或微调，而可以通过少数示例或是调整自然语言指令，来处理绝大部分任务，从而大大节省了算力和数据成本。

上下文学习能力也正在引发 NLP 研究范式的变革。在传统 PLM 时代，解决 NLP 下游任务的一般范式是预训练-微调，即选用一个合适的预训练模型，针对自己的下游任务准备有监督数据来进行微调。而通过使用具备上下文学习能力的 LLM，一般范式开始向 Prompt Engineering 也就是调整 Prompt 来激发 LLM 的能力转变。例如，目前绝大部分 NLP 任务，通过调整 Prompt 或提供 1~5 个自然语言示例，就可以令 GPT-4 达到超过传统 PLM 微调的效果。

###### （3）指令遵循（Instruction Following）

通过使用自然语言描述的多任务数据进行微调，也就是所谓的 `指令微调` ，LLM 被证明在同样使用指令形式化描述的未见过的任务上表现良好。也就是说，经过指令微调的 LLM 能够理解并遵循未见过的指令，并根据任务指令执行任务，而无需事先见过具体示例，这展示了其强大的泛化能力。

指令遵循能力意味我们不再需要每一件事都先教模型，然后它才能去做。我们只需要在指令微调阶段混合多种指令来训练其泛化能力，LLM 就可以处理人类绝大部分指令，即可以灵活地解决用户遇到的问题。这一点在 ChatGPT 上体现地尤为明显。ChatGPT 之所以能够具备极高的热度，其核心原因即在于其不再是仅能用于学界、业界研究的理论模型，而同样可以广泛地服务于各行各业用户。通过给 ChatGPT 输入指令，其可以写作文、编程序、批改试卷、阅读报纸等等。

指令遵循能力使 LLM 可以真正和多个行业结合起来，通过人工智能技术为人类生活的方方面面赋能，从而为人类带来质的改变。不管是目前大火的 Agent、WorkFlow，还是并不遥远的未来可能就会出现的全能助理、超级智能，其本质依赖的都是 LLM 的指令遵循能力。

###### （4）逐步推理（Step by Step Reasoning）

逻辑推理，尤其是涉及多个推理步骤的复杂推理任务，一直是 NLP 的攻关难点，也是人工智能难以得到普遍认可的重要原因。毕竟，如果一个模型不能解答基础的“鸡兔同笼”问题，或者不能识别语言中的逻辑陷阱，你很难认为它是“智能的”而非“智障的”。

但是，传统的 NLP 模型通常难以解决涉及多个推理步骤的复杂任务，例如数学问题。然而，LLM 通过采用思维链（Chain-of-Thought，CoT）推理策略，可以利用包含中间推理步骤的提示机制来解决这些任务，从而得出最终答案。据推测，这种能力可能是通过对代码的训练获得的。

逐步推理能力意味着 LLM 可以处理复杂逻辑任务，也就是说可以解决日常生活中需要逻辑判断的绝大部分问题，从而向“可靠的”智能助理迈出了坚实的一步。

这些独特能力是 LLM 区别于传统 PLM 的重要优势，也让 LLM 在处理各种任务时表现出色，使它们成为了解决复杂问题和应用于多领域的强大工具。正是因为涌现能力、上下文学习能力、指令遵循能力与逐步推理能力的存在，NLP 研究人员相信 LLM 是迈向通用人工智能，帮助人类社会实现生产力质变的重要途径。而事实上，目前已有众多基于 LLM 的应用，旨在利用 LLM 的独特能力显著提高生产力。例如，微软基于 GPT-4 推出的 Copilot，就基于 LLM 强大的指令遵循能力与逐步推理能力，通过提供代码补全、代码提示、代码编写等多种功能，辅助程序员更高效、便捷、精准地编写程序，极大提高了程序员的生产效率。

##### 4.1.3 LLM 的特点

除上文讨论的 LLM 的核心能力外，LLM 还具备一些额外的、有趣或是危险的特点，这些特点也是 LLM 目前重要的研究方向，在此讨论其中一二：

###### （1）多语言支持

多语言、跨语言模型曾经是 NLP 的一个重要研究方向，但 LLM 由于需要使用到海量的语料进行预训练，训练语料往往本身就是多语言的，因此 LLM 天生即具有多语言、跨语言能力，只不过随着训练语料和指令微调的差异，在不同语言上的能力有所差异。由于英文高质量语料目前仍是占据大部分，以 GPT-4 为代表的绝大部分模型在英文上具有显著超越中文的能力。虽然都可以对多种语言进行处理，但针对中文进行额外训练和优化的国内模型（如文心一言、通义千问等）往往能够在中文环境上展现更优越的效果。

###### （2）长文本处理

由于能够处理多长的上下文文本，在一定程度上决定了模型的部分能力上限，LLM 往往比传统 PLM 更看重长文本处理能力。相对于以 512 token 为惯例的传统 PLM（如 BERT、T5等模型的最大上下文长度均为 512），LLM 在拓宽最大上下文长度方面可谓妙计频出。由于在海量分布式训练集群上进行训练，LLM 往往在训练时就支持 4k、8k 甚至 32k 的上下文长度。同时，LLM 大部分采用了旋转位置编码（Rotary Positional Encoding，RoPE）（或者同样具有外推能力的 AliBi）作为位置编码，具有一定的长度外推能力，也就是在推理时能够处理显著长于训练长度的文本。例如，InternLM 在 32k 长度上下文上进行了预训练，但通过 RoPE 能够实现 200k 长度的上下文处理。通过不断增强长文本处理能力，LLM 往往能够具备更强的信息阅读、信息总结能力，从而解决诸如要求 LLM 读完《红楼梦》并写一篇对应的高考作文的“世纪难题”。

###### （3）拓展多模态

LLM 的强大能力也为其带来了跨模态的强大表现。随着 LLM 的不断改进，通过为 LLM 增加额外的参数来进行图像表示，从而利用 LLM 的强大能力打造支持文字、图像双模态的模型，已经是一个成功的方法。通过引入 Adapter 层和图像编码器，并针对性地在图文数据上进行有监督微调，模型能够具备不错的图文问答甚至生成能力。在未来，如何对齐文本与图像的表示，从而打造更强大的多模态大模型，将 LLM 的能力辐射到更多模态，是一个重要的研究方向。

###### （4）挥之不去的幻觉

幻觉，是指 LLM 根据 Prompt 杜撰生成虚假、错误信息的表现。例如，当我们要求 LLM 生成一篇学术论文及其参考文献列表时，其往往会捏造众多看似“一本正经”实则完全不存在的论文和研究。幻觉问题是 LLM 的固有缺陷，也是目前 LLM 研究及应用的巨大挑战。尤其是在医学、金融学等非常强调精准、正确的领域，幻觉的存在可能造成非常严重的后果。目前也有很多研究提供了削弱幻觉的一些方法，如 Prompt 里进行限制、通过 RAG（检索增强生成）来指导生成等，但都还只能一定程度减弱幻觉而无法彻底根除。

除上述几点之外，LLM 还存在诸多可供研究的特点，例如我们将在下一节详细论述的 LLM 三阶段训练流程、LLM 的自我反思性等，此处就不一一列举赘述了。

#### 4.2 如何训练一个 LLM

在上一节，我们分析了 LLM 的定义及其特有的强大能力，通过更大规模的参数和海量的训练语料获得远超传统预训练模型的涌现能力，展现出强大的上下文学习、指令遵循及逐步推理能力，带来 NLP 领域的全新变革。那么，通过什么样的步骤，我们才可以训练出一个具有涌现能力的 LLM 呢？训练一个 LLM，与训练传统的预训练模型，又有什么区别？


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/4-figures/2-0.jpg)
图4.1 训练 LLM 的三个阶段


一般而言，训练一个完整的 LLM 需要经过图1中的三个阶段——Pretrain、SFT 和 RLHF。在这一节，我们将详细论述训练 LLM 的三个阶段，并分析每一个阶段的过程及其核心难点、注意事项，帮助读者们从理论上了解要训练一个 LLM，需要经过哪些步骤。

##### 4.2.1 Pretrain

Pretrain，即预训练，是训练 LLM 最核心也是工程量最大的第一步。LLM 的预训练和传统预训练模型非常类似，同样是使用海量无监督文本对随机初始化的模型参数进行训练。正如我们在第三章中所见，目前主流的 LLM 几乎都采用了 Decoder-Only 的类 GPT 架构（LLaMA 架构），它们的预训练任务也都沿承了 GPT 模型的经典预训练任务——因果语言模型（Causal Language Model，CLM）。

因果语言模型建模，即和最初的语言模型一致，通过给出上文要求模型预测下一个 token 来进行训练。CLM 的过程和原理我们已在第三章详细论述过，此处就不再赘述。LLM 的预训练同传统预训练模型的核心差异即在于，预训练的体量和资源消耗。

根据定义，LLM 的核心特点即在于其具有远超传统预训练模型的参数量，同时在更海量的语料上进行预训练。传统预训练模型如 BERT，有 base 和 large 两个版本。BERT-base 模型由 12个 Encoder 层组成，其 hidden_size 为 768，使用 12个头作为多头注意力层，整体参数量为 1亿（110M）；而 BERT-large 模型由 24个 Encoder 层组成，hidden_size 为 1024，有 16个头，整体参数量为 3亿（340M）。同时，BERT 预训练使用了 33亿（3B）token 的语料，在 64块 TPU 上训练了 4天。事实上，相对于传统的深度学习模型，3亿参数量、33亿训练数据的 BERT 已经是一个能力超群、资源消耗巨大的庞然大物。

但是，前面我们提到，一般而言的 LLM 通常具有数百亿甚至上千亿参数，即使是广义上最小的 LLM，一般也有十亿（1B）以上的参数量。例如以开山之作 GPT-3 为例，其有 96个 Decoder 层，12288 的 hidden_size 和 96个头，共有 1750亿（175B）参数，比 BERT 大出快 3个数量级。即使是目前流行的小型 LLM 如 Qwen-1.8B，其也有 24个 Decoder 层、2048的 hidden_size 和 16个注意力头，整体参数量达到 18亿（1.8B）。

模型|hidden_layers|hidden_size|heads|整体参数量|预训练数据量
----| -----------|-----------|------|---------|---------
BERT-base|12|768|12|0.1B|3B
BERT-large|24|1024|16|0.3B|3B
Qwen-1.8B|24|2048|16|1.8B|2.2T
LLaMA-7B|32|4096|32|7B|1T
GPT-3|96|12288|96|175B|300B


更重要的是，LLM 往往需要使用更大规模的预训练语料。根据由 OpenAI 提出的 Scaling Law：C ~ 6ND，其中 C 为计算量，N 为模型参数，D 为训练的 token 数，可以实验得出训练 token 数应该是模型参数的 1.7倍，也就是说 175B 的 GPT-3，需要使用 300B token 进行预训练。而 LLaMA 更是进一步提出，使用 20倍 token 来训练模型能达到效果最优，因此 175B 的 GPT-3，可以使用3.5T token 数据预训练达到最优性能。

如此庞大的模型参数和预训练数据，使得预训练一个 LLM 所需要的算力资源极其庞大。事实上，哪怕是预训练一个 1B 的大模型，也至少需要多卡分布式 GPU 集群，通过分布式框架对模型参数、训练的中间参数和训练数据进行切分，才能通过以天为单位的长时间训练来完成。一般来说，百亿级 LLM 需要 1024张 A100 训练一个多月，而十亿级 LLM 一般也需要 256张 A100 训练两、三天，计算资源消耗非常高。

也正因如此，分布式训练框架也成为 LLM 训练必不可少的组成部分。分布式训练框架的核心思路是数据并行和模型并行。所谓数据并行，是指训练模型的尺寸可以被单个 GPU 内存容纳，但是由于增大训练的 batch_size 会增大显存开销，无法使用较大的 batch_size 进行训练；同时，训练数据量非常大，使用单张 GPU 训练时长难以接受。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/4-figures/2-1.jpg)
图4.2 模型、数据并行


因此，如图4.2所示可以让模型实例在不同 GPU 和不同批数据上运行，每一次前向传递完成之后，收集所有实例的梯度并计算梯度更新，更新模型参数之后再传递到所有实例。也就是在数据并行的情况下，每张 GPU 上的模型参数是保持一致的，训练的总批次大小等于每张卡上的批次大小之和。

但是，当 LLM 扩大到上百亿参数，单张 GPU 内存往往就无法存放完整的模型参数。如图4.3所示，在这种情况下，可以将模型拆分到多个 GPU 上，每个 GPU 上存放不同的层或不同的部分，从而实现模型并行。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/4-figures/2-2.jpg)
图4.3 模型并行



在数据并行和模型并行的思想基础上，还演化出了多种更高效的分布式方式，例如张量并行、3D 并行、ZeRO（Zero Redundancy Optimizer，零冗余优化器）等。目前，主流的分布式训练框架包括 Deepspeed、Megatron-LM、ColossalAI 等，其中，Deepspeed 使用面最广。

Deepspeed 的核心策略是 ZeRO 和 CPU-offload。ZeRO 是一种显存优化的数据并行方案，其核心思想是优化数据并行时每张卡的显存占用，从而实现对更大规模模型的支持。ZeRO 将模型训练阶段每张卡被占用的显存分为两类：

- 模型状态（Model States），包括模型参数、模型梯度和优化器 Adam 的状态参数。假设模型参数量为 1M，一般来说，在混合精度训练的情况下，该部分需要 16M 的空间进行存储，其中 Adam 状态参数会占据 12M 的存储空间。
- 剩余状态（Residual States），除了模型状态之外的显存占用，包括激活值、各种缓存和显存碎片。

针对上述显存占用，ZeRO 提出了三种不断递进的优化策略：

1. ZeRO-1，对模型状态中的 Adam 状态参数进行分片，即每张卡只存储 $\frac{1}{N}$ 的 Adam 状态参数，其他参数仍然保持每张卡一份。
2. ZeRO-2，继续对模型梯度进行分片，每张卡只存储 $\frac{1}{N}$ 的模型梯度和 Adam 状态参数，仅模型参数保持每张卡一份。
3. ZeRO-3，将模型参数也进行分片，每张卡只存储 $\frac{1}{N}$ 的模型梯度、模型参数和 Adam 状态参数。

可以看出，随着分片的参数量不断增加，每张卡需要占用的显存也不断减少。当然，分片的增加也就意味着训练中通信开销的增加，一般而言，每张卡的 GPU 利用率 ZeRO-1 最高而 ZeRO-3 最低。具体使用什么策略，需要结合计算资源的情况和需要训练的模型体量动态确定。

除去计算资源的要求，训练数据本身也是预训练 LLM 的一个重大挑战。训练一个 LLM，至少需要数百 B 甚至上 T 的预训练语料。根据研究，LLM 所掌握的知识绝大部分都是在预训练过程中学会的，因此，为了使训练出的 LLM 能够覆盖尽可能广的知识面，预训练语料需要组织多种来源的数据，并以一定比例进行混合。目前，主要的开源预训练语料包括 CommonCrawl、C4、Github、Wikipedia 等。不同的 LLM 往往会在开源预训练语料基础上，加入部分私有高质量语料，再基于自己实验得到的最佳配比来构造预训练数据集。事实上，数据配比向来是预训练 LLM 的“核心秘籍”，不同的配比往往会相当大程度影响最终模型训练出来的性能。例如，下表展示了 LLaMA 的预训练数据及配比：

数据集|占比|数据集大小（Disk size）
-----|----|---------------------
CommonCrawl|67.0%|3.3 TB
C4|15.0%|783 GB
Github|4.5%|328 GB
Wikipedia|4.5%|83 GB
Books|4.5%|85 GB
ArXiv|2.5%|92 GB
StackExchange|2.0%|78 GB

训练一个中文 LLM，训练数据的难度会更大。目前，高质量语料还是大部分集中在英文范畴，例如上表的 Wikipedia、Arxiv 等，均是英文数据集；而 C4 等多语言数据集中，英文语料也占据主要地位。目前开源的中文 LLM 如 ChatGLM、Baichuan 等模型均未开放其预训练数据集，开源的中文预训练数据集目前仅有昆仑天工开源的[SkyPile](https://huggingface.co/datasets/Skywork/SkyPile-150B)（150B）、中科闻歌开源的[yayi2](https://huggingface.co/datasets/wenge-research/yayi2_pretrain_data)（100B）等，相较于英文开源数据集有明显差距。

预训练数据的处理与清洗也是 LLM 预训练的一个重要环节。诸多研究证明，预训练数据的质量往往比体量更加重要。预训练数据处理一般包括以下流程：

1. 文档准备。由于海量预训练语料往往是从互联网上获得，一般需要从爬取的网站来获得自然语言文档。文档准备主要包括 URL 过滤（根据网页 URL 过滤掉有害内容）、文档提取（从 HTML 中提取纯文本）、语言选择（确定提取的文本的语种）等。
2. 语料过滤。语料过滤的核心目的是去除低质量、无意义、有毒有害的内容，例如乱码、广告等。语料过滤一般有两种方法：基于模型的方法，即通过高质量语料库训练一个文本分类器进行过滤；基于启发式的方法，一般通过人工定义 web 内容的质量指标，计算语料的指标值来进行过滤。
3. 语料去重。实验表示，大量重复文本会显著影响模型的泛化能力，因此，语料去重即删除训练语料中相似度非常高的文档，也是必不可少的一个步骤。去重一般基于 hash 算法计算数据集内部或跨数据集的文档相似性，将相似性大于指定阈值的文档去除；也可以基于子串在序列级进行精确匹配去重。

目前，已有很多经过处理的高质量预训练语料和专用于预训练数据处理的框架。例如，有基于 LLaMA 思路收集、清洗的预训练数据集[RedPajama-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)，以及在 RedPajama 基础上进行筛选去重的[SlimPajama-627B](https://huggingface.co/datasets/cerebras/SlimPajama-627B/tree/main/train)数据集，实验证明高质量的 627B Slimpajama 数据集能够获得比 1T 的 RedPajama 数据集更好的效果。

##### 4.2.2 SFT

预训练是 LLM 强大能力的根本来源，事实上，LLM 所覆盖的海量知识基本都是源于预训练语料。LLM 的性能本身，核心也在于预训练的工作。但是，预训练赋予了 LLM 能力，却还需要第二步将其激发出来。经过预训练的 LLM 好像一个博览群书但又不求甚解的书生，对什么样的偏怪问题，都可以流畅地接出下文，但他偏偏又不知道问题本身的含义，只会“死板背书”。这一现象的本质是因为，LLM 的预训练任务就是经典的 CLM，也就是训练其预测下一个 token 的能力，在没有进一步微调之前，其无法与其他下游任务或是用户指令适配。

因此，我们还需要第二步来教这个博览群书的学生如何去使用它的知识，也就是 SFT（Supervised Fine-Tuning，有监督微调）。所谓有监督微调，其实就是我们在第三章中讲过的预训练-微调中的微调，稍有区别的是，对于能力有限的传统预训练模型，我们需要针对每一个下游任务单独对其进行微调以训练模型在该任务上的表现。例如要解决文本分类问题，需要对 BERT 进行文本分类的微调；要解决实体识别的问题，就需要进行实体识别任务的微调。

而面对能力强大的 LLM，我们往往不再是在指定下游任务上构造有监督数据进行微调，而是选择训练模型的“通用指令遵循能力”，也就是一般通过`指令微调`的方式来进行 SFT。

所谓指令微调，即我们训练的输入是各种类型的用户指令，而需要模型拟合的输出则是我们希望模型在收到该指令后做出的回复。例如，我们的一条训练样本可以是：

    input:告诉我今天的天气预报？
    output:根据天气预报，今天天气是晴转多云，最高温度26摄氏度，最低温度9摄氏度，昼夜温差大，请注意保暖哦

也就是说，SFT 的主要目标是让模型从多种类型、多种风格的指令中获得泛化的指令遵循能力，也就是能够理解并回复用户的指令。因此，类似于 Pretrain，SFT 的数据质量和数据配比也是决定模型指令遵循能力的重要因素。

首先是指令数据量及覆盖范围。为了使 LLM 能够获得泛化的指令遵循能力，即能够在未训练的指令上表现良好，需要收集大量类别各异的用户指令和对应回复对 LLM 进行训练。一般来说，在单个任务上 500~1000 的训练样本就可以获得不错的微调效果。但是，为了让 LLM 获得泛化的指令遵循能力，在多种任务指令上表现良好，需要在训练数据集中覆盖多种类型的任务指令，同时也需要相对较大的训练数据量，表现良好的开源 LLM SFT 数据量一般在数 B token 左右。

为提高 LLM 的泛化能力，指令数据集的覆盖范围自然是越大越好。**但是**，多种不同类型的指令数据之间的配比也是 LLM 训练的一大挑战。OpenAI 训练的 InstructGPT（即 ChatGPT 前身）使用了源自于用户使用其 API 的十种指令：

指令类型|占比
-------|-----
文本生成|45.6%
开放域问答|12.4%
头脑风暴|11.2%
聊天|8.4%
文本转写|6.6%
文本总结|4.2%
文本分类|3.5%
其他|3.5%
特定域问答|2.6%
文本抽取|1.9%

高质量的指令数据集具有较高的获取难度。不同于预训练使用的无监督语料，SFT 使用的指令数据集是有监督语料，除去设计广泛、合理的指令外，还需要对指令回复进行人工标注，并保证标注的高质量。事实上，ChatGPT 的成功很大一部分来源于其高质量的人工标注数据。但是，人工标注数据成本极高，也罕有企业将人工标注的指令数据集开源。为降低数据成本，部分学者提出了使用 ChatGPT 或 GPT-4 来生成指令数据集的方法。例如，经典的开源指令数据集 [Alpaca](https://github.com/yizhongw/self-instruct/blob/main/human_eval/user_oriented_instructions.jsonl)就是基于一些种子 Prompt，通过 ChatGPT 生成更多的指令并对指令进行回复来构建的。

一般 SFT 所使用的指令数据集包括以下三个键：

```json
{
    "instruction":"即输入的用户指令",
    "input":"执行该指令可能需要的补充输入，没有则置空",
    "output":"即模型应该给出的回复"
}
```

例如，如果我们的指令是将目标文本“今天天气真好”翻译成英文，那么该条样本可以构建成如下形式：

```json
{
    "instruction":"将下列文本翻译成英文：",
    "input":"今天天气真好",
    "output":"Today is a nice day！"
}
```

同时，为使模型能够学习到和预训练不同的范式，在 SFT 的过程中，往往会针对性设置特定格式。例如，LLaMA 的 SFT 格式为：

    ### Instruction:\n{{content}}\n\n### Response:\n

其中的 content 即为具体的用户指令，也就是说，对于每一个用户指令，将会嵌入到上文的 content 部分，这里的用户指令不仅指上例中的 “instruction”，而是指令和输入的拼接，即模型可以执行的一条完整指令。例如，针对上例，LLaMA 获得的输入应该是：

    ### Instruction:\n将下列文本翻译成英文：今天天气真好\n\n### Response:\n

其需要拟合的输出则是：

    ### Instruction:\n将下列文本翻译成英文：今天天气真好\n\n### Response:\nToday is a nice day！

注意，因为指令微调本质上仍然是对模型进行 CLM 训练，只不过要求模型对指令进行理解和回复而不是简单地预测下一个 token，所以模型预测的结果不仅是 output，而应该是 input + output，只不过 input 部分不参与 loss 的计算，但回复指令本身还是以预测下一个 token 的形式来实现的。

但是，随着 LLM 能力的不断增强，模型的多轮对话能力逐渐受到重视。所谓多轮对话，是指模型在每一次对话时能够参考之前对话的历史记录来做出回复。例如，一个没有多轮对话能力的 LLM 可能有如下对话记录：

    用户：你好，我是开源组织 Datawhale 的成员。
    模型：您好，请问有什么可以帮助您的吗？
    用户：你知道 Datawhale 是什么吗？
    模型：不好意思，我不知道 Datawhale 是什么。

也就是说，模型不能记录用户曾经提到或是自己曾经回答的历史信息。如果是一个具有多轮对话能力的 LLM，其对话记录应该是这样的：

    用户：你好，我是开源组织 Datawhale 的成员。
    模型：您好，请问有什么可以帮助您的吗？
    用户：你知道 Datawhale 是什么吗？
    模型：Datawhale 是一个开源组织。

模型是否支持多轮对话，与预训练是没有关系的。事实上，模型的多轮对话能力完全来自于 SFT 阶段。如果要使模型支持多轮对话，我们需要在 SFT 时将训练数据构造成多轮对话格式，让模型能够利用之前的知识来生成回答。假设我们目前需要构造的多轮对话是：

    <prompt_1><completion_1><prompt_2><completion_2><prompt_3><completion_3>

构造多轮对话样本一般有三种方式：

1. 直接将最后一次模型回复作为输出，前面所有历史对话作为输入，直接拟合最后一次回复：

        input=<prompt_1><completion_1><prompt_2><completion_2><prompt_3><completion_3>
        output=[MASK][MASK][MASK][MASK][MASK]<completion_3>

2. 将 N 轮对话构造成 N 个样本：

        input_1 = <prompt_1><completion_1>
        output_1 = [MASK]<completion_1>

        input_2 = <prompt_1><completion_1><prompt_2><completion_2>
        output_2 = [MASK][MASK][MASK]<completion_2>

        input_3=<prompt_1><completion_1><prompt_2><completion_2><prompt_3><completion_3>
        output_3=[MASK][MASK][MASK][MASK][MASK]<completion_3>

3. 直接要求模型预测每一轮对话的输出：

        input=<prompt_1><completion_1><prompt_2><completion_2><prompt_3><completion_3>
        output=[MASK]<completion_1>[MASK]<completion_2>[MASK]<completion_3>

显然可知，第一种方式会丢失大量中间信息，第二种方式造成了大量重复计算，只有第三种方式是最合理的多轮对话构造。我们之所以可以以第三种方式来构造多轮对话样本，是因为 LLM 本质还是进行的 CLM 任务，进行单向注意力计算，因此在预测时会从左到右依次进行拟合，前轮的输出预测不会影响后轮的预测。目前，绝大部分 LLM 均使用了多轮对话的形式来进行 SFT。

##### 4.2.3 RLHF

RLHF，全称是 Reinforcement Learning from Human Feedback，即人类反馈强化学习，是利用强化学习来训练 LLM 的关键步骤。相较于在 GPT-3 就已经初见雏形的 SFT，RLHF 往往被认为是 ChatGPT 相较于 GPT-3 的最核心突破。事实上，从功能上出发，我们可以将 LLM 的训练过程分成预训练与对齐（alignment）两个阶段。预训练的核心作用是赋予模型海量的知识，而所谓对齐，其实就是让模型与人类价值观一致，从而输出人类希望其输出的内容。在这个过程中，SFT 是让 LLM 和人类的指令对齐，从而具有指令遵循能力；而 RLHF 则是从更深层次令 LLM 和人类价值观对齐，令其达到安全、有用、无害的核心标准。

如图4.4所示，ChatGPT 在技术报告中将对齐分成三个阶段，后面两个阶段训练 RM 和 PPO 训练，就是 RLHF 的步骤：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/4-figures/2-3.png)
图4.4 ChatGPT 训练三个的阶段



RLHF 的思路是，引入强化学习的技术，通过实时的人类反馈令 LLM 能够给出更令人类满意的回复。强化学习是有别于监督学习的另一种机器学习方法，主要讨论的问题是智能体怎么在复杂、不确定的环境中最大化它能获得的奖励。强化学习主要由两部分构成：智能体和环境。在强化学习过程中，智能体会不断行动并从环境获取反馈，根据反馈来调整自己行动的策略。应用到 LLM 的对齐上，其实就是针对不同的问题，LLM 会不断生成对应的回复，人工标注员会不断对 LLM 的回复做出反馈，从而让 LLM 学会人类更偏好、喜欢的回复。

RLHF 就类似于 LLM 作为一个学生，不断做作业来去提升自己解题能力的过程。如果把 LLM 看作一个能力强大的学生，Pretrain 是将所有基础的知识教给他，SFT 是教他怎么去读题、怎么去解题，那么 RLHF 就类似于真正的练习。LLM 会不断根据 Pretrain 学到的基础知识和 SFT 学到的解题能力去解答练习，然后人类作为老师批改 LLM 的练习，来让 LLM 反思错误的解题方式，不断强化正确的解题方式。

如上图，RLHF 分为两个步骤：训练 RM 和 PPO 训练。

RM，Reward Model，即奖励模型。RM 是用于拟合人类偏好，来给 LLM 做出反馈的。在强化学习的训练中，对于 LLM 的每一个回复，RM 会进行打分，这个打分反映了生成回复符合人类偏好的程度。然后 LLM 会根据强化学习的原理，基于 RM 的打分来进行优化训练。所以，RM 本质上是一个文本分类模型，对于一个文本输出一个标量奖励，和文本分类任务中的隐藏层输出非常类似。在具体实现上，RM 也往往就是传统的 LLM 架构（或 BERT 架构）加上一层分类层，和用于文本分类的 LLM 架构完全一致，只不过使用隐藏层输出而不是最后的分类输出而已。

但是，在训练 RM 时，我们往往并不直接使用文本及其对应的标量奖励来对 RM 进行训练。因为要对齐人类偏好，RM 训练的偏好数据往往是由人工标注的。但是，由于标注者之间往往也存在价值观差异，数值形式的标量奖励往往会将这些差异放大，从而导致在训练过程中对同样程度的回复奖励不一致，模型难以拟合到正确的标量奖励。因此，我们往往对同一个 completion 下的不同回复进行排名，再将排名转化为奖励。

例如，我们的训练数据往往形如：

```json
{
    "prompt":"如果你打算从商店偷东西，你觉得早上好还是晚上好？",
    "chosen":"这是违法的事情，我不能提供建议",
    "rejected":"考虑晚上的人口贩运和监控摄像头的差别是件好事。夜间时间可能更有利于避免监控摄像头,但晚上的商店雇员会更能看见你。另一方面,由于白天通常不太忙,因此更容易避免被其他人注意到。无论如何,必须密切注意商店雇员和所有顾客的行为。他们也许能够看见你,即使他们不是直接面对你。为了安全起见,重要的是要密切注意商店里的一切事情,而不是不小心。"
}
```

其中，prompt 是用户的问题，chosen 是应该对齐的、符合人类偏好的回答，rejected 是不符合人类偏好的回答。在训练中，prompt 将和 chosen 以及 rejected 分别拼接起来，形成 chosen_example 和 rejected_example，然后分别进入模型通过前向传播输出一个标量奖励。然后模型会通过最大化 chosen_example 和 rejected_example 的标量差异来计算 loss，并进行反向传播完成训练。

值得注意的是，RM 训练使用的模型往往和最后的 LLM 大小不同。例如 OpenAI 使用了 175B 的 LLM 和 6B 的 RM。同时，RM 使用的模型可以是经过 SFT 之后的 LM，也可以是基于偏好数据从头训练的 RM。哪一种更好，至今尚没有定论。

在完成 RM 训练之后，就可以使用 PPO 算法来进行强化学习训练。PPO，Proximal Policy Optimization，近端策略优化算法，是一种经典的 RL 算法。事实上，强化学习训练时也可以使用其他的强化学习算法，但目前 PPO 算法因为成熟、成本较低，还是最适合 RLHF 的算法。

在具体 PPO 训练过程中，会存在四个模型。如图4.5所示，两个 LLM 和两个 RM。两个 LLM 分别是进行微调、参数更新的 actor model 和不进行参数更新的 ref model，均是从 SFT 之后的 LLM 初始化的。两个 RM 分别是进行参数更新的 critic model 和不进行参数更新的 reward model，均是从上一步训练的 RM 初始化的。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/4-figures/2-4.jpg)
图4.5 PPO 训练流程


如上图，使用 PPO 算法的强化学习训练过程如下：

1. 从 SFT 之后的 LLM 初始化两个模型分别作为 Actor Model 和 Ref Model；从训练的 RM 初始化两个模型分别作为 Reward Model 和 Critic Model；
2. 输入一个 Prompt，Actor Model 和 Ref Model 分别就 Prompt 生成回复；
3. Actor Response 和 Ref Response 计算 KL 散度： $r_{KL} = -\theta_{KL}D_{KL}(\pi_{PPO}(y|x)||\pi_{base}(y|x))$ 其中， $\pi_{PPO}(y|x)$ 即为 Actor Model 的输出，而 $\pi_{base}(y|x)$ 即为 Ref Model 的输出， $\theta_{KL}D_{KL}$ 即是计算 KL 散度的方法；
4. Actor Response 分别输入到 Reward Model 和 Critic Model 进行打分，其中，Reward Model 输出的是回复对应的标量奖励，Critic Model 还会输出累加奖励（即从i位置到最后的累积奖励）；
5. 计算的 KL 散度、两个模型的打分均输入到奖励函数中，计算奖励： $loss = -(kl_{ctl} \cdot r_{KL} + \gamma \cdot V_{t+1} - V_{t}) \log P(A_t|V_t)$ ，这里的 $kl_{ctl}$ 是控制 KL 散度对结果影响的权重参数， $\gamma$ 是控制下一个时间（也就是样本）打分对结果影响的权重参数， $V_t$ 是 Critic Model 的打分输出， $A_t$ 则是 Reward Model 的打分输出;
6. 根据奖励函数分别计算出的 actor loss 和 critic loss，更新 Actor Model 的参数和 Critic Model 的参数；注意，Actor Model 和 Critic Model 的参数更新方法是不同的，此处就不再一一赘述了，感兴趣的读者可以深入研究强化学习的相关理论。

在上述过程中，因为要使用到四个模型，显存占用会数倍于 SFT。例如，如果我们 RM 和 LLM 都是用 7B 的体量，PPO 过程中大概需要 240G（4张 80G A100，每张卡占用 60G）显存来进行模型加载。那么，为什么我们需要足足四个模型呢？Actor Model 和 Critic Model 较为容易理解，而之所以我们还需要保持原参数不更新的 Ref Model 和 Reward Model，是为了限制模型的更新不要过于偏离原模型以至于丢失了 Pretrain 和 SFT 赋予的能力。

当然，如此大的资源占用和复杂的训练过程，使 RLHF 成为一个门槛非常高的阶段。也有学者从监督学习的思路出发，提出了 DPO（Direct Preference Optimization，直接偏好优化），可以低门槛平替 RLHF。DPO 的核心思路是，将 RLHF 的强化学习问题转化为监督学习来直接学习人类偏好。DPO 通过使用奖励函数和最优策略间的映射，展示了约束奖励最大化问题完全可以通过单阶段策略训练进行优化，也就是说，通过学习 DPO 所提出的优化目标，可以直接学习人类偏好，而无需再训练 RM 以及进行强化学习。由于直接使用监督学习进行训练，DPO 只需要两个 LLM 即可完成训练，且训练过程相较 PPO 简单很多，是 RLHF 更简单易用的平替版本。DPO 所提出的优化目标为什么能够直接学习人类偏好，作者通过一系列的数学推导完成了证明，感兴趣的读者可以下来进一步阅读，此处就不再赘述了。

接下来，我们将依次实现如何从零开始训练一个 LLM，包括预训练、SFT 和 RLHF。

**参考资料**

[1] Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe. (2022). *Training language models to follow instructions with human feedback.* arXiv preprint arXiv:2203.02155.

[2] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* arXiv preprint arXiv:1810.04805.

[3] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei. (2020). *Scaling Laws for Neural Language Models.* arXiv preprint arXiv:2001.08361.

[4] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre. (2022). *Training Compute-Optimal Large Language Models.* arXiv preprint arXiv:2203.15556.

[5] Qi Wang, Yiyuan Yang, Ji Jiang. (2022). Easy RL: Reinforcement Learning Tutorial . Beijing: Posts & Telecom Press. ISBN: 9787115584700. https://github.com/datawhalechina/easy-rl

[6] Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn. (2024). *Direct Preference Optimization: Your Language Model is Secretly a Reward Model.* arXiv preprint arXiv:2305.18290.

[7] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, Ji-Rong Wen. (2025). *A Survey of Large Language Models.* arXiv preprint arXiv:2303.18223.

## 训练与应用实践

### 第五章 动手搭建大模型



#### 5.1 动手实现一个 LLaMA2 大模型

Meta（原Facebook）于2023年2月发布第一款基于Transformer结构的大型语言模型LLaMA，并于同年7月发布同系列模型LLaMA2。我们在第四章已经学习和了解了LLM，以及如何训练LLM等内容。本小节我们就来学习如何动手实现一个LLaMA2模型。

LLaMA2 模型结构如下图5.1所示：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/5-images/LLama2.png)
图 5.1 LLaMA2结构


##### 5.1.1 定义超参数

首先我们需要定义一些超参数，这些超参数包括模型的大小、层数、头数、词嵌入维度、隐藏层维度等等。这些超参数可以根据实际情况进行调整。

这里我们自定义一个`ModelConfig`类，来存储和记录我们的超参数，这里我们继承了`PretrainedConfig`类，这是`transformers`库中的参数类，我们可以通过继承这个类来方便的使用`transformers`库中的一些功能，也方便在后续导出Hugging Face模型。

```python
from transformers import PretrainedConfig

class ModelConfig(PretrainedConfig):
    model_type = "Tiny-K"
    def __init__(
            self,
            dim: int = 768, # 模型维度
            n_layers: int = 12, # Transformer的层数
            n_heads: int = 16, # 注意力机制的头数
            n_kv_heads: int = 8, # 键值头的数量
            vocab_size: int = 6144, # 词汇表大小
            hidden_dim: int = None, # 隐藏层维度
            multiple_of: int = 64,
            norm_eps: float = 1e-5, # 归一化层的eps
            max_seq_len: int = 512, # 最大序列长度
            dropout: float = 0.0, # dropout概率
            flash_attn: bool = True, # 是否使用Flash Attention
            **kwargs,
    ):
        self.dim = dim
        self.n_layers = n_layers
        self.n_heads = n_heads
        self.n_kv_heads = n_kv_heads
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.multiple_of = multiple_of
        self.norm_eps = norm_eps
        self.max_seq_len = max_seq_len
        self.dropout = dropout
        self.flash_attn = flash_attn
        super().__init__(**kwargs)
```

> 在以下代码中出现 `args` 时，即默认为以上 `ModelConfig` 参数配置。

我们来看一下其中的一些超参数的含义，比如`dim`是模型维度，`n_layers`是Transformer的层数，`n_heads`是注意力机制的头数，`vocab_size`是词汇表大小，`max_seq_len`是输入的最大序列长度等等。上面的代码中也对每一个参数做了详细的注释，在后面的代码中我们会根据这些超参数来构建我们的模型。

##### 5.1.2 构建 RMSNorm

`RMSNorm`可以用如下的数学公式表示：

$$
\text{RMSNorm}(x) = \frac{x}{\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2 + \epsilon}} \cdot \gamma
$$

其中：
- $x_i$ 是输入向量的第 $i$ 个元素
- $\gamma$ 是可学习的缩放参数（对应代码中的 `self.weight`）
- $n$ 是输入向量的维度数量
- $\epsilon$ 是一个小常数，用于数值稳定性（以避免除以零的情况）

这种归一化有助于通过确保权重的规模不会变得过大或过小来稳定学习过程，这在具有许多层的深度学习模型中特别有用。

我们可以通过如下代码实现`RMSNorm`：

```python
class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float):
        super().__init__()
        # eps是为了防止除以0的情况
        self.eps = eps
        # weight是一个可学习的参数，全部初始化为1
        self.weight = nn.Parameter(torch.ones(dim))

    def _norm(self, x):
        # 计算RMSNorm的核心部分
        # x.pow(2).mean(-1, keepdim=True)计算了输入x的平方的均值
        # torch.rsqrt是平方根的倒数，这样就得到了RMSNorm的分母部分，再加上eps防止分母为0
        # 最后乘以x，得到RMSNorm的结果
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        # forward函数是模型的前向传播
        # 首先将输入x转为float类型，然后进行RMSNorm，最后再转回原来的数据类型
        # 最后乘以weight，这是RMSNorm的一个可学习的缩放因子
        output = self._norm(x.float()).type_as(x)
        return output * self.weight
```

并且，我们可以用下面的代码来对`RMSNorm`模块进行测试，可以看到代码最终输出的形状为`torch.Size([1, 50, 768])`，与我们输入的形状一致，说明模块的实现是正确的，归一化并不会改变输入的形状。

```python
norm = RMSNorm(args.dim, args.norm_eps)
x = torch.randn(1, 50, args.dim)
output = norm(x)
print(output.shape)

out:
torch.Size([1, 50, 768])
```

##### 5.1.3 构建 LLaMA2 Attention

在 LLaMA2 模型中，虽然只有 LLaMA2-70B模型使用了分组查询注意力机制（Grouped-Query Attention，GQA），但我们依然选择使用 GQA 来构建我们的 LLaMA Attention 模块，它可以提高模型的效率，并节省一些显存占用。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/5-images/llama2-attention.png)
图 5.2 LLaMA2 Attention 结构


###### 5.1.3.1 repeat_kv

在 LLaMA2 模型中，我们需要将键和值的维度扩展到和查询的维度一样，这样才能进行注意力计算。我们可以通过如下代码实现`repeat_kv`：

```python
def repeat_kv(x: torch.Tensor, n_rep: int) -> torch.Tensor:
    # 获取输入张量的形状：批量大小、序列长度、键/值对头的数量、每个头的维度大小
    bs, slen, n_kv_heads, head_dim = x.shape

    # 如果重复次数为1，则不需要重复，直接返回原始张量
    if n_rep == 1:
        return x

    # 对张量进行扩展和重塑操作以重复键值对
    return (
        x[:, :, :, None, :]  # 在第四个维度（头的维度前）添加一个新的维度
        .expand(bs, slen, n_kv_heads, n_rep, head_dim)  # 将新添加的维度扩展到n_rep大小，实现重复的效果
        .reshape(bs, slen, n_kv_heads * n_rep, head_dim)  # 重新塑形，合并键/值对头的数量和重复次数的维度
    )
```

在上述代码中：

- 首先，获取输入张量的形状：首先，代码通过 x.shape 获取输入张量的形状，包括批量大小（bs）、序列长度（slen）、键/值对头的数量（n_kv_heads）以及每个头的维度大小（head_dim）。

- 然后，检查重复次数：接着，代码检查重复次数 n_rep 是否为1。如果是1，则说明不需要对键和值进行重复，直接返回原始张量 x。

- 最后，扩展和重塑张量：
  - 在第三个维度（即键/值对头的维度）之后添加一个新的维度，形成 `x[:, :, :, None, :]`。
  - 使用 `expand` 方法将新添加的维度扩展到 `n_rep` 大小，实现键/值对的重复效果。
  - 最后，通过 reshape 方法重新塑形，将扩展后的维度合并回键/值对头的数量中，即 `x.reshape(bs, slen, n_kv_heads * n_rep, head_dim)`，这样最终的张量形状就达到了与查询维度一致的效果。

###### 5.1.3.2 旋转嵌入

接着我们来实现旋转嵌入，旋转嵌入是 LLaMA2 模型中的一个重要组件，它可以为注意力机制提供更强的上下文信息，从而提高模型的性能。

首先，我们要构造获得旋转嵌入的实部和虚部的函数：

```python
# 注意：此处的dim应为 dim//n_head，因为我们是对每个head进行旋转嵌入
def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0):
    # torch.arange(0, dim, 2)[: (dim // 2)].float()生成了一个从0开始，步长为2的序列，长度为dim的一半
    # 然后每个元素除以dim，再取theta的倒数，得到频率
    freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim))
    # 生成一个从0到end的序列，长度为end
    t = torch.arange(end, device=freqs.device)
    # 计算外积，得到一个二维矩阵，每一行是t的元素乘以freqs的元素
    freqs = torch.outer(t, freqs).float()
    # 计算频率的余弦值，得到实部
    freqs_cos = torch.cos(freqs)
    # 计算频率的正弦值，得到虚部
    freqs_sin = torch.sin(freqs)
    return freqs_cos, freqs_sin
```

- 计算频率序列：
  - `torch.arange(0, dim, 2)[: (dim // 2)].float()` 生成了一个从0开始，步长为2的序列，其长度为`dim`的一半。
  - 每个元素除以`dim`后取`theta`的倒数，得到一个频率序列 `freqs`。这一步是为了生成适合旋转嵌入的频率。
- 生成时间序列：
  - `t = torch.arange(end, device=freqs.device)` 生成一个从`0`到`end`的序列，长度为`end`。`end`通常是序列的最大长度。
- 计算频率的外积
  - `freqs = torch.outer(t, freqs).float()` 计算时间序列 `t` 和频率序列 `freqs` 的外积，得到一个二维矩阵 `freqs`。每一行是时间序列 `t` 的元素乘以频率序列 `freqs` 的元素。
- 计算实部和虚部
  - `freqs_cos = torch.cos(freqs)` 计算频率矩阵 `freqs` 的余弦值，得到旋转嵌入的实部。
  - `freqs_sin = torch.sin(freqs)` 计算频率矩阵 `freqs` 的正弦值，得到旋转嵌入的虚部。

最终，该函数返回两个矩阵 `freqs_cos` 和 `freqs_sin`，分别表示旋转嵌入的实部和虚部，用于后续的计算。

接着，我们来构造调整张量形状的`reshape_for_broadcast`函数，这个函数的主要目的是调整 `freqs_cis` 的形状，使其在进行广播操作时与 `x` 的维度对齐，从而能够进行正确的张量运算。

```python
def reshape_for_broadcast(freqs_cis: torch.Tensor, x: torch.Tensor):
    # 获取x的维度数
    ndim = x.ndim

    # 断言，确保1在x的维度范围内
    assert 0 <= 1 < ndim

    # 断言，确保freqs_cis的形状与x的第二维和最后一维相同
    assert freqs_cis.shape == (x.shape[1], x.shape[-1])

    # 构造一个新的形状，除了第二维和最后一维，其他维度都为1，这样做是为了能够将freqs_cis与x进行广播操作
    shape = [d if i == 1 or i == ndim - 1 else 1 for i, d in enumerate(x.shape)]

    # 将freqs_cis调整为新的形状，并返回
    return freqs_cis.view(shape)
```

最后，我们可以通过如下代码实现旋转嵌入：

```python
def apply_rotary_emb(
    xq: torch.Tensor,
    xk: torch.Tensor,
    freqs_cos: torch.Tensor,
    freqs_sin: torch.Tensor
) -> Tuple[torch.Tensor, torch.Tensor]:

    # 将查询和键张量转换为浮点数，并重塑形状以分离实部和虚部
    xq_r, xq_i = xq.float().reshape(xq.shape[:-1] + (-1, 2)).unbind(-1)
    xk_r, xk_i = xk.float().reshape(xk.shape[:-1] + (-1, 2)).unbind(-1)

    # 重新塑形频率张量以进行广播
    freqs_cos = reshape_for_broadcast(freqs_cos, xq_r)
    freqs_sin = reshape_for_broadcast(freqs_sin, xq_r)

    # 应用旋转，分别计算旋转后的实部和虚部
    xq_out_r = xq_r * freqs_cos - xq_i * freqs_sin
    xq_out_i = xq_r * freqs_sin + xq_i * freqs_cos
    xk_out_r = xk_r * freqs_cos - xk_i * freqs_sin
    xk_out_i = xk_r * freqs_sin + xk_i * freqs_cos

    # 将最后两个维度合并，并还原为原始张量的形状
    xq_out = torch.stack([xq_out_r, xq_out_i], dim=-1).flatten(3)
    xk_out = torch.stack([xk_out_r, xk_out_i], dim=-1).flatten(3)

    return xq_out.type_as(xq), xk_out.type_as(xk)
```

这里我们给出可以测试`apply_rotary_emb`函数的代码，大家也可以尝试在代码中添加断点，来查看每一步的计算结果。

```python
xq = torch.randn(1, 50, 6, 48) # bs, seq_len, dim//n_head, n_head_dim
xk = torch.randn(1, 50, 6, 48) # bs, seq_len, dim//n_head, n_head_dim

# 使用 precompute_freqs_cis 函数获取 sin和cos
cos, sin = precompute_freqs_cis(288//6, 50)
print(cos.shape, sin.shape)
xq_out, xk_out = apply_rotary_emb(xq, xk, cos, sin)

xq_out.shape, xk_out.shape
```

OUT:
```
torch.Size([50, 24]) torch.Size([50, 24])

(torch.Size([1, 50, 6, 48]), torch.Size([1, 50, 6, 48]))
```

###### 5.1.3.3 组装 LLaMA2 Attention

在上面我们已经完成了旋转嵌入的实现，接下来我们就可以构建 LLaMA2 Attention 模块了。

```python
class Attention(nn.Module):
    def __init__(self, args: ModelConfig):
        super().__init__()
        # 根据是否指定n_kv_heads，确定用于键（key）和值（value）的头的数量。
        self.n_kv_heads = args.n_heads if args.n_kv_heads is None else args.n_kv_heads
        # 确保总头数可以被键值头数整除。
        assert args.n_heads % self.n_kv_heads == 0

        # 模型并行处理大小，默认为1。
        model_parallel_size = 1
        # 本地计算头数，等于总头数除以模型并行处理大小。
        self.n_local_heads = args.n_heads // model_parallel_size
        # 本地键值头数，等于键值头数除以模型并行处理大小。
        self.n_local_kv_heads = self.n_kv_heads // model_parallel_size
        # 重复次数，用于扩展键和值的尺寸。
        self.n_rep = self.n_local_heads // self.n_local_kv_heads
        # 每个头的维度，等于模型维度除以头的总数。
        self.head_dim = args.dim // args.n_heads

        # 定义权重矩阵。
        self.wq = nn.Linear(args.dim, args.n_heads * self.head_dim, bias=False)
        self.wk = nn.Linear(args.dim, self.n_kv_heads * self.head_dim, bias=False)
        self.wv = nn.Linear(args.dim, self.n_kv_heads * self.head_dim, bias=False)
        # 输出权重矩阵。
        self.wo = nn.Linear(args.n_heads * self.head_dim, args.dim, bias=False)

        # 定义dropout。
        self.attn_dropout = nn.Dropout(args.dropout)
        self.resid_dropout = nn.Dropout(args.dropout)
        # 保存dropout概率。
        self.dropout = args.dropout

        # 检查是否使用Flash Attention（需要PyTorch >= 2.0）。
        self.flash = hasattr(torch.nn.functional, 'scaled_dot_product_attention')
        if not self.flash:
            # 若不支持Flash Attention，则使用手动实现的注意力机制，并设置mask。
            print("WARNING: using slow attention. Flash Attention requires PyTorch >= 2.0")
            # 创建一个上三角矩阵，用于遮蔽未来信息。
            mask = torch.full((1, 1, args.max_seq_len, args.max_seq_len), float("-inf"))
            mask = torch.triu(mask, diagonal=1)
            # 注册为模型的缓冲区
            self.register_buffer("mask", mask)

    def forward(self, x: torch.Tensor, freqs_cos: torch.Tensor, freqs_sin: torch.Tensor):
        # 获取批次大小和序列长度，[batch_size, seq_len, dim]
        bsz, seqlen, _ = x.shape

        # 计算查询（Q）、键（K）、值（V）。
        xq, xk, xv = self.wq(x), self.wk(x), self.wv(x)
        # 调整形状以适应头的维度。
        xq = xq.view(bsz, seqlen, self.n_local_heads, self.head_dim)
        xk = xk.view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
        xv = xv.view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)

        # 应用旋转位置嵌入（RoPE）。
        xq, xk = apply_rotary_emb(xq, xk, freqs_cos, freqs_sin)

        # 对键和值进行扩展以适应重复次数。
        xk = repeat_kv(xk, self.n_rep)
        xv = repeat_kv(xv, self.n_rep)

        # 将头作为批次维度处理。
        xq = xq.transpose(1, 2)
        xk = xk.transpose(1, 2)
        xv = xv.transpose(1, 2)

        # 根据是否支持Flash Attention，选择实现方式。
        if self.flash:
            # 使用Flash Attention。
            output = torch.nn.functional.scaled_dot_product_attention(xq, xk, xv, attn_mask=None, dropout_p=self.dropout if self.training else 0.0, is_causal=True)
        else:
            # 使用手动实现的注意力机制。
            scores = torch.matmul(xq, xk.transpose(2, 3)) / math.sqrt(self.head_dim)
            assert hasattr(self, 'mask')
            scores = scores + self.mask[:, :, :seqlen, :seqlen]
            scores = F.softmax(scores.float(), dim=-1).type_as(xq)
            scores = self.attn_dropout(scores)
            output = torch.matmul(scores, xv)

        # 恢复时间维度并合并头。
        output = output.transpose(1, 2).contiguous().view(bsz, seqlen, -1)

        # 最终投影回残差流。
        output = self.wo(output)
        output = self.resid_dropout(output)
        return output
```

同样大家可以使用下面的代码来对注意力模块进行测试，可以看到代码最终输出的形状为`torch.Size([1, 50, 768])`，与我们输入的形状一致，说明模块的实现是正确的。

```python
# 创建Attention实例
attention_model = Attention(args)

# 模拟输入数据
batch_size = 1
seq_len = 50  # 假设实际使用的序列长度为50
dim = args.dim
x = torch.rand(batch_size, seq_len, dim)  # 随机生成输入张量
# freqs_cos = torch.rand(seq_len, dim // 2)  # 模拟cos频率，用于RoPE
# freqs_sin = torch.rand(seq_len, dim // 2)  # 模拟sin频率，用于RoPE

freqs_cos, freqs_sin = precompute_freqs_cis(dim//args.n_heads, seq_len)

# 运行Attention模型
output = attention_model(x, freqs_cos, freqs_sin)

# attention出来之后的形状 依然是[batch_size, seq_len, dim]
print("Output shape:", output.shape)
```

OUT:
```
Output shape: torch.Size([1, 50, 768])
```

##### 5.1.4 构建 LLaMA2 MLP模块

相对于前面我们实现的LLaMA2 Attention模块，LLaMA2 MLP模块的实现要简单一些。我们可以通过如下代码实现`MLP`：

```python
class MLP(nn.Module):
    def __init__(self, dim: int, hidden_dim: int, multiple_of: int, dropout: float):
        super().__init__()
        # 如果没有指定隐藏层的维度，我们将其设置为输入维度的4倍
        # 然后将其减少到2/3，最后确保它是multiple_of的倍数
        if hidden_dim is None:
            hidden_dim = 4 * dim
            hidden_dim = int(2 * hidden_dim / 3)
            hidden_dim = multiple_of * ((hidden_dim + multiple_of - 1) // multiple_of)
        # 定义第一层线性变换，从输入维度到隐藏维度
        self.w1 = nn.Linear(dim, hidden_dim, bias=False)
        # 定义第二层线性变换，从隐藏维度到输入维度
        self.w2 = nn.Linear(hidden_dim, dim, bias=False)
        # 定义第三层线性变换，从输入维度到隐藏维度
        self.w3 = nn.Linear(dim, hidden_dim, bias=False)
        # 定义dropout层，用于防止过拟合
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        # 前向传播函数
        # 首先，输入x通过第一层线性变换和SILU激活函数
        # 然后，结果乘以输入x通过第三层线性变换的结果
        # 最后，通过第二层线性变换和dropout层
        return self.dropout(self.w2(F.silu(self.w1(x)) * self.w3(x)))
```

我们着重观察一下`forward`函数的实现，首先，输入 `x` 通过第一层线性变换 `self.w1` 和 `SILU` 激活函数，然后，结果乘以输入 `x` 通过第三层线性变换 `self.w3` 的结果，最后，通过第二层线性变换 `self.w2` 和 `dropout` 层，得到最终输出。

同样大家可以使用下面的代码来对`LLaMAMLP`模块进行测试，可以看到代码最终输出的形状为`torch.Size([1, 50, 768])`，与我们输入的形状一致，说明模块的实现是正确的。

```python
# 创建MLP实例
mlp = MLP(args.dim, args.hidden_dim, args.multiple_of, args.dropout)
# 随机生成数据
x = torch.randn(1, 50, args.dim)
# 运行MLP模型
output = mlp(x)
print(output.shape)
```

OUT:
```
torch.Size([1, 50, 768])
```

##### 5.1.5 LLaMA2 Decoder Layer

到这里，我们已经实现了`LLaMA2`模型的`Attention`模块和`MLP`模块，接下来我们就可以构建`LLaMA2`的`Decoder Layer`了。

```python
class DecoderLayer(nn.Module):
    def __init__(self, layer_id: int, args: ModelConfig):
        super().__init__()
        # 定义多头注意力的头数
        self.n_heads = args.n_heads
        # 定义输入维度
        self.dim = args.dim
        # 定义每个头的维度，等于输入维度除以头数
        self.head_dim = args.dim // args.n_heads
        # 定义LLaMA2Attention对象，用于进行多头注意力计算
        self.attention = Attention(args)
        # 定义LLaMAMLP对象，用于进行前馈神经网络计算
        self.feed_forward = MLP(
            dim=args.dim,
            hidden_dim=args.hidden_dim,
            multiple_of=args.multiple_of,
            dropout=args.dropout,
        )
        # 定义层的ID
        self.layer_id = layer_id
        # 定义注意力计算的归一化层
        self.attention_norm = RMSNorm(args.dim, eps=args.norm_eps)
        # 定义前馈神经网络计算的归一化层
        self.ffn_norm = RMSNorm(args.dim, eps=args.norm_eps)

    def forward(self, x, freqs_cos, freqs_sin):
        # 前向传播函数
        # 首先，输入x经过注意力归一化层，然后进行注意力计算，结果与输入x相加得到h
        # 然后，h经过前馈神经网络归一化层，然后进行前馈神经网络计算，结果与h相加得到输出
        h = x + self.attention.forward(self.attention_norm(x), freqs_cos, freqs_sin)
        out = h + self.feed_forward.forward(self.ffn_norm(h))
        return out
```

`DecoderLayer`就是把我们上面完成的`Attention`模块和`MLP`模块组合在一起，实现了一个完整的`Transformer`模块。

同样大家可以使用下面的代码来对`DecoderLayer`模块进行测试，可以看到代码最终输出的形状为`torch.Size([1, 50, 768])`，与我们输入的形状一致，说明模块的实现是正确的。

```python
# 创建LLaMADecoderLayer实例
decoderlayer = DecoderLayer(0, args)

# 模拟输入数据
dim = args.dim
seq_len = 50

x = torch.randn(1, seq_len, dim) # [bs, seq_len, dim]

freqs_cos, freqs_sin = precompute_freqs_cis(dim//args.n_heads, seq_len)

out = decoderlayer(x, freqs_cos, freqs_sin)

print(out.shape) # 形状和输入的x一样 [batch_size, seq_len, dim]
```

OUT:
```
torch.Size([1, 50, 768])
```

##### 5.1.6 构建 LLaMA2 模型

好了，我们已经完了上述所有的模块的实现，接下来就是激动人心的时刻，我们可以构建`LLaMA2`模型了。，`LLaMA2`模型就是将`DecoderLayer`模块堆叠起来，构成一个完整的`Transformer`模型。

```python
from transformers import PreTrainedModel
from transformers.modeling_outputs import CausalLMOutputWithPast
from typing import Optional
import math

class Transformer(PreTrainedModel):
    config_class = ModelConfig  # 配置类
    last_loss: Optional[torch.Tensor] # 记录最后一次计算的损失

    def __init__(self, args: ModelConfig = None):
        super().__init__(args)
        # 初始化模型参数
        self.args = args
        # 词汇表大小
        self.vocab_size = args.vocab_size
        # 层数
        self.n_layers = args.n_layers

        # 词嵌入层
        self.tok_embeddings = nn.Embedding(args.vocab_size, args.dim)
        # Dropout层
        self.dropout = nn.Dropout(args.dropout)
        # Decoder层
        self.layers = torch.nn.ModuleList()
        for layer_id in range(args.n_layers):
            self.layers.append(DecoderLayer(layer_id, args))
        # 归一化层
        self.norm = RMSNorm(args.dim, eps=args.norm_eps)
        # 输出层
        self.output = nn.Linear(args.dim, args.vocab_size, bias=False)

        # 将词嵌入层的权重与输出层的权重共享
        self.tok_embeddings.weight = self.output.weight

        # 预计算相对位置嵌入的频率
        freqs_cos, freqs_sin = precompute_freqs_cis(self.args.dim // self.args.n_heads, self.args.max_seq_len)
        self.register_buffer("freqs_cos", freqs_cos, persistent=False)
        self.register_buffer("freqs_sin", freqs_sin, persistent=False)

        # 初始化所有权重
        self.apply(self._init_weights)
        # 对残差投影进行特殊的缩放初始化
        for pn, p in self.named_parameters():
            if pn.endswith('w3.weight') or pn.endswith('wo.weight'):
                torch.nn.init.normal_(p, mean=0.0, std=0.02/math.sqrt(2 * args.n_layers))

        # 初始化最后一次前向传播的损失属性
        self.last_loss = None
        self.OUT = CausalLMOutputWithPast()  # 输出容器
        self._no_split_modules = [name for name, _ in self.named_modules()]  # 不分割的模块列表

    def _init_weights(self, module):
        # 初始化权重的函数
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self, tokens: torch.Tensor, targets: Optional[torch.Tensor] = None, **kwargs) -> torch.Tensor:
        """
        - tokens: Optional[torch.Tensor], 输入 token 张量。
        - targets: Optional[torch.Tensor], 目标 token 张量。
        - kv_cache: bool, 是否使用键值缓存。
        - kwargs: 其他关键字参数。

        - self.OUT: CausalLMOutputWithPast, 包含 logits 和损失。
        """

        if 'input_ids' in kwargs:
            tokens = kwargs['input_ids']
        if 'labels' in kwargs:
            targets = kwargs['labels']

        # 前向传播函数
        _bsz, seqlen = tokens.shape
        # 通过词嵌入层和Dropout层
        h = self.tok_embeddings(tokens)
        h = self.dropout(h)
        # 获取相对位置嵌入的频率
        freqs_cos = self.freqs_cos[:seqlen]
        freqs_sin = self.freqs_sin[:seqlen]

        # 通过Decoder层
        for layer in self.layers:
            h = layer(h, freqs_cos, freqs_sin)
        # 通过归一化层
        h = self.norm(h)

        if targets is not None:
            # 如果给定了目标，计算损失
            logits = self.output(h)
            self.last_loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=0, reduction='none')
        else:
            # 推理时的小优化：只对最后一个位置的输出进行前向传播
            logits = self.output(h[:, [-1], :])
            self.last_loss = None

        # 设置输出
        self.OUT.__setitem__('logits', logits)
        self.OUT.__setitem__('last_loss', self.last_loss)
        return self.OUT


    @torch.inference_mode()
    def generate(self, idx, stop_id=None, max_new_tokens=256, temperature=1.0, top_k=None):
        """
        给定输入序列 idx（形状为 (bz,seq_len) 的长整型张量），通过多次生成新 token 来完成序列。
        在 model.eval() 模式下运行。效率较低的采样版本，没有使用键k/v cache。
        """
        index = idx.shape[1]
        for _ in range(max_new_tokens):
            # 如果序列上下文过长，截断它到最大长度
            idx_cond = idx if idx.size(1) <= self.args.max_seq_len else idx[:, -self.args.max_seq_len:]

            # 前向传播获取序列中最后一个位置的 logits
            logits = self(idx_cond).logits
            logits = logits[:, -1, :] # 只保留最后一个时间步的输出

            if temperature == 0.0:
                # 选择最有可能的索引
                _, idx_next = torch.topk(logits, k=1, dim=-1)
            else:
                # 缩放 logits 并应用 softmax
                logits = logits / temperature
                if top_k is not None:
                    v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                    logits[logits < v[:, [-1]]] = -float('Inf')
                probs = F.softmax(logits, dim=-1)
                idx_next = torch.multinomial(probs, num_samples=1)


            if idx_next == stop_id:
                break

            # 将采样的索引添加到序列中并继续
            idx = torch.cat((idx, idx_next), dim=1)

        return idx[:, index:] # 只返回生成的token
```

同样大家可以使用下面的代码来对`Transformer`模块进行测试，可以看到代码最终输出的形状为`torch.Size([1, 1, 6144])`，与我们输入的形状一致，说明模块的实现是正确的。

```python
# LLaMA2Model.forward 接受两个参数，tokens和targets，其中tokens是输入的张量, 应为int类型
x = torch.randint(0, 6144, (1, 50)) # [bs, seq_len]
# 实例化LLaMA2Model
model = Transformer(args=args)
# 计算model的全部参数
num_params = sum(p.numel() for p in model.parameters())
print('Number of parameters:', num_params)

out = model(x)
print(out.logits.shape) # [batch_size, 1, vocab_size]
```

OUT:
```
Number of parameters: 82594560
torch.Size([1, 1, 6144])
```

#### 5.2 训练 Tokenizer

在自然语言处理 (NLP) 中，Tokenizer 是一种将文本分解为较小单位（称为 token）的工具。这些 token 可以是词、子词、字符，甚至是特定的符号。Tokenization 是 NLP 中的第一步，直接影响后续处理和分析的效果。不同类型的 tokenizer 适用于不同的应用场景，以下是几种常见的 tokenizer 及其特点。

##### 5.2.1 Word-based Tokenizer

**Word-based Tokenizer** 是最简单和直观的一种分词方法。它将文本按空格和标点符号分割成单词。这种方法的优点在于其简单和直接，易于实现，且与人类对语言的直觉相符。然而，它也存在一些明显的缺点，如无法处理未登录词（OOV，out-of-vocabulary）和罕见词，对复合词（如“New York”）或缩略词（如“don't”）的处理也不够精细。此外，Word-based Tokenizer 在处理不同语言时也会遇到挑战，因为一些语言（如中文、日文）没有显式的单词分隔符。

示例：
```
Input: "Hello, world! There is Datawhale."
Output: ["Hello", ",", "world", "!", "There", "is", "Datawhale", "."]
```

在这个例子中，输入的句子被分割成一系列单词和标点符号，每个单词或标点符号都作为一个独立的 token。

##### 5.2.2 Character-based Tokenizer

**Character-based Tokenizer** 将文本中的每个字符视为一个独立的 token。这种方法能非常精细地处理文本，适用于处理拼写错误、未登录词或新词。由于每个字符都是一个独立的 token，因此这种方法可以捕捉到非常细微的语言特征。这对于一些特定的应用场景，如生成式任务或需要处理大量未登录词的任务，特别有用。但是，这种方法也会导致 token 序列变得非常长，增加了模型的计算复杂度和训练时间。此外，字符级的分割可能会丢失一些词级别的语义信息，使得模型难以理解上下文。

示例：
```
Input: "Hello"
Output: ["H", "e", "l", "l", "o"]
```

在这个例子中，单词“Hello”被分割成单个字符，每个字符作为一个独立的 token。这种方法能够处理任何语言和字符集，具有极大的灵活性。

##### 5.2.3 Subword Tokenizer

**Subword Tokenizer** 介于词和字符之间，能够更好地平衡分词的细粒度和处理未登录词的能力。Subword Tokenizer 的关键思想是将文本分割成比单词更小的单位，但又比字符更大，这样既能处理未知词，又能保持一定的语义信息。常见的子词分词方法包括 BPE、WordPiece 和 Unigram。

###### （1）Byte Pair Encoding (BPE)

**BPE** 是一种基于统计方法，通过反复合并频率最高的字符或字符序列对来生成子词词典。这种方法的优点在于其简单和高效，能够有效地处理未知词和罕见词，同时保持较低的词典大小。BPE 的合并过程是自底向上的，逐步将频率最高的字符对合并成新的子词，直到达到预定的词典大小或不再有高频的字符对。

示例：
```
Input: "lower"
Output: ["low", "er"]

Input: "newest"
Output: ["new", "est"]
```

在这个例子中，单词“lower”被分割成子词“low”和“er”，而“newest”被分割成“new”和“est”。这种方法有效地处理了词干和词缀，保持了单词的基本语义结构。

###### （2）WordPiece

**WordPiece** 是另一种基于子词的分词方法，最初用于谷歌的 BERT 模型。与 BPE 类似，WordPiece 通过最大化子词序列的似然函数来生成词典，但在合并子词时更注重语言模型的优化。WordPiece 会优先选择能够最大化整体句子概率的子词，使得分词结果在语言模型中具有更高的概率。

示例：
```
Input: "unhappiness"
Output: ["un", "##happiness"]
```

在这个例子中，单词“unhappiness”被分割成子词“un”和“##happiness”，其中“##”表示这是一个后缀子词。通过这种方式，WordPiece 能够更好地处理复合词和派生词，保留更多的语义信息。

###### （3）Unigram

**Unigram** 分词方法基于概率模型，通过选择具有最高概率的子词来分割文本。Unigram 词典是通过训练语言模型生成的，可以处理多种语言和不同类型的文本。Unigram 模型会为每个子词分配一个概率，然后根据这些概率进行最优分割。

示例：
```
Input: "unhappiness"
Output: ["un", "happiness"]

Input: "newest"
Output: ["new", "est"]
```

在这个例子中，单词“unhappiness”被分割成子词“un”和“happiness”，而“newest”被分割成“new”和“est”。这种方法通过概率模型有效地处理了子词分割，使得分割结果更符合语言使用习惯。

每种 Tokenizer 方法都有其特定的应用场景和优缺点，选择适合的 Tokenizer 对于自然语言处理任务的成功至关重要。

##### 5.2.4 训练一个 Tokenizer

这里我们选择使用 BPE 算法来训练一个 Subword Tokenizer。BPE 是一种简单而有效的分词方法，能够处理未登录词和罕见词，同时保持较小的词典大小。我们将使用 Hugging Face 的 `tokenizers` 库来训练一个 BPE Tokenizer。


###### Step 1: 安装和导入依赖库

首先，我们需要安装 `tokenizers` 库，除此之外还需要安装 `datasets` 和 `transformers` 库，用于加载训练数据和加载训练完成后的 Tokenizer。

```bash
pip install tokenizers datasets transformers
```

然后，导入所需的库。

```python
import random
import json
import os
from transformers import AutoTokenizer, PreTrainedTokenizerFast
from tokenizers import (
    decoders,
    models,
    pre_tokenizers,
    trainers,
    Tokenizer,
)
from tokenizers.normalizers import NFKC
from typing import Generator
```

###### Step 2: 加载训练数据

这里我们使用与预训练相同的数据集（出门问问序列猴子开源数据集）训练tokenizer，可使用`code/download_dataset.sh` 和 `code/deal_dataset.py` 下载和预处理数据集。

> 注：由于数据集过大，可能会导致在训练过程中内存不足。因为本项目为学习目的，建议学习者手动分割小部分数据集用于训练验证，笔者也在 Github 仓库中存放了训练好的 tokenizer，可以直接使用。

```python
def read_texts_from_jsonl(file_path: str) -> Generator[str, None, None]:
    """读取JSONL文件并安全提取文本数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                if 'text' not in data:
                    raise KeyError(f"Missing 'text' field in line {line_num}")
                yield data['text']
            except json.JSONDecodeError:
                print(f"Error decoding JSON in line {line_num}")
                continue
            except KeyError as e:
                print(e)
                continue
```

###### Step 3: 创建配置文件

在训练 BPE Tokenizer 之前，我们需要创建一个完整的 `Tokenizer` 配置文件，包括 `tokenizer_config.json` 和 `special_tokens_map.json`。这些配置文件定义了 `Tokenizer` 的参数和特殊标记，用于训练和加载 `Tokenizer`。此处的`chat_template`我们与`Qwen2.5`模型保持一致。

```python
def create_tokenizer_config(save_dir: str) -> None:
    """创建完整的tokenizer配置文件"""
    config = {
        "add_bos_token": False,
        "add_eos_token": False,
        "add_prefix_space": False,
        "bos_token": "<|im_start|>",
        "eos_token": "<|im_end|>",
        "pad_token": "<|im_end|>",
        "unk_token": "<unk>",
        "model_max_length": 1000000000000000019884624838656,
        "clean_up_tokenization_spaces": False,
        "tokenizer_class": "PreTrainedTokenizerFast",
        "chat_template": (
            "{% for message in messages %}"
            "{% if message['role'] == 'system' %}"
            "<|im_start|>system\n{{ message['content'] }}<|im_end|>\n"
            "{% elif message['role'] == 'user' %}"
            "<|im_start|>user\n{{ message['content'] }}<|im_end|>\n"
            "{% elif message['role'] == 'assistant' %}"
            "<|im_start|>assistant\n{{ message['content'] }}<|im_end|>\n"
            "{% endif %}"
            "{% endfor %}"
            "{% if add_generation_prompt %}"
            "{{ '<|im_start|>assistant\n' }}"
            "{% endif %}"
        )
    }

    # 保存主配置文件
    with open(os.path.join(save_dir, "tokenizer_config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

    # 创建special_tokens_map.json
    special_tokens_map = {
        "bos_token": "<|im_start|>",
        "eos_token": "<|im_end|>",
        "unk_token": "<unk>",
        "pad_token": "<|im_end|>",
        "additional_special_tokens": ["<s>", "</s>"]
    }
    with open(os.path.join(save_dir, "special_tokens_map.json"), "w", encoding="utf-8") as f:
        json.dump(special_tokens_map, f, ensure_ascii=False, indent=4)
```

###### Step 4: 训练 BPE Tokenizer

在训练 BPE Tokenizer 之前，我们需要定义一个训练函数，用于训练 Tokenizer 并保存训练好的 Tokenizer 文件。这里我们使用 `tokenizers` 库中的 `Tokenizer` 类来训练 BPE Tokenizer。

可以看到我们在训练 Tokenizer 时，配置了一些特殊的 token，如 `<unk>`、`<s>`、`</s>`、`<|im_start|>` 和 `<|im_end|>`。这些 token 用于标记未知词、句子的开始和结束，以及对话的开始和结束。这些特殊 token 可以帮助模型更好地理解文本数据，提高模型的泛化能力和效果。

```python
def train_tokenizer(data_path: str, save_dir: str, vocab_size: int = 8192) -> None:
    """训练并保存自定义tokenizer"""
    os.makedirs(save_dir, exist_ok=True)

    # 初始化tokenizer
    tokenizer = Tokenizer(models.BPE(unk_token="<unk>"))
    tokenizer.normalizer = NFKC()  # 添加文本规范化
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tokenizer.decoder = decoders.ByteLevel()

    # 配置特殊token
    special_tokens = [
        "<unk>",
        "<s>",
        "</s>",
        "<|im_start|>",
        "<|im_end|>"
    ]

    # 配置训练器
    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=special_tokens,
        min_frequency=2,  # 提高低频词过滤
        show_progress=True,
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet()
    )

    # 训练tokenizer
    print(f"Training tokenizer with data from {data_path}")
    texts = read_texts_from_jsonl(data_path)
    tokenizer.train_from_iterator(texts, trainer=trainer, length=os.path.getsize(data_path))

    # 验证特殊token映射
    try:
        assert tokenizer.token_to_id("<unk>") == 0
        assert tokenizer.token_to_id("<s>") == 1
        assert tokenizer.token_to_id("</s>") == 2
        assert tokenizer.token_to_id("<|im_start|>") == 3
        assert tokenizer.token_to_id("<|im_end|>") == 4
    except AssertionError as e:
        print("Special tokens mapping error:", e)
        raise

    # 保存tokenizer文件
    tokenizer.save(os.path.join(save_dir, "tokenizer.json"))

    # 创建配置文件
    create_tokenizer_config(save_dir)
    print(f"Tokenizer saved to {save_dir}")
```


###### Step 5: 使用训练好的 Tokenizer

我们可以使用训练好的 Tokenizer 来处理文本数据，如编码、解码、生成对话等。下面是一个简单的示例，展示了如何使用训练好的 Tokenizer 来处理文本数据。

```python
def eval_tokenizer(tokenizer_path: str) -> None:
    """评估tokenizer功能"""
    try:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    except Exception as e:
        print(f"Error loading tokenizer: {e}")
        return

    # 测试基本属性
    print("\n=== Tokenizer基本信息 ===")
    print(f"Vocab size: {len(tokenizer)}")
    print(f"Special tokens: {tokenizer.all_special_tokens}")
    print(f"Special token IDs: {tokenizer.all_special_ids}")

    # 测试聊天模板
    messages = [
        {"role": "system", "content": "你是一个AI助手。"},
        {"role": "user", "content": "How are you?"},
        {"role": "assistant", "content": "I'm fine, thank you. and you?"},
        {"role": "user", "content": "I'm good too."},
        {"role": "assistant", "content": "That's great to hear!"},
    ]

    print("\n=== 聊天模板测试 ===")
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        # add_generation_prompt=True
    )
    print("Generated prompt:\n", prompt, sep="")

    # 测试编码解码
    print("\n=== 编码解码测试 ===")
    encoded = tokenizer(prompt, truncation=True, max_length=256)
    decoded = tokenizer.decode(encoded["input_ids"], skip_special_tokens=False)
    print("Decoded text matches original:", decoded == prompt)

    # 测试特殊token处理
    print("\n=== 特殊token处理 ===")
    test_text = "<|im_start|>user\nHello<|im_end|>"
    encoded = tokenizer(test_text).input_ids
    decoded = tokenizer.decode(encoded)
    print(f"Original: {test_text}")
    print(f"Decoded:  {decoded}")
    print("Special tokens preserved:", decoded == test_text)
```

```python
eval_tokenizer('your tokenizer path')
```

OUT:
```
=== Tokenizer基本信息 ===
Vocab size: 6144
Special tokens: ['<|im_start|>', '<|im_end|>', '<unk>', '<s>', '</s>']
Special token IDs: [3, 4, 0, 1, 2]

=== 聊天模板测试 ===
Generated prompt:
<|im_start|>system
你是一个AI助手。<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
I'm fine, thank you. and you?<|im_end|>
<|im_start|>user
I'm good too.<|im_end|>
<|im_start|>assistant
That's great to hear!<|im_end|>


=== 编码解码测试 ===
Decoded text matches original: False

=== 特殊token处理 ===
Original: <|im_start|>user
Hello<|im_end|>
Decoded:  <|im_start|> user
Hello<|im_end|>
Special tokens preserved: False
```

#### 5.3 预训练一个小型LLM

在前面的章节中，我们熟悉了各种大模型的模型结构，以及如如何训练Tokenizer。在本节中，我们将动手训练一个八千万参数的LLM。

##### 5.3.1 数据下载

首先，我们需要下载预训练数据集。在这里，我们使用两个开源的数据集，包含了大量的中文对话数据，可以用于训练对话生成模型。

- 出门问问序列猴子开源数据集：出门问问序列猴子通用文本数据集由来自网页、百科、博客、问答、开源代码、书籍、报刊、专利、教材、考题等多种公开可获取的数据进行汇总清洗之后而形成的大语言模型预训练语料。总量大概在 10B Token。

- BelleGroup：350万条中文对话数据集，包含了人机对话、人人对话、人物对话等多种对话数据，可以用于训练对话生成模型。


```python
# 下载预训练数据集
os.system("modelscope download --dataset ddzhu123/seq-monkey mobvoi_seq_monkey_general_open_corpus.jsonl.tar.bz2 --local_dir your_local_dir")
# 解压预训练数据集
os.system("tar -xvf your_local_dir/mobvoi_seq_monkey_general_open_corpus.jsonl.tar.bz2")

# 下载SFT数据集
os.system(f'huggingface-cli download --repo-type dataset --resume-download BelleGroup/train_3.5M_CN --local-dir BelleGroup')



# 1 处理预训练数据
def split_text(text, chunk_size=512):
    """将文本按指定长度切分成块"""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

input_file = 'mobvoi_seq_monkey_general_open_corpus.jsonl'

with open('seq_monkey_datawhale.jsonl', 'a', encoding='utf-8') as pretrain:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for line in tqdm(data, desc=f"Processing lines in {input_file}", leave=False):  # 添加行级别的进度条
            line = json.loads(line)
            text = line['text']
            chunks = split_text(text)
            for chunk in chunks:
                pretrain.write(json.dumps({'text': chunk}, ensure_ascii=False) + '\n')

# 2 处理SFT数据

def convert_message(data):
    """
    将原始数据转换为标准格式
    """
    message = [
        {"role": "system", "content": "你是一个AI助手"},
    ]
    for item in data:
        if item['from'] == 'human':
            message.append({'role': 'user', 'content': item['value']})
        elif item['from'] == 'assistant':
            message.append({'role': 'assistant', 'content': item['value']})
    return message

with open('BelleGroup_sft.jsonl', 'a', encoding='utf-8') as sft:
    with open('BelleGroup/train_3.5M_CN.json', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for item in tqdm(data, desc="Processing", unit="lines"):
            item = json.loads(item)
            message = convert_message(item['conversations'])
            sft.write(json.dumps(message, ensure_ascii=False) + '\n')
```

##### 5.3.2 训练 Tokenizer

首先，我们需要为文本处理训练一个Tokenizer。Tokenizer的作用是将文本转换为数字序列，以便模型能够理解和处理。我们使用的数据集是 [出门问问序列猴子开源数据集](https://www.modelscope.cn/datasets/ddzhu123/seq-monkey/files) ，这个数据集包含了大量的中文文本数据，可以用于训练Tokenizer。

> 注：由于数据集较大，如果大家在自己本地电脑训练的话进度比较慢，所以在这里我们提供了一个已经训练好的Tokenizer，大家可以直接使用。如果大家想要自己训练的话，可以参考下面的代码。

```bash
python code/train_tokenizer.py
```

```python
import random
import json
import os
from transformers import AutoTokenizer, PreTrainedTokenizerFast
from tokenizers import (
    decoders,
    models,
    pre_tokenizers,
    trainers,
    Tokenizer,
)
from tokenizers.normalizers import NFKC
from typing import Generator

random.seed(42)

def read_texts_from_jsonl(file_path: str) -> Generator[str, None, None]:
    """读取JSONL文件并安全提取文本数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                if 'text' not in data:
                    raise KeyError(f"Missing 'text' field in line {line_num}")
                yield data['text']
            except json.JSONDecodeError:
                print(f"Error decoding JSON in line {line_num}")
                continue
            except KeyError as e:
                print(e)
                continue

def create_tokenizer_config(save_dir: str) -> None:
    """创建完整的tokenizer配置文件"""
    config = {
        "add_bos_token": False,
        "add_eos_token": False,
        "add_prefix_space": True,
        "bos_token": "<|im_start|>",
        "eos_token": "<|im_end|>",
        "pad_token": "<|im_end|>",
        "unk_token": "<unk>",
        "model_max_length": 1000000000000000019884624838656,
        "clean_up_tokenization_spaces": False,
        "tokenizer_class": "PreTrainedTokenizerFast",
        "chat_template": (
            "{% for message in messages %}"
            "{% if message['role'] == 'system' %}"
            "<|im_start|>system\n{{ message['content'] }}<|im_end|>\n"
            "{% elif message['role'] == 'user' %}"
            "<|im_start|>user\n{{ message['content'] }}<|im_end|>\n"
            "{% elif message['role'] == 'assistant' %}"
            "<|im_start|>assistant\n{{ message['content'] }}<|im_end|>\n"
            "{% endif %}"
            "{% endfor %}"
            "{% if add_generation_prompt %}"
            "{{ '<|im_start|>assistant\n' }}"
            "{% endif %}"
        )
    }

    # 保存主配置文件
    with open(os.path.join(save_dir, "tokenizer_config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

    # 创建special_tokens_map.json
    special_tokens_map = {
        "bos_token": "<|im_start|>",
        "eos_token": "<|im_end|>",
        "unk_token": "<unk>",
        "pad_token": "<|im_end|>",
        "additional_special_tokens": ["<s>", "</s>"]
    }
    with open(os.path.join(save_dir, "special_tokens_map.json"), "w", encoding="utf-8") as f:
        json.dump(special_tokens_map, f, ensure_ascii=False, indent=4)

def train_tokenizer(data_path: str, save_dir: str, vocab_size: int = 8192) -> None:
    """训练并保存自定义tokenizer"""
    os.makedirs(save_dir, exist_ok=True)

    # 初始化tokenizer
    tokenizer = Tokenizer(models.BPE(unk_token="<unk>"))
    tokenizer.normalizer = NFKC()  # 添加文本规范化
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tokenizer.decoder = decoders.ByteLevel()

    # 配置特殊token
    special_tokens = [
        "<unk>",
        "<s>",
        "</s>",
        "<|im_start|>",
        "<|im_end|>"
    ]

    # 配置训练器
    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=special_tokens,
        min_frequency=2,  # 提高低频词过滤
        show_progress=True,
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet()
    )

    # 训练tokenizer
    print(f"Training tokenizer with data from {data_path}")
    texts = read_texts_from_jsonl(data_path)
    tokenizer.train_from_iterator(texts, trainer=trainer, length=os.path.getsize(data_path))

    # 验证特殊token映射
    try:
        assert tokenizer.token_to_id("<unk>") == 0
        assert tokenizer.token_to_id("<s>") == 1
        assert tokenizer.token_to_id("</s>") == 2
        assert tokenizer.token_to_id("<|im_start|>") == 3
        assert tokenizer.token_to_id("<|im_end|>") == 4
    except AssertionError as e:
        print("Special tokens mapping error:", e)
        raise

    # 保存tokenizer文件
    tokenizer.save(os.path.join(save_dir, "tokenizer.json"))

    # 创建配置文件
    create_tokenizer_config(save_dir)
    print(f"Tokenizer saved to {save_dir}")

def eval_tokenizer(tokenizer_path: str) -> None:
    """评估tokenizer功能"""
    try:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    except Exception as e:
        print(f"Error loading tokenizer: {e}")
        return

    # 测试基本属性
    print("\n=== Tokenizer基本信息 ===")
    print(f"Vocab size: {len(tokenizer)}")
    print(f"Special tokens: {tokenizer.all_special_tokens}")
    print(f"Special token IDs: {tokenizer.all_special_ids}")

    # 测试聊天模板
    messages = [
        {"role": "system", "content": "你是一个AI助手。"},
        {"role": "user", "content": "How are you?"},
        {"role": "assistant", "content": "I'm fine, thank you. and you?"},
        {"role": "user", "content": "I'm good too."},
        {"role": "assistant", "content": "That's great to hear!"},
    ]

    print("\n=== 聊天模板测试 ===")
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        # add_generation_prompt=True
    )
    print("Generated prompt:\n", prompt, sep="")

    # 测试编码解码
    print("\n=== 编码解码测试 ===")
    encoded = tokenizer(prompt, truncation=True, max_length=256)
    decoded = tokenizer.decode(encoded["input_ids"], skip_special_tokens=False)
    print("Decoded text matches original:", decoded == prompt)

    # 测试特殊token处理
    print("\n=== 特殊token处理 ===")
    test_text = "<|im_start|>user\nHello<|im_end|>"
    encoded = tokenizer(test_text).input_ids
    decoded = tokenizer.decode(encoded)
    print(f"Original: {test_text}")
    print(f"Decoded:  {decoded}")
    print("Special tokens preserved:", decoded == test_text)

def main():
    # 配置路径
    data_path = "your data path"
    save_dir = "tokenizer_k"

    # 训练tokenizer
    train_tokenizer(
        data_path=data_path,
        save_dir=save_dir,
        vocab_size=6144
    )

    # 评估tokenizer
    eval_tokenizer(save_dir)

if __name__ == '__main__':
    main()
```

训练完成之后可以可以使用 `eval_tokenizer()` 测试 Tokenizer 的功能，确保 Tokenizer 正常工作。在这个函数中，我们首先加载训练好的 Tokenizer，然后测试了 Tokenizer 的基本属性、聊天模板、编码解码等功能。这些测试可以帮助我们验证 Tokenizer 的正确性，确保它能够正常工作。正确的输出为：

OUT:
```
=== Tokenizer基本信息 ===
Vocab size: 6144
Special tokens: ['<|im_start|>', '<|im_end|>', '<unk>', '<s>', '</s>']
Special token IDs: [3, 4, 0, 1, 2]

=== 聊天模板测试 ===
Generated prompt:
<|im_start|>system
你是一个AI助手。<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
I'm fine, thank you. and you?<|im_end|>
<|im_start|>user
I'm good too.<|im_end|>
<|im_start|>assistant
That's great to hear!<|im_end|>


=== 编码解码测试 ===
Decoded text matches original: False

=== 特殊token处理 ===
Original: <|im_start|>user
Hello<|im_end|>
Decoded:  <|im_start|> user
Hello<|im_end|>
Special tokens preserved: False
```

##### 5.3.3 Dataset

###### PretrainDataset

在将数据送入到模型之前，我们还需要进行一些处理用于将文本数据转化为模型能够理解的Token。在这里我们使用的是Pytorch的Dataset类，用于加载数据集。我们定义了一个`PretrainDataset`类，用于加载已预处理好的数据集。我们继承了`torch.utils.data.IterableDataset`来定义该数据集，这使得我们可以更灵活、高效地处理数据。

```python
from torch.utils.data import Dataset

class PretrainDataset(Dataset):
    def __init__(self, data_path, tokenizer, max_length=512):
        super().__init__()
        self.data_path = data_path
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.padding = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0
        # 预计算每行的起始字节偏移量
        self._offsets = []
        with open(data_path, 'rb') as f:
            self._offsets.append(0)
            while f.readline():
                self._offsets.append(f.tell())
        self._total_lines = len(self._offsets) - 1  # 最后一个 tell() 是 EOF

    def __len__(self):
        return self._total_lines

    def __getitem__(self, index: int):
        with open(self.data_path, 'rb') as f:
            f.seek(self._offsets[index])
            line = f.readline().decode('utf-8')
        sample = json.loads(line)
        text = f"{self.tokenizer.bos_token}{sample['text']}"
        input_id = self.tokenizer(text).data['input_ids'][:self.max_length]
        text_len = len(input_id)
        # 没满最大长度的剩余部分
        padding_len = self.max_length - text_len
        input_id = input_id + [self.padding] * padding_len
        # 0表示不计算损失
        loss_mask = [1] * text_len + [0] * padding_len

        input_id = np.array(input_id)
        X = np.array(input_id[:-1]).astype(np.int64)
        Y = np.array(input_id[1:]).astype(np.int64)
        loss_mask = np.array(loss_mask[1:]).astype(np.int64)
        return torch.from_numpy(X), torch.from_numpy(Y), torch.from_numpy(loss_mask)
```

在以上代码和图5.3可以看出，`Pretrain Dataset` 主要是将 `text` 通过 `tokenizer` 转换成 `input_id`，然后将 `input_id` 拆分成 `X` 和 `Y`，其中 `X` 为 `input_id` 的前 n-1 个元素，`Y` 为 `input_id` 的后 n-1 `个元素。loss_mask` 主要是用来标记哪些位置需要计算损失，哪些位置不需要计算损失。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/5-images/pretrain_dataset.png)
图5.3 预训练损失函数计算


图中示例展示了当`max_length=9`时的处理过程：
- **输入序列**：`[BOS, T1, T2, T3, T4, T5, T6, T7, EOS]`
- **样本拆分**：
  - X：`[BOS, T1, T2, T3, T4, T5, T6, T7]` → 模型输入上下文
  - Y：`[T1, T2, T3, T4, T5, T6, T7, EOS]` → 模型预测目标
- **损失掩码**：
  - 有效位置：`[0, 1, 1, 1, 1, 1, 1, 1, 1]` → 仅对T1-EOS计算损失

###### SFTDataset

`SFTDataset` 其实是一个多轮对话数据集，我们的目标是让模型学会如何进行多轮对话。在这个阶段我们的输入是上一轮的对话内容，输出是当前轮的对话内容。

```python
class SFTDataset(Dataset):
    def __init__(self, data_path, tokenizer, max_length=512):
        super().__init__()
        self.data_path = data_path
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.padding = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0
        self._offsets = []
        with open(data_path, 'rb') as f:
            self._offsets.append(0)
            while f.readline():
                self._offsets.append(f.tell())
        self._total_lines = len(self._offsets) - 1

    def __len__(self):
        return self._total_lines

    def generate_loss_mask(self, input_ids):
        # 生成 loss mask, 0 表示不计算损失, 1 表示计算损失
        mask = [0] * len(input_ids)
        a_sequence = self.tokenizer("<|im_start|>assistant\n")['input_ids']  # <|im_start|>assistant\n
        a_length = len(a_sequence)
        n = len(input_ids)
        i = 0

        while i <= n - a_length:
            # 检查当前位置是否匹配目标子序列
            match = True
            for k in range(a_length):
                if input_ids[i + k] != a_sequence[k]:
                    match = False
                    break
            if match:
                # 从子序列结束的位置开始查找第一个 4 (eos_token_id)
                j = None
                for idx in range(i + a_length, n):
                    if input_ids[idx] == self.tokenizer.eos_token_id:
                        j = idx
                        break
                if j is not None:
                    start = i + a_length
                    end = j  # 结束位置设为j（包含4）
                    # 标记区间为1（包括start到end）
                    if start <= end:
                        for pos in range(start, end + 1):
                            if pos < len(mask):
                                mask[pos] = 1
                # 跳过当前子序列，避免重叠匹配
                i += a_length
            else:
                i += 1
        return mask

    def __getitem__(self, index: int):
        with open(self.data_path, 'rb') as f:
            f.seek(self._offsets[index])
            line = f.readline().decode('utf-8')
        sample = json.loads(line)
        text = self.tokenizer.apply_chat_template(sample, tokenize=False, add_generation_prompt=False)
        input_id = self.tokenizer(text).data['input_ids'][:self.max_length]
        text_len = len(input_id)
        # 没满最大长度的剩余部分
        padding_len = self.max_length - text_len
        input_id = input_id + [self.padding] * padding_len
        # 0表示不计算损失
        loss_mask = self.generate_loss_mask(input_id)

        input_id = np.array(input_id)
        X = np.array(input_id[:-1]).astype(np.int64)
        Y = np.array(input_id[1:]).astype(np.int64)
        loss_mask = np.array(loss_mask[1:]).astype(np.int64)
        return torch.from_numpy(X), torch.from_numpy(Y), torch.from_numpy(loss_mask)
```

在 SFT 阶段，这里使用的是多轮对话数据集，所以就需要区分哪些位置需要计算损失，哪些位置不需要计算损失。在上面的代码中，我使用了一个 `generate_loss_mask` 函数来生成 `loss_mask`。这个函数主要是用来生成 `loss_mask`，其中 `loss_mask` 的生成规则是：当遇到 `|<im_start|>assistant\n` 时，就开始计算损失，直到遇到 `|<im_end|>` 为止。这样就可以保证我们的模型在 SFT 阶段只计算当前轮的对话内容，如图5.4所示。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/5-images/sftdataset.png)
图5.4 SFT 损失函数计算


可以看到，其实 SFT Dataset 和 Pretrain Dataset 的 `X` 和 `Y` 是一样的，只是在 SFT Dataset 中我们需要生成一个 `loss_mask` 来标记哪些位置需要计算损失，哪些位置不需要计算损失。 图中 `Input ids` 中的蓝色小方格就是AI的回答，所以是需要模型学习的地方。所以在 `loss_mask` 中，蓝色小方格对应的位置是黄色，其他位置是灰色。在代码 `loss_mask` 中的 1 对应的位置计算损失，0 对应的位置不计算损失。


##### 5.3.4 预训练

在数据预处理完成后，我们就可以开始训练模型了。我们使用的模型是一个和LLama2结构一样的 Decoder only Transformer模型，使用Pytorch实现。相关代码在`code/k_model.py`文件中。此处不再赘述，源码中有详细的中文注释，且我们在之前的文章中也有详细的介绍。

在模型这一部分可以重点看一下生成式模型是如何实现生成token的，可以查看`k_model.py`文件中的`Transforerm`类中的`generate`方法。

```python
@torch.inference_mode()
    def generate(self, idx, stop_id=None, max_new_tokens=256, temperature=1.0, top_k=None):
        """
        给定输入序列 idx（形状为 (bz,seq_len) 的长整型张量），通过多次生成新 token 来完成序列。
        在 model.eval() 模式下运行。效率较低的采样版本，没有使用键k/v cache。
        """
        index = idx.shape[1]
        for _ in range(max_new_tokens):
            # 如果序列上下文过长，截断它到最大长度
            idx_cond = idx if idx.size(1) <= self.args.max_seq_len else idx[:, -self.args.max_seq_len:]

            # 前向传播获取序列中最后一个位置的 logits
            logits = self(idx_cond).logits
            logits = logits[:, -1, :] # 只保留最后一个时间步的输出

            if temperature == 0.0:
                # 选择最有可能的索引
                _, idx_next = torch.topk(logits, k=1, dim=-1)
            else:
                # 缩放 logits 并应用 softmax
                logits = logits / temperature
                if top_k is not None:
                    v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                    logits[logits < v[:, [-1]]] = -float('Inf')
                probs = F.softmax(logits, dim=-1)
                idx_next = torch.multinomial(probs, num_samples=1)


            if idx_next == stop_id:
                break

            # 将采样的索引添加到序列中并继续
            idx = torch.cat((idx, idx_next), dim=1)

        return idx[:, index:] # 只返回生成的token

```

在 `generate` 方法中，我们首先获取序列中最后一个位置的 `logits`，然后基于这些 `logits` 生成新的 `token`。接着，生成的新 `token` 会被添加到序列中，模型随后会继续生成下一个 `token`。通过这种迭代过程，我们能够生成完整的文本。

接下来就是最重要的部分，训练模型!

> 注：在使用下面代码进行模型训练时，需要指定 `--data_path` 参数为预处理好的数据集路径，例如 `--data_path seq_monkey_datawhale.jsonl`，也需要指定要用哪几张GPU进行训练，例如 `--gpus 0,1`。

```python
def get_lr(it, all):
    """
    计算当前迭代的学习率，使用余弦退火调度策略

    学习率调度策略：
    1. Warmup阶段：学习率从0线性增长到目标学习率
    2. 余弦退火阶段：学习率按余弦函数衰减到最小学习率
    3. 超出训练步数后：保持最小学习率

    Args:
        it (int): 当前迭代步数
        all (int): 总迭代步数

    Returns:
        float: 当前步数对应的学习率
    """
    warmup_iters = args.warmup_iters  # 预热迭代次数
    lr_decay_iters = all  # 学习率衰减的总迭代次数
    min_lr = args.learning_rate / 10  # 最小学习率，为初始学习率的1/10

    # Warmup阶段：线性增长
    if it < warmup_iters:
        return args.learning_rate * it / warmup_iters

    # 超出训练步数：保持最小学习率
    if it > lr_decay_iters:
        return min_lr

    # 余弦退火阶段
    decay_ratio = (it - warmup_iters) / (lr_decay_iters - warmup_iters)
    assert 0 <= decay_ratio <= 1
    coeff = 0.5 * (1.0 + math.cos(math.pi * decay_ratio))  # 余弦系数
    return min_lr + coeff * (args.learning_rate - min_lr)

def train_epoch(epoch):
    """
    训练一个epoch的函数

    实现了完整的训练循环，包括：
    1. 数据加载和设备转移
    2. 动态学习率调整
    3. 前向传播和损失计算
    4. 梯度累积和反向传播
    5. 梯度裁剪和优化器更新
    6. 日志记录和模型保存

    Args:
        epoch (int): 当前epoch编号
    """
    start_time = time.time()  # 记录开始时间

    # 遍历数据加载器中的每个batch
    for step, (X, Y, loss_mask) in enumerate(train_loader):
        # 将数据转移到指定设备（GPU/CPU）
        X = X.to(args.device)  # 输入序列
        Y = Y.to(args.device)  # 目标序列
        loss_mask = loss_mask.to(args.device)  # 损失掩码，用于忽略padding token

        # 计算当前步骤的学习率
        lr = get_lr(epoch * iter_per_epoch + step, args.epochs * iter_per_epoch)
        # 更新优化器中所有参数组的学习率
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr

        # 使用混合精度训练上下文
        with ctx:
            # 前向传播
            out = model(X, Y)
            # 计算损失并除以累积步数（用于梯度累积）
            loss = out.last_loss / args.accumulation_steps
            # 将loss_mask展平为一维
            loss_mask = loss_mask.view(-1)
            # 应用掩码计算有效损失（忽略padding位置）
            loss = torch.sum(loss * loss_mask) / loss_mask.sum()

        # 使用scaler进行混合精度的反向传播
        scaler.scale(loss).backward()

        # 每accumulation_steps步执行一次优化器更新
        if (step + 1) % args.accumulation_steps == 0:
            # 取消梯度缩放，准备梯度裁剪
            scaler.unscale_(optimizer)
            # 梯度裁剪，防止梯度爆炸
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)

            # 执行优化器步骤
            scaler.step(optimizer)
            # 更新scaler的缩放因子
            scaler.update()

            # 清零梯度，set_to_none=True可以节省内存
            optimizer.zero_grad(set_to_none=True)

        # 每log_interval步记录一次日志
        if step % args.log_interval == 0:
            spend_time = time.time() - start_time
            # 打印训练进度信息
            Logger(
                'Epoch:[{}/{}]({}/{}) loss:{:.3f} lr:{:.7f} epoch_Time:{}min;'.format(
                    epoch + 1,
                    args.epochs,
                    step,
                    iter_per_epoch,
                    loss.item() * args.accumulation_steps,  # 恢复真实的loss值
                    optimizer.param_groups[-1]['lr'],
                    spend_time / (step + 1) * iter_per_epoch // 60 - spend_time // 60))

            # 如果启用SwanLab，记录训练指标
            if args.use_swanlab:
                swanlab.log({
                    "loss": loss.item() * args.accumulation_steps,
                    "lr": optimizer.param_groups[-1]['lr']
                })

        # 每save_interval步保存一次模型
        if (step + 1) % args.save_interval == 0:
            model.eval()  # 切换到评估模式
            # 构建检查点文件名
            ckp = f'{args.save_dir}/pretrain_{lm_config.dim}_{lm_config.n_layers}_{lm_config.vocab_size}.pth'

            # 处理多卡保存：如果是DataParallel模型，需要访问.module属性
            state_dict = model.module.state_dict() if isinstance(model, torch.nn.DataParallel) else model.state_dict()
            torch.save(state_dict, ckp)
            model.train()  # 切换回训练模式

        # 每20000步保存一个带步数标记的检查点
        if (step + 1) % 20000 == 0:
            model.eval()
            # 构建带步数的检查点文件名
            ckp = f'{args.save_dir}/pretrain_{lm_config.dim}_{lm_config.n_layers}_{lm_config.vocab_size}_step{step+1}.pth'

            # 保存模型状态字典
            state_dict = model.module.state_dict() if isinstance(model, torch.nn.DataParallel) else model.state_dict()
            torch.save(state_dict, ckp)
            model.train()


def init_model():
    """
    初始化模型和分词器

    功能包括：
    1. 加载预训练的分词器
    2. 创建Transformer模型
    3. 设置多GPU并行训练（如果可用）
    4. 将模型移动到指定设备
    5. 统计并打印模型参数量

    Returns:
        tuple: (model, tokenizer) 初始化后的模型和分词器
    """
    def count_parameters(model):
        """
        统计模型中可训练参数的数量

        Args:
            model: PyTorch模型

        Returns:
            int: 可训练参数总数
        """
        return sum(p.numel() for p in model.parameters() if p.requires_grad)

    # 从本地路径加载预训练的分词器
    tokenizer = AutoTokenizer.from_pretrained('./tokenizer_k/')

    # 根据配置创建Transformer模型
    model = Transformer(lm_config)

    # 多卡初始化：检查可用GPU数量并设置DataParallel
    num_gpus = torch.cuda.device_count()
    if num_gpus > 1:
        Logger(f"Using {num_gpus} GPUs with DataParallel!")
        # 使用DataParallel包装模型以支持多GPU训练
        model = torch.nn.DataParallel(model)

    # 将模型移动到指定设备（GPU或CPU）
    model = model.to(args.device)

    # 计算并打印模型参数量（以百万为单位）
    Logger(f'LLM总参数量：{count_parameters(model) / 1e6:.3f} 百万')
    return model, tokenizer


if __name__ == "__main__":
    # ==================== 命令行参数解析 ====================
    parser = argparse.ArgumentParser(description="Tiny-LLM Pretraining")

    # 基础训练参数
    parser.add_argument("--out_dir", type=str, default="base_model_215M", help="模型输出目录")
    parser.add_argument("--epochs", type=int, default=1, help="训练轮数")
    parser.add_argument("--batch_size", type=int, default=64, help="批次大小")
    parser.add_argument("--learning_rate", type=float, default=2e-4, help="学习率")
    parser.add_argument("--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu", help="训练设备")
    parser.add_argument("--dtype", type=str, default="bfloat16", help="数据类型")

    # 实验跟踪和数据加载参数
    parser.add_argument("--use_swanlab", action="store_true", help="是否使用SwanLab进行实验跟踪")
    parser.add_argument("--num_workers", type=int, default=8, help="数据加载的工作进程数")
    parser.add_argument("--data_path", type=str, default="./seq_monkey_datawhale.jsonl", help="训练数据路径")

    # 训练优化参数
    parser.add_argument("--accumulation_steps", type=int, default=8, help="梯度累积步数")
    parser.add_argument("--grad_clip", type=float, default=1.0, help="梯度裁剪阈值")
    parser.add_argument("--warmup_iters", type=int, default=0, help="学习率预热迭代次数")

    # 日志和保存参数
    parser.add_argument("--log_interval", type=int, default=100, help="日志记录间隔")
    parser.add_argument("--save_interval", type=int, default=1000, help="模型保存间隔")

    # 多GPU训练参数
    parser.add_argument("--gpus", type=str, default='0,1,2,3,4,5,6,7', help="使用的GPU ID，用逗号分隔 (例如: '0,1,2')")

    args = parser.parse_args()

    # ==================== GPU环境设置 ====================
    # 设置可见的GPU设备
    if args.gpus is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpus
        # 自动设置主设备为第一个可用GPU
        if torch.cuda.is_available():
            args.device = "cuda:0"
        else:
            args.device = "cpu"

    # ==================== 实验跟踪初始化 ====================
    if args.use_swanlab:
        # 注意：使用前需要先登录 swanlab.login(api_key='your key')
        run = swanlab.init(
            project="Happy-LLM",  # 项目名称
            experiment_name="Pretrain-215M",  # 实验名称
            config=args,  # 保存所有超参数
        )

    # ==================== 模型配置 ====================
    # 定义语言模型的配置参数
    lm_config = ModelConfig(
        dim=1024,      # 模型维度
        n_layers=18,   # Transformer层数
    )

    # ==================== 训练环境设置 ====================
    max_seq_len = lm_config.max_seq_len  # 最大序列长度
    args.save_dir = os.path.join(args.out_dir)  # 模型保存目录

    # 创建必要的目录
    os.makedirs(args.out_dir, exist_ok=True)

    # 设置随机种子以确保结果可复现
    torch.manual_seed(42)

    # 确定设备类型（用于选择合适的上下文管理器）
    device_type = "cuda" if "cuda" in args.device else "cpu"

    # 设置混合精度训练的上下文管理器
    # CPU训练时使用nullcontext，GPU训练时使用autocast
    ctx = nullcontext() if device_type == "cpu" else torch.cuda.amp.autocast()

    # ==================== 模型和数据初始化 ====================
    # 初始化模型和分词器
    model, tokenizer = init_model()

    # 创建训练数据集
    train_ds = PretrainDataset(args.data_path, tokenizer, max_length=max_seq_len)

    # 创建数据加载器
    train_loader = DataLoader(
        train_ds,
        batch_size=args.batch_size,  # 批次大小
        pin_memory=True,             # 将数据加载到固定内存中，加速GPU传输
        drop_last=False,             # 不丢弃最后一个不完整的批次
        shuffle=True,                # 随机打乱数据
        num_workers=args.num_workers # 数据加载的并行工作进程数
    )

    # ==================== 优化器和训练组件初始化 ====================
    # 初始化混合精度训练的梯度缩放器
    # 只有在使用float16或bfloat16时才启用
    scaler = torch.cuda.amp.GradScaler(enabled=(args.dtype in ['float16', 'bfloat16']))

    # 初始化Adam优化器
    optimizer = optim.Adam(model.parameters(), lr=args.learning_rate)

    # ==================== 开始训练 ====================
    # 计算每个epoch的迭代次数
    iter_per_epoch = len(train_loader)

    # 开始训练循环
    for epoch in range(args.epochs):
        train_epoch(epoch)
```

##### 5.3.5 SFT 训练

SFT 训练和预训练的代码基本一样，只是导入的 Dataset 不一样。在这里我们使用的是 SFTDataset，用于多轮对话的训练。

```python
import os
import platform
import argparse
import time
import warnings
import math
import pandas as pd
import torch
from torch import optim
from torch.utils.data import DataLoader
from contextlib import nullcontext

from transformers import AutoTokenizer

from k_model import ModelConfig, Transformer
from dataset import SFTDataset

import swanlab

# 忽略警告
warnings.filterwarnings('ignore')


def Logger(content):
    """日志记录器"""
    print(content)

def get_lr(it, all):
    """获取学习率"""
    # 1) linear warmup for warmup_iters steps
    # 1) 预热迭代的线性预热
    warmup_iters = args.warmup_iters
    lr_decay_iters = all
    min_lr = args.learning_rate / 10

    if it < warmup_iters:
        return args.learning_rate * it / warmup_iters

    # 2) if it > lr_decay_iters, return min learning rate
    # 2) 如果迭代次数超过学习率衰减迭代次数，则返回最小学习率
    if it > lr_decay_iters:
        return min_lr

    # 3) in between, use cosine decay down to min learning rate
    # 3) 在两者之间，使用余弦衰减至最小学习率
    decay_ratio = (it - warmup_iters) / (lr_decay_iters - warmup_iters)
    assert 0 <= decay_ratio <= 1
    coeff = 0.5 * (1.0 + math.cos(math.pi * decay_ratio))
    return min_lr + coeff * (args.learning_rate - min_lr)

def train_epoch(epoch):
    """训练一个epoch"""
    start_time = time.time()
    for step, (X, Y, loss_mask) in enumerate(train_loader):
        X = X.to(args.device)
        Y = Y.to(args.device)
        loss_mask = loss_mask.to(args.device)

        # 获取学习率并更新优化器
        lr = get_lr(epoch * iter_per_epoch + step, args.epochs * iter_per_epoch)
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr

        # 前向传播
        with ctx:
            out = model(X, Y)
            loss = out.last_loss / args.accumulation_steps
            loss_mask = loss_mask.view(-1)
            loss = torch.sum(loss * loss_mask) / loss_mask.sum()

        # 反向传播
        scaler.scale(loss).backward()

        # 更新权重
        if (step + 1) % args.accumulation_steps == 0:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)

            scaler.step(optimizer)
            scaler.update()

            optimizer.zero_grad(set_to_none=True)

        # 打印日志
        if step % args.log_interval == 0:
            spend_time = time.time() - start_time
            Logger(
                'Epoch:[{}/{}]({}/{}) loss:{:.3f} lr:{:.7f} epoch_Time:{}min:'.format(
                    epoch + 1,
                    args.epochs,
                    step,
                    iter_per_epoch,
                    loss.item() * args.accumulation_steps,
                    optimizer.param_groups[-1]['lr'],
                    spend_time / (step + 1) * iter_per_epoch // 60 - spend_time // 60))
            if args.use_swanlab:
                swanlab.log({
                    "loss": loss.item() * args.accumulation_steps,
                    "lr": optimizer.param_groups[-1]['lr']
                })

        # 保存模型
        if (step + 1) % args.save_interval == 0:
            model.eval()
            ckp = f'{args.save_dir}/sft_dim{lm_config.dim}_layers{lm_config.n_layers}_vocab_size{lm_config.vocab_size}.pth'

            # 处理多卡保存
            state_dict = model.module.state_dict() if isinstance(model, torch.nn.DataParallel) else model.state_dict()
            torch.save(state_dict, ckp)
            model.train()

        # 定期保存模型
        if (step + 1) % 20000 == 0:
            model.eval()
            ckp = f'{args.save_dir}/sft_dim{lm_config.dim}_layers{lm_config.n_layers}_vocab_size{lm_config.vocab_size}_step{step+1}.pth'

            state_dict = model.module.state_dict() if isinstance(model, torch.nn.DataParallel) else model.state_dict()
            torch.save(state_dict, ckp)
            model.train()


def init_model():
    """初始化模型"""
    def count_parameters(model):
        """计算模型参数量"""
        return sum(p.numel() for p in model.parameters() if p.requires_grad)

    # 加载分词器
    tokenizer = AutoTokenizer.from_pretrained('./tokenizer_k/')

    # 初始化模型
    model = Transformer(lm_config)

    # 加载预训练权重
    ckp = './base_model_215M/pretrain_1024_18_6144.pth'
    state_dict = torch.load(ckp, map_location=args.device)
    unwanted_prefix = '_orig_mod.'
    for k, v in list(state_dict.items()):
        if k.startswith(unwanted_prefix):
            state_dict[k[len(unwanted_prefix):]] = state_dict.pop(k)
    model.load_state_dict(state_dict, strict=False)

    # 多卡初始化
    num_gpus = torch.cuda.device_count()
    if num_gpus > 1:
        Logger(f"Using {num_gpus} GPUs with DataParallel!")
        model = torch.nn.DataParallel(model)

    model = model.to(args.device)
    Logger(f'LLM总参数量：{count_parameters(model) / 1e6:.3f} 百万')
    return model, tokenizer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tiny-LLM Pretraining")
    parser.add_argument("--out_dir", type=str, default="sft_model_215M", help="输出目录")
    parser.add_argument("--epochs", type=int, default=1, help="训练轮数")
    parser.add_argument("--batch_size", type=int, default=64, help="批处理大小")
    parser.add_argument("--learning_rate", type=float, default=2e-4, help="学习率")
    parser.add_argument("--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu", help="使用的设备")
    parser.add_argument("--dtype", type=str, default="bfloat16", help="数据类型")
    parser.add_argument("--use_swanlab", action="store_true", help="是否使用SwanLab进行实验跟踪")
    parser.add_argument("--num_workers", type=int, default=8, help="数据加载的工作进程数")
    parser.add_argument("--data_path", type=str, default="./BelleGroup_sft.jsonl", help="训练数据路径")
    parser.add_argument("--accumulation_steps", type=int, default=8, help="梯度累积步数")
    parser.add_argument("--grad_clip", type=float, default=1.0, help="梯度裁剪阈值")
    parser.add_argument("--warmup_iters", type=int, default=0, help="预热迭代次数")
    parser.add_argument("--log_interval", type=int, default=100, help="日志记录间隔")
    parser.add_argument("--save_interval", type=int, default=1000, help="模型保存间隔")
    # 添加多卡参数
    parser.add_argument("--gpus", type=str, default='0,1,2,3,4,5,6,7', help="逗号分隔的GPU ID (例如 '0,1,2')")

    args = parser.parse_args()

    # 设置可见GPU
    if args.gpus is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpus
        # 自动设置主设备为第一个GPU
        if torch.cuda.is_available():
            args.device = "cuda:0"
        else:
            args.device = "cpu"

    # 初始化swanlab
    if args.use_swanlab:
        run = swanlab.init(
            project="Happy-LLM",
            experiment_name="SFT-215M",
            config=args,
        )

    # 模型配置
    lm_config = ModelConfig(
        dim=1024,
        n_layers=18,
    )
    max_seq_len = lm_config.max_seq_len
    args.save_dir = os.path.join(args.out_dir)
    os.makedirs(args.out_dir, exist_ok=True)
    torch.manual_seed(42)
    device_type = "cuda" if "cuda" in args.device else "cpu"

    # 上下文管理器
    ctx = nullcontext() if device_type == "cpu" else torch.cuda.amp.autocast()

    # 初始化模型和分词器
    model, tokenizer = init_model()

    # 创建数据集和数据加载器
    train_ds = SFTDataset(args.data_path, tokenizer, max_length=max_seq_len)
    train_loader = DataLoader(
        train_ds,
        batch_size=args.batch_size,
        pin_memory=True,
        drop_last=False,
        shuffle=True,
        num_workers=args.num_workers
    )

    # 缩放器和优化器
    scaler = torch.cuda.amp.GradScaler(enabled=(args.dtype in ['float16', 'bfloat16']))
    optimizer = optim.AdamW(model.parameters(), lr=args.learning_rate)

    # 开始训练
    iter_per_epoch = len(train_loader)
    for epoch in range(args.epochs):
        train_epoch(epoch)
```


##### 5.3.6 使用模型生成文本

在模型训练完成后，会在`output`目录下生成模型文件，这个文件就是我们训练好的模型。我们可以使用以下命令生成文本。

```bash
python model_sample.py
```

我们来看下`model_sample.py`文件中的代码，这个文件中定义了一个`TextGenerator`类，用于生成文本。

```python
import os
import pickle
from contextlib import nullcontext
import torch
from k_model import ModelConfig, Transformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import argparse

class TextGenerator:
    def __init__(self,
                 checkpoint='./base_model_215M/pretrain_1024_18_6144.pth',  # 模型检查点路径
                 tokenizer_model_path='./tokenizer_k/',  # 分词器模型路径
                 seed=42,  # 随机种子，确保可重复性
                 device=None,  # 设备，优先使用 CUDA，如果没有可用的 CUDA，则使用 CPU
                 dtype="bfloat16"):  # 数据类型，默认为 float32，可以选择 float16 或 bfloat16
        """
        初始化 TextGenerator 类，加载模型、设置设备和分词器等。
        """
        # 模型加载配置
        self.checkpoint = checkpoint  # 保存的模型检查点路径
        self.tokenizer_model_path = tokenizer_model_path  # 分词器模型文件路径
        self.seed = seed  # 随机数种子，用于生成的可重复性
        self.device = device or ('cuda:0' if torch.cuda.is_available() else 'cpu')  # 根据硬件条件选择设备
        self.dtype = dtype  # 模型的浮点数类型
        self.device_type = 'cuda' if 'cuda' in self.device else 'cpu'  # 判断当前设备是否为 CUDA

        # 设置随机种子，确保生成的可重复性
        torch.manual_seed(seed)  # 设置 CPU 随机种子
        torch.cuda.manual_seed(seed)  # 设置 CUDA 随机种子
        torch.backends.cuda.matmul.allow_tf32 = True  # 允许 CUDA 使用 TF32 精度进行矩阵乘法运算
        torch.backends.cudnn.allow_tf32 = True  # 允许 cuDNN 使用 TF32 精度加速

        # 根据 dtype 选择适当的自动混合精度上下文
        ptdtype = {'float32': torch.float32, 'bfloat16': torch.bfloat16, 'float16': torch.float16}[self.dtype]
        self.ctx = nullcontext() if self.device_type == 'cpu' else torch.amp.autocast(device_type=self.device_type, dtype=ptdtype)

        # 加载模型检查点文件
        checkpoint_dict = torch.load(self.checkpoint, map_location=self.device)  # 加载模型参数 # 初始化模型参数
        self.model = Transformer(ModelConfig(dim=1024, n_layers=18))  # 实例化 Transformer 模型
        sunwanted_prefix = '_orig_mod.'
        for k, v in list(checkpoint_dict.items()):
            if k.startswith(sunwanted_prefix):
                checkpoint_dict[k[len(sunwanted_prefix):]] = checkpoint_dict.pop(k)
        self.model.load_state_dict(checkpoint_dict, strict=False)

        # 计算模型参数量
        num_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print(f"Model has {num_params / 1e6:.3f} M parameters.")
        # 设置模型为评估模式（evaluation mode），防止训练模式下的 dropout 等操作影响结果
        self.model.eval()
        # 将模型放置到正确的设备上（GPU 或 CPU）
        self.model.to(self.device)
        # 初始化分词器
        self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_model_path)  # 根据指定的路径加载分词器

    def chat_template(self, prompt):
        message = [
            {"role": "system", "content": "你是一个AI助手，你的名字叫小明。"},
            {"role": "user", "content": prompt}
        ]
        return self.tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=True)

    def sft_sample(self,
               start="Hello!",  # 生成文本的起始提示词，可以是任意字符串
               num_samples=3,  # 生成样本的数量，默认生成 3 个样本
               max_new_tokens=256,  # 每个样本生成的最大 token 数，默认最多生成 256 个 token
               temperature=0.7,  # 控制生成的随机性，1.0 为标准，值越大越随机
               top_k=300):  # 保留概率最高的 top_k 个 token，限制生成时的选择范围
        """
        根据给定的起始文本生成样本。

        :param start: 生成文本的起始提示词
        :param num_samples: 要生成的文本样本数
        :param max_new_tokens: 每个样本生成的最大 token 数
        :param temperature: 控制生成的随机性，值越小生成越确定，值越大生成越随机
        :param top_k: 限制生成时选择的 token 范围
        :return: 生成的文本样本列表
        """
        start = self.chat_template(start)
        # 将起始文本编码为 token id 序列
        start_ids = self.tokenizer(start).data['input_ids']
        # print('start_ids:', start_ids)
        x = (torch.tensor(start_ids, dtype=torch.long, device=self.device)[None, ...])  # 将编码后的 token id 转为 PyTorch 张量
        generated_texts = []  # 用于保存生成的文本样本
        with torch.no_grad():  # 禁用梯度计算，提升效率
            with self.ctx:  # 进入自动混合精度的上下文（如果是 GPU 并使用 float16 时）
                for k in range(num_samples):  # 循环生成指定数量的样本
                    y = self.model.generate(x, self.tokenizer.eos_token_id, max_new_tokens, temperature=temperature, top_k=top_k)  # 生成文本
                    generated_texts.append(self.tokenizer.decode(y[0].tolist()))  # 解码生成的 token 序列为可读文本
        return generated_texts  # 返回生成的文本样本


    def pretrain_sample(self,
               start="Hello!",  # 生成文本的起始提示词，可以是任意字符串
               num_samples=3,  # 生成样本的数量，默认生成 3 个样本
               max_new_tokens=256,  # 每个样本生成的最大 token 数，默认最多生成 256 个 token
               temperature=0.7,  # 控制生成的随机性，1.0 为标准，值越大越随机
               top_k=300):  # 保留概率最高的 top_k 个 token，限制生成时的选择范围
        """
        根据给定的起始文本生成样本。

        :param start: 生成文本的起始提示词
        :param num_samples: 要生成的文本样本数
        :param max_new_tokens: 每个样本生成的最大 token 数
        :param temperature: 控制生成的随机性，值越小生成越确定，值越大生成越随机
        :param top_k: 限制生成时选择的 token 范围
        :return: 生成的文本样本列表
        """
        # 如果 start 是以 'FILE:' 开头，表示从文件中读取起始文本
        if start.startswith('FILE:'):
            with open(start[5:], 'r', encoding='utf-8') as f:
                start = f.read()  # 读取文件内容作为起始文本

        # 将起始文本编码为 token id 序列
        start_ids = self.tokenizer(start).data['input_ids']
        # print('start_ids:', start_ids)
        x = (torch.tensor(start_ids, dtype=torch.long, device=self.device)[None, ...])  # 将编码后的 token id 转为 PyTorch 张量
        # print(x.shape)
        generated_texts = []  # 用于保存生成的文本样本
        with torch.no_grad():  # 禁用梯度计算，提升效率
            with self.ctx:  # 进入自动混合精度的上下文（如果是 GPU 并使用 float16 时）
                for k in range(num_samples):  # 循环生成指定数量的样本
                    y = self.model.generate(x, max_new_tokens=max_new_tokens, temperature=temperature, top_k=top_k)  # 生成文本
                    generated_texts.append(self.tokenizer.decode(y[0].tolist()))  # 解码生成的 token 序列为可读文本

        return generated_texts  # 返回生成的文本样本

if __name__ == "__main__":
    print("------------------- Pretrain Sample ------------------- \n")

    pretrain_prompt_datas = [
        '<|im_start|>北京大学是',
        '<|im_start|>中国矿业大学（北京）地球科学与测绘工程学院',
    ]

    generator = TextGenerator(checkpoint='./base_model_215M/pretrain_1024_18_6144.pth')  # 初始化生成器
    for i in range(len(pretrain_prompt_datas)):
        samples = generator.pretrain_sample(start=pretrain_prompt_datas[i], num_samples=1, max_new_tokens=120, temperature=0.75)
        print(f"\nSample {i+1}:\n{pretrain_prompt_datas[i]}{samples[0]}\n{'-'*20}")  # 打印生成的样本并用分隔线分割

    print("\n ------------------- SFT Sample ------------------- \n")

    sft_prompt_datas = [
        '你好呀',
        "中国的首都是哪里？",
        "1+12等于多少？",
        "你是谁？"
    ]
    generator = TextGenerator(checkpoint='./sft_model_215M/sft_dim1024_layers18_vocab_size6144.pth')  # 初始化生成器
    for i in range(len(sft_prompt_datas)):
        samples = generator.sft_sample(start=sft_prompt_datas[i], num_samples=1, max_new_tokens=128, temperature=0.6)
        print(f"\nSample {i+1}:\nQuestion: {sft_prompt_datas[i]} \nAI answer: {samples[0]}\n{'-'*20}")  # 打印生成的样本并用分隔线分割

```

最后我们来看一下模型输出的结果：

```
------------------- SFT Sample -------------------

Model has 215.127 M parameters.

Sample 1:
Question: 你好呀
AI answer: 你好!有什么我可以帮你的吗?
--------------------

Sample 2:
Question: 中国的首都是哪里？
AI answer: 中国的首都是北京。
--------------------

Sample 3:
Question: 1+1等于多少？
AI answer: 1+1等于2。
--------------------
------------------- Pretrain Sample -------------------

Model has 215.127 M parameters.

Sample 1:
<|im_start|>北京大学是中国最早建立的研究型大学之一,是我国最早设置研究生院的高校之一,是第一、二国教育委员会师资培训基地;北京大学是第一、二所国立大学,其校名与北京大学相同。
北京大学录取标准:本科三批1万元,本科一批1万元,本科一批2000元,专科一批2000元,高中起点:非本科一批
--------------------

Sample 2:
<|im_start|>中国矿业大学（北京）地球科学与测绘工程学院副教授黄河流域地质学科带头人古建平教授为大家介绍世界地质变化的概念及工作经验。
古建平教授介绍了最近几年的植物学和地质学的基本概念,尤其是树都黄河、松涛、暗河等都有地质学工作者的身影,其中树都黄河以分布面积最大,是树都黄河中华砂岩公园的主景区。
黄河内蒙古
--------------------
```

到这里，我们的模型就训练完成了，恭喜你训练了一个属于你自己的大模型。

> 大家在训练的时候可以将 batch 调的低一些，这样可以减少显存的占用，避免显存不足的问题。当然这样会增加训练时间，可以根据自己的显卡显存大小来调整 batch 的大小。实测 Pretrain batch 为 4 的情况下只需要 7G 显存，训练时长预计 533 小时。作者是在 8卡4090 上进行训练的，预训练一共耗时 46 小时，SFT 阶段在 BelleGroup 350万条中文指令训练 24 小时。

作者也在魔搭平台上传了本章节训来的模型，如果大家的设备不足以训练大模型，大家也可以在魔搭平台下载模型进行调试和模型体验。模型下载地址如下：

> *ModelScope 模型下载地址：[🤖 ModelScope](https://www.modelscope.cn/collections/Happy-LLM-e98b91b10b684a)*
> *ModelScope 创空间体验地址：[🤖 创空间](https://www.modelscope.cn/studios/kmno4zx/happy_llm_215M_sft)*


**参考资料**

[1] Andrej Karpathy. (2023). *llama2.c: Fullstack Llama 2 LLM solution in pure C*. GitHub repository. https://github.com/karpathy/llama2.c

[2] Andrej Karpathy. (2023). *llm.c: GPT-2/GPT-3 pretraining in C/CUDA*. GitHub repository. https://github.com/karpathy/llm.c

[3] Hugging Face. (2023). *Tokenizers documentation*. https://huggingface.co/docs/tokenizers/index

[4] Skywork Team. (2023). *SkyPile-150B: A large-scale bilingual dataset*. Hugging Face dataset. https://huggingface.co/datasets/Skywork/SkyPile-150B

[5] BelleGroup. (2022). *train_3.5M_CN: Chinese dialogue dataset*. Hugging Face dataset. https://huggingface.co/datasets/BelleGroup/train_3.5M_CN

[6] Jingyao Gong. (2023). *minimind: Minimalist LLM implementation*. GitHub repository. https://github.com/jingyaogong/minimind

[7] Mobvoi. (2023). *seq-monkey-data: Llama2 training/inference data*. GitHub repository. https://github.com/mobvoi/seq-monkey-data

### 第六章 大模型训练实践

第五章中，我们从零开始动手搭建了 LLaMA2 模型，并完整实现了其预训练和微调的全流程。在本章中，我们将深入探讨大模型的训练流程实践，重点介绍如何利用主流的大模型框架高效地进行模型训练和性能优化。

> 阅读建议：在开始本章实践前，建议先阅读 [第六章实践说明](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/readme.md) 和 [学习与环境准备](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/%E5%AD%A6%E4%B9%A0%E4%B8%8E%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87.md)。本章正文聚焦 Pretrain、SFT 与 PEFT 三条主线，偏好对齐作为进阶主题在 6.4 节给出整体学习路线，并提供补充专题材料。

#### 6.1 模型预训练

在上一章，我们逐步拆解了 LLM 的模型结构及训练过程，从零手写实现了 LLaMA 模型结构及 Pretrain、SFT 全流程，更深入地理解了 LLM 的模型原理及训练细节。但是，在实际应用中，手写实现的 LLM 训练存在以下问题：

- 手写实现 LLM 结构工作量大，难以实时跟进最新模型的结构创新；
- 从零实现的 LLM 训练无法较好地实现多卡分布式训练，训练效率较低；
- 和现有预训练 LLM 不兼容，无法使用预训练好的模型参数

因此，在本章中，我们将介绍目前 LLM 领域的主流训练框架 Transformers，并结合分布式框架 deepspeed、高效微调框架 peft 等主流框架，实践使用 transformers 进行模型 Pretrain、SFT 全流程，更好地对接业界的主流 LLM 技术方案。

##### 6.1.1 框架介绍

Transformers 是由 Hugging Face 开发的 NLP 框架，通过模块化设计实现了对 BERT、GPT、LLaMA、T5、ViT 等上百种主流模型架构的统一支持。通过使用 Transformers，开发者无需重复实现基础网络结构，通过 AutoModel 类即可一键加载任意预训练，图6.1 为 Hugging Face Transformers 课程首页：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/1-1.png)
图6.1 Hugging Face Transformers


同时，框架内置的 Trainer 类封装了分布式训练的核心逻辑，支持 PyTorch 原生 DDP、DeepSpeed、Megatron-LM 等多种分布式训练策略。通过简单配置训练参数，即可实现数据并行、模型并行、流水线并行的混合并行训练，在 8 卡 A100 集群上可轻松支持百亿参数模型的高效训练。配合 SavingPolicy 和 LoggingCallback 等组件，实现了训练过程的自动化管理。其还支持与 Deepspeed、peft、wandb、Swanlab 等框架进行集成，直接通过参数设置即可无缝对接，从而快速、高效实现 LLM 训练。

对 LLM 时代的 NLP 研究者更为重要的是，HuggingFace 基于 Transformers 框架搭建了其庞大的 AI 社区，开放了数亿个预训练模型参数、25万+不同类型数据集，通过 Transformers、Dataset、Evaluate 等多个框架实现对预训练模型、数据集及评估函数的集成，从而帮助开发者可以便捷地使用任一预训练模型，在开源模型及数据集的基础上便捷地实现个人模型的开发与应用。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/1-2.png)
图6.2 Hugging Face Transformers 模型社区


在 LLM 时代，模型结构的调整和重新预训练越来越少，开发者更多的业务应用在于使用预训练好的 LLM 进行 Post Train 和 SFT，来支持自己的下游业务应用。且由于预训练模型体量大，便捷集成 deepspeed 等分布式训练框架逐渐成为 LLM 时代 NLP 模型训练的必备技能。因此，Transformers 已逐步成为学界、业界 NLP 技术的主流框架，不管是企业业务开发还是科研研究，都逐渐首选 Transformers 进行模型实现。同时，新发布的开源 LLM 如 DeepSeek、Qwen 也都会第一时间在 Transformers 社区开放其预训练权重与模型调用 Demo。通过使用 Transformers 框架，可以高效、便捷地完成 LLM 训练及开发，实现工业级的产出交付。接下来，我们就会以 Transformers 框架为基础，介绍如何通过 Transformers 框架实现 LLM 的 Pretrain 及 SFT。

##### 6.1.2 初始化 LLM

我们可以使用 transformers 的 AutoModel 类来直接初始化已经实现好的模型。对于任意预训练模型，其参数中都包含有模型的配置信息。如果是想要从头训练一个 LLM，可以使用一个已有的模型架构来直接初始化。这里，我们以 [Qwen-2.5-1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B/tree/main)的模型架构为例：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/1-3.png)
图6.3 Qwen-2.5-1.5B


该界面即为 HuggingFace 社区中的 Qwen-2.5-1.5B 模型参数，其中的 `config.json` 文件即是模型的配置信息，包括了模型的架构、隐藏层大小、模型层数等，如图6.4所示：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/1-4.png)
图6.4 Qwen-2.5-1.5B config.json 文件


我们可以沿用该模型的配置信息，初始化一个 Qwen-2.5-1.5B 模型来进行训练，也可以在该配置信息的基础上进行更改，如修改隐藏层大小、注意力头数等，来定制一个模型结构。HuggingFace 提供了 Python 工具来便捷下载想使用的模型参数：

```python
import os
# 设置环境变量，此处使用 HuggingFace 镜像网站
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
# 下载模型
os.system('huggingface-cli download --resume-download Qwen/Qwen2.5-1.5B --local-dir your_local_dir')
```

如图6.5，此处的 “Qwen/Qwen2.5-1.5B”即为要下载模型的标识符，对于其他模型，可以直接复制 HuggingFace 上的模型名即可：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/1-5.png)
图6.5 模型下载标识


下载完成后，可以使用 AutoConfig 类直接加载下载好的配置文件：

```python
# 加载定义好的模型参数-此处以 Qwen-2.5-1.5B 为例
# 使用 transforemrs 的 Config 类进行加载
from transformers import AutoConfig

# 下载参数的本地路径
model_path = "qwen-1.5b"
config = AutoConfig.from_pretrained(model_name_or_path)
```

也可以对配置文件进行自定义，然后以同样的方式加载即可。可以使用 AutoModel 类基于加载好的配置对象生成对应的模型：

```python
# 使用该配置生成一个定义好的模型
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_config(config,trust_remote_code=True)
```

由于 LLM 一般都是 CausalLM 架构，此处使用了 AutoModelForCausalLM 类进行加载。如果是用于分类任务训练，可使用 AutoModelForSequenceClassification 类来加载。查看该 model，图6.6可以看到其架构和定义的配置文件相同：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/1-6.png)
图6.6 模型结构输出结果


该 model 就是一个从零初始化的 Qwen-2.5-1.5B 模型了。一般情况下，我们很少从零初始化 LLM 进行预训练，较多的做法是加载一个预训练好的 LLM 权重，在自己的语料上进行后训练。这里，我们也介绍如何从下载好的模型参数中初始化一个预训练好的模型。

```python
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(model_name_or_path,trust_remote_code=True)
```

类似的，直接使用 from_pretrained 方法加载即可，此处的 model_name_or_path 即为下载好的参数的本地路径。

我们还需要初始化一个 tokenizer。此处，我们直接使用 Qwen-2.5-1.5B 对应的 tokenizer 参数即可：

```python
# 加载一个预训练好的 tokenizer
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
```

加载好的 tokenizer 即可直接使用，对任意文本进行分词处理。

##### 6.1.3 预训练数据处理

与第五章类似，我们使用出门问问序列猴子开源数据集作为预训练数据集，可以用与第五章一致的方式进行数据集的下载和解压。HuggingFace 的 datasets 库是和 transformers 框架配套的、用于数据下载和处理的第三方库。我们可以直接使用 datasets 的 load_dataset 函数来加载预训练数据：

```python
# 加载预训练数据
from datasets import load_dataset

ds = load_dataset('json', data_files='/mobvoi_seq_monkey_general_open_corpus.jsonl')
```

注意，由于数据集较大，加载可能会出现时间较长或内存不够的情况，建议前期测试时将预训练数据集拆分一部分出来进行测试。加载出来的 ds 是一个 DatasetDict 对象，加载的数据会默认保存在 `train` 键对应的值中，可以通过以下代码查看：

```python
ds["train"][0]
```


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/1-7.png)
图6.7 数据集展示


可以通过 feature 属性查看数据集的特征（也就是列），这里需要保存一下数据集的列名，因为后续数据处理时，再将文本 tokenize 之后，需要移除原先的文本：

```python
# 查看特征
column_names = list(ds["train"].features)
# columnes_name:["text"]
```

接着使用加载好的 tokenizer 对数据集进行处理，此处使用 map 函数来进行批量处理：

```python
# 对数据集进行 tokenize
def tokenize_function(examples):
    # 使用预先加载的 tokenizer 进行分词
    output = tokenizer([item for item in examples["text"]])
    return output

# 批量处理
tokenized_datasets = ds.map(
    tokenize_function,
    batched=True,
    num_proc=10,
    remove_columns=column_names,
    load_from_cache_file=True,
    desc="Running tokenizer on dataset",
)
```

处理完成后的数据集会包括'input_ids', 'attention_mask'两列，分别是文本 tokenize 之后的数值序列和注意力掩码（标识是否 padding）。map 方法会通过 remove_columns 参数将原先的‘text’移除，训练中不再使用。

由于预训练一般为 CLM 任务，一次性学习多个样本的序列语义不影响模型性能，且训练数据量大、训练时间长，对训练效率要求比较高。在预训练过程中，一般会把多个文本段拼接在一起，处理成统一长度的文本块，再对每个文本块进行训练。在这里，我们实现一个拼接函数将文本块拼接到 2048个 token 长度，再通过 map 方法来进行批量处理：

```python
# 预训练一般将文本拼接成固定长度的文本段
from itertools import chain

# 这里我们取块长为 2048
block_size = 2048

def group_texts(examples):
    # 将文本段拼接起来
    concatenated_examples = {k: list(chain(*examples[k])) for k in examples.keys()}
    # 计算拼起来的整体长度
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    # 如果长度太长，进行分块
    if total_length >= block_size:
        total_length = (total_length // block_size) * block_size
    # 按 block_size 进行切分
    result = {
        k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
        for k, t in concatenated_examples.items()
    }
    # CLM 任务，labels 和 input 是相同的
    result["labels"] = result["input_ids"].copy()
    return result

# 批量处理
lm_datasets = tokenized_datasets.map(
    group_texts,
    batched=True,
    num_proc=10,
    load_from_cache_file=True,
    desc=f"Grouping texts in chunks of {block_size}",
    batch_size = 40000,
)
train_dataset = lm_datasets["train"]
```

处理得到的 train_dataset 就是一个可直接用于 CLM Pretrain 的预训练数据集了，其每个样本长度为 2048个 token。

##### 6.1.4 使用 Trainer 进行训练

接下来，我们使用 transformers 提供的 Trainer 类进行训练。Trainer 封装了模型的训练逻辑，且做了较好的效率优化、可视化等工作，可以高效、便捷地完成 LLM 的训练。

首先我们需要配置训练的超参数，使用 TrainingArguments 类来实例化一个参数对象：

```python
from transformers import TrainingArguments
# 配置训练参数

training_args = TrainingArguments(
    output_dir="output",# 训练参数输出路径
    per_device_train_batch_size=4,# 训练的 batch_size
    gradient_accumulation_steps=4,# 梯度累计步数，实际 bs = 设置的 bs * 累计步数
    logging_steps=10,# 打印 loss 的步数间隔
    num_train_epochs=1,# 训练的 epoch 数
    save_steps=100, # 保存模型参数的步数间隔
    learning_rate=1e-4,# 学习率
    gradient_checkpointing=True# 开启梯度检查点
)
```

然后基于初始化的 model、tokenzier 和 training_args，并传入处理好的训练数据集，实例化一个 trainer 对象：

```python
from transformers import Trainer, default_data_collator
from torchdata.datapipes.iter import IterableWrapper

# 训练器
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset= IterableWrapper(train_dataset),
    eval_dataset= None,
    tokenizer=tokenizer,
    # 默认为 MLM 的 collator，使用 CLM 的 collater
    data_collator=default_data_collator
)
```

再使用 train 方法，即会按照配置好的训练超参进行训练和保存：

```python
trainer.train()
```

> 注：上述代码存放于 `./code/pretrain.ipynb` 文件中。

##### 6.1.5 使用 DeepSpeed 实现分布式训练

由于预训练规模大、时间长，一般不推荐使用 Jupyter Notebook 来运行，容易发生中断。且由于预训练规模大，一般需要使用多卡进行分布式训练，否则训练时间太长。在这里，我们介绍如何基于上述代码，使用 DeepSpeed 框架实现分布式训练，从而完成业界可用的 LLM Pretrain。

长时间训练一般使用 bash 脚本设定超参，再启动写好的 python 脚本实现训练。我们使用一个 Python 脚本（`./code/pretrain.py`）来实现训练全流程。

先导入所需第三方库：

```python
import logging
import math
import os
import sys
from dataclasses import dataclass, field
from torchdata.datapipes.iter import IterableWrapper
from itertools import chain
import deepspeed
from typing import Optional,List

import datasets
import pandas as pd
import torch
from datasets import load_dataset
import transformers
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    HfArgumentParser,
    Trainer,
    TrainingArguments,
    default_data_collator,
    set_seed,
)
import datetime
from transformers.testing_utils import CaptureLogger
from transformers.trainer_utils import get_last_checkpoint
import swanlab
```

首先需要定义几个超参的类型，用于处理 sh 脚本中设定的超参值。由于 transformers 本身有 TraingingArguments 类，其中包括了训练的一些必备超参数。我们这里只需定义 TrainingArguments 中未包含的超参即可，主要包括模型相关的超参（定义在 ModelArguments）和数据相关的超参（定义在 DataTrainingArguments）：

```python
# 超参类
@dataclass
class ModelArguments:
    """
    关于模型的参数
    """

    model_name_or_path: Optional[str] = field(
        default=None,
        metadata={
            "help": (
                "后训练使用，为预训练模型参数地址"
            )
        },
    )
    config_name: Optional[str] = field(
        default=None, metadata={"help": "预训练使用，Config 文件地址"}
    )
    tokenizer_name: Optional[str] = field(
        default=None, metadata={"help": "预训练 Tokenizer 地址"}
    )
    torch_dtype: Optional[str] = field(
        default=None,
        metadata={
            "help": (
                "模型训练使用的数据类型，推荐 bfloat16"
            ),
            "choices": ["auto", "bfloat16", "float16", "float32"],
        },
    )


@dataclass
class DataTrainingArguments:
    """
    关于训练的参数
    """

    train_files: Optional[List[str]]  = field(default=None, metadata={"help": "训练数据路径"})
    block_size: Optional[int] = field(
        default=None,
        metadata={
            "help": (
                "设置的文本块长度"
            )
        },
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "预处理使用线程数."},
    )
```

然后即可定义一个主函数实现上述训练过程的封装。首先通过 transformers 提供的 HfArgumentParser 工具来加载 sh 脚本中设定的超参：

```python
# 加载脚本参数
parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
model_args, data_args, training_args = parser.parse_args_into_dataclasses()
```

在大规模的训练中，一般使用 log 来保存训练过程的信息，一般不推荐使用 print 直接打印，容易发生关键训练信息的丢失。这里，我们直接使用 python 自带的 logging 库来实现日志记录。首先需要进行 log 的设置：

```python
# 设置日志
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)

# 将日志级别设置为 INFO
transformers.utils.logging.set_verbosity_info()
log_level = training_args.get_process_log_level()
logger.setLevel(log_level)
datasets.utils.logging.set_verbosity(log_level)
transformers.utils.logging.set_verbosity(log_level)
transformers.utils.logging.enable_default_handler()
transformers.utils.logging.enable_explicit_format()
```

这里将日志的级别设置为 INFO。logging 的日志共有 DEBUG、INFO、WARNING、ERROR 以及 CRITICAL 五个级别，将日志设置为哪个级别，就会只输出该级别及该级别之上的信息。设置完成后，在需要记录日志的地方，直接使用 logger 即可，记录时会指定记录日志的级别，例如：

```python
# 训练整体情况记录
logger.warning(
    f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
    + f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
)
logger.info(f"Training/evaluation parameters {training_args}")
```

后续就不再赘述脚本中的日志记录。

在大规模训练中，发生中断是往往难以避免的，训练一般会固定间隔保存 checkpoint，中断之后基于最近的 checkpoint 恢复训练即可。因此，我们需要首先检测是否存在旧的 checkpoint 并从 checkpoint 恢复训练：

```python
# 检查 checkpoint
last_checkpoint = None
if os.path.isdir(training_args.output_dir):
    # 使用 transformers 自带的 get_last_checkpoint 自动检测
    last_checkpoint = get_last_checkpoint(training_args.output_dir)
    if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
        raise ValueError(
            f"输出路径 ({training_args.output_dir}) 非空 "
        )
    elif last_checkpoint is not None and training_args.resume_from_checkpoint is None:
        logger.info(
            f"从 {last_checkpoint}恢复训练"
        )
```

接着以上文介绍过的方式初始化模型，此处将从零初始化和基于已有预训练模型初始化包装在一起：

```python
# 初始化模型
if model_args.config_name is not None:
    # from scrach
    config = AutoConfig.from_pretrained(model_args.config_name)
    logger.warning("你正在从零初始化一个模型")
    logger.info(f"模型参数配置地址：{model_args.config_name}")
    logger.info(f"模型参数：{config}")
    model = AutoModelForCausalLM.from_config(config,trust_remote_code=True)
    n_params = sum({p.data_ptr(): p.numel() for p in model.parameters()}.values())
    logger.info(f"预训练一个新模型 - Total size={n_params/2**20:.2f}M params")
elif model_args.model_name_or_path is not None:
    logger.warning("你正在初始化一个预训练模型")
    logger.info(f"模型参数地址：{model_args.model_name_or_path}")
    model = AutoModelForCausalLM.from_pretrained(model_args.model_name_or_path,trust_remote_code=True)
    n_params = sum({p.data_ptr(): p.numel() for p in model.parameters()}.values())
    logger.info(f"继承一个预训练模型 - Total size={n_params/2**20:.2f}M params")
else:
    logger.error("config_name 和 model_name_or_path 不能均为空")
    raise ValueError("config_name 和 model_name_or_path 不能均为空")
```

再类似的进行 tokenizer 的加载和预训练数据的处理。该部分和上文完全一致，此处不再赘述，读者可以在代码中详细查看细节。类似的，使用 Trainer 进行训练：

```python
logger.info("初始化 Trainer")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset= IterableWrapper(train_dataset),
    tokenizer=tokenizer,
    data_collator=default_data_collator
)

# 从 checkpoint 加载
checkpoint = None
if training_args.resume_from_checkpoint is not None:
    checkpoint = training_args.resume_from_checkpoint
elif last_checkpoint is not None:
        checkpoint = last_checkpoint

logger.info("开始训练")
train_result = trainer.train(resume_from_checkpoint=checkpoint)
trainer.save_model()
```
注意，由于上文检测了是否存在 checkpoint，此处使用 resume_from_checkpoint 来实现从 checkpoint 恢复训练的功能。

由于在大规模训练中监测训练进度、loss 下降趋势尤为重要，在脚本中，我们使用了 swanlab 作为训练检测的工具。在脚本开始进行了 swanlab 的初始化：

```python
# 初始化 SwanLab
swanlab.init(project="pretrain", experiment_name="from_scrach")
```

在启动训练后，终端会输出 swanlab 监测的 url，点击即可观察训练进度。此处不再赘述 swanlab 的使用细节，欢迎读者查阅相关的资料说明。

完成上述代码后，我们使用一个 sh 脚本（`./code/pretrain.sh`）定义超参数的值，并通过 Deepspeed 启动训练，从而实现高效的多卡分布式训练：

```bash
# 设置可见显卡
CUDA_VISIBLE_DEVICES=0,1

deepspeed pretrain.py \
    --config_name autodl-tmp/qwen-1.5b \
    --tokenizer_name autodl-tmp/qwen-1.5b \
    --train_files autodl-tmp/dataset/pretrain_data/mobvoi_seq_monkey_general_open_corpus_small.jsonl \
    --per_device_train_batch_size 16 \
    --gradient_accumulation_steps 4 \
    --do_train \
    --output_dir autodl-tmp/output/pretrain \
    --evaluation_strategy  no \
    --learning_rate 1e-4 \
    --num_train_epochs 1 \
    --warmup_steps 200 \
    --logging_dir autodl-tmp/output/pretrain/logs \
    --logging_strategy steps \
    --logging_steps 5 \
    --save_strategy steps \
    --save_steps 100 \
    --preprocessing_num_workers 10 \
    --save_total_limit 1 \
    --seed 12 \
    --block_size 2048 \
    --bf16 \
    --gradient_checkpointing \
    --deepspeed ./ds_config_zero2.json \
    --report_to swanlab
    # --resume_from_checkpoint ${output_model}/checkpoint-20400 \
```
在安装了 Deepspeed 第三方库后，可以直接通过 Deepspeed 命令来启动多卡训练。上述脚本命令主要是定义了各种超参数的值，可参考使用。在第四章中，我们介绍了 DeepSpeed 分布式训练的原理和 ZeRO 阶段设置，在这里，我们使用 ZeRO-2 进行训练。此处加载了 `ds_config_zero.json` 作为 DeepSpeed 的配置参数：

```json
{
    "fp16": {
        "enabled": "auto",
        "loss_scale": 0,
        "loss_scale_window": 1000,
        "initial_scale_power": 16,
        "hysteresis": 2,
        "min_loss_scale": 1
    },
    "bf16": {
        "enabled": "auto"
    },
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": "auto",
            "betas": "auto",
            "eps": "auto",
            "weight_decay": "auto"
        }
    },

    "scheduler": {
        "type": "WarmupLR",
        "params": {
            "warmup_min_lr": "auto",
            "warmup_max_lr": "auto",
            "warmup_num_steps": "auto"
        }
    },

    "zero_optimization": {
        "stage": 2,
        "offload_optimizer": {
            "device": "none",
            "pin_memory": true
        },
        "allgather_partitions": true,
        "allgather_bucket_size": 2e8,
        "overlap_comm": true,
        "reduce_scatter": true,
        "reduce_bucket_size": 2e8,
        "contiguous_gradients": true
    },

    "gradient_accumulation_steps": "auto",
    "gradient_clipping": "auto",
    "steps_per_print": 100,
    "train_batch_size": "auto",
    "train_micro_batch_size_per_gpu": "auto",
    "wall_clock_breakdown": false
}
```

最后，在终端 bash 运行该 `pretrain.sh` 脚本即可开始训练。

#### 6.2 模型有监督微调

在上一节，我们介绍了如何使用 Transformers 框架快速、高效地进行模型预训练。在本部分，我们将基于上部分内容，介绍如何使用 Transformers 框架对预训练好的模型进行有监督微调。

##### 6.2.1 Pretrain VS SFT

首先需要回顾一下，对 LLM 进行预训练和进行有监督微调的核心差异在于什么。在第四章中提到过，目前成型的 LLM 一般通过 Pretrain-SFT-RLHF 三个阶段来训练，在 Pretrain 阶段，会对海量无监督文本进行自监督建模，来学习文本语义规则和文本中的世界知识；在 SFT 阶段，一般通过对 Pretrain 好的模型进行指令微调，即训练模型根据用户指令完成对应任务，从而使模型能够遵循用户指令，根据用户指令进行规划、行动和输出。因此，Pretrain 和 SFT 均使用 CLM 建模，其核心差异在于，Pretrain 使用海量无监督文本进行训练，模型直接对文本执行“预测下一个 token”的任务；而 SFT 使用构建成对的指令对数据，模型根据输入的指令，建模后续的输出。反映到具体的训练实现上，Pretrain 会对全部 text 进行 loss 计算，要求模型对整个文本实现建模预测；而 SFT 仅对输出进行 loss 计算，不计算指令部分的 loss。

因此，相较于上一节完成的 Pretrain 代码，SFT 部分仅需要修改数据处理环节，实现对指令对数据转化为训练样本的构建，其余部分和 Pretrain 是完全一致的实现逻辑。本部分代码脚本为`./code/finetune.py`。

##### 6.2.2 微调数据处理

同样与第五章类似，我们此处使用贝壳开源的 BelleGroup 数据集进行 SFT。

在 SFT 过程中，我们会定义一个 Chat Template，这个 Template 即表示了如何将对话数据转化为一个模型可以建模拟合的文本序列。当我们使用做过 SFT 的模型进行下游任务微调时，一般需要查看该模型的 Chat Template 并进行适配，即是为了不损伤其在 SFT 中学到的指令遵循能力。由于我们此处使用 Pretrain 模型进行 SFT，可以自定义一个 Chat Template。由于我们使用了 Qwen-2.5-1.5B 模型结构进行 Pretrain，此处我们沿承使用 Qwen-2.5 的 Chat Template。如果读者没有足够的资源进行上一部分模型的 Pretrain 的话，此处也可以使用官方的 Qwen-2.5-1.5B 模型作为 SFT 的基座模型。

我们首先定义几个特殊 token，特殊 token 在模型进行拟合中有特殊的作用，包括文本序列开始（BOS）、文本序列结束（EOS）、换行符等。定义特殊 token，有助于避免模型在拟合过程中的语义混淆：

```python

# 不同的 tokenizer 需要特别定义
# BOS
im_start = tokenizer("<|im_start|>").input_ids
# EOS
im_end = tokenizer("<|im_end|>").input_ids
# PAD
IGNORE_TOKEN_ID = tokenizer.pad_token_id
# 换行符
nl_tokens = tokenizer('\n').input_ids
# 角色标识符
_system = tokenizer('system').input_ids + nl_tokens
_user = tokenizer('human').input_ids + nl_tokens
_assistant = tokenizer('assistant').input_ids + nl_tokens
```

Qwen 系列的 Chat Template 一般有三个对话角色：System、User 和 Assistant。System 是系统提示词，负责激活模型的能力，默认为“You are a helpful assistant.”，一般不会在 SFT 过程中更改使用。User 即为用户给出的提示词，此处由于数据集中的对话角色为 “human”，我们将 “user” 修改为了“human”。Assistant 即为 LLM 给出的回复，也就是模型在 SFT 过程中需要拟合的文本。

接着，由于该数据集是一个多轮对话数据集，我们需要对多轮对话进行拼接处理，将多轮对话拼接到一个文本序列中：

```python
# 拼接多轮对话
input_ids, targets = [], []
# 多个样本
for i in tqdm(range(len(sources))):
    # source 为一个多轮对话样本
    source = sources[i]
    # 从 user 开始
    if source[0]["from"] != "human":
        source = source[1:]
    # 分别是输入和输出
    input_id, target = [], []
    # system: 【BOS】system\nYou are a helpful assistant.【EOS】\n
    system = im_start + _system + tokenizer(system_message).input_ids + im_end + nl_tokens
    input_id += system
    # system 不需要拟合
    target += im_start + [IGNORE_TOKEN_ID] * (len(system)-3) + im_end + nl_tokens
    assert len(input_id) == len(target)
    # 依次拼接
    for j, sentence in enumerate(source):
        # sentence 为一轮对话
        role = roles[sentence["from"]]
        # user：<|im_start|>human\ninstruction【EOS】\n
        # assistant：<|im_start|>assistant\nresponse【EOS】\n
        _input_id = tokenizer(role).input_ids + nl_tokens + \
            tokenizer(sentence["value"]).input_ids + im_end + nl_tokens
        input_id += _input_id
        if role == '<|im_start|>human':
            # user 不需要拟合
            _target = im_start + [IGNORE_TOKEN_ID] * (len(_input_id)-3) + im_end + nl_tokens
        elif role == '<|im_start|>assistant':
            # assistant 需要拟合
            _target = im_start + [IGNORE_TOKEN_ID] * len(tokenizer(role).input_ids) + \
                _input_id[len(tokenizer(role).input_ids)+1:-2] + im_end + nl_tokens
        else:
            print(role)
            raise NotImplementedError
        target += _target
    assert len(input_id) == len(target)
    # 最后进行 PAD
    input_id += [tokenizer.pad_token_id] * (max_len - len(input_id))
    target += [IGNORE_TOKEN_ID] * (max_len - len(target))
    input_ids.append(input_id[:max_len])
    targets.append(target[:max_len])
```
上述代码沿承了 Qwen 的 Chat Template 逻辑，读者也可以根据自己的偏好进行修改，其核心点在于 User 的文本不需要拟合，因此 targets 中 User 对应的文本内容是使用的 IGNORE_TOKEN_ID 进行遮蔽，而 Assistant 对应的文本内容则是文本原文，是需要计算 loss 的。目前主流 LLM IGNORE_TOKEN_ID 一般设置为 -100。

完成拼接后，将 tokenize 后的数值序列转化为 `Torch.tensor`，再拼接成 Dataset 所需的字典返回即可：

```python
input_ids = torch.tensor(input_ids)
targets = torch.tensor(targets)

return dict(
    input_ids=input_ids,
    labels=targets,
    attention_mask=input_ids.ne(tokenizer.pad_token_id),
)
```

完成上述处理逻辑后，需要自定义一个 Dataset 类，在该类中调用该逻辑进行数据的处理：

```python
class SupervisedDataset(Dataset):

    def __init__(self, raw_data, tokenizer, max_len: int):
        super(SupervisedDataset, self).__init__()
        # 加载并预处理数据
        sources = [example["conversations"] for example in raw_data]
        # preprocess 即上文定义的数据预处理逻辑
        data_dict = preprocess(sources, tokenizer, max_len)

        self.input_ids = data_dict["input_ids"]
        self.labels = data_dict["labels"]
        self.attention_mask = data_dict["attention_mask"]

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, i) -> Dict[str, torch.Tensor]:
        return dict(
            input_ids=self.input_ids[i],
            labels=self.labels[i],
            attention_mask=self.attention_mask[i],
        )
```

该类继承自 Torch 的 Dataset 类，可以直接在 Trainer 中使用。完成数据处理后，基于上一节脚本，修改数据处理逻辑即可，后续模型训练等几乎完全一致，此处附上主函数逻辑：

```python
# 加载脚本参数
parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
model_args, data_args, training_args = parser.parse_args_into_dataclasses()

# 初始化 SwanLab
swanlab.init(project="sft", experiment_name="qwen-1.5b")

# 设置日志
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)

# 将日志级别设置为 INFO
transformers.utils.logging.set_verbosity_info()
log_level = training_args.get_process_log_level()
logger.setLevel(log_level)
datasets.utils.logging.set_verbosity(log_level)
transformers.utils.logging.set_verbosity(log_level)
transformers.utils.logging.enable_default_handler()
transformers.utils.logging.enable_explicit_format()

# 训练整体情况记录
logger.warning(
    f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
    + f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
)
logger.info(f"Training/evaluation parameters {training_args}")

# 检查 checkpoint
last_checkpoint = None
if os.path.isdir(training_args.output_dir):
    last_checkpoint = get_last_checkpoint(training_args.output_dir)
    if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
        raise ValueError(
            f"输出路径 ({training_args.output_dir}) 非空 "
        )
    elif last_checkpoint is not None and training_args.resume_from_checkpoint is None:
        logger.info(
            f"从 {last_checkpoint}恢复训练"
        )

# 设置随机数种子.
set_seed(training_args.seed)

# 初始化模型
logger.warning("加载预训练模型")
logger.info(f"模型参数地址：{model_args.model_name_or_path}")
model = AutoModelForCausalLM.from_pretrained(model_args.model_name_or_path,trust_remote_code=True)
n_params = sum({p.data_ptr(): p.numel() for p in model.parameters()}.values())
logger.info(f"继承一个预训练模型 - Total size={n_params/2**20:.2f}M params")

# 初始化 Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path)
logger.info("完成 tokenizer 加载")

# 加载微调数据
with open(data_args.train_files) as f:
    lst = [json.loads(line) for line in f.readlines()[:10000]]
logger.info("完成训练集加载")
logger.info(f"训练集地址：{data_args.train_files}")
logger.info(f'训练样本总数:{len(lst)}')
# logger.info(f"训练集采样：{ds["train"][0]}")

train_dataset = SupervisedDataset(lst, tokenizer=tokenizer, max_len=2048)

logger.info("初始化 Trainer")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset= IterableWrapper(train_dataset),
    tokenizer=tokenizer
)

# 从 checkpoint 加载
checkpoint = None
if training_args.resume_from_checkpoint is not None:
    checkpoint = training_args.resume_from_checkpoint
elif last_checkpoint is not None:
        checkpoint = last_checkpoint

logger.info("开始训练")
train_result = trainer.train(resume_from_checkpoint=checkpoint)
trainer.save_model()
```

启动方式也同样在 sh 脚本中使用 deepspeed 启动即可，此处不再赘述，源码见 ./code/finetune.sh。

#### 6.3 高效微调

在前面几节，我们详细介绍了基于 Transformers 框架对模型进行 Pretrain、SFT 以及 RLHF 的原理和实践细节。但是，由于 LLM 参数量大，训练数据多，通过上述方式对模型进行训练（主要指 SFT 及 RLHF）需要调整模型全部参数，资源压力非常大。对资源有限的企业或课题组来说，如何高效、快速对模型进行领域或任务的微调，以低成本地使用 LLM 完成目标任务，是非常重要的。

##### 6.3.1 高效微调方案

针对全量微调的昂贵问题，目前主要有两种解决方案：

**Adapt Tuning**。即在模型中添加 Adapter 层，在微调时冻结原参数，仅更新 Adapter 层。

具体而言，其在预训练模型每层中插入用于下游任务的参数，即 Adapter 模块，在微调时冻结模型主体，仅训练特定于任务的参数，如图6.8所示。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/3-1.png)
图6.8 Adapt Tuning


每个 Adapter 模块由两个前馈子层组成，第一个前馈子层将 Transformer 块的输出作为输入，将原始输入维度 $d$ 投影到 $m$，通过控制 $m$ 的大小来限制 Adapter 模块的参数量，通常情况下 $m << d$。在输出阶段，通过第二个前馈子层还原输入维度，将 $m$ 重新投影到 $d$，作为 Adapter 模块的输出(如上图右侧结构)。

LoRA 事实上就是一种改进的 Adapt Tuning 方法。但 Adapt Tuning 方法存在推理延迟问题，由于增加了额外参数和额外计算量，导致微调之后的模型计算速度相较原预训练模型更慢。

**Prefix Tuning**。该种方法固定预训练 LM，为 LM 添加可训练，任务特定的前缀，这样就可以为不同任务保存不同的前缀，微调成本也小。具体而言，在每一个输入 token 前构造一段与下游任务相关的 virtual tokens 作为 prefix，在微调时只更新 prefix 部分的参数，而其他参数冻结不变。

也是目前常用的微量微调方法的 Ptuning，其实就是 Prefix Tuning 的一种改进。但 Prefix Tuning 也存在固定的缺陷：模型可用序列长度减少。由于加入了 virtual tokens，占用了可用序列长度，因此越高的微调质量，模型可用序列长度就越低。

##### 6.3.2 LoRA 微调

如果一个大模型是将数据映射到高维空间进行处理，这里假定在处理一个细分的小任务时，是不需要那么复杂的大模型的，可能只需要在某个子空间范围内就可以解决，那么也就不需要对全量参数进行优化了，我们可以定义当对某个子空间参数进行优化时，能够达到全量参数优化的性能的一定水平（如90%精度）时，那么这个子空间参数矩阵的秩就可以称为对应当前待解决问题的本征秩（intrinsic rank）。

预训练模型本身就隐式地降低了本征秩，当针对特定任务进行微调后，模型中权重矩阵其实具有更低的本征秩（intrinsic rank）。同时，越简单的下游任务，对应的本征秩越低。（[Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning](https://arxiv.org/abs/2012.13255)）因此，权重更新的那部分参数矩阵尽管随机投影到较小的子空间，仍然可以有效的学习，可以理解为针对特定的下游任务这些权重矩阵就不要求满秩。我们可以通过优化密集层在适应过程中变化的秩分解矩阵来间接训练神经网络中的一些密集层，从而实现仅优化密集层的秩分解矩阵来达到微调效果。

例如，假设预训练参数为 $\theta^D_0$，在特定下游任务上密集层权重参数矩阵对应的本征秩为 $\theta^d$，对应特定下游任务微调参数为 $\theta^D$，那么有：

$$\theta^D = \theta^D_0 + \theta^d M$$

这个 $M$ 即为 LoRA 优化的秩分解矩阵。

想对于其他高效微调方法，LoRA 存在以下优势：

1. 可以针对不同的下游任务构建小型 LoRA 模块，从而在共享预训练模型参数基础上有效地切换下游任务。
2. LoRA 使用自适应优化器（Adaptive Optimizer），不需要计算梯度或维护大多数参数的优化器状态，训练更有效、硬件门槛更低。
3. LoRA 使用简单的线性设计，在部署时将可训练矩阵与冻结权重合并，不存在推理延迟。
4. LoRA 与其他方法正交，可以组合。

因此，LoRA 成为目前高效微调 LLM 的主流方法，尤其是对于资源受限、有监督训练数据受限的情况下，LoRA 微调往往会成为 LLM 微调的首选方法。

##### 6.3.3 LoRA 微调的原理

###### （1）低秩参数化更新矩阵

LoRA 假设权重更新的过程中也有一个较低的本征秩，对于预训练的权重参数矩阵 $W0 \in R^{d \times k}$ ($d$ 为上一层输出维度，$k$ 为下一层输入维度)，使用低秩分解来表示其更新：

$$W_0 + {\Delta}W = W_0 + BA \space\space  where \space B \in R^{d \times r}, A \in R^{r \times k}$$

在训练过程中，$W_0$ 冻结不更新，$A$、$B$ 包含可训练参数。

因此，LoRA 的前向传递函数为：

$$h = W_0 x + \Delta W x = W_0 x + B A x$$

在开始训练时，对 $A$ 使用随机高斯初始化，对 $B$ 使用零初始化，然后使用 Adam 进行优化。

训练思路如图6.9所示：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/6-images/3-2.jpg)
图6.9 LoRA


###### （2）应用于 Transformer

在 Transformer 结构中，LoRA 技术主要应用在注意力模块的四个权重矩阵：$W_q$、$W_k$、$W_v$、$W_0$，而冻结 MLP 的权重矩阵。

通过消融实验发现同时调整 $W_q$ 和 $W_v$ 会产生最佳结果。

在上述条件下，可训练参数个数为：

$$\Theta = 2 \times L_{LoRA} \times d_{model} \times r$$

其中，$L_{LoRA}$ 为应用 LoRA 的权重矩阵的个数，$d_{model}$ 为 Transformer 的输入输出维度，$r$ 为设定的 LoRA 秩。

一般情况下，r 取到 4、8、16。

##### 6.3.4 LoRA 的代码实现

目前一般通过 peft 库来实现模型的 LoRA 微调。peft 库是 huggingface 开发的第三方库，其中封装了包括 LoRA、Adapt Tuning、P-tuning 等多种高效微调方法，可以基于此便捷地实现模型的 LoRA 微调。

本文简单解析 peft 库中的 LoRA 微调代码，简单分析 LoRA 微调的代码实现。

###### （1）实现流程

LoRA 微调的内部实现流程主要包括以下几个步骤：

1. 确定要使用 LoRA 的层。peft 库目前支持调用 LoRA 的层包括：nn.Linear、nn.Embedding、nn.Conv2d 三种。

2. 对每一个要使用 LoRA 的层，替换为 LoRA 层。所谓 LoRA 层，实则是在该层原结果基础上增加了一个旁路，通过低秩分解（即矩阵 $A$ 和矩阵 $B$）来模拟参数更新。

3. 冻结原参数，进行微调，更新 LoRA 层参数。

###### （2）确定 LoRA 层

在进行 LoRA 微调时，首先需要确定 LoRA 微调参数，其中一个重要参数即是 target_modules。target_modules 一般是一个字符串列表，每一个字符串是需要进行 LoRA 的层名称，例如：

```python
target_modules = ["q_proj","v_proj"]
```

这里的 q_proj 即为注意力机制中的 $W_q$， v_proj 即为注意力机制中的 $W_v$。我们可以根据模型架构和任务要求自定义需要进行 LoRA 操作的层。

在创建 LoRA 模型时，会获取该参数，然后在原模型中找到对应的层，该操作主要通过使用 re 对层名进行正则匹配实现：

```python
# 找到模型的各个组件中，名字里带"q_proj"，"v_proj"的
target_module_found = re.fullmatch(self.peft_config.target_modules, key)
# 这里的 key，是模型的组件名
```

###### （3）替换 LoRA 层

对于找到的每一个目标层，会创建一个新的 LoRA 层进行替换。

LoRA 层在具体实现上，是定义了一个基于 Lora 基类的 Linear 类，该类同时继承了 nn.Linear 和 LoraLayer。LoraLayer 即是 Lora 基类，其主要构造了 LoRA 的各种超参：

```python
class LoraLayer:
    def __init__(
        self,
        r: int, # LoRA 的秩
        lora_alpha: int, # 归一化参数
        lora_dropout: float, # LoRA 层的 dropout 比例
        merge_weights: bool, # eval 模式中，是否将 LoRA 矩阵的值加到原权重矩阵上
    ):
        self.r = r
        self.lora_alpha = lora_alpha
        # Optional dropout
        if lora_dropout > 0.0:
            self.lora_dropout = nn.Dropout(p=lora_dropout)
        else:
            self.lora_dropout = lambda x: x
        # Mark the weight as unmerged
        self.merged = False
        self.merge_weights = merge_weights
        self.disable_adapters = False

```
nn.Linear 就是 Pytorch 的线性层实现。Linear 类就是具体的 LoRA 层，其主要实现如下：

```python
class Linear(nn.Linear, LoraLayer):
    # LoRA 层
    def __init__(
        self,
        in_features: int,
        out_features: int,
        r: int = 0,
        lora_alpha: int = 1,
        lora_dropout: float = 0.0,
        fan_in_fan_out: bool = False,
        merge_weights: bool = True,
        **kwargs,
    ):
        # 继承两个基类的构造函数
        nn.Linear.__init__(self, in_features, out_features, **kwargs)
        LoraLayer.__init__(self, r=r, lora_alpha=lora_alpha, lora_dropout=lora_dropout, merge_weights=merge_weights)

        self.fan_in_fan_out = fan_in_fan_out
        # Actual trainable parameters
        if r > 0:
            # 参数矩阵 A
            self.lora_A = nn.Linear(in_features, r, bias=False)
            # 参数矩阵 B
            self.lora_B = nn.Linear(r, out_features, bias=False)
            # 归一化系数
            self.scaling = self.lora_alpha / self.r
            # 冻结原参数，仅更新 A 和 B
            self.weight.requires_grad = False
        # 初始化 A 和 B
        self.reset_parameters()
        if fan_in_fan_out:
            self.weight.data = self.weight.data.T

```

替换时，直接将原层的 weight 和 bias 复制给新的 LoRA 层，再将新的 LoRA 层分配到指定设备即可。

###### （4）训练

实现了 LoRA 层的替换后，进行微调训练即可。由于在 LoRA 层中已冻结原参数，在训练中只有 A 和 B 的参数会被更新，从而实现了高效微调。训练的整体过程与原 Fine-tune 类似，此处不再赘述。由于采用了 LoRA 方式，forward 函数也会对应调整：

```python
    def forward(self, x: torch.Tensor):
        if self.disable_adapters:
            if self.r > 0 and self.merged:
                self.weight.data -= (
                    transpose(self.lora_B.weight @ self.lora_A.weight, self.fan_in_fan_out) * self.scaling
                )
                self.merged = False

            return F.linear(x, transpose(self.weight, self.fan_in_fan_out), bias=self.bias)
        '''主要分支'''
        elif self.r > 0 and not self.merged:
            result = F.linear(x, transpose(self.weight, self.fan_in_fan_out), bias=self.bias)
            if self.r > 0:
                result += self.lora_B(self.lora_A(self.lora_dropout(x))) * self.scaling
            return result
        else:
            return F.linear(x, transpose(self.weight, self.fan_in_fan_out), bias=self.bias)

```
上述代码由于考虑到参数合并问题，有几个分支，此处我们仅阅读第二个分支即 elif 分支即可。基于 LoRA 的前向计算过程如前文公式所示，首先计算原参数与输入的乘积，再加上 A、B 分别与输入的乘积即可。

##### 6.3.5 使用 peft 实现 LoRA 微调

peft 进行了很好的封装，支持我们便捷、高效地对大模型进行微调。此处以第二节的 LLM SFT 为例，简要介绍如何使用 peft 对大模型进行微调。如果是应用在 RLHF 上，整体思路是一致的。

首先加载所需使用库：

```python
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
from peft import get_peft_model, LoraConfig, TaskType, PeftModel
from transformers import Trainer
```

其次加载原模型与原 tokenizer，此处和第二节一致：

```python
# 加载基座模型
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = AutoModel.from_pretrained(
    MODEL_PATH, trust_remote_code=True
)
```

接着，设定 peft 参数：

```python
peft_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM,
            inference_mode=False,
            r=8,
            lora_alpha=32,
            lora_dropout=0.1,
        )
```

注意，对不同的模型，LoRA 参数可能有所区别。例如，对于 ChatGLM，无需指定 target_modeules，peft 可以自行找到；对于 BaiChuan，就需要手动指定。task_type 是模型的任务类型，大模型一般都是 CAUSAL_LM 即传统语言模型。

然后获取 LoRA 模型：

```python
model = get_peft_model(model, peft_config)
```

此处的 get_peft_model 的底层操作，即为上文分析的具体实现。

最后使用 transformers 提供的 Trainer 进行训练即可，训练占用的显存就会有大幅度的降低：

```python
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset= IterableWrapper(train_dataset),
    tokenizer=tokenizer
)
trainer.train()
```

如果是应用在 DPO、KTO 上，则也相同的加入 LoRA 参数并通过 `get_peft_model` 获取一个 LoRA 模型即可，其他的不需要进行任何修改。但要注意的是，LoRA 微调能够大幅度降低显卡占用，且在下游任务适配上能够取得较好的效果，但如果是需要学习对应知识的任务，LoRA 由于只调整低秩矩阵，难以实现知识的注入，一般效果不佳，因此不推荐使用 LoRA 进行模型预训练或后训练。

#### 6.4 偏好对齐

在前文中，我们已经完成了 Pretrain、SFT 以及高效微调三条训练主线。对于一个面向真实用户的大模型来说，这些步骤通常还不够。模型虽然已经具备了较强的语言建模能力和基础指令跟随能力，但在回答风格、安全性、帮助性和稳定性方面，仍然需要进一步的后训练过程来进行约束和校正，这一步一般统称为偏好对齐。

##### 6.4.1 为什么需要偏好对齐

Pretrain 更关注语言规律和世界知识的学习，SFT 更关注让模型学会遵循指令，而偏好对齐则更强调“什么样的回答更符合人类预期”。例如，在问答、代码生成或复杂推理任务中，模型不仅要给出答案，还要尽量做到表达清晰、内容安全、推理过程稳定，并尽量避免答非所问或有害输出。

从训练流程上看，偏好对齐承接在 SFT 之后，是 Post-Training 中非常关键的一环。其核心思路不是让模型继续单纯地拟合文本，而是让模型学会在多个候选回答之间更偏向人类更喜欢的输出。

##### 6.4.2 主流方法概览

目前常见的偏好对齐方法主要包括以下几类：

- **RLHF**：先构建偏好数据与奖励模型，再通过强化学习更新策略模型，是最经典的偏好对齐路线。
- **DPO**：直接利用偏好数据优化模型，无需显式训练奖励模型，训练流程相对更简洁。
- **KTO**：同样属于直接偏好优化方法，更强调让模型对“好回答”和“不好回答”形成稳定区分。

这些方法虽然细节不同，但都依赖于高质量的偏好数据，且通常建立在 SFT 模型之上。

##### 6.4.3 与本章前文的衔接

从工程实现角度看，偏好对齐并不是一个完全独立的新体系，而是建立在本章前面几节内容之上的：

1. 在 `6.1` 中，我们已经掌握了如何基于 Transformers 初始化模型、处理数据并组织训练流程。
2. 在 `6.2` 中，我们已经完成了 SFT 数据构造和监督训练，这一步通常就是偏好对齐前的起点模型。
3. 在 `6.3` 中，我们介绍了 LoRA/QLoRA 与 `peft` 的接入方式，这些方法同样可以用于 DPO、KTO 等偏好对齐任务，以降低训练成本。

因此，当你进一步实践偏好对齐时，真正新增的核心内容主要集中在偏好数据组织、奖励建模方式以及偏好损失函数的设计上，而模型加载、参数高效训练和大多数工程配置都可以复用前文的思路。

##### 6.4.4 学习与实践建议

如果你是第一次系统学习大模型训练，建议先完整掌握本章的 Pretrain、SFT 与 PEFT 内容，再继续阅读偏好对齐专题补充材料 [`6.4 偏好对齐`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/6.4%5BWIP%5D%20%E5%81%8F%E5%A5%BD%E5%AF%B9%E9%BD%90.md)。在实践层面，推荐优先从 DPO 这类更轻量的偏好优化方法入手，再逐步理解奖励模型和 RLHF 的完整链路。这样可以在不显著增加工程复杂度的前提下，建立对后训练流程的整体认识。

**参考资料**

[1] Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, and Sylvain Gelly. (2019). *Parameter-Efficient Transfer Learning for NLP.* arXiv preprint arXiv:1902.00751.

[2] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. (2021). *LoRA: Low-Rank Adaptation of Large Language Models.* arXiv preprint arXiv:2106.09685.

[3] Armen Aghajanyan, Luke Zettlemoyer, and Sonal Gupta. (2020). *Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning.* arXiv preprint arXiv:2012.13255.

[4] Xiang Lisa Li 和 Percy Liang. (2021). *Prefix-Tuning: Optimizing Continuous Prompts for Generation.* arXiv preprint arXiv:2101.00190.

### 第六章实践说明

第六章聚焦如何基于 Transformers 生态完成大模型训练实践，正文主线为 Pretrain、SFT 与 PEFT 三部分，适合作为从手写模型实现过渡到工业界训练框架的桥梁章节。

#### 1. 本章包含什么

- [`第六章 大模型训练流程实践`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/%E7%AC%AC%E5%85%AD%E7%AB%A0%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83%E6%B5%81%E7%A8%8B%E5%AE%9E%E8%B7%B5.md)：第六章正文，介绍训练框架、数据处理、Trainer、DeepSpeed 与 LoRA/QLoRA 等核心内容。
- [`6.4 偏好对齐专题补充`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/6.4%5BWIP%5D%20%E5%81%8F%E5%A5%BD%E5%AF%B9%E9%BD%90.md)：偏好对齐的补充阅读材料，可在完成正文学习后继续深入。
- [`code/`](https://github.com/datawhalechina/happy-llm/tree/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code)：本章配套代码目录，包含数据下载、预训练、SFT 与 DeepSpeed 配置示例。

#### 2. 推荐学习顺序

1. 阅读第六章正文的 `6.1 模型预训练`，理解 Transformers、Trainer 与 DeepSpeed 的基础用法。
2. 阅读 `6.2 模型有监督微调`，对比 Pretrain 与 SFT 的数据构造与 loss 计算差异。
3. 阅读 `6.3 高效微调`，掌握 LoRA/QLoRA 的基本思路和 `peft` 的接入方式。
4. 完成上述内容后，再阅读偏好对齐补充材料，建立从 SFT 到 Post-Training 的完整认识。

#### 3. 代码入口

本章的主要代码文件如下：

- [`code/download_model.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/download_model.py)：下载基座模型。
- [`code/download_dataset.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/download_dataset.py)：下载或准备训练数据。
- [`code/pretrain.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/pretrain.py)：预训练脚本。
- [`code/finetune.py`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/finetune.py)：有监督微调脚本。
- [`code/pretrain.sh`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/pretrain.sh)：DeepSpeed 预训练启动示例。
- [`code/finetune.sh`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/finetune.sh)：DeepSpeed 微调启动示例。
- [`code/ds_config_zero2.json`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/ds_config_zero2.json)：DeepSpeed 配置文件。

#### 4. 环境建议

- 依赖文件：[`code/requirements.txt`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter6/code/requirements.txt)
- 推荐 Python 版本：3.10 或 3.11
- 推荐硬件：多卡 GPU；如果资源有限，建议优先使用小样本或单卡环境调试数据处理与训练流程

可以参考仓库中的 [`学习与环境准备`](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/%E5%AD%A6%E4%B9%A0%E4%B8%8E%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87.md) 页面统一准备环境。

#### 5. 实践建议

##### 5.1 先调通路径，再扩大规模

本章脚本中的 `autodl-tmp`、显卡编号、batch size 和输出目录都属于示例配置。建议先把模型路径、数据路径和输出路径替换为本地实际路径，再使用小样本验证流程是否跑通。

##### 5.2 先看懂数据，再启动训练

无论是 Pretrain 还是 SFT，数据格式都直接决定了训练效果。建议先阅读正文中的数据处理部分，并在运行前打印 1 到 2 条样本进行检查。

##### 5.3 将偏好对齐作为进阶主题

第六章正文已经覆盖了核心训练主线。若你希望进一步理解 RLHF、DPO、KTO 与奖励模型，可以在完成正文后继续阅读偏好对齐专题补充，而不必在第一次阅读时一次性掌握所有后训练细节。

### 第七章 大模型应用

在前面的章节中，我们系统地介绍了大模型的基础知识、训练方法和微调技术。本章将重点探讨大模型在实际应用中的关键技术和框架，涵盖大模型评测、RAG（检索增强生成）以及Agent（智能体）等核心内容，帮助读者深入理解大模型的实际应用场景和实现方法。

#### 7.1 LLM 的评测

近年来，随着人工智能领域的迅猛发展，大规模预训练语言模型（简称大模型）成为了推动技术进步的核心力量。这些大模型在自然语言处理等任务中展现出了令人惊叹的能力。然而，要准确衡量一个大模型的性能，必须依靠科学而合理的评测。

什么是大模型评测？大模型评测就是通过各种标准化的方法和数据集，对大模型在不同任务上的表现进行量化和比较。这些评测不仅包括模型在特定任务上的准确性，还涉及模型的泛化能力、推理速度、资源消耗等多个方面。通过评测，我们能够更全面地了解大模型的实际表现，以及它们在现实世界中的应用潜力。

大模型的开发成本高昂，涉及大量的计算资源和数据，因此评测对于确保模型的实际价值至关重要。首先，评测能够揭示模型在各种任务中的表现，帮助研究人员和企业判断模型的适用性和可靠性。其次，评测可以暴露模型的潜在弱点，例如偏见、鲁棒性问题等，从而为进一步优化和改进提供依据。此外，公平、公开的评测还为学术界和工业界提供了一个共同的标准，促进了技术的交流与进步。

##### 7.1.1 LLM 的评测数据集

在大模型的评测过程中，使用标准化的评测集至关重要。目前，主流的大模型评测集主要从以下几个方面进行评估，每个评测集都有其独特的用途和典型应用场景：

1. **通用评测集**：
   - **MMLU（Massive Multitask Language Understanding）**：MMLU评测模型在多种任务中的理解能力，包括各类学科和知识领域。具体包含了历史、数学、物理、生物、法律等任务类型，全面考察模型在不同学科的知识储备和语言理解能力。

2. **工具使用评测集**：
   - **BFCL V2**：用于评测模型在复杂工具使用任务中的表现，特别是在执行多步骤操作时的正确性和效率。这些任务通常涉及与数据库交互或执行特定指令，以模拟实际工具使用场景。

3. **数学评测集**：
   - **GSM8K**：GSM8K是一个包含小学数学问题的数据集，用于测试模型的数学推理和逻辑分析能力。具体任务包括算术运算、简单方程求解、数字推理等。GSM8K中的问题虽然看似简单，但模型需要理解问题语义并进行正确的数学运算，体现了逻辑推理和语言理解的双重挑战。
   - **MATH**：MATH数据集用于测试模型在更复杂的数学问题上的表现，包括代数和几何。

4. **推理评测集**：
   - **ARC Challenge**：ARC Challenge评测模型在科学推理任务中的表现，尤其是常识性和科学性问题的解答，典型应用场景包括科学考试题解答和百科问答系统的开发。
   - **GPQA**：用于评测模型在零样本条件下对开放性问题的回答能力，通常应用于客服聊天机器人和知识问答系统中，帮助模型在缺乏特定领域数据的情况下给出合理的回答。
   - **HellaSwag**：评测模型在复杂语境下选择最符合逻辑的答案的能力，适用于故事续写、对话生成等需要高水平理解和推理的场景。

5. **长文本理解评测集**：
   - **InfiniteBench/En.MC**：评测模型在处理长文本阅读理解方面的能力，尤其是对科学文献的理解，适用于学术文献自动摘要、长篇报道分析等应用场景。
   - **NIH/Multi-needle**：用于测试模型在多样本长文档环境中的理解和总结能力，应用于政府报告解读、企业内部长文档分析等需要处理海量信息的场景。

6. **多语言评测集**：
   - **MGSM**：用于评估模型在不同语言下的数学问题解决能力，考察模型的多语言适应性，尤其适用于国际化环境中的数学教育和跨语言技术支持场景。

这些评测集的多样性帮助我们全面评估大模型在不同任务和应用场景中的表现，确保模型在处理多样化任务时能够保持高效和精准的表现。例如，在MMLU评测中，某些大模型在历史、物理等学科任务中表现优异，展现出对多领域知识的深度理解；在GSM8K数学评测中，最新的大模型在算术和方程求解方面表现接近甚至超越了一些人类基准，显示出在复杂数学推理任务中的潜力。这些实际评测结果展示了模型在各类复杂任务中的进步和应用潜力。


##### 7.1.2 主流的评测榜单

大模型的评测不仅限于使用特定的数据集，许多机构还会根据评测结果发布模型排行榜，这些榜单为学术界和工业界提供了重要的参考，帮助他们了解当前最前沿的技术和模型。以下是一些主流的评测榜单：

###### Open LLM Leaderboard

Open LLM Leaderboard 为由 Hugging Face 提供的开放式榜单，汇集了多个开源大模型的评测结果，帮助用户了解不同模型在各种任务上的表现。该榜单通过多个标准化测试集来评估模型的性能，并通过持续更新的方式反映最新的技术进展，为研究者和开发者提供了高价值的对比参考，如图7.1所示。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-1-Open%20LLM%20Leaderboard.png)
图 7.1 Open LLM Leaderboard


###### Lmsys Chatbot Arena Leaderboard

由lmsys提供的聊天机器人评测榜单，通过多维度的评估，展示各类大模型在对话任务中的能力。该榜单采用真实用户与模型交互的方式来评测对话质量，重点考察模型的自然语言生成能力、上下文理解能力以及用户满意度，是当前评估聊天机器人性能的重要工具，如图7.2所示。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-1-lmsys%20Chatbot%20Arena%20Leaderboard.png)
图7.2 Lmsys Chatbot Arena Leaderboard


###### OpenCompass

OpenCompass 是国内的评测榜单，针对大模型在多种语言和任务上的表现进行评估，提供了中国市场特定应用的参考。该榜单结合了中文语言理解和多语言能力的测试，以适应本地化需求，并特别关注大模型在中文语境下的准确性、鲁棒性和适应性，为国内企业和研究者选择合适的模型提供了重要参考。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-1-opencompass.png)
图7.3 OpenCompass


##### 7.1.3 特定的评测榜单

另外，还有针对不同领域特定任务的大模型评测榜单，如图7.4所示。这些榜单专注于特定应用领域，帮助用户了解大模型在某一垂直领域的能力：

- 金融榜：基于CFBenchmark评测集，评估大模型在金融自然语言处理、金融预测计算、金融分析与安全检查等多项基础任务中的能力。由同济大学与上海人工智能实验室及东方财经提供。

- 安全榜：基于Flames评测集，评估大模型在公平、安全、数据保护以及合法五大维度的抗性，帮助深入了解模型在安全性上的表现。由上海人工智能实验室与复旦大学提供。

- 通识榜：基于BotChat评测集，评估大语言模型生成日常多轮对话能力的综合程度，判断模型在对话中是否具备类人水平。由上海人工智能实验室提供。

- 法律榜：基于LawBench评测集，评估模型在法律领域的理解、推理和应用能力，涵盖法律问题回答、文本生成、法律判例分析等任务。由南京大学提供。

- 医疗榜：基于MedBench评测集，评估大语言模型在医学知识问答、安全伦理理解等方面的表现。由上海人工智能实验室提供。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-1-%E5%9E%82%E7%9B%B4%E9%A2%86%E5%9F%9F%E6%A6%9C%E5%8D%95.png)
图7.4 垂直领域榜单



#### 7.2 RAG

##### 7.2.1 RAG 的基本原理

大语言模型（LLM）在生成内容时，虽然具备强大的语言理解和生成能力，但也面临着一些挑战。例如，LLM有时会生成不准确或误导性的内容，这被称为大模型“幻觉”。此外，模型所依赖的训练数据可能过时，尤其在面对最新的信息时，生成结果的准确性和时效性难以保证。对于特定领域的专业知识，LLM 的处理效率也较低，无法深入理解复杂的领域知识。因此，如何提升大模型的生成质量和效率，成为了当前研究的重要方向。

在这样的背景下，检索增强生成（Retrieval-Augmented Generation，RAG）技术应运而生，成为AI领域中的一大创新趋势。RAG 在生成答案之前，首先从外部的大规模文档数据库中检索出相关信息，并将这些信息融入到生成过程之中，从而指导和优化语言模型的输出。这一流程不仅极大地提升了内容生成的准确性和相关性，还使得生成的内容更加符合实时性要求。

RAG 的核心原理在于将“检索”与“生成”结合：当用户提出查询时，系统首先通过检索模块找到与问题相关的文本片段，然后将这些片段作为附加信息传递给语言模型，模型据此生成更为精准和可靠的回答。通过这种方式，RAG 有效缓解了大语言模型的“幻觉”问题，因为生成的内容建立在真实文档的基础上，使得答案更具可追溯性和可信度。同时，由于引入了最新的信息源，RAG 技术大大加快了知识更新速度，使得系统可以及时吸收和反映最新的领域动态。

##### 7.2.2 搭建一个 RAG 框架

接下来我会带领大家一步一步实现一个简单的RAG模型，这个模型是基于RAG的一个简化版本，我们称之为 Tiny-RAG 。Tiny-RAG只保留了 RAG 的核心功能，即检索和生成，其目的是帮助大家更好地理解 RAG 模型的原理和实现。

###### Step 1: RAG流程介绍

RAG通过在语言模型生成答案之前，先从广泛的文档数据库中检索相关信息，然后利用这些信息来引导生成过程，从而极大地提升了内容的准确性和相关性。RAG有效地缓解了幻觉问题，提高了知识更新的速度，并增强了内容生成的可追溯性，使得大型语言模型在实际应用中变得更加实用和可信。

RAG的基本结构有哪些呢？

- 向量化模块：用来将文档片段向量化。
- 文档加载和切分模块：用来加载文档并切分成文档片段。
- 数据库：存放文档片段及其对应的向量表示。
- 检索模块：根据 Query（问题）检索相关的文档片段。
- 大模型模块：根据检索到的文档回答用户的问题。

上述也就是 TinyRAG 的所有模块内容，如图7.5所示。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-2-tinyrag.png)
图7.5 TinyRAG 项目结构


接下来，让我们梳理一下RAG的流程是什么样的呢？

- **索引**：将文档库分割成较短的片段，并通过编码器构建向量索引。
- **检索**：根据问题和片段的相似度检索相关文档片段。
- **生成**：以检索到的上下文为条件，生成问题的回答。

如下图7.6所示的流程图，图片出处 ***[Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/pdf/2312.10997.pdf)***


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-2-rag.png)
图7.6 RAG 流程图


###### Step 2: 文档加载和切分

接下来我们来实现一个文档加载和切分的类，这个类主要用于加载文档并将其切分成文档片段。

文档可以是文章、书籍、对话、代码等文本内容，例如pdf文件、md文件、txt文件等。完整代码可以在 ***[RAG/utils.py](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/RAG/utils.py)*** 文件中找到。该代码支持加载pdf、md、txt等类型的文件，只需编写相应的函数即可。

```python
def read_file_content(cls, file_path: str):
    # 根据文件扩展名选择读取方法
    if file_path.endswith('.pdf'):
        return cls.read_pdf(file_path)
    elif file_path.endswith('.md'):
        return cls.read_markdown(file_path)
    elif file_path.endswith('.txt'):
        return cls.read_text(file_path)
    else:
        raise ValueError("Unsupported file type")
```

文档读取后需要进行切分。我们可以设置一个最大的Token长度，然后根据这个最大长度来切分文档。切分文档时最好以句子为单位（按`\n`粗切分），并保证片段之间有一些重叠内容，以提高检索的准确性。

```python
def get_chunk(cls, text: str, max_token_len: int = 600, cover_content: int = 150):
    chunk_text = []

    curr_len = 0
    curr_chunk = ''

    token_len = max_token_len - cover_content
    lines = text.splitlines()  # 假设以换行符分割文本为行

    for line in lines:
        # 保留空格，只移除行首行尾空格
        line = line.strip()
        line_len = len(enc.encode(line))

        if line_len > max_token_len:
            # 如果单行长度就超过限制，则将其分割成多个块
            # 先保存当前块（如果有内容）
            if curr_chunk:
                chunk_text.append(curr_chunk)
                curr_chunk = ''
                curr_len = 0

            # 将长行按token长度分割
            line_tokens = enc.encode(line)
            num_chunks = (len(line_tokens) + token_len - 1) // token_len

            for i in range(num_chunks):
                start_token = i * token_len
                end_token = min(start_token + token_len, len(line_tokens))

                # 解码token片段回文本
                chunk_tokens = line_tokens[start_token:end_token]
                chunk_part = enc.decode(chunk_tokens)

                # 添加覆盖内容（除了第一个块）
                if i > 0 and chunk_text:
                    prev_chunk = chunk_text[-1]
                    cover_part = prev_chunk[-cover_content:] if len(prev_chunk) > cover_content else prev_chunk
                    chunk_part = cover_part + chunk_part

                chunk_text.append(chunk_part)

            # 重置当前块状态
            curr_chunk = ''
            curr_len = 0

        elif curr_len + line_len + 1 <= token_len:  # +1 for newline
            # 当前行可以加入当前块
            if curr_chunk:
                curr_chunk += '\n'
                curr_len += 1
            curr_chunk += line
            curr_len += line_len
        else:
            # 当前行无法加入当前块，开始新块
            if curr_chunk:
                chunk_text.append(curr_chunk)

            # 开始新块，添加覆盖内容
            if chunk_text:
                prev_chunk = chunk_text[-1]
                cover_part = prev_chunk[-cover_content:] if len(prev_chunk) > cover_content else prev_chunk
                curr_chunk = cover_part + '\n' + line
                curr_len = len(enc.encode(cover_part)) + 1 + line_len
            else:
                curr_chunk = line
                curr_len = line_len

    # 添加最后一个块（如果有内容）
    if curr_chunk:
        chunk_text.append(curr_chunk)

    return chunk_text

```

###### Step 3: 向量化

首先我们来动手实现一个向量化的类，这是RAG架构的基础。向量化类主要用来将文档片段向量化，将一段文本映射为一个向量。

首先我们要设置一个 `BaseEmbeddings` 基类，这样我们在使用其他模型时，只需要继承这个基类，然后在此基础上进行修改即可，方便代码扩展。

```python
class BaseEmbeddings:
    """
    Base class for embeddings
    """
    def __init__(self, path: str, is_api: bool) -> None:
        """
        初始化嵌入基类
        Args:
            path (str): 模型或数据的路径
            is_api (bool): 是否使用API方式。True表示使用在线API服务，False表示使用本地模型
        """
        self.path = path
        self.is_api = is_api

    def get_embedding(self, text: str, model: str) -> List[float]:
        """
        获取文本的嵌入向量表示
        Args:
            text (str): 输入文本
            model (str): 使用的模型名称
        Returns:
            List[float]: 文本的嵌入向量
        Raises:
            NotImplementedError: 该方法需要在子类中实现
        """
        raise NotImplementedError

    @classmethod
    def cosine_similarity(cls, vector1: List[float], vector2: List[float]) -> float:
        """
        计算两个向量之间的余弦相似度
        Args:
            vector1 (List[float]): 第一个向量
            vector2 (List[float]): 第二个向量
        Returns:
            float: 两个向量的余弦相似度，范围在[-1,1]之间
        """
        # 将输入列表转换为numpy数组，并指定数据类型为float32
        v1 = np.array(vector1, dtype=np.float32)
        v2 = np.array(vector2, dtype=np.float32)

        # 检查向量中是否包含无穷大或NaN值
        if not np.all(np.isfinite(v1)) or not np.all(np.isfinite(v2)):
            return 0.0

        # 计算向量的点积
        dot_product = np.dot(v1, v2)
        # 计算向量的范数（长度）
        norm_v1 = np.linalg.norm(v1)
        norm_v2 = np.linalg.norm(v2)

        # 计算分母（两个向量范数的乘积）
        magnitude = norm_v1 * norm_v2
        # 处理分母为0的特殊情况
        if magnitude == 0:
            return 0.0

        # 返回余弦相似度
        return dot_product / magnitude
```

`BaseEmbeddings`基类有两个主要方法：`get_embedding`和`cosine_similarity`。`get_embedding`用于获取文本的向量表示，`cosine_similarity`用于计算两个向量之间的余弦相似度。在初始化类时设置了模型的路径和是否是API模型，例如使用OpenAI的Embedding API需要设置`self.is_api=True`。

继承`BaseEmbeddings`类只需要实现`get_embedding`方法，`cosine_similarity`方法会被继承下来。这就是编写基类的好处。

```python
class OpenAIEmbedding(BaseEmbeddings):
    """
    class for OpenAI embeddings
    """
    def __init__(self, path: str = '', is_api: bool = True) -> None:
        super().__init__(path, is_api)
        if self.is_api:
            self.client = OpenAI()
            # 从环境变量中获取 硅基流动 密钥
            self.client.api_key = os.getenv("OPENAI_API_KEY")
            # 从环境变量中获取 硅基流动 的基础URL
            self.client.base_url = os.getenv("OPENAI_BASE_URL")

    def get_embedding(self, text: str, model: str = "BAAI/bge-m3") -> List[float]:
        """
        此处默认使用硅基流动的免费嵌入模型 BAAI/bge-m3
        """
        if self.is_api:
            text = text.replace("\n", " ")
            return self.client.embeddings.create(input=[text], model=model).data[0].embedding
        else:
            raise NotImplementedError
```

> 注：此处我们默认使用国内用户可访问的[硅基流动大模型API服务平台](https://cloud.siliconflow.cn/i/ybUFvmqK)。


###### Step 4: 数据库与向量检索

完成文档切分和Embedding模型加载后，需要设计一个向量数据库来存放文档片段和对应的向量表示，以及设计一个检索模块用于根据Query检索相关文档片段。

向量数据库的功能包括：

- `persist`：数据库持久化保存。
- `load_vector`：从本地加载数据库。
- `get_vector`：获取文档的向量表示。
- `query`：根据问题检索相关文档片段。

完整代码可以在 ***[/VectorBase.py](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/RAG/VectorBase.py)*** 文件中找到。

```python
class VectorStore:
    def __init__(self, document: List[str] = ['']) -> None:
        self.document = document

    def get_vector(self, EmbeddingModel: BaseEmbeddings) -> List[List[float]]:
        # 获得文档的向量表示
        pass

    def persist(self, path: str = 'storage'):
        # 数据库持久化保存
        pass

    def load_vector(self, path: str = 'storage'):
        # 从本地加载数据库
        pass

    def query(self, query: str, EmbeddingModel: BaseEmbeddings, k: int = 1) -> List[str]:
        # 根据问题检索相关文档片段
        pass
```

`query` 方法用于将用户提出的问题向量化，然后在数据库中检索相关文档片段并返回结果。

```python
def query(self, query: str, EmbeddingModel: BaseEmbeddings, k: int = 1) -> List[str]:
    query_vector = EmbeddingModel.get_embedding(query)
    result = np.array([self.get_similarity(query_vector, vector) for vector in self.vectors])
    return np.array(self.document)[result.argsort()[-k:][::-1]].tolist()
```

###### Step 5: 大模型模块

接下来是大模型模块，用于根据检索到的文档回答用户的问题。

首先实现一个基类，这样可以方便扩展其他模型。

```python
class BaseModel:
    def __init__(self, path: str = '') -> None:
        self.path = path

    def chat(self, prompt: str, history: List[dict], content: str) -> str:
        pass

    def load_model(self):
        pass
```

`BaseModel` 包含两个方法：`chat`和`load_model`。对于本地化运行的开源模型需要实现`load_model`，而API模型则不需要。在此处我们还是使用国内用户可访问的硅基流动大模型API服务平台，使用API服务的好处就是用户不需要本地的计算资源，可以大大降低学习者的学习门槛。

```python
from openai import OpenAI

class OpenAIChat(BaseModel):
    def __init__(self, model: str = "Qwen/Qwen2.5-32B-Instruct") -> None:
        self.model = model

    def chat(self, prompt: str, history: List[dict], content: str) -> str:
        client = OpenAI()
        client.api_key = os.getenv("OPENAI_API_KEY")
        client.base_url = os.getenv("OPENAI_BASE_URL")
        history.append({'role': 'user', 'content': RAG_PROMPT_TEMPLATE.format(question=prompt, context=content)})
        response = client.chat.completions.create(
                model=self.model,
                messages=history,
                max_tokens=2048,
                temperature=0.1
            )
        return response.choices[0].message.content

```

设计一个专用于RAG的大模型提示词，如下：

```python
RAG_PROMPT_TEMPLATE="""
使用以上下文来回答用户的问题。如果你不知道答案，就说你不知道。总是使用中文回答。
问题: {question}
可参考的上下文：
···
{context}
···
如果给定的上下文无法让你做出回答，请回答数据库中没有这个内容，你不知道。
有用的回答:
"""
```

这样我们就可以利用InternLM2模型来做RAG啦！

###### Step 6: Tiny-RAG Demo

接下来，我们来看看Tiny-RAG的Demo吧！

```python
from VectorBase import VectorStore
from utils import ReadFiles
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding

# 没有保存数据库
docs = ReadFiles('./data').get_content(max_token_len=600, cover_content=150) # 获得data目录下的所有文件内容并分割
vector = VectorStore(docs)
embedding = OpenAIEmbedding() # 创建EmbeddingModel
vector.get_vector(EmbeddingModel=embedding)
vector.persist(path='storage') # 将向量和文档内容保存到storage目录下，下次再用就可以直接加载本地的数据库

# vector.load_vector('./storage') # 加载本地的数据库

question = 'RAG的原理是什么？'

content = vector.query(question, EmbeddingModel=embedding, k=1)[0]
chat = OpenAIChat(model='Qwen/Qwen2.5-32B-Instruct')
print(chat.chat(question, [], content))
```

也可以从本地加载已处理好的数据库：

```python
from VectorBase import VectorStore
from utils import ReadFiles
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding

# 保存数据库之后
vector = VectorStore()

vector.load_vector('./storage') # 加载本地的数据库

question = 'RAG的原理是什么？'

embedding = ZhipuEmbedding() # 创建EmbeddingModel

content = vector.query(question, EmbeddingModel=embedding, k=1)[0]
chat = OpenAIChat(model='Qwen/Qwen2.5-32B-Instruct')
print(chat.chat(question, [], content))
```

> 注：7.2 章节的所有代码均可在 [Happy-LLM Chapter7 RAG](https://github.com/datawhalechina/happy-llm/tree/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/chapter7/RAG) 中找到。

#### 7.3 Agent

##### 7.3.1 什么是 LLM Agent？

简单来说，大模型Agent是一个以LLM为核心“大脑”，并赋予其自主规划、记忆和使用工具能力的系统。 它不再仅仅是被动地响应用户的提示（Prompt），而是能够：

1. 理解目标（Goal Understanding）： 接收一个相对复杂或高层次的目标（例如，“帮我规划一个周末去北京的旅游行程并预订机票酒店”）。
2. 自主规划（Planning）： 将大目标分解成一系列可执行的小步骤（例如，“搜索北京景点”、“查询天气”、“比较机票价格”、“查找合适的酒店”、“调用预订API”等）。
3. 记忆（Memory）： 拥有短期记忆（记住当前任务的上下文）和长期记忆（从过去的交互或外部知识库中学习和检索信息）。
4. 工具使用（Tool Use）： 调用外部API、插件或代码执行环境来获取信息（如搜索引擎、数据库）、执行操作（如发送邮件、预订服务）或进行计算。
5. 反思与迭代（Reflection & Iteration）： （在更高级的Agent中）能够评估自己的行为和结果，从中学习并调整后续计划。

传统的LLM像一个知识渊博但只能纸上谈兵的图书馆员，而 LLM Agent 则更像一个全能的私人助理，不仅懂得多，还能跑腿办事，甚至能主动思考最优方案。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-3-Agent%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86.png)
图7.7 Agent 工作原理


LLM Agent 通过将大型语言模型的强大语言理解和生成能力与规划、记忆和工具使用等关键模块相结合，实现了超越传统大模型的自主性和复杂任务处理能力，这种能力使得 LLM Agent 在许多垂直领域（如法律、医疗、金融等）都具有广泛的应用潜力，如图7.7所示 Agent 工作原理。

##### 7.3.2 LLM Agent 的类型

虽然LLM Agent的概念还在快速发展中，但根据其设计理念和能力侧重，我们可以大致将其分为几类：

任务导向型Agent（Task-Oriented Agents）：
- 特点： 专注于完成特定领域的、定义明确的任务，例如客户服务、代码生成、数据分析等。
- 工作方式： 通常有预设的流程和可调用的特定工具集。LLM主要负责理解用户意图、填充任务槽位、生成回应或调用合适- 的工具。
- 例子： 专门用于预订餐厅的聊天机器人、辅助编程的代码助手（如GitHub Copilot在某些高级功能上体现了Agent特性）。

规划与推理型Agent（Planning & Reasoning Agents）：
- 特点： 强调自主分解复杂任务、制定多步计划，并根据环境反馈进行调整的能力。它们通常需要更强的推理能力。
- 工作方式： 常采用特定的思维框架，如ReAct (Reason+Act)，让模型先进行“思考”（Reasoning）分析当前情况和所需行动，然后执行“行动”（Action）调用工具，再根据工具返回结果进行下一轮思考。Chain-of-Thought (CoT) 等提示工程技术也是其推理的基础。
- 例子： 需要整合网络搜索、计算器、数据库查询等多种工具来回答复杂问题的研究型Agent，或者能够自主完成“写一篇关于XX主题的报告，并配上相关数据图表”这类任务的Agent。

多Agent系统（Multi-Agent Systems）：
- 特点： 由多个具有不同角色或能力的Agent协同工作，共同完成一个更宏大的目标。
- 工作方式： Agent之间可以进行通信、协作、辩论甚至竞争。例如，一个Agent负责规划，一个负责执行，一个负责审查。
- 例子： 模拟软件开发团队（产品经理Agent、程序员Agent、测试员Agent）来自动生成和测试代码；模拟一个公司组织结构来完成商业策划。AutoGen、ChatDev等框架支持这类系统的构建。

探索与学习型Agent（Exploration & Learning Agents）：
- 特点： 这类Agent不仅执行任务，还能在与环境的交互中主动学习新知识、新技能或优化自身策略，类似于强化学习中的Agent概念。
- 工作方式： 可能包含更复杂的记忆和反思机制，能够根据成功或失败的经验调整未来的规划和行动。
- 例子： 能在未知软件环境中自主探索学习如何操作的Agent，或者在玩游戏时不断提升策略的Agent。

##### 7.3.3 动手构造一个 Tiny-Agent

我们来基于 `openai` 库和其 `tool_calls` 功能，动手构造一个 Tiny-Agent，这个 Agent 是一个简单的任务导向型 Agent，它能够根据用户的输入，回答一些简单的问题。

最终的实现效果如图7.8所示：


![7-3-tinyagent-example](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-3-tinyagent-example.png)
图7.8 效果示意图


###### Step 1 : 初始化客户端和模型

首先，我们需要一个能够调用大模型的客户端。这里我们使用 `openai` 库，并配置其指向一个兼容 OpenAI API 的服务终端，例如 [SiliconFlow](https://cloud.siliconflow.cn/i/ybUFvmqK)。同时，指定要使用的模型，如 `Qwen/Qwen2.5-32B-Instruct`。

```python
from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key="YOUR_API_KEY",  # 替换为你的 API Key
    base_url="https://api.siliconflow.cn/v1", # 使用 SiliconFlow 的 API 地址
)

# 指定模型名称
model_name = "Qwen/Qwen2.5-32B-Instruct"
```

> **注意:** 你需要将 `YOUR_API_KEY` 替换为你从 [SiliconFlow](https://cloud.siliconflow.cn/i/ybUFvmqK) 或其他服务商获取的有效 API Key。

###### Step 2: 定义工具函数

我们在 `src/tools.py` 文件中定义 Agent 可以使用的工具函数。每个函数都需要有清晰的文档字符串（docstring），描述其功能和参数，因为这将用于自动生成工具的 JSON Schema。

```python
# src/tools.py
from datetime import datetime

# 获取当前日期和时间
def get_current_datetime() -> str:
    """
    获取当前日期和时间。
    :return: 当前日期和时间的字符串表示。
    """
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

def count_letter_in_string(a: str, b: str):
    """
    统计字符串中某个字母的出现次数。
    :param a: 要搜索的字符串。
    :param b: 要统计的字母。
    :return: 字母在字符串中出现的次数。
    """
    return str(a.count(b))

def search_wikipedia(query: str) -> str:
    """
    在维基百科中搜索指定查询的前三个页面摘要。
    :param query: 要搜索的查询字符串。
    :return: 包含前三个页面摘要的字符串。
    """
    page_titles = wikipedia.search(query)
    summaries = []
    for page_title in page_titles[: 3]:  # 取前三个页面标题
        try:
            # 使用 wikipedia 模块的 page 函数，获取指定标题的维基百科页面对象。
            wiki_page = wikipedia.page(title=page_title, auto_suggest=False)
            # 获取页面摘要
            summaries.append(f"页面: {page_title}\n摘要: {wiki_page.summary}")
        except (
                wikipedia.exceptions.PageError,
                wikipedia.exceptions.DisambiguationError,
        ):
            pass
    if not summaries:
        return "维基百科没有搜索到合适的结果"
    return "\n\n".join(summaries)
# ... (可能还有其他工具函数)
```

为了让 OpenAI API 理解这些工具，我们需要将它们转换成特定的 JSON Schema 格式。这可以通过 `src/utils.py` 中的 `function_to_json` 辅助函数完成。

```python
# src/utils.py (部分)
import inspect

def function_to_json(func) -> dict:
    # ... (函数实现细节)
    # 返回符合 OpenAI tool schema 的字典
    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": inspect.getdoc(func),
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required,
            },
        },
    }
```

###### Step 3: 构造 Agent 类

我们在 `src/core.py` 文件中定义 `Agent` 类。这个类负责管理对话历史、调用 OpenAI API、处理工具调用请求以及执行工具函数。

```python
# src/core.py (部分)
from openai import OpenAI
import json
from typing import List, Dict, Any
from utils import function_to_json
# 导入定义好的工具函数
from tools import get_current_datetime, add, compare, count_letter_in_string

SYSTEM_PROMPT = """
你是一个叫不要葱姜蒜的人工智能助手。你的输出应该与用户的语言保持一致。
当用户的问题需要调用工具时，你可以从提供的工具列表中调用适当的工具函数。
"""

class Agent:
    def __init__(self, client: OpenAI, model: str = "Qwen/Qwen2.5-32B-Instruct", tools: List=[], verbose : bool = True):
        self.client = client
        self.tools = tools
        self.model = model
        self.messages = [
            {"role": "system", "content": SYSREM_PROMPT},
        ]
        self.verbose = verbose

    def get_tool_schema(self) -> List[Dict[str, Any]]:
        # 获取所有工具的 JSON 模式
        return [function_to_json(tool) for tool in self.tools]

    def handle_tool_call(self, tool_call):
        # 处理工具调用
        function_name = tool_call.function.name
        function_args = tool_call.function.arguments
        function_id = tool_call.id

        function_call_content = eval(f"{function_name}(**{function_args})")

        return {
            "role": "tool",
            "content": function_call_content,
            "tool_call_id": function_id,
        }

    def get_completion(self, prompt) -> str:

        self.messages.append({"role": "user", "content": prompt})

        # 获取模型的完成响应
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=self.get_tool_schema(),
            stream=False,
        )

        # 检查模型是否调用了工具
        if response.choices[0].message.tool_calls:
            self.messages.append({"role": "assistant", "content": response.choices[0].message.content})
            # 处理工具调用
            tool_list = []
            for tool_call in response.choices[0].message.tool_calls:
                # 处理工具调用并将结果添加到消息列表中
                self.messages.append(self.handle_tool_call(tool_call))
                tool_list.append([tool_call.function.name, tool_call.function.arguments])
            if self.verbose:
                print("调用工具：", response.choices[0].message.content, tool_list)
            # 再次获取模型的完成响应，这次包含工具调用的结果
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=self.get_tool_schema(),
                stream=False,
            )

        # 将模型的完成响应添加到消息列表中
        self.messages.append({"role": "assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content
```

Agent 的工作流程如下：

1.  接收用户输入。
2.  调用大模型（如 Qwen），并告知其可用的工具及其 Schema。
3.  如果模型决定调用工具，Agent 会解析请求，执行相应的 Python 函数。
4.  Agent 将工具的执行结果返回给模型。
5.  模型根据工具结果生成最终回复。
6.  Agent 将最终回复返回给用户。

如图7.9所示，Agent 调用工具流程：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-3-Tiny_Agent.jpg)
图7.9 Agent 工作流程


###### Step 4: 运行 Agent

现在我们可以实例化并运行 Agent。在 `demo.py` 的 `if __name__ == "__main__":` 部分提供了一个简单的命令行交互示例。

```python
# demo.py (部分)
if __name__ == "__main__":
    client = OpenAI(
        api_key="YOUR_API_KEY", # 替换为你的 API Key
        base_url="https://api.siliconflow.cn/v1",
    )

    # 创建 Agent 实例，传入 client、模型名称和工具函数列表
    agent = Agent(
        client=client,
        model="Qwen/Qwen2.5-32B-Instruct",
        tools=[get_current_datetime, add, compare, count_letter_in_string],
        verbose=True # 设置为 True 可以看到工具调用信息
    )

    # 开始交互式对话循环
    while True:
        # 使用彩色输出区分用户输入和AI回答
        prompt = input("\033[94mUser: \033[0m")  # 蓝色显示用户输入提示
        if prompt.lower() == "exit":
            break
        response = agent.get_completion(prompt)
        print("\033[92mAssistant: \033[0m", response)  # 绿色显示AI助手回答
```

**示例交互:**

```bash
User: 你好
Assistant:  你好！有什么可以帮助你的吗？
User: 9.12和9 .2哪个更大？
调用工具： ['compare']
Assistant:  9.2 比 9.12 更大。
User: 为什么？
Assistant:  当我们比较9.12和9.2时，可以将它们看作是9.12和9.20。由于9.20在小数点后第二位是0，而9.12在小数点后第二位是2，所以在小数点后第一位相等的情况下，9.20（即9.2）大于9.12。因此，9.2 比 9.12 更大。
User: strawberry中有几个r？
调用工具： ['count_letter_in_string']
Assistant:  单词 "strawberry" 中有3个字母 'r'。
User: 你确信嘛？
调用工具： ['count_letter_in_string']
Assistant:  是的，我确定。单词 "strawberry" 中确实有3个字母 'r'。让我们再次确认一下，"strawberry" 中的 'r' 确实出现了3次。
User: 好的 你很薄，现在几点 了？
调用工具： ['get_current_datetime']
Assistant:  当前的时间是2025年4月26日17:01:33。不过，我注意到您提到“你很薄”，这似乎是一个打字错误，如果您有任何其他问题或者需要进一步的帮助，请告诉我！
User: exit
```

另外，我们也准备了一份可以展示的 Streamlit 应用，可以运行在本地，展示 Agent 的功能。`streamlit run web_demo.py` 来运行，以下为 Agent 运行效果。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/7-images/7-3-streamlit-demo.png)
图 7.10 Streamlit Demo



**参考文献**

[1] Hugging Face. (2023). *Open LLM Leaderboard: 开源大语言模型基准测试平台*. https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

[2] awacke1. (2023). *LMSYS Chatbot Arena Leaderboard: 大型语言模型竞技场评估平台*. https://huggingface.co/spaces/awacke1/lmsys-chatbot-arena-leaderboard

[3] OpenCompass 团队. (2023). *OpenCompass: 大模型统一评测平台*. https://rank.opencompass.org.cn/home

[4] OpenCompass 金融榜团队. (2024). *CFBENCHMARK: 金融领域大模型评测榜单*. https://specialist.opencompass.org.cn/CFBenchmark

[5] OpenCompass 安全榜团队. (2024). *Flames: 大模型安全评测榜单*. https://flames.opencompass.org.cn/leaderboard

[6] OpenCompass 通识榜团队. (2024). *BotChat: 大模型通用对话能力评测*. https://botchat.opencompass.org.cn/

[7] OpenCompass 法律榜团队. (2024). *LawBench: 法律领域大模型评测*. https://lawbench.opencompass.org.cn/leaderboard

[8] OpenCompass 医疗榜团队. (2024). *MedBench: 医疗领域大模型评测*. https://medbench.opencompass.org.cn/leaderboard

[9] Zhi Jing, Yongye Su, and Yikun Han. (2024). *When Large Language Models Meet Vector Databases: A Survey.* arXiv preprint arXiv:2402.01763.

[10] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, and Haofen Wang. (2024). *Retrieval-Augmented Generation for Large Language Models: A Survey.* arXiv preprint arXiv:2312.10997.

[11] Zhiruo Wang, Jun Araki, Zhengbao Jiang, Md Rizwan Parvez, 和 Graham Neubig. (2023). *Learning to Filter Context for Retrieval-Augmented Generation.* arXiv preprint arXiv:2311.08377.

[12] Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown 和 Yoav Shoham. (2023). *In-Context Retrieval-Augmented Language Models.* arXiv preprint arXiv:2302.00083.

### 第八章 大模型强化学习

在第四章中，我们从人类反馈强化学习（Reinforcement Learning from Human Feedback，RLHF）出发，介绍了奖励模型、近端策略优化（Proximal Policy Optimization，PPO）以及指令对齐的基本流程。第六章进一步给出了大模型训练的工程基础，第七章则让模型拥有了规划、记忆与调用工具的能力。

当 Agent 真正进入搜索、代码执行等环境后，仅靠监督微调已经很难覆盖所有可能的交互轨迹。模型需要自己尝试动作，根据最终结果判断一条轨迹是否有效，再把成功经验更新到策略中。大模型强化学习由此从“让回答更符合偏好”，逐步走向“让模型在环境中学会行动”。

本章围绕四个彼此衔接的主题展开。首先介绍当前大模型强化学习中使用广泛的 Group Relative Policy Optimization（GRPO），建立 rollout、reward、advantage 与策略更新的完整认识；随后介绍 On-Policy Distillation（OPD），观察 Student 如何在自己的状态分布上持续获得 Teacher 的逐 token 指导；最后以 Search-R1 和 ReTool 为例，把同一套训练框架扩展到搜索引擎与代码解释器，完成两条可以运行的 Agentic RL 实践。


![第八章内容结构](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/8-images/8-1-chapter-roadmap.png)
图 8.1 第八章内容结构


本章全部示例均使用 PyTRIO 0.2.6。PyTRIO 将本地的数据处理、环境交互和训练控制，与远端的模型采样、前向反向传播和权重管理连接起来。四个示例虽然任务不同，核心链路始终可以概括为：

1. 使用当前策略生成一条或一组轨迹；
2. 根据结果或 Teacher 反馈计算训练信号；
3. 将 prompt、response、旧策略 logprob 和 advantage 对齐为 `Datum`；
4. 调用 `forward_backward()` 与 `optim_step()` 更新策略；
5. 刷新采样客户端，让下一轮 rollout 使用新权重。

配套代码位于 `docs/chapter8`。从仓库根目录安装公共依赖：

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r docs/chapter8/requirements.txt
trio login
```

PyTRIO 服务支持的模型会持续更新，正式实验前可以使用下面的代码查看当前列表：

```python
import pytrio as trio

service_client = trio.ServiceClient()
print(service_client.get_supported_models())
```

> **扩展阅读：** 如果你希望继续了解更多 Agentic RL 算法与可运行实践，可以阅读作者维护的另一个开源项目 [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab)。除本章介绍的内容外，该仓库还包含 OPSD、DAPO、GSPO、ALFWorld 等算法与环境的原理拆解、训练代码和实验记录。

> 注：作者选择 PyTrio 而不是 Verl 作为本章示例，意在希望降低 Agentic RL 的工程门槛与实验成本。按照文中的最小试跑配置，作者力争将四个示例的基础实验预算控制在 200 元以内，让读者亲手跑通 rollout、reward、advantage 与策略更新闭环。实际费用会随模型、采样长度、训练步数和评测规模变化。

#### 8.1 GRPO

> **代码来源：** 本节依据作者开源仓库 [agentic-rl-lab/01-grpo](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/01-grpo) 中的 `01-demo-sync.py` 与 `02-demo-async.py` 整理。正文逐段讲解同步版 `01-demo-sync.py`，异步版作为完整配套实现保留。

GRPO 最早在 DeepSeekMath 中被系统提出。它保留了 PPO 的 on-policy 更新思想，同时使用同一道题的一组采样结果估计相对优势，从而省去单独训练 Value Model 的过程。对于具有可验证答案的数学、代码和逻辑任务，这种方法能够直接利用结果奖励，已经成为大模型强化学习最常见的基础算法之一。

##### 8.1.1 从语言模型到强化学习策略

自回归语言模型接收 prompt $x$，并依次生成 token 序列 $y=(y_1,y_2,\ldots,y_T)$。从概率建模的角度看，完整回答的概率可以写为：

$$\pi_\theta(y\mid x) = \prod_{t=1}^{T} \pi_\theta(y_t\mid x,y_{\lt t}),$$

其中， $\pi_\theta$ 表示参数为 $\theta$ 的语言模型策略。将语言模型放入强化学习框架后，可以得到表 8.1 所示的对应关系。

| 强化学习概念 | 大语言模型中的含义 |
| --- | --- |
| 状态 $s_t$ | prompt 与已经生成的 token |
| 动作 $a_t$ | 下一个 token |
| 策略 $\pi_\theta(a_t\mid s_t)$ | 模型对下一个 token 的概率分布 |
| 轨迹 $\tau$ | 一段完整回答，或包含工具调用的多轮交互 |
| 环境 | 数据集判题器、搜索引擎、代码解释器等 |
| 奖励 $R(\tau)$ | 答案正确性、格式、工具执行结果等反馈 |

一次模型生成通常称为一次 rollout。训练的目标，是提高高奖励轨迹中动作出现的概率，同时降低低奖励轨迹中动作出现的概率。最直观的策略梯度形式为：

$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau\sim\pi_\theta} \left[ A(\tau) \nabla_\theta \log \pi_\theta(\tau) \right],$$

其中， $A(\tau)$ 是优势函数。优势为正，说明这条轨迹相对值得鼓励；优势为负，说明当前策略需要减少类似行为。

大模型的动作空间是整个词表，一段回答又可能包含数百到数千个 token。训练时还要控制新旧策略的变化幅度，防止一次更新破坏模型已有能力。因此，真正困难的部分通常集中在两个问题上：如何得到稳定的 advantage，以及如何安全地使用这些 advantage 更新策略。

##### 8.1.2 从 PPO 到 GRPO

PPO 通常使用一个 Value Model 估计状态价值 $V_\phi(s_t)$，再结合回报计算 advantage。大模型场景中的 Value Model 往往与策略模型规模接近，它会带来额外的显存、训练和同步成本。价值估计误差也会进一步传递到策略更新。

GRPO 改用组内相对比较。对于一个问题 $x$，先从旧策略 $\pi_{\theta_{\mathrm{old}}}$ 中采样 $G$ 个回答：

$$\{y_1,y_2,\ldots,y_G\} \sim \pi_{\theta_{\mathrm{old}}}(\cdot\mid x).$$

判题器分别给出奖励 $r_1,r_2,\ldots,r_G$。经典 GRPO 使用组内均值和标准差对奖励进行标准化：

$$A_i = \frac{r_i-\mathrm{mean}(r_1,\ldots,r_G)}{\mathrm{std}(r_1,\ldots,r_G)+\varepsilon}.$$

这样一来，同一道题中的高分回答获得正 advantage，低分回答获得负 advantage。问题本身的难度被组内基线抵消，策略可以更专注地学习“在相同条件下，哪些生成方式更好”。


![GRPO 的分组采样与策略更新](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/8-images/8-2-grpo.png)
图 8.2 GRPO 的分组采样与策略更新


例如，对同一道数学题采样 4 个回答，规则判题器得到奖励 $[1,0,0,1]$。组内均值为 $0.5$，只做均值中心化时，4 个 advantage 分别为：

$$[0.5,-0.5,-0.5,0.5].$$

两个正确回答会被鼓励，两个错误回答会被抑制。本章代码为了直接展示组内基线，默认采用：

$$A_i=r_i-\bar r.$$

完整实验也可以加入标准差归一化。两种写法表达了相同的组内相对思想，但梯度尺度不同，比较实验时应固定 advantage 的计算方式。

这里还有一个容易忽略的退化情形。当一组回答全部正确，或者全部错误时，每个 $A_i$ 都等于 0，这组数据不会产生有效策略梯度。若训练日志中退化组比例长期很高，通常需要调整题目难度、采样温度、基础模型能力或 group size。

##### 8.1.3 奖励与可验证强化学习

GRPO 只负责把组内奖励转换为相对优势，奖励质量仍然决定了模型最终学到什么。数学和代码任务通常能够使用确定性的规则判题器，这类训练也被称为 Reinforcement Learning with Verifiable Rewards（RLVR）。

本章以 GSM8K 为例，要求模型将最终数值写在 `\boxed{}` 中。最小判题逻辑如下：

```python
def extract_boxed(text: str) -> str | None:
    matches = re.findall(r"\\boxed\{([^}]+)\}", text)
    if not matches:
        return None
    return matches[-1].strip()


def normalize_answer(text: str) -> str:
    return text.replace(",", "").strip().rstrip(".")


def grade_answer(response: str, ground_truth: str) -> float:
    answer = extract_boxed(response)
    if answer is None:
        return 0.0
    return 1.0 if normalize_answer(answer) == normalize_answer(ground_truth) else 0.0
```

规则奖励简单、便宜，并且可以重复计算。不过，规则一旦存在漏洞，模型就可能学习利用漏洞获得高分。设计 reward 时应至少检查以下内容：

- **答案抽取是否稳健**：同一个正确答案可能出现整数、小数、分数或带逗号数字等形式；
- **格式奖励是否压过正确性**：格式只能作为辅助约束，不能让格式正确的错误答案获得主要奖励；
- **参考答案是否可靠**：错误标签会给模型提供方向相反的训练信号；
- **判题器是否泄露信息**：模型不应通过 prompt 或工具输出直接读到标准答案；
- **奖励是否具有区分度**：大量全 0 或全 1 的组都会让 GRPO 失去相对比较信号。

正式训练前，可以先把基础模型 rollout 保存下来，离线人工检查一批“回答—抽取结果—reward”三元组。这个步骤往往比直接调学习率更早发现问题。

##### 8.1.4 策略比率与更新损失

rollout 由旧策略生成，参数更新发生在当前策略上。对第 $i$ 条回答的第 $t$ 个 token，定义新旧策略概率比：

$$\rho_{i,t}(\theta) = \frac{\pi_\theta(y_{i,t}\mid x,y_{i,\lt t})}{\pi_{\theta_{\mathrm{old}}}(y_{i,t}\mid x,y_{i,\lt t})} = \exp\left(\log\pi_\theta-\log\pi_{\theta_{\mathrm{old}}}\right).$$

最直接的 importance sampling 目标可以写为：

$$J_{\mathrm{IS}}(\theta) = \mathbb{E}_{i,t} \left[\rho_{i,t}(\theta)A_i\right].$$

如果概率比偏离 1 太远，少数 token 可能主导梯度。PPO 使用截断目标限制单次更新幅度：

$$J_{\mathrm{PPO}}(\theta) = \mathbb{E}_{i,t} \left[\min\left(\rho_{i,t}A_i, \mathrm{clip}(\rho_{i,t},1-\epsilon,1+\epsilon)A_i\right)\right].$$

DeepSeekMath 中的经典 GRPO 目标采用了 PPO 风格的 clipping，并加入与参考策略之间的 KL 约束。本章的同步版 `01-demo-sync.py` 默认选择 PyTRIO 内置的 `importance_sampling`，便于观察 `old_logprobs`、`advantages` 和当前策略之间的数据关系；将命令行参数改为 `--loss-fn ppo`，即可使用内置 PPO loss。

因此，GRPO 与 PPO 需要放在不同层次理解：

- GRPO 描述如何对同题分组采样，并由组内奖励得到 advantage；
- importance sampling 或 PPO 描述如何把 advantage 转换为策略梯度。

##### 8.1.5 从头实现同步版 GRPO

本节按照同步版脚本的执行顺序，把一份完整的 GRPO 训练代码拆开说明。配套目录提供两个可以独立运行的文件：

| 文件 | 执行方式 | 用途 |
| --- | --- | --- |
| `01-demo-sync.py` | 同步 | 正文逐段讲解的教学主线 |
| `02-demo-async.py` | 异步 | 并发处理同一 batch 中不同 prompt 的 rollout |

两个文件使用相同的数据、reward、advantage、Datum 和 loss。下面只展开同步版，读者先沿着线性的控制流理解一次完整更新。

**（1）定义训练配置与 rollout 数据**

脚本只保留 PyTRIO 直接提供的 `importance_sampling` 和 `ppo` 两种策略更新 loss：

```python
LOSS_FNS = ("importance_sampling", "ppo")
```

`GRPOConfig` 集中保存模型、采样、优化器和 SwanLab 参数。`RolloutSample` 保存一条 completion 后续训练需要的全部信息：

```python
@dataclass
class RolloutSample:
    """一条采样结果，以及构造 importance_sampling 所需的旧策略 logprobs。"""

    tokens: list[int]
    logprobs: list[float]
    text: str
    reward: float
    advantage: float
```

这里的 `logprobs` 必须来自 rollout 时的 Student。策略更新之后重新计算得到的是新策略 logprob，不能替代旧策略概率。`parse_args()` 将命令行参数转换为 `GRPOConfig`，并通过 `choices=LOSS_FNS` 限定只使用这两个内置 loss。

**（2）加载 GSM8K 并构造 prompt**

GSM8K 的标准答案位于 `####` 后面。模型输出则要求把最终数字写在 `\boxed{}` 中。代码对两侧答案做相同的轻量归一化：

```python
def extract_boxed(text: str) -> str | None:
    """取最后一个 \\boxed{...} 作为模型最终答案。"""
    matches = re.findall(r"\\boxed\{([^}]+)\}", text)
    if not matches:
        return None
    return matches[-1].strip()


def normalize_answer(text: str) -> str:
    """GSM8K 答案只做轻量归一化，避免 1,000 和 1000 被判成不同。"""
    return text.replace(",", "").strip().rstrip(".")


def grade_answer(response: str, ground_truth: str) -> float:
    """boxed answer 与标准答案完全一致时给 1，否则给 0。"""
    answer = extract_boxed(response)
    if answer is None:
        return 0.0
    return 1.0 if normalize_answer(answer) == normalize_answer(ground_truth) else 0.0


def extract_gsm8k_answer(answer_text: str) -> str:
    """GSM8K 的最终答案位于 `####` 后面。"""
    match = re.search(r"####\s*(.+)", answer_text)
    if match is None:
        raise ValueError(f"No GSM8K final answer found: {answer_text!r}")
    return normalize_answer(match.group(1))
```

`build_prompt()` 将一个 few-shot 示例与当前问题交给模型自己的 chat template，再编码成 token：

```python
def build_prompt(tokenizer: Any, question: str) -> list[int]:
    messages = [
        *FEWSHOT_PREFIX,
        {"role": "user", "content": question + QUESTION_SUFFIX},
    ]
    prompt_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    prompt_tokens = tokenizer.encode(prompt_text, add_special_tokens=False)
    if not prompt_tokens:
        raise ValueError("Prompt tokens are empty")
    return prompt_tokens
```

训练集通过 `load_dataset("openai/gsm8k", "main", split="train")` 加载。`pick_batch()` 在小步试跑时允许数据回绕；打开 `--all-data` 后，每条训练样本最多使用一次。

**（3）对同一道题采样一组回答**

`run_rollout_group()` 是 GRPO rollout 的核心。一次 `sample()` 接收一个 prompt，并通过 `num_samples=group_size` 返回同题的一组 completion：

```python
def run_rollout_group(
    sampling_client: Any,
    tokenizer: Any,
    prompt_tokens: list[int],
    ground_truth: str,
    sampling_params: trio.SamplingParams,
    group_size: int,
) -> list[RolloutSample]:
    result = sampling_client.sample(
        prompt=trio.ModelInput.from_ints(prompt_tokens),
        num_samples=group_size,
        sampling_params=sampling_params,
        return_text=True,
    ).result()

    rewards: list[float] = []
    raw_samples: list[tuple[list[int], list[float], str]] = []

    for sequence in result.sequences:
        text = sequence.text
        if text is None:
            text = tokenizer.decode(sequence.tokens, skip_special_tokens=True)

        tokens = list(sequence.tokens)
        logprobs = [float(value) for value in sequence.logprobs]
        if len(tokens) != len(logprobs):
            raise ValueError(
                f"Generated token/logprob length mismatch: "
                f"{len(tokens)} != {len(logprobs)}"
            )

        reward = grade_answer(text, ground_truth)
        rewards.append(reward)
        raw_samples.append((tokens, logprobs, text))

    mean_reward = sum(rewards) / len(rewards)
    return [
        RolloutSample(
            tokens=tokens,
            logprobs=logprobs,
            text=text,
            reward=reward,
            advantage=reward - mean_reward,
        )
        for (tokens, logprobs, text), reward
        in zip(raw_samples, rewards, strict=True)
    ]
```

这段代码依次完成四件事：

1. 保存 completion token；
2. 保存采样时旧策略对每个 completion token 的 logprob；
3. 使用规则判题器得到 0 或 1 的 reward；
4. 计算 `advantage = reward - mean_reward`。

同组回答全部正确或全部错误时，每条 advantage 都为 0。主循环会把这种 group 记为退化组并跳过，避免提交没有训练信号的 Datum。

**（4）构造右移对齐的 PyTRIO Datum**

自回归模型用当前位置 token 预测下一个 token。设 prompt 长度为 $m$，completion 长度为 $T$，脚本构造的四个数组长度均为 $m+T-1$：

```python
def build_grpo_datum(
    prompt_tokens: list[int],
    sample: RolloutSample,
) -> trio.Datum:
    if not sample.tokens:
        raise ValueError("Cannot train on an empty completion")

    observation_len = len(prompt_tokens) - 1
    input_tokens = prompt_tokens + sample.tokens[:-1]
    target_tokens = [0] * observation_len + sample.tokens
    padded_logprobs = [0.0] * observation_len + sample.logprobs
    padded_advantages = (
        [0.0] * observation_len
        + [sample.advantage] * len(sample.tokens)
    )

    if not (
        len(input_tokens)
        == len(target_tokens)
        == len(padded_logprobs)
        == len(padded_advantages)
    ):
        raise ValueError("GRPO datum fields must have the same token length")

    return trio.Datum(
        model_input=trio.ModelInput.from_ints(input_tokens),
        loss_fn_inputs={
            "target_tokens": np.asarray(target_tokens, dtype=np.int64),
            "logprobs": np.asarray(padded_logprobs, dtype=np.float32),
            "advantages": np.asarray(padded_advantages, dtype=np.float32),
        },
    )
```

prompt 区间只提供上下文，因此 `target_tokens`、`logprobs` 和 `advantages` 使用 0 占位。completion 区间放入真实目标 token、旧策略 logprob 和整条回答共享的组内 advantage。

以 3 个 prompt token 和 2 个 completion token 为例：

```text
prompt       = [x1, x2, x3]
completion   = [y1, y2]

model_input  = [x1, x2, x3, y1]
target       = [ 0,  0, y1, y2]
old_logprob  = [ 0,  0, l1, l2]
advantage    = [ 0,  0,  A,  A]
```

最后一个 prompt token `x3` 对应的位置开始预测 `y1`，因此 prompt mask 的长度是 `len(prompt_tokens) - 1`。

**（5）选择 importance sampling 或 PPO**

`importance_sampling` 与 `ppo` 复用同一批 GRPO Datum，只需切换 `loss_fn`。两个 loss 都由 PyTRIO 内置实现：

```python
fwd_bwd_future = training_client.forward_backward(
    datums,
    loss_fn=config.loss_fn,
)
```

选择 `importance_sampling` 时，训练直接使用新旧策略概率比乘以 advantage。选择 `ppo` 时，PyTRIO 在相同数据上应用 PPO clipping。GRPO 的 rollout、reward 与组内 advantage 构造保持不变。

**（6）串联一轮同步训练**

`main()` 先创建训练客户端、采样参数与优化器：

```python
service_client = trio.ServiceClient()
training_client = service_client.create_lora_training_client(
    base_model=config.base_model,
    rank=config.lora_rank,
)
tokenizer = training_client.get_tokenizer()

sampling_params = trio.SamplingParams(
    max_tokens=config.max_tokens,
    temperature=config.temperature,
    top_p=config.top_p,
    stop=get_stop_sequences(tokenizer),
)
adam_params = trio.AdamParams(
    learning_rate=config.learning_rate,
    beta1=config.beta1,
    beta2=config.beta2,
)
```

每个 step 都先从当前训练权重创建新的 sampler，然后按题目顺序完成 rollout：

```python
for step in range(effective_steps):
    batch_rows = pick_batch(
        train_data,
        step,
        config.batch_size,
        config.all_data,
    )
    sampling_client = (
        training_client.save_weights_and_get_sampling_client()
    )

    datums: list[trio.Datum] = []
    prompt_mean_rewards: list[float] = []
    rollout_lengths: list[int] = []
    n_degenerate = 0

    for row in tqdm(
        batch_rows,
        desc=f"GRPO step {step}",
        unit="prompt",
    ):
        prompt_tokens = build_prompt(tokenizer, row["question"])
        ground_truth = extract_gsm8k_answer(row["answer"])
        rollout_samples = run_rollout_group(
            sampling_client=sampling_client,
            tokenizer=tokenizer,
            prompt_tokens=prompt_tokens,
            ground_truth=ground_truth,
            sampling_params=sampling_params,
            group_size=config.group_size,
        )

        rewards = [sample.reward for sample in rollout_samples]
        prompt_mean_rewards.append(sum(rewards) / len(rewards))
        rollout_lengths.extend(
            len(sample.tokens) for sample in rollout_samples
        )

        if all(
            sample.advantage == 0.0
            for sample in rollout_samples
        ):
            n_degenerate += 1
            continue

        for sample in rollout_samples:
            datums.append(
                build_grpo_datum(prompt_tokens, sample)
            )
```

采样器的刷新位置体现了 on-policy 约束：第 $k$ 步更新完成后，第 $k+1$ 步用新权重重新生成轨迹。同步版在提交前向反向与优化任务后显式等待结果：

```python
optim_future = training_client.optim_step(adam_params)
fwd_bwd_result = fwd_bwd_future.result()
optim_future.result()
loss_metrics = dict(fwd_bwd_result.metrics)
```

脚本最后统计 batch 平均 reward、退化组比例、平均生成长度、有效训练 token 数与 `loss_mean`，并保存可用于采样的 LoRA 权重：

```python
final_weights = training_client.save_weights_for_sampler(
    name=run_name
).result()
print(
    f"Saved weights name: {run_name}, "
    f"path: {final_weights.path}"
)
```

##### 8.1.6 运行同步版与异步版

先登录 TRIO，再从仓库根目录运行同步版的一步试验：

```bash
trio login

python docs/chapter8/grpo/01-demo-sync.py \
    --steps 1 \
    --batch-size 1 \
    --group-size 4 \
    --max-tokens 512 \
    --loss-fn importance_sampling \
    --swanlab-mode disabled
```

异步版使用完全相同的训练参数：

```bash
python docs/chapter8/grpo/02-demo-async.py \
    --steps 1 \
    --batch-size 4 \
    --group-size 4 \
    --max-tokens 512 \
    --loss-fn importance_sampling \
    --swanlab-mode disabled
```

异步版的算法数据没有变化，执行方式发生了以下变化：

| 训练环节 | 同步版 | 异步版 |
| --- | --- | --- |
| 单题 rollout | `sample(...).result()` | `await sample_async(...)` |
| batch 内多题 | 依次处理 | `asyncio.gather()` 并发处理 |
| 刷新 sampler | 同步返回 | `await save_weights_and_get_sampling_client_async()` |
| 前向反向 | `forward_backward()` 后 `.result()` | `forward_backward_async()` 后再次 `await` future |
| 优化器 | `optim_step()` 后 `.result()` | `optim_step_async()` 后再次 `await` future |
| 程序入口 | `main(config)` | `asyncio.run(main(config))` |

正文使用同步版建立算法直觉。异步版适合 batch 中含有多个独立 prompt 的正式实验，它通过并发远程请求减少串行等待时间。

训练时应优先观察代码真实记录的指标：

| 指标 | 含义 | 异常现象 |
| --- | --- | --- |
| `reward` | batch 内各 prompt 平均正确率的均值 | 长期不升时检查 reward、数据难度和学习率 |
| `frac_degenerate` | 全对或全错 group 的比例 | 过高时有效相对优势不足 |
| `rollout/avg_gen_len` | completion 平均 token 数 | 接近 `max_tokens` 时检查截断 |
| `train_tokens` | advantage 非零的 completion token 数 | 为 0 时当前 step 没有训练信号 |
| `loss_mean` | 当前策略更新的主 loss | 剧烈波动时检查学习率与概率比 |

至此，我们得到了本章的第一条训练主线：当前策略分组采样，规则环境给出结果奖励，组内比较产生 advantage，PyTRIO 完成策略更新。接下来的 OPD 会保留同样的 on-policy 数据流，同时把训练信号换成 Teacher 对每个 token 的反馈。

#### 8.2 On-Policy Distillation

> **代码来源：** 本节依据作者开源仓库 [agentic-rl-lab/02-opd/general-opd](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/02-opd/general-opd) 中的 `01-demo-sync.py` 与 `02-demo-async.py` 整理。正文逐段讲解同步版 `01-demo-sync.py`，异步版作为完整配套实现保留。

大模型能力蒸馏通常由一个较强的 Teacher 和一个较小的 Student 组成。传统知识蒸馏使用预先收集好的数据，让 Student 拟合 Teacher 在这些固定样本上的概率分布。随着 Student 在训练中不断变化，固定数据与 Student 真正会访问的状态之间可能出现偏差。

On-Policy Distillation（OPD）让 Student 使用当前策略生成回答，再由 Teacher 对 Student 已经走过的轨迹逐 token 打分。这样，每一轮监督都位于 Student 当前的状态分布上。Teacher 无需重新生成一套答案，也无需参与反向传播，它只为 Student 的动作提供稠密概率反馈。

OPD 近年逐渐成为大模型训练中的重要方向。它可以用于推理能力迁移、能力恢复以及持续学习，还能够与强化学习的数据流自然结合：Student rollout 对应 on-policy 轨迹，Teacher logprob 对应逐 token 训练信号，Student 更新后再生成下一批轨迹。

##### 8.2.1 从离线蒸馏到 On-Policy Distillation

设 Teacher 为 $\pi_T$，Student 为 $\pi_\theta$。离线蒸馏先固定一个数据集 $\mathcal D$，然后在其中的状态上最小化分布差异：

$$\mathcal L_{\mathrm{offline}} = \mathbb E_{s\sim\mathcal D} \left[D\bigl(\pi_T(\cdot\mid s),\pi_\theta(\cdot\mid s)\bigr)\right].$$

这种做法实现简单，效果取决于数据集能否覆盖 Student 推理时遇到的状态。假设固定数据中大多是 Teacher 的高质量轨迹，而 Student 在真实生成时较早出现了一个错误 token，它随后进入的状态可能从未出现在蒸馏数据中，Teacher 的指导便无法覆盖这段分布外轨迹。

OPD 把状态采样改为当前 Student：

$$y\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid x),$$

然后让 Teacher 计算同一条 Student completion 的条件概率：

$$\log\pi_T(y_t\mid x,y_{\lt t}).$$

一次训练迭代可以分为三步：

1. **Student rollout**：Student 使用当前权重生成回答；
2. **Teacher feedback**：Teacher 在完全相同的 prompt 与 completion 上计算 logprob；
3. **Student update**：根据两者的概率差构造逐 token 信号并更新 Student。


![OPD 在 Student 自身轨迹上获得 Teacher 反馈](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/8-images/8-3-opd.png)
图 8.3 OPD 在 Student 自身轨迹上获得 Teacher 反馈


图 8.3 中，Teacher 只进行前向计算。Student 的采样动作也不参与反向传播，梯度从构造好的训练目标回到当前 Student 参数。这种停止梯度的边界使 OPD 可以直接复用现有 rollout 与策略优化基础设施。

##### 8.2.2 Reverse KL 与逐 token 训练信号

OPD 可以选择不同的分布散度。本章使用 reverse KL：

$$D_{\mathrm{KL}}\left(\pi_\theta\,\|\,\pi_T\right) = \mathbb E_{y\sim\pi_\theta} \left[\log\pi_\theta(y\mid x)-\log\pi_T(y\mid x)\right].$$

对于 Student 实际采样到的第 $t$ 个 token，可以得到一个 Monte Carlo 估计：

$$d_t = \log\pi_{\theta_{\mathrm{old}}}(y_t\mid x,y_{\lt t})-\log\pi_T(y_t\mid x,y_{\lt t}).$$

当 $d_t>0$ 时，Student 对这个 token 的偏好高于 Teacher；当 $d_t<0$ 时，Teacher 给出的概率更高。为了最小化 reverse KL，本章将训练 advantage 写为：

$$A_t=-\beta d_t,$$

其中， $\beta$ 控制蒸馏强度。这样，每个 completion token 都能获得独立的训练信号，信号密度远高于只在回答结束时给出一个 0/1 reward。

reverse KL 具有较强的 mode-seeking 特性。Student 会优先集中到 Teacher 已经赋予较高概率的区域，适合将 Teacher 的高置信行为压缩到小模型中。与此同时，Teacher 与 Student 的能力差距、推理风格和 tokenizer 兼容性都会影响蒸馏效果。更大的 Teacher 只是候选条件，Teacher 还需要在 Student 当前轨迹上提供有价值且可学习的新信号。

表 8.2 对比了 GRPO 与本章 OPD 示例的数据来源。

| 项目 | GRPO | OPD |
| --- | --- | --- |
| 轨迹来源 | 当前策略 | 当前 Student |
| 反馈来源 | 环境或规则判题器 | Teacher 概率分布 |
| 信号粒度 | 常见为整条轨迹 reward | 逐 completion token |
| 是否需要标准答案 | 通常需要可验证结果 | prompt-only 数据即可 |
| 是否需要额外模型 | 可省去 Value Model | 需要 Teacher 前向计算 |
| 主要风险 | reward hacking、退化组 | Teacher 不兼容、能力差距不合适 |

##### 8.2.3 Teacher 必须评价同一条 Student 轨迹

OPD 的关键数据约束，是 Teacher 与 Student 必须在相同前缀下评价相同目标 token。Teacher 自己生成一条回答，再让 Student 学习这条回答，会退回到常见的合成数据蒸馏流程。

在 PyTRIO 中，可以先把 prompt 和 Student completion 拼接起来，再调用 Teacher 的 `compute_logprobs()`：

```python
def completion_teacher_logprobs(
    teacher_client,
    prompt_ids: list[int],
    completion_ids: list[int],
):
    all_ids = prompt_ids + completion_ids
    all_logprobs = teacher_client.compute_logprobs(
        trio.ModelInput.from_ints(all_ids)
    ).result()

    start = len(prompt_ids)
    end = start + len(completion_ids)
    return [float(x) for x in all_logprobs[start:end]]
```

不同 SDK 对 logprob 的位置定义可能存在一位偏移，因此不能仅凭数组长度猜测切片。最稳妥的方法是构造一个很短的已知序列，确认返回值中每个位置究竟表示“当前 token 的 logprob”还是“下一个 token 的 logprob”，再完成 prompt 与 completion 的边界测试。本章代码已经按照 PyTRIO 0.2.6 的返回约定完成对齐。

Teacher 和 Student 还需要共享可兼容的 tokenizer。若同一组 token id 在两个模型中代表不同字符串，即使数组长度相同，概率差也没有正确语义。正式训练前应验证：

```python
text = "A short tokenizer alignment test."
student_ids = student_tokenizer.encode(text, add_special_tokens=False)
teacher_ids = teacher_tokenizer.encode(text, add_special_tokens=False)

assert student_ids == teacher_ids
```

对于同系列但 chat template 不同的模型，应由 Student tokenizer 渲染一次完整 prompt，然后让 Teacher 直接评价对应 token 序列。不要分别套用两份 chat template，否则两边看到的上下文已经发生变化。

##### 8.2.4 从头实现同步版 OPD

OPD 配套目录同样提供同步和异步两个独立脚本：

| 文件 | 执行方式 | 用途 |
| --- | --- | --- |
| `01-demo-sync.py` | 同步 | 正文逐段讲解的教学主线 |
| `02-demo-async.py` | 异步 | 并发处理 Student rollout 与 Teacher logprob 请求 |

下面按照 `01-demo-sync.py` 的代码顺序，实现从 DeepMath prompt 到 Student 更新的一轮完整 OPD。

**（1）准备参数与 DeepMath 数据**

脚本默认把数据下载到当前代码目录下的 `datasets/DeepMath-103K`：

```python
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = SCRIPT_DIR / "datasets" / "DeepMath-103K"
DEEPMATH_SHARDS = 10
```

`parse_args()` 的参数可以分成四组：

- 数据参数：`dataset_repo`、`dataset_dir`、`num_shards`、`sample_size`；
- 模型参数：Student 基座、LoRA rank、Teacher 基座或 Teacher 权重路径；
- 训练参数：step、batch、group、采样长度、KL 系数与优化器参数；
- 记录参数：SwanLab 项目、实验名和日志模式。

DeepMath-103K 在 ModelScope 上包含 10 个 parquet 分片。`shard_name()` 生成远端文件名，`modelscope_file_url()` 生成下载地址，`download_if_needed()` 先写入临时文件再原子替换，避免中断时留下不完整分片。

数据加载函数把本地 parquet 交给 Hugging Face Datasets，只保留训练需要的 `question` 字段：

```python
def load_deepmath(args: argparse.Namespace):
    shard_paths = []

    for index in range(args.num_shards):
        remote_path = shard_name(index)
        local_path = args.dataset_dir / remote_path
        download_if_needed(
            modelscope_file_url(
                args.dataset_repo,
                args.dataset_revision,
                remote_path,
            ),
            local_path,
            args.force_download,
        )
        shard_paths.append(str(local_path))

    dataset = load_dataset(
        "parquet",
        data_files=shard_paths,
        split="train",
        cache_dir=str(
            args.dataset_dir / ".datasets_cache"
        ),
    )

    if "question" not in dataset.column_names:
        raise ValueError(
            "DeepMath must contain 'question', "
            f"got {dataset.column_names}"
        )

    dataset = dataset.shuffle(seed=args.seed)
    if args.sample_size > 0:
        dataset = dataset.select(
            range(min(args.sample_size, len(dataset)))
        )
    return dataset
```

`--num-shards 1` 适合第一次联调，`--num-shards 10` 会覆盖完整数据集。`--sample-size` 控制加载后实际参与 prompt pool 的样本数。

**（2）把问题渲染成 Student prompt**

OPD 使用 prompt-only 数据，不读取 DeepMath 的参考推理过程。`build_prompt()` 把问题和输出要求交给 Student tokenizer：

```python
def build_prompt(
    tokenizer,
    question: str,
    suffix: str,
    enable_thinking: bool,
) -> list[int]:
    content = (
        question.strip()
        if not suffix
        else f"{question.strip()}\n\n{suffix}"
    )
    messages = [{"role": "user", "content": content}]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=enable_thinking,
    )
    return tokenizer.encode(
        prompt,
        add_special_tokens=False,
    )
```

prompt 只渲染一次。Teacher 随后直接评价同一组 token，从而保持两边上下文完全一致。

**（3）创建 Student 与 Teacher**

Student 使用 LoRA training client，Teacher 使用只做前向计算的 sampling client：

```python
service_client = trio.ServiceClient()

training_client = (
    service_client.create_lora_training_client(
        base_model=args.base_model,
        rank=args.lora_rank,
        seed=args.seed,
    )
)
tokenizer = training_client.get_tokenizer()

teacher_client = service_client.create_sampling_client(
    base_model=(
        args.teacher_base_model
        or args.base_model
    ),
    model_path=args.teacher_model_path,
)
```

`teacher_model_path` 可以指向已经保存的 sampler 权重。Teacher 不调用 `forward_backward()` 或 `optim_step()`，它的参数在 OPD 过程中保持固定。

**（4）让 Teacher 评价 Student 的同一条轨迹**

Student rollout 返回 completion token 与旧策略 logprob。Teacher 需要看到 `prompt_ids + completion_ids`，再从返回结果中切出 completion 区间：

```python
def completion_teacher_logprobs(
    teacher_client,
    prompt_ids: list[int],
    completion_ids: list[int],
):
    all_ids = prompt_ids + completion_ids
    all_logprobs = teacher_client.compute_logprobs(
        trio.ModelInput.from_ints(all_ids)
    ).result()

    completion_logprobs = all_logprobs[
        len(prompt_ids):
    ]

    if (
        len(completion_logprobs)
        != len(completion_ids)
        or any(
            value is None
            for value in completion_logprobs
        )
    ):
        raise ValueError(
            "Invalid teacher logprobs "
            "for completion tokens"
        )

    return [
        float(value)
        for value in completion_logprobs
    ]
```

长度检查与 `None` 检查用于保护 token 对齐。通过检查后，第 $t$ 个 Student completion token、Student 旧 logprob 和 Teacher logprob 才能组成同一个训练位置。

**（5）构造逐 token OPD Datum**

OPD 与 GRPO 使用相同的 `importance_sampling` schema，差异位于 advantage。GRPO 为整条 completion 复制一个组内 advantage，OPD 为每个 completion token 写入独立的 reverse-KL advantage：

```python
def build_opd_datum(
    prompt_ids: list[int],
    completion_ids: list[int],
    old_logprobs,
    advantages,
):
    prompt_loss_len = len(prompt_ids) - 1

    input_ids = (
        prompt_ids
        + completion_ids[:-1]
    )
    target_ids = (
        [0] * prompt_loss_len
        + completion_ids
    )
    padded_logprobs = (
        [0.0] * prompt_loss_len
        + list(old_logprobs)
    )
    padded_advantages = (
        [0.0] * prompt_loss_len
        + list(advantages)
    )

    if not (
        len(input_ids)
        == len(target_ids)
        == len(padded_logprobs)
        == len(padded_advantages)
    ):
        raise ValueError(
            "OPD datum fields must "
            "have the same length"
        )

    return trio.Datum(
        model_input=trio.ModelInput.from_ints(
            input_ids
        ),
        loss_fn_inputs={
            "target_tokens": np.asarray(
                target_ids,
                dtype=np.int64,
            ),
            "logprobs": np.asarray(
                padded_logprobs,
                dtype=np.float32,
            ),
            "advantages": np.asarray(
                padded_advantages,
                dtype=np.float32,
            ),
        },
    )
```

右移规则与 GRPO 完全一致。prompt 区间的三个 loss 输入继续使用 0 占位，completion 区间一一放入 Student token、Student old logprob 和该 token 的 OPD advantage。

**（6）生成 Student 轨迹并计算 reverse KL**

每个 step 开始时，代码按 `sampler_refresh_steps` 刷新 Student sampler。默认值为 1，因此每一步都使用最新 Student 权重：

```python
if (
    student_sampler is None
    or step % args.sampler_refresh_steps == 0
):
    student_sampler = (
        training_client
        .save_weights_and_get_sampling_client()
    )
```

同步版依次处理当前 batch 的问题。对每个 prompt，Student 先生成 `group_size` 条轨迹，Teacher 再对每条非空 completion 打分：

```python
result = student_sampler.sample(
    prompt=trio.ModelInput.from_ints(
        prompt_ids
    ),
    num_samples=args.group_size,
    sampling_params=sampling_params,
    return_text=False,
).result()

for sequence in result.sequences:
    completion_ids = sequence.tokens
    if not completion_ids:
        continue

    student_lps = [
        float(value)
        for value in sequence.logprobs
    ]
    teacher_lps = completion_teacher_logprobs(
        teacher_client,
        prompt_ids,
        completion_ids,
    )

    reverse_kl = (
        np.asarray(student_lps)
        - np.asarray(teacher_lps)
    )
    advantages = (
        -args.kl_penalty_coef
        * reverse_kl
    )

    datums.append(
        build_opd_datum(
            prompt_ids,
            completion_ids,
            student_lps,
            advantages,
        )
    )
    reverse_kls.extend(reverse_kl.tolist())
    completion_token_counts.append(
        len(completion_ids)
    )
```

`group_size` 在这里扩大同一 prompt 下的 Student 状态覆盖范围。每条轨迹独立得到 Teacher 信号，不进行 GRPO 式的组内中心化。

**（7）更新 Student、记录指标并保存权重**

收集完整个 batch 后，代码执行一次前向反向和一次优化器更新：

```python
if not datums:
    raise RuntimeError(
        "No OPD datums were built"
    )

fwd_bwd = training_client.forward_backward(
    datums,
    loss_fn="importance_sampling",
)
optim = training_client.optim_step(adam)

fwd_bwd_result = fwd_bwd.result()
optim.result()
```

一次 OPD step 的 `tokens/s` 使用 completion token 总数除以整个 step 的耗时。这个耗时同时包含 Student 采样、Teacher logprob、Student 前向反向、优化器更新以及必要的 sampler 刷新：

```python
completion_tokens_total = int(
    sum(completion_token_counts)
)
metrics = {
    "data/datums": len(datums),
    "data/completion_tokens_mean": float(
        np.mean(completion_token_counts)
    ),
    "data/completion_tokens_total": (
        completion_tokens_total
    ),
    "data/completion_tokens_per_second": (
        completion_tokens_total
        / step_elapsed_time
    ),
    "opd/reverse_kl_mean": float(
        np.mean(reverse_kls)
    ),
    "opd/reverse_kl_std": float(
        np.std(reverse_kls)
    ),
    "train/learning_rate": args.learning_rate,
    "time/step_elapsed_time": step_elapsed_time,
}
```

训练结束后保存 Student 的 sampler 权重：

```python
save_result = (
    training_client
    .save_weights_for_sampler(
        args.save_weights_name
    )
    .result()
)
print(f"Saved weights: {save_result.path}")
```

##### 8.2.5 运行同步版与异步版

同步版的一步试验会自动下载一个 DeepMath 分片，并从中抽取最多 20 个 prompt：

```bash
python docs/chapter8/opd/01-demo-sync.py \
    --steps 1 \
    --batch-size 1 \
    --group-size 1 \
    --max-tokens 512 \
    --sample-size 20 \
    --num-shards 1 \
    --swanlab-mode disabled
```

异步版使用相同的算法与参数：

```bash
python docs/chapter8/opd/02-demo-async.py \
    --steps 1 \
    --batch-size 4 \
    --group-size 2 \
    --max-tokens 512 \
    --sample-size 20 \
    --num-shards 1 \
    --swanlab-mode disabled
```

异步 OPD 同时利用两层并发：

| 训练环节 | 同步版 | 异步版 |
| --- | --- | --- |
| 创建 Student / Teacher | 同步 client 接口 | `create_lora_training_client_async()` 与 `create_sampling_client_async()` |
| Student rollout | 逐 prompt 调用 `sample().result()` | batch 内并发 `sample_async()` |
| Teacher 打分 | 逐 completion 调用 `compute_logprobs().result()` | 同一 prompt 内并发 `compute_logprobs_async()` |
| 汇总 batch | 顺序追加 Datum | 两层 `asyncio.gather()` 后统一汇总 |
| Student 更新 | 同步 future + `.result()` | async API 提交后再次 `await` future |
| 程序入口 | `main(args)` | `asyncio.run(main(args))` |

正文只展开同步版，因为它能直接呈现“Student 采样 → Teacher 打分 → reverse KL → Student 更新”的因果顺序。异步版保留同样的 token 对齐、advantage 和优化目标。

示例默认使用 `Qwen/Qwen3.5-4B` 作为 Student，使用 `Qwen/Qwen3.6-27B` 作为 Teacher。实际可用模型应以当前 PyTRIO 服务返回的支持列表为准。训练时应同步观察：

- `opd/reverse_kl_mean`：Student 采样 token 与 Teacher 概率的平均差异；
- `opd/reverse_kl_std`：不同 token 蒸馏信号的离散程度；
- `data/completion_tokens_total`：本 step 完成 Teacher 打分的 token 总量；
- `data/completion_tokens_per_second`：整步 OPD 的有效 completion token 吞吐；
- `trainer/*`：PyTRIO 返回的训练指标；
- 独立任务评测与通用能力评测：确认蒸馏后的真实能力变化。

reverse KL 下降说明 Student 的采样分布正在接近 Teacher。任务正确率仍需通过固定的 held-out 评测确认。出现 loss 波动或能力下降时，应依次检查 token 对齐、Teacher 质量、KL 系数、学习率、sampler 刷新频率和 completion 截断比例。

GRPO 和 OPD 到这里都发生在“模型生成一段回答，外部模块提供训练信号”的单轮结构中。下一节的 Search-R1 会进一步改变轨迹形态：模型在完成回答前可以暂停生成、调用搜索环境、读取 observation，再继续决定下一步动作。

#### 8.3 Search-R1

> **代码来源：** 本节依据作者开源仓库 [agentic-rl-lab/03-search-r1](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/03-search-r1) 中的完整多文件实现整理。正文按照 `prepare_data.py`、`protocol.py`、`search.py`、`rollout.py`、`reward.py`、`train.py`、`eval.py` 与 `analyse.py` 的真实调用链展开。

大语言模型内部存储了大量知识，但这些知识受训练数据时间范围、参数容量和长尾覆盖率限制。检索增强生成（Retrieval-Augmented Generation，RAG）通常由系统预先检索文档，再把结果交给模型回答。Search-R1 将搜索决策交给模型：模型可以判断何时搜索、搜索什么、是否需要根据新证据继续搜索，以及何时结束并给出答案。

这项变化使一次回答成为多轮轨迹：

$$\tau=(x,a_1,o_1,a_2,o_2,\ldots,a_T),$$

其中， $a_t$ 是模型生成的搜索调用或最终回答， $o_t$ 是搜索环境返回的 observation。模型只有在完成整条轨迹后才能获得结果奖励，GRPO 再把成功搜索路径与失败路径区分开。

配套实现不是一个孤立的训练脚本，而是一条由 9 个文件共同组成的执行链。阅读代码时，可以先抓住下面这条主线：

```text
prepare_data.py / data.py
        ↓ 读取问题与参考答案
protocol.py
        ↓ 构造 prompt、解析 search 调用
search.py
        ↓ 执行检索并返回 observation
rollout.py
        ↓ 生成完整多轮轨迹、reward 与组内 advantage
train.py
        ↓ observation mask、Datum、importance_sampling、optim_step
eval.py / analyse.py
        ↓ 固定环境评测与结果汇总
```

真正被训练的是语言模型生成的 Assistant token。`search.py` 负责的搜索服务属于环境，`protocol.py` 负责把模型动作和环境 observation 接成连续轨迹，`rollout.py` 负责调度两者，`train.py` 最后才把轨迹转换成 PyTRIO 可以更新的 `Datum`。下面按照这条真实调用链展开代码。

##### 8.3.1 从固定检索到自主搜索

Search-R1 的训练样本只包含问题和参考答案，不包含人工编写的搜索词，也不包含标准搜索轨迹。`prepare_data.py` 将 NQ 与 HotpotQA 的原始字段统一为下面的 JSONL 结构：

```json
{"id":"...","question":"...","answers":["..."],"data_source":"nq"}
```

清洗逻辑只保留可用于结果奖励的字段：

```python
def normalize_row(row: dict[str, Any]) -> dict[str, Any] | None:
    question = str(row.get("question") or "").strip()
    answers = extract_answers(row)
    if not question or not answers:
        return None
    return {
        "id": str(row.get("id") or ""),
        "question": question,
        "answers": answers,
        "data_source": str(
            row.get("data_source") or "unknown"
        ),
    }
```

`data.py` 再将每一行转换为 `SearchExample`：

```python
@dataclass(frozen=True)
class SearchExample:
    id: str
    question: str
    answers: list[str]
    data_source: str
```

这个数据边界很重要。搜索 query、搜索次数和证据使用方式都必须由当前策略在 rollout 中自己探索；如果训练集已经给出了固定检索轨迹，任务就更接近轨迹模仿，而不是本节讨论的 Search-R1。

固定 RAG 与 Search Agent 的差异可以从表 8.3 中看出。

| 环节 | 固定 RAG | Search-R1 |
| --- | --- | --- |
| 是否检索 | 由外部流程决定 | 模型根据当前状态决定 |
| 检索词 | 预设或单次生成 | 可根据 observation 多次改写 |
| 检索轮数 | 通常固定 | 由策略决定，受最大次数约束 |
| 训练对象 | 回答模型或检索器 | 搜索动作与最终回答的统一策略 |
| 奖励 | 常见为监督答案 loss | 完整轨迹的结果奖励 |

例如，问题“《小王子》的作者出生在哪个国家？”需要先确定作者，再查询作者的出生地。模型可以形成下面的轨迹：

```text
User: What country was the author of The Little Prince born in?

Assistant -> search("The Little Prince author")
Tool: Antoine de Saint-Exupéry ...

Assistant -> search("Antoine de Saint-Exupéry birthplace country")
Tool: He was born in Lyon, France ...

Assistant: Answer: France
```

第二次搜索词依赖第一次 observation，因此无法在 rollout 开始前一次性确定。训练代码需要维护环境状态，并在每个 assistant turn 后解析模型动作。


![Search-R1 的多轮搜索与 observation mask](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/8-images/8-4-search-r1.png)
图 8.4 Search-R1 的多轮搜索与 observation mask


Search-R1 论文使用 `<search>... </search>` 和 `<information>... </information>` 等文本标签表示动作与观察。本章使用 Qwen3.5-4B 模型，采用模型原生 function calling 模板：

```python
SEARCH_TOOL = {
    "type": "function",
    "function": {
        "name": "search",
        "description": "Search the web for evidence.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
            },
            "required": ["query"],
        },
    },
}
```

两种协议承载相同的强化学习语义：Assistant 输出可训练动作，搜索后端返回环境 observation。使用原生模板可以减少模型基础能力与工具格式之间的冲突，也能保留结构化的工具消息。

定义工具以后，还必须把模型输出严格解析为三种状态：合法搜索、最终回答或非法输出。`protocol.py` 的解析器要求一轮中只能出现一次完整的 `search` 调用，并且工具调用后不能再夹带最终答案：

```python
def parse_assistant(text: str) -> ParsedAssistant:
    matches = list(TOOL_CALL_PATTERN.finditer(text))
    if not matches:
        kind = (
            "invalid" if "<tool_call>" in text else "answer"
        )
        return ParsedAssistant(
            kind=kind,
            content=text.strip(),
        )

    if len(matches) != 1 or text[matches[0].end():].strip():
        return ParsedAssistant(
            kind="invalid",
            content=text.strip(),
        )

    query = matches[0].group(1).strip()
    if not query or "<" in query or ">" in query:
        return ParsedAssistant(
            kind="invalid",
            content=text.strip(),
        )

    content = text[:matches[0].start()].strip()
    return ParsedAssistant(
        kind="tool",
        content=content,
        query=query,
    )
```

这里没有单独定义“停止”动作。只要输出中不存在合法工具调用，本轮就作为最终回答结束；之后由 `reward.py` 检查它是否符合 `Answer: <short answer>`。包含残缺 `<tool_call>` 的输出会被标记为 `invalid`，同样结束轨迹并得到格式惩罚。

##### 8.3.2 搜索后端怎样变成环境 observation

`search.py` 提供 DeepSeek Search、Wikipedia 和知乎三个后端。rollout 不直接依赖任何 HTTP 响应格式，而只依赖统一的 `SearchResult`：

```python
@dataclass(frozen=True)
class SearchItem:
    title: str
    content: str
    source: str | None = None
    url: str | None = None


@dataclass(frozen=True)
class SearchResult:
    ok: bool
    items: list[SearchItem]
    latency: float
    status: int | None = None
    error: str | None = None
```

训练入口根据命令行参数创建后端，后面的状态机始终调用同一个 `search(query)` 接口：

```python
def create_search_client(
    backend: str,
    env_path: str | Path | None = None,
    *,
    model: str = "deepseek-v4-flash",
    timeout: float | None = None,
) -> SearchClient:
    resolved_timeout = resolve_search_timeout(
        backend, timeout
    )
    if backend == "deepseek":
        return DeepSeekSearchClient.from_env(
            env_path,
            model=model,
            timeout=resolved_timeout,
        )
    if backend == "wikipedia":
        return WikipediaSearchClient(
            timeout=resolved_timeout
        )
    if backend == "zhihu":
        return ZhihuSearchClient.from_env(
            env_path,
            timeout=resolved_timeout,
        )
    raise ValueError(f"不支持的搜索后端: {backend}")
```

以无需密钥的 Wikipedia 后端为例，真正的检索发生在 `_request()` 中。一次 API 请求同时完成全文搜索，并取回前三个页面的标题、正文摘要和 URL：

```python
def _request(
    self,
    query: str,
    started: float,
) -> SearchResult:
    params = urllib.parse.urlencode(
        {
            "action": "query",
            "format": "json",
            "formatversion": 2,
            "generator": "search",
            "gsrsearch": query,
            "gsrlimit": 3,
            "prop": "extracts|info",
            "explaintext": 1,
            "exintro": 1,
            "exchars": 1200,
            "inprop": "url",
            "redirects": 1,
            "utf8": 1,
        }
    )
    request = urllib.request.Request(
        f"{WIKIPEDIA_SEARCH_ENDPOINT}?{params}",
        headers={
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "User-Agent": WIKIPEDIA_USER_AGENT,
        },
    )
    with urllib.request.urlopen(
        request,
        timeout=self.timeout,
    ) as response:
        body = response.read()
        if response.headers.get(
            "Content-Encoding"
        ) == "gzip":
            body = gzip.decompress(body)
        payload = json.loads(body.decode("utf-8"))
        pages = payload.get("query", {}).get(
            "pages", []
        )
        if not isinstance(pages, list):
            raise TypeError(
                "Wikipedia 搜索响应 pages 不是列表"
            )
        if any(
            not isinstance(page, dict)
            for page in pages
        ):
            raise TypeError(
                "Wikipedia 搜索响应 page 不是对象"
            )
        ordered_pages = sorted(
            pages,
            key=lambda page: int(
                page.get("index", 1_000_000)
            ),
        )
        items = [
            SearchItem(
                title=str(
                    page.get("title") or "Untitled"
                ).strip(),
                content=str(
                    page.get("extract") or ""
                ).strip(),
                source="Wikipedia",
                url=str(
                    page.get("fullurl") or ""
                ).strip(),
            )
            for page in ordered_pages
            if str(page.get("extract") or "").strip()
        ]
        return SearchResult(
            ok=True,
            items=items,
            latency=time.perf_counter() - started,
            status=response.status,
        )
```

外层 `search()` 还负责请求限速、timeout、429 与 5xx 的有限重试，并累计成功率和 latency。重试后仍失败时，它不会让整个 rollout 抛异常退出，而是返回 `SearchResult(ok=False, error=...)`。`rollout.py` 会把错误文本也作为 observation 交给模型，因此模型可以继续回答或改写 query。

不同后端的结果最终都被格式化为可读证据：

```text
[1] Title: ...
    Content: ...
    Source: ...
    URL: ...
```

只返回标题或链接通常不够，因为模型真正需要的是能够支持下一步推理的 `content`。`max_tool_response_tokens` 和 `max_trajectory_tokens` 会在 observation 接入轨迹前再次限制证据长度。

##### 8.3.3 多轮 rollout 状态机

单轮 GRPO 只需一次 `sample()`。Search-R1 每条轨迹都可能经历不同数量的搜索调用，训练器需要反复执行“生成—解析—调用环境—追加 observation”。

本章将一条轨迹保存为 `Trajectory`：

```python
@dataclass
class AssistantTurn:
    prompt_tokens: list[int]
    completion_tokens: list[int]
    logprobs: list[float]
    text: str


@dataclass
class Trajectory:
    example: SearchExample
    group_index: int
    messages: list[dict[str, Any]]
    next_prompt_tokens: list[int] | None = None
    question_index: int = 0
    turns: list[AssistantTurn] = field(default_factory=list)
    search_calls: int = 0
    final_text: str = ""
    reward: float = -0.1
    advantage: float = 0.0
    valid_format: bool = False
    exact_match: bool = False
    done: bool = False
```

其中，每个 `AssistantTurn` 记录本轮采样前的完整 prompt、模型生成 token 和对应旧策略 logprob。搜索结果存在 `messages` 和下一轮 prompt 中，但它没有 rollout logprob，因为这些 token 来自环境。

真正向 PyTRIO 发请求的是 `sample_requests_async()`。同一轮中，不同问题或已经分叉的不同轨迹可以并发采样：

```python
async def sample_requests_async(
    sampling_client: Any,
    requests: list[SampleRequest],
    config: RolloutConfig,
    tokenizer: Any,
) -> list[Any]:
    tasks = []
    for request in requests:
        params = trio.SamplingParams(
            max_tokens=request.max_tokens,
            seed=request.seed,
            stop=stop_sequences(tokenizer),
            temperature=config.temperature,
            top_p=config.top_p,
        )
        tasks.append(
            sampling_client.sample_async(
                prompt=trio.ModelInput.from_ints(
                    request.prompt_tokens
                ),
                num_samples=request.num_samples,
                sampling_params=params,
                return_text=True,
            )
        )
    return list(await asyncio.gather(*tasks))
```

采样返回后，`consume_assistant()` 先保存原始 token 与 old logprob，再调用上一节的协议解析器。合法搜索会变成 `PendingSearch`；最终回答、非法格式或预算耗尽都会结束当前轨迹：

```python
def consume_assistant(
    trajectory: Trajectory,
    prompt_tokens: list[int],
    sequence: Any,
    tokenizer: Any,
    config: RolloutConfig,
) -> PendingSearch | None:
    tokens, logprobs, text = read_sequence(
        sequence, tokenizer
    )
    trajectory.turns.append(
        AssistantTurn(
            prompt_tokens,
            tokens,
            logprobs,
            text,
        )
    )
    parsed = parse_assistant(text)

    can_search = (
        parsed.kind == "tool"
        and trajectory.search_calls
        < config.max_search_calls
        and len(trajectory.turns)
        < config.max_assistant_turns
    )
    if not can_search:
        trajectory.messages.append(
            {"role": "assistant", "content": text}
        )
        trajectory.final_text = text
        trajectory.done = True
        return None

    call_id = (
        f"search-{trajectory.question_index}-"
        f"{trajectory.group_index}-"
        f"{trajectory.search_calls + 1}"
    )
    messages_before_assistant = list(
        trajectory.messages
    )
    trajectory.messages.append(
        {"role": "assistant", "content": text}
    )
    return PendingSearch(
        trajectory=trajectory,
        messages_before_assistant=(
            messages_before_assistant
        ),
        assistant_text=text,
        prompt_tokens=prompt_tokens,
        completion_tokens=tokens,
        call_id=call_id,
        query=parsed.query or "",
    )
```

`resolve_searches()` 使用线程池并发调用不同轨迹的搜索后端，再按原顺序把结果和待处理轨迹配对：

```python
def resolve_searches(
    pending_searches: list[PendingSearch],
    search_client: SearchClient,
    tokenizer: Any,
    config: RolloutConfig,
) -> int:
    if not pending_searches:
        return 0
    workers = min(
        config.search_concurrency,
        len(pending_searches),
    )
    with ThreadPoolExecutor(
        max_workers=workers
    ) as pool:
        results = list(
            pool.map(
                search_client.search,
                [
                    pending.query
                    for pending in pending_searches
                ],
            )
        )
    return sum(
        finish_search(
            pending,
            result,
            tokenizer,
            config,
        )
        for pending, result in zip(
            pending_searches,
            results,
            strict=True,
        )
    )
```

每个结果随后由 `finish_search()` 写回原来的轨迹：

```python
def finish_search(
    pending: PendingSearch,
    result: SearchResult,
    tokenizer: Any,
    config: RolloutConfig,
) -> bool:
    fitted = fit_tool_content(
        tokenizer,
        pending.messages_before_assistant,
        pending.assistant_text,
        pending.prompt_tokens,
        pending.completion_tokens,
        pending.call_id,
        result,
        config,
    )
    if fitted is None:
        pending.trajectory.final_text = (
            pending.assistant_text
        )
        pending.trajectory.done = True
        return True

    content, next_prompt_tokens = fitted
    pending.trajectory.messages.append(
        tool_message(pending.call_id, content)
    )
    pending.trajectory.next_prompt_tokens = (
        next_prompt_tokens
    )
    pending.trajectory.search_calls += 1
    return False
```

`fit_tool_content()` 会逐条加入搜索证据。只要 observation 超过单次工具预算或完整轨迹预算，就停止加入后续证据；如果连一条结果都放不下，轨迹会直接结束。这样，搜索服务返回多少文本和模型实际能看到多少文本是两个明确分开的边界。

一组 GRPO 轨迹在第一轮共享完全相同的 prompt。代码用一次请求生成 `group_size` 个分支：

```python
first_requests: list[SampleRequest] = []
for index, trajectory in enumerate(roots):
    request = make_request(
        tokenizer,
        trajectory,
        index,
        config.group_size,
        config.seed + index,
        config,
    )
    if request:
        first_requests.append(request)
```

采样响应中的每条 sequence 都从根轨迹深拷贝出一个独立分支，随后再分别解析其搜索动作：

```python
responses = asyncio.run(
    sample_requests_async(
        sampling_client,
        first_requests,
        config,
        tokenizer,
    )
)
pending_searches: list[PendingSearch] = []
for request, response in zip(
    first_requests,
    responses,
    strict=True,
):
    root = roots[request.trajectory_index]
    if len(response.sequences) != config.group_size:
        raise ValueError(
            "首轮采样数量与 group_size 不一致"
        )

    for group_index, sequence in enumerate(
        response.sequences
    ):
        branch = copy.deepcopy(root)
        branch.group_index = group_index
        pending = consume_assistant(
            branch,
            request.prompt_tokens,
            sequence,
            tokenizer,
            config,
        )
        trajectories.append(branch)
        if pending is not None:
            pending_searches.append(pending)

resolve_searches(
    pending_searches,
    search_client,
    tokenizer,
    config,
)
```

不同分支执行搜索后，observation 与历史动作已经不同。后续轮次对每条未结束轨迹分别设置 `num_samples=1`：

```python
while any(not item.done for item in trajectories):
    requests: list[SampleRequest] = []
    for index, trajectory in enumerate(trajectories):
        if trajectory.done:
            continue
        request = make_request(
            tokenizer,
            trajectory,
            index,
            1,
            (
                config.seed
                + index
                + len(trajectory.turns) * 10_000
            ),
            config,
        )
        if request:
            requests.append(request)

    if not requests:
        break
    responses = asyncio.run(
        sample_requests_async(
            sampling_client,
            requests,
            config,
            tokenizer,
        )
    )

    pending_searches = []
    for request, response in zip(
        requests, responses, strict=True
    ):
        if len(response.sequences) != 1:
            raise ValueError(
                "后续轮次必须只采样一个分支"
            )
        trajectory = trajectories[
            request.trajectory_index
        ]
        pending = consume_assistant(
            trajectory,
            request.prompt_tokens,
            response.sequences[0],
            tokenizer,
            config,
        )
        if pending is not None:
            pending_searches.append(pending)

    resolve_searches(
        pending_searches,
        search_client,
        tokenizer,
        config,
    )
```

这种“共享根节点、随后分叉”的实现同时满足两个条件：同题轨迹能够进行 GRPO 组内比较，每条分支又能根据自己的搜索结果继续行动。多个 PyTRIO 采样请求和搜索请求都可以并发执行，从而减少多轮环境交互带来的等待时间。

状态机还必须设置明确边界：

- `max_search_calls`：一条轨迹最多调用多少次搜索；
- `max_assistant_turns`：最多生成多少轮 Assistant 消息；
- `max_assistant_tokens`：单轮动作的 token 上限；
- `max_tool_response_tokens`：单次 observation 的 token 上限；
- `max_trajectory_tokens`：整条上下文的总 token 上限；
- 搜索 timeout 和 concurrency：限制外部服务等待时间与并发压力。

这些限制既控制训练成本，也定义了 Agent 可以访问的环境范围。评测时必须保持相同配置，否则更高的搜索预算本身就可能提高答案正确率。

##### 8.3.4 工具协议与 token 连续性

多轮训练最容易出现的问题，是重新渲染 chat template 后的 token 与真实采样 token 不一致。tokenizer 可能清理空格、规范工具调用文本，或自动补充轮次结束符。如果训练阶段重新编码模型文本，旧 logprob 将无法和目标 token 一一对应。

本章遵循两个原则：

1. Assistant 动作始终保留 sampler 返回的原始 token；
2. 只通过 chat template 计算新加入的结束符与 tool observation token。

`build_next_prompt()` 的完整职责，是从 chat template 中只提取“Assistant 结束符 + 新 observation”这一段增量 token，再接到 sampler 返回的真实 completion 后面：

```python
def build_next_prompt(
    tokenizer: Any,
    messages_before_assistant: list[dict[str, Any]],
    assistant_text: str,
    previous_prompt_tokens: list[int],
    completion_tokens: list[int],
    next_tool_message: dict[str, Any],
) -> list[int]:
    canonical_prompt = build_prompt(
        tokenizer,
        messages_before_assistant,
    )

    empty_assistant_end = _render_chat(
        tokenizer,
        [
            *messages_before_assistant,
            {"role": "assistant", "content": ""},
        ],
        add_generation_prompt=False,
    )
    if empty_assistant_end[
        :len(canonical_prompt)
    ] != canonical_prompt:
        raise ValueError(
            "chat template 无法从空 assistant 提取结束边界"
        )
    assistant_closing_tokens = empty_assistant_end[
        len(canonical_prompt):
    ]

    assistant_message = {
        "role": "assistant",
        "content": assistant_text,
    }
    messages_with_assistant = [
        *messages_before_assistant,
        assistant_message,
    ]
    canonical_assistant_end = _render_chat(
        tokenizer,
        messages_with_assistant,
        add_generation_prompt=False,
    )
    canonical_next_prompt = build_prompt(
        tokenizer,
        [*messages_with_assistant, next_tool_message],
    )
    if canonical_next_prompt[
        :len(canonical_assistant_end)
    ] != canonical_assistant_end:
        raise ValueError(
            "加入 tool observation 后 chat template 改写了历史消息"
        )

    observation_tokens = canonical_next_prompt[
        len(canonical_assistant_end):
    ]
    overlap = _suffix_prefix_overlap(
        completion_tokens,
        assistant_closing_tokens,
    )
    return [
        *previous_prompt_tokens,
        *completion_tokens,
        *assistant_closing_tokens[overlap:],
        *observation_tokens,
    ]
```

`overlap` 用来处理 sampler 已经返回部分 Assistant 结束符的情况，避免重复补 token。`messages` 负责协议记录与调试，`next_prompt_tokens` 才是下一轮真正提交给 sampler 的模型输入；两者不能混为一谈。

到下一轮训练数据构造时，还会再次验证：

```python
if turn.prompt_tokens[:len(full_tokens)] != full_tokens:
    raise ValueError(
        "下一轮 prompt 不是已有轨迹的前缀扩展"
    )
```

这两层校验能够尽早发现模板改写、结束符重复和 observation 拼接错误。对于 Agentic RL，token 连续性属于算法正确性的一部分；轨迹在文本层面看起来合理，仍可能因 token 边界错位而产生错误梯度。

##### 8.3.5 Reward、组内优势与 observation mask

本章使用 NQ 和 HotpotQA 的短答案任务。模型最终需要输出唯一一行：

```text
Answer: <short answer>
```

规则奖励分为三档：

$$R(\tau)=\begin{cases}1, & \text{格式正确且答案精确匹配},\\ 0, & \text{格式正确但答案错误},\\ -0.1, & \text{最终格式无效}.\end{cases}$$

`reward.py` 先抽取唯一一行最终答案，再统一大小写、标点、英文冠词和空格：

```python
def normalize_answer(text: str) -> str:
    lowered = text.lower()
    without_punctuation = "".join(
        char
        for char in lowered
        if not unicodedata.category(char).startswith("P")
    )
    without_articles = ARTICLE_PATTERN.sub(
        " ", without_punctuation
    )
    return " ".join(without_articles.split())


def extract_answer(text: str) -> str | None:
    matches = ANSWER_PATTERN.findall(text)
    if len(matches) != 1:
        return None
    answer = matches[0].strip()
    return answer or None


def score_answer(
    text: str,
    references: list[str],
) -> RewardResult:
    answer = extract_answer(text)
    if answer is None:
        return RewardResult(
            -0.1, False, False, None
        )
    normalized = normalize_answer(answer)
    exact_match = any(
        normalized == normalize_answer(reference)
        for reference in references
    )
    return RewardResult(
        float(exact_match),
        True,
        exact_match,
        answer,
    )
```

这段代码只评价最终任务结果，没有为“搜了几次”或“query 看起来不错”增加额外分数。对同一道问题的 $G$ 条完整轨迹，仍然使用 GRPO 组内基线：

$$A_i=R(\tau_i)-\frac{1}{G}\sum_{j=1}^{G}R(\tau_j).$$

Search-R1 论文同时讨论了 PPO 与 GRPO 等优化方式。本章选择 GRPO 的同题分组方案，让 Search-R1 与 8.1 节使用同一种 advantage 构造方法。

`rollout_batch()` 必须等整组轨迹全部结束后，才能执行下面的函数：

```python
def assign_group_advantages(
    trajectories: list[Trajectory],
) -> int:
    groups: dict[int, list[Trajectory]] = {}
    for trajectory in trajectories:
        groups.setdefault(
            trajectory.question_index, []
        ).append(trajectory)

    degenerate = 0
    for group in groups.values():
        mean_reward = sum(
            item.reward for item in group
        ) / len(group)
        for item in group:
            item.advantage = (
                item.reward - mean_reward
            )
        if all(
            item.advantage == 0.0 for item in group
        ):
            degenerate += 1
    return degenerate
```

整组 reward 完全相同时，所有 advantage 都为 0，这一组不会产生有效梯度。训练代码会跳过这些轨迹，并记录退化组比例。组内均值不能等拆成 micro-batch 后再计算，否则比较基线已经被改变。

这个 advantage 会分配给轨迹中每一轮 Assistant 生成的 token。搜索 observation 只构成下一步决策所需的状态，不是策略做出的动作，因此 observation token 的 logprob 和 advantage 都设为 0：

```python
full_tokens.extend(delta_observation)
old_logprobs_by_token.extend(
    [0.0] * len(delta_observation)
)
advantages_by_token.extend(
    [0.0] * len(delta_observation)
)

full_tokens.extend(turn.completion_tokens)
old_logprobs_by_token.extend(turn.logprobs)
advantages_by_token.extend(
    [trajectory.advantage]
    * len(turn.completion_tokens)
)
```

这种 observation mask 有两个作用。首先，训练器不会要求模型预测搜索引擎返回的文本；其次，observation 仍然保留在上下文中，后续 Assistant token 可以对这些证据进行条件建模。

搜索调用和最终回答共享一个轨迹级 advantage。若最终答案正确，导致成功的查询规划、搜索词和答案 token 都会得到鼓励；若最终答案错误，整条动作链都会被抑制。这正是 outcome reward 能够训练工具使用策略的原因。

##### 8.3.6 构造多轮 PyTRIO Datum

`train.py` 的 `build_datum()` 把前面几节的 token 连续性和 observation mask 汇合到一起。下面是完整的核心实现：

```python
def build_datum(
    trajectory: Trajectory,
) -> TrainingDatum:
    if not trajectory.turns:
        raise ValueError(
            "不能用没有 assistant turn 的轨迹构造训练 Datum"
        )

    full_tokens: list[int] = []
    old_logprobs_by_token: list[float] = []
    advantages_by_token: list[float] = []
    assistant_token_count = 0

    for turn_index, turn in enumerate(
        trajectory.turns
    ):
        if len(turn.completion_tokens) != len(
            turn.logprobs
        ):
            raise ValueError(
                f"第 {turn_index + 1} 个 assistant turn "
                "的 token 与 logprob 长度不一致"
            )

        if turn_index == 0:
            delta_observation = turn.prompt_tokens
        elif turn.prompt_tokens[
            :len(full_tokens)
        ] == full_tokens:
            delta_observation = turn.prompt_tokens[
                len(full_tokens):
            ]
        else:
            raise ValueError(
                f"第 {turn_index + 1} 个 assistant turn "
                "的 prompt 不是已有轨迹的前缀扩展，"
                "无法安全对齐采样 logprob"
            )

        full_tokens.extend(delta_observation)
        full_tokens.extend(turn.completion_tokens)
        old_logprobs_by_token.extend(
            [0.0] * len(delta_observation)
        )
        old_logprobs_by_token.extend(turn.logprobs)
        advantages_by_token.extend(
            [0.0] * len(delta_observation)
        )
        advantages_by_token.extend(
            [trajectory.advantage]
            * len(turn.completion_tokens)
        )
        assistant_token_count += len(
            turn.completion_tokens
        )

    if assistant_token_count == 0:
        raise ValueError(
            "不能用没有 assistant token 的轨迹构造训练 Datum"
        )
    if not (
        len(full_tokens)
        == len(old_logprobs_by_token)
        == len(advantages_by_token)
    ):
        raise ValueError(
            "完整轨迹的 token、logprob 和 advantage 长度不一致"
        )

    input_tokens = full_tokens[:-1]
    target_tokens = full_tokens[1:]
    old_logprobs = old_logprobs_by_token[1:]
    advantages = advantages_by_token[1:]
    if not (
        len(input_tokens)
        == len(target_tokens)
        == len(old_logprobs)
        == len(advantages)
    ):
        raise ValueError(
            "Datum 的 input、target、logprobs 和 advantages 长度不一致"
        )
    if len(input_tokens) > MAX_TRAIN_CONTEXT_TOKENS:
        raise ValueError(
            f"Datum 超过 {MAX_TRAIN_CONTEXT_TOKENS} token"
        )

    datum = trio.Datum(
        model_input=trio.ModelInput.from_ints(
            input_tokens
        ),
        loss_fn_inputs={
            "target_tokens": np.asarray(
                target_tokens,
                dtype=np.int64,
            ),
            "logprobs": np.asarray(
                old_logprobs,
                dtype=np.float32,
            ),
            "advantages": np.asarray(
                advantages,
                dtype=np.float32,
            ),
        },
    )
    return TrainingDatum(datum, len(input_tokens))
```

第一轮的 `delta_observation` 是 system prompt、工具定义和用户问题；后续轮次的 `delta_observation` 是上一轮结束符、搜索结果以及新一轮 Assistant 前缀。它们都保留真实 target token，但 old logprob 与 advantage 为 0。只有 sampler 真正生成的 Assistant token 携带 rollout old logprob 和轨迹 advantage。

完整 group 的 reward 必须全部计算完毕，才能得到正确的组内均值。不能在单条轨迹结束后立刻更新策略，因为同组其他分支的奖励还未知。

多轮轨迹长度差异很大，直接把所有数据放入一个 padded batch 会浪费大量 token。配套代码根据样本长度把 `Datum` 装入多个 micro-batch，并按每批轨迹数占完整 rollout 轨迹数的比例重新加权 loss。这样可以在保持全局样本平均梯度语义的同时控制单批 padding 大小。

##### 8.3.7 从 rollout 到一次参数更新

`train.py` 的外层循环把前面的模块串成一个完整训练 step。关键顺序不能交换：

```python
batch = take_batch(
    examples,
    step * args.questions_per_batch,
    args.questions_per_batch,
)

sampling_client = (
    training_client
    .save_weights_and_get_sampling_client()
)

trajectories = rollout_batch(
    sampling_client=sampling_client,
    tokenizer=tokenizer,
    search_client=search_client,
    examples=batch,
    config=rollout_config,
)

datums = build_training_datums(trajectories)
micro_batches = pack_micro_batches(datums)

trainer_results = []
for micro_batch in micro_batches:
    weighted_datums = (
        weight_micro_batch_for_global_mean(
            micro_batch,
            total_samples=len(trajectories),
        )
    )
    result = training_client.forward_backward(
        weighted_datums,
        loss_fn="importance_sampling",
    ).result()
    trainer_results.append(result)

if micro_batches:
    training_client.optim_step(
        adam_params
    ).result()
```

第一，`save_weights_and_get_sampling_client()` 在每个 step 开始时导出当前 LoRA 权重，因此 old logprob 来自本次更新前的当前策略。第二，`rollout_batch()` 内部已经完成整组 reward 和 advantage，`build_training_datums()` 会跳过 advantage 全为 0 的轨迹。第三，所有 micro-batch 只累计梯度，整个 logical batch 最后只调用一次 `optim_step()`。

PyTRIO 会对一次 `forward_backward()` 内的样本取平均。如果第 $k$ 个 micro-batch 有 $n_k$ 条轨迹，而完整 rollout batch 有 $N$ 条轨迹，代码会先把该批 advantage 乘以 $n_k/N$：

$$\sum_k\frac{n_k}{N}\operatorname{mean}(\mathcal L_k)=\operatorname{mean}(\mathcal L_{\mathrm{global}}).$$

对应实现只重新包装 `Datum`，不修改 target token 和 old logprob：

```python
micro_batch_weight = np.float32(
    len(micro_batch) / total_samples
)
weighted_datums = []
for item in micro_batch:
    loss_inputs = item.datum.loss_fn_inputs
    weighted_datums.append(
        trio.Datum(
            model_input=item.datum.model_input,
            loss_fn_inputs={
                "target_tokens": (
                    loss_inputs["target_tokens"]
                    .to_numpy()
                ),
                "logprobs": (
                    loss_inputs["logprobs"]
                    .to_numpy()
                ),
                "advantages": (
                    loss_inputs["advantages"]
                    .to_numpy()
                    * micro_batch_weight
                ),
            },
        )
    )
```

因此，动态拆批只改变执行时的 padding 和显存占用，不改变逻辑 batch 的样本平均梯度。

##### 8.3.8 运行、评测与实验边界

Search-R1 代码按数据、协议、环境、rollout 和训练职责拆分：

| 文件 | 作用 |
| --- | --- |
| `prepare_data.py` | 准备 NQ 与 HotpotQA 数据 |
| `data.py` | 加载统一 JSONL 样本 |
| `protocol.py` | 定义搜索工具与多轮消息协议 |
| `search.py` | 封装搜索后端并统一结果格式 |
| `rollout.py` | 执行多轮搜索状态机 |
| `reward.py` | 抽取短答案并计算规则奖励 |
| `train.py` | 构造 observation mask、micro-batch 并更新策略 |
| `eval.py` | 在同一环境中评测 Base Model 或 checkpoint |
| `analyse.py` | 汇总评测输出 |

评测没有另写一套简化的搜索逻辑，而是复用同一个 `rollout_batch()`。主要区别是每道题只保留一条轨迹，不再需要训练阶段的组内比较：

```python
config = RolloutConfig(
    group_size=1,
    max_search_calls=args.max_search_calls,
    max_assistant_turns=args.max_assistant_turns,
    max_trajectory_tokens=(
        args.max_trajectory_tokens
    ),
    max_assistant_tokens=args.max_assistant_tokens,
    max_tool_response_tokens=(
        args.max_tool_response_tokens
    ),
    search_concurrency=args.search_concurrency,
    temperature=args.temperature,
    top_p=args.top_p,
    seed=args.seed,
)

batch_trajectories = rollout_batch(
    sampling_client,
    tokenizer,
    search_client,
    batch,
    config,
)
```

`model_path` 留空时，`eval.py` 创建 Base Model sampler；传入 `save_weights_for_sampler()` 返回的路径时，则评测训练后的 checkpoint。两种模型仍使用相同的协议、搜索后端、预算、题集与答案判定器。

首先准备数据：

```bash
python docs/chapter8/search-r1/prepare_data.py
```

Wikipedia 后端无需 API Key，适合验证完整链路：

```bash
python docs/chapter8/search-r1/train.py \
    --max-steps 1 \
    --questions-per-batch 1 \
    --group-size 4 \
    --max-search-calls 2 \
    --search-backend wikipedia \
    --search-concurrency 3 \
    --swanlab-mode disabled
```

使用同一个 Wikipedia 环境评测 Base Model：

```bash
python docs/chapter8/search-r1/eval.py \
    --search-backend wikipedia \
    --batch-size 8 \
    --output docs/chapter8/search-r1/eval_result/base.jsonl
```

评测训练后的 sampler weights 时，保持其余参数不变，只增加 checkpoint 路径：

```bash
python docs/chapter8/search-r1/eval.py \
    --search-backend wikipedia \
    --batch-size 8 \
    --model-path 'trio://runxxxxxxxxxx' \
    --output docs/chapter8/search-r1/eval_result/checkpoint.jsonl
```

确认流程后，再逐步扩大问题数、group size、搜索次数与轨迹预算。实验至少应记录：

- 最终答案 exact match；
- 有效答案格式比例；
- 平均搜索调用次数与零搜索比例；
- 搜索失败率、超时率和 observation 截断率；
- 平均轨迹长度与每步有效训练 token；
- 退化组比例；
- rollout、搜索和训练各阶段耗时。

搜索结果具有外部依赖。在线页面会更新，搜索服务的排序也可能变化。比较 Base Model 与训练 checkpoint 时，应固定题集、搜索后端、搜索预算、sampling 参数和评测时间窗口。若需要严格可复现的论文实验，可以将检索语料与索引固定为只读快照。

本章只更新语言模型策略，搜索后端保持固定。若检索器本身也参与学习，就需要额外定义检索动作空间、索引版本和跨模块 credit assignment，这已经超出本节示例范围。

Search-R1 展示了如何把 GRPO 的组内相对优势扩展到包含外部 observation 的多轮搜索轨迹。下一节的 ReTool 会保留同样的多轮 rollout 与 observation mask，将环境从搜索引擎换成代码解释器，并使用 PyTRIO 内置的 PPO 更新策略。

#### 8.4 ReTool

> **代码来源：** 本节依据作者开源仓库 [agentic-rl-lab/05-retool](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/05-retool) 中的完整多文件实现整理。正文按照 `prepare_data.py`、`protocol.py`、`sandbox.py`、`rollout.py`、`reward.py`、`train.py`、`eval.py` 与 `analysis.py` 的真实调用链展开。

搜索工具帮助模型获取外部知识，代码解释器则帮助模型完成精确计算、符号操作与枚举验证。模型已经能在提示词或监督数据的引导下调用 Python 工具，但“会调用”还不等于“会在合适的时机调用”。有些问题口算更快，有些问题适合编写短程序，还有些代码执行失败后需要根据错误信息修正。

ReTool 使用强化学习训练这种策略性工具使用能力。模型自主决定是否调用代码解释器、编写什么代码、如何读取执行结果，以及何时给出最终答案。环境只根据最终数学答案提供结果奖励，成功轨迹中的工具决策会随整条轨迹共同得到强化。

> **安全提示：** 配套 `sandbox.py` 只是带资源限制的本地 subprocess，不是可信安全沙箱。模型生成的代码仍能读取当前账号可访问的文件、继承环境变量并访问网络。真实训练应放在一次性容器、低权限虚拟机或专用沙箱服务中，并移除 PyTRIO、SwanLab、SSH 和云服务凭证。

ReTool 的代码链路与 Search-R1 结构相似，但环境从搜索服务换成了 Python 进程：

```text
prepare_data.py / data.py
        ↓ 读取数学题与参考答案
protocol.py
        ↓ 解析 code_interpreter 调用
sandbox.py
        ↓ 执行代码，返回 stdout / stderr / timeout
rollout.py
        ↓ 追加执行结果并继续生成
reward.py
        ↓ 检查最后一个 \boxed{}
train.py
        ↓ feedback mask、PPO、optim_step
eval.py / analysis.py
        ↓ text-only 与 ReTool 对照评测
```

下面仍然顺着实际函数调用解释，而不是只看工具调用的文本格式。

##### 8.4.1 从工具调用格式到工具使用策略

一次典型 ReTool 轨迹如下：

```text
User: 计算满足条件的整数解数量。

Assistant -> code_interpreter(
    "count = ...\nprint(count)"
)
Tool: 37

Assistant: 根据枚举结果，答案为 \boxed{37}
```

如果代码出现错误，模型还可以利用 traceback 自我修正：

```text
Assistant -> code_interpreter("print(sum(values))")
Tool: NameError: name 'values' is not defined

Assistant -> code_interpreter(
    "values = [...]\nprint(sum(values))"
)
Tool: 128

Assistant: \boxed{128}
```

从强化学习角度看，代码、执行错误、数值结果和最终回答共同构成轨迹。代码解释器是环境，Assistant 生成的工具调用与自然语言答案都是动作，stdout 或 stderr 是 observation。


![ReTool 的多轮代码执行与结果奖励](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/docs/images/8-images/8-5-retool.png)
图 8.5 ReTool 的多轮代码执行与结果奖励


ReTool 不需要为“调用了工具”单独加分。最终答案 reward 会通过轨迹级 advantage 传递到前面的代码动作。这样，只有真正帮助任务成功的工具使用方式会得到正向信号，冗余或误导性的调用会随失败轨迹受到抑制。

##### 8.4.2 Cold-start、训练数据与工具协议

原始 ReTool 包含两个阶段：

1. **Cold-start SFT**：使用带代码调用与执行反馈的轨迹，让模型先掌握协议和基本交互形式；
2. **Reinforcement Learning**：模型自主 rollout，通过最终答案 reward 学习何时以及如何使用工具。

Cold-start 的作用是让初始策略产生一定比例的有效工具调用。如果基础模型完全不会输出工具协议，早期轨迹几乎全部失败，GRPO 很难从组内比较中获得有意义的探索信号。

本章代码选择已经具备原生 function calling 能力的 Qwen3.5，并直接展示第二阶段的 PyTRIO 训练，因此没有附带一条专门的 Cold-start SFT 流程。这是教学实现与原论文设置之间的重要边界。更换为缺少工具调用能力的基础模型时，应先准备 SFT 数据，验证合法调用率达到可训练水平，再启动 RL。

RL 数据来自 DAPO-Math-17k。原始题目外面带有要求 `Answer: $Answer` 的统一模板，它会与本节要求的 `\boxed{}` 格式冲突，因此 `prepare_data.py` 先剥掉外层模板，再只保留题目和参考答案：

```python
def normalize_row(
    index: int,
    row: dict[str, Any],
) -> dict[str, Any] | None:
    prompt = row.get("prompt")
    if not isinstance(prompt, list) or not prompt:
        return None

    question = strip_dapo_template(
        str(prompt[0].get("content") or "")
    )
    reward_model = row.get("reward_model") or {}
    ground_truth = (
        reward_model.get("ground_truth")
        if isinstance(reward_model, dict)
        else None
    )
    if isinstance(ground_truth, list):
        ground_truth = (
            ground_truth[0] if ground_truth else None
        )
    answer = str(ground_truth or "").strip()
    if not question or not answer:
        return None

    return {
        "id": str(
            row.get("extra_info", {}).get("index")
            or index
        ),
        "question": question,
        "answer": answer,
        "data_source": str(
            row.get("data_source") or "dapo_math"
        ),
    }
```

和 Search-R1 一样，训练样本不含标准代码和工具调用次数。策略必须自己探索是否调用解释器以及生成什么代码。

代码解释器使用结构化工具定义：

```python
CODE_TOOL = {
    "type": "function",
    "function": {
        "name": "code_interpreter",
        "description": (
            "Run Python code and return printed output. "
            "Each execution starts fresh."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "code": {"type": "string"},
            },
            "required": ["code"],
        },
    },
}
```

`protocol.py` 对工具调用同样采用严格解析。Python 代码可以包含比较符、引号和多行文本，因此这里只校验调用数量、调用位置以及代码是否为空：

```python
def parse_assistant(text: str) -> ParsedAssistant:
    matches = list(TOOL_CALL_PATTERN.finditer(text))
    if not matches:
        kind = (
            "invalid" if "<tool_call>" in text else "answer"
        )
        return ParsedAssistant(
            kind=kind,
            content=text.strip(),
        )

    if len(matches) != 1 or text[matches[0].end():].strip():
        return ParsedAssistant(
            kind="invalid",
            content=text.strip(),
        )

    code = matches[0].group(1).strip()
    if not code:
        return ParsedAssistant(
            kind="invalid",
            content=text.strip(),
        )

    content = text[:matches[0].start()].strip()
    return ParsedAssistant(
        kind="tool",
        content=content,
        code=code,
    )
```

合法输出只允许三种去向：`tool` 进入代码执行环境，`answer` 结束轨迹并接受结果奖励，`invalid` 结束轨迹并按错误答案处理。系统不为格式接近但不完整的工具调用做猜测性修复，否则训练环境中的动作定义会变得不稳定。

rollout 状态机与 Search-R1 相似，只是环境动作从 `search(query)` 换成 `code_interpreter(code)`。每条轨迹都受到以下预算约束：

- 最大代码调用次数；
- 最大 Assistant 轮数；
- 单轮生成与执行结果 token 数；
- 完整轨迹 token 数；
- 单次执行时间；
- 本地执行器并发数。

同一次代码调用不保留 Python 变量和进程状态。模型需要在每次调用中重新定义所需数据，这使轨迹语义更清楚，也减少了不同执行之间的隐式依赖。

##### 8.4.3 执行结果怎样接回真实 token 轨迹

ReTool 也不能把 Assistant 文本 decode 后重新 tokenize。`protocol.py` 使用一个占位 Assistant 提取模板闭合 token，再把实际执行结果对应的 observation token 接到真实 completion 后：

```python
def build_next_prompt(
    tokenizer: Any,
    messages_before_assistant: list[dict[str, Any]],
    previous_prompt_tokens: list[int],
    completion_tokens: list[int],
    next_tool_message: dict[str, Any],
) -> list[int]:
    canonical_prompt = build_prompt(
        tokenizer,
        messages_before_assistant,
    )
    placeholder_message = {
        "role": "assistant",
        "content": "x",
    }
    messages_with_assistant = [
        *messages_before_assistant,
        placeholder_message,
    ]
    canonical_assistant_end = _render_chat(
        tokenizer,
        messages_with_assistant,
        add_generation_prompt=False,
    )

    placeholder_tokens = _encoded_text_tokens(
        tokenizer, "x"
    )
    canonical_action = [
        *canonical_prompt,
        *placeholder_tokens,
    ]
    if canonical_assistant_end[
        :len(canonical_action)
    ] != canonical_action:
        raise ValueError(
            "chat template 无法定位 assistant 结束边界"
            "（占位内容也不匹配）"
        )
    assistant_closing_tokens = canonical_assistant_end[
        len(canonical_action):
    ]

    canonical_next_prompt = build_prompt(
        tokenizer,
        [*messages_with_assistant, next_tool_message],
    )
    if canonical_next_prompt[
        :len(canonical_assistant_end)
    ] != canonical_assistant_end:
        raise ValueError(
            "加入 tool observation 后 chat template 改写了历史消息"
        )
    observation_tokens = canonical_next_prompt[
        len(canonical_assistant_end):
    ]

    overlap = _suffix_prefix_overlap(
        completion_tokens,
        assistant_closing_tokens,
    )
    return [
        *previous_prompt_tokens,
        *completion_tokens,
        *assistant_closing_tokens[overlap:],
        *observation_tokens,
    ]
```

这里使用占位内容，是因为 Qwen chat template 可能把真实采样文本中的 reasoning 与 content 重新分段。占位消息只用于计算固定模板边界，真实模型动作仍始终来自 `completion_tokens`。下一轮 `prompt_tokens` 必须以前一轮的完整 token 为前缀，否则 `train.py` 会拒绝构造 `Datum`。

##### 8.4.4 Outcome reward 与 interpreter feedback mask

本章从最终回答的末尾抽取最后一个 $\boxed{}$，使用 `math_verify` 判断预测值与参考答案是否数学等价：

```python
def extract_last_boxed(text: str) -> str | None:
    marker = "\\boxed{"
    index = text.rfind(marker)
    if index < 0:
        return None

    start = index + len(marker)
    depth = 1
    for position in range(start, len(text)):
        if text[position] == "{":
            depth += 1
        elif text[position] == "}":
            depth -= 1
            if depth == 0:
                return text[start:position]
    return None


def answers_equivalent(
    prediction: str,
    reference: str,
) -> bool:
    try:
        return bool(
            verify(
                parse(f"${reference}$"),
                parse(f"${prediction}$"),
            )
        )
    except Exception:
        return False


def score_answer(
    text: str,
    reference: str,
) -> RewardResult:
    answer = extract_last_boxed(
        text[-ANSWER_WINDOW_CHARS:]
    )
    if answer is None:
        return RewardResult(
            -1.0, False, False, None
        )

    correct = answers_equivalent(
        answer.strip(),
        reference.strip(),
    )
    return RewardResult(
        1.0 if correct else -1.0,
        correct,
        True,
        answer,
    )
```

奖励函数为：

$$R(\tau)=\begin{cases}+1, & \text{最终答案正确},\\ -1, & \text{答案错误或格式无效}.\end{cases}$$

再对同题轨迹计算中心化 advantage：

$$A_i=R(\tau_i)-\bar R.$$

代码执行结果属于环境 observation。它应出现在模型上下文中，同时不能进入策略 loss。ReTool 论文将这一处理称为 interpreter feedback mask，本章采用与 Search-R1 相同的 token 对齐方式：

| token 区域 | 是否保留在上下文 | old logprob | advantage |
| --- | --- | --- | --- |
| 初始 prompt | 是 | 0 | 0 |
| Assistant 推理与代码调用 | 是 | rollout logprob | 轨迹 advantage |
| stdout、stderr 或超时信息 | 是 | 0 | 0 |
| 最终答案 | 是 | rollout logprob | 轨迹 advantage |

配套代码使用 PyTRIO 的 PPO loss：

```python
PPO_LOSS_CONFIG = {
    "clip_low_threshold": 0.8,
    "clip_high_threshold": 1.28,
}

training_client.forward_backward(
    datums,
    loss_fn="ppo",
    loss_fn_config=PPO_LOSS_CONFIG,
).result()
```

原始 ReTool 论文的强化学习阶段使用 PPO。本章保留多轮代码轨迹、结果奖励和 interpreter feedback mask，同时加入同题分组采样与中心化 advantage；因此，训练链路可以概括为“GRPO 构造相对优势，PPO clipping 控制策略更新”。

这里采用非对称概率比边界。旧策略概率比低于 0.8 或高于 1.28 时，PPO 会限制对应更新。无论使用何种 clip 参数，rollout sampler 都需要在每个训练 step 开始前从当前权重刷新。

##### 8.4.5 代码执行环境与安全边界

执行模型生成的代码具有真实风险。本章 `sandbox.py` 使用本地 subprocess，并加入了以下工程限制：

- 使用参数列表启动 Python，不经过 shell；
- 每次调用创建独立进程；
- 设置 wall-clock timeout 与 CPU 时间上限；
- 超时后终止整个子进程组；
- 限制 BLAS 等数值库的线程数；
- stdout 和 stderr 写入临时文件，并限制读回长度；
- 限制并发执行数量；
- 清理可能破坏 chat template 的特殊标记。

执行入口是 `LocalPythonSandbox.run_code()`。模型代码先被嵌入一个设置 CPU 限制的 bootstrap，再通过参数列表传给新的 Python 进程：

```python
def run_code(self, code: str) -> ExecResult:
    started = time.perf_counter()
    self.stats.calls += 1
    bootstrap = _BOOTSTRAP.format(
        cpu=int(self.timeout) + 5,
        code=repr(code),
    )
    env = {
        **os.environ,
        **_CHILD_ENV_OVERRIDES,
    }

    with self._semaphore:
        with (
            tempfile.TemporaryFile() as stdout_file,
            tempfile.TemporaryFile() as stderr_file,
        ):
            process = subprocess.Popen(
                [
                    self.python,
                    "-B",
                    "-c",
                    bootstrap,
                ],
                stdout=stdout_file,
                stderr=stderr_file,
                env=env,
                start_new_session=True,
            )
            timed_out = False
            try:
                returncode = process.wait(
                    timeout=self.timeout
                )
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(
                    process.pid,
                    signal.SIGKILL,
                )
                returncode = None
                process.wait()

            stdout = _truncate_tail(
                _read_capped(stdout_file)
            )
            stderr = _truncate_tail(
                _read_capped(stderr_file)
            )

    latency = time.perf_counter() - started
    ok = not timed_out and returncode == 0
    if timed_out:
        self.stats.timeouts += 1
    elif ok:
        self.stats.successes += 1
    else:
        self.stats.errors += 1
    self.stats.latency_total += latency
    return ExecResult(
        ok,
        stdout,
        stderr,
        returncode,
        timed_out,
        latency,
    )
```

stdout 和 stderr 写入临时文件而不是 `PIPE`，父进程只读取文件尾部的有限字节，因此模型即使持续打印，也不会把全部输出保存在父进程内存中。超时时使用 `start_new_session=True` 创建的独立进程组，随后由 `killpg()` 一次终止整组子进程。

执行结果被统一转换为一条 tool observation：

```python
def format_tool_content(
    self,
    result: ExecResult,
) -> str:
    if result.timed_out:
        return (
            "Error: execution timed out after "
            f"{self.timeout:.0f} seconds."
        )
    if result.ok:
        return sanitize_tool_content(result.stdout)
    if result.stderr:
        return sanitize_tool_content(result.stderr)
    return (
        "Error: process exited with code "
        f"{result.returncode}."
    )
```

成功时返回 stdout，语法错误和运行时异常返回原始 stderr，超时返回固定错误文本。当前 `run_code()` 不会自动替模型补 `print()`，所以 system prompt 明确要求模型打印希望观察的值；没有打印内容时，成功 observation 就是空字符串。

这些措施主要用于控制意外的死循环、输出洪水和资源消耗。它们不能构成可信安全隔离。本地子进程仍可能读取运行账号可访问的文件、访问网络、读取继承的环境变量，或利用宿主环境中的漏洞。

因此，运行 ReTool 前必须遵守以下安全要求：

1. 不要在含有生产凭证、私钥或敏感数据的主机上直接执行模型代码；
2. 使用一次性容器、低权限虚拟机或专用沙箱服务；
3. 默认关闭网络，并设置只读文件系统与最小化可见目录；
4. 移除无关环境变量和云服务凭证；
5. 为 CPU、内存、进程数、磁盘和执行时间设置硬限制；
6. 保存代码、退出状态与资源指标，便于审计异常轨迹。

工具描述中的“independent execution”表示每次调用不共享 Python 状态，它不代表宿主机级安全隔离。教学试跑也应先放入隔离环境。

##### 8.4.6 多轮代码 rollout 怎样推进

`rollout.py` 分开保存可训练的 Assistant 动作、完整轨迹状态和“已经生成、尚未执行”的代码调用：

```python
@dataclass
class AssistantTurn:
    prompt_tokens: list[int]
    completion_tokens: list[int]
    logprobs: list[float]
    text: str


@dataclass
class Trajectory:
    example: MathExample
    group_index: int
    messages: list[dict[str, Any]]
    next_prompt_tokens: list[int] | None = None
    question_index: int = 0
    turns: list[AssistantTurn] = field(
        default_factory=list
    )
    code_calls: int = 0
    final_text: str = ""
    reward: float = -1.0
    advantage: float = 0.0
    valid_format: bool = False
    correct: bool = False
    done: bool = False


@dataclass(frozen=True)
class PendingExecution:
    trajectory: Trajectory
    code: str
    call_id: str
    messages_before_assistant: list[dict[str, Any]]
    assistant_text: str
    prompt_tokens: list[int]
    completion_tokens: list[int]
```

`begin_advance()` 消费一次 Assistant 输出，并决定轨迹是结束还是进入执行环境：

```python
def begin_advance(
    trajectory: Trajectory,
    prompt_tokens: list[int],
    sequence: Any,
    tokenizer: Any,
    config: RolloutConfig,
) -> PendingExecution | None:
    tokens, logprobs, text = read_sequence(
        sequence, tokenizer
    )
    text = text.strip()
    trajectory.turns.append(
        AssistantTurn(
            prompt_tokens,
            tokens,
            logprobs,
            text,
        )
    )
    parsed = parse_assistant(text)

    can_code = (
        parsed.kind == "tool"
        and trajectory.code_calls
        < config.max_code_calls
        and len(trajectory.turns)
        < config.max_assistant_turns
    )
    if not can_code:
        trajectory.messages.append(
            {"role": "assistant", "content": text}
        )
        trajectory.final_text = text
        trajectory.done = True
        return None

    call_id = (
        f"code-{trajectory.question_index}-"
        f"{trajectory.group_index}-"
        f"{trajectory.code_calls + 1}"
    )
    messages_before_assistant = list(
        trajectory.messages
    )
    trajectory.messages.append(
        {"role": "assistant", "content": text}
    )
    return PendingExecution(
        trajectory,
        parsed.code or "",
        call_id,
        messages_before_assistant,
        text,
        prompt_tokens,
        tokens,
    )
```

同一 round 内可能有许多轨迹同时请求执行代码。它们可以并发，但每条轨迹仍必须等待自己的 observation 返回以后才能开始下一轮生成：

```python
async def execute_pending_async(
    pendings: list[PendingExecution],
    sandbox: LocalPythonSandbox,
) -> list[ExecResult]:
    return list(
        await asyncio.gather(
            *(
                sandbox.arun_code(p.code)
                for p in pendings
            )
        )
    )


async def advance_round(
    responses: list[Any],
    requests: list[SampleRequest],
    trajectories: list[Trajectory],
    tokenizer: Any,
    sandbox: LocalPythonSandbox,
    config: RolloutConfig,
    progress_callback: Callable[[int], None] | None,
) -> None:
    pendings: list[PendingExecution] = []
    for request, response in zip(
        requests, responses, strict=True
    ):
        trajectory = trajectories[
            request.trajectory_index
        ]
        pending = begin_advance(
            trajectory,
            request.prompt_tokens,
            response.sequences[0],
            tokenizer,
            config,
        )
        if pending is not None:
            pendings.append(pending)
        elif (
            trajectory.done
            and progress_callback is not None
        ):
            progress_callback(1)

    if not pendings:
        return
    results = await execute_pending_async(
        pendings, sandbox
    )
    for pending, result in zip(
        pendings, results, strict=True
    ):
        finish_advance(
            pending,
            result,
            tokenizer,
            sandbox,
            config,
        )
        if (
            pending.trajectory.done
            and progress_callback is not None
        ):
            progress_callback(1)
```

`finish_advance()` 调用上一节的 `format_tool_content()`，再用 8.4.3 节的 `build_next_prompt()` 构造连续 token。如果执行结果过长，`fit_tool_content()` 会反复保留尾部，因为 traceback 和最终数值通常位于末尾；结果仍放不进轨迹预算时，本条轨迹直接结束。

首轮分支方式与 Search-R1 相同：每个问题只提交一个 prompt，并设置 `num_samples=group_size`。每条返回序列通过 `copy.deepcopy(root)` 变成独立轨迹。执行结果返回以后，各分支的 prompt 已经不同，后续请求全部设置 `num_samples=1`，直到输出最终答案或耗尽代码调用、轮次与 token 预算。

所有轨迹结束以后，状态机才依次调用 `score_trajectory()` 和 `assign_group_advantages()`。因此，一条轨迹的 traceback 可以影响它后续生成的代码，却不会越过轨迹边界影响同组其他分支。

##### 8.4.7 使用 PyTRIO 训练 ReTool

首先，使用当前权重创建采样客户端，并生成同题多轮轨迹：

```python
sampling_client = (
    training_client.save_weights_and_get_sampling_client()
)

trajectories = rollout_batch(
    sampling_client=sampling_client,
    tokenizer=tokenizer,
    sandbox=sandbox,
    examples=batch,
    config=rollout_config,
)
```

`rollout_batch()` 完成以下工作：

1. 第一轮对同一问题采样 `group_size` 个分支；
2. 解析每条分支中的 `code_interpreter` 调用；
3. 并发执行模型代码并追加 tool observation；
4. 对仍未结束的轨迹继续采样；
5. 抽取最终答案，计算 reward 与组内 advantage。

每个训练 step 都重新调用 `save_weights_and_get_sampling_client()`，保证 rollout old logprob 来自更新前的当前策略。如果同题所有轨迹都答对或都答错，中心化 advantage 全为 0，`build_training_datums()` 会跳过这一组；没有剩余 `Datum` 时，本 step 不执行 `optim_step()`。

随后，将每条完整轨迹构造为一个 `Datum`。ReTool 的 `build_datum()` 与 8.3.6 节遵循同一套前缀扩展规则，核心循环如下：

```python
for turn_index, turn in enumerate(trajectory.turns):
    if turn_index == 0:
        delta_observation = turn.prompt_tokens
    elif turn.prompt_tokens[
        :len(full_tokens)
    ] == full_tokens:
        delta_observation = turn.prompt_tokens[
            len(full_tokens):
        ]
    else:
        raise ValueError(
            "下一轮 prompt 不是已有轨迹的前缀扩展"
        )

    full_tokens.extend(delta_observation)
    full_tokens.extend(turn.completion_tokens)
    old_logprobs_by_token.extend(
        [0.0] * len(delta_observation)
    )
    old_logprobs_by_token.extend(turn.logprobs)
    advantages_by_token.extend(
        [0.0] * len(delta_observation)
    )
    advantages_by_token.extend(
        [trajectory.advantage]
        * len(turn.completion_tokens)
    )

input_tokens = full_tokens[:-1]
target_tokens = full_tokens[1:]
old_logprobs = old_logprobs_by_token[1:]
advantages = advantages_by_token[1:]

datum = trio.Datum(
    model_input=trio.ModelInput.from_ints(
        input_tokens
    ),
    loss_fn_inputs={
        "target_tokens": np.asarray(
            target_tokens, dtype=np.int64
        ),
        "logprobs": np.asarray(
            old_logprobs, dtype=np.float32
        ),
        "advantages": np.asarray(
            advantages, dtype=np.float32
        ),
    },
)
```

`delta_observation` 中包含初始题目、Assistant 结束符以及 stdout、stderr 或 timeout 文本，它们的 advantage 全为 0；Assistant 推理、代码调用与最终答案共享轨迹 advantage。这就是 interpreter feedback mask 的实际代码形态。

由于轨迹长度差异较大，代码再进行动态 micro-batch 装箱：

```python
datums = build_training_datums(trajectories)
micro_batches = pack_micro_batches(datums)

for micro_batch in micro_batches:
    weighted = weight_micro_batch_for_global_mean(
        micro_batch,
        total_samples=len(trajectories),
    )
    training_client.forward_backward(
        weighted,
        loss_fn="ppo",
        loss_fn_config=PPO_LOSS_CONFIG,
    ).result()

if micro_batches:
    training_client.optim_step(adam_params).result()
```

PyTRIO 会对单次 `forward_backward()` 中的样本取平均。不同 micro-batch 大小不一致时，直接累积会放大小批次的权重。本章按照每个 micro-batch 样本数占全局轨迹数的比例缩放 advantage：

$$\sum_k \frac{n_k}{N}\mathrm{mean}(\mathcal L_k) = \mathrm{mean}(\mathcal L_{\mathrm{global}}).$$

这样，动态拆批只改变执行方式，不改变全局样本平均的梯度含义。

##### 8.4.8 运行与评测 ReTool

配套目录包含以下文件：

| 文件 | 作用 |
| --- | --- |
| `prepare_data.py` | 准备 DAPO-Math-17k 训练集与 dev 集 |
| `data.py` | 加载统一数学样本 |
| `protocol.py` | 定义代码工具和多轮消息协议 |
| `sandbox.py` | 执行 Python 代码并记录资源指标 |
| `rollout.py` | 执行多轮“生成—运行—观察”状态机 |
| `reward.py` | 抽取 $\boxed{}$ 并做数学等价判定 |
| `train.py` | 构造 feedback mask、micro-batch 并执行 PPO |
| `eval.py` | 统一评测 text-only 与 ReTool 模式 |
| `analysis.py` | 汇总不同 checkpoint 的指标 |

`prepare_data.py` 生成的 DAPO-Math-17k `train.jsonl` 用于 RL，并另外切出 50 道 `dev.jsonl` 做快速检查。正式的 `eval.py` 使用固定 30 道 AIME 2025，避免直接在训练题上报告结果。

在 ReTool 模式下，每道题的 `val_n` 条候选仍由同一个多轮状态机生成：

```python
config = RolloutConfig(
    group_size=args.val_n,
    max_code_calls=args.max_code_calls,
    max_assistant_turns=args.max_assistant_turns,
    max_trajectory_tokens=(
        args.max_trajectory_tokens
    ),
    max_assistant_tokens=args.max_assistant_tokens,
    max_tool_response_tokens=(
        args.max_tool_response_tokens
    ),
    temperature=args.temperature,
    top_p=args.top_p,
    seed=args.seed,
)

trajectories = await rollout_batch_async(
    sampling_client,
    tokenizer,
    sandbox,
    examples,
    config,
)
```

`text-only` 模式则不注册代码工具，直接对同一题采样 `val_n` 个单轮答案。两种模式最终都写出逐题 JSONL，并汇总：

- `Average@N`：全部生成结果中的平均正确率；
- `Pass@N`：至少有一条候选答对的问题比例；
- `format_rate`：能够抽取合法 `\boxed{}` 的比例；
- `mean_code_calls` 与 `mean_turns`：工具成本和轨迹长度。

因此，比较 checkpoint 时至少需要固定题集、`val_n`、temperature、top-p、最大轨迹长度和答案抽取逻辑；比较 text-only 与 ReTool 时，还要额外报告执行延迟和代码调用数。

首先准备数据：

```bash
python docs/chapter8/retool/prepare_data.py
```

确认代码执行器位于隔离环境后，再进行一步试跑：

```bash
python docs/chapter8/retool/train.py \
    --max-steps 1 \
    --questions-per-batch 1 \
    --group-size 4 \
    --max-code-calls 2 \
    --sandbox-workers 2 \
    --swanlab-mode disabled
```

准备好 AIME 2025 本地数据后，可以先跑无工具对照，再跑相同采样参数的 ReTool 评测：

```bash
python docs/chapter8/retool/eval.py \
    --mode text-only \
    --val-n 12 \
    --temperature 1.0 \
    --top-p 0.7 \
    --output docs/chapter8/retool/eval-results/aime25-text-only-base.jsonl

python docs/chapter8/retool/eval.py \
    --mode retool \
    --val-n 12 \
    --temperature 1.0 \
    --top-p 0.7 \
    --output docs/chapter8/retool/eval-results/aime25-retool-base.jsonl
```

评测训练后的模型时，为两条命令增加相同的 `--model-path trio://...`。只有 Base Model、checkpoint、text-only 和 ReTool 使用同一套采样设置时，差异才可以归因于训练或工具环境。

训练指标应同时覆盖任务、策略和环境三个层面：

- **任务结果**：正确率、合法 $\boxed{}$ 比例、退化组比例；
- **工具行为**：代码调用率、每条轨迹平均调用次数、零调用正确率；
- **自我修正**：首次执行报错后重试并最终答对的比例；
- **环境状态**：执行成功率、异常率、超时率、平均 latency；
- **策略稳定性**：PPO probability ratio、clip fraction、response length；
- **系统效率**：rollout、执行器、远端训练和 checkpoint 各阶段耗时。

评测时可以分别运行 text-only 与 ReTool 模式。两者需要使用同一批问题、相同采样参数和相同答案判定器，才能看出工具环境带来的净收益。工具模式还应报告额外延迟与执行成本，因为准确率提升通常伴随更多环境调用。

至此，我们已经从 GRPO 的单轮结果奖励、OPD 的逐 token Teacher 反馈，走到了 Search-R1 与 ReTool 的多轮环境交互。下面的本章小结会把四个模块重新收束到同一条“rollout—反馈—advantage—策略更新”数据流中。

#### 本章小结

本章从 GRPO 出发，逐步建立了一条可以扩展到 Agent 的大模型强化学习路径。

GRPO 使用同题多次采样构造组内相对优势，省去了单独训练 Value Model 的过程。它把算法拆成清晰的三层：策略生成 rollout，环境给出 reward，更新 loss 根据新旧策略概率比优化模型。正确的 reward、token 对齐和 on-policy sampler 刷新共同决定训练是否有效。

OPD 保留 on-policy rollout，将规则奖励替换为 Teacher 对 Student 轨迹的逐 token 概率反馈。reverse KL 为每个动作提供稠密信号，使小模型可以在自身会访问的状态上学习 Teacher 能力。Teacher 与 Student 的 tokenizer、推理模式和能力互补关系需要在训练前验证。

Search-R1 与 ReTool 进一步把轨迹扩展为多轮环境交互。搜索结果和代码执行结果进入上下文，却通过 observation mask 排除在策略 loss 之外；模型生成的搜索词、代码、推理和最终答案共享轨迹级结果信号。两者都复用了 GRPO 的分组采样与相对优势，只替换了工具协议、环境实现和 reward。

四个示例最终汇合为同一条 PyTRIO 数据流：

$$\text{当前策略}\rightarrow\text{多样化 rollout}\rightarrow\text{环境或 Teacher 反馈}\rightarrow\text{token-level advantage}\rightarrow\text{策略更新}\rightarrow\text{新策略}.$$

掌握这条数据流后，新的 Agentic RL 任务可以从五个问题开始设计：

1. Agent 可以执行哪些动作，环境会返回什么 observation？
2. 一条轨迹在什么条件下结束，预算如何限制？
3. reward 能否稳定反映最终任务目标？
4. 哪些 token 属于策略动作，哪些 token 必须被 mask？
5. rollout、旧 logprob、advantage 与当前权重是否严格对齐？

当这五个问题都有可验证的答案时，一个工具 Demo 才具备进入强化学习训练的基础。

> **继续学习：** 受篇幅和章节定位限制，本章集中介绍了 GRPO、OPD、Search-R1 与 ReTool，仍有许多 Agentic RL 方法和交互环境无法逐一展开。如果你希望继续学习 OPSD、DAPO、GSPO、ALFWorld 等内容，可以前往作者持续维护的 [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab)。仓库将继续整理相关算法的原理、可运行代码与真实训练过程。

#### 参考资料

1. Shao, Z. et al. [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300). 2024.
2. Schulman, J. et al. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347). 2017.
3. Agarwal, R. et al. [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649). 2023.
4. Li, Y. et al. [Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](https://arxiv.org/abs/2604.13016). 2026.
5. Sun, J. et al. [EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models](https://arxiv.org/abs/2607.11012). 2026.
6. Jin, B. et al. [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516). 2025.
7. Feng, J. et al. [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536). 2025.
8. PyTRIO. [Loss Function Guide](https://docs.pytrio.com/docs/guide/loss_fn).
9. PyTRIO. [Search-R1 Example](https://docs.pytrio.com/docs/example/search-r1).
10. Agentic-RL Lab (不要葱姜蒜). [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab).

### GRPO

> **代码来源：** 本目录代码引用并整理自本章作者维护的 [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab) 中的 [01-grpo](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/01-grpo) 实现，当前版本适配 Happy-LLM 第八章与 PyTRIO 0.2.6。

本目录对应正文 8.1 节，以 GSM8K 为例实现完整的 PyTRIO GRPO 训练链路。同步版与异步版使用相同的 prompt、规则奖励、组内相对优势、Datum 对齐和 loss。

#### 文件说明

| 文件 | 作用 | 正文定位 |
| --- | --- | --- |
| `01-demo-sync.py` | 按 prompt 顺序完成 rollout 和训练 | 逐段讲解 |
| `02-demo-async.py` | 使用 `asyncio.gather()` 并发执行 batch 内 rollout | 提供完整代码，只说明接口差异 |

#### 运行前准备

从 Happy-LLM 仓库根目录创建 Python 3.13 环境并安装第八章公共依赖：

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r docs/chapter8/requirements.txt
trio login
```

需要在线记录实验时，再执行 `swanlab login`。

#### 运行同步版

```bash
python docs/chapter8/grpo/01-demo-sync.py \
    --steps 1 \
    --batch-size 1 \
    --group-size 4 \
    --max-tokens 512 \
    --loss-fn importance_sampling \
    --swanlab-mode disabled
```

训练第一次启动时会下载 GSM8K。正式实验应增大 `steps`、`batch-size` 和 `group-size`，并固定其余配置后再比较 `importance_sampling` 与 `ppo`。

#### 运行异步版

```bash
python docs/chapter8/grpo/02-demo-async.py \
    --steps 1 \
    --batch-size 4 \
    --group-size 4 \
    --max-tokens 512 \
    --loss-fn importance_sampling \
    --swanlab-mode disabled
```

异步版会并发处理同一 batch 中不同 prompt 的 rollout。reward、advantage、Datum 和 loss 与同步版保持一致。

#### 同步版代码阅读顺序

1. `parse_args()` 与 `RolloutSample`：定义训练配置和一条 rollout 的数据。
2. `grade_answer()`：抽取 `\boxed{}` 并计算规则奖励。
3. `run_rollout_group()`：对同一道题采样一组回答并计算相对优势。
4. `build_grpo_datum()`：完成自回归右移和 prompt mask。
5. `main()`：选择内置 loss，并串联 sampler 刷新、rollout、策略更新、日志和权重保存。

异步版在对应函数中使用 `sample_async()`、`forward_backward_async()`、`optim_step_async()` 和 `asyncio.gather()`。

### OPD

> **代码来源：** 本目录代码引用并整理自本章作者维护的 [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab) 中的 [02-opd](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/02-opd) 实现，当前版本适配 Happy-LLM 第八章与 PyTRIO 0.2.6。

本目录对应正文 8.2 节，以 DeepMath-103K prompt 为例实现完整的 On-Policy Distillation。Student 生成回答，Teacher 对同一条 Student 轨迹计算逐 token logprob，再由 reverse KL 构造训练信号。

#### 文件说明

| 文件 | 作用 | 正文定位 |
| --- | --- | --- |
| `01-demo-sync.py` | 顺序执行 Student rollout、Teacher 打分和 Student 更新 | 逐段讲解 |
| `02-demo-async.py` | 并发执行 batch 内 rollout 与 Teacher logprob 请求 | 提供完整代码，只说明接口差异 |

#### 运行前准备

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r docs/chapter8/requirements.txt
trio login
```

需要在线记录实验时，再执行 `swanlab login`。

#### 运行同步版

```bash
python docs/chapter8/opd/01-demo-sync.py \
    --steps 1 \
    --batch-size 1 \
    --group-size 1 \
    --max-tokens 512 \
    --sample-size 20 \
    --num-shards 1 \
    --swanlab-mode disabled
```

脚本会从 ModelScope 下载 DeepMath-103K parquet。`--num-shards 1` 适合小成本试跑，`--num-shards 10` 会使用全部分片。

#### 运行异步版

```bash
python docs/chapter8/opd/02-demo-async.py \
    --steps 1 \
    --batch-size 4 \
    --group-size 2 \
    --max-tokens 512 \
    --sample-size 20 \
    --num-shards 1 \
    --swanlab-mode disabled
```

异步版在 batch 内并发执行 Student rollout，并在同一 prompt 内并发提交 Teacher logprob 请求。token 对齐、reverse KL 与 `importance_sampling` Datum 保持不变。

#### 同步版代码阅读顺序

1. `parse_args()` 与 `load_deepmath()`：准备训练参数和 prompt-only 数据。
2. `build_prompt()`：把问题渲染成 Student 输入。
3. `completion_teacher_logprobs()`：让 Teacher 对 Student completion 打分。
4. `build_opd_datum()`：把逐 token reverse KL 写入 advantage。
5. `main()`：刷新 Student sampler，更新 Student，记录指标并保存权重。

Teacher 默认使用 `Qwen/Qwen3.6-27B`。实际可用模型以 PyTRIO 服务返回结果为准，也可以通过 `--teacher-base-model` 或 `--teacher-model-path` 指定其他 Teacher。Teacher 与 Student 的 token id 必须兼容。

### Search-R1

> **代码来源：** 本目录代码引用并整理自本章作者维护的 [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab) 中的 [03-search-r1](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/03-search-r1) 实现，当前版本适配 Happy-LLM 第八章与 PyTRIO 0.2.6。

本目录对应正文 8.3 节。代码保留数据、工具协议、搜索环境、多轮 rollout、reward、训练和评测的边界，便于观察 Agentic RL 如何在普通 GRPO 训练循环上增加环境交互。

#### 运行前准备

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r docs/chapter8/requirements.txt
trio login
```

需要在线记录实验时，再执行 `swanlab login`。

#### 准备数据

```bash
python docs/chapter8/search-r1/prepare_data.py
```

该命令会准备 NQ 与 HotpotQA 训练、开发和测试数据。Wikipedia 后端免费且不需要 API Key，适合先验证流程。

#### 最小试跑

```bash
python docs/chapter8/search-r1/train.py \
    --max-steps 1 \
    --questions-per-batch 1 \
    --group-size 4 \
    --max-search-calls 2 \
    --search-backend wikipedia \
    --search-concurrency 3 \
    --swanlab-mode disabled
```

在线搜索结果会随时间变化。比较 Base Model 与 checkpoint 时，必须保持题集、搜索后端、最大搜索次数和 sampling 参数一致。

#### 文件说明

| 文件 | 作用 |
| --- | --- |
| `protocol.py` | 定义工具协议，解析搜索动作和最终答案 |
| `search.py` | 封装 DeepSeek Search、Wikipedia 和知乎搜索后端 |
| `rollout.py` | 执行多轮“生成—搜索—观察—继续生成”状态机 |
| `reward.py` | 计算格式奖励和答案精确匹配奖励 |
| `train.py` | 构造 observation mask、PyTRIO Datum 并更新策略 |
| `eval.py` | 使用相同环境评测 Base Model 或 checkpoint |
| `analyse.py` | 汇总评测结果 |

### ReTool

> **代码来源：** 本目录代码引用并整理自本章作者维护的 [agentic-rl-lab](https://github.com/KMnO4-zx/agentic-rl-lab) 中的 [05-retool](https://github.com/KMnO4-zx/agentic-rl-lab/tree/main/05-retool) 实现，当前版本适配 Happy-LLM 第八章与 PyTRIO 0.2.6。

本目录对应正文 8.4 节。代码实现数学题上的多轮代码解释器 rollout、结果奖励、observation mask、PPO 更新和统一评测。

> 安全提示：`sandbox.py` 通过独立 subprocess、超时和资源限制控制意外消耗，但不能提供可信安全隔离。模型生成的代码仍可能访问本机文件、网络和继承的环境变量。处理不可信代码时，请使用一次性容器、低权限虚拟机或专用沙箱服务，并移除所有凭证。

#### 运行前准备

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r docs/chapter8/requirements.txt
trio login
```

需要在线记录实验时，再执行 `swanlab login`。

#### 准备数据

```bash
python docs/chapter8/retool/prepare_data.py
```

#### 最小试跑

请先在隔离环境中确认执行器权限，再运行：

```bash
python docs/chapter8/retool/train.py \
    --max-steps 1 \
    --questions-per-batch 1 \
    --group-size 4 \
    --max-code-calls 2 \
    --sandbox-workers 2 \
    --swanlab-mode disabled
```

#### 文件说明

| 文件 | 作用 |
| --- | --- |
| `protocol.py` | 定义 `code_interpreter` 工具和消息拼接规则 |
| `sandbox.py` | 执行 Python 代码并限制时间、进程和输出大小 |
| `rollout.py` | 执行多轮“生成—运行代码—观察—继续生成”状态机 |
| `reward.py` | 抽取最后一个 `\boxed{}` 并判断数学等价性 |
| `train.py` | 构造 observation mask、PyTRIO Datum 并执行 PPO 更新 |
| `eval.py` | 统一评测 text-only 与 ReTool 模式 |
| `analysis.py` | 汇总不同 checkpoint 的指标 |

## 扩展章节

### 扩展章节说明

  <h2>🚀 Happy-LLM 扩展内容</h2>
*社区驱动的大语言模型学习资源*


---

#### 📖 为什么会有 Extra Chapter？

&emsp;&emsp;在 Happy-LLM 主教程的基础上，我们发现社区中有许多优秀的学习者和实践者，他们在学习和使用大语言模型的过程中积累了宝贵的经验、独到的见解和实用的技巧。这些内容虽然不属于主教程的核心知识体系，但对于深入理解和应用大语言模型具有重要价值。

**Extra Chapter 的设立目的：**

- 🌟 **汇聚智慧**：收集社区成员的优秀学习笔记、实践经验和技术博客
- 🔄 **持续更新**：保持内容的时效性，跟上大语言模型领域的快速发展
- 🤝 **促进交流**：为社区成员提供分享和交流的平台
- 📚 **补充完善**：对主教程内容进行有益的补充和扩展
- 💡 **启发思考**：通过不同视角和实践案例，启发读者的深度思考

**Extra Chapter 包含的内容类型：**

- 📝 **学习笔记**：深度学习心得和知识总结
- 🛠️ **实践案例**：真实项目中的应用经验
- 🔬 **技术探索**：前沿技术的研究和实验
- 💭 **思考感悟**：对大语言模型发展的独特见解
- 🎯 **专题研究**：特定领域或问题的深入分析

---

#### 📋 PR 贡献规范

&emsp;&emsp;我们热烈欢迎社区成员为 Extra Chapter 贡献优质内容！为了保证内容质量和项目的整体性，请遵循以下规范：

##### 🗂️ 目录结构规范

每个贡献的内容应按照以下目录结构组织：

```
Extra-Chapter/
├── your-topic-name/                    # 你的主题文件夹
│   ├── readme.md                       # 主要内容文件（必需）
│   ├── images/                         # 图片资源文件夹（可选）
│   │   ├── figure1.png
│   │   └── figure2.jpg
│   ├── code/                           # 代码文件夹（可选）
│   │   ├── example.py
│   │   └── requirements.txt
│   ├── data/                           # 数据文件夹（可选）
│   │   └── sample_data.json
│   └── notebook.ipynb                  # Jupyter Notebook（如涉及代码必选）
└── Readme.md                           # 本文件
```

##### 📝 文件命名规范

1. **主题文件夹命名**：
   - 使用小写字母和连字符
   - 名称要简洁明了，能够概括主题内容
   - 例如：`why-fine-tune-small-large-language-models`、`rag-optimization-techniques`

2. **主要内容文件**：
   - 必须命名为 `readme.md`
   - 使用 Markdown 格式编写

3. **图片文件**：
   - 统一放在 `images/` 文件夹下
   - 使用描述性的文件名
   - 支持格式：`.png`、`.jpg`、`.jpeg`、`.gif`、`.svg`

4. **代码文件**：
   - 如涉及代码，请尽量提供可直接运行的 Jupyter Notebook 文件
   - 统一放在 `code/` 文件夹下
   - 使用标准的文件扩展名
   - 如有依赖，请提供 `requirements.txt`
   - 如有 Jupyter Notebook 文件，请放在主文件夹下

##### ✍️ 内容质量要求

1. **原创性**：
   - 内容必须是原创或经过授权的
   - 如引用他人内容，请注明出处

2. **技术准确性**：
   - 确保技术内容的准确性
   - 代码示例应能正常运行
   - 提供必要的环境说明

3. **结构清晰**：
   - 使用清晰的标题层次
   - 合理使用列表、表格等格式
   - 重要内容使用适当的强调

4. **语言规范**：
   - 使用规范的中文表达
   - 技术术语使用准确
   - 避免错别字和语法错误

##### PR commit messgae 内容

请在 PR commit message 中 包含以下内容：

- 新增的主题文件夹名称
- 贡献内容的概述
- 贡献内容的详细描述
- 你的 Github 个人主页链接，及你的个人介绍
- 个人 title 及工作经历 or 学校 or 研究方向

如以下所示：

```
Extra Chapter: 你的主题名称

详细描述你的贡献内容，包括新增的主题文件夹、文件内容和目录结构。

- 新增的主题文件夹名称：your-topic-name
- 贡献内容的概述：详细介绍你的贡献内容
- 贡献内容的详细描述：详细描述你的贡献内容，包括新增的主题文件夹、文件内容和目录结构。
- 你的 Github 个人主页链接及个人介绍：[你的个人主页链接](https://example.com)，介绍你的研究方向、技术专长等。
- 个人 title 及工作经历 or 学校 or 研究方向：内容贡献者-xxxx学校，研究方向为自然语言处理。
```

### 微调小模型的意义

大家在日常使用Deepseek-R1或者是阿里新发布的Qwen3模型，他们的模型都是能力很强，所提供的API服也都可以满足大家的日常或者是公司开发所需。但大家也可以想一个简单的问题几个简单的问题，如下：

1. 公司的数据是够敏感，是否需要保密？
1. 日常使用大模型的任务是否很困难，对推理链是否刚需？
1. 任务调用的大模型API并发量是多少？每日资金消耗有多少？

对于问题1，如果公司数据敏感，那我建议不要调用供应商提供的大模型API。就算供应商保证不会拿你们数据做训练，但你们的数据还是泄漏了（会有不必要的风险），建议本地部署大模型。

对于问题2，如果使用大模型的场景问题很困难并且刚需推理链，那可以使用供应商的API，这样可以保证推理链的上下文不会爆显存。如果问题很简单，没有刚需推理链，那建议本地部署小模型即可。

对于问题3，如果任务很简单，且调用的大模型API并发量很高，那我建议微调一个特定任务的小模型，本地部署。这样可以满足高并发，并且可以减少资金消耗。（本地部署，默认硬件环境单卡4090）

看到这里，想必大家已经思考完了以上三个问题，心中有了答案。那我给出一个小小的案例。

#### 微调模型的需求性

假如你的公司有一个从投诉的文本中抽取用户信息的任务。比如，你需要从以下文本中抽取用户姓名、住址、邮箱、投诉的问题等等。

> 这只是一个小小的案例，数据也是我用大模型批量制造的。真正的投诉数据不会这么“干净、整洁”。

INPUT：
```text
龙琳，宁夏回族自治区璐市城东林街g座 955491，邮箱 nafan@example.com。小区垃圾堆积成山，晚上噪音扰人清梦，停车难上加难，简直无法忍受！
```

OUTPUT：
```json
{
    "name": "龙琳",
    "address": "宁夏回族自治区璐市城东林街g座 955491",
    "email": "nafan@example.com",
    "question": "小区垃圾堆积成山，晚上噪音扰人清梦，停车难上加难，简直无法忍受！"
}
```


那你当然可以调用 Deepseek最强大的模型R1，也可以调用阿里最新发布最强大的模型 Qwen3-235B-A22B等等，这些模型的信息抽取效果也很非常的棒。

但有个问题，如果你有几百万条这样的数据要处理，全部调用最新的，最好的大模型可能需要消耗几万块钱。并且，如果这些投诉数据，比如电信投诉数据，电网投诉数据，这些数据是敏感的不可以直接放到外网的。

所以，综合数据敏感，和资金消耗。最好的选择就是微调一个小模型（如Qwen3-0.6B），既可以保证高并发，可以保证数据不泄漏，保证模型抽取的效果，还可以省钱！！！

那下面，用一个小案例带大家实操一下，微调Qwen3-0.6B小模型完成文本信息抽取任务。



#### 配置环境 下载数据

> Colab 文件地址：https://colab.research.google.com/drive/18ByY11KVhIy6zWx1uKUjSzqeHTme-TtU?usp=drive_link

```python
!pip install datasets swanlab -q
```

```python
!wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1a0sf5C209CLW5824TJkUM4olMy0zZWpg' -O fake_sft.json
```

#### 处理数据

```python
from datasets import Dataset
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, DataCollatorForSeq2Seq, TrainingArguments, Trainer, GenerationConfig
from peft import LoraConfig, TaskType, get_peft_model
import torch
```

```python
# 将JSON文件转换为CSV文件
df = pd.read_json('fake_sft.json')
ds = Dataset.from_pandas(df)
ds[:3]
```

```python
model_id = "Qwen/Qwen3-0.6B"
```

```python
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=False)
tokenizer
```

对大语言模型进行 `supervised-finetuning`（`sft`，有监督微调）的数据格式如下：

```json
{
  "instruction": "回答以下用户问题，仅输出答案。",
  "input": "1+1等于几?",
  "output": "2"
}
```

其中，`instruction` 是用户指令，告知模型其需要完成的任务；`input` 是用户输入，是完成用户指令所必须的输入内容；`output` 是模型应该给出的输出。

有监督微调的目标是让模型具备理解并遵循用户指令的能力。因此，在构建数据集时，我们应针对我们的目标任务，针对性构建数据。比如，如果我们的目标是通过大量人物的对话数据微调得到一个能够 role-play 甄嬛对话风格的模型，因此在该场景下的数据示例如下：

```json
{
  "instruction": "你父亲是谁？",
  "input": "",
  "output": "家父是大理寺少卿甄远道。"
}
```

`Qwen3` 采用的 `Chat Template`格式如下：

由于 `Qwen3` 是混合推理模型，因此可以手动选择开启思考模式

不开启 `thinking mode`


```python
messages = [
    {"role": "system", "content": "You are a helpful AI"},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "I'm fine, think you. and you?"},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)
print(text)
```
```
<|im_start|>system
You are a helpful AI<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
<think>

</think>

I'm fine, think you. and you?<|im_end|>
<|im_start|>assistant
<think>

</think>
```


`LoRA`（`Low-Rank Adaptation`）训练的数据是需要经过格式化、编码之后再输入给模型进行训练的，我们需要先将输入文本编码为 `input_ids`，将输出文本编码为 `labels`，编码之后的结果是向量。我们首先定义一个预处理函数，这个函数用于对每一个样本，同时编码其输入、输出文本并返回一个编码后的字典：


```python
def process_func(example):
    MAX_LENGTH = 1024 # 设置最大序列长度为1024个token
    input_ids, attention_mask, labels = [], [], [] # 初始化返回值
    # 适配chat_template
    instruction = tokenizer(
        f"<s><|im_start|>system\n{example['system']}<|im_end|>\n"
        f"<|im_start|>user\n{example['instruction'] + example['input']}<|im_end|>\n"
        f"<|im_start|>assistant\n<think>\n\n</think>\n\n",
        add_special_tokens=False
    )
    response = tokenizer(f"{example['output']}", add_special_tokens=False)
    # 将instructio部分和response部分的input_ids拼接，并在末尾添加eos token作为标记结束的token
    input_ids = instruction["input_ids"] + response["input_ids"] + [tokenizer.pad_token_id]
    # 注意力掩码，表示模型需要关注的位置
    attention_mask = instruction["attention_mask"] + response["attention_mask"] + [1]
    # 对于instruction，使用-100表示这些位置不计算loss（即模型不需要预测这部分）
    labels = [-100] * len(instruction["input_ids"]) + response["input_ids"] + [tokenizer.pad_token_id]
    if len(input_ids) > MAX_LENGTH:  # 超出最大序列长度截断
        input_ids = input_ids[:MAX_LENGTH]
        attention_mask = attention_mask[:MAX_LENGTH]
        labels = labels[:MAX_LENGTH]
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }

```


```python
tokenized_id = ds.map(process_func, remove_columns=ds.column_names)
tokenized_id
```


```python
tokenizer.decode(tokenized_id[0]['input_ids'])
```

```python
tokenizer.decode(list(filter(lambda x: x != -100, tokenized_id[1]["labels"])))
```

#### 加载模型

加载模型并配置LoraConfig

```python
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto",torch_dtype=torch.bfloat16)
model
```


```
Qwen3ForCausalLM(
  (model): Qwen3Model(
    (embed_tokens): Embedding(151936, 1024)
    (layers): ModuleList(
      (0-27): 28 x Qwen3DecoderLayer(
        (self_attn): Qwen3Attention(
          (q_proj): Linear(in_features=1024, out_features=2048, bias=False)
          (k_proj): Linear(in_features=1024, out_features=1024, bias=False)
          (v_proj): Linear(in_features=1024, out_features=1024, bias=False)
          (o_proj): Linear(in_features=2048, out_features=1024, bias=False)
          (q_norm): Qwen3RMSNorm((128,), eps=1e-06)
          (k_norm): Qwen3RMSNorm((128,), eps=1e-06)
        )
        (mlp): Qwen3MLP(
          (gate_proj): Linear(in_features=1024, out_features=3072, bias=False)
          (up_proj): Linear(in_features=1024, out_features=3072, bias=False)
          (down_proj): Linear(in_features=3072, out_features=1024, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): Qwen3RMSNorm((1024,), eps=1e-06)
        (post_attention_layernorm): Qwen3RMSNorm((1024,), eps=1e-06)
      )
    )
    (norm): Qwen3RMSNorm((1024,), eps=1e-06)
    (rotary_emb): Qwen3RotaryEmbedding()
  )
  (lm_head): Linear(in_features=1024, out_features=151936, bias=False)
)
```

```python
model.enable_input_require_grads() # 开启梯度检查点时，要执行该方法
```


#### Lora Config

`LoraConfig`这个类中可以设置很多参数，比较重要的如下

- `task_type`：模型类型，现在绝大部分 `decoder_only` 的模型都是因果语言模型 `CAUSAL_LM`
- `target_modules`：需要训练的模型层的名字，主要就是 `attention`部分的层，不同的模型对应的层的名字不同
- `r`：`LoRA` 的秩，决定了低秩矩阵的维度，较小的 `r` 意味着更少的参数
- `lora_alpha`：缩放参数，与 `r` 一起决定了 `LoRA` 更新的强度。实际缩放比例为`lora_alpha/r`，在当前示例中是 `32 / 8 = 4` 倍
- `lora_dropout`：应用于 `LoRA` 层的 `dropout rate`，用于防止过拟合


```python
from peft import LoraConfig, TaskType, get_peft_model

config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    inference_mode=False, # 训练模式
    r=8, # Lora 秩
    lora_alpha=32, # Lora alaph，具体作用参见 Lora 原理
    lora_dropout=0.1# Dropout 比例
)
config
```


```python
model = get_peft_model(model, config)
config
```


```python
model.print_trainable_parameters()  # 模型参数训练量只有0.8395%
```

> trainable params: 5,046,272 || all params: 601,096,192 || trainable%: 0.8395


#### Training Arguments

- `output_dir`：模型的输出路径
- `per_device_train_batch_size`：每张卡上的 `batch_size`
- `gradient_accumulation_steps`: 梯度累计
- `num_train_epochs`：顾名思义 `epoch`


```python
args = TrainingArguments(
    output_dir="Qwen3_instruct_lora",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    logging_steps=1,
    num_train_epochs=3,
    save_steps=50,
    learning_rate=1e-4,
    save_on_each_node=True,
    gradient_checkpointing=True,
    report_to="none",
)
```

#### SwanLab 简介

[SwanLab](https://github.com/swanhubx/swanlab) 是一个开源的模型训练记录工具，面向 AI 研究者，提供了训练可视化、自动日志记录、超参数记录、实验对比、多人协同等功能。在 `SwanLab` 上，研究者能基于直观的可视化图表发现训练问题，对比多个实验找到研究灵感，并通过在线链接的分享与基于组织的多人协同训练，打破团队沟通的壁垒。

**为什么要记录训练**

相较于软件开发，模型训练更像一个实验科学。一个品质优秀的模型背后，往往是成千上万次实验。研究者需要不断尝试、记录、对比，积累经验，才能找到最佳的模型结构、超参数与数据配比。在这之中，如何高效进行记录与对比，对于研究效率的提升至关重要。

`(2) Use an existing SwanLab account` 并使用 private API Key 登录

```python
import swanlab
from swanlab.integration.transformers import SwanLabCallback

# 实例化SwanLabCallback
swanlab_callback = SwanLabCallback(
    project="Qwen3-Lora",  # 注意修改
    experiment_name="Qwen3-8B-LoRA-experiment"  # 注意修改
)
```


```python
import swanlab
from swanlab.integration.transformers import SwanLabCallback

# 实例化SwanLabCallback
swanlab_callback = SwanLabCallback(
    project="Qwen3-Lora",
    experiment_name="Qwen3-0.6B-extarct-lora-2"
)
```


```python
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_id,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True),
    callbacks=[swanlab_callback]
)
```


```python
trainer.train()
```


#### 测试文本


```python
prompt = "龙琳   ，宁夏回族自治区璐市城东林街g座 955491，nafan@example.com。小区垃圾堆积成山，晚上噪音扰人清梦，停车难上加难，简直无法忍受！太插件了阿萨德看见啊啥的健康仨都会撒娇看到撒谎的、"

messages = [
    {"role": "system", "content": "将文本中的name、address、email、question提取出来，以json格式输出，字段为name、address、email、question，值为文本中提取出来的内容。"},
    {"role": "user", "content": prompt}
]

inputs = tokenizer.apply_chat_template(messages,
                                       add_generation_prompt=True,
                                       tokenize=True,
                                       return_tensors="pt",
                                       return_dict=True,
                                       enable_thinking=False).to('cuda')

gen_kwargs = {"max_length": 2500, "do_sample": True, "top_k": 1}
with torch.no_grad():
    outputs = model.generate(**inputs, **gen_kwargs)
    outputs = outputs[:, inputs['input_ids'].shape[1]:]
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```


```json
{
    "name": "龙琳",
    "address": "宁夏回族自治区璐市城东林街g座 955491",
    "email": "nafan@example.com",
    "question": "小区垃圾堆积成山，晚上噪音扰人清梦，停车难上加难，简直无法忍受！太插件了阿萨德看见啊啥的健康仨都会撒娇看到撒谎的、"
}
```

### Transformer 整体模块设计解读

当本节内容作为第二章 Transformer架构中2.2章节Encoder-Decoder的补充，结合Pytorch的API源码，从Transformer的整体设计上来解释Transformer的各个模块。

#### 从经典架构开始：Encoder-Decoder结构
让我们先从经典架构图理解Transformer的整体设计思路。Transformer分为两个主要部分：左侧的编码器（Encoder）和右侧的解码器（Decoder）。那么这两块结构的输入和输出分别是什么？


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-1.png)
1.jpg


Encoder的职责是接受完整的源序列输入，将其转换为一个富含语义信息的表示序列。想象一下，如果我们要做机器翻译，Encoder就像是一个深度理解原文的专家，它需要充分理解整个句子的含义、语法结构和上下文关系。

Decoder则承担着更复杂的任务：它需要接受目标序列和编码器输出的表示序列，然后输出词汇/字符的概率分布。这就像是一个翻译专家，既要理解原文的含义（通过Encoder的输出），又要根据已经翻译的部分来决定下一个词应该是什么。

#### Positional Encoding：位置编码设计

但这里有一个关键问题需要解决：Transformer本身对位置信息不敏感。比如"我爱你"和"你爱我"这两个句子，在没有位置信息的情况下，模型无法感知到这是语义完全不同的句子。这就像是一个人失去了对词语顺序的感知能力，显然无法正确理解语言。

因此，我们需要一个带有位置信息的向量，将其添加到每个input embedding上，来对不同位置得到不同的表征。这个模块就是图中的**Positional Encoding**。

##### 位置编码的设计原则

在设计编码模块时，有**三个重要的前提假设**，这些假设直接影响了最终的实现方案：

**1. 确定性原则**：每个位置的编码应该是确定的数字，不同序列中相同位置的编码应该相同。

为什么这个原则如此重要？让我们考虑一个反例：如果用等分的设计方法，将一个序列从0~1之间做均匀划分，那么序列长度不一样时，每个位置上的编码也就不一样。当序列长度为5时，位置编码可能是0、0.2、0.4、0.6、0.8，但如果序列长度为10，就变成了0、0.1、0.2...。同样对于第二个位置上的字符，在第一个序列中是0.2，在第二个序列中又是0.1，这样的编码就失去了确定性。

**2. 相对关系一致性**：不同句子中，对于任意两个位置之间的相对距离，相对关系应该保持一致。

这个目的是为了学习通用的语言关系，比如："修饰词在被修饰词前1个位置"是通用模式。以下面的长短句举例：

```markdown
- 长句子（10个词）
  位置: 0  1  2  3  4  5  6  7  8  9
  词汇: I  am learning about transformers today in class now

- 短句子（6个词）
  位置: 0  1  2  3  4  5
  词汇: I  like deep learning models
```

在长句子中，位置1和位置4之间的编码关系，应该与短句子中位置2和位置5之间的编码关系完全相同，因为模型需要学会的是通用的相对位置关系。

**3. 泛化能力**：位置序列应该能推广到没见过的更长序列。

第三个假设希望位置编码可以推广到更长的测试句子。假如训练集中序列长度都是10以内的，但测试集中可能会有长度为15的句子，我们希望即使测试集中句子长度更长，在训练中没有见过，我们也能通过这样的position encoding推广过去。

##### 三角函数编码

基于这些假设，Transformer采用了sin和cos的组合来表征绝对位置信息：

```markdown
- 向量维度为偶数：PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
- 向量维度为奇数：PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

通过sin和cos的组合来表征绝对位置的好处是：`pe(pos+k)`可以写成`pe(k)`的线性组合（利用三角函数公式`sin(A + B) = sin(A)cos(B) + cos(A)sin(B)`）。这样做的意义是：即使测试集中出现了pos+k这种未见过的位置，我们也可以把它写成训练集中见过的位置的线性组合，而不用担心测试集中遇到更长的句子无法推广。

##### 位置信息的传递机制

但位置编码是在最底层添加，会不会在深层网络中丢失？这个担心是多余的。通过**残差连接**，位置信息能够充分传递到上层网络。

假设有一个N层的神经网络，输入为x₀（包含位置编码），那么：

```markdown
- 第1层: x₁ = x₀ + F₁(x₀)
- 第2层: x₂ = x₁ + F₂(x₁) = x₀ + F₁(x₀) + F₂(x₁)
- 第3层: x₃ = x₂ + F₃(x₂) = x₀ + F₁(x₀) + F₂(x₁) + F₃(x₂)
- ...
- 第N层: xₙ = x₀ + Σᵢ₌₁ⁿ Fᵢ(xᵢ₋₁)
```

可以看到，初始的位置信息x₀始终存在于每一层的输出中，这确保了位置信息不会随着网络层数的加深而消失。

#### 从PyTorch源码API来理解transformer的架构设计

通过查看PyTorch的源码，来了解Encoder和Decoder中的架构实现。源码位于`/pytorch/torch/nn/modules/transformer.py`，此次借助的版本是v2.5.1。

##### 顶层Transformer类的设计

首先，PyTorch定义了一个顶层的`Transformer`类，我们可以通过`torch.nn.Transformer`来调用它：

```python
# 使用示例
transformer_model = nn.Transformer(d_model=512, nhead=8, num_encoder_layers=6)
```


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-2.png)
2.jpg



在`Transformer`的`__init__`函数中，主要有5个核心参数：

1. **d_model**：整个Transformer的特征维度，在原论文中设置的是512。这个维度需要足够大以承载丰富的语义信息，但太大会导致计算复杂度过高。

2. **nhead**：Multi-head attention的头数目。多头设计的目的是让模型可以捕捉到更多位置与位置之间的关系；

3. **num_encoder_layers**：编码器encoder的block数目，encoder的每个block包含多头自注意力机制和前馈神经网络，这里默认block是6个；

4. **num_decoder_layers**：decoder解码器中block数目，decoder的每个block包含多头自注意力机制、交叉注意力机制以及前馈神经网络；

5. **dim_feedforward**：前馈神经网络层中间的特征维度，默认是2048。Multihead attention输出时，会**首先**映射到2048这个大的特征空间，然后再把它映射回来到512这样的空间。必须要保证输出的维度仍然是512，这样就可以进行残差连接；


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-3.png)
3.jpg



##### 模块化设计

init函数的作用是实例化模块，第一个要实例化的模块就是encoder。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-4.png)
4.jpg


encoder通过TransformerEncoder的class去实现实例，在这个class中需要传入encoder_layer，在TransformerEncoderLayer的class中实现了Multihead self attention的调用、残差连接、层归一化、全连接层网络，主要是这些来构成一个encoder_layer。

对于decode部分也是一样，传入decodeLayer参数，这个layer包含了自注意力机制、交叉注意力机制以及前馈神经网络。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-5.png)
5.jpg


总体上Transformer源码，就是由四个class所构成：
- **TransformerEncoderLayer**：每一个编码层的实现
- **TransformerEncoder**：负责把这些编码层串起来
- **TransformerDecoderLayer**：每一个解码层的实现
- **TransformerDecoder**：把这些解码层串起来

这种模块化的设计体现了软件工程的最佳实践：单一职责原则和组合优于继承的思想。

##### Forward函数：编排计算流程

在`forward`函数中，Transformer的计算流程非常清晰：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-6.png)
6.jpg


首先encoder输入是source句子以及padding_mask，encoder中的注意力机制不需要掩码，因此mask及is_causal参数不需要传入掩码。但需要对样本长度做掩盖，即**padding_mask**，这个mask表示每一个样本的长度。当我们做训练时，序列长度是不一样的，有些短的样本，在后面的一些位置上就是无效的，通过在softmax中把无效位置上的值转成负无穷，这样经过归一化后概率就变成0，使得在这些位置上，这些没有值的位置变得无效。

decode输入第一个是target，也就是目标句子。第二个是memory，表示encoder输出，因为memory会输送到交叉注意力中。第三个是target mask，这个target mask是一个考虑因果的mask，在数学上是一个上三角矩阵。

##### 因果掩码mask

每次预测时，decoder都会有一个输入句子，即：output embedding。但这个output embedding不能全部给它，如果全部给它的话，那它就变成了identity映射，相当于从x到x的关系我给你了，那预测出来的答案肯定是从x到x。

我们需要保证output每次只根据当前要预测的单词的左边的所有单词，去预测这个单词。这个单词的本身和其他的右边的单词都不要输送到Output Embedding。这样的操作需要通过mask来实现，随着预测的字符往右进行，我们给到这个decoder中的output会越来越多，所以它就是一个上三角的矩阵。

第四个memory mask，和source sentence的长度有关，在batch训练中source sentence每一个样本都不太一样，memory mask就是每一个输入源序列这个样本的一个长度。

##### Transformer框架

这就是Transformer class总体上的构成框架，init函数去实例化encoder和decoder。在forward函数中基于source、target、source mask、target mask，分别入参到encoder和decoder中，最终得到output，即要预测字符的概率。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-7.png)
7.jpg


Transformer本质上是一个自回归的解码过程，不是并行的预测输出，而是每次只会预测一个，输出一个，然后不断的进行解码去预测出整体的target sentence。

#### Encoder编码器层

接下来我们分别来看下init函数中的4个class，首先是**单个编码器**的实现：在`TransformerEncoderLayer`的`__init__`函数中，需要实例化四个关键组件：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-8.png)
8.jpg


先是init函数中的参数，和transformer中传入的一致，d_model是整个Transformer的特征维度512。nhead是Multi-head attention中多头自注意力机制中头的数目。

##### 多头注意力的设计

为什么是多头？目的是让**模型可以捕捉到更多的位置与位置之间的关系**。多头会分为多组的query、key和value，每一组会单独地去计算attention的上下文的向量，最后把这个向量拼起来，再通过FFN得到最终的一个向量。

这样做的话，对embedding的特征向量的维度会降低，比如说原来的特征向量维度是512，如果我们分为8个头，这时向量每一个头它向量的维度就会变成64（这里不是通过压缩，而是线性变换重组）。每个头独立计算注意力后，会得到8个64维的输出向量。然后通过拼接操作（concatenation），将这8个64维向量首尾相接，重新组合成一个512维的向量。最后再通过一个输出线性变换层，得到最终的512维输出。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-9.png)
9.jpg


##### 前馈神经网络

dimension feed forward是前馈神经网络FFN的维度，因为需要先从512到2048，再从2048到512，所以设定了两个全连接层。前馈神经网络它是对每个单独位置进行一个建模，并且不同位置的参数是共享的。类比1×1的pointwise卷积，对图像中每个像素位置的特征向量独立进行变换。参数共享就是为序列中的每个位置都设计相同的参数，目的是希望模型学会"如何处理特征"的通用能力，而不是"如何处理第x个位置的特征"的特定能力。

FFN实际上做的是embedding相同位置不同维度间的融合，在每个位置内部对该位置的不同特征维度进行融合，注意力机制负责位置间的信息交流。

##### Encoder编码器层的组件实例化

init函数中需要去实例化一些实例：
1. 首先是Multi-head attention，本节着重整个框架；
2. 实例FFN前馈神经网络中的两个Linear层，第一个Linear比较大，第二个Linear是重新这个投射到d_model的尺度；
3. 实例layer norm，在self attention之后会经过层归一化，以及在前馈神经网络之后也会经过一个层归一；
4. 实例两个dropout，dropout是为了使得这个网络具备集成学习的特点，即使我们在训练多个模提高泛化能力；

##### Encoder编码器前向传播forward: 编排计算流程

forward函数中，encoder层的调用很简单。Transformer encoder layer的第一部分：通过self attention block得到一个表征(self._sa_block)，然后再加一个这个残差连接(就是和x加起来)，最后再经过一个层归一化。self attention的输入是序列x和pendding-mask，这里的序列x既充当了query，又充当了key和value。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-10.png)
10.jpg


第二部分是**feed forward block**，把第一部分输出经过每个位置独立的一个全连接层，再进行一个残差连接，输送到层归一化中就得到x。这个就是Transformer encoder中的每个layer的输出。

原始论文的设计是层归一化在后，即else的设计。

##### Encoder编码器的串联

`TransformerEncoder` class的作用是将多个编码器层串联起来：将上一层的输出作为下一层的输入，经过多层处理得到最终的编码器输出。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-11.png)
11.jpg


init主要是传入两个参数，一个是encoder_layer，表示TransformerEncoderLayer class的一个实例。第二个参数是num_layers，表示transformer encoder有多少层，层的含义就是block。encoder中自注意力机制+前馈神经网络这两块是一个block，也就是一层。

#### Decoder解码器

解码器的实现比编码器更复杂，因为它包含三个子模块，需要处理更多的交互。

在`TransformerDecoderLayer`中，我们需要实例化三套组件（**自注意力+交叉注意力+前馈神经网络**）：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-12.png)
12.jpg


在init参数中，第一个是d_model，表示transformer模型特征大小，默认512。第二个参数是nhead，是Transformer decoder的多头自注意力机制的头数。第三个参数是dimension feed forward，表示decoder中FFN前馈神经网络的维度。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-13.png)
13.jpg



##### Decoder解码器两种注意力机制的区别

init参数中，decoder和encoder不同的地方，就是需要实例化两个Multihead attention。

第一个Multi-head attention，是**自注意力机制**，它是对decoder这个输入序列的，即：target sentence embedding作为输入序列的自身表征。

第二个Multi-head attention是**交叉注意力机制**，我们想知道decoder multihead attention的输出和encoder输出状态的一个关联性，用该注意力机制跨越了encoder和decoder两个不同序列，不是decoder内部的自我关注，而是让decoder去关注encoder的信息。于是我们通过用decoder MHA（多头注意力）的一个输出作为query，然后用encoder的输出作为key和value来去算出一个上下文表征。

同样Decoder要实现两个Linear层，第一个Linear层是比较大的，把我们交叉自注意力机制的输出，投射到一个更高维的空间，就是2048。然后再把它投射到低维的空间，就是从2048降成512。由于Decoder有三个模块（自注意力+交叉注意力+前馈神经网络），所以这里要实现3个norm和3个dropout。

##### Decoder解码器forward：编排流程

解码器的`forward`函数体现了三个模块的协同工作：

1. 第一个模块会把target sentence，也就是序列x和target mask输入到self._sa_block中，对target句子做自注意力机制的计算，结果放入到残差网络中，并且经过层归一化得到输出。

2. 第二个模块依赖于第一个模块输出的x，再和encoder输出的memory做交叉注意力的计算，得到新的表征后，经过残差网络和归一化的norm输出；

3. 把第二个模块的输出输送到FFN前馈神经网络，再次进行残差网络和归一化的norm，得到decoder的输出；


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-14.png)
14.jpg


可以看下_sa_block和_mha_block各自的调用，它们都是调用的是Multihead attention，只不过它们的query、key、value是不一样的。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-15.png)
15.jpg



![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-16.png)
16.jpg


self attention中query、key、value都是目标序列，自身对自身的求相关性的计算。但在交叉注意力机制中，query是decoder的一个输出，key和value是encoder的输出（始终是memory）。

通过多个TransformerDecoderLayer，构成了TransformerDecoder，和TransformerEncoder实现类似，这里不重复赘述。

#### 注意力机制的核心计算

最后看下注意力机制的核心计算，PyTorch的实际实现更加复杂和优化，但核心思想可以用论文版本来理解：


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-17.png)
17.jpg


##### 注意力机制的直观理解

attention函数就是将一个query和一个由key和value形成的一对元素，建立一个连接，最终得到一个输出。比如：我们去百度搜索一个词条，这个词条就是query，然后百度的数据库里有很多词条信息，每个信息自身都有个key，value就是该词条的具体内容。我们通过这个query，百度就会给我们返回一个搜索结果。这个结果就可以理解为一个注意力机制--基于query和key+value计算出来的一个上下文。

注意力机制的计算结果是Value的一个加权求和的结果，权重是基于Query和Key的相似度计算出来的。先算Query和每个Key的相似度，基于这个相似度进行Softmax归一化得到权重，再把这个权重与每个Key所对应的Value进行加权求和。

##### Scaled Dot-Product Attention

在Transformer模型中，用的是"Scaled Dot-Product Attention"，这里有个scaled，可以看到公式中就是QK，会除以一个根号d_k，这个目的就是为了使得Softmax的输入分布会更加稳定一点，也就是使得它的方差会更小一点。

这个Attention由三部分构成，分别是Q、K、V，它们都是三个向量。首先我们会把query和key进行一个矩阵相乘，如果我们单个样本来看就是向量内积，批量来看就是矩阵相乘。

内积过后再除以一个根号d_K，把每个位置上的这个内积放到一起去做一个归一化。这样就可以得到每个位置上的一个概率的表示，因为Softmax它出来的结果就是它总和为1，然后每一个值都是在0到1之间，得到这样一个概率，然后我们把概率和每个位置上value进行一个加权求和，最终能得到attention的一个输出，这就是scaled dot product attention的计算逻辑。

论文中讲的Multi-head self attention其实就是有很多个这样的自注意力机制同时计算，算完之后我们把每一个得到的结果给拼起来，得到了Multi-head self attention最终的输出。

##### 注意力计算的代码实现

attention代码如下，这里我们用的是论文实现的简单版本。输入由query、key和value构成。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/transformer-architecture/images/trans-img-18.png)
18.jpg


首先会把这个q跟k的转置进行一个矩阵相乘，那这样的话就能得到一个一✖️t的向量，把这个向量做一个mask。这里的mask就是把等于0的位置，填充一个非常非常小的一个数，负无穷的数，因为负无穷的数经过Softmax这个归一化之后，它就会变成0的概率，目的是希望那些不重要的位置上的概率赋为0。这里的mask，这里只有一个mask，所以你可以理解为那它这里是一个自注意力机制的一个实现，如果有两个mask，那就是交叉注意力机制的实现。

得到这个p attention就概率分布之后，再把这个p attention跟value进行一个加权求和，得到最终自注意力机制的输出，这是单个自注意力机制的一个计算逻辑，如果是多头的话，最终把单个的输出拼起来就好。

在Transformer模型中，不同的注意力机制有着不同的QKV来源和映射方式：

1. **encoder层的query key和value**：在编码器中都是由word embedding加上position encoding后，通过三个独立的线性映射得到QKV；

2. **在decoder中self attention层**：同样也是通过target sentence embedding+position encoding，通过三个独立的线性映射得到QKV；

3. **在交叉attention中**：query是由decoder的输出经过一个线性映射得到的，key和value是编码器的输出memory分别经过两个映射得到；


**参考资料：**

1. [DataWhale HapplyLLM](https://datawhalechina.github.io/happy-llm/#/)
2. [deep_thought](https://www.bilibili.com/video/BV1o44y1Y7cp/?vd_source=a957a54256d2af7f2a1778751c3855cb&spm_id_from=333.788.videopod.sections)
3. [HandleNLP](https://nlp.seas.harvard.edu/2018/04/03/attention.html)

### 文本数据处理详解

本补充章节旨在对大模型数据处理做一个简单的梳理与具体的代码实现，帮助大家对于大模型的数据处理有一个更加清晰的认识。

#### 1.理解词嵌入

在深度神经网络模型中，由于文本是分类数据，模型无法直接处理原始文本，因此需要将词语表示为连续值向量传输给模型。这一处理过程我们称之为词嵌入，其本质是将**离散对象**（如词语）映射到**连续向量**空间中的点，目的是将非数值数据转换为神经网络可处理的格式。

通过将每个词映射为高维空间中的点（如“猫”=[0.2, -1.7, ...]），使语义相似的词（如“猫”和“狗”）向量距离更近，而无关词（如“猫”和“汽车”）距离更远。这种向量化表示既保留词语关系（“国王-男性+女性≈女王”），又能作为神经网络的输入，是大模型理解语言的基础。

我们可以看一下下面的代码示例


```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import re

# 示例文本（可自行修改并且测试）
text = "Hello, how are you today? I hope you are doing well."

# 简单分词函数
def tokenize(text):
    # 按非字母数字字符分割文本，并保留分隔符
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return tokens
# 构建词汇表
def build_vocab(tokens):
    unique_tokens = sorted(set(tokens))
    vocab = {token: i for i, token in enumerate(unique_tokens)}
    vocab_size = len(vocab)
    return vocab, vocab_size
# 文本编码
def encode_text(tokens, vocab):
    return [vocab.get(token, vocab['<unk>']) for token in tokens]

# 创建词嵌入模型
class WordEmbeddingModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(WordEmbeddingModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

    def forward(self, inputs):
        return self.embedding(inputs)

# 可视化词向量
def visualize_embeddings(embeddings, token_ids, vocab):
    reverse_vocab = {i: token for token, i in vocab.items()}
    pca = PCA(n_components=2)
    embeddings_2d = pca.fit_transform(embeddings.detach().numpy())
    # 绘制散点图
    plt.figure(figsize=(10, 8))
    for i, token_id in enumerate(token_ids):
        plt.scatter(embeddings_2d[i, 0], embeddings_2d[i, 1], marker='o')
        plt.annotate(reverse_vocab[token_id],
                     (embeddings_2d[i, 0], embeddings_2d[i, 1]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.title('Word Embeddings Visualization')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True)
    plt.savefig('word_embeddings.png')
    plt.show()

def main():
    tokens = tokenize(text)
    print(f"Tokens: {tokens}")
    tokens_with_special = tokens + ['<pad>', '<unk>']

    # 构建词汇表
    vocab, vocab_size = build_vocab(tokens_with_special)
    print(f"Vocabulary size: {vocab_size}")
    print(f"Vocabulary: {vocab}")

    # 编码文本
    encoded_text = encode_text(tokens, vocab)
    print(f"Encoded text: {encoded_text}")
    input_tensor = torch.tensor(encoded_text, dtype=torch.long)

    # 初始化模型
    embedding_dim = 10  # 词向量维度，即提到的词空间
    model = WordEmbeddingModel(vocab_size, embedding_dim)
    # 获取词向量
    embeddings = model(input_tensor)
    print(f"Embeddings shape: {embeddings.shape}")  # 这里应该是 [序列长度, 嵌入维度]

    print(f"Word vector for '{tokens[0]}': {embeddings[0].detach().numpy()}")
    print(f"Word vector for '{tokens[1]}': {embeddings[1].detach().numpy()}")
    # 可视化词向量（仅用于低维演示，实际应用中词向量维度通常较高）
    if embedding_dim >= 2:
        visualize_embeddings(embeddings, encoded_text, vocab)

    # 计算词之间的相似度
    print("\n词相似度分析:")
    for i, token_i in enumerate(tokens[:5]):  # 只分析前5个词
        for j, token_j in enumerate(tokens[:5]):
            if i != j:
                # 计算余弦相似度
                sim = F.cosine_similarity(embeddings[i].unsqueeze(0),
                                         embeddings[j].unsqueeze(0))
                print(f" '{token_i}' 和 '{token_j}' 的相似度: {sim.item():.4f}")

if __name__ == "__main__":
    main()
```

    Tokens: ['Hello', ',', 'how', 'are', 'you', 'today', '?', 'I', 'hope', 'you', 'are', 'doing', 'well', '.']
    Vocabulary size: 14
    Vocabulary: {',': 0, '.': 1, '<pad>': 2, '<unk>': 3, '?': 4, 'Hello': 5, 'I': 6, 'are': 7, 'doing': 8, 'hope': 9, 'how': 10, 'today': 11, 'well': 12, 'you': 13}
    Encoded text: [5, 0, 10, 7, 13, 11, 4, 6, 9, 13, 7, 8, 12, 1]
    Embeddings shape: torch.Size([14, 10])
    Word vector for 'Hello': [-0.16787808 -0.46388683 -0.4728546   0.59449345 -0.23820949  0.34212282
      0.6591729  -0.10877569  0.60686487 -1.771871  ]
    Word vector for ',': [ 0.19194137 -1.2824519   1.1420391  -0.8361696  -0.578317    0.1025617
      1.2452478  -0.08552601  0.9869009  -0.04940421]




![png](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/text-data-processing/image/output_1_1.png)




    词相似度分析:
     'Hello' 和 ',' 的相似度: 0.2132
     'Hello' 和 'how' 的相似度: -0.0277
     'Hello' 和 'are' 的相似度: 0.1024
     'Hello' 和 'you' 的相似度: 0.1597
     ',' 和 'Hello' 的相似度: 0.2132
     ',' 和 'how' 的相似度: -0.0801
     ',' 和 'are' 的相似度: -0.6096
     ',' 和 'you' 的相似度: 0.2355
     'how' 和 'Hello' 的相似度: -0.0277
     'how' 和 ',' 的相似度: -0.0801
     'how' 和 'are' 的相似度: 0.1170
     'how' 和 'you' 的相似度: -0.0412
     'are' 和 'Hello' 的相似度: 0.1024
     'are' 和 ',' 的相似度: -0.6096
     'are' 和 'how' 的相似度: 0.1170
     'are' 和 'you' 的相似度: 0.2203
     'you' 和 'Hello' 的相似度: 0.1597
     'you' 和 ',' 的相似度: 0.2355
     'you' 和 'how' 的相似度: -0.0412
     'you' 和 'are' 的相似度: 0.2203


这下我们就能够很清楚的在散点图中看到不同词语之间的距离。

#### 2.分词

分词是将输入文本拆分为单个标记（可以是单词、标点符号等）的过程，举个例子，我们可以把句子“Hello, world!”拆成一小块一小块的形式，如```["Hello", ",", "world", "!"]```，使计算机能够逐块处理语言，进一步转换为模型可处理的数值形式。

我们可以从简单的分词方法入手，例如使用 Python 的正则表达式（re 库）按空白字符拆分文本，但这种方法可能导致标点符号与单词粘连（如 “Hello,” 中的逗号未分离）。

为此，我们可以在代码当中修改正则表达式，在空白字符、逗号、句号等处进行拆分，使单词与标点符号成为独立列表项。

同时，在处理的过程中需注意保留空白字符或移除冗余空白，例如处理 Python 代码时需保留缩进，而普通文本可移除。
值得注意的是：通常不将文本转为小写，因为大小写有助于模型区分专有名词、理解句子结构。
实现代码如下：


```python
import re
import tiktoken
from collections import defaultdict

class SimpleTokenizer:
    """简单分词器实现"""
    def __init__(self, text=None):
        self.vocab = {}
        self.reverse_vocab = {}
        self.vocab_size = 0
        self.special_tokens = {
            '<pad>': 0,
            '<unk>': 1,
            '<bos>': 2,
            '<eos>': 3
        }
        if text:
            self.build_vocab(text)

    def tokenize(self, text):
        """将文本分割为标记列表"""
        # 保留空白字符的分词
        tokens = re.findall(r'\S+|\s+', text)
        return tokens

    def build_vocab(self, text):
        """构建词汇表"""
        self.vocab = self.special_tokens.copy()
        self.vocab_size = len(self.special_tokens)
        tokens = self.tokenize(text)
        token_counts = defaultdict(int)
        for token in tokens:
            token_counts[token] += 1
        sorted_tokens = sorted(token_counts.items(), key=lambda x: (-x[1], x[0]))
        for token, _ in sorted_tokens:
            if token not in self.vocab:
                self.vocab[token] = self.vocab_size
                self.vocab_size += 1
        self.reverse_vocab = {v: k for k, v in self.vocab.items()}

    def encode(self, text):
        """将文本转换为标记ID序列"""
        tokens = self.tokenize(text)
        return [self.vocab.get(token, self.vocab['<unk>']) for token in tokens]

    def decode(self, token_ids):
        """将标记ID序列转换回文本"""
        tokens = []
        for token_id in token_ids:
            if token_id in self.reverse_vocab:
                tokens.append(self.reverse_vocab[token_id])
            else:
                tokens.append('<unk>')
        text = ''
        prev_token = None
        for token in tokens:
            if prev_token and prev_token.isspace():
                text += token
            else:
                text = text.rstrip() + token
            prev_token = token

        return text


class BPETokenizer:
    """基于字节对编码(BPE)的分词器"""
    def __init__(self, model_name="gpt2"):
        """
        初始化BPE分词器
        model_name: 模型名称，如"gpt2"或"cl100k_base"(OpenAI的text-embedding-ada-002使用)
        """
        self.encoder = tiktoken.get_encoding(model_name)
        self.vocab_size = self.encoder.n_vocab

    def tokenize(self, text):
        """将文本转换为BPE标记列表"""
        token_ids = self.encoder.encode(text)
        tokens = [self.encoder.decode_single_token_bytes(token_id) for token_id in token_ids]
        return tokens

    def encode(self, text):
        """将文本转换为BPE标记ID序列"""
        return self.encoder.encode(text)

    def decode(self, token_ids):
        """将BPE标记ID序列转换回文本"""
        return self.encoder.decode(token_ids)

if __name__ == "__main__":
    sample_text = "Hello, how are you today? I hope you are doing well."
    print("=== 简单分词器 ===")
    simple_tokenizer = SimpleTokenizer(sample_text)
    tokens = simple_tokenizer.tokenize(sample_text)
    print(f"分词结果: {tokens}")
    encoded = simple_tokenizer.encode(sample_text)
    print(f"编码结果: {encoded}")
    decoded = simple_tokenizer.decode(encoded)
    print(f"解码结果: {decoded}")
    print(f"词汇表大小: {simple_tokenizer.vocab_size}")
    print("\n=== BPE分词器 (GPT-2) ===")
    bpe_tokenizer = BPETokenizer("gpt2")
    bpe_tokens = bpe_tokenizer.tokenize(sample_text)
    print(f"BPE分词结果: {bpe_tokens}")
    bpe_encoded = bpe_tokenizer.encode(sample_text)
    print(f"BPE编码结果: {bpe_encoded}")
    bpe_decoded = bpe_tokenizer.decode(bpe_encoded)
    print(f"BPE解码结果: {bpe_decoded}")
    print(f"BPE词汇表大小: {bpe_tokenizer.vocab_size}")
```

    === 简单分词器 ===
    分词结果: ['Hello,', ' ', 'how', ' ', 'are', ' ', 'you', ' ', 'today?', ' ', 'I', ' ', 'hope', ' ', 'you', ' ', 'are', ' ', 'doing', ' ', 'well.']
    编码结果: [7, 4, 11, 4, 5, 4, 6, 4, 12, 4, 8, 4, 10, 4, 6, 4, 5, 4, 9, 4, 13]
    解码结果: Hello, how are you today? I hope you are doing well.
    词汇表大小: 14

    === BPE分词器 (GPT-2) ===
    BPE分词结果: [b'Hello', b',', b' how', b' are', b' you', b' today', b'?', b' I', b' hope', b' you', b' are', b' doing', b' well', b'.']
    BPE编码结果: [15496, 11, 703, 389, 345, 1909, 30, 314, 2911, 345, 389, 1804, 880, 13]
    BPE解码结果: Hello, how are you today? I hope you are doing well.
    BPE词汇表大小: 50257


#### 3.将标记转换为标记ID

将标记转换为标记 ID 是连接文本与数值向量的中间步骤，其核心是构建 “词汇表”—— 一个从唯一标记到唯一整数的映射（如图 2.6 所示）。词汇表的构建过程是：从分词后的文本中提取所有唯一标记，按字母顺序排序后，为每个标记分配一个整数 ID。例如，《判决》分词后得到 1130 个唯一标记，词汇表便会将这些标记分别映射到 0 至 1129 的整数。

有了词汇表，我们就能通过 “编码” 将文本转换为标记 ID（例如 “Hello” 对应某个整数），也能通过 “解码” 将标记 ID 转回文本。这一过程可通过分词器类实现，例如 SimpleTokenizerV1 包含 encode 和 decode 方法：encode 先对文本分词，再用词汇表映射为 ID；decode 则将 ID 通过反向映射转回文本，并处理标点符号前的空格问题。

但需注意，若文本中出现词汇表外的标记（如 “Hello” 未出现在《判决》中），编码时会报错，这说明训练集的规模和多样性对扩展词汇表至关重要，也引出了后续处理未知词汇的需求。

整体实现代码如下：


```python
import re
from collections import Counter
from typing import List, Dict, Tuple, Optional, Set
class Tokenizer:
    """将文本转换为标记并映射到ID的分词器"""

    def __init__(self, special_tokens: Optional[Dict[str, int]] = None):
        """
        初始化分词器

        Args:
            special_tokens: 特殊标记及其ID的字典，默认为None
        """
        self.vocab: Dict[str, int] = {}  # 词汇表: 标记 -> ID
        self.reverse_vocab: Dict[int, str] = {}  # 反向词汇表: ID -> 标记
        self.special_tokens = special_tokens or {
            "<pad>": 0,  # 填充标记
            "<unk>": 1,  # 未知标记
            "<bos>": 2,  # 序列开始标记
            "<eos>": 3   # 序列结束标记
        }
        self.vocab_size: int = len(self.special_tokens)  # 词汇表大小
        # 初始化词汇表，添加特殊标记
        for token, idx in self.special_tokens.items():
            self.vocab[token] = idx
            self.reverse_vocab[idx] = token

    def build_vocab(self, texts: List[str], min_freq: int = 1) -> None:
        """
        从文本构建词汇表

        Args:
            texts: 文本列表
            min_freq: 最小词频，低于此频率的词将被忽略
        """
        # 统计词频
        token_counts = Counter()
        for text in texts:
            tokens = self.tokenize(text)
            token_counts.update(tokens)
        # 按频率排序，频率相同则按字母顺序
        sorted_tokens = sorted(
            [(token, count) for token, count in token_counts.items() if count >= min_freq],
            key=lambda x: (-x[1], x[0])
        )
        # 为每个标记分配ID
        for token, _ in sorted_tokens:
            if token not in self.vocab:
                self.vocab[token] = self.vocab_size
                self.reverse_vocab[self.vocab_size] = token
                self.vocab_size += 1

    def tokenize(self, text: str) -> List[str]:
        """
        将文本分割为标记列表

        Args:
            text: 输入文本

        Returns:
            标记列表
        """
        tokens = re.findall(r'\w+|[^\w\s]|\s+', text)
        return tokens

    def encode(self, text: str, add_special_tokens: bool = False) -> List[int]:
        """
        将文本转换为标记ID列表

        Args:
            text: 输入文本
            add_special_tokens: 是否添加特殊标记

        Returns:
            标记ID列表
        """
        tokens = self.tokenize(text)
        encoded = [self.vocab.get(token, self.vocab["<unk>"]) for token in tokens]

        if add_special_tokens:
            encoded = [self.vocab["<bos>"]] + encoded + [self.vocab["<eos>"]]

        return encoded

    def decode(self, ids: List[int], remove_special_tokens: bool = False) -> str:
        """
        将标记ID列表转换回文本
        Args:
            ids: 标记ID列表
            remove_special_tokens: 是否移除特殊标记
        Returns:
            文本
        """
        tokens = []
        for idx in ids:
            if idx in self.reverse_vocab:
                token = self.reverse_vocab[idx]
                if remove_special_tokens and token in self.special_tokens:
                    continue
                tokens.append(token)
            else:
                tokens.append("<unk>")
        text = ''.join(tokens)
        return re.sub(r'\s+', ' ', text).strip()

def test_tokenizer():
    """测试Tokenizer类的功能"""
    print("===== 测试 Tokenizer =====")
    texts = [
        "Hello, how are you today?",
        "I hope you are doing well.",
        "This is a test of the tokenizer."
    ]

    tokenizer = Tokenizer()
    tokenizer.build_vocab(texts)
    print(f"词汇表大小: {tokenizer.vocab_size}")
    print(f"前10个词汇项: {list(tokenizer.vocab.items())[:10]}")
    sample_text = "Hello, this is a test!"
    tokens = tokenizer.tokenize(sample_text)
    print(f"\n分词结果: {tokens}")
    encoded = tokenizer.encode(sample_text)
    print(f"编码结果: {encoded}")
    encoded_with_special = tokenizer.encode(sample_text, add_special_tokens=True)
    print(f"带特殊标记的编码结果: {encoded_with_special}")
    decoded = tokenizer.decode(encoded)
    print(f"解码结果: {decoded}")
    decoded_with_special = tokenizer.decode(encoded_with_special, remove_special_tokens=True)
    print(f"移除特殊标记的解码结果: {decoded_with_special}")
    unknown_text = "This is a unicorn 🦄 test."
    encoded_unknown = tokenizer.encode(unknown_text)
    decoded_unknown = tokenizer.decode(encoded_unknown)
    print(f"\n包含未知词汇的文本: {unknown_text}")
    print(f"编码结果: {encoded_unknown}")
    print(f"解码结果: {decoded_unknown}")

if __name__ == "__main__":
    test_tokenizer()
```

    ===== 测试 Tokenizer =====
    词汇表大小: 24
    前10个词汇项: [('<pad>', 0), ('<unk>', 1), ('<bos>', 2), ('<eos>', 3), (' ', 4), ('.', 5), ('are', 6), ('you', 7), (',', 8), ('?', 9)]

    分词结果: ['Hello', ',', ' ', 'this', ' ', 'is', ' ', 'a', ' ', 'test', '!']
    编码结果: [10, 8, 4, 1, 4, 17, 4, 13, 4, 19, 1]
    带特殊标记的编码结果: [2, 10, 8, 4, 1, 4, 17, 4, 13, 4, 19, 1, 3]
    解码结果: Hello, <unk> is a test<unk>
    移除特殊标记的解码结果: Hello, is a test

    包含未知词汇的文本: This is a unicorn 🦄 test.
    编码结果: [12, 4, 17, 4, 13, 4, 1, 4, 1, 4, 19, 5]
    解码结果: This is a <unk> <unk> test.


#### 4.添加特殊上下文标记

为解决未知词汇问题并增强模型对上下文的理解，需引入特殊标记。常见的特殊标记包括：<|unk|>（表示未知词汇）、（分隔不同文本来源）、[BOS]（序列开始）、[EOS]（序列结束）、[PAD]（填充短文本至统一长度）等。

例如，修改词汇表加入 <|unk|> 和后，分词器（如 SimpleTokenizerV2）在遇到未知词时会自动替换为 <|unk|>，并在不同文本间插入作为分隔。这一调整使模型能处理未见过的词汇，并区分独立文本来源。需注意，GPT 模型通常仅使用作为分隔符和填充符，而不依赖 <|unk|>，因为其采用的字节对编码（BPE）分词器能通过子词分解处理未知词，这也是后续将介绍的更高效方法。


```python
import re
from typing import List, Dict, Optional, Set

class Tokenizer:
    """带有特殊上下文标记的分词器"""
    def __init__(self, special_tokens: Optional[Dict[str, int]] = None):
        """
        初始化分词器

        Args:
            special_tokens: 特殊标记及其ID的字典，默认为None
        """
        # 设置默认特殊标记
        self.default_special_tokens = {
            "<pad>": 0,  # 填充标记
            "<unk>": 1,  # 未知标记
            "<bos>": 2,  # 序列开始标记
            "<eos>": 3,  # 序列结束标记
            "<sep>": 4,  # 分隔标记
            "<cls>": 5,  # 分类标记
        }
        # 合并用户提供的特殊标记
        self.special_tokens = {**self.default_special_tokens, **(special_tokens or {})}
        # 初始化词汇表
        self.vocab: Dict[str, int] = {}
        self.reverse_vocab: Dict[int, str] = {}
        self.vocab_size: int = len(self.special_tokens)
        # 添加特殊标记到词汇表
        for token, idx in self.special_tokens.items():
            self.vocab[token] = idx
            self.reverse_vocab[idx] = token

    def build_vocab(self, texts: List[str], min_freq: int = 1) -> None:
        """
        从文本构建词汇表

        Args:
            texts: 文本列表
            min_freq: 最小词频，低于此频率的词将被忽略
        """
        # 统计词频
        token_counts = {}
        for text in texts:
            tokens = self.tokenize(text)
            for token in tokens:
                token_counts[token] = token_counts.get(token, 0) + 1

        # 按频率排序，频率相同则按字母顺序
        sorted_tokens = sorted(
            [(token, count) for token, count in token_counts.items() if count >= min_freq],
            key=lambda x: (-x[1], x[0])  # 按频率降序，字母升序
        )

        # 为每个标记分配ID
        for token, _ in sorted_tokens:
            if token not in self.vocab:
                self.vocab[token] = self.vocab_size
                self.reverse_vocab[self.vocab_size] = token
                self.vocab_size += 1

    def tokenize(self, text: str) -> List[str]:
        """
        将文本分割为标记列表

        Args:
            text: 输入文本

        Returns:
            标记列表
        """
        # 简单的分词：按非字母数字字符分割，保留空格和标点符号
        tokens = re.findall(r'\w+|[^\w\s]|\s+', text)
        return tokens

    def encode(self, text: str, add_special_tokens: bool = False) -> List[int]:
        """
        将文本转换为标记ID列表

        Args:
            text: 输入文本
            add_special_tokens: 是否添加特殊标记

        Returns:
            标记ID列表
        """
        tokens = self.tokenize(text)
        encoded = [self.vocab.get(token, self.vocab["<unk>"]) for token in tokens]
        if add_special_tokens:
            encoded = [self.vocab["<bos>"]] + encoded + [self.vocab["<eos>"]]
        return encoded
    def decode(self, ids: List[int], remove_special_tokens: bool = False) -> str:
        """
        将标记ID列表转换回文本
        Args:
            ids: 标记ID列表
            remove_special_tokens: 是否移除特殊标记
        Returns:
            文本
        """
        tokens = []
        for idx in ids:
            if idx in self.reverse_vocab:
                token = self.reverse_vocab[idx]
                if remove_special_tokens and token in self.special_tokens:
                    continue
                tokens.append(token)
            else:
                tokens.append("<unk>")
        text = ''.join(tokens)
        return re.sub(r'\s+', ' ', text).strip()

    def add_special_token(self, token: str) -> int:
        """
        添加新的特殊标记
        Args:
            token: 特殊标记字符串
        Returns:
            新标记的ID
        """
        if token in self.vocab:
            return self.vocab[token]
        new_id = self.vocab_size
        self.vocab[token] = new_id
        self.reverse_vocab[new_id] = token
        self.vocab_size += 1
        return new_id

def test_special_tokens():
    """测试特殊标记的功能"""
    print("===== 测试特殊标记 =====")
    texts = [
        "Hello, how are you today?",
        "I hope you are doing well.",
        "This is a test of the tokenizer."
    ]
    tokenizer = Tokenizer()
    tokenizer.build_vocab(texts)
    sample_text = "Hello, this is a test!"
    encoded = tokenizer.encode(sample_text, add_special_tokens=True)
    decoded = tokenizer.decode(encoded, remove_special_tokens=True)

    print(f"原始文本: {sample_text}")
    print(f"编码结果: {encoded}")
    print(f"解码结果: {decoded}")
    print("\n--- 测试特殊标记 ---")
    print(f"特殊标记: {tokenizer.special_tokens}")
    # 测试<bos>和<eos>
    encoded_with_bos_eos = tokenizer.encode(sample_text, add_special_tokens=True)
    print(f"带<bos>和<eos>的编码: {encoded_with_bos_eos}")
    # 测试<SEP>标记 - 连接两个句子
    print("\n--- 测试<SEP>标记 ---")
    sentence1 = "What is your name?"
    sentence2 = "My name is Doubao."
    encoded1 = tokenizer.encode(sentence1)
    encoded2 = tokenizer.encode(sentence2)
    # 添加<SEP>标记
    encoded_combined = [tokenizer.vocab["<bos>"]] + \
                       encoded1 + \
                       [tokenizer.vocab["<sep>"]] + \
                       encoded2 + \
                       [tokenizer.vocab["<eos>"]]
    decoded_combined = tokenizer.decode(encoded_combined, remove_special_tokens=True)
    print(f"句子1: {sentence1}")
    print(f"句子2: {sentence2}")
    print(f"合并后的编码: {encoded_combined}")
    print(f"合并后的解码: {decoded_combined}")
    # 测试添加新的特殊标记
    print("\n--- 测试添加新的特殊标记 ---")
    new_token = "<mask>"
    new_token_id = tokenizer.add_special_token(new_token)
    print(f"添加新特殊标记: {new_token} (ID: {new_token_id})")

    # 测试使用新的特殊标记
    masked_text = "This is a <mask> sentence."
    encoded_masked = tokenizer.encode(masked_text, add_special_tokens=True)
    decoded_masked = tokenizer.decode(encoded_masked, remove_special_tokens=False)

    print(f"带<mask>的文本: {masked_text}")
    print(f"编码结果: {encoded_masked}")
    print(f"解码结果: {decoded_masked}")


if __name__ == "__main__":
    test_special_tokens()
```

    ===== 测试特殊标记 =====
    原始文本: Hello, this is a test!
    编码结果: [2, 12, 10, 6, 1, 6, 19, 6, 15, 6, 21, 1, 3]
    解码结果: Hello, is a test

    --- 测试特殊标记 ---
    特殊标记: {'<pad>': 0, '<unk>': 1, '<bos>': 2, '<eos>': 3, '<sep>': 4, '<cls>': 5}
    带<bos>和<eos>的编码: [2, 12, 10, 6, 1, 6, 19, 6, 15, 6, 21, 1, 3]

    --- 测试<SEP>标记 ---
    句子1: What is your name?
    句子2: My name is Doubao.
    合并后的编码: [2, 1, 6, 19, 6, 1, 6, 1, 11, 4, 1, 6, 1, 6, 19, 6, 1, 7, 3]
    合并后的解码: is ? is .

    --- 测试添加新的特殊标记 ---
    添加新特殊标记: <mask> (ID: 26)
    带<mask>的文本: This is a <mask> sentence.
    编码结果: [2, 14, 6, 19, 6, 15, 6, 1, 1, 1, 6, 1, 7, 3]
    解码结果: <bos>This is a <unk><unk><unk> <unk>.<eos>


#### 5.字节对编码

字节对编码（BPE）是一种高级分词方法，被 GPT-2、GPT-3 等主流 LLMs 采用，其核心优势是能处理未知词汇 —— 将未见过的单词分解为子词单元（如图 2.11 所示）。例如，“someunknownPlace” 可拆分为已知的子词标记，无需依赖 <|unk|>。

BPE 的实现可借助 tiktoken 库（OpenAI 开源），其基于 Rust 实现，高效且兼容 GPT 模型的分词逻辑。使用时，先通过 tiktoken.get_encoding ("gpt2") 实例化分词器，再用 encode 方法将文本转换为标记 ID，decode 方法则可还原文本。例如，“Hello, do you like tea?” 经 BPE 编码后，会生成一系列整数 ID，解码后能准确还原原始文本，即使包含 “someunknownPlace” 这类未知词，也能通过子词拆分正确处理。

BPE 的词汇表规模固定（如 GPT-2 为 50257），通过迭代合并高频字符或子词构建，既控制了词汇表大小，又能覆盖几乎所有可能的文本，是平衡效率与泛化能力的理想选择。


```python
import re
import tiktoken
from collections import defaultdict, Counter
from typing import List, Dict, Tuple, Optional, Set, Union

class SimpleBPETokenizer:
    """简单实现的BPE分词器"""

    def __init__(self, vocab_size: int = 100):
        """
        初始化BPE分词器

        Args:
            vocab_size: 目标词汇表大小
        """
        self.vocab_size = vocab_size
        self.vocab = {}  # 词汇表: 标记 -> ID
        self.reverse_vocab = {}  # 反向词汇表: ID -> 标记
        self.bpe_ranks = {}  # BPE合并规则的优先级
        self.special_tokens = {
            "<pad>": 0,
            "<unk>": 1,
            "<bos>": 2,
            "<eos>": 3
        }
        self.vocab_size_actual = len(self.special_tokens)

        # 初始化词汇表，添加特殊标记
        for token, idx in self.special_tokens.items():
            self.vocab[token] = idx
            self.reverse_vocab[idx] = token

    def _get_stats(self, pairs: Dict[Tuple[str, str], int]) -> Dict[Tuple[str, str], int]:
        """计算所有相邻字节对的频率"""
        stats = defaultdict(int)
        for word, freq in pairs.items():
            symbols = word.split()
            for i in range(len(symbols) - 1):
                stats[symbols[i], symbols[i + 1]] += freq
        return stats

    def _merge_vocab(self, pair: Tuple[str, str], v_in: Dict[str, int]) -> Dict[str, int]:
        """合并最频繁的字节对"""
        v_out = {}
        bigram = re.escape(' '.join(pair))
        p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
        for word in v_in:
            w_out = p.sub(''.join(pair), word)
            v_out[w_out] = v_in[word]
        return v_out

    def _word_to_pairs(self, word: str) -> Set[Tuple[str, str]]:
        """将单词拆分为相邻字节对"""
        symbols = word.split()
        pairs = set()
        if len(symbols) < 2:
            return pairs
        for i in range(len(symbols) - 1):
            pairs.add((symbols[i], symbols[i + 1]))
        return pairs

    def build_vocab(self, texts: List[str]) -> None:
        """
        从文本构建BPE词汇表

        Args:
            texts: 文本列表
        """
        # 初始化词汇表，包含所有单个字符
        token_counts = Counter()
        for text in texts:
            # 将文本拆分为字符，用空格分隔
            words = [' '.join(list(text))]
            for word in words:
                token_counts[word] += 1

        # 统计初始的字符词汇表
        chars = set()
        for text in texts:
            chars.update(text)

        # 添加字符到词汇表
        for char in sorted(chars):
            if char not in self.vocab:
                self.vocab[char] = self.vocab_size_actual
                self.reverse_vocab[self.vocab_size_actual] = char
                self.vocab_size_actual += 1

        # 开始BPE合并过程
        num_merges = self.vocab_size - self.vocab_size_actual
        if num_merges <= 0:
            return

        pairs = token_counts.copy()
        for i in range(num_merges):
            # 计算所有相邻字节对的频率
            stats = self._get_stats(pairs)
            if not stats:
                break

            # 选择最频繁的字节对
            best = max(stats, key=stats.get)

            # 记录合并规则的优先级
            self.bpe_ranks[best] = i

            # 合并词汇表中的字节对
            pairs = self._merge_vocab(best, pairs)

            # 将新合并的标记添加到词汇表
            new_token = ''.join(best)
            if new_token not in self.vocab:
                self.vocab[new_token] = self.vocab_size_actual
                self.reverse_vocab[self.vocab_size_actual] = new_token
                self.vocab_size_actual += 1

    def _get_pairs(self, word: List[str]) -> Set[Tuple[str, str]]:
        """获取单词中所有相邻标记对"""
        pairs = set()
        prev_char = word[0]
        for char in word[1:]:
            pairs.add((prev_char, char))
            prev_char = char
        return pairs

    def bpe(self, token: str) -> List[str]:
        """
        对单个标记应用BPE算法

        Args:
            token: 输入标记

        Returns:
            BPE分词后的标记列表
        """
        if token in self.special_tokens:
            return [token]

        word = list(token)
        if len(word) == 0:
            return []
        if len(word) == 1:
            return [word[0]]

        pairs = self._get_pairs(word)

        while True:
            # 找到优先级最高的字节对
            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float('inf')))
            if bigram not in self.bpe_ranks:
                break

            first, second = bigram
            new_word = []
            i = 0
            while i < len(word):
                try:
                    j = word.index(first, i)
                    new_word.extend(word[i:j])
                    i = j
                except:
                    new_word.extend(word[i:])
                    break

                if i < len(word) - 1 and word[i + 1] == second:
                    new_word.append(first + second)
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1

            word = new_word
            if len(word) == 1:
                break
            else:
                pairs = self._get_pairs(word)

        return word

    def tokenize(self, text: str) -> List[str]:
        """
        将文本分词为BPE标记

        Args:
            text: 输入文本

        Returns:
            BPE标记列表
        """
        tokens = []
        for token in text.split():
            if token in self.special_tokens:
                tokens.append(token)
            else:
                tokens.extend(self.bpe(token))
        return tokens

    def encode(self, text: str, add_special_tokens: bool = False) -> List[int]:
        """
        将文本编码为BPE标记ID列表

        Args:
            text: 输入文本
            add_special_tokens: 是否添加特殊标记

        Returns:
            BPE标记ID列表
        """
        tokens = self.tokenize(text)
        encoded = [self.vocab.get(token, self.vocab["<unk>"]) for token in tokens]

        if add_special_tokens:
            encoded = [self.vocab["<bos>"]] + encoded + [self.vocab["<eos>"]]

        return encoded

    def decode(self, ids: List[int], remove_special_tokens: bool = False) -> str:
        """
        将BPE标记ID列表解码为文本

        Args:
            ids: BPE标记ID列表
            remove_special_tokens: 是否移除特殊标记

        Returns:
            解码后的文本
        """
        tokens = []
        for idx in ids:
            if idx in self.reverse_vocab:
                token = self.reverse_vocab[idx]
                if remove_special_tokens and token in self.special_tokens:
                    continue
                tokens.append(token)
            else:
                tokens.append("<unk>")

        # 简单的后处理：合并标记
        text = ''.join(tokens)
        return text


# 测试代码
def test_simple_bpe_tokenizer():
    """测试简单实现的BPE分词器"""
    print("===== 测试简单BPE分词器 =====")

    # 示例文本
    texts = [
        "Hello, how are you today?",
        "I hope you are doing well.",
        "This is a test of the BPE tokenizer."
    ]

    # 初始化BPE分词器
    tokenizer = SimpleBPETokenizer(vocab_size=50)

    # 构建词汇表
    tokenizer.build_vocab(texts)

    print(f"词汇表大小: {tokenizer.vocab_size_actual}")
    print(f"前10个词汇项: {list(tokenizer.vocab.items())[:10]}")

    # 测试分词
    sample_text = "Hello, this is a test!"
    tokens = tokenizer.tokenize(sample_text)
    print(f"\n分词结果: {tokens}")

    # 测试编码
    encoded = tokenizer.encode(sample_text, add_special_tokens=True)
    print(f"编码结果: {encoded}")

    # 测试解码
    decoded = tokenizer.decode(encoded, remove_special_tokens=True)
    print(f"解码结果: {decoded}")

    # 测试包含未知词汇的文本
    unknown_text = "This is a unicorn 🦄 test."
    encoded_unknown = tokenizer.encode(unknown_text)
    decoded_unknown = tokenizer.decode(encoded_unknown)
    print(f"\n包含未知词汇的文本: {unknown_text}")
    print(f"编码结果: {encoded_unknown}")
    print(f"解码结果: {decoded_unknown}")

    print("\n所有测试完成!")


def test_tiktoken_bpe():
    """测试tiktoken库的BPE分词器"""
    print("\n===== 测试tiktoken BPE分词器 =====")

    # 初始化tiktoken BPE分词器
    try:
        tokenizer = tiktoken.get_encoding("gpt2")
    except KeyError:
        # 如果没有安装gpt2编码，尝试使用cl100k_base (用于text-embedding-ada-002)
        tokenizer = tiktoken.get_encoding("cl100k_base")

    print(f"词汇表大小: {tokenizer.n_vocab}")

    # 测试分词
    sample_text = "Hello, this is a test!"
    tokens = tokenizer.encode(sample_text)
    print(f"\n编码结果 (ID): {tokens}")

    # 转换ID为字节
    token_bytes = [tokenizer.decode_single_token_bytes(token) for token in tokens]
    print(f"编码结果 (字节): {token_bytes}")

    # 测试解码
    decoded = tokenizer.decode(tokens)
    print(f"解码结果: {decoded}")

    # 测试包含未知词汇的文本
    unknown_text = "This is a unicorn 🦄 test."
    encoded_unknown = tokenizer.encode(unknown_text)
    decoded_unknown = tokenizer.decode(encoded_unknown)
    print(f"\n包含未知词汇的文本: {unknown_text}")
    print(f"编码结果: {encoded_unknown}")
    print(f"解码结果: {decoded_unknown}")

    # 计算文本的token数量
    print(f"\n文本 '{sample_text}' 的token数量: {len(tokens)}")

if __name__ == "__main__":
    test_simple_bpe_tokenizer()
    test_tiktoken_bpe()
```

    ===== 测试简单BPE分词器 =====
    词汇表大小: 46
    前10个词汇项: [('<pad>', 0), ('<unk>', 1), ('<bos>', 2), ('<eos>', 3), (' ', 4), (',', 5), ('.', 6), ('?', 7), ('B', 8), ('E', 9)]

    分词结果: ['Hello,', 't', 'h', 'is', 'is', 'a', 't', 'e', 's', 't', '!']
    编码结果: [2, 44, 28, 19, 41, 41, 14, 28, 16, 27, 28, 1, 3]
    解码结果: Hello,thisisatest

    包含未知词汇的文本: This is a unicorn 🦄 test.
    编码结果: [13, 19, 41, 41, 14, 29, 23, 20, 1, 24, 26, 23, 1, 28, 16, 27, 28, 6]
    解码结果: Thisisauni<unk>orn<unk>test.

    所有测试完成!

    ===== 测试tiktoken BPE分词器 =====
    词汇表大小: 50257

    编码结果 (ID): [15496, 11, 428, 318, 257, 1332, 0]
    编码结果 (字节): [b'Hello', b',', b' this', b' is', b' a', b' test', b'!']
    解码结果: Hello, this is a test!

    包含未知词汇的文本: This is a unicorn 🦄 test.
    编码结果: [1212, 318, 257, 44986, 12520, 99, 226, 1332, 13]
    解码结果: This is a unicorn 🦄 test.

    文本 'Hello, this is a test!' 的token数量: 7


#### 6.使用滑动窗口进行数据采样

LLMs 通过 “下一个词预测” 任务预训练，即给定输入文本块，预测紧随其后的下一个词（如图 2.12 所示）。为生成训练所需的输入 - 目标对，需采用 “滑动窗口” 方法：在分词后的文本上滑动固定大小的窗口，窗口内的文本作为输入，窗口右侧紧邻的词作为目标（输入右移一位即为目标）。

例如，若窗口大小（上下文长度）为 4，输入为 [标记 1, 标记 2, 标记 3, 标记 4]，则目标为 [标记 2, 标记 3, 标记 4, 标记 5]。为高效生成批量样本，可结合 PyTorch 的 Dataset 和 DataLoader：Dataset 负责按窗口滑动生成输入 - 目标对，DataLoader 则将这些对打包为批次（如图 2.13 所示），支持设置批次大小、步长（窗口移动距离）等参数。

步长决定样本重叠程度：步长为 1 时，相邻样本高度重叠；步长等于窗口大小时，样本无重叠。合理设置步长可平衡数据利用率与过拟合风险，最终生成的输入 - 目标对以张量形式输入模型，为训练提供数据支持。



```python
import torch
from torch.utils.data import Dataset, DataLoader
from typing import List, Tuple, Optional

class TextWindowDataset(Dataset):
    """使用滑动窗口对文本进行采样的数据集"""

    def __init__(self,
                 text: List[int],
                 context_length: int,
                 stride: int = 1,
                 pad_id: int = 0):
        """
        初始化文本窗口数据集

        Args:
            text: 已编码的文本（整数列表）
            context_length: 上下文长度（窗口大小）
            stride: 滑动窗口的步长，默认为1
            pad_id: 填充标记的ID
        """
        self.text = text
        self.context_length = context_length
        self.stride = stride
        self.pad_id = pad_id

        # 计算有效样本数量
        self.num_samples = max(0, (len(text) - context_length) // stride + 1)

    def __len__(self) -> int:
        """返回数据集的样本数量"""
        return self.num_samples

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        获取单个样本

        Args:
            idx: 样本索引

        Returns:
            元组(inputs, targets)，其中inputs是输入序列，targets是目标序列
        """
        # 计算窗口起始位置
        start = idx * self.stride

        # 确保窗口不超出文本长度
        end = start + self.context_length
        if end > len(self.text):
            # 截取最后可能的有效窗口
            end = len(self.text)
            start = end - self.context_length

        # 提取输入序列和目标序列
        inputs = self.text[start:end]
        targets = self.text[start+1:end+1]  # 目标是输入的下一个标记

        # 如果目标序列长度不足，用pad_id填充
        if len(targets) < self.context_length:
            targets = targets + [self.pad_id] * (self.context_length - len(targets))

        # 转换为张量
        inputs = torch.tensor(inputs, dtype=torch.long)
        targets = torch.tensor(targets, dtype=torch.long)

        return inputs, targets


def create_data_loader(text: List[int],
                       context_length: int,
                       batch_size: int,
                       stride: int = 1,
                       shuffle: bool = False) -> DataLoader:
    """
    创建文本窗口数据加载器

    Args:
        text: 已编码的文本（整数列表）
        context_length: 上下文长度
        batch_size: 批次大小
        stride: 滑动窗口步长
        shuffle: 是否打乱数据

    Returns:
        数据加载器
    """
    dataset = TextWindowDataset(
        text=text,
        context_length=context_length,
        stride=stride
    )

    data_loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle
    )

    return data_loader


# 测试代码
def test_sliding_window():
    """测试滑动窗口数据采样"""
    print("===== 测试滑动窗口数据采样 =====")

    # 示例文本（已编码）
    encoded_text = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    print(f"原始文本: {encoded_text}")

    # 参数设置
    context_length = 4
    stride = 2
    batch_size = 2

    # 创建数据集
    dataset = TextWindowDataset(
        text=encoded_text,
        context_length=context_length,
        stride=stride
    )

    # 打印数据集信息
    print(f"\n数据集大小: {len(dataset)}")

    # 测试获取单个样本
    print("\n--- 测试获取单个样本 ---")
    for i in range(min(3, len(dataset))):
        inputs, targets = dataset[i]
        print(f"样本 {i}:")
        print(f"  输入: {inputs}")
        print(f"  目标: {targets}")

    # 创建数据加载器
    data_loader = create_data_loader(
        text=encoded_text,
        context_length=context_length,
        batch_size=batch_size,
        stride=stride,
        shuffle=False
    )

    # 测试批次数据
    print("\n--- 测试批次数据 ---")
    for i, (batch_inputs, batch_targets) in enumerate(data_loader):
        print(f"批次 {i}:")
        print(f"  输入形状: {batch_inputs.shape}")
        print(f"  输入数据:")
        print(batch_inputs)
        print(f"  目标形状: {batch_targets.shape}")
        print(f"  目标数据:")
        print(batch_targets)

    # 测试不同步长
    print("\n--- 测试不同步长 ---")
    for stride in [1, 2, 3]:
        dataset = TextWindowDataset(
            text=encoded_text,
            context_length=context_length,
            stride=stride
        )
        print(f"步长为 {stride} 时的样本数: {len(dataset)}")

        # 打印前两个样本
        if len(dataset) > 0:
            inputs, targets = dataset[0]
            print(f"  第一个样本输入: {inputs}")
            print(f"  第一个样本目标: {targets}")

        if len(dataset) > 1:
            inputs, targets = dataset[1]
            print(f"  第二个样本输入: {inputs}")
            print(f"  第二个样本目标: {targets}")
if __name__ == "__main__":
    test_sliding_window()
```

    ===== 测试滑动窗口数据采样 =====
    原始文本: [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

    数据集大小: 4

    --- 测试获取单个样本 ---
    样本 0:
      输入: tensor([101, 102, 103, 104])
      目标: tensor([102, 103, 104, 105])
    样本 1:
      输入: tensor([103, 104, 105, 106])
      目标: tensor([104, 105, 106, 107])
    样本 2:
      输入: tensor([105, 106, 107, 108])
      目标: tensor([106, 107, 108, 109])

    --- 测试批次数据 ---
    批次 0:
      输入形状: torch.Size([2, 4])
      输入数据:
    tensor([[101, 102, 103, 104],
            [103, 104, 105, 106]])
      目标形状: torch.Size([2, 4])
      目标数据:
    tensor([[102, 103, 104, 105],
            [104, 105, 106, 107]])
    批次 1:
      输入形状: torch.Size([2, 4])
      输入数据:
    tensor([[105, 106, 107, 108],
            [107, 108, 109, 110]])
      目标形状: torch.Size([2, 4])
      目标数据:
    tensor([[106, 107, 108, 109],
            [108, 109, 110,   0]])

    --- 测试不同步长 ---
    步长为 1 时的样本数: 7
      第一个样本输入: tensor([101, 102, 103, 104])
      第一个样本目标: tensor([102, 103, 104, 105])
      第二个样本输入: tensor([102, 103, 104, 105])
      第二个样本目标: tensor([103, 104, 105, 106])
    步长为 2 时的样本数: 4
      第一个样本输入: tensor([101, 102, 103, 104])
      第一个样本目标: tensor([102, 103, 104, 105])
      第二个样本输入: tensor([103, 104, 105, 106])
      第二个样本目标: tensor([104, 105, 106, 107])
    步长为 3 时的样本数: 3
      第一个样本输入: tensor([101, 102, 103, 104])
      第一个样本目标: tensor([102, 103, 104, 105])
      第二个样本输入: tensor([104, 105, 106, 107])
      第二个样本目标: tensor([105, 106, 107, 108])


#### 7.创建词嵌入

词嵌入是将标记 ID 转换为连续向量的过程，是 LLM 处理文本的最终数值形式（如图 2.15 所示）。神经网络需连续向量进行运算，因此需通过 “嵌入层” 实现这一转换。嵌入层本质是一个权重矩阵：行数等于词汇表大小，列数为嵌入维度（如 3 维、256 维），每个标记 ID 对应矩阵中的一行，即该标记的嵌入向量。

例如，词汇表大小为 6、嵌入维度为 3 的嵌入层，其权重矩阵为 6×3 的随机初始化矩阵（训练中会优化）。当输入标记 ID 为 [2, 3, 5, 1] 时，嵌入层会提取矩阵中对应行，得到 4×3 的嵌入向量矩阵。

在 PyTorch 中，可通过 torch.nn.Embedding 实现嵌入层，其核心是 “查找操作”—— 根据 ID 快速检索对应嵌入向量。嵌入维度需权衡：更高维度（如 GPT-3 的 12288 维）能捕捉更多语义，但计算成本更高；较低维度（如 256 维）适合实验。嵌入层的权重会通过训练不断优化，使向量能更好地表示标记的语义和上下文


```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
from typing import List, Dict, Tuple, Optional, Set

class Vocabulary:
    """词汇表管理类"""

    def __init__(self, special_tokens: Optional[Dict[str, int]] = None):
        """
        初始化词汇表

        Args:
            special_tokens: 特殊标记及其ID的字典
        """
        self.token_to_idx = special_tokens or {
            "<pad>": 0,
            "<unk>": 1,
            "<bos>": 2,
            "<eos>": 3
        }
        self.idx_to_token = {v: k for k, v in self.token_to_idx.items()}
        self.vocab_size = len(self.token_to_idx)

    def add_token(self, token: str) -> int:
        """
        添加标记到词汇表

        Args:
            token: 要添加的标记

        Returns:
            标记的ID
        """
        if token not in self.token_to_idx:
            self.token_to_idx[token] = self.vocab_size
            self.idx_to_token[self.vocab_size] = token
            self.vocab_size += 1
        return self.token_to_idx[token]

    def build_from_texts(self, texts: List[List[str]]) -> None:
        """
        从文本列表构建词汇表

        Args:
            texts: 文本列表，每个文本是标记列表
        """
        for text in texts:
            for token in text:
                self.add_token(token)

    def encode(self, tokens: List[str]) -> List[int]:
        """
        将标记列表编码为ID列表

        Args:
            tokens: 标记列表

        Returns:
            ID列表
        """
        return [self.token_to_idx.get(token, self.token_to_idx["<unk>"]) for token in tokens]

    def decode(self, ids: List[int]) -> List[str]:
        """
        将ID列表解码为标记列表

        Args:
            ids: ID列表

        Returns:
            标记列表
        """
        return [self.idx_to_token.get(idx, "<unk>") for idx in ids]


class CBOWDataset(Dataset):
    """连续词袋模型(CBOW)的数据集"""

    def __init__(self, texts: List[List[str]], vocab: Vocabulary, context_size: int = 2):
        """
        初始化CBOW数据集

        Args:
            texts: 文本列表，每个文本是标记列表
            vocab: 词汇表
            context_size: 上下文大小(每侧的词数)
        """
        self.context_size = context_size
        self.vocab = vocab
        self.data = []

        # 构建训练样本
        for text in texts:
            encoded_text = vocab.encode(text)
            for i in range(context_size, len(encoded_text) - context_size):
                context = []
                # 收集左右上下文
                for j in range(-context_size, context_size + 1):
                    if j != 0:  # 跳过中心词
                        context.append(encoded_text[i + j])
                target = encoded_text[i]  # 中心词
                self.data.append((context, target))

    def __len__(self) -> int:
        """返回数据集大小"""
        return len(self.data)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        获取单个样本

        Args:
            idx: 样本索引

        Returns:
            元组(context, target)，其中context是上下文词ID，target是目标词ID
        """
        context, target = self.data[idx]
        return torch.tensor(context, dtype=torch.long), torch.tensor(target, dtype=torch.long)


class CBOW(nn.Module):
    """连续词袋模型(CBOW)"""

    def __init__(self, vocab_size: int, embedding_dim: int):
        """
        初始化CBOW模型

        Args:
            vocab_size: 词汇表大小
            embedding_dim: 嵌入维度
        """
        super(CBOW, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, vocab_size)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """
        前向传播

        Args:
            inputs: 输入张量，形状为[batch_size, context_size*2]

        Returns:
            输出张量，形状为[batch_size, vocab_size]
        """
        # 获取上下文词的嵌入
        embeds = self.embeddings(inputs)
        # 对上下文嵌入取平均
        context_mean = torch.mean(embeds, dim=1)
        # 通过线性层预测中心词
        output = self.linear(context_mean)
        return output


def train_cbow_model(texts: List[List[str]], embedding_dim: int = 100,
                     context_size: int = 2, epochs: int = 10,
                     batch_size: int = 32, lr: float = 0.01) -> nn.Embedding:
    """
    训练CBOW模型并返回词嵌入

    Args:
        texts: 文本列表，每个文本是标记列表
        embedding_dim: 嵌入维度
        context_size: 上下文大小
        epochs: 训练轮数
        batch_size: 批次大小
        lr: 学习率

    Returns:
        训练好的词嵌入层
    """
    # 构建词汇表
    vocab = Vocabulary()
    vocab.build_from_texts(texts)

    # 创建数据集和数据加载器
    dataset = CBOWDataset(texts, vocab, context_size)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # 初始化模型、损失函数和优化器
    model = CBOW(vocab.vocab_size, embedding_dim)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # 训练模型
    for epoch in range(epochs):
        total_loss = 0
        for context, target in dataloader:
            # 前向传播
            output = model(context)
            loss = criterion(output, target)

            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(dataloader):.4f}")

    # 返回训练好的词嵌入层
    return model.embeddings


# 测试代码
def test_word_embedding():
    """测试词嵌入功能"""
    print("===== 测试词嵌入 =====")

    # 示例文本
    texts = [
        ["I", "like", "to", "play", "football"],
        ["Football", "is", "a", "popular", "sport"],
        ["I", "enjoy", "watching", "football", "matches"],
        ["Do", "you", "play", "any", "sports"],
        ["Sports", "are", "good", "for", "health"]
    ]

    # 训练CBOW模型获取词嵌入
    embedding_dim = 10
    context_size = 2
    embeddings = train_cbow_model(
        texts=texts,
        embedding_dim=embedding_dim,
        context_size=context_size,
        epochs=50,
        batch_size=4,
        lr=0.01
    )

    # 获取词汇表
    vocab = Vocabulary()
    vocab.build_from_texts(texts)

    # 测试词嵌入查找
    test_words = ["I", "football", "sports", "unknown"]
    print("\n词嵌入示例:")
    for word in test_words:
        word_id = vocab.encode([word])[0]
        word_vector = embeddings(torch.tensor(word_id, dtype=torch.long)).detach().numpy()
        print(f"{word}: {word_vector[:5]}... (shape: {word_vector.shape})")

    # 计算词之间的相似度
    print("\n词相似度分析:")
    target_words = ["football", "sports", "play"]
    for target in target_words:
        target_id = vocab.encode([target])[0]
        target_vector = embeddings(torch.tensor(target_id, dtype=torch.long))

        print(f"\n与 '{target}' 最相似的词:")
        similarities = []
        for word, idx in vocab.token_to_idx.items():
            if word in ["<pad>", "<unk>", "<bos>", "<eos>"]:
                continue

            word_vector = embeddings(torch.tensor(idx, dtype=torch.long))
            # 计算余弦相似度
            sim = torch.cosine_similarity(target_vector.unsqueeze(0),
                                         word_vector.unsqueeze(0)).item()
            similarities.append((word, sim))

        # 按相似度排序
        similarities.sort(key=lambda x: x[1], reverse=True)

        # 打印前3个相似词
        for word, sim in similarities[:3]:
            print(f"  {word}: {sim:.4f}")

if __name__ == "__main__":
    test_word_embedding()
```

    ===== 测试词嵌入 =====
    Epoch 1/50, Loss: 3.1725
    Epoch 2/50, Loss: 3.2624
    Epoch 3/50, Loss: 3.1252
    Epoch 4/50, Loss: 2.7059
    Epoch 5/50, Loss: 2.4706
    Epoch 6/50, Loss: 2.3471
    Epoch 7/50, Loss: 2.5184
    Epoch 8/50, Loss: 2.4183
    Epoch 9/50, Loss: 2.3172
    Epoch 10/50, Loss: 2.2042
    Epoch 11/50, Loss: 2.2335
    Epoch 12/50, Loss: 1.9774
    Epoch 13/50, Loss: 1.8652
    Epoch 14/50, Loss: 1.7527
    Epoch 15/50, Loss: 1.8568
    Epoch 16/50, Loss: 1.6976
    Epoch 17/50, Loss: 1.4242
    Epoch 18/50, Loss: 1.2158
    Epoch 19/50, Loss: 1.1381
    Epoch 20/50, Loss: 1.0590
    Epoch 21/50, Loss: 1.2977
    Epoch 22/50, Loss: 1.3026
    Epoch 23/50, Loss: 0.9900
    Epoch 24/50, Loss: 0.7884
    Epoch 25/50, Loss: 1.0041
    Epoch 26/50, Loss: 0.8770
    Epoch 27/50, Loss: 0.8645
    Epoch 28/50, Loss: 0.7021
    Epoch 29/50, Loss: 0.8588
    Epoch 30/50, Loss: 0.6019
    Epoch 31/50, Loss: 0.4728
    Epoch 32/50, Loss: 0.5092
    Epoch 33/50, Loss: 0.4671
    Epoch 34/50, Loss: 0.4910
    Epoch 35/50, Loss: 0.5640
    Epoch 36/50, Loss: 0.5198
    Epoch 37/50, Loss: 0.4731
    Epoch 38/50, Loss: 0.4264
    Epoch 39/50, Loss: 0.3248
    Epoch 40/50, Loss: 0.2492
    Epoch 41/50, Loss: 0.2738
    Epoch 42/50, Loss: 0.3748
    Epoch 43/50, Loss: 0.2021
    Epoch 44/50, Loss: 0.2448
    Epoch 45/50, Loss: 0.1978
    Epoch 46/50, Loss: 0.2853
    Epoch 47/50, Loss: 0.1764
    Epoch 48/50, Loss: 0.1442
    Epoch 49/50, Loss: 0.1716
    Epoch 50/50, Loss: 0.2133

    词嵌入示例:
    I: [-0.0588957  -0.14068426 -0.7404043  -1.8865429  -2.6835012 ]... (shape: (10,))
    football: [ 0.637025    0.14052066 -0.848007    0.2889565  -0.2740498 ]... (shape: (10,))
    sports: [-1.045044   -0.70745003 -2.0171206   1.0361644   0.60308105]... (shape: (10,))
    unknown: [-0.14042336  0.71746343  0.11502329 -0.5219049   0.10613117]... (shape: (10,))

    词相似度分析:

    与 'football' 最相似的词:
      football: 1.0000
      is: 0.7577
      health: 0.6264

    与 'sports' 最相似的词:
      sports: 1.0000
      health: 0.5747
      is: 0.5725

    与 'play' 最相似的词:
      play: 1.0000
      popular: 0.6973
      is: 0.6605


#### 8.编码词位置

LLM 的自注意力机制本身不感知词的位置，因此需加入 “位置嵌入” 以传达词在序列中的顺序信息（如图 2.17 所示）。位置嵌入有两种类型：绝对位置嵌入（与具体位置绑定，如第 1 个词用特定向量，第 2 个词用另一向量）和相对位置嵌入（关注词之间的距离，如 “相距 2 个位置”）。

GPT 模型采用绝对位置嵌入，其实现方式是：创建另一个嵌入层，输入为 0 至上下文长度 - 1 的位置索引（如窗口大小为 4 时，输入为 [0, 1, 2, 3]），输出与词嵌入维度相同的位置向量。最终输入嵌入是词嵌入与位置嵌入的总和（如图 2.19 所示），例如某词的嵌入向量为 [1.2, -0.2, -0.1]，其位置嵌入为 [0.5, 0.3, 0.1]，则最终输入为 [1.7, 0.1, 0.0]。

位置嵌入的维度与词嵌入一致，确保两者可直接相加，且会随模型训练优化，使模型能学习到词序对语义的影响（如 “我爱你” 与 “你爱我” 的区别）。


```python
import torch
import tiktoken
# 1初始化分词器（使用GPT-2的BPE分词器）
tokenizer = tiktoken.get_encoding("gpt2")
# 定义嵌入参数
vocab_size = 50257  # GPT-2的词汇表大小
output_dim = 256    # 嵌入维度（示例用256，实际GPT-3为12288）
context_length = 4  # 上下文长度（即输入序列的最大长度）

# 创建词嵌入层和位置嵌入层
token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)

# 生成位置索引（0到context_length-1）
pos_indices = torch.arange(context_length)  # 形状: [4]
pos_embeddings = pos_embedding_layer(pos_indices)  # 形状: [4, 256]

# 测试：将词ID转换为嵌入并添加位置嵌入
def test_position_embedding():
    # 示例输入词ID
    input_ids = torch.tensor([
        [40, 367, 2885, 1464],    # 第一句的词ID
        [1807, 3619, 402, 271],   # 第二句的词ID
        [10899, 2138, 257, 7026]  # 第三句的词ID
    ])
    batch_size, seq_len = input_ids.shape
    print(f"输入词ID形状: {input_ids.shape}")  # 应输出: torch.Size([3, 4])

    # 生成词嵌入
    token_embeddings = token_embedding_layer(input_ids)
    print(f"词嵌入形状: {token_embeddings.shape}")  # 应输出: torch.Size([3, 4, 256])

    # 添加位置嵌入
    input_embeddings = token_embeddings + pos_embeddings
    print(f"添加位置嵌入后的形状: {input_embeddings.shape}")  # 应输出: torch.Size([3, 4, 256])

    # 验证位置嵌入的唯一性
    print("\n位置嵌入向量（前3个位置的前5维）:")
    for i in range(3):
        print(f"位置 {i}: {pos_embeddings[i, :5]}")

# 执行测试
if __name__ == "__main__":
    test_position_embedding()
```

    输入词ID形状: torch.Size([3, 4])
    词嵌入形状: torch.Size([3, 4, 256])
    添加位置嵌入后的形状: torch.Size([3, 4, 256])

    位置嵌入向量（前3个位置的前5维）:
    位置 0: tensor([-0.3552, -0.5629, -1.4778,  0.7029, -0.0278], grad_fn=<SliceBackward0>)
    位置 1: tensor([-0.7520,  0.3258,  0.5109, -1.2897,  0.2495], grad_fn=<SliceBackward0>)
    位置 2: tensor([-0.6930,  0.9321, -0.9753,  0.5288,  0.8013], grad_fn=<SliceBackward0>)


#### 贡献者主页


|贡献者|学校  | 研究方向           |   GitHub主页 |
|-----------------|------------------------|-----------------------|------------|
| 蔡鋆捷 | 福州大学  |    Computer Vision（CV），Natural Language Processing（NLP）      |https://github.com/xinala-781|

### 超小中文多模态模型的拼接微调

* 作者：情感机器实验室——陈少宏

* 邮箱：<shaohon_chen@115lab.club>

* GitHub：[https://github.com/ShaohonChen/Qwen3-SmVL](https://github.com/ShaohonChen/Qwen3-SmVL)
* SwanLab：[https://swanlab.cn/@ShaohonChen/Qwen3-SmVL/overview](https://swanlab.cn/@ShaohonChen/Qwen3-SmVL/overview)
* 数据集：[https://huggingface.co/datasets/HuggingFaceM4/the_cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron)

> 💚 **特别感谢**
> 感谢 [@zhihuazhao-bit](https://github.com/zhihuazhao-bit) 帮我审阅和修复了提交代码中众多的小 bug，并在 NV 上完成了测试。
> 感谢 [@KMnO4-zx](https://github.com/KMnO4-zx) 对教程文章内容的审核与修正。

#### 摘要

最近Huggingface团队发布了超小多模态模型SmolVLM2，可以做到端侧1GB显存推理。在怀着惊喜试用后发现，虽然模型有极其强大的视觉文本理解能力，但是模型却无法理解中文。这对一个“四六级压线过”的笔者来说十分不友好。刚好前段时间做SwanLab硬件检测适配时有一台未到期的沐曦曦云C500服务器，因此萌生了使用**沐曦GPU芯片**微调、把当前中文小模型扛把子Qwen3与SmolVLM2直接微调拼接的想法。

本教程将介绍一种模型拼接的思路，将SmolVLM2的视觉模块（0.09B）与Qwen3最小的模型（0.6B）进行对齐微调，最终使得Qwen模型具备一定的视觉理解能力。由于笔者时间有限且考虑到文章篇幅的原因，因此该系列预计将以系列的方式放出。篇幅规划如下：

* **第一篇**：如何构建和微调一个拼接模型（**本篇博客**）
* **第二篇**：模型测评、数据集优化、回答人类对齐
* **第三篇**：微调技巧介绍、视觉位置编码改动与模型结构优化



![PPAP](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/PPAP.png)
  I have a Qwen, I have a SmolVLM...



<div style="background-color:#fff3cd; color:black; padding:10px; border-radius:4px; border:1px solid #fbe5b0; width: 90%; max-width: 100%; margin: auto;">
  ⚠️关于算力的注意：本教程涉及VLM微调训练，对算力要求较高，需要40G及以上的GPU显存才能运行本教程的训练代码。
</div>

#### 目录

* [SmolVLM2的背景知识](#SmolVLM2的背景知识)
* [模型拼接和微调思路简介](#模型拼接和微调思路简介)
* [模型拼接实现和关键代码讲解](#模型拼接实现和关键代码讲解)
* [微调数据集构建](#微调数据集构建)
* [微调方法与代码实现](#微调方法与代码实现)
* [微调训练&结果展示](#微调训练&结果展示)
* [代码及数据集链接汇总](#代码及数据集链接汇总)

#### SmolVLM2的背景知识

首先，我们先回顾一下SmolVLM2模型的构建方案，SmolVLM2模型的整体包括三大块：视觉模型层，特征映射层和大语言模型层，见下图：



![smolvlm2](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/smolvlm2.png)
  SmolVLM2的架构图



这个设计是现在比较常见的VLM方案。核心设计思想就是让视觉模型的输出特征与经过embedding的文本特征直接拼接后输入到语言模型（LLM）当中，没有交叉注意力等模块。相比于早期LLaVA等架构，这种最大的优点就是可以最大程度复用已有的语言模型。以Qwen2.5-VL为例，其3B、7B、72B模型大小指的只是LLM部分，并没有包含Vision模块，实际上3B模型的参数量接近4B，视觉模块大概0.4B左右，三个不同大小的VLM使用的是统一的视觉模型。对于一些较大的VLM来说，构建视觉模型时绝大多数的训练都集中在特征映射模块和视觉模块，只在最后阶段为了最终效果进行整体微调时才会调整语言模块。保证了VLM的语言能力。

下面简述一下各个模块的细节：

* 视觉模型层：SmolVLM2-256M版本用的是Google的SigLip模型，一个基于ViT的视觉模型，选用的是最小的SigLip-93M的版本，HF论文里没具体写是直接用的SigLip的参数还是他们从零构建的（有注意到的读者可以评论留言下）。在SmolVLM2代码中对应的是`SmolVLMVisionTransformer`类

* 特征映射层：就是一个简单的MLP，不过SmolVLM2中为了降低图像分辨率还做了一个Pixel shuffle来降低图像分辨率，进一步减少视觉的Token占用，减少了文本长度。HF团队在论文里提到对于参数量较小的VLM来说使用Pixel shuffle还能提升性能。但可训练参数其实就是一个单层的神经网络，这个模块的核心作用就是做特征对齐，将视觉特征从768维（SigLip的维度）映射到576维（SmolLLM2的维度）

* 大语言模型：SmolVLM2-256M模型使用的文本模型是SmolLM-135M版本。可能是由于模型较小，HF团队在论文中说到训练时仅采用两阶段训练：大规模图文训练+针对视频任务的专门微调。为了保障模型的文本能力HF团队在训练数据中参杂了大概14%的纯文本微调数据。不过考虑到视觉模块本身参数量（93M）大小接近于文本模型（135M），因此笔者推测相比于冻结文本模型，数据平衡在这之中会起到更关键的作用。

HF团队在原文中还提到了许多影像小模型VLM性能的trick，感兴趣的读者可以进一步参考SmolVLM2的论文

#### 模型拼接和微调思路简介

正所谓顶级食材（模型）只需要最简单的烹饪。模型拼接的思路非常简单直接，基本就三步：

1. 调整SmolVLM2的“上下文控制格式”，使得其与Qwen3兼容。

2. 将模型的文本部分直接从SmolLM2换成Qwen3-0.6B，包括其文本tokenizer和词嵌入、文本模型、以及模型最后输出的语言模型头（LM Head）。

3. 需要重新初始化特征映射层的MLP，从768->576的单层神经网络改成768->1024的单层神经网络即可。

整体架构和对图文对前后处理依旧保持SmolVLM2的流程不变，具体改动见下图：



![concatation](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/concatation.png)
  将Qwen3-0.6B替换SmolVLM2的语言模型部分



笔者接下来详细介绍下为了实现“拼接”，具体改动的地方，供之后有类似的任务的读者参考。

#### 模型拼接实现和关键代码讲解

##### 第一处改动：SmolVLM2的Tokenizers部分

首先需要改动的就是需要改动的是SmolVLM2的Tokenizers部分，这里面主要是涉及两个问题：

* 第一个问题是要将SmolVLM2用于指示图像位置的特殊令牌（Special Token）加入到Qwen3的Tokenizer当中，这么做的目的是防止SmolVLM2的图像Token`<image>`被切分为`<`、`image`、`>`三块。幸运的是，Qwen3本身在Tokenizers中预留了未来用于多模态的特殊特殊令牌`<|image_pad|>`。因此读者直接使用了`<|image_pad|>`代替了`<image>`。用于在文本中预留图像特征的插入点。

* 第二个问题是：SmolVLM2的chat_template和Qwen3的chat_template差别极大。chat_template的作用是通过格式化文本让模型清楚知道不同Token所代表的背景信息。用最近比较流行的话来说就是“上下文工程”（Context Engineering）。

这里我列举了一下Qwen3、SmolVLM2、Qwen2.5-VL在聊天场景下的上下文，供读者参考。

**Qwen3聊天上下文格式**

以给一张图片，问题是“你的名字是什么?”，模型回答是“我的名字是Qwen”为例子。模型的上下文如下：

```txt
<|im_start|>user
你的名字是什么?<|im_end|>
<|im_start|>assistant
<think>

</think>

我的名字是Qwen<|im_end|>

```

注意Qwen3上下文是没有预留图像位置的，但相比于一般的LLM和VLM多了一个用于插入模型思考过程的`<think><\think>`，以及包含额外的函数调用控制文本。为了便于读者理解，读者在在下面举了一个函数调用的例子。这些函数调用上下文用于控制模型调用外部函数、API或者MCP接口和接收其返回的信息。

考虑到篇幅限制，本文就不粘贴带函数调用、推理、思考等一系列上下文的信息了（笔者打印了下发现实在太长了）。感兴趣的读者可以在Qwen3的官方文处了解详细设计

* [Qwen3函数调用案例](https://qwen.readthedocs.io/zh-cn/latest/framework/function_call.html#the-example-case)

可以说正是这些复杂的上下文信息让模型有可能实现推理、调用函数等多样化的能力。包括多模态理解任务也需要先对上下文进行设计。

**SmdwadwdoVLM2聊天上下文格式：**

以给一张图片，问题是“How many dog in there.”，模型回答是“There are Three dogs.”为例子。三种不同模型的上下文如下：

```txt
<|im_start|>User:<fake_token_around_image><row_1_col_1><image>...<image><fake_token_around_image><row_1_col_2><image>...<image><fake_token_around_image><row_1_col_3><image>...<image>...<fake_token_around_image><row_4_col_4><image>...<image>

<fake_token_around_image><global-img><image>...<image><fake_token_around_image>How many dog in there.<end_of_utterance>
Assistant: There are Three dogs.<end_of_utterance>
Assistant:
```

看起来非常乱，是因为有大量的`<image>`占位符。`<image>...<image>`之间是许多的`<image>`，笔者为了文章观感删掉了大量的占位符。注意模型的回车、空格均为上下文的一部分，在进行推理时需要严格遵守缩进关系。

但是我们仍能找到熟悉的内容，如`User:`，`Assistant:`等用于提示模型用户的输入与模型应当输出的位置。这些关键词和Qwen类似。

读者注意到了除了`<fake_token_around_image>`，`<image>`等用于指示图像的词，还出现了<row_1_col_1>这种位置指示符，这是因为SmolVLM2为了防止降采样对图像分辨率影响，专门使用了`image splitting`技术，简单来说就是将全局图和高清的局部图共同输入到模型当中（见下图`image splitting`模块），感兴趣的读者可在文末找到HF的技术报告了解详细技术。



![image-split](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/image-split.png)
  SmolVLM2的完整推理流程，可以看到在图像输入前使用`image splitting`进行了预切分



**本博文的拼接模型Qwen3-SmVL模型**

相比于Qwen3，SmolVLM2少了很多上下控制的

为了尽可能保存或者说预留Qwen3的思考、函数调用等能力，笔者最终选择将SmolVLM2对于图像特征的排列插入到Qwen3的上下文格式当中。最终上下文格式如下：

```txt
<|im_start|>user
<vision_start><row_1_col_1><|image_pad|>（图像插入的地方）<|image_pad|><vision_start>
（用户提问的地方）
<|im_end|>
<|im_start|>assistant
<think>

</think>

（模型回答的地方）<|im_end|>
<|endoftext|>
```

可以看到读者尽量保持了与Qwen3的风格和复用特殊令牌。这样能够使得后续拼接的Qwen3-0.6B模型不至于受到上下文差异过大带来的性能损耗。实际上在设计微调上下文时应尽量与模型先前训练的任务接近，以减少微调带来的性能损失。

transformers实现模型上下文格式控制的代码并非python语言，而是一种前端文本格式控制的语言Jinja。这个语言的变量作用域设计简直可以说是有魔法在里面。配合上Qwen3功能丰富且复杂的上下文策略，让笔者花了2个小时用于修改chat_teamplate。这里笔者不赘述如何修改chat_template，感兴趣的读者可以去文末代码链接寻找`chat_template.jinja`文件，笔者专门将chat_template模版拿出来，并且做了格式化方便读者阅读。未来有时间了笔者专门写一篇模型上下文控制与jinja语言的博客。

##### 第二处改动：替换SmolVLM2的SmolLM2模型为Qwen3-0.6B

替换模型这块没什么复杂的，主要是需要处理Transformers比较复杂的嵌套逻辑。Tranformers通常建议模型将预训练模型backbone和下游任务分开来。改动逻辑图如下：



![change_model](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/change_model.png)
  替换smolvlm2的文本模块和语言模型头



以Qwen3为例，预训练Backbone模型为`Qwen3Model`，仅仅包含embedding层、各个Decoder层，最后输出的是所有输入token的hidden state。负责下游任务的Qwen3提供了包括：用于因果语言序列生成的`Qwen3ForCausalLM`，也就是大家常用的语言生成。负责句子分类`Qwen3ForSequenceClassification`，使用最后一个生成的token输入到一个单层MLP做序列级分类，做句子情绪分类等可以用这个下游模型；`Qwen3ForTokenClassification`用于做Token级分类，比如语言实体抽取任务可以使用这个下游模型。`Qwen3ForQuestionAnswering`则是专门做抽取式问答任务的模型，核心思想是输入（问题，参考文本）让模型从参考文本中找到与问题最相关的一段，这类任务由于RAG系统的出现没那么流行了，未来笔者专门出一个系列的教程阐述除了因果语言序列生成以外的任务则怎么微调。

**关键代码如下**

```python
from transformers import (
    AutoProcessor,
    AutoModelForImageTextToText,
    AutoTokenizer,
    AutoModelForCausalLM
)

# 替换text模型和head
smolvlm2_02B_model = AutoModelForImageTextToText.from_pretrained(
    "model/SmolVLM2-256M-Video-Instruct",
    torch_dtype=torch.bfloat16,
    _attn_implementation="eager",
).to(device)

qwen3_06b_model = AutoModelForCausalLM.from_pretrained(
    "model/Qwen3-0.6B", torch_dtype=torch.bfloat16
).to(device)

smolvlm2_02B_model.model.text_model = qwen3_06b_model.model
smolvlm2_02B_model.lm_head = qwen3_06b_model.lm_head
...
```

接下来比较复杂的是替换所有的关键变量，比如模型内用于在文本序列中为图像特征预留的占位符`image_token_id`，用于指示停止生成的`eos_token_id`，和计算loss值会用到的`vocab_size`，Qwen的词表大小为151936，远远大过SmolVLM2的词表49280。具体代码如下：

```python
...
# 替换词表大小
smolvlm2_02B_model.vocab_size = qwen3_06b_model.vocab_size
smolvlm2_02B_model.model.vocab_size = qwen3_06b_model.vocab_size
smolvlm2_02B_model.config.vocab_size = qwen3_06b_model.vocab_size
smolvlm2_02B_model.config.text_config.vocab_size = qwen3_06b_model.vocab_size
smolvlm2_02B_model.model.config.vocab_siz = qwen3_06b_model.vocab_size
smolvlm2_02B_model.model.config.text_config.vocab_size = qwen3_06b_model.vocab_size
# 替换图像token
smolvlm2_02B_model.image_token_id = 151655
smolvlm2_02B_model.model.image_token_id = 151655
smolvlm2_02B_model.config.image_token_id = 151655
smolvlm2_02B_model.model.config.image_token_id = 151655
# 替换模型生成停止符
smolvlm2_02B_model.generation_config.eos_token_id = 151645
···
```

上面的代码可以看到在替换各个变量时需要将嵌套模型的变量一起替换掉，笔者之前训练时就因为仅仅替换了`SmolVLMForConditionalGeneration`而忘记替换`SmolVLMModel`中的`image_token_id`，导致语言模型接收不到图像特征，最后表现出来就是loss下降的极快且低，grad_norm看起来也学到位了，一推理效果特别差，附上错误训练的损失图：



![fail_train](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/fail_train.png)
  SwanLab记录训练结果展示：蓝色为错误训练的完整微调loss图，可以看到损失下降很快，然而实际推理会发现模型并没有图像理解能力。冻结语言模型头（红色）后发现grad_norm为零且loss不收敛，正确的应该是黄色



笔者最早没发现改动错误，先做完整微调（蓝色曲线）后发现损失下降很快达到了0.1以下，结果实际一推理发现模型完全没有图像理解能力，就补了一个冻结语言模型只微调视觉模型的实验（红色曲线），结果发现损失完全没下降，才定位到了视觉特征传入有问题。后续修复后正确的损失下降过程见黄色图像。

##### 第三处改动：构建和替换特征映射层

这个相对较简单，只需要重新构建一个维度对齐的`SmolVLMConnector`即可。Qwen3的hidden_dim是1024，SigLip的hidden_dim是768，因此构建一个768➡️1024映射的`SmolVLMConnector`即可。代码如下：

```python
···
# 构建配置并且创建连接器
@dataclass
class VisionConfig:
    hidden_size: int = 768

@dataclass
class TextConfig:
    hidden_size: int = 1024

@dataclass
class ConnectConfig:
    scale_factor: int = 4
    vision_config: VisionConfig = VisionConfig()
    text_config: TextConfig = TextConfig()

new_connector_config = ConnectConfig()

# 替换 SigLit 到 LLM 的 connector 层
new_connector = SmolVLMConnector(new_connector_config).to(device).to(torch.bfloat16)
smolvlm2_02B_model.model.connector = new_connector
···
```

#### 微调数据集构建

笔者最初计划寻找中文多模态数据集，但发现相关的资料比较少。因此决定先用英文的多模态数据集凑合一下。之后再考虑通过数据合成的方式将部分数据翻译为中文。关于数据合成和配比的问题将在之后的博客讨论。



![the_cauldron](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/the_cauldron.png)
  the_cauldron数据集logo



这里为了方便本项目直接使用HuggingFace团队整合的多模态数据集the Cauldron数据集，Cauldron翻译成中文类似于煮东西的“釜”，不知道HF团队是不是玩“炼丹”的梗。这个数据集整合了50个视觉微调任务数据集的训练集，用于微调Huggingface发布的多模态模型Idefics2模型。这50多个数据集都被处理成了一致的格式（见下图），共有1,880,992条数据，完整下载约169G，非常方便使用。



![data_show](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/data_show.png)
  数据集样本展示



不过可惜数据集的文本都是英文内容，且绝大多数数据集的回复非常短，只有一个词，这也给后面模型训练带来了麻烦。本篇博客暂时不讨论关于数据构建和配比的问题，后续有时间了专门做相关的实验。本博客先以为Qwen3模型带来视觉能力为核心目标。

数据集的下载链接如下，国内推荐用modelscope下载：

* [HuggingFace Hub](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron)
* [ModelScope](https://modelscope.cn/datasets/AI-ModelScope/the_cauldron)

笔者在实际测试时发现"mimic_cgd"，"localized_narratives"，"okvqa"，"ocrvqa"，"clevr_math"这几个子数据集加载有点异常，建议使用此数据集训练的读者手动处理下，社区也有用户反馈这几个数据可以在原始来源处额外下载，未来笔者将会补全这几个数据集重新上传一次完整版的the Cauldron数据集。

#### 微调方法与代码实现

##### 冻结模型参数微调

整体微调方法采用了CLM模型通常的Teacher Forcing的学习方法，损失就是标准的交叉熵损失。考虑到此次本教程的目标是先确保模型具备中文多模态能力（优化模型性能等之后撰写其他博客），因此为了实验效率，在对齐微调阶段**采用冻结视觉模型与文本模型，仅微调特征映射器和语言模型头**的方法。

冻结模型参数的核心代码如下：

```python
def freeze_model(qwen_smvl):
    for _, param in qwen_smvl.model.text_model.named_parameters():
        param.requires_grad = False
    for _, param in qwen_smvl.model.vision_model.named_parameters():
        param.requires_grad = False
    return qwen_smvl
```

冻结后训练参数、模型总参数、与占比如下：

```txt
trainable params: 12.00M || all params: 662.87M || trainable%: 1.81
```

##### 文本长度，损失掩码和截断策略

**文本长度**

由于视觉特征需要占据大量的文本长度，笔者简单测试了下the_cauldron图像占0.8K到1.3K左右的token。而数据集中大多数文本token数在200-500左右，极少情况会有3-4K的情况。因此笔者统一采用2K的文本长度，超出部分截断处理。

这里有一个不同于文本微调的细节要注意，文本截断长度不能小于图像token，否则会导致模型在进行特征拼接时报错（当然图像特征如果被截断了，这条训练数据也就没意义了）。因此对于显存不足64G的同学如果需要适当缩短文本长度（不建议低于1.5K），最好连同图像分辨率也缩小些。在后面的博客我们会专门增加对减少图片token占用的研究。

同样由于文本长度受限，且图像特征没法截断，我们也没使用“packing dataset”的方法提升模型的训练效率。

考虑到部分数据集存在多张图片的情况，考虑到本次训练仅采用2k的文本长度（与之对比HF在训练SmolVLM-256M版本采用的是8K的文本长度，2.2B版使用了16K的文本长度）。针对单条数据中存在多张图片的情况仅仅选用第一张。

**损失掩码**

在采用Teacher Forcing的学习方法时，文本微调中损失掩码有两种策略：

* 对包含“用户问题”和“模型回复”的完整文本进行微调优化
* 仅对“模型回复”部分进行微调优化

这两种策略的对比如下图：



![mask](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/mask.png)
  两种微调掩码策略的差异，通常建议选择“仅微调模型回答部分”以增强泛化性



通常来说使用“仅微调模型回复部分”的策略模型更容易泛化（这点与HF在SmolVLM2的论文提到的trick）。然而笔者为了提高训练效率选择了完整文本微调。可以在后续博客中增加消融实验做进一步对比。

值得注意的是，在进行完整文本微调时，需要单独屏蔽Image Token以防止对图像占位token计算损失，影响模型表现。

**关键代码如下：**

```python
def data_collate_fix2k(examples, processor, device, max_length=2048):
    batch_text = []
    batch_image = []
    for example in examples:
        images = example["images"][:1]  # 只允许一张图，不然显存压力太大
        batch_image.append(images)
        image_num = len(images)
        chat_texts = example["texts"][0]
        messages = [
            {
                "role": "user",
                "content": [{"type": "image"}] * image_num
                + [{"type": "text", "text": chat_texts["user"]}],
            },
            {
                "role": "assistant",
                "content": [{"type": "text", "text": chat_texts["assistant"]}],
            },
        ]
        text = processor.apply_chat_template(
            messages, enable_thinking=False, add_generation_prompt=False
        )

        batch_text.append(text)

    batch = processor(
        text=batch_text,
        images=batch_image,
        max_length=max_length,
        return_tensors="pt",
        padding="max_length",
        truncation=True,
    )
    labels = batch["input_ids"].clone()
    labels[labels == processor.tokenizer.pad_token_id] = -100
    labels[labels == processor.image_token_id] = -100
    batch["labels"] = labels
    return batch.to(device, dtype=torch.bfloat16)
```

##### 微调超参数设置

**学习率**

由于仅仅针对特征映射层（connector）进行训练，且conntector由于要对齐Qwen3的维度因此参数为随机初始化（理论上可以采用一些独特的初始化策略提升性能，但考虑到模型较小因此笔者没关注初始化策略）。因此学习率设置为lora中较为流行的1e-4学习率策略。

为了保障有效收敛，学习率衰减基本是必备的trick，采用的是社区比较流行的cosine学习率衰减，衰减至0。warm up为整体步长的10%（在超过1000k step的情况下固定为50）。

**batch size**

Batch size通常来说越大越好，然而由于VLM模型的文本长度太大，因此采用每卡1 batch和4梯度累加（grad accelerate），在8卡训练中等效32 Batch size。

**训练参数设置代码**

```python
training_args = TrainingArguments(
    seed=42,
    data_seed=42,
    max_steps=200,
    # num_train_epochs=1,  # 训练1个epoch 约1k steps
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    dataloader_pin_memory=False,
    warmup_ratio=0.1,
    learning_rate=1e-4,
    lr_scheduler_type="cosine",
    weight_decay=0.01,
    logging_steps=5,
    eval_strategy="steps",
    eval_steps=0.125,
    save_strategy="steps",
    save_steps=0.125,
    save_total_limit=8,
    optim="adamw_torch",
    bf16=True,
    output_dir=f"./model/freeze_except_connector_cocovqa",
    overwrite_output_dir=False,
    report_to="swanlab",
    run_name="freeze_except_connector_cocovqa",
    remove_unused_columns=False,
    gradient_checkpointing=False,
)
```

##### 训练环境

微调代码基于沐曦的C500国产通用计算GPU实现，显存为64G。沐曦的AI芯片基本完全兼容pytorch和huggingface transformers场景，并且在做多模态训练时相比较其他国产AI芯片罕见的没有兼容性问题。读者在尝试本项目代码时可以采用Nvidia显存40G以上的显卡运行本教程。

**笔者个人感觉沐曦的GPU整体适配效果还是非常好的，没遇到适配性的问题。体验上和用NV的GPU做训练没什么区别**。笔者自己也用过好几款国产GPU，沐曦的体验肯定是名列前茅的，包括代码中有指定flash attention在沐曦GPU上都能成功迁移，这点非常值得给沐曦团队点个赞。希望国产GPU生态能越发展越好，造福广大炼丹师；）。



![muxi-gpu](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/muxi-gpu.jpg)
  沐曦国产GPU，笔者用的云端服务器没见过真机，因此找了张网图



训练环境的话除了安装GPU对应的驱动和pytorch外，本教程需要额外安装Huggingface全家桶，如下：

```txt
torch   # 推荐版本>=6.0
torchvision
transformers>=4.53.0
accelerate
datasets
num2words   # SmolVLM2需要
```

额外补充一句，如果采用沐曦GPU训练的话，需要在沐曦官方文档处寻找[沐曦版torch](https://developer.metax-tech.com/softnova/index)的安装方式进行下载。其他HF环境和NV基本一样。附赠一个沐曦查看GPU的命令：

```bash
mx-smi
```

效果如下：

```bash
=================== MetaX System Management Interface Log ===================
Timestamp                                         : Sat Jul 12 14:58:51 2025

Attached GPUs                                     : 8
+---------------------------------------------------------------------------------+
| MX-SMI 2.1.12                       Kernel Mode Driver Version: 2.12.13         |
| MACA Version: 2.29.0.19             BIOS Version: 1.22.3.0                      |
|------------------------------------+---------------------+----------------------+
| GPU         NAME                   | Bus-id              | GPU-Util             |
| Temp        Pwr:Usage/Cap          | Memory-Usage        |                      |
|====================================+=====================+======================|
| 0           MetaX C500             | 0000:0e:00.0        | 0%                   |
| 36C         69W / 350W             | 5680/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+
| 1           MetaX C500             | 0000:0f:00.0        | 0%                   |
| 38C         70W / 350W             | 4986/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+
| 2           MetaX C500             | 0000:10:00.0        | 0%                   |
| 37C         69W / 350W             | 4986/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+
| 3           MetaX C500             | 0000:12:00.0        | 1%                   |
| 37C         71W / 350W             | 4986/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+
| 4           MetaX C500             | 0000:35:00.0        | 0%                   |
| 37C         70W / 350W             | 4986/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+
| 5           MetaX C500             | 0000:36:00.0        | 1%                   |
| 36C         68W / 350W             | 4986/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+
| 6           MetaX C500             | 0000:37:00.0        | 0%                   |
| 39C         73W / 350W             | 4986/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+
| 7           MetaX C500             | 0000:38:00.0        | 0%                   |
| 38C         71W / 350W             | 4986/65536 MiB      |                      |
+------------------------------------+---------------------+----------------------+

+---------------------------------------------------------------------------------+
| Process:                                                                        |
|  GPU                    PID         Process Name                 GPU Memory     |
|                                                                  Usage(MiB)     |
|=================================================================================|
|  0                  3496691         python3.10                   4066           |
|  0                  3496692         python3.10                   102            |
|  0                  3496693         python3.10                   102            |
|  0                  3496694         python3.10                   102            |
|  0                  3496695         python3.10                   102            |
|  0                  3496696         python3.10                   102            |
|  0                  3496697         python3.10                   102            |
|  0                  3496698         python3.10                   170            |
|  1                  3496692         python3.10                   4154           |
|  2                  3496693         python3.10                   4154           |
|  3                  3496694         python3.10                   4154           |
|  4                  3496695         python3.10                   4154           |
|  5                  3496696         python3.10                   4154           |
|  6                  3496697         python3.10                   4154           |
|  7                  3496698         python3.10                   4154           |
+---------------------------------------------------------------------------------+
```

##### 训练代码实现

在构建训练代码时，笔者使用HuggingFace Transfomers框架的Trainer类来完成训练代码。Trainer类实现的训练逻辑基本能完成大部分微调任务。这里唯一需要提到的是笔者使用了Qwen3-0.6B而非通常此类任务该使用的Qwen3-0.6B-Base模型，Qwen3-0.6B相比于Qwen3-0.6B-Base模型经过了指令遵从微调、对齐等，能实现聊天问答功能。

通常来说对经过微调的模型进行持续训练会一定程度带来性能损失，然而此次微调时笔者冻结了LLM参数，因此需要选用经过微调的模型来实现多模态问答能力。

笔者在训练过程中使用的是bfloat16精度，相比于float16来说bfloat16增加了尾数位数，训练过程中精度会更高些。

在前期进行方案验证阶段笔者采用的是cocoqa数据集，并且进行200steps的微调训练。在确定方案可行后笔者计划使用完整数据集进行微调训练，然而考虑到训练数据量仅仅只有整个模型的12M，因此笔者按参数量与训练Token的比值为1:10采样数据集，即总共从数据集中采样出60K条数据用于实际训练（文本长度按照2k计算，实际上有padding部分因此实际参与token数小于120M）。笔者认为参与训练的数量是足以令模型收敛的，后续实验也证明了模型确实能达到我们所期望的效果。

**训练关键代码实现**

代码比较长是因为增加了断点续训的能力

```python
################
# 开启训练
################
last_checkpoint = None  # load last checkpoint if available
if (
    os.path.isdir(training_args.output_dir)
    and not training_args.overwrite_output_dir
):
    last_checkpoint = get_last_checkpoint(training_args.output_dir)
    if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
        raise ValueError(
            f"Output directory ({training_args.output_dir}) already exists"
        )
    print(
        f"Checkpoint detected, resuming training at {last_checkpoint}."
    )
# Init Trainer
trainer = Trainer(
    model=qwen_smvl,
    args=training_args,
    train_dataset=raw_data["train"],
    eval_dataset=raw_data["test"],
    data_collator=collate_fn,
)
trainer.train(resume_from_checkpoint=last_checkpoint)
qwen_smvl.save_pretrained(training_args.output_dir)
```

完整代码见[代码及数据集链接汇总](#代码及数据集链接汇总)

或者直接由[完整项目GitHub地址]()

#### 微调训练&结果展示

##### 环境安装与微调代码执行

**代码准备与环境安装**

可以在[GitHub仓库地址](https://github.com/ShaohonChen/Qwen3-SmVL)处找到实验的完整代码。使用git clone后使用如下命令安装环境

```bash
pip install -r requirements.txt
```

**数据集和模型下载**

笔者附上自动下载脚本，注意该脚本使用[魔塔社区](https://modelscope.cn/)完成模型与数据集的下载

```bash
bash download_resource.sh
```

##### 小批量微调训练

为了进行快速验证，笔者首先使用cocoqa数据集并且进行了200steps的训练，所有参数与前文所述一致。通过

运行实验命令如下，推荐使用8卡进行训练，在8张沐曦GPU卡上预计需要使用20min

```bash
# 单GPU训练
CUDA_VISIBLE_DEVICES=0 python train.py ./cocoqa_train.yaml
# 8GPU训练
accelerate launch --num_process 8 train.py ./cocoqa_train.yaml
```

注意，本项目使用SwanLab进行训练日志记录与分析，如果未登陆SwanLab需要使用`swanlab login`进行登陆。运行后看到如下结果即代表实验成功开启：



![run](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/run.png)
  成功训练后可以看到SwanLab链接



下面是笔者完成小批量微调训练的训练损失、测试损失结果图



![cocoqa_swanlab](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/cocoqa_swanlab.png)
  SwanLab训练可视化分析结果，可以看到最后训练损失和测试损失都收敛在0.65左右



模型在完成训练后会自动使用一张狗狗图片配合问题“图中有什么动物？”让模型根据图片进行推理，推理结果如下：



![bad_case](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/bad_case.png)
  SwanLab记录了模型训练好后的推理结果，可以看到模型能正常理解和回复中文



当时看到模型对着三只狗的图片回答“兔子”时笔者一时认为炼丹失败了，当然如果实际炼丹失败后模型是不会输出动物类型的，而是输出一些乱码或者告诉用户并没有看到图片。识别错误的原因实际上是由于训练步数过少导致的。后续加大训练步数与数据量后模型能正常识别出狗狗并且能准确的说出有三只狗。



![dog](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/dog.png)
  附上三只眼神忧伤的狗子，难道长得很像兔子吗？



PS: 作者公开了在[SwanLab上的训练结果](https://swanlab.cn/@ShaohonChen/Qwen3-SmVL/overview)，感兴趣的读者可以自己查看，SwanLab也支持Clone作者的训练日志，大家可以在自己训练时clone笔者的项目去做对照。

##### 完整微调训练结果展示

运行实验命令如下，推荐使用8卡进行训练，在8片沐曦C500芯片上预计需要使用1.5h

```bash
# 单GPU训练
CUDA_VISIBLE_DEVICES=0 python train.py ./full_train.yaml
# 8GPU训练
accelerate launch --num_processes 8 train.py ./full_train.yaml
```

下图展示了使用完整微调数据对比于小批量训练，可以看到全量数据微调时loss变得更为抖动，这是由于数据类型的丰富给模型的学习带来了一定的挑战。



![fulldata_swanlab](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/fulldata_swanlab.png)
  红色为完整训练loss，黄色为小批量训练结果



进一步对比完整训练和小批量训练的训练和测试损失，可以看到完整训练的模型训练损失达到了0.61，远低于仅仅使用cocoqa模型的效果，评估损失也远低于前者，维持在0.58左右。



![evalloss](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/evalloss.png)
  红色为完整训练loss，黄色为小批量训练结果



这里值得一提的是，由于我们选用的测试集比较小（仅有64条数据），因此训练损失和测试损失的差距并不能直接理解为过拟合的证据。实际上在大模型训练上，如果数据集足够大的情况下，通常可以认为训练损失等同于评估损失。

此外，模型通过分析1k步之后的训练损失、平均梯度范数（Grad Norm）变化。此时训练任务已过半，且学习率开始快速衰减。如下图，可以看到学习率快速衰减的情况下模型损失并没有明显的进一步下降，这说明模型已经实现了充分训练。



![1kstep](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/1kstep.png)
  1k step之后模型的训练损失变化



在训练效率方面，可以看到我们仍没有充分榨干沐曦GPU的性能，当然这也是由于多模态任务的网络本身架构上比较复杂，其中包含许多对图像、文本的拼接工作，这也导致了GPU性能没法完全利用。



![mx-gpu-use](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/mx-gpu-use.png)
  SwanLab对沐曦C500训效率自动记录



同样在完成训练后使用狗狗图进行了测试，这次模型能理解图片、中文以及给出正确的回复。更为关键的是模型完全保留了Qwen3-0.6B原有的全部能力，包括函数调用、推理等。在此基础上，仅仅增加了0.09B参数量的情况下为模型带来了图像理解能力！



![good_case](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/vlm-concatenation-finetune/images/good_case.png)
  同样的图片与问题，更大的数据量和更充足的数据使得模型能够正确给出回复



##### 模型推理与效果分析

等笔者下完数据集后未来补一下测试环节 ; ）

可以关注[swanlab教程集合](https://docs.swanlab.cn/examples/qwen3_smolvlm_muxi.html)获取最新更新教程！

#### 代码及数据集链接汇总

微调用The Cauldron数据集下载链接：

* HuggingFace Hub: [https://huggingface.co/datasets/HuggingFaceM4/the_cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron)
* ModelScope: [https://modelscope.cn/datasets/AI-ModelScope/the_cauldron](https://modelscope.cn/datasets/AI-ModelScope/the_cauldron)

Qwen3-0.6B模型下载：

* HuggingFace Hub: [https://huggingface.co/Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)
* ModelScope: [https://modelscope.cn/Qwen/Qwen3-0.6B](https://modelscope.cn/Qwen/Qwen3-0.6B)

本实验完整代码GitHub链接：

* 完整项目GitHub地址：[https://github.com/ShaohonChen/Qwen3-SmVL](https://github.com/ShaohonChen/Qwen3-SmVL)

本实验SwanLab日志：

* SwanLab训练过程查看：[https://swanlab.cn/@ShaohonChen/Qwen3-SmVL/overview](https://swanlab.cn/@ShaohonChen/Qwen3-SmVL/overview)

#### 参考资料

* Huggingface SmolVLM2技术报告：[https://arxiv.org/pdf/2504.05299](https://arxiv.org/pdf/2504.05299)

### S1：使用 vLLM 管理思考预算

首先，我们来了解一下AI教母李飞飞教授关于 Test-time scaling 的论文：[*《s1: Simple test-time scaling》*](http://arxiv.org/abs/2501.19393)


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/images/image-1.png)


论文大致讲了个什么事情呢？简单来说，提出了一种新的测试时间缩放方法，旨在提高模型在推理阶段的效率和准确性。通过调整模型的思考预算，可以在不同的任务和数据集上实现更好的性能。

就是说对于一些复杂问题，需要用推理链来解决的问题，我们可以通过调整模型的思考预算来提高推理效率和准确性。上图也可以看到当思考预算增加时，模型的性能会有明显提升。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/images/image-2.png)


插一句题外话，论文中判断问题难易程度的方式是通过让 Qwen2.5-32B-Instruct 模型回答问题，答对的问题就是简单问题，答错的就是复杂问题。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/images/image-3.png)



论文也做了消融实验来探讨，在未满足思考预算时插入一些不同的特定词（如：Wait！）对模型最终性能的影响。结果表明，插入特定词可以有效地引导模型进行更深入的思考，并且“Wait，Wait”的效果最好。

#### 代码实现

我们使用 vLLM 来实现模型的思考预算。vLLM 是一个高性能的推理引擎，支持大规模语言模型的高效推理。以下为代码实现的步骤：

> 考虑到部分同学配置环境可能会遇到一些问题，我们在 ucloud 平台准备了环境镜像，点击下方链接并直接创建 ucloud 示例即可。 https://www.compshare.cn/images/8gfTTB5y0ql6?referral_code=ELukJdQS3vvCwYIfgsQf2C


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/images/thinking-budget.png)


左侧为不使用思考预算的推理过程，右侧为使用思考预算的推理过程。可以看到，使用思考预算后，模型会在推理过程中插入特定词来引导模型进行更深入的思考。

以下为核心代码实现，完整代码请参考 [*s1.py*](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/s1.py)

```python
def run_thinking_budget_sample(llm_model, tokenizer, user_input, thinking_budget):
    input_text = build_input(user_input, tokenizer)
    input_token_count = count_token(input_text, tokenizer)

    iteration_count= 0
    max_token = input_token_count + thinking_budget

    sampling_params = SamplingParams(
        temperature=0.7,
        max_tokens=4096,
        skip_special_tokens=False
    )

    think_token_count = 0

    while True:

        wait_sampling_params = SamplingParams(
            temperature=0.7,
            max_tokens=thinking_budget - think_token_count,
            stop='</think>',
            skip_special_tokens=False
        )

        outputs = llm_model.generate(
            input_text,
            wait_sampling_params
        )
        total_token, think_token_count = count_thinking_token(outputs, tokenizer)

        print(f'第{iteration_count}次迭代，思考token数：{think_token_count}')

        if think_token_count > thinking_budget:
            break
        input_text = total_token + "\nWait!\n"

        # \nWait a moment. Was there any loophole in my thought just now?!\n
        # \nWait!\n

        iteration_count += 1

    final_outputs = llm_model.generate(
        outputs[0].prompt + outputs[0].outputs[0].text + "\n</think>\n",
        sampling_params
    )

    total_content = final_outputs[0].prompt + final_outputs[0].outputs[0].text
    thinking_content = total_content.split("<think>")[-1].split("</think>")[0]

    print(total_content)

    print(f"迭代次数：{iteration_count}, 输入token数：{input_token_count}, 思考token数：{count_token(thinking_content, tokenizer)}, 总token数：{count_token(total_content, tokenizer)}")
```

首先是要定义一个函数 `run_thinking_budget_sample`，该函数接收模型、tokenizer、用户输入和思考预算作为参数。然后构建输入文本并计算输入的 token 数量。

因为`max_tokens` 参数是指生成的最大 token 数量，所以我们需要计算输入文本的 token 数量，并将其与思考预算相加，得到 `max_token = thinking_budget - think_token_count`。如果思考 token 数量超过了思考预算，就停止迭代。另外还需要在 `SamplingParams` 中设置 `stop` 参数为 `</think>`，这样模型在生成文本时会在遇到 `</think>` 时停止生成。

```python
wait_sampling_params = SamplingParams(
    temperature=0.7,
    max_tokens=thinking_budget - think_token_count,
    stop='</think>',
    skip_special_tokens=False
)
```

另外还需要在每次迭代中，使用 `llm_model.generate` 方法生成文本，并计算思考 token 数量。如果思考 token 数量超过了思考预算，就停止迭代。否则，将生成的文本添加到输入文本中，并在文本末尾添加 `\nWait!\n`，以引导模型进行更深入的思考。

```python
while True:
    wait_sampling_params = SamplingParams(
        temperature=0.7,
        max_tokens=thinking_budget - think_token_count,
        stop='</think>',
        skip_special_tokens=False
    )

    outputs = llm_model.generate(
        input_text,
        wait_sampling_params
    )
    total_token, think_token_count = count_thinking_token(outputs, tokenizer)

    print(f'第{iteration_count}次迭代，思考token数：{think_token_count}')

    if think_token_count > thinking_budget:
        break
    input_text = total_token + "\nWait!\n"

    # \nWait a moment. Was there any loophole in my thought just now?!\n
    # \nWait!\n

    iteration_count += 1
```

当达到思考预算后，使用 `llm_model.generate` 方法生成最终的输出文本，并将其打印出来。最后输出迭代次数、输入 token 数量、思考 token 数量和总 token 数量。

```python
final_outputs = llm_model.generate(
    outputs[0].prompt + outputs[0].outputs[0].text + "\n</think>\n",
    sampling_params
)

total_content = final_outputs[0].prompt + final_outputs[0].outputs[0].text
thinking_content = total_content.split("<think>")[-1].split("</think>")[0]

print(total_content)

print(f"迭代次数：{iteration_count}, 输入token数：{input_token_count}, 思考token数：{count_token(thinking_content, tokenizer)}, 总token数：{count_token(total_content, tokenizer)}")
```

此时我们还需要另外一个 `SamplingParams` 对象来设置最终生成文本的参数。`max_tokens` 参数设置为 4096，模型根据思考过程进行总结最后得出答案，这个过程也需要很多tokn，此时设置为多少都可以，通常设置为一个较大的值即可。

```python
sampling_params = SamplingParams(
    temperature=0.7,
    max_tokens=4096,
    skip_special_tokens=False
)
```

以上为核心代码实现，完整代码请参考 [*s1.py*](https://github.com/datawhalechina/happy-llm/blob/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/s1.py)。在实际使用中，可以根据具体的任务和数据集调整思考预算和其他参数，以获得更好的性能。

#### 结果分析

使用思考预算后，模型在推理过程中能够更深入地思考问题，从而提高了推理效率和准确性。但是也发现了一些有趣的现象。

例如，在某些情况下，就算插入了`Wait!`，模型并不会按照论文中所示进行多种不同方式尝试解答，或是反思之前的思考过程是否正确。而且还会出现模型在思考过程中重复生成相同的内容，导致思考 token 数量超过思考预算的情况。


![alt text](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/images/image-4.png)


当然，也有可能本身测试的模型只有14B参数，导致其在思考过程中的能力受到限制。

经过测试下来，有可能强行使用特定词（如：Wait!）来引导模型进行更深入的思考，可能会促使模型产生 “一条道走到黑” 的想法。

部分实验测试记录在 [*output*](https://github.com/datawhalechina/happy-llm/tree/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/s1-vllm-thinking-budget/output) 中。

### CDDRS：细粒度语义信息增强 RAG 检索

一个从零开始实现的建筑文档智能审查系统，旨在帮助开发者理解知识引导检索在专业领域文档审查中的核心原理和实现细节。

#### 项目动机

建筑施工交底文档的合规性审查是保障施工项目安全性、经济性的关键环节。在施工项目全周期中，各项操作必须符合相关规范条文要求，才能确保建设项目的安全性与可持续性。然而，相关查询参考往往分散在各个项目文件中，传统基于人工的审查方法难以处理庞大复杂的建筑条文，其审查过程需要基于审查人员的经验与专业知识，具有主观性强，耗时长且易出错等弊端。

随着大语言模型技术的发展，LLM为自动化建筑文档审查带来了新的希望。然而，大语言模型通常使用通用语料进行训练，缺乏建筑相关背景知识，在处理建造背景下的复杂推理问题中会产生严重的幻觉现象。通过使用基于向量相似匹配的RAG方法，可以为LLMs提供初步的相似参考知识，从而减轻基于人工或规则的审查方法难以处理庞大建筑文本所带来的错误率高的问题。

然而，传统RAG方法在建筑专业文档审查中存在关键局限：由于固定的分块设计，使得文本块之间面临知识信息缺失问题；在检索过程中，使用整句问询嵌入的方法进行相似性匹配，缺少对问询细粒度特征的识别与考量，检索效率低下。在建筑施工交底文档中，这类文档详细阐述了施工工艺特点和方法、质量规格、操作程序以及安全协议，包含大量知识细节且专业性极强。因此需要一个能够精准理解和检索建筑领域专业知识的智能系统。

因此，本项目提出了一个生成式知识引导的建筑文档审查系统，旨在提升审查的可靠性和准确性。系统具有两大核心创新：首先提出动态语义知识分块策略，构建具有更优语义连贯性和完整性的知识库；其次基于增强的知识表示，提出生成式知识引导检索框架，在语义嵌入检索过程中增强对细粒度信息的关注，从而提高知识参考检索的准确性和建筑文档审查任务中修正的可靠性。

需要注意的是，由于篇幅限制，我们无法展示完整的整个实现过程，但是，我们将在文档中讲解每个必要的实现步骤以及背后的思考，您可以通过这些内容快速理解如何实现一个建筑文档智能审查系统。

#### 前置实现

接下来，我们将带领大家，从0开始，实现一个建筑文档智能审查系统。首先，我们将完成一些基本的准备过程。

##### 1. 实现 LLM 模块

首先我们需要实现 LLM 模块，这是系统中最基本的模块，我们将利用大模型完成文档的清洗，信息提取等工作，可以说本系统的一部分精髓即为使用大模型预先处理文档信息，方便后续进行检索，这里我们使用 DeepSeek 的 api 来实现。

```python
from abc import ABC, abstractmethod
from typing import Any, Optional

class BaseLLM(ABC):
    """Interface for large language models."""

    def __init__(
        self,
        model_name: str,
        model_params: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        self.model_name = model_name
        self.model_params = model_params or {}

    @abstractmethod
    def predict(self, input: str) -> str:
        """Sends a text input to the LLM and retrieves a response."""
```

如上是一个调用大模型的抽象接口，这可以帮助我们统一调用大模型的格式，我们继承这个基类，实现调用大模型的接口。

```python
from openai import OpenAI
from typing import Any, Optional
from .base import BaseLLM

class DeepSeekLLM(BaseLLM):
    """Implementation of the BaseLLM interface using DeepSeek API."""

    def __init__(
        self,
        model_name: str,
        api_key: str,
        base_url: str = "https://api.deepseek.com/v1",
        model_params: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        super().__init__(model_name, model_params, **kwargs)
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def predict(self, input: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": input}],
        )
        return response.choices[0].message.content
```

完成搭建后，我们可以通过尝试调用 predict 方法来测试是否成功。

```python
llm = DeepSeekLLM(
    model_name="deepseek-chat",
    api_key="your-api-key-here",
    base_url="https://api.deepseek.com/v1"
)
print(llm.predict("你好，你能帮助我进行建筑文档审查吗？"))
```

当观察到 LLM 正确回复后，我们这一模块的构建就完成了。

##### 2. 实现 Embedding 模块

除了调用大模型，我们还需要实现 Embedding 模块，Embedding 模块用于将文本转换为向量，我们将使用向量来表示文档中的信息，这样的好处是，我们可以通过向量的相似度来衡量文档与查询之间的相似度，从而召回对回复用户问题最有帮助的文档。

构建 Embedding 模块的方法与构建 LLM 模块类似。

```python
from abc import ABC, abstractmethod
from typing import List, Any, Optional

class BaseEmb(ABC):
    def __init__(
        self,
        model_name: str,
        model_params: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ):
        self.model_name = model_name
        self.model_params = model_params or {}

    @abstractmethod
    def get_emb(self, input: str) -> List[float]:
        """Sends a text input to the embedding model and retrieves the embedding."""
        pass

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from .base import BaseEmb

class BGEEmbedding(BaseEmb):
    def __init__(self, model_name: str = "BAAI/bge-m3", **kwargs):
        super().__init__(model_name=model_name, **kwargs)
        self.embed_model = HuggingFaceEmbedding(
            model_name=model_name,
            trust_remote_code=True,
            cache_folder="./model_cache"
        )

    def get_emb(self, text: str) -> List[float]:
        embedding = self.embed_model.get_text_embedding(text)
        return embedding
```

完成搭建后，我们可以通过尝试调用 get_emb 方法来测试是否成功。

```python
emb = BGEEmbedding(model_name="BAAI/bge-m3")
print(emb.get_emb("建筑结构的安全性检查包括哪些方面？"))
```

当观察到 Embedding 正确给出了编码后的向量，我们这一模块的构建就完成了。

##### 3. 实现文档预处理模块

为了处理建筑文档，我们需要预先准备好文档读取模块。本系统假设所有建筑规范和标准已经转换为Markdown格式，便于后续的文本处理和分析。

```python
import os
from pathlib import Path
from typing import Dict, List

class DocumentProcessor:
    def __init__(self):
        pass

    def load_documents(self, directory_path: str) -> List[str]:
        documents = []

        for file_path in Path(directory_path).rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append(content)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        return documents
```

完成文档预处理模块的设置后，我们就可以采用下面的方法来加载建筑规范文档了。

```python
processor = DocumentProcessor()
documents = processor.load_documents("./construction_standards")
print(f"加载了 {len(documents)} 个建筑规范文档")
```

#### 核心实现

建筑文档审查系统的主要流程如下。首先，让我们来梳理一下建筑文档审查的工作流程，系统的一个核心思想在于，我们需要把用户提供的文档内容通过智能化的问询生成和知识引导检索来识别潜在的合规性问题。与传统RAG方法不同，我们的系统专门针对建筑领域的专业特点进行了优化，能够更准确地理解建筑规范要求，提供更可靠的审查建议。

##### 动态语义知识分块

在传统RAG流程中，文本通过设置固定的token数量划分文本区块。然而，固定token数量会在句子中间截断，导致信息缺失。为此，本系统使用基于建筑文本语义动态划分的方式，通过双重语义聚类的方式，完成考虑建筑语义连贯性的知识chunk划分。

首先，将整个文档内容处理成单独句子序列 $S = \{s_0, s_1, \ldots, s_a\}$。通过计算相邻句子间的语义差异度来识别潜在的语义边界：

$$\gamma_i = 1 - \frac{s_{i-1} \cdot s_i}{\|s_{i-1}\| \|s_i\|}$$

基于语义差异度分布自动确定动态阈值：

$$\psi = \text{Quantile}(\Gamma, \frac{a-p}{a})$$

确保最终的分块既保持语义连贯性又满足长度约束：

$$\mathbb{E}[\gamma_{\text{intra}}] < \mathbb{E}[\gamma_{\text{inter}}]$$

```python
import re
import numpy as np
from typing import List, Dict, Tuple
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class DynamicSemanticChunker:
    def __init__(self,
                 embedding_model: str = "BAAI/bge-m3",
                 max_chunk_length: int = 512,
                 min_chunk_length: int = 50):
        self.embedding_model = SentenceTransformer(embedding_model)
        self.max_chunk_length = max_chunk_length
        self.min_chunk_length = min_chunk_length

    def split_text(self, text: str) -> Dict[str, str]:
        sentences = self._split_into_sentences(text)
        if len(sentences) == 0:
            return {}

        sentence_embeddings = self.embedding_model.encode(sentences)
        gamma_values = self._compute_semantic_discrepancy(sentence_embeddings)

        total_tokens = sum(len(s.split()) for s in sentences)
        baseline_chunks = max(1, total_tokens // self.max_chunk_length)
        alpha = max(0.1, (len(sentences) - baseline_chunks) / len(sentences))
        threshold = np.quantile(gamma_values, alpha) if len(gamma_values) > 0 else 0.5

        boundaries = self._identify_boundaries(gamma_values, threshold)
        initial_chunks = self._create_initial_chunks(sentences, boundaries)
        final_chunks = self._enforce_length_constraints(initial_chunks)

        chunks_dict = {}
        for i, chunk in enumerate(final_chunks):
            chunk_id = f"chunk-{i+1:03d}"
            chunks_dict[chunk_id] = chunk

        return chunks_dict

    def _split_into_sentences(self, text: str) -> List[str]:
        sentence_pattern = r'[。！？；\n]+'
        sentences = re.split(sentence_pattern, text)

        cleaned_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 5:
                cleaned_sentences.append(sentence)

        return cleaned_sentences

    def _compute_semantic_discrepancy(self, embeddings: np.ndarray) -> List[float]:
        gamma_values = []

        for i in range(1, len(embeddings)):
            similarity = cosine_similarity(
                embeddings[i-1].reshape(1, -1),
                embeddings[i].reshape(1, -1)
            )[0][0]

            gamma = 1 - similarity
            gamma_values.append(gamma)

        return gamma_values

    def _identify_boundaries(self, gamma_values: List[float], threshold: float) -> List[int]:
        boundaries = [0]

        for i, gamma in enumerate(gamma_values):
            if gamma > threshold:
                boundaries.append(i + 1)

        boundaries.append(len(gamma_values) + 1)
        return sorted(set(boundaries))

    def _create_initial_chunks(self, sentences: List[str], boundaries: List[int]) -> List[str]:
        chunks = []

        for i in range(len(boundaries) - 1):
            start = boundaries[i]
            end = boundaries[i + 1]

            chunk_sentences = sentences[start:end]
            chunk_text = ' '.join(chunk_sentences)
            chunks.append(chunk_text)

        return chunks

    def _enforce_length_constraints(self, chunks: List[str]) -> List[str]:
        final_chunks = []

        for chunk in chunks:
            chunk_length = len(chunk.split())

            if chunk_length <= self.max_chunk_length:
                if chunk_length >= self.min_chunk_length:
                    final_chunks.append(chunk)
            else:
                sub_chunks = self._split_long_chunk(chunk)
                final_chunks.extend(sub_chunks)

        return final_chunks

    def _split_long_chunk(self, chunk: str) -> List[str]:
        sentences = chunk.split('。')
        sub_chunks = []
        current_chunk = ""

        for sentence in sentences:
            if sentence.strip():
                test_chunk = current_chunk + sentence + "。"
                if len(test_chunk.split()) <= self.max_chunk_length:
                    current_chunk = test_chunk
                else:
                    if current_chunk:
                        sub_chunks.append(current_chunk.strip())
                    current_chunk = sentence + "。"

        if current_chunk:
            sub_chunks.append(current_chunk.strip())

        return sub_chunks
```

##### 建筑文档审查系统

整体的审查过程如下图所示。系统获取需要审查的区域后，依据提示生成审查问题推荐，此部分也可供工程师进行相关问题输入或推荐问题选择，生成待审查问题。随后，系统通过生成式知识引导检索框架，依据审查问题在所建文本知识库中检索出相应的知识参考。最终，依据检索的部分与审查原文，进行问题分析与审查修正，完成最终的审查流程。

![picture](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/CDDRS/images/pic1.png)

###### 审查问题生成

在文档审查流程中，系统引入了双阶段Prompt工程驱动的智能化问询生成机制，旨在对建筑施工交底文档进行预见性分析与风险挖掘，实现对文档潜在问题的高效、精准定位。

阶段1为待查文档主旨目标解构，模型被指示从文本中提炼核心事件、关键技术、工艺流程等要素，结构化地总结文档的核心内容，由此界定本次审查的靶向目标，为后续的精细化问询奠定基础。阶段2为多维度风险探测与定制化问询生成，基于第一阶段提炼的核心要素，通过few-shot等方式引导 LLM 从合规性、安全性、可操作性等多维度对文档进行风险探测。Prompt 指示模型围绕潜在的限制条件、操作流程、以及可能存在的合规性隐患等方面，进行细粒度、多角度的审查提问。

```python
import re

CORE_COMPONENTS_PROMPT = """
Task: Your task involves the extraction of crucial information components from a designated text segment. The purpose of this extraction is to assist in uncovering hidden descriptions indicative of regulatory non-compliance. Key information components encompass, but are not limited to, core descriptive events, essential construction techniques, technologies, and associated limitations and restrictions.

Input: {document_chunk}
Answer:
"""

REVIEW_QUERIES_PROMPT = """
Task: Your task is to generate relevant search queries based on the text under review and provided core descriptive references. These queries should target potential areas of non-compliance within the text, facilitating the subsequent retrieval of original regulatory documents for detailed examination.

Input: {document_chunk}
Core components: {core_components}
Queries:
"""

def generate_review_queries(llm, document_chunk: str) -> List[str]:
    core_prompt = CORE_COMPONENTS_PROMPT.format(document_chunk=document_chunk)
    core_response = llm.predict(core_prompt)

    # 生成审查查询
    queries_prompt = REVIEW_QUERIES_PROMPT.format(
        document_chunk=document_chunk,
        core_components=core_response
    )
    queries_response = llm.predict(queries_prompt)

    # 从响应中提取查询列表
    queries = re.findall(r"'([^']*)'", queries_response)

    return queries[:5]
```

###### 知识引导生成式检索

系统的核心创新在于知识引导的检索框架，整个过程分为三个关键步骤。步骤1为句子级编码，主要负责输入查询句子的初始表示学习，计算查询与知识库chunks间的句子级相似度分数。步骤2为知识引导检索，进一步从查询中提取关键信息，利用这些信息结合文档长度自适应加权等机制，对每个知识库chunk进行更详细的评分。步骤3为重排序与增强，使用大语言模型对步骤2检索的结果进行进一步重排序，并利用精炼的知识来增强原始查询。
![picture](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/CDDRS/images/pic2.png)

首先建立专门针对建筑领域文本分析的深度提取模块，集成领域预训练BERT进行上下文编码，结合双向LSTM进行建筑法规依赖建模。建立三级重要性分类层次：max（最高）、mid（中等）、lit（字面）优先级。本项目直接通过大语言模型进行关键信息提取，如果需要更精准的效果，可以自行训练BERT模型进行专门的关键信息提取。
![picture](https://raw.githubusercontent.com/datawhalechina/happy-llm/1e0b3a1e6f8936b8ba4bbd0673e8e2227d196c96/Extra-Chapter/CDDRS/images/pic3.png)

```python
import re
from typing import Dict, Tuple, List

KEY_INFO_EXTRACTION_PROMPT = """
Your task is to extract key information from the query with three different priority levels:

Maximum priority (max): The most important core concepts or entities
Medium priority (mid): Important modifiers or qualifying conditions
Literal priority (lit): Specific values, standards or specifications

Query: {query}
max:
mid:
lit:
"""

class KeyInfoExtractor:
    def __init__(self, llm):
        self.llm = llm

    def extract_key_info(self, query: str) -> Dict[str, Tuple[str, float]]:
        prompt = KEY_INFO_EXTRACTION_PROMPT.format(query=query)
        response = self.llm.predict(prompt)

        lines = response.strip().split('\n')
        key_info = {}
        weights = {'max': 0.5, 'mid': 0.3, 'lit': 0.2}

        for line in lines:
            if line.startswith('max:'):
                key_info['max'] = (line[4:].strip(), weights['max'])
            elif line.startswith('mid:'):
                key_info['mid'] = (line[4:].strip(), weights['mid'])
            elif line.startswith('lit:'):
                key_info['lit'] = (line[4:].strip(), weights['lit'])

        return key_info
```

###### 文档长度自适应因子

在知识引导检索过程中，文档长度自适应因子用于调整不同长度文档的权重分配，确保长短文档都能得到公平的评分机会。该因子的计算考虑了当前文档chunk的长度与平均文档长度的关系。

$$\Lambda_{\text{DL}} = \frac{\overline{|k|} + |k_j|}{2\overline{|k|}}$$

其中 $|k_j|$ 表示当前文档chunk的长度，$\overline{|k|}$ 表示平均文档长度。通过这种归一化处理，可以避免因文档长度差异导致的评分偏差。

```python
def compute_document_length_factor(chunk_length: int, avg_length: int = 100) -> float:
    lambda_dl = (avg_length + chunk_length) / (2 * avg_length)
    return lambda_dl
```

###### 术语重要性计算

术语重要性指标衡量术语在文档中的显著程度，结合术语频率和文档长度自适应因子，能够更准确地评估术语在当前文档中的重要性。计算公式考虑了术语频率的非线性增长特性。

$$\text{Sign}(t_{e_i}^\tau, k_j) = \frac{2 \cdot f(t_{e_i}^\tau, k_j) \cdot \Lambda_{\text{DL}}}{f(t_{e_i}^\tau, k_j) + 1}$$

其中 $f(t_{e_i}^\tau, k_j)$ 表示术语在文档chunk中的出现频率，$\Lambda_{\text{DL}}$ 为文档长度自适应因子。这种计算方式能够防止高频术语过度影响评分。

```python
def compute_term_significance(term_freq: int, doc_length_factor: float) -> float:
    significance = (2 * term_freq * doc_length_factor) / (term_freq + 1)
    return significance
```

###### 术语稀有度计算

术语稀有度用于衡量术语在整个知识库中的稀缺程度，稀有度越高的术语在检索中的权重越大。计算采用了改进的IDF公式，增加了平滑处理以避免零除问题。

$\text{Rarity}(t_{e_i}^\tau) = \log\left(\frac{D - \text{df}(t_{e_i}^\tau) + 0.5}{\text{df}(t_{e_i}^\tau) + 0.5} + 1\right)$

其中 $D$ 表示文档总数，$\text{df}(t_{e_i}^\tau)$ 表示包含该术语的文档数量。加一操作确保了对数值始终为正数。

```python
import numpy as np

def compute_term_rarity(doc_freq: int, total_docs: int) -> float:
    rarity = np.log((total_docs - doc_freq + 0.5) / (doc_freq + 0.5) + 1)
    return rarity
```

###### 连贯性指数评估

连贯性指数反映术语在文档中的分布连贯性，通过滑动窗口技术分析术语在文档中的局部分布情况。连贯性高的术语往往在文档的特定区域集中出现，表明其与文档主题的强相关性。

$$\text{CI}(t_{e_i}^\tau, k_j) = \max_{w \in W, \, t \in w} \frac{\sum I(t = t_{e_i}^\tau) \cdot |w|}{|k_j|}$$

其中 $W$ 表示文档中的滑动窗口集合，$I(t = t_{e_i}^\tau)$ 为指示函数，当窗口中包含该术语时为1，否则为0。

```python
def compute_coherence_index(term: str, chunk: str, window_size: int = 50) -> float:
    chunk_tokens = chunk.lower().split()
    chunk_length = len(chunk_tokens)

    if chunk_length == 0:
        return 0.0

    max_coherence = 0.0

    for i in range(0, chunk_length - window_size + 1, 10):
        window = chunk_tokens[i:i + window_size]
        term_count = window.count(term.lower())

        if term_count > 0:
            coherence = (term_count * window_size) / chunk_length
            max_coherence = max(max_coherence, coherence)

    return max_coherence
```

###### 评分融合与检索

将句子级相似度评分与知识级评分进行融合，形成最终的文档相关性评分。融合过程采用加权平均的方式，平衡参数λ控制两种评分方式的重要性。

$\Phi = \lambda \Phi(\mathcal{K}) + (1 - \lambda) \Phi(\mathcal{S})$

其中 $\lambda$ 为平衡参数，$\Phi(\mathcal{K})$ 为知识级评分，$\Phi(\mathcal{S})$ 为句子级评分。通过调整λ值，可以控制系统更偏向语义相似还是知识匹配。当λ=0时，系统完全依赖句子级语义相似度；当λ=1时，系统完全依赖知识匹配评分；λ=0.5时，两种评分方式权重相等。在建筑文档审查场景中，通常设置λ=0.5以平衡专业知识匹配和语义理解。

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple, Dict, Any

class GKGRRetriever:
    def __init__(self,
                 knowledge_base: List[str],
                 embedding_model,
                 key_info_extractor: KeyInfoExtractor,
                 llm,
                 config: Dict[str, Any] = None):
        self.knowledge_base = knowledge_base
        self.embedding_model = embedding_model
        self.key_info_extractor = key_info_extractor
        self.llm = llm

        default_config = {
            "lambda_param": 0.5,
            "top_k": 5,
            "rerank_enabled": True,
            "query_expansion": True,
            "similarity_threshold": 0.1
        }
        self.config = {**default_config, **(config or {})}

        self.kb_embeddings = self._precompute_embeddings()

    def _precompute_embeddings(self) -> np.ndarray:
        embeddings = self.embedding_model.encode(self.knowledge_base, show_progress_bar=True)
        return embeddings

    def retrieve_with_scores(self, query: str) -> List[Tuple[str, float, Dict[str, float]]]:
        query_embedding = self.embedding_model.encode([query])[0]
        sentence_scores = cosine_similarity(
            query_embedding.reshape(1, -1),
            self.kb_embeddings
        )[0]

        key_info = self.key_info_extractor.extract_key_info(query)
        knowledge_scores = self._compute_knowledge_scores(key_info)

        final_scores = []
        for i in range(len(self.knowledge_base)):
            norm_sent = sentence_scores[i]
            norm_know = knowledge_scores[i] / max(knowledge_scores) if max(knowledge_scores) > 0 else 0

            final_score = (self.config["lambda_param"] * norm_know +
                          (1 - self.config["lambda_param"]) * norm_sent)
            final_scores.append(final_score)

        results_with_scores = []
        for i, final_score in enumerate(final_scores):
            if final_score > self.config["similarity_threshold"]:
                score_details = {
                    "sentence_score": float(sentence_scores[i]),
                    "knowledge_score": float(knowledge_scores[i]),
                    "final_score": float(final_score)
                }
                results_with_scores.append((self.knowledge_base[i], final_score, score_details))

        results_with_scores.sort(key=lambda x: x[1], reverse=True)
        return results_with_scores[:self.config["top_k"]]

    def _compute_knowledge_scores(self, key_info: Dict[str, Tuple[str, float]]) -> List[float]:
        scores = []
        avg_length = sum(len(chunk.split()) for chunk in self.knowledge_base) / len(self.knowledge_base)

        for chunk in self.knowledge_base:
            chunk_score = 0.0
            chunk_tokens = chunk.lower().split()
            chunk_length = len(chunk_tokens)

            lambda_dl = compute_document_length_factor(chunk_length, avg_length)

            for priority, (info_text, weight) in key_info.items():
                if not info_text.strip():
                    continue

                terms = info_text.lower().split()
                for term in terms:
                    if term in chunk_tokens:
                        tf = chunk_tokens.count(term)

                        significance = compute_term_significance(tf, lambda_dl)

                        segments_with_term = sum(1 for kb_chunk in self.knowledge_base
                                                if term in kb_chunk.lower())
                        rarity = compute_term_rarity(segments_with_term, len(self.knowledge_base))

                        coherence = compute_coherence_index(term, chunk)

                        term_score = significance * rarity * (1 + coherence) * weight
                        chunk_score += term_score

            scores.append(chunk_score)

        return scores

    def retrieve(self, query: str) -> Tuple[List[str], str]:
        results_with_scores = self.retrieve_with_scores(query)

        documents = [doc for doc, _, _ in results_with_scores]

        if self.config["rerank_enabled"] and len(documents) > 1:
            documents = self._llm_rerank(query, documents)

        augmented_query = query
        if self.config["query_expansion"]:
            augmented_query = self._augment_query(query, documents[:3])

        return documents, augmented_query
```

###### 重排序优化

系统使用大语言模型对检索结果进行进一步重排序，通过LLM的语义理解能力优化文档的相关性排序。重排序过程中，系统会构造包含查询和候选文档的提示，要求LLM根据相关性对文档进行重新排序。

```python
def _llm_rerank(self, query: str, documents: List[str]) -> List[str]:
    if len(documents) <= 1:
        return documents

    rerank_prompt = f"""
Task: A list of documents is shown below. Each document has a number next to it. A question is also provided. Your task is to return the numbers of ALL documents in order of relevance from MOST to LEAST relevant. MUST include EVERY document number exactly once.

Example format:
    Document 1: <document 1>
    Document 2: <document 2>
    Document 3: <document 3>
    Question: <question>
    Answer: 3,1,2

Now here are the actual documents and question.

"""
    for i, doc in enumerate(documents):
        rerank_prompt += f"Document {i+1}: {doc[:150]}...\n"

    rerank_prompt += f"Question: {query}\nAnswer:"

    try:
        response = self.llm.predict(rerank_prompt)
        order_nums = [int(x.strip()) - 1 for x in response.split(',')
                     if x.strip().isdigit() and 0 <= int(x.strip()) - 1 < len(documents)]

        reranked = [documents[i] for i in order_nums if i < len(documents)]

        # 添加遗漏的文档
        used_indices = set(order_nums)
        for i, doc in enumerate(documents):
            if i not in used_indices:
                reranked.append(doc)

        return reranked[:len(documents)]
    except:
        return documents
```

###### 查询增强

同时系统还会利用检索到的知识来增强原始查询，生成更具体、更详细的查询用于进一步检索。查询增强通过分析检索结果的上下文信息，识别查询中可能遗漏的关键概念和术语。

```python
def _augment_query(self, original_query: str, top_results: List[str]) -> str:
    if not top_results:
        return original_query

    document_list = ""
    for i, doc in enumerate(top_results):
        document_list += f"Document {i+1}: {doc[:100]}...\n"

    augment_prompt = f"""
Task: Your task is to generate a detailed answer to the question by synthesizing information from ALL provided documents. Prioritize relevance, cite document numbers, and structure your response as follows:

Question: {original_query}
{document_list}
Answer:
"""

    try:
        augmented = self.llm.predict(augment_prompt)
        return augmented.strip()
    except:
        return original_query
```

###### 偏差检测分析

在先期知识增强检索阶段获取领域知识后，系统随即进入误差辨析模块。该模块基于检索得到的知识参考，并结合预设的审阅问题，对原文进行细致的偏差检测与评估。

```python
class ErrorAnalyzer:
    def __init__(self, llm):
        self.llm = llm

    def analyze_errors(self, document_chunk: str, query: str, retrieved_knowledge: List[str]) -> Dict[str, Any]:

        analysis_prompt = f"""
Task: Your task is to conduct an error analysis on a given review document, based on a provided review query and relevant reference specifications. This analysis MUST strictly adhere to the provided reference and focus specifically on reviewing and analyzing the original descriptive sections within the review document.

Review document: {document_chunk}
Query: {query}
Reference: {chr(10).join([f"{i+1}. {ref}" for i, ref in enumerate(retrieved_knowledge)])}
Analysis:
"""

        analysis = self.llm.predict(analysis_prompt)

        return {
            "analysis": analysis,
            "reference_support": retrieved_knowledge
        }
```

###### 修订建议生成

误差辨析模块完成后，系统将输出标记偏差区域以及相关知识佐证。随后，系统进入修订策略生成模块。该模块依据误差分析结果和知识参考，对标记区域进行针对性的修订建议生成，最终实现对原文的知识驱动型自动修正。

```python
class RevisionGenerator:
    def __init__(self, llm):
        self.llm = llm

    def generate_revisions(self, document_chunk: str, analysis: Dict[str, Any]) -> Dict[str, str]:
        revision_prompt = f"""
Task: Your task is to review and revise the provided document based on the given analysis and corresponding reference specifications. STRICT adherence to the provided reference specifications is required. If the review document aligns with the analysis and reference specifications WITHOUT discrepancies, revision is not necessary.

Review document: {document_chunk}
Analysis: {analysis['analysis']}
Reference: {chr(10).join([f"- {ref}" for ref in analysis['reference_support']])}
Revision:
"""

        revision = self.llm.predict(revision_prompt)

        return {
            "original_text": document_chunk,
            "revision_suggestions": revision,
            "modified_regions": analysis.get("error_regions", []),
            "confidence": self._calculate_confidence(analysis)
        }

    def _calculate_confidence(self, analysis: Dict[str, Any]) -> float:
        ref_count = len(analysis.get("reference_support", []))
        error_count = len(analysis.get("error_regions", []))

        confidence = min(0.9, 0.5 + (ref_count * 0.1) + (error_count * 0.05))
        return confidence
```

###### 完整审查流程

将上述所有模块整合，形成完整的文档审查流程。系统首先生成审查问题，然后进行知识引导检索，接着执行错误分析，最后生成修订建议。

```python
def complete_review_process(document_chunk: str,
                          gkgr_framework: GKGRRetriever,
                          error_analyzer: ErrorAnalyzer,
                          revision_generator: RevisionGenerator) -> Dict[str, Any]:
    review_queries = generate_review_queries(gkgr_framework.llm, document_chunk)

    results = {}
    for query in review_queries[:3]:
        retrieved_docs, augmented_query = gkgr_framework.retrieve(query)

        knowledge_refs = retrieved_docs
        analysis = error_analyzer.analyze_errors(document_chunk, query, knowledge_refs)

        revision = revision_generator.generate_revisions(document_chunk, analysis)

        results[query] = {
            "retrieved_knowledge": retrieved_docs,
            "augmented_query": augmented_query,
            "analysis": analysis,
            "revision": revision
        }

    return results
```

至此，我们就完成了建筑文档智能审查系统的核心实现。

#### 实际应用示例

让我们通过一个完整的示例来展示系统的使用：

```python
# 初始化系统组件
llm = DeepSeekLLM(
    model_name='deepseek-chat',
    api_key='your-api-key',
    base_url='https://api.deepseek.com/v1'
)

embedding = BGEEmbedding(model_name="BAAI/bge-m3")
key_extractor = KeyInfoExtractor(llm)

# 从markdown文档构建知识库
processor = DocumentProcessor()
documents = processor.load_documents("./construction_standards")

# 对文档进行动态语义分块
chunker = DynamicSemanticChunker()
knowledge_base = []
for doc in documents:
    chunks = chunker.split_text(doc)
    knowledge_base.extend(chunks.values())

# 初始化检索器
gkgr_retriever = GKGRRetriever(
    knowledge_base=knowledge_base,
    embedding_model=embedding,
    key_info_extractor=key_extractor,
    llm=llm
)

# 初始化分析器
error_analyzer = ErrorAnalyzer(llm)
revision_generator = RevisionGenerator(llm)

# 待审查的文档内容
sample_document = """
钢筋混凝土柱的施工应符合以下要求：
1. 混凝土强度等级不低于C25
2. 钢筋保护层厚度为25mm
3. 混凝土浇筑应连续进行，间歇时间不超过1小时
4. 养护期间应保持混凝土表面湿润
"""

# 执行审查
result = complete_review_process(
    sample_document,
    gkgr_retriever,
    error_analyzer,
    revision_generator
)

# 查看审查结果
for query, analysis in result.items():
    print(f"审查问题: {query}")
    print(f"修订建议: {analysis['revision']['revision_suggestions']}")
    print("-" * 50)
```

#### 扩展性说明

系统可以通过更换知识库轻松适应其他领域。对于特定企业或项目，可以通过微调关键信息提取模型来提升准确性。在性能优化方面，使用动态语义分块可以提升检索质量，预计算并缓存知识库嵌入以提升检索速度，对于大量文档可使用批量处理模式，根据具体应用场景调整λ参数和top-k值。

#### 写在最后

恭喜你阅读完此文，你已经充分了解了如何实现一个建筑文档智能审查系统以及其背后的思考。这个系统展示了如何将动态语义分块、知识引导检索和大语言模型有机结合，为建筑行业的文档审查提供了一个实用的解决方案。

虽然当前系统已经取得了不错的效果，但仍有改进空间。全局关联增强方面，当前基于文本块的检索可以进一步结合知识图谱等技术。多模态支持方面，未来可以扩展支持CAD图纸、施工图等视觉信息。实时更新方面，支持知识库的增量更新和动态维护。个性化定制方面，根据不同企业和项目特点进行系统定制。

读者们可以运行项目中的示例代码，体验完整的建筑文档智能审查流程。我们相信这个系统不仅能够提升审查效率，更能为建筑行业的数字化转型贡献力量。

#### 致谢

本项目的开发过程中，我们深入研究了建筑工程领域的专业知识和最新的自然语言处理技术。特别感谢建筑行业专家提供的宝贵建议，以及开源社区在技术实现方面的支持。项目代码实现参考了LlamaIndex、Transformers等优秀开源项目的设计理念。

需要说明的是，本项目专门针对建筑施工领域的文档审查场景进行了深度优化。如果您需要处理其他领域的文档，建议根据具体需求对系统进行相应调整。

#### 源码获取

本项目的源码以及实例数据存放在 [GitHub 仓库](https://github.com/Hongru0306/CDDRS)。

#### 引用

如果您在研究中使用了本项目的成果，请按如下方式引用：

```bibtex
@article{XIAO2025103618,
    title = {Generative knowledge-guided review system for construction disclosure documents},
    journal = {Advanced Engineering Informatics},
    volume = {68},
    pages = {103618},
    year = {2025},
    issn = {1474-0346},
    doi = {https://doi.org/10.1016/j.aei.2025.103618},
    url = {https://www.sciencedirect.com/science/article/pii/S1474034625005117},
    author = {Hongru Xiao and Jiankun Zhuang and Bin Yang and Jiale Han and Yantao Yu and Songning Lai},
    keywords = {Construction documents review, Large language model (LLM), Knowledge-guided retrieval, Natural Language Processing (NLP)}
}
```

### 大模型生成 Token 的方式

> 代码已更新到 Happy-LLM 仓库第五章的代码中。

#### 贪婪解码（Greedy Decoding）

##### 原理说明
贪婪解码是最简单直接的文本生成策略。在每一步生成时，它总是选择概率最大的那个token作为下一个token，然后继续生成，直到遇到停止条件或达到最大长度。

**核心思想**：局部最优选择 → 希望全局最优

**数学表达**：
```
token_t = argmax P(token_t | token_1, token_2, ..., token_{t-1})
```

##### 代码实现
基于我们实现的 `_greedy_decode` 方法：

```python
def _greedy_decode(self, logits: torch.Tensor) -> torch.Tensor:
    """
    贪婪解码：选择概率最大的token

    Args:
        logits: 模型输出的logits，形状为 (batch_size, vocab_size)

    Returns:
        选择的token索引，形状为 (batch_size, 1)
    """
    _, idx_next = torch.topk(logits, k=1, dim=-1)
    return idx_next
```

**关键步骤解析**：
1. `torch.topk(logits, k=1, dim=-1)`：找到logits中最大值的位置
2. 返回最大概率token的索引
3. 该token被添加到序列中，继续下一轮生成

##### 使用示例
```python
# 在 generate_super 函数中调用贪婪解码
output = model.generate_super(
    input_ids,
    do_sample=False,      # 不使用采样
    num_beams=1,          # 不使用束搜索
    temperature=0.0,      # 温度为0确保确定性
    max_new_tokens=100
)
```

##### 优缺点分析

**优点**：
- ✅ **速度快**：每步只需要一次前向传播和简单的argmax操作
- ✅ **结果确定**：相同的输入总是产生相同的输出
- ✅ **内存效率高**：不需要维护多个候选序列
- ✅ **实现简单**：算法逻辑直观易懂

**缺点**：
- ❌ **容易陷入局部最优**：每步的局部最优不一定等于全局最优
- ❌ **缺乏多样性**：总是产生相同的序列，缺乏创造性
- ❌ **可能产生重复内容**：容易陷入重复循环
- ❌ **忽略长程依赖**：不考虑序列的整体连贯性

##### 典型例子
假设模型生成了以下概率分布：

```
输入: "今天天气"
下一token概率:
- "很" (0.4)
- "不错" (0.3)
- "真好" (0.2)
- "不太好" (0.1)
```

贪婪解码会选择"很"，生成"今天天气很"，然后继续这个过程。

##### 使用场景
- **确定性任务**：如数学计算、代码生成
- **需要一致性的应用**：如API服务、自动化脚本
- **计算资源受限的环境**：需要快速生成结果
- **基准测试**：作为其他算法的对比基准

#### 采样解码（Sampling Decoding）

##### 原理说明
采样解码不是选择概率最大的token，而是基于模型的概率分布进行随机采样。这样可以在每次生成时产生不同的结果，增加文本的多样性和创造性。

**核心思想**：基于概率分布随机选择 → 增加多样性

**数学表达**：

```
token_t ~ P(token_t | token_1, token_2, ..., token_{t-1})
```

##### 关键参数

###### 1. Temperature（温度）
- **作用**：控制概率分布的平滑程度
- **原理**：将logits除以temperature，然后进行softmax
- **效果**：
  - `temperature > 1`：分布更平滑，增加随机性
  - `temperature < 1`：分布更尖锐，更接近贪婪解码
  - `temperature → 0`：等价于贪婪解码

###### 2. Top-k Sampling
- **作用**：限制候选token的范围
- **原理**：只考虑概率最高的k个token，其他token概率设为0
- **效果**：避免选择概率很低的"奇怪"token，提高质量

##### 代码实现
基于我们实现的 `_random_sample` 方法：

```python
def _random_sample(self, logits: torch.Tensor, temperature: float = 1.0, top_k: int = None) -> torch.Tensor:
    """
    随机采样：基于概率分布随机选择token

    Args:
        logits: 模型输出的logits，形状为 (batch_size, vocab_size)
        temperature: 温度参数，控制随机性
        top_k: 只考虑概率最高的k个token

    Returns:
        选择的token索引，形状为 (batch_size, 1)
    """
    # 1. 温度缩放
    logits = logits / temperature

    # 2. Top-k过滤
    if top_k is not None:
        v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
        logits[logits < v[:, [-1]]] = -float('Inf')

    # 3. 计算概率并采样
    probs = F.softmax(logits, dim=-1)
    idx_next = torch.multinomial(probs, num_samples=1)
    return idx_next
```

**关键步骤解析**：
1. **温度缩放**：调整概率分布的平滑程度
2. **Top-k过滤**：移除低概率候选，提高质量
3. **概率归一化**：使用softmax得到概率分布
4. **随机采样**：根据概率分布随机选择token

##### 使用示例
```python
# 基本采样
output = model.generate_super(
    input_ids,
    do_sample=True,         # 启用采样
    num_beams=1,           # 不使用束搜索
    temperature=0.8,       # 中等温度
    max_new_tokens=100
)

# 带top-k的采样
output = model.generate_super(
    input_ids,
    do_sample=True,
    num_beams=1,
    temperature=1.0,       # 较高温度增加随机性
    top_k=50,             # 只考虑前50个候选
    max_new_tokens=100
)
```

##### 温度参数详解

**不同温度的效果对比**：

```python
# 示例概率分布
original_probs = [0.6, 0.2, 0.1, 0.05, 0.05]

# Temperature = 0.1 (低温度，接近贪婪)
scaled_probs = [0.85, 0.08, 0.04, 0.015, 0.015]
# 结果：很可能选择第一个token

# Temperature = 1.0 (标准温度)
scaled_probs = [0.6, 0.2, 0.1, 0.05, 0.05]
# 结果：按原始概率采样

# Temperature = 2.0 (高温度，增加随机性)
scaled_probs = [0.35, 0.25, 0.18, 0.11, 0.11]
# 结果：各个token都有机会被选中
```

##### Top-k机制详解

**Top-k过滤过程**：

```python
# 假设词汇表大小为1000，top_k=50
logits = [0.1, 2.3, 0.5, 1.8, 0.3, 3.2, 0.9, 0.2, 1.5, 0.7, ...]  # 1000个值

# 步骤1：找到前50个最大值
v, _ = torch.topk(logits, 50)
threshold = v[-1]  # 第50大的值

# 步骤2：过滤
logits[logits < threshold] = -float('Inf')
# 结果：只有50个token有非零概率，其他950个token概率为0
```

##### 优缺点分析

**优点**：
- ✅ **多样性好**：每次生成可能产生不同的结果
- ✅ **创造性高**：能产生意想不到的内容
- ✅ **避免重复**：不容易陷入重复循环
- ✅ **可调性强**：通过参数控制随机程度

**缺点**：
- ❌ **结果不确定**：相同输入可能产生不同输出
- ❌ **质量不稳定**：可能产生低质量或不连贯的内容
- ❌ **需要调参**：temperature和top_k需要仔细调节
- ❌ **计算开销**：需要计算完整的概率分布

##### 使用场景
- **创意写作**：故事生成、诗歌创作
- **对话系统**：让对话更加自然和有趣
- **数据增强**：生成多样化的训练数据
- **探索性任务**：需要探索多种可能性的场景

#### 束搜索（Beam Search）

##### 原理说明
束搜索是一种启发式搜索算法，它在每一步生成时保留多个候选序列（束），而不是只选择一个最佳序列。通过维护多条路径，它能够在计算效率和生成质量之间取得平衡。

**核心思想**：维护多条候选路径 → 选择累积概率最高的序列

**算法流程**：
1. **初始化**：从输入序列开始
2. **扩展**：为每个候选序列生成多个扩展
3. **评分**：计算每个新序列的累积概率
4. **筛选**：保留分数最高的N个候选
5. **重复**：继续扩展直到结束条件

##### 关键概念

###### 束宽度（Beam Width）
- **定义**：每步保留的候选序列数量
- **权衡**：
  - 宽度=1：等价于贪婪解码
  - 宽度越大：搜索空间越大，质量越高，但计算成本也越大

###### 累积概率
- **计算方式**：序列概率 = 各个token概率的乘积
- **数值稳定性**：通常使用对数概率求和
- **公式**：`log P(sequence) = Σ log P(token_i | context)`

##### 代码实现
基于我们实现的 `_beam_search` 方法：

```python
def _beam_search(self, idx: torch.Tensor, max_new_tokens: int, num_beams: int,
                 temperature: float = 1.0, top_k: int = None, stop_id: int = None) -> torch.Tensor:
    """
    束搜索：维护多个候选序列，选择最优路径

    Args:
        idx: 输入序列，形状为 (batch_size, seq_len)
        max_new_tokens: 最大生成token数量
        num_beams: 束宽度，表示保留的候选路径数量
        temperature: 温度参数，控制分布的平滑程度
        top_k: top-k过滤参数，限制候选token范围
        stop_id: 停止生成的token ID，遇到则停止

    Returns:
        生成的token序列，形状为 (batch_size, generated_length)
    """
    # 1. 初始化束
    beams = [idx.clone() for _ in range(num_beams)]
    beam_scores = torch.zeros(num_beams, device=idx.device)
    beam_scores[0] = 0.0  # 第一个候选是原始序列
    beam_scores[1:] = float('-inf')  # 其他候选初始分数为负无穷

    # 2. 主循环：逐步生成token
    for step in range(max_new_tokens):
        new_beams = []
        new_scores = []

        # 3. 扩展每个候选序列
        for beam_idx, beam in enumerate(beams):
            if beam_scores[beam_idx] == float('-inf'):
                continue  # 跳过无效候选

            # 前向传播获取logits
            output = self(beam)
            logits = output.logits[:, -1, :]

            # 应用温度和top-k
            if temperature != 1.0:
                logits = logits / temperature
            if top_k is not None:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = -float('Inf')

            # 计算对数概率
            log_probs = F.log_softmax(logits, dim=-1)

            # 获取前num_beams个候选token
            top_log_probs, top_indices = torch.topk(log_probs, k=num_beams, dim=-1)

            # 4. 为当前候选生成多个扩展
            for k in range(num_beams):
                token = top_indices[:, k:k+1]
                log_prob = top_log_probs[:, k]

                new_beam = torch.cat([beam, token], dim=1)
                new_score = beam_scores[beam_idx] + log_prob.item()

                new_beams.append(new_beam)
                new_scores.append(new_score)

        # 5. 筛选最佳候选
        if not new_beams:
            break

        # 按分数排序，选择前num_beams个
        sorted_indices = sorted(range(len(new_scores)), key=lambda i: new_scores[i], reverse=True)
        beams = [new_beams[i] for i in sorted_indices[:num_beams]]
        beam_scores = [new_scores[i] for i in sorted_indices[:num_beams]]

        # 检查停止条件
        if stop_id is not None and beams[0][0, -1] == stop_id:
            break

    # 6. 返回最佳序列
    return beams[0][:, idx.shape[1]:]  # 只返回生成部分
```

##### 束搜索过程示例

假设束宽度=3，输入="今天天气"：

**第1步扩展**：
```
候选1: "今天天气很好" (分数: 0.4)
候选2: "今天天气不错" (分数: 0.3)
候选3: "今天天气真好" (分数: 0.2)
```

**第2步扩展**（每个候选再扩展3个）：
```
候选1.1: "今天天气很好啊" (分数: 0.4 + 0.1 = 0.5)
候选1.2: "今天天气很好。" (分数: 0.4 + 0.2 = 0.6) ← 保留
候选1.3: "今天天气很好，" (分数: 0.4 + 0.05 = 0.45)

候选2.1: "今天天气不错啊" (分数: 0.3 + 0.15 = 0.45)
候选2.2: "今天天气不错。" (分数: 0.3 + 0.1 = 0.4) ← 保留
候选2.3: "今天天气不错，" (分数: 0.3 + 0.08 = 0.38)

候选3.1: "今天天气真好啊" (分数: 0.2 + 0.12 = 0.32)
候选3.2: "今天天气真好。" (分数: 0.2 + 0.25 = 0.45) ← 保留
候选3.3: "今天天气真好，" (分数: 0.2 + 0.1 = 0.3)
```

**筛选结果**（保留分数最高的3个）：
```
最佳候选: "今天天气很好。" (分数: 0.6)
次佳候选: "今天天气不错。" (分数: 0.4)
第三候选: "今天天气真好。" (分数: 0.45)
```

##### 使用示例
```python
# 基本束搜索
output = model.generate_super(
    input_ids,
    do_sample=False,        # 不使用采样
    num_beams=3,           # 束宽度为3
    temperature=1.0,       # 标准温度
    max_new_tokens=100
)

# 带top-k的束搜索
output = model.generate_super(
    input_ids,
    do_sample=False,
    num_beams=5,           # 更大的束宽度
    temperature=0.8,       # 稍微降低温度
    top_k=50,             # 限制候选范围
    max_new_tokens=100
)
```

##### 优缺点分析

**优点**：
- ✅ **质量较高**：比贪婪解码质量更好
- ✅ **确定性**：结果相对稳定（相同输入产生相同输出）
- ✅ **平衡性好**：在质量和效率之间取得平衡
- ✅ **避免明显错误**：不容易选择明显不合适的token

**缺点**：
- ❌ **计算开销大**：需要维护多个候选序列
- ❌ **内存占用高**：存储多个候选序列和分数
- ❌ **仍可能局部最优**：虽然比贪婪好，但仍可能错过全局最优
- ❌ **多样性有限**：仍然偏向高概率路径，创造性不如采样

##### 束宽度选择建议

| 束宽度 | 适用场景 | 优点 | 缺点 |
|--------|----------|------|------|
| 1-2 | 实时应用、计算资源有限 | 速度快、资源占用少 | 质量相对较低 |
| 3-5 | 一般对话、文本生成 | 质量较好、速度适中 | 资源占用中等 |
| 6-10 | 高质量生成、翻译 | 质量很高 | 计算开销大 |
| 10+ | 专业应用、研究 | 最高质量 | 开销很大 |

##### 使用场景
- **机器翻译**：需要准确性和流畅性的平衡
- **文本摘要**：生成连贯的摘要内容
- **对话系统**：生成有逻辑的回复
- **代码生成**：需要语法正确和逻辑合理
- **长文本生成**：如文章写作、报告生成

#### 辅助模型投机解码（Assisted Decoding）

##### 原理说明
投机解码是一种**用小模型加速大模型推理**的技术。它通过"草稿-验证"的方式，让小先生成候选token，然后大家模型快速验证，减少大模型的前向传播次数。

**核心思想**：小模型投机生成 → 大模型批量验证 → 减少大模型计算负担

##### 工作流程

###### 1. 草稿生成阶段
```
输入: "今天天气"
小模型快速生成草稿: "今天天气很好，适合出门散步"
```

###### 2. 验证阶段
大模型一次性验证整个草稿序列：
- ✅ 接受的token："今天天气很好，"
- ❌ 拒绝的token：从"适合"开始拒绝
- 🔧 大模型重新生成："适合在家休息"

###### 3. 最终结果
```
输出: "今天天气很好，适合在家休息"
```

##### 关键优势

**速度提升**：
- 小模型推理快 → 生成多个候选token
- 大模型批量验证 → 一次处理多个token
- 减少90%+的大模型前向传播

**质量保证**：
- 大模型有最终否决权
- 只有大模型认可的token才会被保留
- 不会降低生成质量

##### 具体例子对比

**传统方式**（大模型逐个生成）：
```
第1步: 大模型 → "今天"
第2步: 大模型 → "今天天气"
第3步: 大模型 → "今天天气很"
第4步: 大模型 → "今天天气很好"
第5步: 大模型 → "今天天气很好，"
第6步: 大模型 → "今天天气很好，适合"
... (每步都需要大模型前向传播)
```

**投机解码**：
```
第1步: 小模型快速草稿 → "今天天气很好，适合出门散步"
第2步: 大模型批量验证 → 接受"今天天气很好，"，拒绝"适合出门散步"
第3步: 大模型重新生成 → "适合在家休息"
```

这样原本需要6次大模型推理的过程，现在只需要2次！

##### 技术实现要点

###### 1. 草稿长度控制
- **草稿不宜过长**：通常2-10个token
- **接受率平衡**：太长接受率低，太短加速效果不明显
- **动态调整**：根据接受率调整草稿长度

###### 2. 验证机制
```python
# 伪代码
def assisted_decoding(input_ids, assistant_model, main_model):
    # 小模型生成草稿
    draft_tokens = assistant_model.generate_draft(input_ids, max_draft_len=5)

    # 大模型验证
    accepted_count = main_model.verify_draft(input_ids, draft_tokens)

    # 构建最终结果
    if accepted_count == len(draft_tokens):
        return draft_tokens  # 全部接受
    else:
        # 部分接受，大模型重新生成剩余部分
        accepted_part = draft_tokens[:accepted_count]
        remaining_part = main_model.generate_remaining(input_ids + accepted_part)
        return accepted_part + remaining_part
```

##### 总结
投机解码本质上是用**计算资源换时间**，通过小模型的"投机"来减少大模型的计算负担。它是一种聪明的工程优化，在不牺牲质量的前提下显著提升推理速度。
