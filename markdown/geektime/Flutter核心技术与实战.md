---
title: "Flutter核心技术与实战"
authors:
  - "陈航"
language: "zh-CN"
tags:
  - "flutter"
  - "dart"
  - "mobile-development"
  - "tutorial"
published_at: "2024-12-14"
updated_at: "2024-12-14"
---

# Flutter核心技术与实战

## 文档信息

| 项目 | 内容 |
| --- | --- |
| 文档标题 | Flutter核心技术与实战 |
| 文档类型 | zh-CN 整合 Markdown |
| 上游仓库 | [Yvan0329/lianglianglee](https://github.com/Yvan0329/lianglianglee) |
| 锁定提交 | [4afe4a62c4e1](https://github.com/Yvan0329/lianglianglee/commit/4afe4a62c4e105a59d41319a29e523eee3bd82c4) |
| 提交时间 | 2024-12-14T17:33:19+08:00 |
| 生成器版本 | `generic@1;engine@8` |

> 本文件由 reference 仓库自动生成。请修改上游源文件或本仓库的清单/适配器后重新生成，不要直接编辑此文件。

## 阅读说明

本文档按清单中的阅读顺序合并上游 Markdown。图片被改写为锁定提交的 GitHub Raw 链接，章节内有效的本地文档链接被改写为同一提交的 GitHub 源文件链接。

## 目录

- [入门与 Dart 基础](#入门与-dart-基础)
  - [开篇词 为什么每一位大前端从业者都应该学习Flutter？](#开篇词-为什么每一位大前端从业者都应该学习flutter)
  - [预习篇 · 从0开始搭建Flutter工程环境](#预习篇-从0开始搭建flutter工程环境)
  - [预习篇 · Dart语言概览](#预习篇-dart语言概览)
  - [深入理解跨平台方案的历史发展逻辑](#深入理解跨平台方案的历史发展逻辑)
  - [Flutter区别于其他方案的关键技术是什么？](#flutter区别于其他方案的关键技术是什么)
  - [从标准模板入手，体会Flutter代码是如何运行在原生系统上的](#从标准模板入手体会flutter代码是如何运行在原生系统上的)
  - [基础语法与类型变量：Dart是如何表示信息的？](#基础语法与类型变量dart是如何表示信息的)
  - [函数、类与运算符：Dart是如何处理信息的？](#函数类与运算符dart是如何处理信息的)
  - [综合案例：掌握Dart核心特性](#综合案例掌握dart核心特性)
- [Widget 与界面构建](#widget-与界面构建)
  - [Widget，构建Flutter界面的基石](#widget构建flutter界面的基石)
  - [Widget中的State到底是什么？](#widget中的state到底是什么)
  - [提到生命周期，我们是在说什么？](#提到生命周期我们是在说什么)
  - [经典控件（一）：文本、图片和按钮在Flutter中怎么用？](#经典控件一文本图片和按钮在flutter中怎么用)
  - [经典控件（二）：UITableView_ListView在Flutter中是什么？](#经典控件二uitableviewlistview在flutter中是什么)
  - [经典布局：如何定义子控件在父容器中排版的位置？](#经典布局如何定义子控件在父容器中排版的位置)
  - [组合与自绘，我该选用何种方式自定义Widget？](#组合与自绘我该选用何种方式自定义widget)
  - [从夜间模式说起，如何定制不同风格的App主题？](#从夜间模式说起如何定制不同风格的app主题)
  - [依赖管理（一）：图片、配置和字体在Flutter中怎么用？](#依赖管理一图片配置和字体在flutter中怎么用)
  - [依赖管理（二）：第三方组件库在Flutter中要如何管理？](#依赖管理二第三方组件库在flutter中要如何管理)
- [交互、数据与网络](#交互数据与网络)
  - [用户交互事件该如何响应？](#用户交互事件该如何响应)
  - [关于跨组件传递数据，你只需要记住这三招](#关于跨组件传递数据你只需要记住这三招)
  - [路由与导航，Flutter是这样实现页面切换的](#路由与导航flutter是这样实现页面切换的)
  - [如何构造炫酷的动画效果？](#如何构造炫酷的动画效果)
  - [单线程模型怎么保证UI运行流畅？](#单线程模型怎么保证ui运行流畅)
  - [HTTP网络编程与JSON解析](#http网络编程与json解析)
  - [本地存储与数据库的使用和优化](#本地存储与数据库的使用和优化)
- [平台互操作与适配](#平台互操作与适配)
  - [如何在Dart层兼容Android_iOS平台特定实现？（一）](#如何在dart层兼容androidios平台特定实现一)
  - [如何在Dart层兼容Android_iOS平台特定实现？（二）](#如何在dart层兼容androidios平台特定实现二)
  - [如何在原生应用中混编Flutter工程？](#如何在原生应用中混编flutter工程)
  - [混合开发，该用何种方案管理导航栈？](#混合开发该用何种方案管理导航栈)
  - [为什么需要做状态管理，怎么做？](#为什么需要做状态管理怎么做)
  - [如何实现原生推送能力？](#如何实现原生推送能力)
  - [适配国际化，除了多语言我们还需要注意什么_](#适配国际化除了多语言我们还需要注意什么)
  - [如何适配不同分辨率的手机屏幕？](#如何适配不同分辨率的手机屏幕)
- [构建、调试、测试与发布](#构建调试测试与发布)
  - [如何理解Flutter的编译模式？](#如何理解flutter的编译模式)
  - [Hot Reload是怎么做到的？](#hot-reload是怎么做到的)
  - [如何通过工具链优化开发调试效率？](#如何通过工具链优化开发调试效率)
  - [如何检测并优化Flutter App的整体性能表现？](#如何检测并优化flutter-app的整体性能表现)
  - [如何通过自动化测试提高交付质量？](#如何通过自动化测试提高交付质量)
  - [线上出现问题，该如何做好异常捕获与信息采集？](#线上出现问题该如何做好异常捕获与信息采集)
  - [衡量Flutter App线上质量，我们需要关注这三个指标](#衡量flutter-app线上质量我们需要关注这三个指标)
  - [组件化和平台化，该如何组织合理稳定的Flutter工程结构？](#组件化和平台化该如何组织合理稳定的flutter工程结构)
  - [如何构建高效的Flutter App打包发布环境？](#如何构建高效的flutter-app打包发布环境)
- [混合开发框架](#混合开发框架)
  - [如何构建自己的Flutter混合开发框架（一）？](#如何构建自己的flutter混合开发框架一)
  - [如何构建自己的Flutter混合开发框架（二）？](#如何构建自己的flutter混合开发框架二)
- [特别放送与结束语](#特别放送与结束语)
  - [特别放送   温故而知新，与你说说专栏的那些思考题](#特别放送-温故而知新与你说说专栏的那些思考题)
  - [结束语 勿畏难，勿轻略](#结束语-勿畏难勿轻略)

---

## 入门与 Dart 基础

### 开篇词 为什么每一位大前端从业者都应该学习Flutter？

你好，我是陈航，之前在美团外卖担任商家业务大前端团队技术负责人。在接下来三个月的时间里，我将和你一起学习Flutter。

当下是移动互联网的时代，也是大前端技术紧密整合的时代。而移动系统与终端设备的碎片化，让我们一直头痛于在不同平台上开发和维护同一个产品的成本问题：使用原生方式来开发App，不仅要求分别针对iOS和Android平台，使用不同的语言实现同样的产品功能，还要对不同的终端设备和不同的操作系统进行功能适配，并承担由此带来的测试维护升级工作。

这对中小型团队而言无疑是非常大的负担，也无形中拖慢了追求“小步快跑”，以快速应对市场变化的互联网产品交付节奏。

为解决这一问题，各类打着“一套代码，多端运行”口号的跨平台开发方案，如雨后春笋般涌现，**React Native就是其中的典型代表**。

React Native希望开发者能够在性能、展示、交互能力和迭代交付效率之间做到平衡。它在Web容器方案的基础上，优化了加载、解析和渲染这三大过程，以相对简单的方式支持了构建移动端页面必要的Web标准，保证了便捷的前端开发体验；并且在保留基本渲染能力的基础上，用原生自带的UI组件实现代替了核心的渲染引擎，从而保证了良好的渲染性能。

但是，由于React Native的技术方案所限，使用原生控件承载界面渲染，在牺牲了部分Web标准灵活性的同时，固然解决了不少性能问题，但也引入了新的问题：除开通过JavaScript虚拟机进行原生接口的调用，而带来的通信低效不谈，由于框架本身不负责渲染，而是由原生代理，因此我们还需要面对大量平台相关的逻辑。

而随着系统版本和API的变化，我们还需要处理不同平台的原生控件渲染能力上的差异，修复各类怪异的Bug，甚至还需要在原生系统上打各类补丁。

这都使React Native的跨平台特性被大打折扣：要用好React Native，除了掌握这个框架外，开发者还必须同时熟悉iOS和Android系统。这，无疑给开发者提出了更多挑战，也是很多开发者们对React Native又爱又恨的原因。在这其中，也有一些团队决定放弃React Native回归原生开发，Airbnb就是一个例子。

备注：2018年，Airbnb团队在Medium上发布的一系列文章（[React Native at Airbnb](https://medium.com/airbnb-engineering/react-native-at-airbnb-f95aa460be1c)、[React Native at Airbnb: The Technology](https://medium.com/airbnb-engineering/react-native-at-airbnb-the-technology-dafd0b43838)、[Building a Cross-Platform Mobile Team](https://medium.com/airbnb-engineering/building-a-cross-platform-mobile-team-3e1837b40a88)、[Sunsetting React Native](https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a)、[What’s Next for Mobile at Airbnb](https://medium.com/airbnb-engineering/whats-next-for-mobile-at-airbnb-5e71618576ab)）详细描述了这个过程。

**而我们本次课程的主角Flutter，则完全不同于React Native。**

它开辟了全新的思路，提供了一整套从底层渲染逻辑到上层开发语言的完整解决方案：视图渲染完全闭环在其框架内部，不依赖于底层操作系统提供的任何组件，从根本上保证了视图渲染在Android和iOS上的高度一致性；Flutter的开发语言Dart，是Google专门为（大）前端开发量身打造的专属语言，借助于先进的工具链和编译器，成为了少数同时支持JIT和AOT的语言之一，开发期调试效率高，发布期运行速度快、执行性能好，在代码执行效率上可以媲美原生App。而这与React Native所用的只能解释执行的JavaScript，又拉开了性能差距。

正是因为这些革命性的特点，Flutter在正式版发布半年多的时间里，在GitHub上的Star就已经超过了68,000，与已经发布4年多的、拥有78,000 Star的同行业领头羊React Native的差距非常小。同时，阿里闲鱼、今日头条等知名商用案例的加持，更使得Flutter的热度不断攀升。

**现在看来，在Google的强力带动下，Flutter极有可能成为跨平台开发领域的终极解决方案。**在过去的大半年时间里，我曾面试了20多位初、中、高级候选人，包括前端、Android、iOS的开发者。当问到最近想学习什么新技术时，超过80%的候选人告诉我，他会学习或正在学习Flutter。

不过坦白讲，相比其他跨平台技术，Flutter的学习成本相对较高。我听过很多（大）前端开发者反馈：Flutter从语言到开发框架都是全新的，技术栈的积累也要从头开始，学不动了。

**学习成本高，这也是目前大多数开发者犹豫是否要跟进这个框架的最重要原因。对此，我感同身受。**

但其实，大前端各个方向的工作有很多相似、相通之处。面对业务侧日益增多的需求，作为大前端团队的负责人，我曾在不同时期带领团队分别探索并大规模落地了以React Native和Flutter为代表的跨平台方案，也是美团最早落地Flutter线上大规模应用的发起者和推动者之一。

在探索并大规模落地Flutter的过程中，我阅读过大量关于Flutter的教程和技术博客，但我发现很多文章的学习门槛都比较高，而且过于重视应用层API各个参数的介绍或实现细节，导致很多从其他平台转来的开发者无从下手，只能依葫芦画瓢，却不知道为什么要“画瓢”，无法与自身的经验串联进而形成知识体系。这，无疑又增加了学习门槛，加长了学习周期。

那么，**Flutter到底该怎么学？真的要从头开始么？**

虽然Flutter是全新的跨平台技术，但其背后的框架原理和底层设计思想，无论是底层渲染机制与事件处理方式，还是组件化解耦思路，亦或是工程化整体方法等，与原生Android/iOS开发并没有本质区别，甚至还从React Native那里吸收了不少优秀的设计理念。就连Flutter所采用的Dart语言，关于信息表达和处理的方式，也有诸多其他优秀编程语言的影子。

因此，从本质上看，Flutter并没有开创新的概念。这也就意味着，如果我们在学习Flutter时，能够深入进去搞懂它的原理、设计思路和通用理念，并与过往的开发经验相结合，建立起属于自己的知识体系抽象层次，而不是仅停留在应用层API的使用上，就摆脱了经验与平台的强绑定。

这样的话，即使未来老框架不断更新，或者出现新的解决方案，我们仍旧可以立于不败之地。

那么，Flutter框架底层有哪些关键技术？它们是如何高效运转，以支撑起可以媲美原生应用的跨平台方案的？Flutter应用开发的最佳实践是怎样的？企业需要什么样的终端技术人才？终端技术未来有哪些发展方向？

这些问题，正是我要通过这个课程为你解答的。在这个课程里，我不仅会帮助你快速上手，能够使用Flutter开发一款企业级App，更希望帮助你将其与过往的开发经验串联起来，以建立起自己的知识体系；同时，希望你能透过现象明白Flutter框架的用法，并看到其背后的原理和设计理念。

为了帮助你领悟到Flutter的核心思想和关键技术，而不是陷入组件的API细节难以自拔，我会在不影响学习、理解的情况下，省去一些不影响核心功能的代码和参数讲解，着重为你剖析框架的核心知识点和背后原理，并与你分享一些常见问题的解决思路。

整体来说，专栏主要包括以下五大部分内容：

- **Flutter开发起步模块。**我会从跨平台方案发展历史出发，与你介绍Flutter的诞生背景、基本原理，并带你体验一下Flutter代码是如何在原生系统上运行的。
- **Dart基础模块。**我会从Dart与其他编程语言的设计思想对比出发，与你讲述Dart设计的关键思路以及独有特性，并通过一个综合案例带你去实践一下。
- **Flutter基础模块。**我将通过Flutter与原生系统对应概念对比，与你讲述Flutter独有的概念和框架设计思路。学完这个模块，你就可以开发出一个简单的App了。
- **Flutter进阶模块。**我会与你讲述Flutter开发中的一些疑难问题、高级特性及其背后原理，帮助你在遇到问题时化被动为主动。
- **Flutter综合应用模块。**我将和你聊聊在企业级应用迭代的生命周期中，如何从效率和质量这两个维度出发，构建自己的Flutter开发体系。

最后，我希望通过这个课程，能够帮助你快速上手Flutter开发应用，掌握其精髓，并引导你建立起属于自己的终端知识体系。

现在，Flutter正处于快速发展中，社区也非常活跃。站在未来看未来，尽管Flutter全平台制霸的目标已经非常清晰，但为期三个月的专栏分享未必能穷尽Flutter未来可能的技术发展方向。接下来，我会持续关注Flutter包括移动端之外的最新变化，持续更新这个专栏，第一时间与你分享Flutter的那些事儿。

好了，今天的内容就到这里了。如果可以的话，还请你在留言区中做个自我介绍，和我聊聊你目前的工作、学习情况，以及你在学习或者使用Flutter时遇到的问题，这样我们可以彼此了解，也方便我在后面针对性地给你讲解。

加油，让我们突破自己的瓶颈，保持学习、保持冷静、保持成长。

### 预习篇 · 从0开始搭建Flutter工程环境

你好，我是陈航。

俗话说，工欲善其事，必先利其器。任何一门新技术、新语言的学习，都需要从最基础的工程环境搭建开始，学习Flutter也不例外。所以，作为专栏的第一篇文章，我会与你逐一介绍Flutter的开发环境配置，并通过一个Demo为你演示Flutter项目是如何运行在Andorid和iOS的模拟器和真机上的。如果你已经掌握了这部分内容，那可以跳过这篇预习文章，直接开始后面内容的学习。

由于是跨平台开发，所以为了方便调试，你需要一个可以支持Android和iOS运行的操作系统，也就是macOS，因此后面的内容主要针对的是在macOS系统下如何配置Flutter开发环境。

如果你身边没有macOS系统的电脑也没关系，在Windows或Linux系统上配置Flutter也是类似的方法，一些关键的区别我也会重点说明。但这样的话，你就只能在Android单平台上开发调试了。

#### 准备工作

##### 安装Android Studio

Android Studio是基于IntelliJ IDEA的、Google官方的Android应用集成开发环境(IDE)。

我们在[官网](https://developer.android.com/studio/index.html?hl=zh-cn)上找到最新版（截止至本文定稿，最新版为3.4），下载后启动安装文件，剩下的就是按照系统提示进行SDK的安装和工程配置工作了。

配置完成后，我们打开AVD Manager，点击“Create Virtual Device”按钮创建一台Nexus 6P模拟器，至此Android Studio的安装配置工作就完成了。

##### 安装Xcode

Xcode是苹果公司官方的iOS和macOS应用集成开发环境(IDE)。它的安装方式非常简单，直接在macOS系统的App Store搜索Xcode，然后安装即可。

安装完成后，我们会在Launchpad看到Xcode图标，打开它，按照提示接受Xcode许可协议，以及安装配置组件就可以了。

配置完成后，我们打开Terminal，输入命令**open -a Simulator**打开iOS模拟器，检查 **Hardware>Device** 菜单项中的设置，并试着在不同的模拟器之间做切换。

至此，Xcode的安装配置工作也就顺利完成了。

#### 安装Flutter

Flutter源站在国内可能不太稳定，因此谷歌中国开发者社区（GDG）专门搭建了临时镜像，使得我们的Flutter 命令行工具可以到该镜像站点下载所需资源。

接下来，我们需要配置镜像站点的环境变量。对于macOS和Linux系统来说，我们通过文本编辑器，打开~/.bash_profile文件，在文件最后添加以下代码，来配置镜像站点的环境变量：

```
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
```

而对于Windows系统来说，我们右键点击计算机图标，依次选择属性–>高级系统设置–>高级–>环境变量，新建用户变量PUB_HOSTED_URL，其值为`https://pub.flutter-io.cn`；随后新建FLUTTER_STORAGE_BASE_URL，其值为`https://storage.flutter-io.cn`，重启电脑即可完成配置。

**到这里，我们就完成了镜像的配置。**

不过，由于GDG并不是官方组织，因此Flutter团队也无法保证此服务长期可用。但是，你也不用担心，可以关注Flutter社区 [Using Flutter in China](https://flutter.dev/community/china)，来获取其他可用的镜像资源，随时更新环境变量即可。

随后，我们再去[Flutter官网](https://flutter.dev/docs/development/tools/sdk/releases?tab=macos)，选择并下载最新的稳定版（截止至本文定稿，最新稳定版为1.5）。

接下来，我们把下载的压缩包解压到你想安装的目录，比如~/Documents或C:\src\flutter。为了可以在命令行中执行flutter命令，我们同样需要配置环境变量。

对于macOS与Linux系统，我们编辑~/.bash_profile文件，把以下代码添加至文件最后，将flutter命令的执行路径追加到环境变量PATH中：

```
export PATH=~/Documents/flutter/bin:$PATH
```

而对于Windows系统，我们在当前用户变量下Path，以; 为分隔符，在其后追加flutter命令行的全路径C:\src\flutter\bin，重启电脑即可完成配置。

**到这里，我们就完成了Flutter SDK的安装。**

打开Flutter根目录，我们可以发现有一个examples文件夹，里面是一些基本的flutter示例。在今天这篇文章中，我会以hello_world示例为例，和你演示一下**如何在模拟器和真机中运行Flutter项目**。

**首先**，我给你介绍的是通过Flutter命令行运行的模式。进入hello_world目录，输入**flutter emulators**命令，查看当前可用的模拟器：

![ece21db3e7764f8fbc3f091c89b0969c](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ece21db3e7764f8fbc3f091c89b0969c.jpg)

图1 查看可用的flutter模拟器

可以看到，我们刚刚创建的两台模拟器，也就是Nexus 6P和iOS模拟器都已经在列表中了。于是，我们启动iOS模拟器，运行Flutter项目：

```
flutter emulators --launch apple_ios_simulator
flutter run
```

等待10秒左右，一个熟悉的hello world大屏幕就出现在我们面前了：

![a8f2e75fba7e45d8b86dc211df038d47](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a8f2e75fba7e45d8b86dc211df038d47.jpg)

图2 Flutter demo

Android模拟器的启动和运行，也与之类似，我就不再赘述了。

不过，使用命令行的方式来开发调试Flutter还是非常不方便，**更高效的方式是配置Android和iOS的集成开发环境**。

Flutter 提供了一个命令**flutter doctor**协助我们安装 Flutter的工程依赖，它会检查本地是否有Android和iOS的开发环境，如果检测到依赖缺失，就会给出对应依赖的安装方法。

接下来，我们试着运行下flutter doctor这条命令，得到了如下图所示的结果：

![16ce45ba532e4b8d96d45c024746177c](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/16ce45ba532e4b8d96d45c024746177c.jpg)

图3 flutter doctor命令示意

可以看到，flutter doctor检测出了iOS工具链、Android Studio工程这两项配置中的问题。此外，由于我的电脑还安装了IDEA和VS Code，而它们也是Flutter官方支持的IDE，因此也一并检测出了问题。

接下来，我们根据运行flutter doctor命令得到的提示，来分别解决iOS工具链和Android Studio工程配置问题。

##### iOS工具链设置

现在，我们已经可以在iOS模拟器上开发调试Flutter应用了。但要将Flutter应用部署到真实的iOS设备上，我们还需要安装一些额外的连接控制命令工具（就像通过电脑的iTunes给手机安装应用一样），并申请一个iOS开发者账号进行Xcode签名配置。

依据提示，我们**首先**安装libimobiledevice和ideviceinstaller这两项依赖：

```
brew update
brew install --HEAD usbmuxd
brew link usbmuxd
brew install --HEAD libimobiledevice
brew install ideviceinstaller
```

其中，usbmuxd是一个与iOS设备建立多路通信连接的socket守护进程，通过它，可以将USB通信抽象为TCP通信；libimobiledevice是一个与iOS设备进行通信的跨平台协议库；而ideviceinstaller则是一个使用它们在iOS设备上管理App的工具。

现在，你不了解它们的具体作用也没关系，只要知道安装了它们，Flutter就可以进行iOS真机的开发调试就可以了。

**然后**，进行Xcode签名配置。

打开hello_world项目中的ios/Runner.xcworkspace，在Xcode中，选择导航面板左侧最上方的Runner项目。

![72219327423541b2a2ba8cef7c4d1e9b](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/72219327423541b2a2ba8cef7c4d1e9b.jpg)

图4 Flutter Xcode签名配置

在**General > Signing > Team** 中，我们需要配置一下开发团队，也就是用你的Apple ID登录Xcode。当配置完成时，Xcode会自动创建并下载开发证书。

任意Apple ID都支持开发和测试，但如果想将应用发布到App Store，则必须加入Apple开发者计划。开发者计划的详细信息，你可以通过苹果官方的[compare memberships](https://developer.apple.com/support/compare-memberships/)了解，这里我就不再展开了。

**最后**，当我们第一次连接真机设备进行开发时，Xcode会在你的帐户中自动注册这个设备，随后自动创建和下载配置文件。我们只需要在真机设备上，按照手机提示，信任你的Mac和开发证书就可以了。

至此，我们就可以在iOS真机上开发调试Flutter项目了。

##### Android 工具链配置

相对于iOS工具链的设置，Android工具链配置就简单多了，这是因为Google官方已经在Android Studio中提供了Flutter和Dart这两个插件。因此，我们可以通过这两个工程插件，进行Flutter项目的管理以及开发调试。又因为Flutter插件本身依赖于Dart插件，所以我们只安装Flutter插件就可以了。

![9e1ee7ff201e4bd9a9df46f1accd5405](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/9e1ee7ff201e4bd9a9df46f1accd5405.jpg)

图5 Flutter插件安装

启动Android Studio，打开菜单项 **Preferences > Plugins**，搜索Flutter插件并点击 install进行安装。安装完毕后重启Android Studio，Flutter插件就生效了。

由于Android Studio本身是基于IDEA开发的，因此IDEA的环境配置与Android Studio并无不同，这里就不再赘述了。

对于VS Code，我们点击View->Command Palette，输入”install”，然后选择”Extensions：Install Extension”。在搜索框中输入flutter，选择安装即可。

至此，Android的工具链配置也完成了。

尽管Android Studio是Google官方的Android集成开发环境，但借助于Flutter插件的支持，Android Studio也因此具备了提供一整套Flutter开发、测试、集成打包等跨平台开发环境的能力，而插件底层通过调用Xcode提供的命令行工具，可以同时支持开发调试及部署iOS和Android应用。

因此，**我后续的分享都会以Android Studio作为讲解Flutter开发测试的IDE。**

##### 运行Flutter项目

用Android Studio打开hello_world工程（Open an existing Android Studio Project），然后定位到工具栏：

![a9f3ed3e62cc441c9201821ad817712a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a9f3ed3e62cc441c9201821ad817712a.jpg)

图6 Flutter工具栏

在Target selector中，我们可以选择一个运行该应用的设备。如果没有列出可用设备，你可以采用下面的两种方式：

- 参考我在前面讲到的方法，也就是打开AVD Manager并创建一台Android模拟器；或是通过open -a Simulator 命令，在不同的iOS模拟器之间进行切换。
- 直接插入Android或iOS真机。

hello_world工程稍微有点特殊，因为它提供了两个Dart启动入口：一个英文版的hello world-main.dart，和一个阿拉伯语版的hello world-arabic.dart。因此，我们可以在Config selector中进行启动入口的选择，也可以直接使用默认的main.dart。

在工具栏中点击 Run图标，稍等10秒钟左右，就可以在模拟器或真机上看到启动的应用程序了。

对于Flutter开发测试，如果每次修改代码都需要重新编译加载的话，那需要等待少则数十秒多则几分钟的时间才能查看样式效果，无疑是非常低效的。

正是因为Flutter在开发阶段使用了JIT编译模式，使得通过热重载（Hot Reload）这样的技术去进一步提升调试效率成为可能。简单来说，热重载就是在无需重新编译代码、重启应用程序、丢失程序执行状态的情况下，就能实时加载修改后的代码，查看改动效果。

> 备注：我会在“02 | 预习篇 · Dart语言概览”中，与你分析Flutter使用Dart语言，同时支持AOT和JIT。

就hello_world示例而言，为了体验热重载，我们还需要对代码做一些改造，将其根节点修改为StatelessWidget：

```
import 'package:flutter/widgets.dart';

class MyAPP extends StatelessWidget {
@override
  Widget build(BuildContext context) {
    return const Center(child: Text('Hello World', textDirection: TextDirection.ltr));
  }
}

void main() => runApp(new MyAPP());
```

点击Run图标，然后试着修改一下代码，保存后仅需几百毫秒就可以看到最新的显示效果。

![9feb8125db2140e8bba9321be76e9cec](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/9feb8125db2140e8bba9321be76e9cec.jpg)

图7 热重载

是不是很Cool！但是，**热重载也有一定的局限性，并不是所有的代码改动都可以通过热重载来更新。**

对hello_world示例而言，由于Flutter并不会在热重载后重新执行main函数，而只会根据原来的根节点重新创建控件树，因此我们刚才做了一些改造之后才支持热重载。

关于Flutter热重载的原理以及限制原因，我会在后面“34 | Hot Reload是怎么做到的？”文章，和你详细分析。现在，你只需要知道，如果热重载不起作用的时候，我们也不需要进行漫长的重新编译加载等待，只要点击位于工程面板左下角的热重启（Hot Restart）按钮就可以以秒级的速度进行代码重编译以及程序重启了，而它与热重载的区别只是因为重启丢失了当前程序的运行状态而已，对实际调试也没什么影响。

![12a477c470b943cabdac4ddf2090bb40](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/12a477c470b943cabdac4ddf2090bb40.jpg)

图8 热重启

#### 总结

通过今天的内容，相信你已经完成了Flutter开发测试环境的安装配置，对如何在安装过程中随时检测工程依赖，以及如何分别在Android和iOS真机及模拟器上运行Flutter程序有了一定的理解，并对Flutter开发调试常用工具有了初步的认知。

善用这些集成工具能够帮助我们能提升Flutter开发效率，而这些有关工程环境的基础知识则为Flutter的学习提供了支撑。这样，如果你后续在开发测试中遇到了环境相关的问题，也就知道应该如何去解决。

#### 思考题

你在搭建Flutter工程环境的过程中，遇到过哪些问题，又是怎么解决的呢？

欢迎留言告诉我，我们一起讨论。感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 预习篇 · Dart语言概览

你好，我是陈航。

我们知道，Flutter开发框架采用的开发语言是Dart，所以要用好这个框架，我们必须要搞清楚Dart语言。

关于新技术的学习，一直以来我都非常认同一个观点：千万不要直接陷入细节里，你应该先鸟瞰其全貌，这样才能从高维度理解问题。所以，为了帮助你更高效地掌握Dart，以最快的速度具备开发一款Flutter应用的能力，今天这篇文章，我会先从Flutter开发的角度，和你介绍Dart语言出现的历史背景、特性以及未来。

然后，我会在本专栏的“Dart基础”模块，与你详细分享它的特性、基础语法、类型变量、函数等知识，并和你分享一个使用Dart的综合案例，帮你学懂、学会这门语言。

如果你已经对Dart有一个初步印象了，也可以跳过这篇预习文章，直接学习后面的内容。

#### Dart是什么？

2011年10月，在丹麦召开的GOTO大会上，Google发布了一种新的编程语言Dart。如同Kotlin和Swift的出现，分别是为了解决Java和Objective-C在编写应用程序的一些实际问题一样，Dart的诞生正是要解决JavaScript存在的、在语言本质上无法改进的缺陷。

那么，**JavaScript到底有哪些问题和缺陷呢？**JavaScript之父布兰登 · 艾克（Brendan Eich）曾在一次采访中说，JavaScript“几天就设计出来了”。

概括来说，他的设计思路是这样的：

- 借鉴C语言的基本语法；
- 借鉴Java语言的数据类型和内存管理机制；
- 借鉴Scheme语言，将函数提升到“第一等公民”（first class）的地位；
- 借鉴Self语言，使用基于原型（prototype）的继承机制。

所以，**JavaScript实际上是两类编程语言风格的混合产物：（简化的）函数式编程风格，与（简化的）面向对象编程风格。**

由于设计时间太短，一些细节考虑得不够严谨，导致后来很长一段时间，使用JavaScript开发的程序混乱不堪。出于对JavaScript的不满，Google的程序员们决定自己写一个新语言来换掉它，所以Dart的最初定位也是一种运行在浏览器中的脚本语言。

而为了推广Dart，Google甚至将自己的Chrome浏览器内置了Dart VM，可以直接高效地运行Dart代码。而对于普通浏览器来说，Google也提供了一套能够将Dart代码编译成JavaScript代码的转换工具。这样一来，开发者们就可以毫无顾虑地使用Dart去开发了，而不必担心兼容问题。再加上出身名门，Dart在一开始就赢得了部分前端开发者的关注。

但，JavaScript的生命力似乎比预想的更强大。

原本JavaScript只能在浏览器中运行，但Node.js的出现让它开始有能力运行在服务端，很快手机应用与桌面应用也成为了JavaScript的宿主容器，一些明星项目比如React、React Native、Vue、Electron、NW（node-webkit）等框架如雨后春笋般崛起，迅速扩展了它的边界。

于是，JavaScript成为了前后端通吃的全栈语言，前端的开发模式也因此而改变，进入了一个新的世界。就如同Atwood定律描述的：凡是能用JavaScript写出来的系统，最终都会用JavaScript写出来（Any application that can be written in JavaScript, will eventually be written in JavaScript.）。

JavaScript因为Node.js焕发了第二春，而Dart就没有那么好的运气了。由于缺少顶级项目的使用，Dart始终不温不火。2015年，在听取了大量开发者的反馈后，Google决定将内置的Dart VM引擎从Chrome移除，这对Dart的发展来说是重大挫折，替代JavaScript就更无从谈起了。

但，Dart也借此机会开始转型：在Google内部孵化了移动开发框架Flutter，弯道超车进入了移动开发的领域；而在Google未来的操作系统Fuchsia中，Dart更是被指定为官方的开发语言。

与此同时，Dart的老本行，浏览器前端的发展也并未停滞。著名的前端框架Angular，除了常见的TS版本外，也在持续迭代对应的Dart版本[AngularDart](https://github.com/dart-lang/angular)。（不过不得不说的是，这个项目的star一直以来只有可怜的1,100出头）。

也正是因为使用者不多、历史包袱少，所以在经历了这么多的故事后，Dart可以彻底转变思路，成为专注大前端与跨平台生态的语言。

接下来，我们就从Flutter开发的视角，聊聊Dart最重要的核心特性吧。

#### Dart的特性

每门语言都有各自的特点，适合自己的才是最好的。

作为移动端开发的后来者，Dart语言可以说是集百家之长，拥有其他优秀编程语言的诸多特性和影子，所以对于其他语言的开发者而言，学习成本无疑是非常低的。同时，Dart拥有的特点则恰到好处，在对Flutter的支持上做到了独一无二。所以，Dart成了Flutter的选择。

下面，我就和你详细分享下它的核心特性。

##### JIT与AOT

借助于先进的工具链和编译器，Dart是少数同时支持JIT（Just In Time，即时编译）和AOT（Ahead of Time，运行前编译）的语言之一。那，到底什么是JIT和AOT呢？

语言在运行之前通常都需要编译，JIT和AOT则是最常见的两种编译模式。

- JIT在运行时即时编译，在开发周期中使用，可以动态下发和执行代码，开发测试效率高，但运行速度和执行性能则会因为运行时即时编译受到影响。
- AOT即提前编译，可以生成被直接执行的二进制代码，运行速度快、执行性能表现好，但每次执行前都需要提前编译，开发测试效率低。

总结来讲，在开发期使用JIT编译，可以缩短产品的开发周期。Flutter最受欢迎的功能之一热重载，正是基于此特性。而在发布期使用AOT，就不需要像React Native那样在跨平台JavaScript代码和原生Android、iOS代码之间建立低效的方法调用映射关系。所以说，Dart具有运行速度快、执行性能好的特点。

那么，**如何区分一门语言究竟是AOT还是JIT呢？**通常来说，看代码在执行前是否需要编译即可。如果需要编译，通常属于AOT；如果不需要，则属于JIT。

AOT的典型代表是C/C++，它们必须在执行前编译成机器码；而JIT的代表，则包括了如JavaScript、Python等几乎所有的脚本语言。

##### 内存分配与垃圾回收

Dart VM的内存分配策略比较简单，创建对象时只需要在堆上移动指针，内存增长始终是线性的，省去了查找可用内存的过程。

在Dart中，并发是通过Isolate实现的。Isolate是类似于线程但不共享内存，独立运行的worker。这样的机制，就可以让Dart实现无锁的快速分配。

Dart的垃圾回收，则是采用了多生代算法。新生代在回收内存时采用“半空间”机制，触发垃圾回收时，Dart会将当前半空间中的“活跃”对象拷贝到备用空间，然后整体释放当前空间的所有内存。回收过程中，Dart只需要操作少量的“活跃”对象，没有引用的大量“死亡”对象则被忽略，这样的回收机制很适合Flutter框架中大量Widget销毁重建的场景。

##### 单线程模型

支持并发执行线程的高级语言（比如，C++、Java、Objective-C），大都以抢占式的方式切换线程，即：每个线程都会被分配一个固定的时间片来执行，超过了时间片后线程上下文将被抢占后切换。如果这时正在更新线程间的共享资源，抢占后就可能导致数据不同步的问题。

解决这一问题的典型方法是，使用锁来保护共享资源，但锁本身又可能会带来性能损耗，甚至出现死锁等更严重的问题。

这时，Dart是单线程模型的优势就体现出来了，因为它天然不存在资源竞争和状态同步的问题。这就意味着，一旦某个函数开始执行，就将执行到这个函数结束，而不会被其他Dart代码打断。

所以，**Dart中并没有线程，只有Isolate（隔离区）**。Isolates之间不会共享内存，就像几个运行在不同进程中的worker，通过事件循环（Event Looper）在事件队列（Event Queue）上传递消息通信。

##### 无需单独的声明式布局语言

在Flutter中，界面布局直接通过Dart编码来定义。

Dart声明式编程布局易于阅读和可视化，使得Flutter并不需要类似JSX或XML的声明式布局语言。所有的布局都使用同一种格式，也使得Flutter很容易提供高级工具使布局更简单。

开发过程也不需要可视化界面构建器，因为热重载可以让我们立即在手机上看到运行效果。

#### Dart的未来

那么，在这样的背景下诞生的Dart，今后发展会怎样呢?

Dart是一个优秀而年轻的现代语言，但一种编程语言并不是搞定了引擎和开发者接口就算完成了，而是必须在这个语言得以立足的库、框架、 应用程序等“生态”都成熟起来之后，其价值才会真正开始体现。而要走到这一步，通常需要花上数年的时间。

目前，基于Dart语言的第三方库还很少，并且质量一般，不过值得庆幸的是，因为Flutter和Fuchsia的推动，Dart SDK更新迭代的速度快了很多，开发者的热情也急剧增长，Dart生态增速很快。

毕竟，在Dart社区目前最顶级的产品就是Flutter和Fuchsia了，因此Dart开发者主要以Flutter开发者居多，当然了也有用Dart开发浏览器前端的开发者，但人数并不多。所以，**我觉得Dart是否能够成功，目前来看主要取决于Flutter和Fuchsia能否成功**。**而，Flutter是构建Fuchsia的UI开发框架，因此这个问题也变成了Flutter能否成功。**

正如我在开篇词中提到的，Flutter正式版发布也就半年多的时间，在GitHub上Star就已经超过了68,000，仅落后React Native 10,000左右，可见热度之高。

现在，我们一起回到Flutter自身来看，它的出现提供了一套彻底的跨平台方案，也确实弥补了当今跨平台开发框架的短板，解决了业界痛点，极有可能成为跨平台开发领域的终极解决方案，前途光明，未来非常值得期待。

至此，我们已经可以清晰地看到，Google在遭受与Oracle的Java侵权案后，痛定思痛后下定决心要发展自己的语言生态的布局愿景：Dart凭借Flutter与Fuchsia的生态主攻前端和移动端，而服务端，则有借助于Docker的火热势头增长迅猛的Go语言。

所以说，Google的布局不仅全面，应用和影响也非常广泛，前后端均有杀手级产品用来构建语言生态。相信随着Google新系统Fuchsia的发布，Flutter和Dart会以更迅猛的速度释放它们的力量，而Google统一前后端开发技能栈的愿望也会在一定程度上得以实现。

#### 总结

今天，我带你了解了Dart出现的历史背景，从Flutter开发者的视角详细介绍了Dart语言的各种特性，并分析了Dart的未来发展。

Dart是一门现代语言，集合了各种优秀语言的优点。如果你不了解Dart也无需担心，只要你有过其他编程语言，尤其是Java、JavaScript、Swift或Objective-C编程经验的话，可以很容易地在Dart身上找它们的影子，以极低的成本快速上手。

希望通过这篇文章，你可以先对Dart语言有个初步了解，为我们接下来的学习打好基础。在本专栏的“Dart基础”模块中，我会对照着其他编程语言的特性，和你讲述Dart与它们相似的设计理念，帮助你快速建立起构建Flutter程序的所需要的Dart知识体系。

#### 思考题

对于学习Dart或是其他编程语言，你有什么困扰或者心得吗？

欢迎你在评论区给我留言分享你的经历和观点，我会在下一篇文章中等你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 深入理解跨平台方案的历史发展逻辑

你好，我是陈航。

今天，我会从跨平台开发方案的诞生背景、原理和发展历史的角度，和你聊聊这些常见的开发方案，以及针对不同的场景我们应该如何选择对应的方案。

#### 浅述跨平台开发的背景

我们当下所处的移动互联网时代，以它独有的变革方式，带给我们快捷、经济、安全和方便，改变着生活的方方面面。而对于企业来说，移动应用已然成为各类手机终端上一张必备的产品名片。

在移动互联网的浪潮下，我们开发的应用要想取胜，开发效率和使用体验可以说是同等重要。但是，使用原生的方式来开发App，就要求我们必须针对iOS和Android这两个平台分别开发，这对于中小型团队来说就是隐患和额外的负担。

因为这样的话，我们不仅需要在不同的项目间尝试用不同的语言去实现同样的功能，还要承担由此带来的维护任务。如果还要继续向其他平台（比如Web、Mac或Windows）拓展的话，我们需要付出的成本和时间将成倍增长。而这，显然是难以接受的。于是，跨平台开发的概念顺势走进了我们的视野。

所以从本质上讲，**跨平台开发是为了增加业务代码的复用率，减少因为要适配多个平台带来的工作量，从而降低开发成本。**在提高业务专注度的同时，能够为用户提供一致的用户体验。用一个词来概括这些好处的话，就是“多快好省”。

“一次编码，到处运行”。二十多年前Java正是以跨平台特性的口号登场，击败了众多竞争对手。这个口号，意味着Java可以在任何平台上进行开发，然后编译成一段标准的字节码后，就可以运行在任何安装有Java虚拟机（JVM）的设备上。虽然现在跨平台已经不是Java的最大优势（而是它繁荣的生态），但不可否认它当年打着跨平台旗号横空出世确实势不可挡。

而对于移动端开发来讲，如果能实现“一套代码，多端运行”，这样的技术势必会引发新的生产力变革，在目前多终端时代的大环境下，可以为企业节省人力资源上，从而带来直接的经济效益。

伴随着移动端的诞生和繁荣，为了满足人们对开发效率和用户体验的不懈追求，各种跨平台的开发方案也如雨后春笋般涌现。除了React Native和Flutter之外，这几年还出现过许多其他的解决方案，接下来我将会为你一一分析这些方案。这样，你在选择适合自己的移动开发框架时，也就有章可循了。

在此，我特地强调一下，我在下文提到的跨平台开发方案，如果没有特殊说明的话，指的就是跨iOS和Android开发。

#### 跨平台开发方案的三个时代

根据实现方式的不同，业内常见的观点是将主流的跨平台方案划分为三个时代。

- Web容器时代：基于Web相关技术通过浏览器组件来实现界面及功能，典型的框架包括Cordova(PhoneGap)、Ionic和微信小程序。
- 泛Web容器时代：采用类Web标准进行开发，但在运行时把绘制和渲染交由原生系统接管的技术，代表框架有React Native、Weex和快应用，广义的还包括天猫的Virtual View等。
- 自绘引擎时代：自带渲染引擎，客户端仅提供一块画布即可获得从业务逻辑到功能呈现的多端高度一致的渲染体验。Flutter，是为数不多的代表。

接下来，我们先看一下目前使用最广泛的Web容器方案。

##### Web容器时代

Web时代的方案，主要采用的是原生应用内嵌浏览器控件WebView（iOS为UIWebView或WKWebView，Android为WebView）的方式进行HTML5页面渲染，并定义HTML5与原生代码交互协议，将部分原生系统能力暴露给HTML5，从而扩展HTML5的边界。这类交互协议，就是我们通常说的JS Bridge（桥）。

这种开发模式既有原生应用代码又有Web应用代码，因此又被称为Hybrid开发模式。由于HTML5代码只需要开发一次，就能同时在多个系统运行，因此大大降低了开发成本。

由于采用了Web开发技术，社区和资源非常丰富，开发效率也很高。但，**一个完整HTML5页面的展示要经历浏览器控件的加载、解析和渲染三大过程，性能消耗要比原生开发增加N个数量级**。

接下来，我以加载过程为例，和你说明这个过程的复杂性。

1. 浏览器控件加载HTML5页面的HTML主文档；
2. 加载过程中遇到外部CSS文件，浏览器另外发出一个请求，来获取CSS文件；
3. 遇到图片资源，浏览器也会另外发出一个请求，来获取图片资源。这是异步请求，并不会影响HTML文档的加载。
4. 加载过程中遇到JavaScript文件，由于JavaScript代码可能会修改DOM树，因此HTML文档会挂起渲染（加载解析渲染同步）的线程，直到JavaScript文件加载解析并执行完毕，才可以恢复HTML文档的渲染线程。
5. JavaScript代码中有用到CSS文件中的属性样式，于是阻塞，等待CSS加载完毕才能恢复执行。

而这，只是完成HTML5页面渲染的最基础的加载过程。加载、解析和渲染这三个过程在实际运行时又不是完全独立的，还会有交叉。也就是说，会存在一边加载，一边解析，一边渲染的现象。这，就使得页面的展示并不像想象中那么容易。

通过上面的分析你可以看出，一个HTML5页面的展示是多么得复杂！这和原生开发通过简单直接的创建控件，设置属性后即可完成页面渲染有非常大的差异。Web与原生在UI渲染与系统功能调用上各司其职，因此这个时代的框架在Web与原生系统间还有比较明显的、甚至肉眼可见的边界。

![0b01418fc6c24aa2b4fc1e06eb275632](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0b01418fc6c24aa2b4fc1e06eb275632.jpg)

图1 Hybrid开发框架

我也曾碰到过很多人觉得跨平台开发不靠谱。但其实，Web容器方案是跨平台开发历史上最成功的例子。也正是因为它太成功了，以至于很多人都忽略了它也是跨平台方案之一。

##### 泛Web容器时代

虽然Web容器方案具有生态繁荣、开发体验友好、生产效率高、跨平台兼容性强等优势，但它最大的问题在于承载着大量Web标准的Web容器过于笨重，以至于性能和体验都达不到与原生同样的水准，在复杂交互和动画上较难实现出优良的用户体验。

而在实际的产品功能研发中，我们通常只会用到Web标准中很小的一部分。面对这样的现实，我们很快就想到：能否对笨重的Web容器进行功能裁剪，在仅保留必要的Web标准和渲染能力的基础上，使得友好的开发体验与稳定的渲染性能保持一个平衡？

答案当然是可以。

泛Web容器时代的解决方案优化了Web容器时代的加载、解析和渲染这三大过程，把影响它们独立运行的Web标准进行了裁剪，以相对简单的方式支持了构建移动端页面必要的Web标准（如Flexbox等），也保证了便捷的前端开发体验；同时，这个时代的解决方案基本上完全放弃了浏览器控件渲染，而是采用原生自带的UI组件实现代替了核心的渲染引擎，仅保持必要的基本控件渲染能力，从而使得渲染过程更加简化，也保证了良好的渲染性能。

也就是说，在泛Web容器时代，我们仍然采用前端友好的JavaScript进行开发，整体加载、渲染机制大大简化，并且由原生接管绘制，即将原生系统作为渲染的后端，为依托于JavaScript虚拟机的JavaScript代码提供所需要的UI控件的实体。这，也是现在绝大部分跨平台框架的思路，而React Native和Weex就是其中的佼佼者。

![4b6a186469114f359926c451bb18a0c6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4b6a186469114f359926c451bb18a0c6.jpg)

图2 泛Web容器框架

为了追求性能体验的极致，并进一步维持方案的简单可扩展性，有些轻量级的跨平台方案甚至会完全抛弃Web标准、放弃JavaScript的动态执行能力而自创一套原生DSL，如天猫的[VirtualView](http://pingguohe.net/2017/12/07/Tangram-2.html)框架。从广义上来说，这些方案也是泛Web容器类方案。

##### 自绘引擎时代

泛Web容器时代使用原生控件承载界面渲染，固然解决了不少性能问题，但同时也带来了新的问题。抛开框架本身需要处理大量平台相关的逻辑外，随着系统版本变化和API的变化，我们还需要处理不同平台的原生控件渲染能力差异，修复各类奇奇怪怪的Bug。始终需要Follow Native的思维方式，就使得泛Web容器框架的跨平台特性被大打折扣。

而这一时期的代表Flutter则开辟了一种全新的思路，即从头到尾重写一套跨平台的UI框架，包括渲染逻辑，甚至是开发语言。

- 渲染引擎依靠跨平台的Skia图形库来实现，Skia引擎会将使用Dart构建的抽象的视图结构数据加工成GPU数据，交由OpenGL最终提供给GPU渲染，至此完成渲染闭环，因此可以在最大程度上保证一款应用在不同平台、不同设备上的体验一致性。
- 而开发语言选用的是同时支持JIT（Just-in-Time，即时编译）和AOT（Ahead-of-Time，预编译）的Dart，不仅保证了开发效率，更提升了执行效率（比使用JavaScript开发的泛Web容器方案要高得多）。

![612dec551a8349359978978071991f69](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/612dec551a8349359978978071991f69.jpg)

图3 自绘引擎开发框架

通过这样的思路，Flutter可以尽可能地减少不同平台之间的差异, 同时保持和原生开发一样的高性能。所以说，Flutter成了三类跨平台移动开发方案中最灵活的那个，也成了目前最受业界关注的框架。

现在，我们已经弄明白了三类跨平台方案，那么我在开发应用的时候，到底应该如何选择最适合自己的框架呢？

#### 我该选择哪一类跨平台开发方案？

从不同的角度来看，三个时代的跨平台框架代表们在开发效率、渲染性能、维护成本和社区生态上各有优劣，如下图所示：

![4adc44fabd194237bd2df72bfaeb2fed](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4adc44fabd194237bd2df72bfaeb2fed.jpg)

图 4 主流跨平台框架对比

我们在做技术选型时，可以参考以上维度，从开发效率、技术栈、性能表现、维护成本和社区生态来进行综合考虑。比如，是否必须支持动态化？是只解决Android、iOS的跨端问题，还是要包括Web？对性能要求如何？对多端体验的绝对一致性和维护成本是否有强诉求？

从各个维度综合考量，React Native和Flutter无疑是最均衡的两种跨平台开发方案，而其他的方案或多或少都“偏科严重”。

- React Native依托于Facebook，经过4年多的发展已经成长为跨平台开发方案的实际领导者，并拥有较为丰富的第三方库和开发社区；
- Flutter以挑战者姿态出现在我们的面前，可以提供更彻底的跨平台技术解决方案。虽然Flutter推出时间不长，但也有了诸多商用案例，加上清晰的[产品路线图](https://mp.weixin.qq.com/s/aRhQdMd0R74adph9_V0wgQ)和Google的强大号召力，Flutter未来的发展非常值得期待。

那么问题来了，我究竟应该选择React Native还是Flutter呢？

在这里，我和你说一下我的建议吧。

**对于知识学习来说，**这两个应用层面的框架最好都学。学习的过程中最重要的是打好基础，深入理解框架的原理和设计思想，重点思考它们的API设计的取舍，发现它们的共性和差异。

Flutter作为后来者，也从React Native社区学习和借鉴了不少的优秀设计，很多概念两边都有对应，比如React Native的Component和Flutter的Widget、Flex布局思想、状态管理和函数式编程等等，这类的知识都是两个框架通用的技术。**未来也许还会出现新的解决方案，老框架也会不断更新，只有掌握核心原理才能真正立于不败之地。**

**对于实际项目来说，**这两个框架都已达到了大面积商业应用的标准。综合成熟度和生态，目前俩看React Native略胜Flutter。因此，如果是中短期项目的话，我建议使用React Native。但作为技术选型，我们要看得更远一些。Flutter的设计理念比较先进，解决方案也相对彻底，在渲染能力的一致性以及性能上，和React Native相比优势非常明显。

此外，Flutter的野心不仅仅是移动端。前段时间，Google团队已经完成了Hummingbird，即Flutter的Web的官方Demo，在桌面操作系统的探索上也取得了进展，未来大前端技术栈是否会由Flutter完成统一，值得期待。

#### 小结

这就是今天分享的全部内容了。

在不同平台开发和维护同一个产品，所付出的成本一直以来一个令人头疼的问题，于是各类跨平台开发方案顺应而生。从Web容器时代到以React Native、Weex为代表的泛Web容器时代，最后再到以Flutter为代表的自绘引擎时代，这些优秀的跨平台开发框架们慢慢抹平了各个平台的差异，使得操作系统的边界变得越来越模糊。

与此同时，这个时代对开发者的要求也到达了一个新的阶段，拥抱大前端的时代已经向我们走来。在这个专栏里，我会假设你有一定的前端（Android、iOS或Web）开发基础。比如，你知道View是什么，路由是什么，如何实现一个基本页面布局等等。我会让希望迅速掌握Flutter开发的爱好者们，通过一种比较熟悉和友好的路径去学习Flutter相关的代码和程序，以及背后的原理和设计思想。

#### 思考题

你有哪些跨平台开发框架的使用经历呢？

欢迎你在评论区给我留言分享你的经历和观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### Flutter区别于其他方案的关键技术是什么？

你好，我是陈航。

Flutter是什么？它出现的动机是什么，解决了哪些痛点？相比其他跨平台技术，Flutter的优势在哪里？……相信很多人在第一眼看到Flutter时，都会有类似的疑问。

别急，在今天的这篇文章中，我会与你介绍Flutter的历史背景和运行机制，并以界面渲染过程为例与你讲述其实现原理，让你对Flutter能够有一个全方位的认知和感受。在对Flutter有了全面了解后，这些疑问自然也就迎刃而解了。

接下来，我们就从Flutter出现的历史背景开始谈起吧。

#### Flutter出现的历史背景

为不同的操作系统开发拥有相同功能的应用程序，开发人员只有两个选择：

1. 使用原生开发语言（即Java和Objective-C），针对不同平台分别进行开发。
2. 使用跨平台解决方案，对不同平台进行统一开发。

原生开发方式的体验最好，但研发效率和研发成本相对较高；而跨平台开发方式研发虽然效率高，但为了抹平多端平台差异，各类解决方案暴露的组件和API较原生开发相比少很多，因此研发体验和产品功能并不完美。

所以，最成功的跨平台开发方案其实是依托于浏览器控件的Web。浏览器保证了99%的概率下Web的需求都是可以实现的，不需要业务将就“技术”。不过，Web最大的问题在于它的性能和体验与原生开发存在肉眼可感知的差异，因此并不适用于对体验要求较高的场景。

对于用户体验更接近于原生的React Native，对业务的支持能力却还不到浏览器的5%，仅适用于中低复杂度的低交互类页面。面对稍微复杂一点儿的交互和动画需求，开发者都需要case by case地去review，甚至还可能要通过原生代码去扩展才能实现。

这些因素，也就导致了虽然跨平台开发从移动端诞生之初就已经被多次提及，但到现在也没有被很好地解决。

带着这些问题，我们终于迎来了本次专栏的主角——Flutter。

Flutter是构建Google物联网操作系统Fuchsia的SDK，主打跨平台、高保真、高性能。开发者可以通过 Dart语言开发App，一套代码可以同时运行在 iOS 和 Android平台。 Flutter使用Native引擎渲染视图，并提供了丰富的组件和接口，这无疑为开发者和用户都提供了良好的体验。

从2017年5月，谷歌公司发布的了Alpha版本的Flutter，到2018年底Flutter Live发布的1.0版本，再到现在最新的1.5版本（截止至2019年7月1日），Flutter正在赢得越来越多的关注。

很多人开始感慨，跨平台技术似乎终于迎来了最佳解决方案。那么，接下来我们就从原理层面去看看，Flutter是如何解决既有跨平台开发方案问题的。

#### Flutter是怎么运转的？

与用于构建移动应用程序的其他大多数框架不同，Flutter是重写了一整套包括底层渲染逻辑和上层开发语言的完整解决方案。这样不仅可以保证视图渲染在Android和iOS上的高度一致性（即高保真），在代码执行效率和渲染性能上也可以媲美原生App的体验（即高性能）。

这，就是Flutter和其他跨平台方案的本质区别：

- React Native之类的框架，只是通过JavaScript虚拟机扩展调用系统组件，由Android和iOS系统进行组件的渲染；
- Flutter则是自己完成了组件渲染的闭环。

那么，**Flutter是怎么完成组件渲染的呢**？这需要从图像显示的基本原理说起。

在计算机系统中，图像的显示需要CPU、GPU和显示器一起配合完成：CPU负责图像数据计算，GPU负责图像数据渲染，而显示器则负责最终图像显示。

CPU把计算好的、需要显示的内容交给GPU，由GPU完成渲染后放入帧缓冲区，随后视频控制器根据垂直同步信号（VSync）以每秒60次的速度，从帧缓冲区读取帧数据交由显示器完成图像显示。

操作系统在呈现图像时遵循了这种机制，而Flutter作为跨平台开发框架也采用了这种底层方案。下面有一张更为详尽的示意图来解释Flutter的绘制原理。

![c391ca66da994ebd801684828d3afdf6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c391ca66da994ebd801684828d3afdf6.jpg)

图1 Flutter绘制原理

可以看到，Flutter关注如何尽可能快地在两个硬件时钟的VSync信号之间计算并合成视图数据，然后通过Skia交给GPU渲染：UI线程使用Dart来构建视图结构数据，这些数据会在GPU线程进行图层合成，随后交给Skia引擎加工成GPU数据，而这些数据会通过OpenGL最终提供给GPU渲染。

在进一步学习Flutter之前，我们有必要了解下构建Flutter的关键技术，即Skia和Dart。

#### Skia是什么？

要想了解Flutter，你必须先了解它的底层图像渲染引擎Skia。因为，Flutter只关心如何向GPU提供视图数据，而Skia就是它向GPU提供视图数据的好帮手。

Skia是一款用C++开发的、性能彪悍的2D图像绘制引擎，其前身是一个向量绘图软件。2005年被Google公司收购后，因为其出色的绘制表现被广泛应用在Chrome和Android等核心产品上。Skia在图形转换、文字渲染、位图渲染方面都表现卓越，并提供了开发者友好的API。

因此，架构于Skia之上的Flutter，也因此拥有了彻底的跨平台渲染能力。通过与Skia的深度定制及优化，Flutter可以最大限度地抹平平台差异，提高渲染效率与性能。

底层渲染能力统一了，上层开发接口和功能体验也就随即统一了，开发者再也不用操心平台相关的渲染特性了。也就是说，Skia保证了同一套代码调用在Android和iOS平台上的渲染效果是完全一致的。

#### 为什么是Dart？

除了我们在第2篇预习文章“[预习篇 · Dart语言概览](https://time.geekbang.org/column/article/104071)”中提到的，Dart因为同时支持AOT和JIT，所以具有运行速度快、执行性能好的特点外，Flutter为什么选择了Dart，而不是前端应用的准官方语言JavaScript呢？这个问题很有意思，但也很有争议。

很多人说，选择Dart是Flutter推广的一大劣势，毕竟多学一门新语言就多一层障碍。想想Java对Android，JavaScript对NodeJS的推动，如果换个语言可能就不一样了。

但，**Google公司给出的原因很简单也很直接**：Dart语言开发组就在隔壁，对于Flutter需要的一些语言新特性，能够快速在语法层面落地实现；而如果选择了JavaScript，就必须经过各种委员会和浏览器提供商漫长的决议。

事实上，Flutter的确得到了兄弟团队的紧密支持。2018年2月发布的Dart 2.0，2018年12月发布的Dart 2.1，2019年2月发布的Dart 2.2，2019年5月发布的Dart2.3，每次发布都包含了为Flutter量身定制的诸多改造（比如，改进的AOT性能、更智能的类型隐式转换等）。

当然，Google公司选择使用Dart作为Flutter的开发语言，我想还有其他更有说服力的理由：

1. Dart同时支持即时编译JIT和事前编译AOT。在开发期使用JIT，开发周期异常短，调试方式颠覆常规（支持有状态的热重载）；而发布期使用AOT，本地代码的执行更高效，代码性能和用户体验也更卓越。
2. Dart作为一门现代化语言，集百家之长，拥有其他优秀编程语言的诸多特性（比如，完善的包管理机制）。也正是这个原因，Dart的学习成本并不高，很容易上手。
3. Dart避免了抢占式调度和共享内存，可以在没有锁的情况下进行对象分配和垃圾回收，在性能方面表现相当不错。

Dart是一门优秀的现代语言，最初设计也是为了取代JavaScript成为Web开发的官方语言。竞争对手如此强劲，最后的结果可想而知。这，也是为什么相比于其他热门语言，Dart的生态要冷清不少的原因。

而随着Flutter的发布，Dart开始转型，其自身定位也发生了变化，专注于改善构建客户端应用程序的体验，因此越来越多的开发者开始慢慢了解、学习这门语言，并共同完善它的生态。凭借着Flutter的火热势头，辅以Google强大的商业运作能力，相信转型后的Dart前景会非常光明。

#### Flutter的原理

在了解了Flutter的基本运作机制后，我们再来深入了解一下Flutter的实现原理。

首先，我们来看一下Flutter的架构图。我希望通过这张图以及对应的解读，你能在开始学习的时候就建立起对Flutter的整体印象，能够从框架设计和实现原理的高度去理解Flutter区别其他跨平台解决方案的关键所在，为后面的学习打好基础，而不是直接一上来就陷入语言和框架的功能细节“泥潭”而无法自拔。

![9093f09dc47e434a80fd7d88e90b1624](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/9093f09dc47e434a80fd7d88e90b1624.jpg)

图2 Flutter架构图

备注：此图引自[Flutter System Overview](https://flutter.dev/docs/resources/technical-overview)

Flutter架构采用分层设计，从下到上分为三层，依次为：Embedder、Engine、Framework。

- Embedder是操作系统适配层，实现了渲染Surface设置，线程设置，以及平台插件等平台相关特性的适配。从这里我们可以看到，Flutter平台相关特性并不多，这就使得从框架层面保持跨端一致性的成本相对较低。
- Engine层主要包含Skia、Dart和Text，实现了Flutter的渲染引擎、文字排版、事件处理和Dart运行时等功能。Skia和Text为上层接口提供了调用底层渲染和排版的能力，Dart则为Flutter提供了运行时调用Dart和渲染引擎的能力。而Engine层的作用，则是将它们组合起来，从它们生成的数据中实现视图渲染。
- Framework层则是一个用Dart实现的UI SDK，包含了动画、图形绘制和手势识别等功能。为了在绘制控件等固定样式的图形时提供更直观、更方便的接口，Flutter还基于这些基础能力，根据Material和Cupertino两种视觉设计风格封装了一套UI组件库。我们在开发Flutter的时候，可以直接使用这些组件库。

接下来，我**以界面渲染过程为例，和你介绍Flutter是如何工作的。**

页面中的各界面元素（Widget）以树的形式组织，即控件树。Flutter通过控件树中的每个控件创建不同类型的渲染对象，组成渲染对象树。而渲染对象树在Flutter的展示过程分为四个阶段：布局、绘制、合成和渲染。

##### 布局

Flutter采用深度优先机制遍历渲染对象树，决定渲染对象树中各渲染对象在屏幕上的位置和尺寸。在布局过程中，渲染对象树中的每个渲染对象都会接收父对象的布局约束参数，决定自己的大小，然后父对象按照控件逻辑决定各个子对象的位置，完成布局过程。

![42cc8bdbb80744fcb2594065268ba497](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/42cc8bdbb80744fcb2594065268ba497.jpg)

图3 Flutter布局过程

为了防止因子节点发生变化而导致整个控件树重新布局，Flutter加入了一个机制——布局边界（Relayout Boundary），可以在某些节点自动或手动地设置布局边界，当边界内的任何对象发生重新布局时，不会影响边界外的对象，反之亦然。

![81aea8d6382346e68d6a5e13ce88b3c7](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/81aea8d6382346e68d6a5e13ce88b3c7.jpg)

图4 Flutter布局边界

##### 绘制

布局完成后，渲染对象树中的每个节点都有了明确的尺寸和位置。Flutter会把所有的渲染对象绘制到不同的图层上。与布局过程一样，绘制过程也是深度优先遍历，而且总是先绘制自身，再绘制子节点。

以下图为例：节点1在绘制完自身后，会再绘制节点2，然后绘制它的子节点3、4和5，最后绘制节点6。

![eae1b893f8924403ab1f8d29ae4bc9cd](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/eae1b893f8924403ab1f8d29ae4bc9cd.jpg)

图5 Flutter 绘制示例

可以看到，由于一些其他原因（比如，视图手动合并）导致2的子节点5与它的兄弟节点6处于了同一层，这样会导致当节点2需要重绘的时候，与其无关的节点6也会被重绘，带来性能损耗。

为了解决这一问题，Flutter提出了与布局边界对应的机制——重绘边界（Repaint Boundary）。在重绘边界内，Flutter会强制切换新的图层，这样就可以避免边界内外的互相影响，避免无关内容置于同一图层引起不必要的重绘。

![3da36a61b5c04efda688016b85a5f4f9](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/3da36a61b5c04efda688016b85a5f4f9.jpg)

图6 Flutter重绘边界

重绘边界的一个典型场景是Scrollview。ScrollView滚动的时候需要刷新视图内容，从而触发内容重绘。而当滚动内容重绘时，一般情况下其他内容是不需要重绘的，这时候重绘边界就派上用场了。

##### 合成和渲染

终端设备的页面越来越复杂，因此Flutter的渲染树层级通常很多，直接交付给渲染引擎进行多图层渲染，可能会出现大量渲染内容的重复绘制，所以还需要先进行一次图层合成，即将所有的图层根据大小、层级、透明度等规则计算出最终的显示效果，将相同的图层归类合并，简化渲染树，提高渲染效率。

合并完成后，Flutter会将几何图层数据交由Skia引擎加工成二维图像数据，最终交由GPU进行渲染，完成界面的展示。这部分内容，我已经在前面的内容中介绍过，这里就不再赘述了。

接下来，我们再看看学习Flutter，都需要学习哪些知识。

#### 学习Flutter需要掌握哪些知识？

终端设备越来越碎片化，需要支持的操作系统越来越多，从研发效率和维护成本综合考虑，跨平台开发一定是未来大前端的趋势，我们应该拥抱变化。而Flutter提供了一套彻底的移动跨平台方案，也确实弥补了如今跨平台开发框架的短板，解决了业界痛点，极有可能成为跨平台开发领域的终极解决方案，前途非常光明。

那么，**我们学习Flutter都需要掌握哪些知识呢？**

我按照App的开发流程（开发、调试测试、发布与线上运维）将Flutter的技术栈进行了划分，里面几乎包含了Flutter开发需要的所有知识点。而这些所有知识点，我会在专栏中为你一一讲解。掌握了这些知识点后，你也就具备了企业级应用开发的必要技能。

这些知识点，如下图所示：

![a1a73043ee114500836f0be30d115cfe](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a1a73043ee114500836f0be30d115cfe.jpg)

图7 Flutter知识体系

有了这张图，你是否感觉到学习Flutter的路线变得更加清晰了呢？

#### 小结

今天，我带你了解了Flutter的历史背景与运行机制，并以界面渲染过程为例，从布局、绘制、合成和渲染四个阶段讲述了Flutter的实现原理。此外，我向你介绍了构建Flutter底层的关键技术：Skia与Dart，它们是Flutter有别于其他跨平台开发方案的核心所在。

最后，我梳理了一张Flutter学习思维导图，围绕一个应用的迭代周期介绍了Flutter相关的知识点。我希望通过这个专栏，能和你把Flutter背后的设计原理和知识体系讲清楚，让你能对Flutter有一个整体感知。这样，在你学完这个专栏以后，就能够具备企业级应用开发的理论基础与实践。

#### 思考题

你是如何理解Flutter的三大特点：跨平台、高保真、高性能的？你又打算怎么学习这个专栏呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 从标准模板入手，体会Flutter代码是如何运行在原生系统上的

你好，我是陈航。

在专栏的第一篇预习文章中，我和你一起搭建了Flutter的开发环境，并且通过自带的hello_world示例，和你演示了Flutter项目是如何运行在Android和iOS模拟器以及真机上的。

今天，我会通过Android Studio创建的Flutter应用模板，带你去了解Flutter的项目结构，分析Flutter工程与原生Android和iOS工程有哪些联系，体验一个有着基本功能的Flutter应用是如何运转的，从而加深你对构建Flutter应用的关键概念和技术的理解。

如果你现在还不熟悉Dart语言也不用担心，只要能够理解基本的编程概念（比如，类型、变量、函数和面向对象），并具备一定的前端基础（比如，了解View是什么、页面基本布局等基础知识），就可以和我一起完成今天的学习。而关于Dart语言基础概念的讲述、案例分析，我会在下一个模块和你展开。

#### 计数器示例工程分析

首先，我们打开Android Studio，创建一个Flutter工程应用flutter_app。Flutter会根据自带的应用模板，自动生成一个简单的计数器示例应用Demo。我们先运行此示例，效果如下：

![a923839df71e4663819e1e9a8cf3b6bc](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a923839df71e4663819e1e9a8cf3b6bc.jpg)

图1 计数器示例运行效果

每点击一次右下角带“+”号的悬浮按钮，就可以看到屏幕中央的数字随之+1。

##### 工程结构

在体会了示例工程的运行效果之后，我们再来看看Flutter工程目录结构，了解Flutter工程与原生Android和iOS工程之间的关系，以及这些关系是如何确保一个Flutter程序可以最终运行在Android和iOS系统上的。

![f8abcbcd16b744bdb6a3f6ff2769bb30](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/f8abcbcd16b744bdb6a3f6ff2769bb30.jpg)

图2 Flutter工程目录结构

可以看到，除了Flutter本身的代码、资源、依赖和配置之外，Flutter工程还包含了Android和iOS的工程目录。

这也不难理解，因为Flutter虽然是跨平台开发方案，但却需要一个容器最终运行到Android和iOS平台上，所以**Flutter工程实际上就是一个同时内嵌了Android和iOS原生子工程的父工程**：我们在lib目录下进行Flutter代码的开发，而某些特殊场景下的原生功能，则在对应的Android和iOS工程中提供相应的代码实现，供对应的Flutter代码引用。

Flutter会将相关的依赖和构建产物注入这两个子工程，最终集成到各自的项目中。而我们开发的Flutter代码，最终则会以原生工程的形式运行。

##### 工程代码

在对Flutter的工程结构有了初步印象之后，我们就可以开始学习Flutter的项目代码了。

Flutter自带的应用模板，也就是这个计数器示例，对初学者来说是一个极好的入门范例。在这个简单示例中，从基础的组件、布局到手势的监听，再到状态的改变，Flutter最核心的思想在这60余行代码中展现得可谓淋漓尽致。

为了便于你学习理解，领会构建Flutter程序的大体思路与关键技术，而不是在一开始时就陷入组件的API细节中，我删掉了与核心流程无关的组件配置代码及布局逻辑，在不影响示例功能的情况下对代码进行了改写，并将其分为两部分：

- 第一部分是应用入口、应用结构以及页面结构，可以帮助你理解构建Flutter程序的基本结构和套路；
- 第二部分则是页面布局、交互逻辑及状态管理，能够帮你理解Flutter页面是如何构建、如何响应交互，以及如何更新的。

首先，我们来看看**第一部分的代码**，也就是应用的整体结构：

```
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(home: MyHomePage(title: 'Flutter Demo Home Page'));
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  Widget build(BuildContext context) => {...};
}
```

在本例中，Flutter应用为MyApp类的一个实例，而MyApp类继承自StatelessWidget类，这也就意味着应用本身也是一个Widget。事实上，在Flutter中，Widget是整个视图描述的基础，在Flutter的世界里，包括应用、视图、视图控制器、布局等在内的概念，都建立在Widget之上，**Flutter的核心设计思想便是一切皆Widget**。

Widget是组件视觉效果的封装，是UI界面的载体，因此我们还需要为它提供一个方法，来告诉Flutter框架如何构建UI界面，这个方法就是build。

在build方法中，我们通常通过对基础Widget进行相应的UI配置，或是组合各类基础Widget的方式进行UI的定制化。比如在MyApp中，我通过MaterialApp这个Flutter App框架设置了应用首页，即MyHomePage。当然，MaterialApp也是一个Widget。

MaterialApp类是对构建material设计风格应用的组件封装框架，里面还有很多可配置的属性，比如应用主题、应用名称、语言标识符、组件路由等。但是，这些配置属性并不是本次分享的重点，如果你感兴趣的话，可以参考Flutter官方的[API文档](https://api.flutter.dev/flutter/material/MaterialApp/MaterialApp.html)，来了解MaterialApp框架的其他配置能力。

MyHomePage是应用的首页，继承自StatefulWidget类。这，代表着它是一个有状态的Widget（Stateful Widget），而_MyHomePageState就是它的状态。

如果你足够细心的话就会发现，虽然MyHomePage类也是Widget，但与MyApp类不同的是，它并没有一个build方法去返回Widget，而是多了一个createState方法返回_MyHomePageState对象，而build方法则包含在这个_MyHomePageState类当中。

那么，**StatefulWidget与StatelessWidget的接口设计，为什么会有这样的区别呢？**

这是因为Widget需要依据数据才能完成构建，而对于StatefulWidget来说，其依赖的数据在Widget生命周期中可能会频繁地发生变化。由State创建Widget，以数据驱动视图更新，而不是直接操作UI更新视觉属性，代码表达可以更精炼，逻辑也可以更清晰。

在了解了计数器示例程序的整体结构以后，我们再来看看这个**示例代码的第二部分**，也就是页面布局及交互逻辑部分。

```
class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  void _incrementCounter() => setState(() {_counter++;});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(Widget.title)),
      body: Text('You have pushed the button this many times:$_counter')),
      floatingActionButton: FloatingActionButton(onPressed: _incrementCounter)
    );
  }
```

_MyHomePageState中创建的Widget Scaffold，是Material库中提供的页面布局结构，它包含AppBar、Body，以及FloatingActionButton。

- AppBar是页面的导航栏，我们直接将MyHomePage中的title属性作为标题使用。
- body则是一个Text组件，显示了一个根据_counter属性可变的文本：‘You have pushed the button this many times:$_counter’。
- floatingActionButton，则是页面右下角的带“+”的悬浮按钮。我们将_incrementCounter作为其点击处理函数。

_incrementCounter的实现很简单，使用setState方法去自增状态属性_counter。setState方法是Flutter以数据驱动视图更新的关键函数，它会通知Flutter框架：我这儿有状态发生了改变，赶紧给我刷新界面吧。而Flutter框架收到通知后，会执行Widget的build方法，根据新的状态重新构建界面。

**这里需要注意的是：状态的更改一定要配合使用setState。**通过这个方法的调用，Flutter会在底层标记Widget的状态，随后触发重建。于我们的示例而言，即使你修改了_counter，如果不调用setState，Flutter框架也不会感知到状态的变化，因此界面上也不会有任何改变（你可以动手验证一下）。

下面的图3，就是整个计数器示例的代码流程示意图。通过这张图，你就能够把这个实例的整个代码流程串起来了：

![c59c908e02da4521bcad1aa47b650d2d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c59c908e02da4521bcad1aa47b650d2d.jpg)

图3 代码流程示意图

MyApp为Flutter应用的运行实例，通过在main函数中调用runApp函数实现程序的入口。而应用的首页则为MyHomePage，一个拥有_MyHomePageState状态的StatefulWidget。_MyHomePageState通过调用build方法，以相应的数据配置完成了包括导航栏、文本及按钮的页面视图的创建。

而当按钮被点击之后，其关联的控件函数_incrementCounter会触发调用。在这个函数中，通过调用setState方法，更新_counter属性的同时，也会通知Flutter框架其状态发生变化。随后，Flutter会重新调用build方法，以新的数据配置重新构建_MyHomePageState的UI，最终完成页面的重新渲染。

Widget只是视图的“配置信息”，是数据的映射，是“只读”的。对于StatefulWidget而言，当数据改变的时候，我们需要重新创建Widget去更新界面，这也就意味着Widget的创建销毁会非常频繁。

为此，Flutter对这个机制做了优化，其框架内部会通过一个中间层去收敛上层UI配置对底层真实渲染的改动，从而最大程度降低对真实渲染视图的修改，提高渲染效率，而不是上层UI配置变了就需要销毁整个渲染视图树重建。

这样一来，Widget仅是一个轻量级的数据配置存储结构，它的重新创建速度非常快，所以我们可以放心地重新构建任何需要更新的视图，而无需分别修改各个子Widget的特定样式。关于Widget具体的渲染过程细节，我会在后续的第9篇文章“Widget，构建Flutter界面的基石”中向你详细介绍，在这里就不再展开了。

#### 总结

今天的这次Flutter项目初体验，我们就先进行到这里。接下来，我们一起回顾下涉及到的知识点。

首先，我们通过Flutter标准模板创建了计数器示例，并分析了Flutter的项目结构，以及Flutter工程与原生Android、iOS工程的联系，知道了Flutter代码是怎么运行在原生系统上的。

然后，我带你学习了示例项目代码，了解了Flutter应用结构及页面结构，并认识了构建Flutter的基础，也就是Widget，以及状态管理机制，知道了Flutter页面是如何构建的，StatelessWidget与StatefulWidget的区别，以及如何通过State的成员函数setState以数据驱动的方式更新状态，从而更新页面。

有原生Android和iOS框架开发经验的同学，可能更习惯命令式的UI编程风格：手动创建UI组件，在需要更改UI时调用其方法修改视觉属性。而Flutter采用声明式UI设计，我们只需要描述当前的UI状态（即State）即可，不同UI状态的视觉变更由Flutter在底层完成。

虽然命令式的UI编程风格更直观，但声明式UI编程方式的好处是，可以让我们把复杂的视图操作细节交给框架去完成，这样一来不仅可以提高我们的效率，也可以让我们专注于整个应用和页面的结构和功能。

所以在这里，我非常希望你能够适应这样的UI编程思维方式的转换。

#### 思考题

最后，我给你留下一个思考题吧。

示例项目代码在_MyHomePageState类中，直接在build函数里以内联的方式完成了Scaffold页面元素的构建，这样做的好处是什么呢？

在实现同样功能的情况下，如果将Scaffold页面元素的构建封装成一个新Widget类，我们该如何处理？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 基础语法与类型变量：Dart是如何表示信息的？

你好，我是陈航。

在专栏的第2篇预习文章“[Dart语言概览](https://time.geekbang.org/column/article/104071)”中，我们简单地认识了Dart这门优秀的程序语言。那么，Dart与其他语言究竟有什么不同呢？在已有其他编程语言经验的基础上，我又如何快速上手呢？

今天，我们就从编程语言中最重要的组成部分，也就是基础语法与类型变量出发，一起来学习Dart吧。

#### Dart初体验

为了简单地体验一下Dart，我们打开浏览器，直接在[repl.it](https://repl.it/languages/dart) 新建一个main.dart文件就可以了（当然，你也可以在电脑安装Dart SDK，体验最新的语法）。

下面是一个基本的hello world示例，我声明了一个带int参数的函数，并通过字符串内嵌表达式的方式把这个参数打印出来：

```
printInteger(int a) {
  print('Hello world, this is $a.');
}

main() {
  var number = 2019;
  printInteger(number);
}
```

然后，在编辑器中点击“run”按钮，命令行就会输出：

```
Hello world, this is 2019.
```

和绝大多数编译型语言一样，Dart要求以main函数作为执行的入口。

在知道了如何简单地运行Dart代码后，我们再来看一下Dart的基本变量类型。

#### Dart的变量与类型

在Dart中，我们可以用var或者具体的类型来声明一个变量。当使用var定义变量时，表示类型是交由编译器推断决定的，当然你也可以用静态类型去定义变量，更清楚地跟编译器表达你的意图，这样编辑器和编译器就能使用这些静态类型，向你提供代码补全或编译警告的提示了。

在默认情况下，未初始化的变量的值都是null，因此我们不用担心无法判定一个传递过来的、未定义变量到底是undefined，还是烫烫烫而写一堆冗长的判断语句了。

Dart是类型安全的语言，并且所有类型都是对象类型，都继承自顶层类型Object，因此一切变量的值都是类的实例（即对象），甚至数字、布尔值、函数和null也都是继承自Object的对象。

Dart内置了一些基本类型，如 num、bool、String、List和Map，在不引入其他库的情况下可以使用它们去声明变量。下面，我将逐一和你介绍。

##### num、bool与String

作为编程语言中最常用的类型，num、bool、String这三种基本类型被我放到了一起来介绍。

**Dart的数值类型num，只有两种子类**：即64位int和符合IEEE 754标准的64位double。前者代表整数类型，而后者则是浮点数的抽象。在正常情况下，它们的精度与取值范围就足够满足我们的诉求了。

```
int x = 1;
int hex = 0xEEADBEEF;
double y = 1.1;
double exponents = 1.13e5;
int roundY = y.round();
```

除了常见的基本运算符，比如+、-、*、/，以及位运算符外，你还能使用继承自num的 abs()、round()等方法，来实现求绝对值、取整的功能。

实际上，你打开官方文档或查看源码，就会发现这些常见的运算符也是继承自num：

![57e35da2719244039549c554f54d1c64](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/57e35da2719244039549c554f54d1c64.jpg)

图1 num中的运算符

如果还有其他高级运算方法的需求num无法满足，你可以试用一下dart:math库。这个库提供了诸如三角函数、指数、对数、平方根等高级函数。

**为了表示布尔值，Dart使用了一种名为bool的类型**。在Dart里，只有两个对象具有bool类型：true和false，它们都是编译时常量。

Dart是类型安全的，因此我们不能使用**if(nonbooleanValue)** 或**assert(nonbooleanValue)**之类的在JavaScript可以正常工作的代码，而应该显式地检查值。

如下所示，检查变量是否为0，在Dart中需要显示地与0做比较：

```
// 检查是否为0.
var number = 0;
assert(number == 0);
// assert(number); 错误
```

**Dart的String由UTF-16的字符串组成。**和JavaScript一样，构造字符串字面量时既能使用单引号也能使用双引号，还能在字符串中嵌入变量或表达式：你可以使用 **${express}** 把一个表达式的值放进字符串。而如果是一个标识符，你可以省略{}。

下面这段代码就是内嵌表达式的例子。我们把单词’cat’转成大写放入到变量s1的声明中：

```
var s = 'cat';
var s1 = 'this is a uppercased string: ${s.toUpperCase()}';
```

为了获得内嵌对象的字符串，Dart会调用对象的**toString()**方法。而常见字符串的拼接，Dart则通过内置运算符“+”实现。比如，下面这条语句会如你所愿声明一个值为’Hello World!‘的字符串：

```
var s2 = 'Hello' + ' ' + 'World!' ;
```

对于多行字符串的构建，你可以通过三个单引号或三个双引号的方式声明，这与Python是一致的：

```
var s3 = """This is a
multi-line string.""";
```

##### List与Map

其他编程语言中常见的数组和字典类型，在Dart中的对应实现是List和Map，统称为集合类型。它们的声明和使用很简单，和JavaScript中的用法类似。

接下来，我们一起看一段代码示例。

- 在代码示例的前半部分，我们声明并初始化了两个List变量，在第二个变量中添加了一个新的元素后，调用其迭代方法依次打印出其内部元素；
- 在代码示例的后半部分，我们声明并初始化了两个Map变量，在第二个变量中添加了两个键值对后，同样调用其迭代方法依次打印出其内部元素。

```
var arr1 = ["Tom", "Andy", "Jack"];
var arr2 = List.of([1,2,3]);
arr2.add(499);
arr2.forEach((v) => print('${v}'));

var map1 = {"name": "Tom", 'sex': 'male'};
var map2 = new Map();
map2['name'] = 'Tom';
map2['sex'] = 'male';
map2.forEach((k,v) => print('${k}: ${v}'));
```

容器里的元素也需要有类型，比如上述代码中arr2的类型是**List**，map2的类型则为**Map**。Dart会自动根据上下文进行类型推断，所以你后续往容器内添加的元素也必须遵照这一类型。

如果编译器自动推断的类型不符合预期，我们当然可以在声明时显式地把类型标记出来，不仅可以让代码提示更友好一些，更重要的是可以让静态分析器帮忙检查字面量中的错误，解除类型不匹配带来的安全隐患或是Bug。

以上述代码为例，如果往arr2集合中添加一个浮点数**arr2.add(1.1)**，尽管语义上合法，但编译器会提示类型不匹配，从而导致编译失败。

和Java语言类似，在初始化集合实例对象时，你可以为它的类型添加约束，也可以用于后续判断集合类型。

下面的这段代码，在增加了类型约束后，语义是不是更清晰了？

```
var arr1 = <String>['Tom', 'Andy', 'Jack'];
var arr2 = new List<int>.of([1,2,3]);
arr2.add(499);
arr2.forEach((v) => print('${v}'));
print(arr2 is List<int>); // true

var map1 = <String, String>{'name': 'Tom','sex': 'male',};
var map2 = new Map<String, String>();
map2['name'] = 'Tom';
map2['sex'] = 'male';
map2.forEach((k,v) => print('${k}: ${v}'));
print(map2 is Map<String, String>); // true
```

##### 常量定义

如果你想定义不可变的变量，则需要在定义变量前加上final或const关键字：

- const，表示变量在编译期间即能确定的值；
- final则不太一样，用它定义的变量可以在运行时确定值，而一旦确定后就不可再变。

声明const常量与final常量的典型例子，如下所示：

```
final name = 'Andy';
const count = 3;

var x = 70;
var y = 30;
final z = x / y;
```

可以看到，const适用于定义编译常量（字面量固定值）的场景，而final适用于定义运行时常量的场景。

#### 总结

通过上面的介绍，相信你已经对Dart的基本语法和类型系统有了一个初步的印象。这些初步的印象，有助于你理解Dart语言设计的基本思路，在已有编程语言经验的基础上快速上手。

而对于流程控制语法：如**if-else、for**、**while**、**do-while**、**break/continue、switch-case、assert**，由于与其他编程语言类似，在这里我就不做一一介绍了，更多的Dart语言特性需要你在后续的使用过程中慢慢学习。在我们使用Dart的过程中，[官方文档](https://api.dartlang.org/stable/2.2.0/index.html)是我们最重要的学习参考资料。

恭喜你！你现在已经迈出了Dart语言学习的第一步。接下来，我们简单回顾一下今天的内容，以便加深记忆与理解：

- 在Dart中，所有类型都是对象类型，都继承自顶层类型Object，因此一切变量都是对象，数字、布尔值、函数和null也概莫能外；
- 未初始化变量的值都是null；
- 为变量指定类型，这样编辑器和编译器都能更好地理解你的意图。

#### 思考题

对于集合类型List和Map，如何让其内部元素支持多种类型（比如，int、double）呢？又如何在遍历集合时，判断究竟是何种类型呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 函数、类与运算符：Dart是如何处理信息的？

你好，我是陈航。

在上一篇文章中，我通过一个基本hello word的示例，带你体验了Dart的基础语法与类型变量，并与其他编程语言的特性进行对比，希望可以帮助你快速建立起对Dart的初步印象。

其实，编程语言虽然千差万别，但归根结底，它们的设计思想无非就是回答两个问题：

- 如何表示信息；
- 如何处理信息。

在上一篇文章中，我们已经解决了Dart如何表示信息的问题，今天这篇文章我就着重和你分享它是如何处理信息的。

作为一门真正面向对象的编程语言，Dart将处理信息的过程抽象为了对象，以结构化的方式将功能分解，而函数、类与运算符就是抽象中最重要的手段。

接下来，我就从函数、类与运算符的角度，来进一步和你讲述Dart面向对象设计的基本思路。

#### 函数

函数是一段用来独立地完成某个功能的代码。我在上一篇文章中和你提到，在Dart中，所有类型都是对象类型，函数也是对象，它的类型叫作Function。这意味着函数也可以被定义为变量，甚至可以被定义为参数传递给另一个函数。

在下面这段代码示例中，我定义了一个判断整数是否为0的isZero函数，并把它传递了给另一个printInfo函数，完成格式化打印出判断结果的功能。

```
bool isZero(int number) { //判断整数是否为0
  return number == 0;
}

void printInfo(int number,Function check) { //用check函数来判断整数是否为0
  print("$number is Zero: ${check(number)}");
}

Function f = isZero;
int x = 10;
int y = 0;
printInfo(x,f);  // 输出 10 is Zero: false
printInfo(y,f);  // 输出 0 is Zero: true
```

如果函数体只有一行表达式，就比如上面示例中的isZero和printInfo函数，我们还可以像JavaScript语言那样用箭头函数来简化这个函数：

```
bool isZero(int number) => number == 0;

void printInfo(int number,Function check) => print("$number is Zero: ${check(number)}");
```

有时，一个函数中可能需要传递多个参数。那么，如何让这类函数的参数声明变得更加优雅、可维护，同时降低调用者的使用成本呢？

C++与Java的做法是，提供函数的重载，即提供同名但参数不同的函数。但**Dart认为重载会导致混乱，因此从设计之初就不支持重载，而是提供了可选命名参数和可选参数**。

具体方式是，在声明函数时：

- 给参数增加{}，以paramName: value的方式指定调用参数，也就是可选命名参数；
- 给参数增加[]，则意味着这些参数是可以忽略的，也就是可选参数。

在使用这两种方式定义函数时，我们还可以在参数未传递时设置默认值。我以一个只有两个参数的简单函数为例，来和你说明这两种方式的具体用法：

```
//要达到可选命名参数的用法，那就在定义函数的时候给参数加上 {}
void enable1Flags({bool bold, bool hidden}) => print("$bold , $hidden");

//定义可选命名参数时增加默认值
void enable2Flags({bool bold = true, bool hidden = false}) => print("$bold ,$hidden");

//可忽略的参数在函数定义时用[]符号指定
void enable3Flags(bool bold, [bool hidden]) => print("$bold ,$hidden");

//定义可忽略参数时增加默认值
void enable4Flags(bool bold, [bool hidden = false]) => print("$bold ,$hidden");

//可选命名参数函数调用
enable1Flags(bold: true, hidden: false); //true, false
enable1Flags(bold: true); //true, null
enable2Flags(bold: false); //false, false

//可忽略参数函数调用
enable3Flags(true, false); //true, false
enable3Flags(true,); //true, null
enable4Flags(true); //true, false
enable4Flags(true,true); // true, true
```

**这里我要和你强调的是，在Flutter中会大量用到可选命名参数的方式，你一定要记住它的用法。**

#### 类

类是特定类型的数据和方法的集合，也是创建对象的模板。与其他语言一样，Dart为类概念提供了内置支持。

##### 类的定义及初始化

Dart是面向对象的语言，每个对象都是一个类的实例，都继承自顶层类型Object。在Dart中，实例变量与实例方法、类变量与类方法的声明与Java类似，我就不再过多展开了。

值得一提的是，Dart中并没有public、protected、private这些关键字，我们只要在声明变量与方法时，在前面加上“_”即可作为private方法使用。如果不加“_”，则默认为public。不过，**“_”的限制范围并不是类访问级别的，而是库访问级别**。

接下来，我们以一个具体的案例看看**Dart是如何定义和使用类的。**

我在Point类中，定义了两个成员变量x和y，通过构造函数语法糖进行初始化，成员函数printInfo的作用是打印它们的信息；而类变量factor，则在声明时就已经赋好了默认值0，类函数printZValue会打印出它的信息。

```
class Point {
  num x, y;
  static num factor = 0;
  //语法糖，等同于在函数体内：this.x = x;this.y = y;
  Point(this.x,this.y);
  void printInfo() => print('($x, $y)');
  static void printZValue() => print('$factor');
}

var p = new Point(100,200); // new 关键字可以省略
p.printInfo();  // 输出(100, 200);
Point.factor = 10;
Point.printZValue(); // 输出10
```

有时候类的实例化需要根据参数提供多种初始化方式。除了可选命名参数和可选参数之外，Dart还提供了**命名构造函数**的方式，使得类的实例化过程语义更清晰。

此外，**与C++类似，Dart支持初始化列表**。在构造函数的函数体真正执行之前，你还有机会给实例变量赋值，甚至重定向至另一个构造函数。

如下面实例所示，Point类中有两个构造函数Point.bottom与Point，其中：Point.bottom将其成员变量的初始化重定向到了Point中，而Point则在初始化列表中为z赋上了默认值0。

```
class Point {
  num x, y, z;
  Point(this.x, this.y) : z = 0; // 初始化变量z
  Point.bottom(num x) : this(x, 0); // 重定向构造函数
  void printInfo() => print('($x,$y,$z)');
}

var p = Point.bottom(100);
p.printInfo(); // 输出(100,0,0)
```

##### 复用

在面向对象的编程语言中，将其他类的变量与方法纳入本类中进行复用的方式一般有两种：**继承父类和接口实现**。当然，在Dart也不例外。

在Dart中，你可以对同一个父类进行继承或接口实现：

- 继承父类意味着，子类由父类派生，会自动获取父类的成员变量和方法实现，子类可以根据需要覆写构造函数及父类方法；
- 接口实现则意味着，子类获取到的仅仅是接口的成员变量符号和方法符号，需要重新实现成员变量，以及方法的声明和初始化，否则编译器会报错。

接下来，我以一个例子和你说明**在Dart中继承和接口的差别**。

Vector通过继承Point的方式增加了成员变量，并覆写了printInfo的实现；而Coordinate，则通过接口实现的方式，覆写了Point的变量定义及函数实现：

```
class Point {
  num x = 0, y = 0;
  void printInfo() => print('($x,$y)');
}

//Vector继承自Point
class Vector extends Point{
  num z = 0;
  @override
  void printInfo() => print('($x,$y,$z)'); //覆写了printInfo实现
}

//Coordinate是对Point的接口实现
class Coordinate implements Point {
  num x = 0, y = 0; //成员变量需要重新声明
  void printInfo() => print('($x,$y)'); //成员函数需要重新声明实现
}

var xxx = Vector();
xxx
  ..x = 1
  ..y = 2
  ..z = 3; //级联运算符，等同于xxx.x=1; xxx.y=2;xxx.z=3;
xxx.printInfo(); //输出(1,2,3)

var yyy = Coordinate();
yyy
  ..x = 1
  ..y = 2; //级联运算符，等同于yyy.x=1; yyy.y=2;
yyy.printInfo(); //输出(1,2)
print (yyy is Point); //true
print(yyy is Coordinate); //true
```

可以看出，子类Coordinate采用接口实现的方式，仅仅是获取到了父类Point的一个“空壳子”，只能从语义层面当成接口Point来用，但并不能复用Point的原有实现。那么，**我们是否能够找到方法去复用Point的对应方法实现呢？**

也许你很快就想到了，我可以让Coordinate继承Point，来复用其对应的方法。但，如果Coordinate还有其他的父类，我们又该如何处理呢？

其实，**除了继承和接口实现之外，Dart还提供了另一种机制来实现类的复用，即“混入”（Mixin）**。混入鼓励代码重用，可以被视为具有实现方法的接口。这样一来，不仅可以解决Dart缺少对多重继承的支持问题，还能够避免由于多重继承可能导致的歧义（菱形问题）。

> 备注：继承歧义，也叫菱形问题，是支持多继承的编程语言中一个相当棘手的问题。当B类和C类继承自A类，而D类继承自B类和C类时会产生歧义。如果A中有一个方法在B和C中已经覆写，而D没有覆写它，那么D继承的方法的版本是B类，还是C类的呢？

**要使用混入，只需要with关键字即可。**我们来试着改造Coordinate的实现，把类中的变量声明和函数实现全部删掉：

```
class Coordinate with Point {
}

var yyy = Coordinate();
print (yyy is Point); //true
print(yyy is Coordinate); //true
```

可以看到，通过混入，一个类里可以以非继承的方式使用其他类中的变量与方法，效果正如你想象的那样。

#### 运算符

Dart和绝大部分编程语言的运算符一样，所以你可以用熟悉的方式去执行程序代码运算。不过，**Dart多了几个额外的运算符，用于简化处理变量实例缺失（即null）的情况**。

- **?.**运算符：假设Point类有printInfo()方法，p是Point的一个可能为null的实例。那么，p调用成员方法的安全代码，可以简化为p?.printInfo() ，表示p为null的时候跳过，避免抛出异常。
- **??=** 运算符：如果a为null，则给a赋值value，否则跳过。这种用默认值兜底的赋值语句在Dart中我们可以用a ??= value表示。
- **??**运算符：如果a不为null，返回a的值，否则返回b。在Java或者C++中，我们需要通过三元表达式(a != null)? a : b来实现这种情况。而在Dart中，这类代码可以简化为a ?? b。

**在Dart中，一切都是对象，就连运算符也是对象成员函数的一部分。**

对于系统的运算符，一般情况下只支持基本数据类型和标准库中提供的类型。而对于用户自定义的类，如果想支持基本操作，比如比较大小、相加相减等，则需要用户自己来定义关于这个运算符的具体实现。

**Dart提供了类似C++的运算符覆写机制**，使得我们不仅可以覆写方法，还可以覆写或者自定义运算符。

接下来，我们一起看一个Vector类中自定义“+”运算符和覆写”==“运算符的例子：

```
class Vector {
  num x, y;
  Vector(this.x, this.y);
  // 自定义相加运算符，实现向量相加
  Vector operator +(Vector v) =>  Vector(x + v.x, y + v.y);
  // 覆写相等运算符，判断向量相等
  bool operator == (dynamic v) => x == v.x && y == v.y;
}

final x = Vector(3, 3);
final y = Vector(2, 2);
final z = Vector(1, 1);
print(x == (y + z)); //  输出true
```

operator是Dart的关键字，与运算符一起使用，表示一个类成员运算符函数。在理解时，我们应该把operator和运算符作为整体，看作是一个成员函数名。

#### 总结

函数、类与运算符是Dart处理信息的抽象手段。从今天的学习中你可以发现，Dart面向对象的设计吸纳了其他编程语言的优点，表达和处理信息的方式既简单又简洁，但又不失强大。

通过这两篇文章的内容，相信你已经了解了Dart的基本设计思路，熟悉了在Flutter开发中常用的语法特性，也已经具备了快速上手实践的能力。

接下来，我们简单回顾一下今天的内容，以便加深记忆与理解。

首先，我们认识了函数。函数也是对象，可以被定义为变量，或者参数。Dart不支持函数重载，但提供了可选命名参数和可选参数的方式，从而解决了函数声明时需要传递多个参数的可维护性。

然后，我带你学习了类。类提供了数据和函数的抽象复用能力，可以通过继承（父类继承，接口实现）和非继承（Mixin）方式实现复用。在类的内部，关于成员变量，Dart提供了包括命名构造函数和初始化列表在内的两种初始化方式。

最后，需要注意的是，运算符也是对象成员函数的一部分，可以覆写或者自定义。

#### 思考题

最后，请你思考以下两个问题。

1. 你是怎样理解父类继承，接口实现和混入的？我们应该在什么场景下使用它们？
2. 在父类继承的场景中，父类子类之间的构造函数执行顺序是怎样的？如果父类有多个构造函数，子类也有多个构造函数，如何从代码层面确保父类子类之间构造函数的正确调用？

```
class Point {
  num x, y;
  Point() : this.make(0,0);
  Point.left(x) : this.make(x,0);
  Point.right(y) : this.make(0,y);
  Point.make(this.x, this.y);
  void printInfo() => print('($x,$y)');
}

class Vector extends Point{
  num z = 0;
/*5个构造函数
  Vector
  Vector.left;
  Vector.middle
  Vector.right
  Vector.make
*/
  @override
  void printInfo() => print('($x,$y,$z)'); //覆写了printInfo实现
}
```

欢迎将你的答案留言告诉我，我们一起讨论。感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 综合案例：掌握Dart核心特性

你好，我是陈航。

在前两篇文章中，我首先与你一起学习了Dart程序的基本结构和语法，认识了Dart语言世界的基本构成要素，也就是类型系统，以及它们是怎么表示信息的。然后，我带你学习了Dart面向对象设计的基本思路，知道了函数、类与运算符这些其他编程语言中常见的概念，在Dart中的差异及典型用法，理解了Dart是怎么处理信息的。

可以看到，Dart吸纳了其他编程语言的优点，在关于如何表达以及处理信息上，既简单又简洁，而且又不失强大。俗话说，纸上得来终觉浅，绝知此事要躬行。那么今天，我就用一个综合案例，把前面学习的关于Dart的零散知识串起来，希望你可以动手试验一下这个案例，借此掌握如何用Dart编程。

有了前面学习的知识点，再加上今天的综合案例练习，我认为你已经掌握了Dart最常用的80%的特性，可以在基本没有语言障碍的情况下去使用Flutter了。至于剩下的那20%的特性，因为使用较少，所以我不会在本专栏做重点讲解。如果你对这部分内容感兴趣的话，可以访问[官方文档](https://dart.dev/tutorials)去做进一步了解。

此外，关于Dart中的异步和并发，我会在后面的第23篇文章“单线程模型怎么保证UI运行流畅？”中进行深入介绍。

#### 案例介绍

今天，我选择的案例是，先用Dart写一段购物车程序，但先不使用Dart独有的特性。然后，我们再以这段程序为起点，逐步加入Dart语言特性，将其改造为一个符合Dart设计思想的程序。你可以在这个改造过程中，进一步体会到Dart的魅力所在。

首先，我们来看看在不使用任何Dart语法特性的情况下，一个有着基本功能的购物车程序长什么样子。

```
//定义商品Item类
class Item {
  double price;
  String name;
  Item(name, price) {
    this.name = name;
    this.price = price;
  }
}

//定义购物车类
class ShoppingCart {
  String name;
  DateTime date;
  String code;
  List<Item> bookings;

  price() {
    double sum = 0.0;
    for(var i in bookings) {
      sum += i.price;
    }
    return sum;
  }

  ShoppingCart(name, code) {
    this.name = name;
    this.code = code;
    this.date = DateTime.now();
  }

  getInfo() {
    return '购物车信息:' +
          '\n-----------------------------' +
          '\n用户名: ' + name+
          '\n优惠码: ' + code +
          '\n总价: ' + price().toString() +
          '\n日期: ' + date.toString() +
          '\n-----------------------------';
  }
}

void main() {
  ShoppingCart sc = ShoppingCart('张三', '123456');
  sc.bookings = [Item('苹果',10.0), Item('鸭梨',20.0)];
  print(sc.getInfo());
}
```

在这段程序中，我定义了商品Item类，以及购物车ShoppingCart类。它们分别包含了一个初始化构造方法，将main函数传入的参数信息赋值给对象内部属性。而购物车的基本信息，则通过ShoppingCart类中的getInfo方法输出。在这个方法中，我采用字符串拼接的方式，将各类信息进行格式化组合后，返回给调用者。

运行这段程序，不出意外，购物车对象sc包括的用户名、优惠码、总价与日期在内的基本信息都会被打印到命令行中。

```
购物车信息:
-----------------------------
用户名: 张三
优惠码: 123456
总价: 30.0
日期: 2019-06-01 17:17:57.004645
-----------------------------
```

这段程序的功能非常简单：我们初始化了一个购物车对象，然后给购物车对象进行加购操作，最后打印出基本信息。可以看到，在不使用Dart语法任何特性的情况下，这段代码与Java、C++甚至JavaScript没有明显的语法差异。

在关于如何表达以及处理信息上，Dart保持了既简单又简洁的风格。那接下来，**我们就先从表达信息入手，看看Dart是如何优化这段代码的。**

#### 类抽象改造

我们先来看看Item类与ShoppingCart类的初始化部分。它们在构造函数中的初始化工作，仅仅是将main函数传入的参数进行属性赋值。

在其他编程语言中，在构造函数的函数体内，将初始化参数赋值给实例变量的方式非常常见。而在Dart里，我们可以利用语法糖以及初始化列表，来简化这样的赋值过程，从而直接省去构造函数的函数体：

```
class Item {
  double price;
  String name;
  Item(this.name, this.price);
}

class ShoppingCart {
  String name;
  DateTime date;
  String code;
  List<Item> bookings;
  price() {...}
  //删掉了构造函数函数体
  ShoppingCart(this.name, this.code) : date = DateTime.now();
...
}
```

这一下就省去了7行代码！通过这次改造，我们有两个新的发现：

- 首先，Item类与ShoppingCart类中都有一个name属性，在Item中表示商品名称，在ShoppingCart中则表示用户名；
- 然后，Item类中有一个price属性，ShoppingCart中有一个price方法，它们都表示当前的价格。

考虑到name属性与price属性（方法）的名称与类型完全一致，在信息表达上的作用也几乎一致，因此我可以在这两个类的基础上，再抽象出一个新的基类Meta，用于存放price属性与name属性。

同时，考虑到在ShoppingCart类中，price属性仅用做计算购物车中商品的价格（而不是像Item类那样用于数据存取），因此在继承了Meta类后，我改写了ShoppingCart类中price属性的get方法：

```
class Meta {
  double price;
  String name;
  Meta(this.name, this.price);
}
class Item extends Meta{
  Item(name, price) : super(name, price);
}

class ShoppingCart extends Meta{
  DateTime date;
  String code;
  List<Item> bookings;

  double get price {...}
  ShoppingCart(name, this.code) : date = DateTime.now(),super(name,0);
  getInfo() {...}
}
```

通过这次类抽象改造，程序中各个类的依赖关系变得更加清晰了。不过，目前这段程序中还有两个冗长的方法显得格格不入，即ShoppingCart类中计算价格的price属性get方法，以及提供购物车基本信息的getInfo方法。接下来，我们分别来改造这两个方法。

#### 方法改造

我们先看看price属性的get方法：

```
double get price {
  double sum = 0.0;
  for(var i in bookings) {
    sum += i.price;
  }
  return sum;
}
```

在这个方法里，我采用了其他语言常见的求和算法，依次遍历bookings列表中的Item对象，累积相加求和。

而在Dart中，这样的求和运算我们只需重载Item类的“+”运算符，并通过对列表对象进行归纳合并操作即可实现（你可以想象成，把购物车中的所有商品都合并成了一个商品套餐对象）。

另外，由于函数体只有一行，所以我们可以使用Dart的箭头函数来进一步简化实现函数：

```
class Item extends Meta{
  ...
  //重载了+运算符，合并商品为套餐商品
  Item operator+(Item item) => Item(name + item.name, price + item.price);
}

class ShoppingCart extends Meta{
  ...
  //把迭代求和改写为归纳合并
  double get price => bookings.reduce((value, element) => value + element).price;
  ...
  getInfo() {...}
}
```

可以看到，这段代码又简洁了很多！接下来，我们再看看getInfo方法如何优化。

在getInfo方法中，我们将ShoppingCart类的基本信息通过字符串拼接的方式，进行格式化组合，这在其他编程语言中非常常见。而在Dart中，我们可以通过对字符串插入变量或表达式，并使用多行字符串声明的方式，来完全抛弃不优雅的字符串拼接，实现字符串格式化组合。

```
getInfo () => '''
购物车信息:
-----------------------------
  用户名: $name
  优惠码: $code
  总价: $price
  Date: $date
-----------------------------
''';
```

在去掉了多余的字符串转义和拼接代码后，getInfo方法看着就清晰多了。

在优化完了ShoppingCart类与Item类的内部实现后，我们再来看看main函数，从调用方的角度去分析程序还能在哪些方面做优化。

#### 对象初始化方式的优化

在main函数中，我们使用

```
ShoppingCart sc = ShoppingCart('张三', '123456') ;
```

初始化了一个使用‘123456’优惠码、名为‘张三’的用户所使用的购物车对象。而这段初始化方法的调用，我们可以从两个方面优化：

- 首先，在对ShoppingCart的构造函数进行了大量简写后，我们希望能够提供给调用者更明确的初始化方法调用方式，让调用者以“参数名:参数键值对”的方式指定调用参数，让调用者明确传递的初始化参数的意义。在Dart中，这样的需求，我们在声明函数时，可以通过给参数增加{}实现。
- 其次，对一个购物车对象来说，一定会有一个有用户名，但不一定有优惠码的用户。因此，对于购物车对象的初始化，我们还需要提供一个不含优惠码的初始化方法，并且需要确定多个初始化方法与父类的初始化方法之间的正确调用顺序。

按照这样的思路，我们开始对ShoppingCart进行改造。

需要注意的是，由于优惠码可以为空，我们还需要对getInfo方法进行兼容处理。在这里，我用到了a??b运算符，这个运算符能够大量简化在其他语言中三元表达式(a != null)? a : b的写法：

```
class ShoppingCart extends Meta{
  ...
  //默认初始化方法，转发到withCode里
  ShoppingCart({name}) : this.withCode(name:name, code:null);
  //withCode初始化方法，使用语法糖和初始化列表进行赋值，并调用父类初始化方法
  ShoppingCart.withCode({name, this.code}) : date = DateTime.now(), super(name,0);

  //??运算符表示为code不为null，则用原值，否则使用默认值"没有"
  getInfo () => '''
购物车信息:
-----------------------------
  用户名: $name
  优惠码: ${code??"没有"}
  总价: $price
  Date: $date
-----------------------------
''';
}

void main() {
  ShoppingCart sc = ShoppingCart.withCode(name:'张三', code:'123456');
  sc.bookings = [Item('苹果',10.0), Item('鸭梨',20.0)];
  print(sc.getInfo());

  ShoppingCart sc2 = ShoppingCart(name:'李四');
  sc2.bookings = [Item('香蕉',15.0), Item('西瓜',40.0)];
  print(sc2.getInfo());
}
```

运行这段程序，张三和李四的购物车信息都会被打印到命令行中：

```
购物车信息:
-----------------------------
  用户名: 张三
  优惠码: 123456
  总价: 30.0
  Date: 2019-06-01 19:59:30.443817
-----------------------------

购物车信息:
-----------------------------
  用户名: 李四
  优惠码: 没有
  总价: 55.0
  Date: 2019-06-01 19:59:30.451747
-----------------------------
```

关于购物车信息的打印，我们是通过在main函数中获取到购物车对象的信息后，使用全局的print函数打印的，我们希望把打印信息的行为封装到ShoppingCart类中。而对于打印信息的行为而言，这是一个非常通用的功能，不止ShoppingCart类需要，Item对象也可能需要。

因此，我们需要把打印信息的能力单独封装成一个单独的类PrintHelper。但，ShoppingCart类本身已经继承自Meta类，考虑到Dart并不支持多继承，我们怎样才能实现PrintHelper类的复用呢？

这就用到了我在上一篇文章中提到的“混入”（Mixin），相信你还记得只要在使用时加上with关键字即可。

我们来试着增加PrintHelper类，并调整ShoppingCart的声明：

```
abstract class PrintHelper {
  printInfo() => print(getInfo());
  getInfo();
}

class ShoppingCart extends Meta with PrintHelper{
...
}
```

经过Mixin的改造，我们终于把所有购物车的行为都封装到ShoppingCart内部了。而对于调用方而言，还可以使用级联运算符“..”，在同一个对象上连续调用多个函数以及访问成员变量。使用级联操作符可以避免创建临时变量，让代码看起来更流畅：

```
void main() {
  ShoppingCart.withCode(name:'张三', code:'123456')
  ..bookings = [Item('苹果',10.0), Item('鸭梨',20.0)]
  ..printInfo();

  ShoppingCart(name:'李四')
  ..bookings = [Item('香蕉',15.0), Item('西瓜',40.0)]
  ..printInfo();
}
```

很好！通过Dart独有的语法特性，我们终于把这段购物车代码改造成了简洁、直接而又强大的Dart风格程序。

#### 总结

这就是今天分享的全部内容了。在今天，我们以一个与Java、C++甚至JavaScript没有明显语法差异的购物车雏形为起步，逐步将它改造成了一个符合Dart设计思想的程序。

首先，我们使用构造函数语法糖及初始化列表，简化了成员变量的赋值过程。然后，我们重载了“+”运算符，并采用归纳合并的方式实现了价格计算，并且使用多行字符串和内嵌表达式的方式，省去了无谓的字符串拼接。最后，我们重新梳理了类之间的继承关系，通过mixin、多构造函数，可选命名参数等手段，优化了对象初始化调用方式。

下面是今天购物车综合案例的完整代码，希望你在IDE中多多练习，体会这次的改造过程，从而对Dart那些使代码变得更简洁、直接而强大的关键语法特性产生更深刻的印象。同时，改造前后的代码，你也可以在GitHub的[Dart_Sample](https://github.com/cyndibaby905/08_Dart_Sample)中找到：

```
class Meta {
  double price;
  String name;
  //成员变量初始化语法糖
  Meta(this.name, this.price);
}

class Item extends Meta{
  Item(name, price) : super(name, price);
  //重载+运算符，将商品对象合并为套餐商品
  Item operator+(Item item) => Item(name + item.name, price + item.price);
}

abstract class PrintHelper {
  printInfo() => print(getInfo());
  getInfo();
}

//with表示以非继承的方式复用了另一个类的成员变量及函数
class ShoppingCart extends Meta with PrintHelper{
  DateTime date;
  String code;
  List<Item> bookings;
  //以归纳合并方式求和
  double get price => bookings.reduce((value, element) => value + element).price;
  //默认初始化函数，转发至withCode函数
  ShoppingCart({name}) : this.withCode(name:name, code:null);
  //withCode初始化方法，使用语法糖和初始化列表进行赋值，并调用父类初始化方法
  ShoppingCart.withCode({name, this.code}) : date = DateTime.now(), super(name,0);

  //??运算符表示为code不为null，则用原值，否则使用默认值"没有"
  @override
  getInfo() => '''
购物车信息:
-----------------------------
  用户名: $name
  优惠码: ${code??"没有"}
  总价: $price
  Date: $date
-----------------------------
''';
}

void main() {
  ShoppingCart.withCode(name:'张三', code:'123456')
  ..bookings = [Item('苹果',10.0), Item('鸭梨',20.0)]
  ..printInfo();

  ShoppingCart(name:'李四')
  ..bookings = [Item('香蕉',15.0), Item('西瓜',40.0)]
  ..printInfo();
}
```

#### 思考题

请你扩展购物车程序的实现，使得我们的购物车可以支持：

1. 商品数量属性；
2. 购物车信息增加商品列表信息（包括商品名称，数量及单价）输出，实现小票的基本功能。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

## Widget 与界面构建

### Widget，构建Flutter界面的基石

你好，我是陈航。

在前面的Flutter开发起步和Dart基础模块中，我和你一起学习了Flutter框架的整体架构与基本原理，分析了Flutter的项目结构和运行机制，并从Flutter开发角度介绍了Dart语言的基本设计思路，也通过和其他高级语言的类比深入认识了Dart的语法特性。

这些内容，是我们接下来系统学习构建Flutter应用的基础，可以帮助我们更好地掌握Flutter的核心概念和技术。

在第4篇文章“[Flutter区别于其他方案的关键技术是什么？](https://time.geekbang.org/column/article/105703)”中，我和你分享了一张来自Flutter官方的架构图，不难看出Widget是整个视图描述的基础。这张架构图很重要，所以我在这里又放了一次。

![16a65ce49c7546e086fa2b20d053b528](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/16a65ce49c7546e086fa2b20d053b528.jpg)

图1 Flutter架构图

备注：此图引自[Flutter System Overview](https://flutter.dev/docs/resources/technical-overview)

那么，Widget到底是什么呢？

Widget是Flutter功能的抽象描述，是视图的配置信息，同样也是数据的映射，是Flutter开发框架中最基本的概念。前端框架中常见的名词，比如视图（View）、视图控制器（View Controller）、活动（Activity）、应用（Application）、布局（Layout）等，在Flutter中都是Widget。

事实上，**Flutter的核心设计思想便是“一切皆Widget”**。所以，我们学习Flutter，首先得从学会使用Widget开始。

那么，在今天的这篇文章中，我会带着你一起学习Widget在Flutter中的设计思路和基本原理，以帮助你深入理解Flutter的视图构建过程。

#### Widget渲染过程

在进行App开发时，我们往往会关注的一个问题是：如何结构化地组织视图数据，提供给渲染引擎，最终完成界面显示。

通常情况下，不同的UI框架中会以不同的方式去处理这一问题，但无一例外地都会用到视图树（View Tree）的概念。而Flutter将视图树的概念进行了扩展，把视图数据的组织和渲染抽象为三部分，即Widget，Element和 RenderObject。

这三部分之间的关系，如下所示：

![6d195bd6ada3491bbecf4214e3ae3aaa](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/6d195bd6ada3491bbecf4214e3ae3aaa.jpg)

图2 Widget，Element与RenderObject

##### Widget

Widget是Flutter世界里对视图的一种结构化描述，你可以把它看作是前端中的“控件”或“组件”。Widget是控件实现的基本逻辑单位，里面存储的是有关视图渲染的配置信息，包括布局、渲染属性、事件响应信息等。

在页面渲染上，**Flutter将“Simple is best”这一理念做到了极致**。为什么这么说呢？Flutter将Widget设计成不可变的，所以当视图渲染的配置信息发生变化时，Flutter会选择重建Widget树的方式进行数据更新，以数据驱动UI构建的方式简单高效。

但，这样做的缺点是，因为涉及到大量对象的销毁和重建，所以会对垃圾回收造成压力。不过，Widget本身并不涉及实际渲染位图，所以它只是一份轻量级的数据结构，重建的成本很低。

另外，由于Widget的不可变性，可以以较低成本进行渲染节点复用，因此在一个真实的渲染树中可能存在不同的Widget对应同一个渲染节点的情况，这无疑又降低了重建UI的成本。

##### Element

Element是Widget的一个实例化对象，它承载了视图构建的上下文数据，是连接结构化的配置信息到完成最终渲染的桥梁。

Flutter渲染过程，可以分为这么三步：

- 首先，通过Widget树生成对应的Element树；
- 然后，创建相应的RenderObject并关联到Element.renderObject属性上；
- 最后，构建成RenderObject树，以完成最终的渲染。

可以看到，Element同时持有Widget和RenderObject。而无论是Widget还是Element，其实都不负责最后的渲染，只负责发号施令，真正去干活儿的只有RenderObject。那你可能会问，**既然都是发号施令，那为什么需要增加中间的这层Element树呢？直接由Widget命令RenderObject去干活儿不好吗？**

答案是，可以，但这样做会极大地增加渲染带来的性能损耗。

因为Widget具有不可变性，但Element却是可变的。实际上，Element树这一层将Widget树的变化（类似React 虚拟DOM diff）做了抽象，可以只将真正需要修改的部分同步到真实的RenderObject树中，最大程度降低对真实渲染视图的修改，提高渲染效率，而不是销毁整个渲染视图树重建。

这，就是Element树存在的意义。

##### RenderObject

从其名字，我们就可以很直观地知道，RenderObject是主要负责实现视图渲染的对象。

在前面的第4篇文章“[Flutter区别于其他方案的关键技术是什么？](https://time.geekbang.org/column/article/105703)”中，我们提到，Flutter通过控件树（Widget树）中的每个控件（Widget）创建不同类型的渲染对象，组成渲染对象树。

而渲染对象树在Flutter的展示过程分为四个阶段，即布局、绘制、合成和渲染。 其中，布局和绘制在RenderObject中完成，Flutter采用深度优先机制遍历渲染对象树，确定树中各个对象的位置和尺寸，并把它们绘制到不同的图层上。绘制完毕后，合成和渲染的工作则交给Skia搞定。

Flutter通过引入Widget、Element与RenderObject这三个概念，把原本从视图数据到视图渲染的复杂构建过程拆分得更简单、直接，在易于集中治理的同时，保证了较高的渲染效率。

#### RenderObjectWidget介绍

通过第5篇文章“[从标准模板入手，体会Flutter代码是如何运行在原生系统上的](https://time.geekbang.org/column/article/106199)”的介绍，你应该已经知道如何使用StatelessWidget和StatefulWidget了。

不过，StatelessWidget和StatefulWidget只是用来组装控件的容器，并不负责组件最后的布局和绘制。在Flutter中，布局和绘制工作实际上是在Widget的另一个子类RenderObjectWidget内完成的。

所以，在今天这篇文章的最后，我们再来看一下RenderObjectWidget的源码，来看看如何使用Element和RenderObject完成图形渲染工作。

```
abstract class RenderObjectWidget extends Widget {
  @override
  RenderObjectElement createElement();
  @protected
  RenderObject createRenderObject(BuildContext context);
  @protected
  void updateRenderObject(BuildContext context, covariant RenderObject renderObject) { }
  ...
}
```

RenderObjectWidget是一个抽象类。我们通过源码可以看到，这个类中同时拥有创建Element、RenderObject，以及更新RenderObject的方法。

但实际上，**RenderObjectWidget本身并不负责这些对象的创建与更新**。

对于Element的创建，Flutter会在遍历Widget树时，调用createElement去同步Widget自身配置，从而生成对应节点的Element对象。而对于RenderObject的创建与更新，其实是在RenderObjectElement类中完成的。

```
abstract class RenderObjectElement extends Element {
  RenderObject _renderObject;

  @override
  void mount(Element parent, dynamic newSlot) {
    super.mount(parent, newSlot);
    _renderObject = widget.createRenderObject(this);
    attachRenderObject(newSlot);
    _dirty = false;
  }

  @override
  void update(covariant RenderObjectWidget newWidget) {
    super.update(newWidget);
    widget.updateRenderObject(this, renderObject);
    _dirty = false;
  }
  ...
}
```

在Element创建完毕后，Flutter会调用Element的mount方法。在这个方法里，会完成与之关联的RenderObject对象的创建，以及与渲染树的插入工作，插入到渲染树后的Element就可以显示到屏幕中了。

如果Widget的配置数据发生了改变，那么持有该Widget的Element节点也会被标记为dirty。在下一个周期的绘制时，Flutter就会触发Element树的更新，并使用最新的Widget数据更新自身以及关联的RenderObject对象，接下来便会进入Layout和Paint的流程。而真正的绘制和布局过程，则完全交由RenderObject完成：

```
abstract class RenderObject extends AbstractNode with DiagnosticableTreeMixin implements HitTestTarget {
  ...
  void layout(Constraints constraints, { bool parentUsesSize = false }) {...}

  void paint(PaintingContext context, Offset offset) { }
}
```

布局和绘制完成后，接下来的事情就交给Skia了。在VSync信号同步时直接从渲染树合成Bitmap，然后提交给GPU。这部分内容，我已经在之前的“[Flutter区别于其他方案的关键技术是什么](https://time.geekbang.org/column/article/105703)？”中与你介绍过了，这里就不再赘述了。

接下来，我以下面的界面示例为例，与你说明Widget、Element与RenderObject在渲染过程中的关系。在下面的例子中，一个Row容器放置了4个子Widget，左边是Image，而右边则是一个Column容器下排布的两个Text。

![816294d4e780462ab58e0357c0a13b1f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/816294d4e780462ab58e0357c0a13b1f.jpg)

图3 界面示例

那么，在Flutter遍历完Widget树，创建了各个子Widget对应的Element的同时，也创建了与之关联的、负责实际布局和绘制的RenderObject。

![a237ab3403934d46a5b39cfac316bbfd](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a237ab3403934d46a5b39cfac316bbfd.jpg)

图4 示例界面生成的“三棵树”

#### 总结

好了，今天关于Widget的设计思路和基本原理的介绍，我们就先进行到这里。接下来，我们一起回顾下今天的主要内容吧。

首先，我与你介绍了Widget渲染过程，学习了在Flutter中视图数据的组织和渲染抽象的三个核心概念，即Widget、 Element和RenderObject。

其中，Widget是Flutter世界里对视图的一种结构化描述，里面存储的是有关视图渲染的配置信息；Element则是Widget的一个实例化对象，将Widget树的变化做了抽象，能够做到只将真正需要修改的部分同步到真实的Render Object树中，最大程度地优化了从结构化的配置信息到完成最终渲染的过程；而RenderObject，则负责实现视图的最终呈现，通过布局、绘制完成界面的展示。

最后，在对Flutter Widget渲染过程有了一定认识后，我带你阅读了RenderObjectWidget的代码，理解Widget、Element与RenderObject这三个对象之间是如何互相配合，实现图形渲染工作的。

熟悉了Widget、Element与RenderObject这三个概念，相信你已经对组件的渲染过程有了一个清晰而完整的认识。这样，我们后续再学习常用的组件和布局时，就能够从不同的视角去思考框架设计的合理性了。

不过在日常开发学习中，绝大多数情况下，我们只需要了解各种Widget特性及使用方法，而无需关心Element及RenderObject。因为Flutter已经帮我们做了大量优化工作，因此我们只需要在上层代码完成各类Widget的组装配置，其他的事情完全交给Flutter就可以了。

#### 思考题

你是如何理解Widget、Element和RenderObject这三个概念的？它们之间是一一对应的吗？你能否在Android/iOS/Web中找到对应的概念呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### Widget中的State到底是什么？

你好，我是陈航。

通过上一篇文章，我们已经深入理解了Widget是Flutter构建界面的基石，也认识了Widget、Element、RenderObject是如何互相配合，实现图形渲染工作的。Flutter在底层做了大量的渲染优化工作，使得我们只需要通过组合、嵌套不同类型的Widget，就可以构建出任意功能、任意复杂度的界面。

同时，我们通过前面的学习，也已经了解到Widget有StatelessWidget和StatefulWidget两种类型。StatefulWidget应对有交互、需要动态变化视觉效果的场景，而StatelessWidget则用于处理静态的、无状态的视图展示。StatefulWidget的场景已经完全覆盖了StatelessWidget，因此我们在构建界面时，往往会大量使用StatefulWidget来处理静态的视图展示需求，看起来似乎也没什么问题。

那么，StatelessWidget存在的必要性在哪里？StatefulWidget是否是Flutter中的万金油？在今天这篇文章中，我将着重和你介绍这两种类型的区别，从而帮你更好地理解Widget，掌握不同类型Widget的正确使用时机。

#### UI编程范式

要想理解StatelessWidget与StatefulWidget的使用场景，我们首先需要了解，在Flutter中，如何调整一个控件（Widget）的展示样式，即UI编程范式。

如果你有过原生系统（Android、iOS）或原生JavaScript开发经验的话，应该知道视图开发是命令式的，需要精确地告诉操作系统或浏览器用何种方式去做事情。比如，如果我们想要变更界面的某个文案，则需要找到具体的文本控件并调用它的控件方法命令，才能完成文字变更。

下述代码分别展示了在Android、iOS及原生Javascript中，如何将一个文本控件的展示文案更改为Hello World：

```
// Android设置某文本控件展示文案为Hello World
TextView textView = (TextView) findViewById(R.id.txt);
textView.setText("Hello World");

// iOS设置某文本控件展示文案为Hello World
UILabel *label = (UILabel *)[self.view viewWithTag:1234];
label.text = @"Hello World";

// 原生JavaScript设置某文本控件展示文案为Hello World
document.querySelector("#demo").innerHTML = "Hello World!";
```

与此不同的是，**Flutter的视图开发是声明式的，其核心设计思想就是将视图和数据分离，这与React的设计思路完全一致**。

对我们来说，如果要实现同样的需求，则要稍微麻烦点：除了设计好Widget布局方案之外，还需要提前维护一套文案数据集，并为需要变化的Widget绑定数据集中的数据，使Widget根据这个数据集完成渲染。

但是，当需要变更界面的文案时，我们只要改变数据集中的文案数据，并通知Flutter框架触发Widget的重新渲染即可。这样一来，开发者将无需再精确关注UI编程中的各个过程细节，只要维护好数据集即可。比起命令式的视图开发方式需要挨个设置不同组件（Widget）的视觉属性，这种方式要便捷得多。

**总结来说，命令式编程强调精确控制过程细节；而声明式编程强调通过意图输出结果整体。**对应到Flutter中，意图是绑定了组件状态的State，结果则是重新渲染后的组件。在Widget的生命周期内，应用到State中的任何更改都将强制Widget重新构建。

其中，对于组件完成创建后就无需变更的场景，状态的绑定是可选项。这里“可选”就区分出了Widget的两种类型，即：StatelessWidget不带绑定状态，而StatefulWidget带绑定状态。**当你所要构建的用户界面不随任何状态信息的变化而变化时，需要选择使用StatelessWidget，反之则选用StatefulWidget。**前者一般用于静态内容的展示，而后者则用于存在交互反馈的内容呈现中。

接下来，我分别和你介绍StatelessWidget和StatefulWidget，从源码分析它们的区别，并总结一些关于Widget选型的基本原则。

#### StatelessWidget

在Flutter中，Widget采用由父到子、自顶向下的方式进行构建，父Widget控制着子Widget的显示样式，其样式配置由父Widget在构建时提供。

用这种方式构建出的Widget，有些（比如Text、Container、Row、Column等）在创建时，除了这些配置参数之外不依赖于任何其他信息，换句话说，它们一旦创建成功就不再关心、也不响应任何数据变化进行重绘。在Flutter中，**这样的Widget被称为StatelessWidget（无状态组件）**。

这里有一张StatelessWidget的示意图，如下所示：

![e06d906714cf4c3aa2d7b955fbb98f9c](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e06d906714cf4c3aa2d7b955fbb98f9c.jpg)

图1 StatelessWidget 示意图

接下来，我以Text的部分源码为例，和你说明StatelessWidget的构建过程。

```
class Text extends StatelessWidget {
  //构造方法及属性声明部分
  const Text(this.data, {
    Key key,
    this.textAlign,
    this.textDirection,
    //其他参数
    ...
  }) : assert(data != null),
     textSpan = null,
     super(key: key);

  final String data;
  final TextAlign textAlign;
  final TextDirection textDirection;
  //其他属性
  ...

  @override
  Widget build(BuildContext context) {
    ...
    Widget result = RichText(
       //初始化配置
       ...
      )
    );
    ...
    return result;
  }
}
```

可以看到，在构造方法将其属性列表赋值后，build方法随即将子组件RichText通过其属性列表（如文本data、对齐方式textAlign、文本展示方向textDirection等）初始化后返回，之后Text内部不再响应外部数据的变化。

那么，什么场景下应该使用StatelessWidget呢？

这里，我有一个简单的判断规则：**父Widget是否能通过初始化参数完全控制其UI展示效果？**如果能，那么我们就可以使用StatelessWidget来设计构造函数接口了。

我准备了两个简单的小例子，来帮助你理解这个判断规则。

第一个小例子是，我需要创建一个自定义的弹窗控件，把使用App过程中出现的一些错误信息提示给用户。这个组件的父Widget，能够完全在子Widget初始化时将组件所需要的样式信息和错误提示信息传递给它，也就意味着父Widget通过初始化参数就能完全控制其展示效果。所以，我可以采用继承StatelessWidget的方式，来进行组件自定义。

第二个小例子是，我需要定义一个计数器按钮，用户每次点击按钮后，按钮颜色都会随之加深。可以看到，这个组件的父Widget只能控制子Widget初始的样式展示效果，而无法控制在交互过程中发生的颜色变化。所以，我无法通过继承StatelessWidget的方式来自定义组件。那么，这个时候就轮到StatefulWidget出场了。

#### StatefulWidget

与StatelessWidget相对应的，有一些Widget（比如Image、Checkbox）的展示，除了父Widget初始化时传入的静态配置之外，还需要处理用户的交互（比如，用户点击按钮）或其内部数据的变化（比如，网络数据回包），并体现在UI上。

换句话说，这些Widget创建完成后，还需要关心和响应数据变化来进行重绘。在Flutter中，**这一类Widget被称为StatefulWidget（有状态组件）**。这里有一张StatefulWidget的示意图，如下所示：

![897b70ccd83c4043a926d905af24dfb6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/897b70ccd83c4043a926d905af24dfb6.jpg)

图2 StatefulWidget 示意图

看到这里，你可能有点困惑了。因为，我在上一篇文章“Widget，构建Flutter界面的基石”中和你分享到，Widget是不可变的，发生变化时需要销毁重建，所以谈不上状态。那么，这到底是怎么回事呢？

其实，StatefulWidget是以State类代理Widget构建的设计方式实现的。接下来，我就以Image的部分源码为例，和你说明StatefulWidget的构建过程，来帮助你理解这个知识点。

和上面提到的Text一样，Image类的构造函数会接收要被这个类使用的属性参数。然而，不同的是，Image类并没有build方法来创建视图，而是通过createState方法创建了一个类型为_ImageState的state对象，然后由这个对象负责视图的构建。

这个state对象持有并处理了Image类中的状态变化，所以我就以_imageInfo属性为例来和你展开说明。

_imageInfo属性用来给Widget加载真实的图片，一旦State对象通过_handleImageChanged方法监听到_imageInfo属性发生了变化，就会立即调用_ImageState类的setState方法通知Flutter框架：“我这儿的数据变啦，请使用更新后的_imageInfo数据重新加载图片！”。而，Flutter框架则会标记视图状态，更新UI。

```
class Image extends StatefulWidget {
  //构造方法及属性声明部分
  const Image({
    Key key,
    @required this.image,
    //其他参数
  }) : assert(image != null),
       super(key: key);

  final ImageProvider image;
  //其他属性
  ...

  @override
  _ImageState createState() => _ImageState();
  ...
}

class _ImageState extends State<Image> {
  ImageInfo _imageInfo;
  //其他属性
  ...

  void _handleImageChanged(ImageInfo imageInfo, bool synchronousCall) {
    setState(() {
      _imageInfo = imageInfo;
    });
  }
  ...
  @override
  Widget build(BuildContext context) {
    final RawImage image = RawImage(
      image: _imageInfo?.image,
      //其他初始化配置
      ...
    );
    return image;
  }
 ...
}
```

可以看到，在这个例子中，Image以一种动态的方式运行：监听变化，更新视图。与StatelessWidget通过父Widget完全控制UI展示不同，StatefulWidget的父Widget仅定义了它的初始化状态，而其自身视图运行的状态则需要自己处理，并根据处理情况即时更新UI展示。

好了，至此我们已经通过StatelessWidget与StatefulWidget的源码，理解了这两种类型的Widget。这时，你可能会问，既然StatefulWidget不仅可以响应状态变化，又能展示静态UI，那么StatelessWidget这种只能展示静态UI的Widget，还有存在的必要吗？

#### StatefulWidget不是万金油，要慎用

对于UI框架而言，同样的展示效果一般可以通过多种控件实现。从定义来看，StatefulWidget仿佛是万能的，替代StatelessWidget看起来合情合理。于是StatefulWidget的滥用，也容易因此变得顺理成章，难以避免。

但事实是，StatefulWidget的滥用会直接影响Flutter应用的渲染性能。

接下来，在今天这篇文章的最后，我就再带你回顾一下Widget的更新机制，来帮你意识到完全使用StatefulWidget的代价：

> Widget是不可变的，更新则意味着销毁+重建（build）。StatelessWidget是静态的，一旦创建则无需更新；而对于StatefulWidget来说，在State类中调用setState方法更新数据，会触发视图的销毁和重建，也将间接地触发其每个子Widget的销毁和重建。

那么，这意味着什么呢？

如果我们的根布局是一个StatefulWidget，在其State中每调用一次更新UI，都将是一整个页面所有Widget的销毁和重建。

在上一篇文章中，我们了解到，虽然Flutter内部通过Element层可以最大程度地降低对真实渲染视图的修改，提高渲染效率，而不是销毁整个RenderObject树重建。但，大量Widget对象的销毁重建是无法避免的。如果某个子Widget的重建涉及到一些耗时操作，那页面的渲染性能将会急剧下降。

因此，**正确评估你的视图展示需求，避免无谓的StatefulWidget使用，是提高Flutter应用渲染性能最简单也是最直接的手段**。

在接下来的第29篇文章“为什么需要做状态管理，怎么做？”中，我会继续带你学习StatefulWidget常见的几种状态管理方法，与你更为具体地介绍在不同场景中，该选用何种Widget的基本原则。这些原则，你都可以根据实际需要应用到后续工作中。

#### 总结

好了，今天关于StatelessWidget与StatefulWidget的介绍，我们就到这里了。我们一起来回顾下今天的主要知识点。

首先，我带你了解了Flutter基于声明式的UI编程范式，并通过阅读两个典型Widget（Text与Image）源码的方式，与你一起学习了StatelessWidget与StatefulWidget的基本设计思路。

由于Widget采用由父到子、自顶向下的方式进行构建，因此在自定义组件时，我们可以根据父Widget是否能通过初始化参数完全控制其UI展示效果的基本原则，来判断究竟是继承StatelessWidget还是StatefulWidget。

然后，针对StatefulWidget的“万金油”误区，我带你重新回顾了Widget的UI更新机制。尽管Flutter会通过Element层去最大程度降低对真实渲染视图的修改，但大量的Widget销毁重建无法避免，因此避免StatefulWidget的滥用，是最简单、直接地提升应用渲染性能的手段。

需要注意的是，除了我们主动地通过State刷新UI之外，在一些特殊场景下，Widget的build方法有可能会执行多次。因此，我们不应该在这个方法内部，放置太多有耗时的操作。而关于这个build方法在哪些场景下会执行，以及为什么会执行多次，我会在下一篇文章“提到生命周期，我们是在说什么？”中，与你一起详细分析。

#### 思考题

Flutter工程应用模板是计数器示例应用Demo，这个Demo的根节点是一个StatelessWidget。请在保持原有功能的情况下，将这个Demo改造为根节点为StatefulWidget的App。你能通过数据打点，得出这两种方式的性能差异吗？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 提到生命周期，我们是在说什么？

你好，我是陈航。今天，我要和你分享的主题是Flutter中的生命周期是什么。

在上一篇文章中，我们从常见的StatefulWidget的“万金油”误区出发，一起回顾了Widget的UI更新机制。

通过父Widget初始化时传入的静态配置，StatelessWidget就能完全控制其静态展示。而StatefulWidget，还需要借助于State对象，在特定的阶段来处理用户的交互或其内部数据的变化，并体现在UI上。这些特定的阶段，就涵盖了一个组件从加载到卸载的全过程，即生命周期。与iOS的ViewController、Android的Activity一样，Flutter中的Widget也存在生命周期，并且通过State来体现。

而App则是一个特殊的Widget。除了需要处理视图显示的各个阶段（即视图的生命周期）之外，还需要应对应用从启动到退出所经历的各个状态（App的生命周期）。

对于开发者来说，无论是普通Widget（的State）还是App，框架都给我们提供了生命周期的回调，可以让我们选择恰当的时机，做正确的事儿。所以，在对生命周期有了深入理解之后，我们可以写出更加连贯流畅、体验优良的程序。

那么，今天我就分别从Widget（的State）和App这两个维度，与你介绍它们的生命周期。

#### State生命周期

State的生命周期，指的是在用户参与的情况下，其关联的Widget所经历的，从创建到显示再到更新最后到停止，直至销毁等各个过程阶段。

这些不同的阶段涉及到特定的任务处理，因此为了写出一个体验和性能良好的控件，正确理解State的生命周期至关重要。

State的生命周期流程，如图1所示：

![94cd6182ba544a0d98d9c87583e3dab6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/94cd6182ba544a0d98d9c87583e3dab6.jpg)

图1 State生命周期图

可以看到，State的生命周期可以分为3个阶段：创建（插入视图树）、更新（在视图树中存在）、销毁（从视图树中移除）。接下来，我们一起看看每一个阶段的具体流程。

##### 创建

State初始化时会依次执行 ：构造方法 -> initState -> didChangeDependencies -> build，随后完成页面渲染。

我们来看一下初始化过程中每个方法的意义。

- 构造方法是State生命周期的起点，Flutter会通过调用StatefulWidget.createState() 来创建一个State。我们可以通过构造方法，来接收父Widget传递的初始化UI配置数据。这些配置数据，决定了Widget最初的呈现效果。
- initState，会在State对象被插入视图树的时候调用。这个函数在State的生命周期中只会被调用一次，所以我们可以在这里做一些初始化工作，比如为状态变量设定默认值。
- didChangeDependencies则用来专门处理State对象依赖关系变化，会在initState() 调用结束后，被Flutter调用。
- build，作用是构建视图。经过以上步骤，Framework认为State已经准备好了，于是调用build。我们需要在这个函数中，根据父Widget传递过来的初始化配置数据，以及State的当前状态，创建一个Widget然后返回。

##### 更新

Widget的状态更新，主要由3个方法触发：setState、didchangeDependencies与didUpdateWidget。

接下来，我和你分析下这三个方法分别会在什么场景下调用。

- setState：我们最熟悉的方法之一。当状态数据发生变化时，我们总是通过调用这个方法告诉Flutter：“我这儿的数据变啦，请使用更新后的数据重建UI！”
- didChangeDependencies：State对象的依赖关系发生变化后，Flutter会回调这个方法，随后触发组件构建。哪些情况下State对象的依赖关系会发生变化呢？典型的场景是，系统语言Locale或应用主题改变时，系统会通知State执行didChangeDependencies回调方法。
- didUpdateWidget：当Widget的配置发生变化时，比如，父Widget触发重建（即父Widget的状态发生变化时），热重载时，系统会调用这个函数。

一旦这三个方法被调用，Flutter随后就会销毁老Widget，并调用build方法重建Widget。

##### 销毁

组件销毁相对比较简单。比如组件被移除，或是页面销毁的时候，系统会调用deactivate和dispose这两个方法，来移除或销毁组件。

接下来，我们一起看一下它们的具体调用机制：

- 当组件的可见状态发生变化时，deactivate函数会被调用，这时State会被暂时从视图树中移除。值得注意的是，页面切换时，由于State对象在视图树中的位置发生了变化，需要先暂时移除后再重新添加，重新触发组件构建，因此这个函数也会被调用。
- 当State被永久地从视图树中移除时，Flutter会调用dispose函数。而一旦到这个阶段，组件就要被销毁了，所以我们可以在这里进行最终的资源释放、移除监听、清理环境，等等。

如图2所示，左边部分展示了当父Widget状态发生变化时，父子双方共同的生命周期；而中间和右边部分则描述了页面切换时，两个关联的Widget的生命周期函数是如何响应的。

![3cb1622e74ee482ca1f6f3bc29529ae7](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/3cb1622e74ee482ca1f6f3bc29529ae7.jpg)

图2 几种常见场景下State生命周期图

我准备了一张表格，从功能，调用时机和调用次数的维度总结了这些方法，帮助你去理解、记忆。

![0a1b5b9442054269880f9aec1d5d8aa6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0a1b5b9442054269880f9aec1d5d8aa6.jpg)

图3 State生命周期中的方法调用对比

另外，我强烈建议你打开自己的IDE，在应用模板中增加以上回调函数并添加打印代码，多运行几次看看各个函数的执行顺序，从而加深对State生命周期的印象。毕竟，实践出真知。

#### App生命周期

视图的生命周期，定义了视图的加载到构建的全过程，其回调机制能够确保我们可以根据视图的状态选择合适的时机做恰当的事情。而App的生命周期，则定义了App从启动到退出的全过程。

在原生Android、iOS开发中，有时我们需要在对应的App生命周期事件中做相应处理，比如App从后台进入前台、从前台退到后台，或是在UI绘制完成后做一些处理。

这样的需求，在原生开发中，我们可以通过重写Activity、ViewController生命周期回调方法，或是注册应用程序的相关通知，来监听App的生命周期并做相应的处理。而在Flutter中，我们可以利用**WidgetsBindingObserver**类，来实现同样的需求。

接下来，我们就来看看具体如何实现这样的需求。

首先，我们来看看WidgetsBindingObserver中具体有哪些回调函数：

```
abstract class WidgetsBindingObserver {
  //页面pop
  Future<bool> didPopRoute() => Future<bool>.value(false);
  //页面push
  Future<bool> didPushRoute(String route) => Future<bool>.value(false);
  //系统窗口相关改变回调，如旋转
  void didChangeMetrics() { }
  //文本缩放系数变化
  void didChangeTextScaleFactor() { }
  //系统亮度变化
  void didChangePlatformBrightness() { }
  //本地化语言变化
  void didChangeLocales(List<Locale> locale) { }
  //App生命周期变化
  void didChangeAppLifecycleState(AppLifecycleState state) { }
  //内存警告回调
  void didHaveMemoryPressure() { }
  //Accessibility相关特性回调
  void didChangeAccessibilityFeatures() {}
}
```

可以看到，WidgetsBindingObserver这个类提供的回调函数非常丰富，常见的屏幕旋转、屏幕亮度、语言变化、内存警告都可以通过这个实现进行回调。我们通过给WidgetsBinding的单例对象设置监听器，就可以监听对应的回调方法。

考虑到其他的回调相对简单，你可以参考[官方文档](https://api.flutter.dev/flutter/widgets/WidgetsBindingObserver-class.html)，对照着进行练习。因此，我今天主要和你分享App生命周期的回调didChangeAppLifecycleState，和帧绘制回调addPostFrameCallback与addPersistentFrameCallback。

##### 生命周期回调

didChangeAppLifecycleState回调函数中，有一个参数类型为AppLifecycleState的枚举类，这个枚举类是Flutter对App生命周期状态的封装。它的常用状态包括resumed、inactive、paused这三个。

- resumed：可见的，并能响应用户的输入。
- inactive：处在不活动状态，无法处理用户响应。
- paused：不可见并不能响应用户的输入，但是在后台继续活动中。

这里，我来和你分享一个实际案例。

在下面的代码中，我们在initState时注册了监听器，在didChangeAppLifecycleState回调方法中打印了当前的App状态，最后在dispose时把监听器移除：

```
class _MyHomePageState extends State<MyHomePage>  with WidgetsBindingObserver{//这里你可以再回顾下，第7篇文章“函数、类与运算符：Dart是如何处理信息的？”中关于Mixin的内容
...
  @override
  @mustCallSuper
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);//注册监听器
  }
  @override
  @mustCallSuper
  void dispose(){
    super.dispose();
    WidgetsBinding.instance.removeObserver(this);//移除监听器
  }
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) async {
    print("$state");
    if (state == AppLifecycleState.resumed) {
      //do sth
    }
  }
}
```

我们试着切换一下前、后台，观察控制台输出的App状态，可以发现：

- 从后台切入前台，控制台打印的App生命周期变化如下: AppLifecycleState.paused->AppLifecycleState.inactive->AppLifecycleState.resumed；
- 从前台退回后台，控制台打印的App生命周期变化则变成了：AppLifecycleState.resumed->AppLifecycleState.inactive->AppLifecycleState.paused。

可以看到，App前后台切换过程中打印出的状态是完全符合预期的。

![a0197562f83c495cb9995f201e5f53d7](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a0197562f83c495cb9995f201e5f53d7.jpg)

图4 App切换前后台状态变化示意

##### 帧绘制回调

除了需要监听App的生命周期回调做相应的处理之外，有时候我们还需要在组件渲染之后做一些与显示安全相关的操作。

在iOS开发中，我们可以通过dispatch_async(dispatch_get_main_queue(),^{…})方法，让操作在下一个RunLoop执行；而在Android开发中，我们可以通过View.post()插入消息队列，来保证在组件渲染后进行相关操作。

其实，**在Flutter中实现同样的需求会更简单**：依然使用万能的WidgetsBinding来实现。

WidgetsBinding提供了单次Frame绘制回调，以及实时Frame绘制回调两种机制，来分别满足不同的需求：

- 单次Frame绘制回调，通过addPostFrameCallback实现。它会在当前Frame绘制完成后进行进行回调，并且只会回调一次，如果要再次监听则需要再设置一次。

```
WidgetsBinding.instance.addPostFrameCallback((_){
    print("单次Frame绘制回调");//只回调一次
  });
```

- 实时Frame绘制回调，则通过addPersistentFrameCallback实现。这个函数会在每次绘制Frame结束后进行回调，可以用做FPS监测。

```
WidgetsBinding.instance.addPersistentFrameCallback((_){
  print("实时Frame绘制回调");//每帧都回调
});
```

#### 总结

在今天这篇文章中，我和你介绍了State和App的生命周期，这是Flutter给我们提供的，感知Widget和应用在不同阶段状态变化的回调。

首先，我带你重新认识了Widget生命周期的实际承载者State。我将State的生命周期划分为了创建（插入视图树）、更新（在视图树中存在）、销毁（从视图树种移除）这3个阶段，并为你介绍了每个阶段中涉及的关键方法，希望你能够深刻理解Flutter组件从加载到卸载的完整周期。

然后，通过与原生Android、iOS平台能力的对比，以及查看WidgetsBindingObserver源码的方式，我与你讲述了Flutter常用的生命周期状态切换机制。希望你能掌握Flutter的App生命周期监听方法，并理解Flutter常用的生命周期状态切换机制。

最后，我和你一起学习了Flutter帧绘制回调机制，理解了单次Frame绘制回调与实时Frame绘制回调的异同与使用场景。

为了能够精确地控制Widget，Flutter提供了很多状态回调，所以今天这一篇文章，涉及到的方法有些多。但，**只要你分别记住创建、更新与销毁这三条主线的调用规则，就一定能把这些方法的调用顺序串起来，并能在实际开发中运用正确的方法去感知状态变更，写出合理的组件。**

我把今天分享所涉及的全部知识点打包成了一个[小项目](https://github.com/cyndibaby905/11_Flutter_lifecycle)，你可以下载后在工程中实际运行，并对照着今天的课程学习，体会在不同场景下这些函数的调用时机。

#### 思考题

最后，请你思考下这两个问题：

1. 构造方法与initState函数在State的生命周期中都只会被调用一次，也大都用于完成一些初始化的工作。根据我们今天的学习，你能否举出例子，比如哪些操作适合放在构造方法，哪些操作适合放在initState，而哪些操作必须放在initState。
2. 通过didChangeDependencies触发Widget重建时，父子Widget之间的生命周期函数调用时序是怎样的？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 经典控件（一）：文本、图片和按钮在Flutter中怎么用？

你好，我是陈航。

在上一篇文章中，我与你介绍了Widget生命周期的实际承载者State，并详细介绍了初始化、状态更新与控件销毁，这3个不同阶段所涉及的关键方法调用顺序。深入理解视图从加载到构建再到销毁的过程，可以帮助你理解如何根据视图的状态在合适的时机做恰当的事情。

前面几次分享我们讲了很多关于Flutter框架视图渲染的基础知识和原理。但有些同学可能会觉得这些基础知识和原理在实践中并不常用，所以在学习时会选择忽视这些内容。

但其实，像视图数据流转机制、底层渲染方案、视图更新策略等知识，都是构成一个UI框架的根本，看似枯燥，却往往具有最长久的生命力。新框架每年层出不穷，可是扒下那层炫酷的“外衣”，里面其实还是那些最基础的知识和原理。

因此，**只有把这些最基础的知识弄明白了，修炼好了内功，才能触类旁通，由点及面形成自己的知识体系，也能够在框架之上思考应用层构建视图实现的合理性。**

在对视图的基础知识有了整体印象后，我们再来学习Flutter视图系统所提供的UI控件，就会事半功倍了。而作为一个UI框架，与Android、iOS和React类似的，Flutter自然也提供了很多UI控件。而文本、图片和按钮则是这些不同的UI框架中构建视图都要用到的三个最基本的控件。因此，在今天这篇文章中，我就与你一起学习在Flutter中该如何使用它们。

#### 文本控件

文本是视图系统中的常见控件，用来显示一段特定样式的字符串，就比如Android里的TextView、iOS中的UILabel。而在Flutter中，文本展示是通过Text控件实现的。

Text支持两种类型的文本展示，一个是默认的展示单一样式的文本Text，另一个是支持多种混合样式的富文本Text.rich。

我们先来看看**如何使用单一样式的文本Text**。

单一样式文本Text的初始化，是要传入需要展示的字符串。而这个字符串的具体展示效果，受构造函数中的其他参数控制。这些参数大致可以分为两类：

- **控制整体文本布局的参数**，如文本对齐方式textAlign、文本排版方向textDirection，文本显示最大行数maxLines、文本截断规则overflow等等，这些都是构造函数中的参数；
- **控制文本展示样式的参数**，如字体名称fontFamily、字体大小fontSize、文本颜色color、文本阴影shadows等等，这些参数被统一封装到了构造函数中的参数style中。

接下来，我们以一个具体的例子来看看Text控件的使用方法。如下所示，我在代码中定义了一段居中布局、20号红色粗体展示样式的字符串：

```
Text(
  '文本是视图系统中的常见控件，用来显示一段特定样式的字符串，就比如Android里的TextView，或是iOS中的UILabel。',
  textAlign: TextAlign.center,//居中显示
  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20, color: Colors.red),//20号红色粗体展示
);
```

运行效果如下图所示：

![c7c4967c8cc04477a1278b40624f44d4](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c7c4967c8cc04477a1278b40624f44d4.jpg)

图1 单一样式文本Text示例

理解了展示单一样式的文本Text的使用方法后，我们再来看看**如何在一段字符串中支持多种混合展示样式**。

**混合展示样式与单一样式的关键区别在于分片**，即如何把一段字符串分为几个片段来管理，给每个片段单独设置样式。面对这样的需求，在Android中，我们使用SpannableString来实现；在iOS中，我们使用NSAttributedString来实现；而在Flutter中也有类似的概念，即TextSpan。

TextSpan定义了一个字符串片段该如何控制其展示样式，而将这些有着独立展示样式的字符串组装在一起，则可以支持混合样式的富文本展示。

如下方代码所示，我们分别定义了黑色与红色两种展示样式，随后把一段字符串分成了4个片段，并设置了不同的展示样式：

```
TextStyle blackStyle = TextStyle(fontWeight: FontWeight.normal, fontSize: 20, color: Colors.black); //黑色样式

TextStyle redStyle = TextStyle(fontWeight: FontWeight.bold, fontSize: 20, color: Colors.red); //红色样式

Text.rich(
    TextSpan(
        children: <TextSpan>[
          TextSpan(text:'文本是视图系统中常见的控件，它用来显示一段特定样式的字符串，类似', style: redStyle), //第1个片段，红色样式
          TextSpan(text:'Android', style: blackStyle), //第1个片段，黑色样式
          TextSpan(text:'中的', style:redStyle), //第1个片段，红色样式
          TextSpan(text:'TextView', style: blackStyle) //第1个片段，黑色样式
        ]),
  textAlign: TextAlign.center,
);
```

运行效果，如下图所示：

![862edc48adbc461bb6f03d285d75dd9d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/862edc48adbc461bb6f03d285d75dd9d.jpg)

图2 混合样式富文本Text.rich示例

接下来，我们再看看Flutter中的图片控件Image。

#### 图片

使用Image，可以让我们向用户展示一张图片。图片的显示方式有很多，比如资源图片、网络图片、文件图片等，图片格式也各不相同，因此在Flutter中也有多种方式，用来加载不同形式、支持不同格式的图片：

- 加载本地资源图片，如Image.asset(‘images/logo.png’)；
- 加载本地（File文件）图片，如Image.file(new File(’/storage/xxx/xxx/test.jpg’))；
- 加载网络图片，如Image.network(`'http://xxx/xxx/test.gif'`) 。

除了可以根据图片的显示方式设置不同的图片源之外，图片的构造方法还提供了填充模式fit、拉伸模式centerSlice、重复模式repeat等属性，可以针对图片与目标区域的宽高比差异制定排版模式。

这，和Android中ImageView、iOS里的UIImageView的属性都是类似的。因此，我在这里就不再过多展开了。你可以参考官方文档中的[Image的构造函数](https://api.flutter.dev/flutter/widgets/Image/Image.html)部分，去查看Image控件的具体使用方法。

关于图片展示，我还要和你分享下Flutter中的**FadeInImage**控件。在加载网络图片的时候，为了提升用户的等待体验，我们往往会加入占位图、加载动画等元素，但是默认的Image.network构造方法并不支持这些高级功能，这时候FadeInImage控件就派上用场了。

FadeInImage控件提供了图片占位的功能，并且支持在图片加载完成时淡入淡出的视觉效果。此外，由于Image支持gif格式，我们甚至还可以将一些炫酷的加载动画作为占位图。

下述代码展示了这样的场景。我们在加载大图片时，将一张loading的gif作为占位图展示给用户：

```
FadeInImage.assetNetwork(
  placeholder: 'assets/loading.gif', //gif占位
  image: 'https://xxx/xxx/xxx.jpg',
  fit: BoxFit.cover, //图片拉伸模式
  width: 200,
  height: 200,
)
```

![97d185c67f7948b5b96e693d46f909db](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/97d185c67f7948b5b96e693d46f909db.jpg)

图3 FadeInImage占位图

Image控件需要根据图片资源异步加载的情况，决定自身的显示效果，因此是一个StatefulWidget。图片加载过程由ImageProvider触发，而ImageProvider表示异步获取图片数据的操作，可以从资源、文件和网络等不同的渠道获取图片。

首先，ImageProvider根据_ImageState中传递的图片配置生成对应的图片缓存key；然后，去ImageCache中查找是否有对应的图片缓存，如果有，则通知_ImageState刷新UI；如果没有，则启动ImageStream开始异步加载，加载完毕后，更新缓存；最后，通知_ImageState刷新UI。

图片展示的流程，可以用以下流程图表示：

![3964a4a8a817430db840ef72bcac57d8](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/3964a4a8a817430db840ef72bcac57d8.jpg)

图4 图片加载流程

值得注意的是，ImageCache使用LRU（Least Recently Used，最近最少使用）算法进行缓存更新策略，并且默认最多存储 1000张图片，最大缓存限制为100MB，当限定的空间已存满数据时，把最久没有被访问到的图片清除。图片**缓存只会在运行期间生效，也就是只缓存在内存中**。如果想要支持缓存到文件系统，可以使用第三方的[CachedNetworkImage](https://pub.dev/packages/cached_network_image/)控件。

CachedNetworkImage的使用方法与Image类似，除了支持图片缓存外，还提供了比FadeInImage更为强大的加载过程占位与加载错误占位，可以支持比用图片占位更灵活的自定义控件占位。

在下面的代码中，我们在加载图片时，不仅给用户展示了作为占位的转圈loading，还提供了一个错误图兜底，以备图片加载出错：

```
CachedNetworkImage(
        imageUrl: "http://xxx/xxx/jpg",
        placeholder: (context, url) => CircularProgressIndicator(),
        errorWidget: (context, url, error) => Icon(Icons.error),
     )
```

最后，我们再来看看Flutter中的按钮控件。

#### 按钮

通过按钮，我们可以响应用户的交互事件。Flutter提供了三个基本的按钮控件，即FloatingActionButton、FlatButton和RaisedButton。

- FloatingActionButton：一个圆形的按钮，一般出现在屏幕内容的前面，用来处理界面中最常用、最基础的用户动作。在之前的第5篇文章“[从标准模板入手，体会Flutter代码是如何运行在原生系统上的](https://time.geekbang.org/column/article/106199)”中，计数器示例的“+”悬浮按钮就是一个FloatingActionButton。
- RaisedButton：凸起的按钮，默认带有灰色背景，被点击后灰色背景会加深。
- FlatButton：扁平化的按钮，默认透明背景，被点击后会呈现灰色背景。

这三个按钮控件的使用方法类似，唯一的区别只是默认样式不同而已。

下述代码中，我分别定义了FloatingActionButton、FlatButton与RaisedButton，它们的功能完全一样，在点击时打印一段文字：

```
FloatingActionButton(onPressed: () => print('FloatingActionButton pressed'),child: Text('Btn'),);
FlatButton(onPressed: () => print('FlatButton pressed'),child: Text('Btn'),);
RaisedButton(onPressed: () => print('RaisedButton pressed'),child: Text('Btn'),);
```

![0386b6d9c1044a30a6f2867e74af4261](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0386b6d9c1044a30a6f2867e74af4261.jpg)

图5 按钮控件

既然是按钮，因此除了控制基本样式之外，还需要响应用户点击行为。这就对应着按钮控件中的两个最重要的参数了：

- onPressed参数用于设置点击回调，告诉Flutter在按钮被点击时通知我们。如果onPressed参数为空，则按钮会处于禁用状态，不响应用户点击。
- child参数用于设置按钮的内容，告诉Flutter控件应该长成什么样，也就是控制着按钮控件的基本样式。child可以接收任意的Widget，比如我们在上面的例子中传入的Text，除此之外我们还可以传入Image等控件。

虽然我们可以通过child参数来控制按钮控件的基本样式，但是系统默认的样式还是太单调了。因此通常情况下，我们还是会进行控件样式定制。

与Text控件类似，按钮控件也提供了丰富的样式定制功能，比如背景颜色color、按钮形状shape、主题颜色colorBrightness，等等。

接下来，我就以FlatButton为例，与你介绍按钮的样式定制：

```
FlatButton(
    color: Colors.yellow, //设置背景色为黄色
    shape:BeveledRectangleBorder(borderRadius: BorderRadius.circular(20.0)), //设置斜角矩形边框
    colorBrightness: Brightness.light, //确保文字按钮为深色
    onPressed: () => print('FlatButton pressed'),
    child: Row(children: <Widget>[Icon(Icons.add), Text("Add")],)
)；
```

可以看到，我们将一个加号Icon与文本组合，定义了按钮的基本外观；随后通过shape来指定其外形为一个斜角矩形边框，并将按钮的背景色设置为黄色。

因为按钮背景颜色是浅色的，为避免按钮文字看不清楚，我们通过设置按钮主题colorBrightness为Brightness.light，保证按钮文字颜色为深色。

展示效果如下：

![bfce61f210a344b5a91955fcb136e46a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/bfce61f210a344b5a91955fcb136e46a.jpg)

图6 按钮控件定制外观

#### 总结

UI控件是构建一个视图的基本元素，而文本、图片和按钮则是其中最经典的控件。

接下来，我们简单回顾一下今天的内容，以便加深理解与记忆。

首先，我们认识了支持单一样式和混合样式两种类型的文本展示控件Text。其中，通过TextStyle控制字符串的展示样式，其他参数控制文本布局，可以实现单一样式的文本展示；而通过TextSpan将字符串分割为若干片段，对每个片段单独设置样式后组装，可以实现支持混合样式的富文本展示。

然后，我带你学习了支持多种图片源加载方式的图片控件Image。Image内部通过ImageProvider根据缓存状态，触发异步加载流程，通知_ImageState刷新UI。不过，由于图片缓存是内存缓存，因此只在运行期间生效。如果要支持缓存到文件系统，可以使用第三方的CachedNetworkImage。

最后，我们学习了按钮控件。Flutter提供了多种按钮控件，而它们的使用方法也都类似。其中，控件初始化的child参数用于设置按钮长什么样，而onPressed参数则用于设置点击回调。与Text类似，按钮内部也有丰富的UI定制接口，可以满足开发者的需求。

通过今天的学习，我们可以发现，在UI基本信息的表达上，Flutter的经典控件与原生Android、iOS系统提供的控件没有什么本质区别。但是，在自定义控件样式上，Flutter的这些经典控件提供了强大而简洁的扩展能力，使得我们可以快速开发出功能复杂、样式丰富的页面。

#### 思考题

最后，我给你留下一道思考题吧。

请你打开IDE，阅读Flutter SDK中Text、Image、FadeInImage，以及按钮控件FloatingActionButton、FlatButton与RaisedButton的源码，在build函数中找出在内部真正承载其视觉功能的控件。请和我分享下，你在这一过程中发现了什么现象？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 经典控件（二）：UITableView_ListView在Flutter中是什么？

你好，我是陈航。

在上一篇文章中，我和你一起学习了文本、图片和按钮这3大经典组件在Flutter中的使用方法，以及如何在实际开发中根据不同的场景，去自定义展示样式。

文本、图片和按钮这些基本元素，需要进行排列组合，才能构成我们看到的UI视图。那么，当这些基本元素的排列布局超过屏幕显示尺寸（即超过一屏）时，我们就需要引入列表控件来展示视图的完整内容，并根据元素的多少进行自适应滚动展示。

这样的需求，在Android中是由ListView或RecyclerView实现的，在iOS中是用UITableView实现的；而在Flutter中，实现这种需求的则是列表控件ListView。

#### ListView

在Flutter中，ListView可以沿一个方向（垂直或水平方向）来排列其所有子Widget，因此常被用于需要展示一组连续视图元素的场景，比如通信录、优惠券、商家列表等。

我们先来看看ListView怎么用。**ListView提供了一个默认构造函数ListView**，我们可以通过设置它的children参数，很方便地将所有的子Widget包含到ListView中。

不过，这种创建方式要求提前将所有子Widget一次性创建好，而不是等到它们真正在屏幕上需要显示时才创建，所以有一个很明显的缺点，就是性能不好。因此，**这种方式仅适用于列表中含有少量元素的场景**。

如下所示，我定义了一组列表项组件，并将它们放在了垂直滚动的ListView中：

```
ListView(
  children: <Widget>[
    //设置ListTile组件的标题与图标
    ListTile(leading: Icon(Icons.map),  title: Text('Map')),
    ListTile(leading: Icon(Icons.mail), title: Text('Mail')),
    ListTile(leading: Icon(Icons.message), title: Text('Message')),
  ]);
```

> 备注：ListTile是Flutter提供的用于快速构建列表项元素的一个小组件单元，用于1~3行（leading、title、subtitle）展示文本、图标等视图元素的场景，通常与ListView配合使用。- 上面这段代码中用到ListTile，是为了演示ListView的能力。关于ListTile的具体使用细节，并不是本篇文章的重点，如果你想深入了解的话，可以参考[官方文档](https://api.flutter.dev/flutter/material/ListTile-class.html)。

运行效果，如下图所示：

![8654e8eba2d348029a13c075685aa012](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/8654e8eba2d348029a13c075685aa012.jpg)

图1 ListView默认构造函数

除了默认的垂直方向布局外，ListView还可以通过设置scrollDirection参数支持水平方向布局。如下所示，我定义了一组不同颜色背景的组件，将它们的宽度设置为140，并包在了水平布局的ListView中，让它们可以横向滚动：

```
ListView(
    scrollDirection: Axis.horizontal,
    itemExtent: 140, //item延展尺寸(宽度)
    children: <Widget>[
      Container(color: Colors.black),
      Container(color: Colors.red),
      Container(color: Colors.blue),
      Container(color: Colors.green),
      Container(color: Colors.yellow),
      Container(color: Colors.orange),
    ]);
```

运行效果，如下图所示：

![54ad0314599045ebabfe644f85380f74](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/54ad0314599045ebabfe644f85380f74.jpg)

图2 水平滚动的ListView

在这个例子中，我们一次性创建了6个子Widget。但从图2的运行效果可以看到，由于屏幕的宽高有限，同一时间用户只能看到3个Widget。也就是说，是否一次性提前构建出所有要展示的子Widget，与用户而言并没有什么视觉上的差异。

所以，考虑到创建子Widget产生的性能问题，更好的方法是抽象出创建子Widget的方法，交由ListView统一管理，在真正需要展示该子Widget时再去创建。

**ListView的另一个构造函数ListView.builder，则适用于子Widget比较多的场景**。这个构造函数有两个关键参数：

- itemBuilder，是列表项的创建方法。当列表滚动到相应位置时，ListView会调用该方法创建对应的子Widget。
- itemCount，表示列表项的数量，如果为空，则表示ListView为无限列表。

同样地，我通过一个案例，与你说明itemBuilder与itemCount这两个参数的具体用法。

我定义了一个拥有100个列表元素的ListView，在列表项的创建方法中，分别将index的值设置为ListTile的标题与子标题。比如，第一行列表项会展示title 0 body 0：

```
ListView.builder(
    itemCount: 100, //元素个数
    itemExtent: 50.0, //列表项高度
    itemBuilder: (BuildContext context, int index) => ListTile(title: Text("title $index"), subtitle: Text("body $index"))
);
```

这里需要注意的是，**itemExtent并不是一个必填参数。但，对于定高的列表项元素，我强烈建议你提前设置好这个参数的值。**

因为如果这个参数为null，ListView会动态地根据子Widget创建完成的结果，决定自身的视图高度，以及子Widget在ListView中的相对位置。在滚动发生变化而列表项又很多时，这样的计算就会非常频繁。

但如果提前设置好itemExtent，ListView则可以提前计算好每一个列表项元素的相对位置，以及自身的视图高度，省去了无谓的计算。

因此，在ListView中，指定itemExtent比让子Widget自己决定自身高度会更高效。

运行这个示例，效果如下所示：

![1b5d09ea270a4f399bc84ba01ee33ca9](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/1b5d09ea270a4f399bc84ba01ee33ca9.jpg)

图3 ListView.builder构造函数

可能你已经发现了，我们的列表还缺少分割线。在ListView中，有两种方式支持分割线：

- 一种是，在itemBuilder中，根据index的值动态创建分割线，也就是将分割线视为列表项的一部分；
- 另一种是，使用ListView的另一个构造方法ListView.separated，单独设置分割线的样式。

第一种方式实际上是视图的组合，之前的分享中我们已经多次提及，对你来说应该已经比较熟悉了，这里我就不再过多地介绍了。接下来，我和你演示一下**如何使用ListView.separated设置分割线。**

与ListView.builder抽离出了子Widget的构建方法类似，ListView.separated抽离出了分割线的创建方法separatorBuilder，以便根据index设置不同样式的分割线。

如下所示，我针对index为偶数的场景，创建了绿色的分割线，而针对index为奇数的场景，创建了红色的分割线：

```
//使用ListView.separated设置分割线
ListView.separated(
    itemCount: 100,
    separatorBuilder: (BuildContext context, int index) => index %2 ==0? Divider(color: Colors.green) : Divider(color: Colors.red),//index为偶数，创建绿色分割线；index为奇数，则创建红色分割线
    itemBuilder: (BuildContext context, int index) => ListTile(title: Text("title $index"), subtitle: Text("body $index"))//创建子Widget
)
```

运行效果，如下所示：

![05e97e474c7d443f99368042e081085e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/05e97e474c7d443f99368042e081085e.jpg)

图4 ListView.separated构造函数

好了，我已经与你分享完了ListView的常见构造函数。接下来，我准备了一张表格，总结了ListView常见的构造方法及其适用场景，供你参考，以便理解与记忆：

![5ecaa1a05b8448c785734ae40ad7167f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/5ecaa1a05b8448c785734ae40ad7167f.jpg)

图5 ListView常见的构造方法及其适用场景

#### CustomScrollView

好了，ListView实现了单一视图下可滚动Widget的交互模型，同时也包含了UI显示相关的控制逻辑和布局模型。但是，对于某些特殊交互场景，比如多个效果联动、嵌套滚动、精细滑动、视图跟随手势操作等，还需要嵌套多个ListView来实现。这时，各自视图的滚动和布局模型就是相互独立、分离的，就很难保证整个页面统一一致的滑动效果。

那么，**Flutter是如何解决多ListView嵌套时，页面滑动效果不一致的问题的呢？**

在Flutter中有一个专门的控件CustomScrollView，用来处理多个需要自定义滚动效果的Widget。在CustomScrollView中，**这些彼此独立的、可滚动的Widget被统称为Sliver**。

比如，ListView的Sliver实现为SliverList，AppBar的Sliver实现为SliverAppBar。这些Sliver不再维护各自的滚动状态，而是交由CustomScrollView统一管理，最终实现滑动效果的一致性。

接下来，我通过一个滚动视差的例子，与你演示CustomScrollView的使用方法。

**视差滚动**是指让多层背景以不同的速度移动，在形成立体滚动效果的同时，还能保证良好的视觉体验。 作为移动应用交互设计的热点趋势，越来越多的移动应用使用了这项技术。

以一个有着封面头图的列表为例，我们希望封面头图和列表这两层视图的滚动联动起来，当用户滚动列表时，头图会根据用户的滚动手势，进行缩小和展开。

经分析得出，要实现这样的需求，我们需要两个Sliver：作为头图的SliverAppBar，与作为列表的SliverList。具体的实现思路是：

- 在创建SliverAppBar时，把flexibleSpace参数设置为悬浮头图背景。flexibleSpace可以让背景图显示在AppBar下方，高度和SliverAppBar一样；
- 而在创建SliverList时，通过SliverChildBuilderDelegate参数实现列表项元素的创建；
- 最后，将它们一并交由CustomScrollView的slivers参数统一管理。

具体的示例代码如下所示：

```
CustomScrollView(
  slivers: <Widget>[
    SliverAppBar(//SliverAppBar作为头图控件
      title: Text('CustomScrollView Demo'),//标题
      floating: true,//设置悬浮样式
      flexibleSpace: Image.network("https://xx.jpg",fit:BoxFit.cover),//设置悬浮头图背景
      expandedHeight: 300,//头图控件高度
    ),
    SliverList(//SliverList作为列表控件
      delegate: SliverChildBuilderDelegate(
            (context, index) => ListTile(title: Text('Item #$index')),//列表项创建方法
        childCount: 100,//列表元素个数
      ),
    ),
  ]);
```

运行一下，视差滚动效果如下所示：

![d3393957567f4952831037637b15e64d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d3393957567f4952831037637b15e64d.jpg)

图6 CustomScrollView示例

#### ScrollController与ScrollNotification

现在，你应该已经知道如何实现滚动视图的视觉和交互效果了。接下来，我再与你分享一个更为复杂的问题：在某些情况下，我们希望获取视图的滚动信息，并进行相应的控制。比如，列表是否已经滑到底（顶）了？如何快速回到列表顶部？列表滚动是否已经开始，或者是否已经停下来了？

对于前两个问题，我们可以使用ScrollController进行滚动信息的监听，以及相应的滚动控制；而最后一个问题，则需要接收ScrollNotification通知进行滚动事件的获取。下面我将分别与你介绍。

在Flutter中，因为Widget并不是渲染到屏幕的最终视觉元素（RenderObject才是），所以我们无法像原生的Android或iOS系统那样，向持有的Widget对象获取或设置最终渲染相关的视觉信息，而必须通过对应的组件控制器才能实现。

ListView的组件控制器则是ScrollControler，我们可以通过它来获取视图的滚动信息，更新视图的滚动位置。

一般而言，获取视图的滚动信息往往是为了进行界面的状态控制，因此ScrollController的初始化、监听及销毁需要与StatefulWidget的状态保持同步。

如下代码所示，我们声明了一个有着100个元素的列表项，当滚动视图到特定位置后，用户可以点击按钮返回列表顶部：

- 首先，我们在State的初始化方法里，创建了ScrollController，并通过_controller.addListener注册了滚动监听方法回调，根据当前视图的滚动位置，判断当前是否需要展示“Top”按钮。
- 随后，在视图构建方法build中，我们将ScrollController对象与ListView进行了关联，并且在RaisedButton中注册了对应的回调方法，可以在点击按钮时通过_controller.animateTo方法返回列表顶部。
- 最后，在State的销毁方法中，我们对ScrollController进行了资源释放。

```
class MyAPPState extends State<MyApp> {
  ScrollController _controller;//ListView控制器
  bool isToTop = false;//标示目前是否需要启用"Top"按钮
  @override
  void initState() {
    _controller = ScrollController();
    _controller.addListener(() {//为控制器注册滚动监听方法
      if(_controller.offset > 1000) {//如果ListView已经向下滚动了1000，则启用Top按钮
        setState(() {isToTop = true;});
      } else if(_controller.offset < 300) {//如果ListView向下滚动距离不足300，则禁用Top按钮
        setState(() {isToTop = false;});
      }
    });
    super.initState();
  }

  Widget build(BuildContext context) {
    return MaterialApp(
        ...
        //顶部Top按钮，根据isToTop变量判断是否需要注册滚动到顶部的方法
        RaisedButton(onPressed: (isToTop ? () {
                  if(isToTop) {
                    _controller.animateTo(.0,
                        duration: Duration(milliseconds: 200),
                        curve: Curves.ease
                    );//做一个滚动到顶部的动画
                  }
                }:null),child: Text("Top"),)
        ...
        ListView.builder(
                controller: _controller,//初始化传入控制器
                itemCount: 100,//列表元素总数
                itemBuilder: (context, index) => ListTile(title: Text("Index : $index")),//列表项构造方法
               )
        ...
    );

  @override
  void dispose() {
    _controller.dispose(); //销毁控制器
    super.dispose();
  }
}
```

ScrollController的运行效果如下所示：

![02282eb1d4f1428ca9b7925c955c1777](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/02282eb1d4f1428ca9b7925c955c1777.jpg)

图7 ScrollController示例

介绍完了如何通过ScrollController来监听ListView滚动信息，以及怎样进行滚动控制之后，接下来我们再看看**如何获取ScrollNotification通知，从而感知ListView的各类滚动事件**。

在Flutter中，ScrollNotification通知的获取是通过NotificationListener来实现的。与ScrollController不同的是，NotificationListener是一个Widget，为了监听滚动类型的事件，我们需要将NotificationListener添加为ListView的父容器，从而捕获ListView中的通知。而这些通知，需要通过onNotification回调函数实现监听逻辑：

```
Widget build(BuildContext context) {
  return MaterialApp(
    title: 'ScrollController Demo',
    home: Scaffold(
      appBar: AppBar(title: Text('ScrollController Demo')),
      body: NotificationListener<ScrollNotification>(//添加NotificationListener作为父容器
        onNotification: (scrollNotification) {//注册通知回调
          if (scrollNotification is ScrollStartNotification) {//滚动开始
            print('Scroll Start');
          } else if (scrollNotification is ScrollUpdateNotification) {//滚动位置更新
            print('Scroll Update');
          } else if (scrollNotification is ScrollEndNotification) {//滚动结束
            print('Scroll End');
          }
        },
        child: ListView.builder(
          itemCount: 30,//列表元素个数
          itemBuilder: (context, index) => ListTile(title: Text("Index : $index")),//列表项创建方法
        ),
      )
    )
  );
}
```

相比于ScrollController只能和具体的ListView关联后才可以监听到滚动信息；通过NotificationListener则可以监听其子Widget中的任意ListView，不仅可以得到这些ListView的当前滚动位置信息，还可以获取当前的滚动事件信息 。

#### 总结

在处理用于展示一组连续、可滚动的视图元素的场景，Flutter提供了比原生Android、iOS系统更加强大的列表组件ListView与CustomScrollView，不仅可以支持单一视图下可滚动Widget的交互模型及UI控制模型，对于某些特殊交互，需要嵌套多重可滚动Widget的场景，也提供了统一管理的机制，最终实现体验一致的滑动效果。这些强大的组件，使得我们不仅可以开发出样式丰富的界面，更可以实现复杂的交互。

接下来，我们简单回顾一下今天的内容，以便加深你的理解与记忆。

首先，我们认识了ListView组件。它同时支持垂直方向和水平方向滚动，不仅提供了少量一次性创建子视图的默认构造方式，也提供了大量按需创建子视图的ListView.builder机制，并且支持自定义分割线。为了节省性能，对于定高的列表项视图，提前指定itemExtent比让子Widget自己决定要更高效。

随后，我带你学习了CustomScrollView组件。它引入了Sliver的概念，将多重嵌套的可滚动视图的交互与布局进行统一接管，使得像视差滚动这样的高级交互变得更加容易。

最后，我们学习了ScrollController与NotificationListener，前者与ListView绑定，进行滚动信息的监听，进行相应的滚动控制；而后者，通过将ListView纳入子Widget，实现滚动事件的获取。

我把今天分享讲的三个例子（视差、ScrollController、ScrollNotification）放到了[GitHub](https://github.com/cyndibaby905/13_listview_demo)上，你可以下载后在工程中实际运行，并对照着今天的知识点进行学习，体会ListView的一些高级用法。

#### 思考题

最后，我给你留下两个小作业吧：

1. 在ListView.builder方法中，ListView根据Widget是否将要出现在可视区域内，按需创建。对于一些场景，为了避免Widget渲染时间过长（比如图片下载），我们需要提前将可视区域上下一定区域内的Widget提前创建好。那么，在Flutter中，如何才能实现呢？
2. 请你使用NotificationListener，来实现图7 ScrollController示例中同样的功能。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 经典布局：如何定义子控件在父容器中排版的位置？

你好，我是陈航。

在前面两篇文章中，我们一起学习了构建视图的基本元素：文本、图片和按钮，用于展示一组连续视图元素的ListView，以及处理多重嵌套的可滚动视图的CustomScrollView。

在Flutter中，一个完整的界面通常就是由这些小型、单用途的基本控件元素依据特定的布局规则堆砌而成的。那么今天，我就带你一起学习一下，在Flutter中，搭建出一个漂亮的布局，我们需要了解哪些布局规则，以及这些规则与其他平台类似概念的差别在哪里。希望这样的设计，可以帮助你站在已有经验的基础上去高效学习Flutter的布局规则。

我们已经知道，在Flutter中一切皆Widget，那么布局也不例外。但与基本控件元素不同，布局类的Widget并不会直接呈现视觉内容，而是作为承载其他子Widget的容器。

这些布局类的Widget，内部都会包含一个或多个子控件，并且都提供了摆放子控件的不同布局方式，可以实现子控件的对齐、嵌套、层叠和缩放等。而我们要做的就是，通过各种定制化的参数，将其内部的子Widget依照自己的布局规则放置在特定的位置上，最终形成一个漂亮的布局。

Flutter提供了31种[布局Widget](https://flutter.dev/docs/development/ui/widgets/layout)，对布局控件的划分非常详细，一些相同（或相似）的视觉效果可以通过多种布局控件实现，因此布局类型相比原生Android、iOS平台多了不少。比如，Android布局一般就只有FrameLayout、LinearLayout、RelativeLayout、GridLayout和TableLayout这5种，而iOS的布局更少，只有Frame布局和自动布局两种。

为了帮你建立起对布局类Widget的认知，了解基本布局类Widget的布局特点和用法，从而学以致用快速上手开发，在今天的这篇文章中，我特意挑选了几类在开发Flutter应用时，最常用也最有代表性的布局Widget，包括单子Widget布局、多子Widget布局、层叠Widget布局，与你展开介绍。

掌握了这些典型的Widget，你也就基本掌握了构建一个界面精美的App所需要的全部布局方式了。接下来，我们就先从单子Widget布局聊起吧。

#### 单子Widget布局：Container、Padding与Center

单子Widget布局类容器比较简单，一般用来对其唯一的子Widget进行样式包装，比如限制大小、添加背景色样式、内间距、旋转变换等。这一类布局Widget，包括Container、Padding与Center三种。

Container，是一种允许在其内部添加其他控件的控件，也是UI框架中的一个常见概念。

在Flutter中，Container本身可以单独作为控件存在（比如单独设置背景色、宽高），也可以作为其他控件的父级存在：Container可以定义布局过程中子Widget如何摆放，以及如何展示。与其他框架不同的是，**Flutter的Container仅能包含一个子Widget**。

所以，对于多个子Widget的布局场景，我们通常会这样处理：先用一个根Widget去包装这些子Widget，然后把这个根Widget放到Container中，再由Container设置它的对齐alignment、边距padding等基础属性和样式属性。

接下来，我通过一个示例，与你演示如何定义一个Container。

在这个示例中，我将一段较长的文字，包装在一个红色背景、圆角边框的、固定宽高的Container中，并分别设置了Container的外边距（距离其父Widget的边距）和内边距（距离其子Widget的边距）：

```
Container(
  child: Text('Container（容器）在UI框架中是一个很常见的概念，Flutter也不例外。'),
  padding: EdgeInsets.all(18.0), // 内边距
  margin: EdgeInsets.all(44.0), // 外边距
  width: 180.0,
  height:240,
  alignment: Alignment.center, // 子Widget居中对齐
  decoration: BoxDecoration( //Container样式
    color: Colors.red, // 背景色
    borderRadius: BorderRadius.circular(10.0), // 圆角边框
  ),
)
```

![efa3656188874d219b369cc9f09108c9](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/efa3656188874d219b369cc9f09108c9.jpg)

图1 Container示例

如果我们只需要将子Widget设定间距，则可以使用另一个单子容器控件Padding进行内容填充：

```
Padding(
  padding: EdgeInsets.all(44.0),
  child: Text('Container（容器）在UI框架中是一个很常见的概念，Flutter也不例外。'),
);
```

![ac81266c91c5407891944d1ec7c459f8](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ac81266c91c5407891944d1ec7c459f8.jpg)

图2 Padding示例

在需要设置内容间距时，我们可以通过EdgeInsets的不同构造函数，分别制定四个方向的不同补白方式，如均使用同样数值留白、只设置左留白或对称方向留白等。如果你想更深入地了解这部分内容，可以参考这个[API文档](https://api.flutter.dev/flutter/painting/EdgeInsets-class.html#constructors)。

接下来，我们再来看看单子Widget布局容器中另一个常用的容器Center。正如它的名字一样，Center会将其子Widget居中排列。

比如，我们可以把一个Text包在Center里，实现居中展示：

```
Scaffold(
  body: Center(child: Text("Hello")) // This trailing comma makes auto-formatting nicer for build methods.
);
```

![83c2e174eb334602998fed8c4a492152](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/83c2e174eb334602998fed8c4a492152.jpg)

图3 Center示例

需要注意的是，为了实现居中布局，Center所占据的空间一定要比其子Widget要大才行，这也是显而易见的：如果Center和其子Widget一样大，自然就不需要居中，也没空间居中了。因此Center通常会结合Container一起使用。

现在，我们结合Container，一起看看Center的具体使用方法吧。

```
Container(
  child: Center(child: Text('Container（容器）在UI框架中是一个很常见的概念，Flutter也不例外。')),
  padding: EdgeInsets.all(18.0), // 内边距
  margin: EdgeInsets.all(44.0), // 外边距
  width: 180.0,
  height:240,
  decoration: BoxDecoration( //Container样式
    color: Colors.red, // 背景色
    borderRadius: BorderRadius.circular(10.0), // 圆角边框
  ),
);
```

可以看到，我们通过Center容器实现了Container容器中**alignment: Alignment.center**的效果。

事实上，为了达到这一效果，Container容器与Center容器底层都依赖了同一个容器Align，通过它实现子Widget的对齐方式。Align的使用也比较简单，如果你想深入了解的话，可以参考[官方文档](https://api.flutter.dev/flutter/widgets/Align-class.html)，这里我就不再过多介绍了。

接下来，我们再看看多子Widget布局的三种方式，即Row、Column与Expanded。

#### 多子Widget布局：Row、Column与Expanded

对于拥有多个子Widget的布局类容器而言，其布局行为无非就是两种规则的抽象：水平方向上应该如何布局、垂直方向上应该如何布局。

如同Android的LinearLayout、前端的Flex布局一样，Flutter中也有类似的概念，即将子Widget按行水平排列的Row，按列垂直排列的Column，以及负责分配这些子Widget在布局方向（行/列）中剩余空间的Expanded。

Row与Column的使用方法很简单，我们只需要将各个子Widget按序加入到children数组即可。在下面的代码中，我们把4个分别设置了不同的颜色和宽高的Container加到Row与Column中：

```
//Row的用法示范
Row(
  children: <Widget>[
    Container(color: Colors.yellow, width: 60, height: 80,),
    Container(color: Colors.red, width: 100, height: 180,),
    Container(color: Colors.black, width: 60, height: 80,),
    Container(color: Colors.green, width: 60, height: 80,),
  ],
);

//Column的用法示范
Column(
  children: <Widget>[
    Container(color: Colors.yellow, width: 60, height: 80,),
    Container(color: Colors.red, width: 100, height: 180,),
    Container(color: Colors.black, width: 60, height: 80,),
    Container(color: Colors.green, width: 60, height: 80,),
  ],
);
```

![23d1616f9bcc4dd5af3b10b7104c6f68](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/23d1616f9bcc4dd5af3b10b7104c6f68.jpg)

(a)Row示例

![80fa0e6cd6e944229b2a25fb4f28a73f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/80fa0e6cd6e944229b2a25fb4f28a73f.jpg)

(b)Column示例

图4 Row与Column示例

可以看到，单纯使用Row和Column控件，在子Widget的尺寸较小时，无法将容器填满，视觉样式比较难看。对于这样的场景，我们可以通过Expanded控件，来制定分配规则填满容器的剩余空间。

比如，我们希望Row组件（或Column组件）中的绿色容器与黄色容器均分剩下的空间，于是就可以设置它们的弹性系数参数flex都为1，这两个Expanded会按照其flex的比例（即1：1）来分割剩余的Row横向（Column纵向）空间：

```
Row(
  children: <Widget>[
    Expanded(flex: 1, child: Container(color: Colors.yellow, height: 60)), //设置了flex=1，因此宽度由Expanded来分配
    Container(color: Colors.red, width: 100, height: 180,),
    Container(color: Colors.black, width: 60, height: 80,),
    Expanded(flex: 1, child: Container(color: Colors.green,height: 60),)/设置了flex=1，因此宽度由Expanded来分配
  ],
);
```

![91e7aba8cc4b494e91fe96226ff57c5d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/91e7aba8cc4b494e91fe96226ff57c5d.jpg)

图5 Expanded控件示例

于Row与Column而言，Flutter提供了依据坐标轴的布局对齐行为，即根据布局方向划分出主轴和纵轴：主轴，表示容器依次摆放子Widget的方向；纵轴，则是与主轴垂直的另一个方向。

![2ace8c6585784a5d9b5e4524833f4838](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/2ace8c6585784a5d9b5e4524833f4838.jpg)

图6 Row和Column控件的主轴与纵轴

我们可以根据主轴与纵轴，设置子Widget在这两个方向上的对齐规则mainAxisAlignment与crossAxisAlignment。比如，主轴方向start表示靠左对齐、center表示横向居中对齐、end表示靠右对齐、spaceEvenly表示按固定间距对齐；而纵轴方向start则表示靠上对齐、center表示纵向居中对齐、end表示靠下对齐。

下图展示了在Row中设置不同方向的对齐规则后的呈现效果：

![b39944d437974f92bd88fe4ba849045d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/b39944d437974f92bd88fe4ba849045d.jpg)

图7 Row的主轴对齐方式

![119f7dd74c33492b87faccbe731d7fc8](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/119f7dd74c33492b87faccbe731d7fc8.jpg)

图8 Row的纵轴对齐方式

Column的对齐方式也是类似的，我就不再过多展开了。

这里需要注意的是，对于主轴而言，Flutter默认是让父容器决定其长度，即尽可能大，类似Android中的match_parent。

在上面的例子中，Row的宽度为屏幕宽度，Column的高度为屏幕高度。主轴长度大于所有子Widget的总长度，意味着容器在主轴方向的空间比子Widget要大，这也是我们能通过主轴对齐方式设置子Widget布局效果的原因。

如果想让容器与子Widget在主轴上完全匹配，我们可以通过设置Row的mainAxisSize参数为MainAxisSize.min，由所有子Widget来决定主轴方向的容器长度，即主轴方向的长度尽可能小，类似Android中的wrap_content：

```
Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly, //由于容器与子Widget一样宽，因此这行设置排列间距的代码并未起作用
  mainAxisSize: MainAxisSize.min, //让容器宽度与所有子Widget的宽度一致
  children: <Widget>[
    Container(color: Colors.yellow, width: 60, height: 80,),
    Container(color: Colors.red, width: 100, height: 180,),
    Container(color: Colors.black, width: 60, height: 80,),
    Container(color: Colors.green, width: 60, height: 80,),
  ],
)
```

![fe4934b45fde49fda3bdb3ef8af5a4f0](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/fe4934b45fde49fda3bdb3ef8af5a4f0.jpg)

图9 Row 的主轴大小

可以看到，我们设置了主轴大小为MainAxisSize.min之后，Row的宽度变得和其子Widget一样大，因此再设置主轴的对齐方式也就不起作用了。

#### 层叠Widget布局：Stack与Positioned

有些时候，我们需要让一个控件叠加在另一个控件的上面，比如在一张图片上放置一段文字，又或者是在图片的某个区域放置一个按钮。这时候，我们就需要用到层叠布局容器Stack了。

Stack容器与前端中的绝对定位、Android中的Frame布局非常类似，子Widget之间允许叠加，还可以根据父容器上、下、左、右四个角的位置来确定自己的位置。

**Stack提供了层叠布局的容器，而Positioned则提供了设置子Widget位置的能力**。接下来，我们就通过一个例子来看一下Stack和Positioned的具体用法吧。

在这个例子中，我先在Stack中放置了一块300_300的黄色画布，随后在(18,18)处放置了一个50_50的绿色控件，然后在(18,70)处放置了一个文本控件。

```
Stack(
  children: <Widget>[
    Container(color: Colors.yellow, width: 300, height: 300),//黄色容器
    Positioned(
      left: 18.0,
      top: 18.0,
      child: Container(color: Colors.green, width: 50, height: 50),//叠加在黄色容器之上的绿色控件
    ),
    Positioned(
      left: 18.0,
      top:70.0,
      child: Text("Stack提供了层叠布局的容器"),//叠加在黄色容器之上的文本
    )
  ],
)
```

试着运行一下，可以看到，这三个子Widget都按照我们预定的规则叠加在一起了。

![be60af61f4c246a196227e3d8ec2d6a3](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/be60af61f4c246a196227e3d8ec2d6a3.jpg)

图10 Stack与Positioned容器示例

Stack控件允许其子Widget按照创建的先后顺序进行层叠摆放，而Positioned控件则用来控制这些子Widget的摆放位置。需要注意的是，Positioned控件只能在Stack中使用，在其他容器中使用会报错。

#### 总结

Flutter的布局容器强大而丰富，可以将小型、单用途的基本视觉元素快速封装成控件。今天我选取了Flutter中最具代表性，也最常用的几类布局Widget，与你介绍了构建一个界面精美的App所需要的布局概念。

接下来，我们简单回顾一下今天的内容，以便加深理解与记忆：

首先，我们认识了单子容器Container、Padding与Center。其中，Container内部提供了间距、背景样式等基础属性，为子Widget的摆放方式，及展现样式都提供了定制能力。而Padding与Center提供的功能，则正如其名一样简洁，就是对齐与居中。

然后，我们深入学习了多子Widget布局中的Row和Column，各子Widget间对齐的规则，以及容器自身扩充的规则，以及如何通过Expanded控件使用容器内部的剩余空间，

最后，我们学习了层叠布局Stack，以及与之搭配使用的，定位子Widget位置的Positioned容器，你可以通过它们，实现多个控件堆放的布局效果。

通过今天的文章，相信你已经对如何搭建App的界面有了足够的知识储备，所以在下一篇文章中，我会通过一些实际的例子，带你认识在Flutter中，如何通过这些基本控件与布局规则，实现好看的界面。

#### 思考题

最后，我给你留下一道思考题吧。

Row与Column自身的大小是如何决定的？当它们嵌套时，又会出现怎样的情况呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 组合与自绘，我该选用何种方式自定义Widget？

你好，我是陈航。

在上一次分享中，我们认识了Flutter中最常用也最经典的布局Widget，即单子容器Container、多子容器Row/Column，以及层叠容器Stack与Positioned，也学习了这些不同容器之间的摆放子Widget的布局规则，我们可以通过它们，来实现子控件的对齐、嵌套、层叠等，它们也是构建一个界面精美的App所必须的布局概念。

在实际开发中，我们会经常遇到一些复杂的UI需求，往往无法通过使用Flutter的基本Widget，通过设置其属性参数来满足。这个时候，我们就需要针对特定的场景自定义Widget了。

在Flutter中，自定义Widget与其他平台类似：可以使用基本Widget组装成一个高级别的Widget，也可以自己在画板上根据特殊需求来画界面。

接下来，我会分别与你介绍组合和自绘这两种自定义Widget的方式。

#### 组装

使用组合的方式自定义Widget，即通过我们之前介绍的布局方式，摆放项目所需要的基础Widget，并在控件内部设置这些基础Widget的样式，从而组合成一个更高级的控件。

这种方式，对外暴露的接口比较少，减少了上层使用成本，但也因此增强了控件的复用性。在Flutter中，**组合的思想始终贯穿在框架设计之中**，这也是Flutter提供了如此丰富的控件库的原因之一。

比如，在新闻类应用中，我们经常需要将新闻Icon、标题、简介与日期组合成一个单独的控件，作为一个整体去响应用户的点击事件。面对这类需求，我们可以把现有的Image、Text及各类布局，组合成一个更高级的新闻Item控件，对外暴露设置model和点击回调的属性即可。

接下来，我通过一个例子为你说明如何通过组装去自定义控件。

下图是App Store的升级项UI示意图，图里的每一项，都有应用Icon、名称、更新日期、更新简介、应用版本、应用大小以及更新/打开按钮。可以看到，这里面的UI元素还是相对较多的，现在我们希望将升级项UI封装成一个单独的控件，节省使用成本，以及后续的维护成本。

![017827ec5e1f48d687e192f578738f9e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/017827ec5e1f48d687e192f578738f9e.jpg)

图1 App Store 升级项UI

在分析这个升级项UI的整体结构之前，我们先定义一个数据结构UpdateItemModel来存储升级信息。在这里为了方便讨论，我把所有的属性都定义为了字符串类型，你在实际使用中可以根据需要将属性定义得更规范（比如，将appDate定义为DateTime类型）。

```
class UpdateItemModel {
  String appIcon;//App图标
  String appName;//App名称
  String appSize;//App大小
  String appDate;//App更新日期
  String appDescription;//App更新文案
  String appVersion;//App版本
  //构造函数语法糖，为属性赋值
  UpdateItemModel({this.appIcon, this.appName, this.appSize, this.appDate, this.appDescription, this.appVersion});
}
```

接下来，我以Google Map为例，和你一起分析下这个升级项UI的整体结构。

按照子Widget的摆放方向，布局方式只有水平和垂直两种，因此我们也按照这两个维度对UI结构进行拆解。

按垂直方向，我们用绿色的框把这个UI拆解为上半部分与下半部分，如图2所示。下半部分比较简单，是两个文本控件的组合；上半部分稍微复杂一点，我们先将其包装为一个水平布局的Row控件。

接下来，我们再一起看看水平方向应该如何布局。

![d6cdaf56f2454b028575592941f53df9](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d6cdaf56f2454b028575592941f53df9.jpg)

图2 升级项UI整体结构示意图

我们先把升级项的上半部分拆解成对应的UI元素：

- 左边的应用图标拆解为Image；
- 右边的按钮拆解为FlatButton；
- 中间部分是两个文本在垂直方向上的组合，因此拆解为Column，Column内部则是两个Text。

拆解示意图，如下所示：

![8403e44c2d3b4b348be2295645a2b092](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/8403e44c2d3b4b348be2295645a2b092.jpg)

图3 上半部分UI结构示意图

通过与拆解前的UI对比，你就会发现还有3个问题待解决：即控件间的边距如何设置、中间部分的伸缩（截断）规则又是怎样、图片圆角怎么实现。接下来，我们分别来看看。

Image、FlatButton，以及Column这三个控件，与父容器Row之间存在一定的间距，因此我们还需要在最左边的Image与最右边的FlatButton上包装一层Padding，用以留白填充。

另一方面，考虑到需要适配不同尺寸的屏幕，中间部分的两个文本应该是变长可伸缩的，但也不能无限制地伸缩，太长了还是需要截断的，否则就会挤压到右边按钮的固定空间了。

因此，我们需要在Column的外层用Expanded控件再包装一层，让Image与FlatButton之间的空间全留给Column。不过，通常情况下这两个文本并不能完全填满中间的空间，因此我们还需要设置对齐格式，按照垂直方向上居中，水平方向上居左的方式排列。

最后一项需要注意的是，升级项UI的App Icon是圆角的，但普通的Image并不支持圆角。这时，我们可以使用ClipRRect控件来解决这个问题。ClipRRect可以将其子Widget按照圆角矩形的规则进行裁剪，所以用ClipRRect将Image包装起来，就可以实现图片圆角的功能了。

下面的代码，就是控件上半部分的关键代码：

```
Widget buildTopRow(BuildContext context) {
  return Row(//Row控件，用来水平摆放子Widget
    children: <Widget>[
      Padding(//Paddng控件，用来设置Image控件边距
        padding: EdgeInsets.all(10),//上下左右边距均为10
        child: ClipRRect(//圆角矩形裁剪控件
          borderRadius: BorderRadius.circular(8.0),//圆角半径为8
          child: Image.asset(model.appIcon, width: 80,height:80)图片控件//
        )
      ),
      Expanded(//Expanded控件，用来拉伸中间区域
        child: Column(//Column控件，用来垂直摆放子Widget
          mainAxisAlignment: MainAxisAlignment.center,//垂直方向居中对齐
          crossAxisAlignment: CrossAxisAlignment.start,//水平方向居左对齐
          children: <Widget>[
            Text(model.appName,maxLines: 1),//App名字
            Text(model.appDate,maxLines: 1),//App更新日期
          ],
        ),
      ),
      Padding(//Paddng控件，用来设置Widget间边距
        padding: EdgeInsets.fromLTRB(0,0,10,0),//右边距为10，其余均为0
        child: FlatButton(//按钮控件
          child: Text("OPEN"),
          onPressed: onPressed,//点击回调
        )
      )
  ]);
}
```

升级项UI的下半部分比较简单，是两个文本控件的组合。与上半部分的拆解类似，我们用一个Column控件将它俩装起来，如图4所示：

![c53ffd48571b421d9ee4a1ad8cf9bcc5](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c53ffd48571b421d9ee4a1ad8cf9bcc5.jpg)

图4 下半部分UI结构示意图

与上半部分类似，这两个文本与父容器之间存在些间距，因此在Column的最外层还需要用Padding控件给包装起来，设置父容器间距。

另一方面，Column的两个文本控件间也存在间距，因此我们仍然使用Padding控件将下面的文本包装起来，单独设置这两个文本之间的间距。

同样地，通常情况下这两个文本并不能完全填满下部空间，因此我们还需要设置对齐格式，即按照水平方向上居左的方式对齐。

控件下半部分的关键代码如下所示：

```
Widget buildBottomRow(BuildContext context) {
  return Padding(//Padding控件用来设置整体边距
    padding: EdgeInsets.fromLTRB(15,0,15,0),//左边距和右边距为15
    child: Column(//Column控件用来垂直摆放子Widget
      crossAxisAlignment: CrossAxisAlignment.start,//水平方向距左对齐
      children: <Widget>[
        Text(model.appDescription),//更新文案
        Padding(//Padding控件用来设置边距
          padding: EdgeInsets.fromLTRB(0,10,0,0),//上边距为10
          child: Text("${model.appVersion} • ${model.appSize} MB")
        )
      ]
  ));
}
```

最后，我们将上下两部分控件通过Column包装起来，这次升级项UI定制就完成了：

```
class UpdatedItem extends StatelessWidget {
  final UpdatedItemModel model;//数据模型
  //构造函数语法糖，用来给model赋值
  UpdatedItem({Key key,this.model, this.onPressed}) : super(key: key);
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return Column(//用Column将上下两部分合体
        children: <Widget>[
          buildTopRow(context),//上半部分
          buildBottomRow(context)//下半部分
        ]);
  }
  Widget buildBottomRow(BuildContext context) {...}
  Widget buildTopRow(BuildContext context) {...}
}
```

试着运行一下，效果如下所示：

![a4d74f1bbff941d0ba1c2a39513b0d66](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a4d74f1bbff941d0ba1c2a39513b0d66.jpg)

图5 升级项UI运行示例

搞定！

**按照从上到下、从左到右去拆解UI的布局结构，把复杂的UI分解成各个小UI元素，在以组装的方式去自定义UI中非常有用，请一定记住这样的拆解方法。**

#### 自绘

Flutter提供了非常丰富的控件和布局方式，使得我们可以通过组合去构建一个新的视图。但对于一些不规则的视图，用SDK提供的现有Widget组合可能无法实现，比如饼图，k线图等，这个时候我们就需要自己用画笔去绘制了。

在原生iOS和Android开发中，我们可以继承UIView/View，在drawRect/onDraw方法里进行绘制操作。其实，在Flutter中也有类似的方案，那就是CustomPaint。

**CustomPaint是用以承接自绘控件的容器，并不负责真正的绘制**。既然是绘制，那就需要用到画布与画笔。

在Flutter中，画布是Canvas，画笔则是Paint，而画成什么样子，则由定义了绘制逻辑的CustomPainter来控制。将CustomPainter设置给容器CustomPaint的painter属性，我们就完成了一个自绘控件的封装。

对于画笔Paint，我们可以配置它的各种属性，比如颜色、样式、粗细等；而画布Canvas，则提供了各种常见的绘制方法，比如画线drawLine、画矩形drawRect、画点DrawPoint、画路径drawPath、画圆drawCircle、画圆弧drawArc等。

这样，我们就可以在CustomPainter的paint方法里，通过Canvas与Paint的配合，实现定制化的绘制逻辑。

接下来，我们看一个例子。

在下面的代码中，我们继承了CustomPainter，在定义了绘制逻辑的paint方法中，通过Canvas的drawArc方法，用6种不同颜色的画笔依次画了6个1/6圆弧，拼成了一张饼图。最后，我们使用CustomPaint容器，将painter进行封装，就完成了饼图控件Cake的定义。

```
class WheelPainter extends CustomPainter {
 // 设置画笔颜色
  Paint getColoredPaint(Color color) {//根据颜色返回不同的画笔
    Paint paint = Paint();//生成画笔
    paint.color = color;//设置画笔颜色
    return paint;
  }

  @override
  void paint(Canvas canvas, Size size) {//绘制逻辑
    double wheelSize = min(size.width,size.height)/2;//饼图的尺寸
    double nbElem = 6;//分成6份
    double radius = (2 * pi) / nbElem;//1/6圆
    //包裹饼图这个圆形的矩形框
    Rect boundingRect = Rect.fromCircle(center: Offset(wheelSize, wheelSize), radius: wheelSize);
    // 每次画1/6个圆弧
    canvas.drawArc(boundingRect, 0, radius, true, getColoredPaint(Colors.orange));
    canvas.drawArc(boundingRect, radius, radius, true, getColoredPaint(Colors.black38));
    canvas.drawArc(boundingRect, radius * 2, radius, true, getColoredPaint(Colors.green));
    canvas.drawArc(boundingRect, radius * 3, radius, true, getColoredPaint(Colors.red));
    canvas.drawArc(boundingRect, radius * 4, radius, true, getColoredPaint(Colors.blue));
    canvas.drawArc(boundingRect, radius * 5, radius, true, getColoredPaint(Colors.pink));
  }
  // 判断是否需要重绘，这里我们简单的做下比较即可
  @override
  bool shouldRepaint(CustomPainter oldDelegate) => oldDelegate != this;
}
//将饼图包装成一个新的控件
class Cake extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return CustomPaint(
        size: Size(200, 200),
        painter: WheelPainter(),
      );
  }
}
```

试着运行一下，效果如下所示：

![c9ca996544794880aaca34c5f4d6d819](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c9ca996544794880aaca34c5f4d6d819.jpg)

图6 自绘控件示例

可以看到，使用CustomPainter进行自绘控件并不算复杂。这里，我建议你试着用画笔和画布，去实现更丰富的功能。

**在实现视觉需求上，自绘需要自己亲自处理绘制逻辑，而组合则是通过子Widget的拼接来实现绘制意图。**因此从渲染逻辑处理上，自绘方案可以进行深度的渲染定制，从而实现少数通过组合很难实现的需求（比如饼图、k线图）。不过，当视觉效果需要调整时，采用自绘的方案可能需要大量修改绘制代码，而组合方案则相对简单：只要布局拆分设计合理，可以通过更换子Widget类型来轻松搞定。

#### 总结

在面对一些复杂的UI视图时，Flutter提供的单一功能类控件往往不能直接满足我们的需求。于是，我们需要自定义Widget。Flutter提供了组装与自绘两种自定义Widget的方式，来满足我们对视图的自定义需求。

以组装的方式构建UI，我们需要将目标视图分解成各个UI小元素。通常，我们可以按照从上到下、从左到右的布局顺序去对控件层次结构进行拆解，将基本视觉元素封装到Column、Row中。对于有着固定间距的视觉元素，我们可以通过Padding对其进行包装，而对于大小伸缩可变的视觉元素，我们可以通过Expanded控件让其填充父容器的空白区域。

而以自绘的方式定义控件，则需要借助于CustomPaint容器，以及最终承接真实绘制逻辑的CustomPainter。CustomPainter是绘制逻辑的封装，在其paint方法中，我们可以使用不同类型的画笔Paint，利用画布Canvas提供的不同类型的绘制图形能力，实现控件自定义绘制。

无论是组合还是自绘，在自定义UI时，有了目标视图整体印象后，我们首先需要考虑的事情应该是如何将它化繁为简，把视觉元素拆解细分，变成自己立即可以着手去实现的一个小控件，然后再思考如何将这些小控件串联起来。把大问题拆成小问题后，实现目标也逐渐清晰，落地方案就自然浮出水面了。

这其实就和我们学习新知识的过程是一样的，在对整体知识概念有了初步认知之后，也需要具备将复杂的知识化繁为简的能力：先理清楚其逻辑脉络，然后再把不懂的知识拆成小点，最后逐个攻破。

我把今天分享讲的两个例子放到了[GitHub](https://github.com/cyndibaby905/15_custom_ui_demo)上，你可以下载后在工程中实际运行，并对照着今天的知识点进行学习，体会在不同场景下，组合和自绘这两种自定义Widget的具体使用方法。

#### 思考题

最后，我给你留下两道作业题吧。

- 请扩展UpdatedItem控件，使其能自动折叠过长的更新文案，并能支持点击后展开的功能。

![3ce5adcab7a4436da82c347e23fdfcf9](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/3ce5adcab7a4436da82c347e23fdfcf9.jpg)

- 请扩展Cake控件，使其能够根据传入的double数组（最多10个元素）中数值的大小，定义饼图的圆弧大小。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 从夜间模式说起，如何定制不同风格的App主题？

你好，我是陈航。今天，我和你分享的主题是，从夜间模式说起，如何定制不同风格的App主题。

在上一篇文章中，我与你介绍了组装与自绘这两种自定义Widget的方式。对于组装，我们按照从上到下、从左到右的布局顺序去分解目标视图，将基本的Widget封装到Column、Row中，从而合成更高级别的Widget；而对于自绘，我们则通过承载绘制逻辑的载体CustomPainter，在其paint方法中使用画笔Paint与画布Canvas，绘制不同风格、不同类型的图形，从而实现基于自绘的自定义组件。

对于一个产品来说，在业务早期其实更多的是处理基本功能有和无的问题：工程师来负责实现功能，PM负责功能好用不好用。在产品的基本功能已经完善，做到了六七十分的时候，再往上的如何做增长就需要运营来介入了。

在这其中，如何通过用户分层去实现App的个性化是常见的增长运营手段，而主题样式更换则是实现个性化中的一项重要技术手段。

比如，微博、UC浏览器和电子书客户端都提供了对夜间模式的支持，而淘宝、京东这样的电商类应用，还会在特定的电商活动日自动更新主题样式，就连现在的手机操作系统也提供了系统级切换展示样式的能力。

那么，这些在应用内切换样式的功能是如何实现的呢？在Flutter中，在普通的应用上增加切换主题的功能又要做哪些事情呢？这些问题，我都会在今天的这篇文章中与你详细分享。

#### 主题定制

主题，又叫皮肤、配色，一般由颜色、图片、字号、字体等组成，我们可以把它看做是视觉效果在不同场景下的可视资源，以及相应的配置集合。比如，App的按钮，无论在什么场景下都需要背景图片资源、字体颜色、字号大小等，而所谓的主题切换只是在不同主题之间更新这些资源及配置集合而已。

因此在App开发中，我们通常不关心资源和配置的视觉效果好不好看，只要关心资源提供的视觉功能能不能用。比如，对于图片类资源，我们并不需要关心它渲染出来的实际效果，只需要确定它渲染出来是一张固定宽高尺寸的区域，不影响页面布局，能把业务流程跑通即可。

**视觉效果是易变的，我们将这些变化的部分抽离出来，把提供不同视觉效果的资源和配置按照主题进行归类，整合到一个统一的中间层去管理，这样我们就能实现主题的管理和切换了。**

在iOS中，我们通常会将主题的配置信息预先写到plist文件中，通过一个单例来控制App应该使用哪种配置；而Android的配置信息则写入各个style属性值的xml中，通过activity的setTheme进行切换；前端的处理方式也类似，简单更换css就可以实现多套主题/配色之间的切换。

Flutter也提供了类似的能力，**由ThemeData来统一管理主题的配置信息**。

ThemeData涵盖了Material Design规范的可自定义部分样式，比如应用明暗模式brightness、应用主色调primaryColor、应用次级色调accentColor、文本字体fontFamily、输入框光标颜色cursorColor等。如果你想深入了解ThemeData的其他API参数，可以参考官方文档[ThemeData](https://api.flutter.dev/flutter/material/ThemeData/ThemeData.html)。

通过ThemeData来自定义应用主题，我们可以实现App全局范围，或是Widget局部范围的样式切换。接下来，我便分别与你讲述这两种范围的主题切换。

#### 全局统一的视觉风格定制

在Flutter中，应用程序类MaterialApp的初始化方法，为我们提供了设置主题的能力。我们可以通过参数theme，选择改变App的主题色、字体等，设置界面在MaterialApp下的展示样式。

以下代码演示了如何设置App全局范围主题。在这段代码中，我们设置了App的明暗模式brightness为暗色、主色调为青色：

```
MaterialApp(
  title: 'Flutter Demo',//标题
  theme: ThemeData(//设置主题
      brightness: Brightness.dark,//明暗模式为暗色
      primaryColor: Colors.cyan,//主色调为青色
  ),
  home: MyHomePage(title: 'Flutter Demo Home Page'),
);
```

试着运行一下，效果如下：

![7cf026a9a87048b8bb14f4f7c1e3adcf](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/7cf026a9a87048b8bb14f4f7c1e3adcf.jpg)

图1 Flutter全局模式主题

可以看到，虽然我们只修改了主色调和明暗模式两个参数，但按钮、文字颜色都随之调整了。这是因为默认情况下，**ThemeData中很多其他次级视觉属性，都会受到主色调与明暗模式的影响**。如果我们想要精确控制它们的展示样式，需要再细化一下主题配置。

下面的例子中，我们将icon的颜色调整为黄色，文字颜色调整为红色，按钮颜色调整为黑色：

```
MaterialApp(
  title: 'Flutter Demo',//标题
  theme: ThemeData(//设置主题
      brightness: Brightness.dark,//设置明暗模式为暗色
      accentColor: Colors.black,//(按钮）Widget前景色为黑色
      primaryColor: Colors.cyan,//主色调为青色
      iconTheme:IconThemeData(color: Colors.yellow),//设置icon主题色为黄色
      textTheme: TextTheme(body1: TextStyle(color: Colors.red))//设置文本颜色为红色
  ),
  home: MyHomePage(title: 'Flutter Demo Home Page'),
);
```

运行一下，可以看到图标、文字、按钮的颜色都随之更改了。

![98b33bc3ed834cc08b587c23043eb002](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/98b33bc3ed834cc08b587c23043eb002.jpg)

图2 Flutter全局模式主题示例2

#### 局部独立的视觉风格定制

为整个App提供统一的视觉呈现效果固然很有必要，但有时我们希望为某个页面、或是某个区块设置不同于App风格的展现样式。以主题切换功能为例，我们希望为不同的主题提供不同的展示预览。

在Flutter中，我们可以使用Theme来对App的主题进行局部覆盖。Theme是一个单子Widget容器，与MaterialApp类似的，我们可以通过设置其data属性，对其子Widget进行样式定制：

- 如果我们不想继承任何App全局的颜色或字体样式，可以直接新建一个ThemeData实例，依次设置对应的样式；
- 而如果我们不想在局部重写所有的样式，则可以继承App的主题，使用copyWith方法，只更新部分样式。

下面的代码演示了这两种方式的用法：

```
// 新建主题
Theme(
    data: ThemeData(iconTheme: IconThemeData(color: Colors.red)),
    child: Icon(Icons.favorite)
);

// 继承主题
Theme(
    data: Theme.of(context).copyWith(iconTheme: IconThemeData(color: Colors.green)),
    child: Icon(Icons.feedback)
);
```

![13243e2a1ff947e19b2bd8bd05f0c3e3](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/13243e2a1ff947e19b2bd8bd05f0c3e3.jpg)

图3 Theme局部主题更改示例

对于上述例子而言，由于Theme的子Widget只有一个Icon组件，因此这两种方式都可以实现覆盖全局主题，从而更改Icon样式的需求。而像这样使用局部主题覆盖全局主题的方式，在Flutter中是一种常见的自定义子Widget展示样式的方法。

**除了定义Material Design规范中那些可自定义部分样式外，主题的另一个重要用途是样式复用。**

比如，如果我们想为一段文字复用Materia Design规范中的title样式，或是为某个子Widget的背景色复用App的主题色，我们就可以通过Theme.of(context)方法，取出对应的属性，应用到这段文字的样式中。

Theme.of(context)方法将向上查找Widget树，并返回Widget树中最近的主题Theme。如果Widget的父Widget们有一个单独的主题定义，则使用该主题。如果不是，那就使用App全局主题。

在下面的例子中，我们创建了一个包装了一个Text组件的Container容器。在Text组件的样式定义中，我们复用了全局的title样式，而在Container的背景色定义中，则复用了App的主题色：

```
Container(
    color: Theme.of(context).primaryColor,//容器背景色复用应用主题色
    child: Text(
      'Text with a background color',
      style: Theme.of(context).textTheme.title,//Text组件文本样式复用应用文本样式
    ));
```

![34cfb7275a494bc88ddd694b4c939968](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/34cfb7275a494bc88ddd694b4c939968.jpg)

图4 主题复用示例

#### 分平台主题定制

有时候，**为了满足不同平台的用户需求，我们希望针对特定的平台设置不同的样式**。比如，在iOS平台上设置浅色主题，在Android平台上设置深色主题。面对这样的需求，我们可以根据defaultTargetPlatform来判断当前应用所运行的平台，从而根据系统类型来设置对应的主题。

在下面的例子中，我们为iOS与Android分别创建了两个主题。在MaterialApp的初始化方法中，我们根据平台类型，设置了不同的主题：

```
// iOS浅色主题
final ThemeData kIOSTheme = ThemeData(
    brightness: Brightness.light,//亮色主题
    accentColor: Colors.white,//(按钮)Widget前景色为白色
    primaryColor: Colors.blue,//主题色为蓝色
    iconTheme:IconThemeData(color: Colors.grey),//icon主题为灰色
    textTheme: TextTheme(body1: TextStyle(color: Colors.black))//文本主题为黑色
);
// Android深色主题
final ThemeData kAndroidTheme = ThemeData(
    brightness: Brightness.dark,//深色主题
    accentColor: Colors.black,//(按钮)Widget前景色为黑色
    primaryColor: Colors.cyan,//主题色Wie青色
    iconTheme:IconThemeData(color: Colors.blue),//icon主题色为蓝色
    textTheme: TextTheme(body1: TextStyle(color: Colors.red))//文本主题色为红色
);
// 应用初始化
MaterialApp(
  title: 'Flutter Demo',
  theme: defaultTargetPlatform == TargetPlatform.iOS ? kIOSTheme : kAndroidTheme,//根据平台选择不同主题
  home: MyHomePage(title: 'Flutter Demo Home Page'),
);
```

试着运行一下：

![b2cc50e3d9b34bd690ae7493d0f15591](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/b2cc50e3d9b34bd690ae7493d0f15591.jpg)

（a）iOS平台

![9d995688e1d042bb8f47203be5d90b6d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/9d995688e1d042bb8f47203be5d90b6d.jpg)

（b）Android平台

图5 根据不同平台设置对应主题

当然，除了主题之外，你也可以用defaultTargetPlatform这个变量去实现一些其他需要判断平台的逻辑，比如在界面上使用更符合Android或iOS设计风格的组件。

#### 总结

好了，今天的分享就到这里。我们简单回顾一下今天的主要内容吧。

主题设置属于App开发的高级特性，归根结底其实是提供了一种视觉资源与视觉配置的管理机制。与其他平台类似，Flutter也提供了集中式管理主题的机制，可以在遵循Material Design规范的ThemeData中，定义那些可定制化的样式。

我们既可以通过设置MaterialApp全局主题实现应用整体视觉风格的统一，也可以通过Theme单子Widget容器使用局部主题覆盖全局主题，实现局部独立的视觉风格。

除此之外，在自定义组件过程中，我们还可以使用Theme.of方法取出主题对应的属性值，从而实现多种组件在视觉风格上的复用。

最后，面对常见的分平台设置主题场景，我们可以根据defaultTargetPlatform，来精确识别当前应用所处的系统，从而配置对应的主题。

#### 思考题

最后，我给你留下一个课后小作业吧。

在上一篇文章中，我与你介绍了如何实现App Store升级项UI自定义组件布局。现在，请在这个自定义Widget的基础上，增加切换夜间模式的功能。

![49054e8bb8594b86a13e4962bb3177bf](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/49054e8bb8594b86a13e4962bb3177bf.jpg)

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 依赖管理（一）：图片、配置和字体在Flutter中怎么用？

你好，我是陈航。

在上一篇文章中，我与你介绍了Flutter的主题设置，也就是将视觉资源与视觉配置进行集中管理的机制。

Flutter提供了遵循Material Design规范的ThemeData，可以对样式进行定制化：既可以初始化App时实现全局整体视觉风格统一，也可以在使用单子Widget容器Theme实现局部主题的覆盖，还可以在自定义组件时取出主题对应的属性值，实现视觉风格的复用。

一个应用程序主要由两部分内容组成：代码和资源。代码关注逻辑功能，而如图片、字符串、字体、配置文件等资源则关注视觉功能。如果说上一次文章更多的是从逻辑层面分享应该如何管理资源的配置，那今天的分享则会从物理存储入手与你介绍Flutter整体的资源管理机制。

资源外部化，即把代码与资源分离，是现代UI框架的主流设计理念。因为这样不仅有利于单独维护资源，还可以对特定设备提供更准确的兼容性支持，使得我们的应用程序可以自动根据实际运行环境来组织视觉功能，适应不同的屏幕大小和密度等。

随着各类配置各异的终端设备越来越多，资源管理也越来越重要。那么今天，我们就先看看Flutter中的图片、配置和字体的管理机制吧。

#### 资源管理

在移动开发中，常见的资源类型包括JSON文件、配置文件、图标、图片以及字体文件等。它们都会被打包到App安装包中，而App中的代码可以在运行时访问这些资源。

在Android、iOS平台中，为了区分不同分辨率的手机设备，图片和其他原始资源是区别对待的：

- iOS使用Images.xcassets来管理图片，其他的资源直接拖进工程项目即可；
- Android的资源管理粒度则更为细致，使用以drawable+分辨率命名的文件夹来分别存放不同分辨率的图片，其他类型的资源也都有各自的存放方式，比如布局文件放在res/layout目录下，资源描述文件放在res/values目录下，原始文件放在assets目录下等。

而在Flutter中，资源管理则简单得多：资源（assets）可以是任意类型的文件，比如JSON配置文件或是字体文件等，而不仅仅是图片。

而关于资源的存放位置，Flutter并没有像Android那样预先定义资源的目录结构，所以我们可以把资源存放在项目中的任意目录下，只需要使用根目录下的pubspec.yaml文件，对这些资源的所在位置进行显式声明就可以了，以帮助Flutter识别出这些资源。

而在指定路径名的过程中，我们既可以对每一个文件进行挨个指定，也可以采用子目录批量指定的方式。

接下来，**我以一个示例和你说明挨个指定和批量指定这两种方式的区别。**

如下所示，我们将资源放入assets目录下，其中，两张图片background.jpg、loading.gif与JSON文件result.json在assets根目录，而另一张图片food_icon.jpg则在assets的子目录icons下。

```
assets
├── background.jpg
├── icons
│   └── food_icon.jpg
├── loading.gif
└── result.json
```

对于上述资源文件存放的目录结构，以下代码分别演示了挨个指定和子目录批量指定这两种方式：通过单个文件声明的，我们需要完整展开资源的相对路径；而对于目录批量指定的方式，只需要在目录名后加路径分隔符就可以了：

```
flutter:
  assets:
    - assets/background.jpg   #挨个指定资源路径
    - assets/loading.gif  #挨个指定资源路径
    - assets/result.json  #挨个指定资源路径
    - assets/icons/    #子目录批量指定
    - assets/ #根目录也是可以批量指定的
```

需要注意的是，**目录批量指定并不递归，只有在该目录下的文件才可以被包括，如果下面还有子目录的话，需要单独声明子目录下的文件。**

完成资源的声明后，我们就可以在代码中访问它们了。**在Flutter中，对不同类型的资源文件处理方式略有差异**，接下来我将分别与你介绍。

对于图片类资源的访问，我们可以使用Image.asset构造方法完成图片资源的加载及显示，在第12篇文章“[经典控件（一）：文本、图片和按钮在Flutter中怎么用？](https://time.geekbang.org/column/article/110292)”中，你应该已经了解了具体的用法，这里我就不再赘述了。

而对于其他资源文件的加载，我们可以通过Flutter应用的主资源Bundle对象rootBundle，来直接访问。

对于字符串文件资源，我们使用loadString方法；而对于二进制文件资源，则通过load方法。

以下代码演示了获取result.json文件，并将其打印的过程：

```
rootBundle.loadString('assets/result.json').then((msg)=>print(msg));
```

与Android、iOS开发类似，**Flutter也遵循了基于像素密度的管理方式**，如1.0x、2.0x、3.0x或其他任意倍数，Flutter可以根据当前设备分辨率加载最接近设备像素比例的图片资源。而为了让Flutter更好地识别，我们的资源目录应该将1.0x、2.0x与3.0x的图片资源分开管理。

以background.jpg图片为例，这张图片位于assets目录下。如果想让Flutter适配不同的分辨率，我们需要将其他分辨率的图片放到对应的分辨率子目录中，如下所示：

```
assets
├── background.jpg    //1.0x图
├── 2.0x
│   └── background.jpg  //2.0x图
└── 3.0x
    └── background.jpg  //3.0x图
```

而在pubspec.yaml文件声明这个图片资源时，仅声明1.0x图资源即可：

```
flutter:
  assets:
    - assets/background.jpg   #1.0x图资源
```

1.0x分辨率的图片是资源标识符，而Flutter则会根据实际屏幕像素比例加载相应分辨率的图片。这时，如果主资源缺少某个分辨率资源，Flutter会在剩余的分辨率资源中选择最接近的分辨率资源去加载。

举个例子，如果我们的App包只包括了2.0x资源，对于屏幕像素比为3.0的设备，则会自动降级读取2.0x的资源。不过需要注意的是，即使我们的App包没有包含1.0x资源，我们仍然需要像上面那样在pubspec.yaml中将它显示地声明出来，因为它是资源的标识符。

**字体则是另外一类较为常用的资源**。手机操作系统一般只有默认的几种字体，在大部分情况下可以满足我们的正常需求。但是，在一些特殊的情况下，我们可能需要使用自定义字体来提升视觉体验。

在Flutter中，使用自定义字体同样需要在pubspec.yaml文件中提前声明。需要注意的是，字体实际上是字符图形的映射。所以，除了正常字体文件外，如果你的应用需要支持粗体和斜体，同样也需要有对应的粗体和斜体字体文件。

在将RobotoCondensed字体摆放至assets目录下的fonts子目录后，下面的代码演示了如何将支持斜体与粗体的RobotoCondensed字体加到我们的应用中：

```
fonts:
  - family: RobotoCondensed  #字体名字
    fonts:
      - asset: assets/fonts/RobotoCondensed-Regular.ttf #普通字体
      - asset: assets/fonts/RobotoCondensed-Italic.ttf
        style: italic  #斜体
      - asset: assets/fonts/RobotoCondensed-Bold.ttf
        weight: 700  #粗体
```

这些声明其实都对应着TextStyle中的样式属性，如字体名family对应着 fontFamily属性、斜体italic与正常normal对应着style属性、字体粗细weight对应着fontWeight属性等。在使用时，我们只需要在TextStyle中指定对应的字体即可：

```
Text("This is RobotoCondensed", style: TextStyle(
    fontFamily: 'RobotoCondensed',//普通字体
));
Text("This is RobotoCondensed", style: TextStyle(
    fontFamily: 'RobotoCondensed',
    fontWeight: FontWeight.w700, //粗体
));
Text("This is RobotoCondensed italic", style: TextStyle(
  fontFamily: 'RobotoCondensed',
  fontStyle: FontStyle.italic, //斜体
));
```

![3f82554ffe9f419f85d20ac7ecc48268](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/3f82554ffe9f419f85d20ac7ecc48268.jpg)

图1 自定义字体

#### 原生平台的资源设置

在前面的第5篇文章“[从标准模板入手，体会Flutter代码是如何运行在原生系统上的](https://time.geekbang.org/column/article/106199)”中，我与你介绍了Flutter应用，实际上最终会以原生工程的方式打包运行在Android和iOS平台上，因此Flutter启动时依赖的是原生Android和iOS的运行环境。

上面介绍的资源管理机制其实都是在Flutter应用内的，而在Flutter框架运行之前，我们是没有办法访问这些资源的。Flutter需要原生环境才能运行，但是有些资源我们需要在Flutter框架运行之前提前使用，比如要给应用添加图标，或是希望在等待Flutter框架启动时添加启动图，我们就需要在对应的原生工程中完成相应的配置，所以**下面介绍的操作步骤都是在原生系统中完成的。**

我们先看一下**如何更换App启动图标**。

对于Android平台，启动图标位于根目录android/app/src/main/res/mipmap下。我们只需要遵守对应的像素密度标准，保留原始图标名称，将图标更换为目标资源即可：

![405c7e3ff1e149eeb92716828f758f1a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/405c7e3ff1e149eeb92716828f758f1a.jpg)

图2 更换Android启动图标

对于iOS平台，启动图位于根目录ios/Runner/Assets.xcassets/AppIcon.appiconset下。同样地，我们只需要遵守对应的像素密度标准，将其替换为目标资源并保留原始图标名称即可：

![6cfca39dd4a24718b784d3cb0345188c](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/6cfca39dd4a24718b784d3cb0345188c.jpg)

图3 更换iOS启动图标

然后。我们来看一下**如何更换启动图**。

对于Android平台，启动图位于根目录android/app/src/main/res/drawable下，是一个名为launch_background的XML界面描述文件。

![1cbb284705e148dd81adfbded34d11b3](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/1cbb284705e148dd81adfbded34d11b3.jpg)

图4 修改Android启动图描述文件

我们可以在这个界面描述文件中自定义启动界面，也可以换一张启动图片。在下面的例子中，我们更换了一张居中显示的启动图片：

```
<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- 白色背景 -->
    <item android:drawable="@android:color/white" />
    <item>
         <!-- 内嵌一张居中展示的图片 -->
        <bitmap
            android:gravity="center"
            android:src="@mipmap/bitmap_launcher" />
    </item>
</layer-list>
```

而对于iOS平台，启动图位于根目录ios/Runner/Assets.xcassets/LaunchImage.imageset下。我们保留原始启动图名称，将图片依次按照对应像素密度标准，更换为目标启动图即可。

![4e7c10fd5e404abab112bc66c4ea5d86](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4e7c10fd5e404abab112bc66c4ea5d86.jpg)

图5 更换iOS启动图

#### 总结

好了，今天的分享就到这里。我们简单回顾一下今天的内容。

将代码与资源分离，不仅有助于单独维护资源，还可以更精确地对特定设备提供兼容性支持。在Flutter中，资源可以是任意类型的文件，可以被放到任意目录下，但需要通过pubspec.yaml文件将它们的路径进行统一地显式声明。

Flutter对图片提供了基于像素密度的管理方式，我们需要将1.0x，2.0x与3.0x的资源分开管理，但只需要在pubspec.yaml中声明一次。如果应用中缺少对于高像素密度设备的资源支持，Flutter会进行自动降级。

对于字体这种基于字符图形映射的资源文件，Flutter提供了精细的管理机制，可以支持除了正常字体外，还支持粗体、斜体等样式。

最后，由于Flutter启动时依赖原生系统运行环境，因此我们还需要去原生工程中，设置相应的App启动图标和启动图。

#### 思考题

最后，我给你留下两道思考题吧。

1. 如果我们只提供了1.0x与2.0x的资源图片，对于像素密度为3.0的设备，Flutter会自动降级到哪套资源？
2. 如果我们只提供了2.0x的资源图片，对于像素密度为1.0的设备，Flutter会如何处理呢？

你可以参考原生平台的经验，在模拟器或真机上实验一下。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 依赖管理（二）：第三方组件库在Flutter中要如何管理？

你好，我是陈航。

在上一篇文章中，我与你介绍了Flutter工程的资源管理机制。在Flutter中，资源采用先声明后使用的机制，在pubspec.yaml显式地声明资源路径后，才可以使用。

对于图片，Flutter基于像素密度，设立不同分辨率的目录分开管理，但只需要在pubspec.yaml声明一次；而字体则基于样式支持，除了正常字体，还可以支持粗体、斜体等样式。最后，由于Flutter需要原生运行环境，因此对于在其启动之前所需的启动图和图标这两类特殊资源，我们还需要分别去原生工程中进行相应的设置。

其实，除了管理这些资源外，pubspec.yaml更为重要的作用是管理Flutter工程代码的依赖，比如第三方库、Dart运行环境、Flutter SDK版本都可以通过它来进行统一管理。所以，pubspec.yaml与iOS中的Podfile、Android中的build.gradle、前端的package.json在功能上是类似的。

那么，今天这篇文章，我就主要与你分享，在Flutter中如何通过配置文件来管理工程代码依赖。

#### Pub

Dart提供了包管理工具Pub，用来管理代码和资源。从本质上说，包（package）实际上就是一个包含了pubspec.yaml文件的目录，其内部可以包含代码、资源、脚本、测试和文档等文件。包中包含了需要被外部依赖的功能抽象，也可以依赖其他包。

与Android中的JCenter/Maven、iOS中的CocoaPods、前端中的npm库类似，Dart提供了官方的包仓库Pub。通过Pub，我们可以很方便地查找到有用的第三方包。

当然，这并不意味着我们可以简单地拿别人的库来拼凑成一个应用程序。**Dart提供包管理工具Pub的真正目的是，让你能够找到真正好用的、经过线上大量验证的库，复用他人的成果来缩短开发周期，提升软件质量。**

在Dart中，库和应用都属于包。pubspec.yaml是包的配置文件，包含了包的元数据（比如，包的名称和版本）、运行环境（也就是Dart SDK与Fluter SDK版本）、外部依赖、内部配置（比如，资源管理）。

在下面的例子中，我们声明了一个flutter_app_example的应用配置文件，其版本为1.0，Dart运行环境支持2.1至3.0之间，依赖flutter和cupertino_icon：

```
name: flutter_app_example #应用名称
description: A new Flutter application. #应用描述
version: 1.0.0
#Dart运行环境区间
environment:
  sdk: ">=2.1.0 <3.0.0"
#Flutter依赖库
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ">0.1.1"
```

运行环境和依赖库cupertino_icons冒号后面的部分是版本约束信息，由一组空格分隔的版本描述组成，可以支持指定版本、版本号区间，以及任意版本这三种版本约束方式。比如上面的例子中，cupertino_icons引用了大于0.1.1的版本。

需要注意的是，由于元数据与名称使用空格分隔，因此版本号中不能出现空格；同时又由于大于符号“>”也是YAML语法中的折叠换行符号，因此在指定版本范围的时候，必须使用引号， 比如”>=2.1.0 < 3.0.0”。

**对于包，我们通常是指定版本区间，而很少直接指定特定版本**，因为包升级变化很频繁，如果有其他的包直接或间接依赖这个包的其他版本时，就会经常发生冲突。

而**对于运行环境，如果是团队多人协作的工程，建议将Dart与Flutter的SDK环境写死，统一团队的开发环境**，避免因为跨SDK版本出现的API差异进而导致工程问题。

比如，在上面的示例中，我们可以将Dart SDK写死为2.3.0，Flutter SDK写死为1.2.1。

```
environment:
  sdk: 2.3.0
  flutter: 1.2.1
```

基于版本的方式引用第三方包，需要在其Pub上进行公开发布，我们可以访问[https://pub.dev/](https://pub.dev/)来获取可用的第三方包。而对于不对外公开发布，或者目前处于开发调试阶段的包，我们需要设置数据源，使用本地路径或Git地址的方式进行包声明。

在下面的例子中，我们分别以路径依赖以及Git依赖的方式，声明了package1和package2这两个包：

```
dependencies:
  package1:
    path: ../package1/  #路径依赖
  date_format:
    git:
      url: https://github.com/xxx/package2.git #git依赖
```

在开发应用时，我们可以不写明具体的版本号，而是以区间的方式声明包的依赖；但对于一个程序而言，其运行时具体引用哪个版本的依赖包必须要确定下来。因此，**除了管理第三方依赖，包管理工具Pub的另一个职责是，找出一组同时满足每个包版本约束的包版本。**包版本一旦确定，接下来就是下载对应版本的包了。

对于dependencies中的不同数据源，Dart会使用不同的方式进行管理，最终会将远端的包全部下载到本地。比如，对于Git声明依赖的方式，Pub会clone Git仓库；对于版本号的方式，Pub则会从pub.dartlang.org下载包。如果包还有其他的依赖包，比如package1包还依赖package3包，Pub也会一并下载。

然后，在完成了所有依赖包的下载后，**Pub会在应用的根目录下创建.packages文件**，将依赖的包名与系统缓存中的包文件路径进行映射，方便后续维护。

最后，**Pub会自动创建pubspec.lock文件**。pubspec.lock文件的作用类似iOS的Podfile.lock或前端的package-lock.json文件，用于记录当前状态下实际安装的各个直接依赖、间接依赖的包的具体来源和版本号。

比较活跃的第三方包的升级通常比较频繁，因此对于多人协作的Flutter应用来说，我们需要把pubspec.lock文件也一并提交到代码版本管理中，这样团队中的所有人在使用这个应用时安装的所有依赖都是完全一样的，以避免出现库函数找不到或者其他的依赖错误。

**除了提供功能和代码维度的依赖之外，包还可以提供资源的依赖**。在依赖包中的pubspec.yaml文件已经声明了同样资源的情况下，为节省应用程序安装包大小，我们需要复用依赖包中的资源。

在下面的例子中，我们的应用程序依赖了一个名为package4的包，而它的目录结构是这样的：

```
pubspec.yaml
└──assets
    ├──2.0x
    │   └── placeholder.png
    └──3.0x
        └── placeholder.png
```

其中，placeholder.png是可复用资源。因此，在应用程序中，我们可以通过Image和AssetImage提供的package参数，根据设备实际分辨率去加载图像。

```
Image.asset('assets/placeholder.png', package: 'package4');

AssetImage('assets/placeholder.png', package: 'package4');
例子
```

#### 例子

接下来，我们通过一个日期格式化的例子，来演示如何使用第三方库。

在Flutter中，提供了表达日期的数据结构[DateTime](https://api.flutter.dev/flutter/dart-core/DateTime-class.html)，这个类拥有极大的表示范围，可以表达1970-01-01 UTC时间后 100,000,000天内的任意时刻。不过，如果我们想要格式化显示日期和时间，DateTime并没有提供非常方便的方法，我们不得不自己取出年、月、日、时、分、秒，来定制显示方式。

值得庆幸的是，我们可以通过date_format这个第三方包来实现我们的诉求：date_format提供了若干常用的日期格式化方法，可以很方便地实现格式化日期的功能。

**首先**，我们在Pub上找到date_format这个包，确定其使用说明：

![cd7a22dbaf304e7ca6e4e7e3919f68a0](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/cd7a22dbaf304e7ca6e4e7e3919f68a0.jpg)

图1 date_format使用说明

date_format包最新的版本是1.0.6，于是**接下来**我们把date_format添加到pubspec.yaml中：

```
dependencies:
  date_format: 1.0.6
```

**随后**，IDE（Android Studio）监测到了配置文件的改动，提醒我们进行安装包依赖更新。于是，我们点击Get dependencies，下载date_format :

![9f77c5091c594075918405c008dfcefa](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/9f77c5091c594075918405c008dfcefa.jpg)

图2 下载安装包依赖

下载完成后，我们就可以在工程中使用date_format来进行日期的格式化了：

```
print(formatDate(DateTime.now(), [mm, '月', dd, '日', hh, ':', n]));
//输出2019年06月30日01:56
print(formatDate(DateTime.now(), [m, '月第', w, '周']));
//输出6月第5周
```

#### 总结

好了，今天的分享就到这里。我们简单回顾一下今天的内容。

在Flutter中，资源与工程代码依赖属于包管理范畴，采用包的配置文件pubspec.yaml进行统一管理。

我们可以通过pubspec.yaml设置包的元数据（比如，包的名称和版本）、运行环境（比如，Dart SDK与Fluter SDK版本）、外部依赖和内部配置。

对于依赖的指定，可以以区间的方式确定版本兼容范围，也可以指定本地路径、Git、Pub这三种不同的数据源，包管理工具会找出同时满足每个依赖包版本约束的包版本，然后依次下载，并通过.packages文件建立下载缓存与包名的映射，最后统一将当前状态下，实际安装的各个包的具体来源和版本号记录至pubspec.lock文件。

现代编程语言大都自带第依赖管理机制，其核心功能是为工程中所有直接或间接依赖的代码库找到合适的版本，但这并不容易。就比如前端的依赖管理器npm的早期版本，就曾因为不太合理的算法设计，导致计算依赖耗时过长，依赖文件夹也高速膨胀，一度被开发者们戏称为“黑洞”。而Dart使用的Pub依赖管理机制所采用的[PubGrub算法](https://github.com/dart-lang/pub/blob/master/doc/solver.md)则解决了这些问题，因此被称为下一代版本依赖解决算法，在2018年底被苹果公司吸纳，成为Swift所采用的[依赖管理器算法](https://github.com/apple/swift-package-manager/pull/1918)。

当然，如果你的工程里的依赖比较多，并且依赖关系比较复杂，即使再优秀的依赖解决算法也需要花费较长的时间才能计算出合适的依赖库版本。如果我们想减少依赖管理器为你寻找代码库依赖版本所耗费的时间，一个简单的做法就是从源头抓起，在pubspec.yaml文件中固定那些依赖关系复杂的第三方库们，及它们递归依赖的第三方库的版本号。

#### 思考题

最后，我给你留下两道思考题吧。

1. pubspec.yaml、.packages与pubspec.lock这三个文件，在包管理中的具体作用是什么？
2. .packages与pubspec.lock是否需要做代码版本管理呢？为什么？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

## 交互、数据与网络

### 用户交互事件该如何响应？

你好，我是陈航。今天，我和你分享的主题是，如何响应用户交互事件。

在前面两篇文章中，我和你一起学习了Flutter依赖的包管理机制。在Flutter中，包是包含了外部依赖的功能抽象。对于资源和工程代码依赖，我们采用包配置文件pubspec.yaml进行统一管理。

通过前面几个章节的学习，我们已经掌握了如何在Flutter中通过内部实现和外部依赖去实现自定义UI，完善业务逻辑。但除了按钮和ListView这些动态的组件之外，我们还无法响应用户交互行为。那今天的分享中，我就着重与你讲述Flutter是如何监听和响应用户的手势操作的。

手势操作在Flutter中分为两类：

- 第一类是原始的指针事件（Pointer Event），即原生开发中常见的触摸事件，表示屏幕上触摸（或鼠标、手写笔）行为触发的位移行为；
- 第二类则是手势识别（Gesture Detector），表示多个原始指针事件的组合操作，如点击、双击、长按等，是指针事件的语义化封装。

接下来，我们先看一下原始的指针事件。

#### 指针事件

指针事件表示用户交互的原始触摸数据，如手指接触屏幕PointerDownEvent、手指在屏幕上移动PointerMoveEvent、手指抬起PointerUpEvent，以及触摸取消PointerCancelEvent，这与原生系统的底层触摸事件抽象是一致的。

在手指接触屏幕，触摸事件发起时，Flutter会确定手指与屏幕发生接触的位置上究竟有哪些组件，并将触摸事件交给最内层的组件去响应。与浏览器中的事件冒泡机制类似，事件会从这个最内层的组件开始，沿着组件树向根节点向上冒泡分发。

不过Flutter无法像浏览器冒泡那样取消或者停止事件进一步分发，我们只能通过hitTestBehavior去调整组件在命中测试期内应该如何表现，比如把触摸事件交给子组件，或者交给其视图层级之下的组件去响应。

关于组件层面的原始指针事件的监听，Flutter提供了Listener Widget，可以监听其子Widget的原始指针事件。

现在，我们一起看一个Listener的案例。我定义了一个宽度为300的红色正方形Container，利用Listener监听其内部Down、Move及Up事件：

```
Listener(
  child: Container(
    color: Colors.red,//背景色红色
    width: 300,
    height: 300,
  ),
  onPointerDown: (event) => print("down $event"),//手势按下回调
  onPointerMove:  (event) => print("move $event"),//手势移动回调
  onPointerUp:  (event) => print("up $event"),//手势抬起回调
);
```

我们试着在红色正方形区域内进行触摸点击、移动、抬起，可以看到Listener监听到了一系列原始指针事件，并打印出了这些事件的位置信息：

```
I/flutter (13829): up PointerUpEvent(Offset(97.7, 287.7))
I/flutter (13829): down PointerDownEvent(Offset(150.8, 313.4))
I/flutter (13829): move PointerMoveEvent(Offset(152.0, 313.4))
I/flutter (13829): move PointerMoveEvent(Offset(154.6, 313.4))
I/flutter (13829): up PointerUpEvent(Offset(157.1, 312.3))
```

#### 手势识别

使用Listener可以直接监听指针事件。不过指针事件毕竟太原始了，如果我们想要获取更多的触摸事件细节，比如判断用户是否正在拖拽控件，直接使用指针事件的话就会非常复杂。

通常情况下，响应用户交互行为的话，我们会使用封装了手势语义操作的Gesture，如点击onTap、双击onDoubleTap、长按onLongPress、拖拽onPanUpdate、缩放onScaleUpdate等。另外，Gesture可以支持同时分发多个手势交互行为，意味着我们可以通过Gesture同时监听多个事件。

**Gesture是手势语义的抽象，而如果我们想从组件层监听手势，则需要使用GestureDetector**。GestureDetector是一个处理各种高级用户触摸行为的Widget，与Listener一样，也是一个功能性组件。

接下来，我们通过一个案例来看看GestureDetector的用法。

我定义了一个Stack层叠布局，使用Positioned组件将1个红色的Container放置在左上角，并同时监听点击、双击、长按和拖拽事件。在拖拽事件的回调方法中，我们更新了Container的位置：

```
//红色container坐标
double _top = 0.0;
double _left = 0.0;
Stack(//使用Stack组件去叠加视图，便于直接控制视图坐标
  children: <Widget>[
    Positioned(
      top: _top,
      left: _left,
      child: GestureDetector(//手势识别
        child: Container(color: Colors.red,width: 50,height: 50),//红色子视图
        onTap: ()=>print("Tap"),//点击回调
        onDoubleTap: ()=>print("Double Tap"),//双击回调
        onLongPress: ()=>print("Long Press"),//长按回调
        onPanUpdate: (e) {//拖动回调
          setState(() {
            //更新位置
            _left += e.delta.dx;
            _top += e.delta.dy;
          });
        },
      ),
    )
  ],
);
```

运行这段代码，并查看控制台输出，可以看到，红色的Container除了可以响应我们的拖拽行为外，还能够同时响应点击、双击、长按这些事件。

![55eb1854904a4db9af2f07f0c41cad69](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/55eb1854904a4db9af2f07f0c41cad69.jpg)

图1 GestureDetector示例

尽管在上面的例子中，我们对一个Widget同时监听了多个手势事件，但最终只会有一个手势能够得到本次事件的处理权。对于多个手势的识别，Flutter引入了**手势竞技场（Arena）**的概念，用来识别究竟哪个手势可以响应用户事件。手势竞技场会考虑用户触摸屏幕的时长、位移以及拖动方向，来确定最终手势。

**那手势竞技场具体是怎么实现的呢？**

实际上，GestureDetector内部对每一个手势都建立了一个工厂类（Gesture Factory）。而工厂类的内部会使用手势识别类（GestureRecognizer），来确定当前处理的手势。

而所有手势的工厂类都会被交给RawGestureDetector类，以完成监测手势的大量工作：使用Listener监听原始指针事件，并在状态改变时把信息同步给所有的手势识别器，然后这些手势会在竞技场决定最后由谁来响应用户事件。

有些时候我们可能会在应用中给多个视图注册同类型的手势监听器，比如微博的信息流列表中的微博，点击不同区域会有不同的响应：点击头像会进入用户个人主页，点击图片会进入查看大图页面，点击其他部分会进入微博详情页等。

像这样的手势识别发生在多个存在父子关系的视图时，手势竞技场会一并检查父视图和子视图的手势，并且通常最终会确认由子视图来响应事件。而这也是合乎常理的：从视觉效果上看，子视图的视图层级位于父视图之上，相当于对其进行了遮挡，因此从事件处理上看，子视图自然是事件响应的第一责任人。

在下面的示例中，我定义了两个嵌套的Container容器，分别加入了点击识别事件：

```
GestureDetector(
  onTap: () => print('Parent tapped'),//父视图的点击回调
  child: Container(
    color: Colors.pinkAccent,
    child: Center(
      child: GestureDetector(
        onTap: () => print('Child tapped'),//子视图的点击回调
        child: Container(
          color: Colors.blueAccent,
          width: 200.0,
          height: 200.0,
        ),
      ),
    ),
  ),
);
```

运行这段代码，然后在蓝色区域进行点击，可以发现：尽管父容器也监听了点击事件，但Flutter只响应了子容器的点击事件。

```
I/flutter (16188): Child tapped
```

![61ae49bbfca04d4f9f9af92a9eaf96a1](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/61ae49bbfca04d4f9f9af92a9eaf96a1.jpg)

图2 父子嵌套GestureDetector示例

为了让父容器也能接收到手势，我们需要同时使用RawGestureDetector和GestureFactory，来改变竞技场决定由谁来响应用户事件的结果。

在此之前，**我们还需要自定义一个手势识别器**，让这个识别器在竞技场被PK失败时，能够再把自己重新添加回来，以便接下来还能继续去响应用户事件。

在下面的代码中，我定义了一个继承自点击手势识别器TapGestureRecognizer的类，并重写了其rejectGesture方法，手动地把自己又复活了：

```
class MultipleTapGestureRecognizer extends TapGestureRecognizer {
  @override
  void rejectGesture(int pointer) {
    acceptGesture(pointer);
  }
}
```

接下来，我们需要将手势识别器和其工厂类传递给RawGestureDetector，以便用户产生手势交互事件时能够立刻找到对应的识别方法。事实上，RawGestureDetector的初始化函数所做的配置工作，就是定义不同手势识别器和其工厂类的映射关系。

这里，由于我们只需要处理点击事件，所以只配置一个识别器即可。工厂类的初始化采用GestureRecognizerFactoryWithHandlers函数完成，这个函数提供了手势识别对象创建，以及对应的初始化入口。

在下面的代码中，我们完成了自定义手势识别器的创建，并设置了点击事件回调方法。需要注意的是，由于我们只需要在父容器监听子容器的点击事件，所以只需要将父容器用RawGestureDetector包装起来就可以了，而子容器保持不变：

```
RawGestureDetector(//自己构造父Widget的手势识别映射关系
  gestures: {
    //建立多手势识别器与手势识别工厂类的映射关系，从而返回可以响应该手势的recognizer
    MultipleTapGestureRecognizer: GestureRecognizerFactoryWithHandlers<
        MultipleTapGestureRecognizer>(
          () => MultipleTapGestureRecognizer(),
          (MultipleTapGestureRecognizer instance) {
        instance.onTap = () => print('parent tapped ');//点击回调
      },
    )
  },
  child: Container(
    color: Colors.pinkAccent,
    child: Center(
      child: GestureDetector(//子视图可以继续使用GestureDetector
        onTap: () => print('Child tapped'),
        child: Container(...),
      ),
    ),
  ),
);
```

运行一下这段代码，我们可以看到，当点击蓝色容器时，其父容器也收到了Tap事件。

```
I/flutter (16188): Child tapped
I/flutter (16188): parent tapped
```

#### 总结

好了，今天的分享就到这里。我们来简单回顾下Flutter是如何响应用户事件的。

首先，我们了解了Flutter底层原始指针事件，以及对应的监听方式和冒泡分发机制。

然后，我们学习了封装了底层指针事件手势语义的Gesture，了解了多个手势的识别方法，以及其同时支持多个手势交互的能力。

最后，我与你介绍了Gesture的事件处理机制：在Flutter中，尽管我们可以对一个Widget监听多个手势，或是对多个Widget监听同一个手势，但Flutter会使用手势竞技场来进行各个手势的PK，以保证最终只会有一个手势能够响应用户行为。如果我们希望同时能有多个手势去响应用户行为，需要去自定义手势，利用RawGestureDetector和手势工厂类，在竞技场PK失败时，手动把它复活。

在处理多个手势识别场景，很容易出现手势冲突的问题。比如，当需要对图片进行点击、长按、旋转、缩放、拖动等操作的时候，如何识别用户当前是点击还是长按，是旋转还是缩放。如果想要精确地处理复杂交互手势，我们势必需要介入手势识别过程，解决异常。

不过需要注意的是，冲突的只是手势的语义化识别过程，原始指针事件是不会冲突的。所以，在遇到复杂的冲突场景通过手势很难搞定时，我们也可以通过Listener直接识别原始指针事件，从而解决手势识别的冲突。

我把今天分享所涉及到的[事件处理demo](https://github.com/cyndibaby905/19_gesture_demo)放到了GitHub上，你可以下载下来自己运行，进一步巩固学习效果。

#### 思考题

最后，我给你留下两个思考题吧。

1. 对于一个父容器中存在按钮FlatButton的界面，在父容器使用GestureDetector监听了onTap事件的情况下，如果我们点击按钮，父容器的点击事件会被识别吗，为什么？
2. 如果监听的是onDoubleTap事件，在按钮上双击，父容器的双击事件会被识别吗，为什么？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 关于跨组件传递数据，你只需要记住这三招

你好，我是陈航。

在上一篇文章中，我带你一起学习了在Flutter中如何响应用户交互事件（手势）。手势处理在Flutter中分为两种：原始的指针事件处理和高级的手势识别。

其中，指针事件以冒泡机制分发，通过Listener完成监听；而手势识别则通过Gesture处理。但需要注意的是，虽然Flutter可以同时支持多个手势（包括一个Widget监听多个手势，或是多个Widget监听同一个手势），但最终只会有一个Widget的手势能够响应用户行为。为了改变这一点，我们需要自定义手势，修改手势竞技场对于多手势优先级判断的默认行为。

除了需要响应外部的事件之外，UI框架的另一个重要任务是，处理好各个组件之间的数据同步关系。尤其对于Flutter这样大量依靠组合Widget的行为来实现用户界面的框架来说，如何确保数据的改变能够映射到最终的视觉效果上就显得更为重要。所以，在今天这篇文章中，我就与你介绍在Flutter中如何进行跨组件数据传递。

在之前的分享中，通过组合嵌套的方式，利用数据对基础Widget的样式进行视觉属性定制，我们已经实现了多种界面布局。所以，你应该已经体会到了，在Flutter中实现跨组件数据传递的标准方式是通过属性传值。

但是，对于稍微复杂一点的、尤其视图层级比较深的UI样式，一个属性可能需要跨越很多层才能传递给子组件，这种传递方式就会导致中间很多并不需要这个属性的组件也需要接收其子Widget的数据，不仅繁琐而且冗余。

所以，对于数据的跨层传递，Flutter还提供了三种方案：InheritedWidget、Notification和EventBus。接下来，我将依次为你讲解这三种方案。

#### InheritedWidget

InheritedWidget是Flutter中的一个功能型Widget，适用于在Widget树中共享数据的场景。通过它，我们可以高效地将数据在Widget树中进行跨层传递。

在前面的第16篇文章“[从夜间模式说起，如何定制不同风格的App主题？](https://time.geekbang.org/column/article/112148)”中，我与你介绍了如何通过Theme去访问当前界面的样式风格，从而进行样式复用的例子，比如Theme.of(context).primaryColor。

**Theme类是通过InheritedWidget实现的典型案例**。在子Widget中通过Theme.of方法找到上层Theme的Widget，获取到其属性的同时，建立子Widget和上层父Widget的观察者关系，当上层父Widget属性修改的时候，子Widget也会触发更新。

接下来，我就以Flutter工程模板中的计数器为例，与你说明InheritedWidget的使用方法。

- 首先，为了使用InheritedWidget，我们定义了一个继承自它的新类CountContainer。
- 然后，我们将计数器状态count属性放到CountContainer中，并提供了一个of方法方便其子Widget在Widget树中找到它。
- 最后，我们重写了updateShouldNotify方法，这个方法会在Flutter判断InheritedWidget是否需要重建，从而通知下层观察者组件更新数据时被调用到。在这里，我们直接判断count是否相等即可。

```
class CountContainer extends InheritedWidget {
  //方便其子Widget在Widget树中找到它
  static CountContainer of(BuildContext context) => context.inheritFromWidgetOfExactType(CountContainer) as CountContainer;

  final int count;

  CountContainer({
    Key key,
    @required this.count,
    @required Widget child,
  }): super(key: key, child: child);

  // 判断是否需要更新
  @override
  bool updateShouldNotify(CountContainer oldWidget) => count != oldWidget.count;
}
```

然后，我们使用CountContainer作为根节点，并用0初始化count。随后在其子Widget Counter中，我们通过InheritedCountContainer.of方法找到它，获取计数状态count并展示：

```
class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
   //将CountContainer作为根节点，并使用0作为初始化count
    return CountContainer(
      count: 0,
      child: Counter()
    );
  }
}

class Counter extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //获取InheritedWidget节点
    CountContainer state = CountContainer.of(context);
    return Scaffold(
      appBar: AppBar(title: Text("InheritedWidget demo")),
      body: Text(
        'You have pushed the button this many times: ${state.count}',
      ),
    );
}
```

运行一下，效果如下图所示：

![2073de6086744ac6b3c5e723a9f52eb4](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/2073de6086744ac6b3c5e723a9f52eb4.jpg)

图1 InheritedWidget使用方法

可以看到InheritedWidget的使用方法还是比较简单的，无论Counter在CountContainer下层什么位置，都能获取到其父Widget的计数属性count，再也不用手动传递属性了。

**不过，InheritedWidget仅提供了数据读的能力，如果我们想要修改它的数据，则需要把它和StatefulWidget中的State配套使用**。我们需要把InheritedWidget中的数据和相关的数据修改方法，全部移到StatefulWidget中的State上，而InheritedWidget只需要保留对它们的引用。

我们对上面的代码稍加修改，删掉CountContainer中持有的count属性，增加对数据持有者State，以及数据修改方法的引用：

```
class CountContainer extends InheritedWidget {
  ...
  final _MyHomePageState model;//直接使用MyHomePage中的State获取数据
  final Function() increment;

  CountContainer({
    Key key,
    @required this.model,
    @required this.increment,
    @required Widget child,
  }): super(key: key, child: child);
  ...
}
```

然后，我们将count数据和其对应的修改方法放在了State中，仍然使用CountContainer作为根节点，完成了数据和修改方法的初始化。

在其子Widget Counter中，我们还是通过InheritedCountContainer.of方法找到它，将计数状态count与UI展示同步，将按钮的点击事件与数据修改同步：

```
class _MyHomePageState extends State<MyHomePage> {
  int count = 0;
  void _incrementCounter() => setState(() {count++;});//修改计数器

  @override
  Widget build(BuildContext context) {
    return CountContainer(
      model: this,//将自身作为model交给CountContainer
      increment: _incrementCounter,//提供修改数据的方法
      child:Counter()
    );
  }
}

class Counter extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //获取InheritedWidget节点
    CountContainer state = CountContainer.of(context);
    return Scaffold(
      ...
      body: Text(
        'You have pushed the button this many times: ${state.model.count}', //关联数据读方法
      ),
      floatingActionButton: FloatingActionButton(onPressed: state.increment), //关联数据修改方法
    );
  }
}
```

运行一下，可以看到，我们已经实现InheritedWidget数据的读写了。

![caaaf68bdd314128891f66db92e113de](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/caaaf68bdd314128891f66db92e113de.jpg)

图2 InheritedWidget数据修改示例

#### Notification

Notification是Flutter中进行跨层数据共享的另一个重要的机制。如果说InheritedWidget的数据流动方式是从父Widget到子Widget逐层传递，那Notificaiton则恰恰相反，数据流动方式是从子Widget向上传递至父Widget。这样的数据传递机制适用于子Widget状态变更，发送通知上报的场景。

在前面的第13篇文章“[经典控件（二）：UITableView/ListView在Flutter中是什么？](https://time.geekbang.org/column/article/110859)”中，我与你介绍了ScrollNotification的使用方法：ListView在滚动时会分发通知，我们可以在上层使用NotificationListener监听ScrollNotification，根据其状态做出相应的处理。

自定义通知的监听与ScrollNotification并无不同，而如果想要实现自定义通知，我们首先需要继承Notification类。Notification类提供了dispatch方法，可以让我们沿着context对应的Element节点树向上逐层发送通知。

接下来，我们一起看一个具体的案例吧。在下面的代码中，我们自定义了一个通知和子Widget。子Widget是一个按钮，在点击时会发送通知：

```
class CustomNotification extends Notification {
  CustomNotification(this.msg);
  final String msg;
}

//抽离出一个子Widget用来发通知
class CustomChild extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return RaisedButton(
      //按钮点击时分发通知
      onPressed: () => CustomNotification("Hi").dispatch(context),
      child: Text("Fire Notification"),
    );
  }
}
```

而在子Widget的父Widget中，我们监听了这个通知，一旦收到通知，就会触发界面刷新，展示收到的通知信息：

```
class _MyHomePageState extends State<MyHomePage> {
  String _msg = "通知：";
  @override
  Widget build(BuildContext context) {
    //监听通知
    return NotificationListener<CustomNotification>(
        onNotification: (notification) {
          setState(() {_msg += notification.msg+"  ";});//收到子Widget通知，更新msg
        },
        child:Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[Text(_msg),CustomChild()],//将子Widget加入到视图树中
        )
    );
  }
}
```

运行一下代码，可以看到，我们每次点击按钮之后，界面上都会出现最新的通知信息：

![1a7792ad641f410ba50c03af94703dd7](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/1a7792ad641f410ba50c03af94703dd7.jpg)

图3 自定义Notification

#### EventBus

无论是InheritedWidget还是Notificaiton，它们的使用场景都需要依靠Widget树，也就意味着只能在有父子关系的Widget之间进行数据共享。但是，组件间数据传递还有一种常见场景：这些组件间不存在父子关系。这时，事件总线EventBus就登场了。

事件总线是在Flutter中实现跨组件通信的机制。它遵循发布/订阅模式，允许订阅者订阅事件，当发布者触发事件时，订阅者和发布者之间可以通过事件进行交互。发布者和订阅者之间无需有父子关系，甚至非Widget对象也可以发布/订阅。这些特点与其他平台的事件总线机制是类似的。

接下来，我们通过一个跨页面通信的例子，来看一下事件总线的具体使用方法。需要注意的是，EventBus是一个第三方插件，因此我们需要在pubspec.yaml文件中声明它：

```
dependencies:
  event_bus: 1.1.0
```

EventBus的使用方式灵活，可以支持任意对象的传递。所以在这里，我们传输数据的载体就选择了一个有字符串属性的自定义事件类CustomEvent：

```
class CustomEvent {
  String msg;
  CustomEvent(this.msg);
}
```

然后，我们定义了一个全局的eventBus对象，并在第一个页面监听了CustomEvent事件，一旦收到事件，就会刷新UI。需要注意的是，千万别忘了在State被销毁时清理掉事件注册，否则你会发现State永远被EventBus持有着，无法释放，从而造成内存泄漏：

```
//建立公共的event bus
EventBus eventBus = new EventBus();
//第一个页面
class _FirstScreenState extends  State<FirstScreen>  {

  String msg = "通知：";
  StreamSubscription subscription;
  @override
  initState() {
   //监听CustomEvent事件，刷新UI
    subscription = eventBus.on<CustomEvent>().listen((event) {
      setState(() {msg+= event.msg;});//更新msg
    });
    super.initState();
  }
  dispose() {
    subscription.cancel();//State销毁时，清理注册
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      body:Text(msg),
      ...
    );
  }
}
```

最后，我们在第二个页面以按钮点击回调的方式，触发了CustomEvent事件：

```
class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      ...
      body: RaisedButton(
          child: Text('Fire Event'),
          // 触发CustomEvent事件
          onPressed: ()=> eventBus.fire(CustomEvent("hello"))
      ),
    );
  }
}
```

运行一下，多点击几下第二个页面的按钮，然后返回查看第一个页面上的消息：

![95cdd48d16ff412696f4fe1755eca181](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/95cdd48d16ff412696f4fe1755eca181.jpg)

图4 EventBus示例

可以看到，EventBus的使用方法还是比较简单的，使用限制也相对最少。

这里我准备了一张表格，把属性传值、InheritedWidget、Notification与EventBus这四种数据共享方式的特点和使用场景做了简单总结，供你参考：

![e286492d3a274662982dd8f79e9b0450](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e286492d3a274662982dd8f79e9b0450.jpg)

图5 属性传值、InheritedWidget、Notification与EventBus数据传递方式对比

#### 总结

好了，今天的分享就到这里。我们来简单回顾下在Flutter中，如何实现跨组件的数据共享。

首先，我们认识了InheritedWidget。对于视图层级比较深的UI样式，直接通过属性传值的方式会导致很多中间层增加冗余属性，而使用InheritedWidget可以实现子Widget跨层共享父Widget的属性。需要注意的是，InheritedWidget中的属性在子Widget中只能读，如果有修改的场景，我们需要把它和StatefulWidget中的State配套使用。

然后，我们学习了Notification，这种由下到上传递数据的跨层共享机制。我们可以使用NotificationListener，在父Widget监听来自子Widget的事件。

最后，我与你介绍了EventBus，这种无需发布者与订阅者之间存在父子关系的数据同步机制。

我把今天分享所涉及到的三种跨组件的[数据共享方式demo](https://github.com/cyndibaby905/20_data_transfer)放到了GitHub，你可以下载下来自己运行，体会它们之间的共同点和差异。

#### 思考题

最后，我来给你留下一个思考题吧。

请你分别概括属性传值、InheritedWidget、Notification与EventBus的优缺点。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 路由与导航，Flutter是这样实现页面切换的

你好，我是陈航。

在上一篇文章中，我带你一起学习了如何在Flutter中实现跨组件数据传递。其中，InheritedWidget适用于子Widget跨层共享父Widget数据的场景，如果子Widget还需要修改父Widget数据，则需要和State一起配套使用。而Notification，则适用于父Widget监听子Widget事件的场景。对于没有父子关系的通信双方，我们还可以使用EventBus实现基于订阅/发布模式的机制实现数据交互。

如果说UI框架的视图元素的基本单位是组件，那应用程序的基本单位就是页面了。对于拥有多个页面的应用程序而言，如何从一个页面平滑地过渡到另一个页面，我们需要有一个统一的机制来管理页面之间的跳转，通常被称为**路由管理或导航管理**。

我们首先需要知道目标页面对象，在完成目标页面初始化后，用框架提供的方式打开它。比如，在Android/iOS中我们通常会初始化一个Intent或ViewController，通过startActivity或pushViewController来打开一个新的页面；而在React中，我们使用navigation来管理所有页面，只要知道页面的名称，就可以立即导航到这个页面。

其实，Flutter的路由管理也借鉴了这两种设计思路。那么，今天我们就来看看，如何在一个Flutter应用中管理不同页面的命名和过渡。

#### 路由管理

在Flutter中，页面之间的跳转是通过Route和Navigator来管理的：

- Route是页面的抽象，主要负责创建对应的界面，接收参数，响应Navigator打开和关闭；
- 而Navigator则会维护一个路由栈管理Route，Route打开即入栈，Route关闭即出栈，还可以直接替换栈内的某一个Route。

而根据是否需要提前注册页面标识符，Flutter中的路由管理可以分为两种方式：

- 基本路由。无需提前注册，在页面切换时需要自己构造页面实例。
- 命名路由。需要提前注册页面标识符，在页面切换时通过标识符直接打开新的路由。

接下来，我们先一起看看基本路由这种管理方式吧。

##### 基本路由

在Flutter中，**基本路由的使用方法和Android/iOS打开新页面的方式非常相似**。要导航到一个新的页面，我们需要创建一个MaterialPageRoute的实例，调用Navigator.push方法将新页面压到堆栈的顶部。

其中，MaterialPageRoute是一种路由模板，定义了路由创建及切换过渡动画的相关配置，可以针对不同平台，实现与平台页面切换动画风格一致的路由切换动画。

而如果我们想返回上一个页面，则需要调用Navigator.pop方法从堆栈中删除这个页面。

下面的代码演示了基本路由的使用方法：在第一个页面的按钮事件中打开第二个页面，并在第二个页面的按钮事件中回退到第一个页面：

```
class FirstScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return RaisedButton(
      //打开页面
      onPressed: ()=> Navigator.push(context, MaterialPageRoute(builder: (context) => SecondScreen()));
    );
  }
}

class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return RaisedButton(
      // 回退页面
      onPressed: ()=> Navigator.pop(context)
    );
  }
}
```

运行一下代码，效果如下：

![5095923739164df8adb0ce7feabf05f7](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/5095923739164df8adb0ce7feabf05f7.jpg)

图1 基本路由示例

可以看到，基本路由的使用还是比较简单的。接下来，我们再看看命名路由的使用方法。

##### 命名路由

基本路由使用方式相对简单灵活，适用于应用中页面不多的场景。而在应用中页面比较多的情况下，再使用基本路由方式，那么每次跳转到一个新的页面，我们都要手动创建MaterialPageRoute实例，初始化页面，然后调用push方法打开它，还是比较麻烦的。

所以，Flutter提供了另外一种方式来简化路由管理，即命名路由。我们给页面起一个名字，然后就可以直接通过页面名字打开它了。这种方式简单直观，**与React中的navigation使用方式类似**。

要想通过名字来指定页面切换，我们必须先给应用程序MaterialApp提供一个页面名称映射规则，即路由表routes，这样Flutter才知道名字与页面Widget的对应关系。

路由表实际上是一个Map，其中key值对应页面名字，而value值则是一个WidgetBuilder回调函数，我们需要在这个函数中创建对应的页面。而一旦在路由表中定义好了页面名字，我们就可以使用Navigator.pushNamed来打开页面了。

下面的代码演示了命名路由的使用方法：在MaterialApp完成了页面的名字second_page及页面的初始化方法注册绑定，后续我们就可以在代码中以second_page这个名字打开页面了：

```
MaterialApp(
    ...
    //注册路由
    routes:{
      "second_page":(context)=>SecondPage(),
    },
);
//使用名字打开页面
Navigator.pushNamed(context,"second_page");
```

可以看到，命名路由的使用也很简单。

不过**由于路由的注册和使用都采用字符串来标识，这就会带来一个隐患**：如果我们打开了一个不存在的路由会怎么办？

也许你会想到，我们可以约定使用字符串常量去定义、使用路由，但我们无法避免通过接口数据下发的错误路由标识符场景。面对这种情况，无论是直接报错或是不响应错误路由，都不是一个用户体验良好的解决办法。

**更好的办法是**，对用户进行友好的错误提示，比如跳转到一个统一的NotFoundScreen页面，也方便我们对这类错误进行统一收集、上报。

在注册路由表时，Flutter提供了UnknownRoute属性，我们可以对未知的路由标识符进行统一的页面跳转处理。

下面的代码演示了如何注册错误路由处理。和基本路由的使用方法类似，我们只需要返回一个固定的页面即可。

```
MaterialApp(
    ...
    //注册路由
    routes:{
      "second_page":(context)=>SecondPage(),
    },
    //错误路由处理，统一返回UnknownPage
    onUnknownRoute: (RouteSettings setting) => MaterialPageRoute(builder: (context) => UnknownPage()),
);

//使用错误名字打开页面
Navigator.pushNamed(context,"unknown_page");
```

运行一下代码，可以看到，我们的应用不仅可以处理正确的页面路由标识，对错误的页面路由标识符也可以统一跳转到固定的错误处理页面了。

![7b714dd0f03e4664824e88c6174616cf](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/7b714dd0f03e4664824e88c6174616cf.jpg)

图2 命名路由示例

##### 页面参数

与基本路由能够精确地控制目标页面初始化方式不同，命名路由只能通过字符串名字来初始化固定目标页面。为了解决不同场景下目标页面的初始化需求，Flutter提供了路由参数的机制，可以在打开路由时传递相关参数，在目标页面通过RouteSettings来获取页面参数。

下面的代码演示了如何传递并获取参数：使用页面名称second_page打开页面时，传递了一个字符串参数，随后在SecondPage中，我们取出了这个参数，并将它展示在了文本中。

```
//打开页面时传递字符串参数
Navigator.of(context).pushNamed("second_page", arguments: "Hey");

class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //取出路由参数
    String msg = ModalRoute.of(context).settings.arguments as String;
    return Text(msg);
  }
}
```

除了页面打开时需要传递参数，对于特定的页面，在其关闭时，也需要传递参数告知页面处理结果。

比如在电商场景下，我们会在用户把商品加入购物车时，打开登录页面让用户登录，而在登录操作完成之后，关闭登录页面返回到当前页面时，登录页面会告诉当前页面新的用户身份，当前页面则会用新的用户身份刷新页面。

与Android提供的startActivityForResult方法可以监听目标页面的处理结果类似，Flutter也提供了**返回参数**的机制。在push目标页面时，可以设置目标页面关闭时监听函数，以获取返回参数；而目标页面可以在关闭路由时传递相关参数。

下面的代码演示了如何获取参数：在SecondPage页面关闭时，传递了一个字符串参数，随后在上一页监听函数中，我们取出了这个参数，并将它展示了出来。

```
class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: <Widget>[
          Text('Message from first screen: $msg'),
          RaisedButton(
            child: Text('back'),
            //页面关闭时传递参数
            onPressed: ()=> Navigator.pop(context,"Hi")
          )
        ]
      ));
  }
}

class _FirstPageState extends State<FirstPage> {
  String _msg='';
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      body: Column(children: <Widget>[
        RaisedButton(
            child: Text('命名路由（参数&回调）'),
            //打开页面，并监听页面关闭时传递的参数
            onPressed: ()=> Navigator.pushNamed(context, "third_page",arguments: "Hey").then((msg)=>setState(()=>_msg=msg)),
        ),
        Text('Message from Second screen: $_msg'),

      ],),
    );
  }
}
```

运行一下，可以看到在关闭SecondPage，重新回到FirstPage页面时，FirstPage把接收到的msg参数展示了出来：

![eb0fac7afbaa4d81a83d4c9e047a4c49](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/eb0fac7afbaa4d81a83d4c9e047a4c49.jpg)

图3 页面路由参数

#### 总结

好了，今天的分享就到这里。我们简单回顾一下今天的主要内容吧。

Flutter提供了基本路由和命名路由两种方式，来管理页面间的跳转。其中，基本路由需要自己手动创建页面实例，通过Navigator.push完成页面跳转；而命名路由需要提前注册页面标识符和页面创建方法，通过Navigator.pushNamed传入标识符实现页面跳转。

对于命名路由，如果我们需要响应错误路由标识符，还需要一并注册UnknownRoute。为了精细化控制路由切换，Flutter提供了页面打开与页面关闭的参数机制，我们可以在页面创建和目标页面关闭时，取出相应的参数。

可以看到，关于路由导航，Flutter综合了Android、iOS和React的特点，简洁而不失强大。

而在中大型应用中，我们通常会使用命名路由来管理页面间的切换。命名路由的最重要作用，就是建立了字符串标识符与各个页面之间的映射关系，使得各个页面之间完全解耦，应用内页面的切换只需要通过一个字符串标识符就可以搞定，为后期模块化打好基础。

我把今天分享所涉及的的知识点打包到了[GitHub](https://github.com/cyndibaby905/21_router_demo)上，你可以下载工程到本地，多运行几次，从而加深对基本路由、命名路由以及路由参数具体用法的印象。

#### 思考题

最后，我给你留下两个小作业吧。

1. 对于基本路由，如何传递页面参数？
2. 请实现一个计算页面，这个页面可以对前一个页面传入的2个数值参数进行求和，并在该页面关闭时告知上一页面计算的结果。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何构造炫酷的动画效果？

你好，我是陈航。

在上一篇文章中，我带你一起学习了Flutter中实现页面路由的两种方式：基本路由与命名路由，即手动创建页面进行切换，和通过前置路由注册后提供标识符进行跳转。除此之外，Flutter还在这两种路由方式的基础上，支持页面打开和页面关闭传递参数，可以更精确地控制路由切换。

通过前面第[12](https://time.geekbang.org/column/article/110292)、[13](https://time.geekbang.org/column/article/110859)、[14](https://time.geekbang.org/column/article/110848)和[15](https://time.geekbang.org/column/article/111673)篇文章的学习，我们已经掌握了开发一款样式精美的小型App的基本技能。但当下，用户对于终端页面的要求已经不再满足于只能实现产品功能，除了样式美观之外，还希望交互良好、有趣、自然。

动画就是提升用户体验的一个重要方式，一个恰当的组件动画或者页面切换动画，不仅能够缓解用户因为等待而带来的情绪问题，还会增加好感。Flutter既然完全接管了渲染层，除了静态的页面布局之外，对组件动画的支持自然也不在话下。

因此在今天的这篇文章中，我会向你介绍Flutter中动画的实现方法，看看如何让我们的页面动起来。

#### Animation、AnimationController与Listener

动画就是动起来的画面，是静态的画面根据事先定义好的规律，在一定时间内不断微调，产生变化效果。而动画实现由静止到动态，主要是靠人眼的视觉残留效应。所以，对动画系统而言，为了实现动画，它需要做三件事儿：

1. 确定画面变化的规律；
2. 根据这个规律，设定动画周期，启动动画；
3. 定期获取当前动画的值，不断地微调、重绘画面。

这三件事情对应到Flutter中，就是Animation、AnimationController与Listener：

1. Animation是Flutter动画库中的核心类，会根据预定规则，在单位时间内持续输出动画的当前状态。Animation知道当前动画的状态（比如，动画是否开始、停止、前进或者后退，以及动画的当前值），但却不知道这些状态究竟应用在哪个组件对象上。换句话说，Animation仅仅是用来提供动画数据，而不负责动画的渲染。
2. AnimationController用于管理Animation，可以用来设置动画的时长、启动动画、暂停动画、反转动画等。
3. Listener是Animation的回调函数，用来监听动画的进度变化，我们需要在这个回调函数中，根据动画的当前值重新渲染组件，实现动画的渲染。

接下来，我们看一个具体的案例：让大屏幕中间的Flutter Logo由小变大。

首先，我们初始化了一个动画周期为1秒的、用于管理动画的AnimationController对象，并用线性变化的Tween创建了一个变化范围从50到200的Animaiton对象。

然后，我们给这个Animaiton对象设置了一个进度监听器，并在进度监听器中强制界面重绘，刷新动画状态。

接下来，我们调用AnimationController对象的forward方法，启动动画：

```
class _AnimateAppState extends State<AnimateApp> with SingleTickerProviderStateMixin {
  AnimationController controller;
  Animation<double> animation;
  @override
  void initState() {
    super.initState();
    //创建动画周期为1秒的AnimationController对象
    controller = AnimationController(
        vsync: this, duration: const Duration(milliseconds: 1000));
    // 创建从50到200线性变化的Animation对象
    animation = Tween(begin: 50.0, end: 200.0).animate(controller)
      ..addListener(() {
        setState(() {}); //刷新界面
      });
    controller.forward(); //启动动画
  }
...
}
```

需要注意的是，我们在创建AnimationController的时候，设置了一个vsync属性。这个属性是用来防止出现不可见动画的。vsync对象会把动画绑定到一个Widget，当Widget不显示时，动画将会暂停，当Widget再次显示时，动画会重新恢复执行，这样就可以避免动画的组件不在当前屏幕时白白消耗资源。

我们在一开始提到，Animation只是用于提供动画数据，并不负责动画渲染，所以我们还需要在Widget的build方法中，把当前动画状态的值读出来，用于设置Flutter Logo容器的宽和高，才能最终实现动画效果：

```
@override
@override
Widget build(BuildContext context) {
  return MaterialApp(
    home: Center(
      child: Container(
      width: animation.value, // 将动画的值赋给widget的宽高
      height: animation.value,
      child: FlutterLogo()
    )));
}
```

最后，别忘了在页面销毁时，要释放动画资源：

```
@override
void dispose() {
  controller.dispose(); // 释放资源
  super.dispose();
}
```

我们试着运行一下，可以看到，Flutter Logo动起来了：

![9c84ff1e809f40b4b73a885c4817689f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/9c84ff1e809f40b4b73a885c4817689f.jpg)

图1 动画示例

我们在上面用到的Tween默认是线性变化的，但可以创建CurvedAnimation来实现非线性曲线动画。CurvedAnimation提供了很多常用的曲线，比如震荡曲线elasticOut：

```
//创建动画周期为1秒的AnimationController对象
controller = AnimationController(
    vsync: this, duration: const Duration(milliseconds: 1000));

//创建一条震荡曲线
final CurvedAnimation curve = CurvedAnimation(
    parent: controller, curve: Curves.elasticOut);
// 创建从50到200跟随振荡曲线变化的Animation对象
animation = Tween(begin: 50.0, end: 200.0).animate(curve)
```

运行一下，可以看到Flutter Logo有了一个弹性动画：

![d3b9c1fc966844fbbd91114e3dfeb26b](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d3b9c1fc966844fbbd91114e3dfeb26b.jpg)

图2 CurvedAnimation 示例

现在的问题是，这些动画只能执行一次。如果想让它像心跳一样执行，有两个办法：

1. 在启动动画时，使用repeat(reverse: true)，让动画来回重复执行。
2. 监听动画状态。在动画结束时，反向执行；在动画反向执行完毕时，重新启动执行。

具体的实现代码，如下所示：

```
//以下两段语句等价
//第一段
controller.repeat(reverse: true);//让动画重复执行

//第二段
animation.addStatusListener((status) {
    if (status == AnimationStatus.completed) {
      controller.reverse();//动画结束时反向执行
    } else if (status == AnimationStatus.dismissed) {
      controller.forward();//动画反向执行完毕时，重新执行
    }
});
controller.forward();//启动动画
```

运行一下，可以看到，我们实现了Flutter Logo的心跳效果。

![4b4713aa938c482f80215e99e9534234](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4b4713aa938c482f80215e99e9534234.jpg)

图3 Flutter Logo心跳

#### AnimatedWidget与AnimatedBuilder

在为Widget添加动画效果的过程中我们不难发现，Animation仅提供动画的数据，因此我们还需要监听动画执行进度，并在回调中使用setState强制刷新界面才能看到动画效果。考虑到这些步骤都是固定的，Flutter提供了两个类来帮我们简化这一步骤，即AnimatedWidget与AnimatedBuilder。

接下来，我们分别看看这两个类如何使用。

在构建Widget时，AnimatedWidget会将Animation的状态与其子Widget的视觉样式绑定。要使用AnimatedWidget，我们需要一个继承自它的新类，并接收Animation对象作为其初始化参数。然后，在build方法中，读取出Animation对象的当前值，用作初始化Widget的样式。

下面的案例演示了Flutter Logo的AnimatedWidget版本：用AnimatedLogo继承了AnimatedWidget，并在build方法中，把动画的值与容器的宽高做了绑定：

```
class AnimatedLogo extends AnimatedWidget {
  //AnimatedWidget需要在初始化时传入animation对象
  AnimatedLogo({Key key, Animation<double> animation})
      : super(key: key, listenable: animation);

  Widget build(BuildContext context) {
    //取出动画对象
    final Animation<double> animation = listenable;
    return Center(
      child: Container(
        height: animation.value,//根据动画对象的当前状态更新宽高
        width: animation.value,
        child: FlutterLogo(),
    ));
  }
}
```

在使用时，我们只需把Animation对象传入AnimatedLogo即可，再也不用监听动画的执行进度刷新UI了：

```
MaterialApp(
  home: Scaffold(
    body: AnimatedLogo(animation: animation)//初始化AnimatedWidget时传入animation对象
));
```

在上面的例子中，在AnimatedLogo的build方法中，我们使用Animation的value作为logo的宽和高。这样做对于简单组件的动画没有任何问题，但如果动画的组件比较复杂，一个更好的解决方案是，**将动画和渲染职责分离**：logo作为外部参数传入，只做显示；而尺寸的变化动画则由另一个类去管理。

这个分离工作，我们可以借助AnimatedBuilder来完成。

与AnimatedWidget类似，AnimatedBuilder也会自动监听Animation对象的变化，并根据需要将该控件树标记为dirty以自动刷新UI。事实上，如果你翻看[源码](https://github.com/flutter/flutter/blob/ca5411e3aa99d571ddd80b75b814718c4a94c839/packages/flutter/lib/src/widgets/transitions.dart#L920)，就会发现AnimatedBuilder其实也是继承自AnimatedWidget。

我们以一个例子来演示如何使用AnimatedBuilder。在这个例子中，AnimatedBuilder的尺寸变化动画由builder函数管理，渲染则由外部传入child参数负责：

```
MaterialApp(
  home: Scaffold(
    body: Center(
      child: AnimatedBuilder(
        animation: animation,//传入动画对象
        child:FlutterLogo(),
        //动画构建回调
        builder: (context, child) => Container(
          width: animation.value,//使用动画的当前状态更新UI
          height: animation.value,
          child: child, //child参数即FlutterLogo()
        )
      )
    )
));
```

可以看到，通过使用AnimatedWidget和AnimatedBuilder，动画的生成和最终的渲染被分离开了，构建动画的工作也被大大简化了。

#### hero动画

现在我们已经知道了如何在一个页面上实现动画效果，那么如何实现在两个页面之间切换的过渡动画呢？比如在社交类App，在Feed流中点击小图进入查看大图页面的场景中，我们希望能够实现小图到大图页面逐步放大的动画切换效果，而当用户关闭大图时，也实现原路返回的动画。

这样的跨页面共享的控件动画效果有一个专门的名词，即“共享元素变换”（Shared Element Transition）。

对于Android开发者来说，这个概念并不陌生。Android原生提供了对这种动画效果的支持，通过几行代码，就可以实现在两个Activity共享的组件之间做出流畅的转场动画。

又比如，Keynote提供了的“神奇移动”（Magic Move）功能，可以实现两个Keynote页面之间的流畅过渡。

Flutter也有类似的概念，即Hero控件。**通过Hero，我们可以在两个页面的共享元素之间，做出流畅的页面切换效果。**

接下来，我们通过一个案例来看看Hero组件具体如何使用。

在下面的例子中，我定义了两个页面，其中page1有一个位于底部的小Flutter Logo，page2有一个位于中部的大Flutter Logo。在点击了page1的小logo后，会使用hero效果过渡到page2。

为了实现共享元素变换，我们需要将这两个组件分别用Hero包裹，并同时为它们设置相同的tag “hero”。然后，为page1添加点击手势响应，在用户点击logo时，跳转到page2：

```
class Page1 extends StatelessWidget {
  Widget build(BuildContext context) {
    return  Scaffold(
      body: GestureDetector(//手势监听点击
        child: Hero(
          tag: 'hero',//设置共享tag
          child: Container(
            width: 100, height: 100,
            child: FlutterLogo())),
        onTap: () {
          Navigator.of(context).push(MaterialPageRoute(builder: (_)=>Page2()));//点击后打开第二个页面
        },
      )
    );
  }
}

class Page2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      body: Hero(
        tag: 'hero',//设置共享tag
        child: Container(
          width: 300, height: 300,
          child: FlutterLogo()
        ))
    );
  }
}
```

运行一下，可以看到，我们通过简单的两步，就可以实现元素跨页面飞行的复杂动画效果了！

![710d38eb87404672bfc763084419c384](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/710d38eb87404672bfc763084419c384.jpg)

图4 Hero动画

#### 总结

好了，今天的分享就到这里。我们简单回顾一下今天的主要内容吧。

在Flutter中，动画的状态与渲染是分离的。我们通过Animation生成动画曲线，使用AnimationController控制动画时间、启动动画。而动画的渲染，则需要设置监听器获取动画进度后，重新触发组件用新的动画状态刷新后才能实现动画的更新。

为了简化这一步骤，Flutter提供了AnimatedWidget和AnimatedBuilder这两个组件，省去了状态监听和UI刷新的工作。而对于跨页面动画，Flutter提供了Hero组件，只要两个相同（相似）的组件有同样的tag，就能实现元素跨页面过渡的转场效果。

可以看到，Flutter对于动画的分层设计还是非常简单清晰的，但造成的副作用就是使用起来稍微麻烦一些。对于实际应用而言，由于动画过程涉及到页面的频繁刷新，因此我强烈建议你尽量使用AnimatedWidget或AnimatedBuilder来缩小受动画影响的组件范围，只重绘需要做动画的组件即可，要避免使用进度监听器直接刷新整个页面，让不需要做动画的组件也跟着一起销毁重建。

我把今天分享中所涉及的针对控件的普通动画，AnimatedBuilder和AnimatedWidget，以及针对页面的过渡动画Hero打包到了[GitHub](https://github.com/cyndibaby905/22_app_animation)上，你可以把工程下载下来，多运行几次，体会这几种动画的具体使用方法。

#### 思考题

最后，我给你留下两个小作业吧。

```
AnimatedBuilder(
  animation: animation,
  child:FlutterLogo(),
  builder: (context, child) => Container(
    width: animation.value,
    height: animation.value,
    child: child
  )
)
```

1. 在AnimatedBuilder的例子中，child似乎被指定了两遍（第3行的child与第7行的child），你可以解释下这么做的原因吗？
2. 如果我把第3行的child删掉，把Flutter Logo放到第7行，动画是否能正常执行？这会有什么问题吗？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 单线程模型怎么保证UI运行流畅？

你好，我是陈航。

在上一篇文章中，我带你一起学习了如何在Flutter中实现动画。对于组件动画，Flutter将动画的状态与渲染进行了分离，因此我们需要使用动画曲线生成器Animation、动画状态控制器AnimationController与动画进度监听器一起配合完成动画更新；而对于跨页面动画，Flutter提供了Hero组件，可以实现共享元素变换的页面切换效果。

在之前的章节里，我们介绍了很多Flutter框架出色的渲染和交互能力。支撑起这些复杂的能力背后，实际上是基于单线程模型的Dart。那么，与原生Android和iOS的多线程机制相比，单线程的Dart如何从语言设计层面和代码运行机制上保证Flutter UI的流畅性呢？

因此今天，我会通过几个小例子，循序渐进地向你介绍Dart语言的Event Loop处理机制、异步处理和并发编程的原理和使用方法，从语言设计和实践层面理解Dart单线程模型下的代码运行本质，从而懂得后续如何在工作中使用Future与Isolate，优化我们的项目。

#### Event Loop机制

首先，我们需要建立这样一个概念，那就是**Dart是单线程的**。那单线程意味着什么呢？这意味着Dart代码是有序的，按照在main函数出现的次序一个接一个地执行，不会被其他代码中断。另外，作为支持Flutter这个UI框架的关键技术，Dart当然也支持异步。需要注意的是，**单线程和异步并不冲突。**

那为什么单线程也可以异步？

这里有一个大前提，那就是我们的App绝大多数时间都在等待。比如，等用户点击、等网络请求返回、等文件IO结果，等等。而这些等待行为并不是阻塞的。比如说，网络请求，Socket本身提供了select模型可以异步查询；而文件IO，操作系统也提供了基于事件的回调机制。

所以，基于这些特点，单线程模型可以在等待的过程中做别的事情，等真正需要响应结果了，再去做对应的处理。因为等待过程并不是阻塞的，所以给我们的感觉就像是同时在做多件事情一样。但其实始终只有一个线程在处理你的事情。

等待这个行为是通过Event Loop驱动的。事件队列Event Queue会把其他平行世界（比如Socket）完成的，需要主线程响应的事件放入其中。像其他语言一样，Dart也有一个巨大的事件循环，在不断的轮询事件队列，取出事件（比如，键盘事件、I\O事件、网络事件等），在主线程同步执行其回调函数，如下图所示：

![04513b698a0d47d08f56d300a4734470](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/04513b698a0d47d08f56d300a4734470.jpg)

图1 简化版Event Loop

#### 异步任务

事实上，图1的Event Loop示意图只是一个简化版。在Dart中，实际上有两个队列，一个事件队列（Event Queue），另一个则是微任务队列（Microtask Queue）。在每一次事件循环中，Dart总是先去第一个微任务队列中查询是否有可执行的任务，如果没有，才会处理后续的事件队列的流程。

所以，Event Loop完整版的流程图，应该如下所示：

![33304a20a498468681f7f557feda6ae1](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/33304a20a498468681f7f557feda6ae1.jpg)

图2 Microtask Queue与Event Queue

接下来，我们分别看一下这两个队列的特点和使用场景吧。

首先，我们看看微任务队列。微任务顾名思义，表示一个短时间内就会完成的异步任务。从上面的流程图可以看到，微任务队列在事件循环中的优先级是最高的，只要队列中还有任务，就可以一直霸占着事件循环。

微任务是由scheduleMicroTask建立的。如下所示，这段代码会在下一个事件循环中输出一段字符串：

```
scheduleMicrotask(() => print('This is a microtask'));
```

不过，一般的异步任务通常也很少必须要在事件队列前完成，所以也不需要太高的优先级，因此我们通常很少会直接用到微任务队列，就连Flutter内部，也只有7处用到了而已（比如，手势识别、文本输入、滚动视图、保存页面效果等需要高优执行任务的场景）。

异步任务我们用的最多的还是优先级更低的Event Queue。比如，I/O、绘制、定时器这些异步事件，都是通过事件队列驱动主线程执行的。

**Dart为Event Queue的任务建立提供了一层封装，叫作Future**。从名字上也很容易理解，它表示一个在未来时间才会完成的任务。

把一个函数体放入Future，就完成了从同步任务到异步任务的包装。Future还提供了链式调用的能力，可以在异步任务执行完毕后依次执行链路上的其他函数体。

接下来，我们看一个具体的代码示例：分别声明两个异步任务，在下一个事件循环中输出一段字符串。其中第二个任务执行完毕之后，还会继续输出另外两段字符串：

```
Future(() => print('Running in Future 1'));//下一个事件循环输出字符串

Future(() => print(‘Running in Future 2'))
  .then((_) => print('and then 1'))
  .then((_) => print('and then 2’));//上一个事件循环结束后，连续输出三段字符串
```

当然，这两个Future异步任务的执行优先级比微任务的优先级要低。

正常情况下，一个Future异步任务的执行是相对简单的：在我们声明一个Future时，Dart会将异步任务的函数执行体放入事件队列，然后立即返回，后续的代码继续同步执行。而当同步执行的代码执行完毕后，事件队列会按照加入事件队列的顺序（即声明顺序），依次取出事件，最后同步执行Future的函数体及后续的then。

这意味着，**then与Future函数体共用一个事件循环**。而如果Future有多个then，它们也会按照链式调用的先后顺序同步执行，同样也会共用一个事件循环。

如果Future执行体已经执行完毕了，但你又拿着这个Future的引用，往里面加了一个then方法体，这时Dart会如何处理呢？面对这种情况，Dart会将后续加入的then方法体放入微任务队列，尽快执行。

下面的代码演示了Future的执行规则，即，先加入事件队列，或者先声明的任务先执行；then在Future结束后立即执行。

- 在第一个例子中，由于f1比f2先声明，因此会被先加入事件队列，所以f1比f2先执行；
- 在第二个例子中，由于Future函数体与then共用一个事件循环，因此f3执行后会立刻同步执行then 3；
- 最后一个例子中，Future函数体是null，这意味着它不需要也没有事件循环，因此后续的then也无法与它共享。在这种场景下，Dart会把后续的then放入微任务队列，在下一次事件循环中执行。

```
//f1比f2先执行
Future(() => print('f1'));
Future(() => print('f2'));

//f3执行后会立刻同步执行then 3
Future(() => print('f3')).then((_) => print('then 3'));

//then 4会加入微任务队列，尽快执行
Future(() => null).then((_) => print('then 4'));
```

说了这么多规则，可能大家并没有完全记住。那我们通过一个综合案例，来把之前介绍的各个执行规则都串起来，再集中学习一下。

在下面的例子中，我们依次声明了若干个异步任务Future，以及微任务。在其中的一些Future内部，我们又内嵌了Future与microtask的声明：

```
Future(() => print('f1'));//声明一个匿名Future
Future fx = Future(() =>  null);//声明Future fx，其执行体为null

//声明一个匿名Future，并注册了两个then。在第一个then回调里启动了一个微任务
Future(() => print('f2')).then((_) {
  print('f3');
  scheduleMicrotask(() => print('f4'));
}).then((_) => print('f5'));

//声明了一个匿名Future，并注册了两个then。第一个then是一个Future
Future(() => print('f6'))
  .then((_) => Future(() => print('f7')))
  .then((_) => print('f8'));

//声明了一个匿名Future
Future(() => print('f9'));

//往执行体为null的fx注册了了一个then
fx.then((_) => print('f10'));

//启动一个微任务
scheduleMicrotask(() => print('f11'));
print('f12');
```

运行一下，上述各个异步任务会依次打印其内部执行结果：

```
f12
f11
f1
f10
f2
f3
f5
f4
f6
f9
f7
f8
```

看到这儿，你可能已经懵了。别急，我们先来看一下这段代码执行过程中，Event Queue与Microtask Queue中的变化情况，依次分析一下它们的执行顺序为什么会是这样的：

![29b382ec91ba4235a1cebabbf3c4e85d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/29b382ec91ba4235a1cebabbf3c4e85d.jpg)

图3 Event Queue与Microtask Queue变化示例

- 因为其他语句都是异步任务，所以先打印f12。
- 剩下的异步任务中，微任务队列优先级最高，因此随后打印f11；然后按照Future声明的先后顺序，打印f1。
- 随后到了fx，由于fx的执行体是null，相当于执行完毕了，Dart将fx的then放入微任务队列，由于微任务队列的优先级最高，因此fx的then还是会最先执行，打印f10。
- 然后到了fx下面的f2，打印f2，然后执行then，打印f3。f4是一个微任务，要到下一个事件循环才执行，因此后续的then继续同步执行，打印f5。本次事件循环结束，下一个事件循环取出f4这个微任务，打印f4。
- 然后到了f2下面的f6，打印f6，然后执行then。这里需要注意的是，这个then是一个Future异步任务，因此这个then，以及后续的then都被放入到事件队列中了。
- f6下面还有f9，打印f9。
- 最后一个事件循环，打印f7，以及后续的f8。

上面的代码很是烧脑，万幸我们平时开发Flutter时一般不会遇到这样奇葩的写法，所以你大可放心。你只需要记住一点：**then会在Future函数体执行完毕后立刻执行，无论是共用同一个事件循环还是进入下一个微任务。**

在深入理解Future异步任务的执行规则之后，我们再来看看怎么封装一个异步函数。

#### 异步函数

对于一个异步函数来说，其返回时内部执行动作并未结束，因此需要返回一个Future对象，供调用者使用。调用者根据Future对象，来决定：是在这个Future对象上注册一个then，等Future的执行体结束了以后再进行异步处理；还是一直同步等待Future执行体结束。

对于异步函数返回的Future对象，如果调用者决定同步等待，则需要在调用处使用await关键字，并且在调用处的函数体使用async关键字。

在下面的例子中，异步方法延迟3秒返回了一个Hello 2019，在调用处我们使用await进行持续等待，等它返回了再打印：

```
//声明了一个延迟3秒返回Hello的Future，并注册了一个then返回拼接后的Hello 2019
Future<String> fetchContent() =>
  Future<String>.delayed(Duration(seconds:3), () => "Hello")
    .then((x) => "$x 2019");

  main() async{
    print(await fetchContent());//等待Hello 2019的返回
  }
```

也许你已经注意到了，我们在使用await进行等待的时候，在等待语句的调用上下文函数main加上了async关键字。为什么要加这个关键字呢？

因为**Dart中的await并不是阻塞等待，而是异步等待**。Dart会将调用体的函数也视作异步函数，将等待语句的上下文放入Event Queue中，一旦有了结果，Event Loop就会把它从Event Queue中取出，等待代码继续执行。

接下来，为了帮助你加深印象，我准备了两个具体的案例。

我们先来看下这段代码。第二行的then执行体f2是一个Future，为了等它完成再进行下一步操作，我们使用了await，期望打印结果为f1、f2、f3、f4：

```
Future(() => print('f1'))
  .then((_) async => await Future(() => print('f2')))
  .then((_) => print('f3'));
Future(() => print('f4'));
```

实际上，当你运行这段代码时就会发现，打印出来的结果其实是f1、f4、f2、f3！

我来给你分析一下这段代码的执行顺序：

- 按照任务的声明顺序，f1和f4被先后加入事件队列。
- f1被取出并打印；然后到了then。then的执行体是个future f2，于是放入Event Queue。然后把await也放到Event Queue里。
- 这个时候要注意了，Event Queue里面还有一个f4，我们的await并不能阻塞f4的执行。因此，Event Loop先取出f4，打印f4；然后才能取出并打印f2，最后把等待的await取出，开始执行后面的f3。

由于await是采用事件队列的机制实现等待行为的，所以比它先在事件队列中的f4并不会被它阻塞。

接下来，我们再看另一个例子：在主函数调用一个异步函数去打印一段话，而在这个异步函数中，我们使用await与async同步等待了另一个异步函数返回字符串：

```
//声明了一个延迟2秒返回Hello的Future，并注册了一个then返回拼接后的Hello 2019
Future<String> fetchContent() =>
  Future<String>.delayed(Duration(seconds:2), () => "Hello")
    .then((x) => "$x 2019");
//异步函数会同步等待Hello 2019的返回，并打印
func() async => print(await fetchContent());

main() {
  print("func before");
  func();
  print("func after");
}
```

运行这段代码，我们发现最终输出的顺序其实是“func before”“func after”“Hello 2019”。func函数中的等待语句似乎没起作用。这是为什么呢？

同样，我来给你分析一下这段代码的执行顺序：

- 首先，第一句代码是同步的，因此先打印“func before”。
- 然后，进入func函数，func函数调用了异步函数fetchContent，并使用await进行等待，因此我们把fetchContent、await语句的上下文函数func先后放入事件队列。
- await的上下文函数并不包含调用栈，因此func后续代码继续执行，打印“func after”。
- 2秒后，fetchContent异步任务返回“Hello 2019”，于是func的await也被取出，打印“Hello 2019”。

通过上述分析，你发现了什么现象？那就是await与async只对调用上下文的函数有效，并不向上传递。因此对于这个案例而言，func是在异步等待。如果我们想在main函数中也同步等待，需要在调用异步函数时也加上await，在main函数也加上async。

经过上面两个例子的分析，你应该已经明白await与async是如何配合，完成等待工作的了吧。

介绍完了异步，我们再来看在Dart中，如何通过多线程实现并发。

#### Isolate

尽管Dart是基于单线程模型的，但为了进一步利用多核CPU，将CPU密集型运算进行隔离，Dart也提供了多线程机制，即Isolate。在Isolate中，资源隔离做得非常好，每个Isolate都有自己的Event Loop与Queue，**Isolate之间不共享任何资源，只能依靠消息机制通信，因此也就没有资源抢占问题**。

和其他语言一样，Isolate的创建非常简单，我们只要给定一个函数入口，创建时再传入一个参数，就可以启动Isolate了。如下所示，我们声明了一个Isolate的入口函数，然后在main函数中启动它，并传入了一个字符串参数：

```
doSth(msg) => print(msg);

main() {
  Isolate.spawn(doSth, "Hi");
  ...
}
```

但更多情况下，我们的需求并不会这么简单，不仅希望能并发，还希望Isolate在并发执行的时候告知主Isolate当前的执行结果。

对于执行结果的告知，Isolate通过发送管道（SendPort）实现消息通信机制。我们可以在启动并发Isolate时将主Isolate的发送管道作为参数传给它，这样并发Isolate就可以在任务执行完毕后利用这个发送管道给我们发消息了。

下面我们通过一个例子来说明：在主Isolate里，我们创建了一个并发Isolate，在函数入口传入了主Isolate的发送管道，然后等待并发Isolate的回传消息。在并发Isolate中，我们用这个管道给主Isolate发了一个Hello字符串：

```
Isolate isolate;

start() async {
  ReceivePort receivePort= ReceivePort();//创建管道
  //创建并发Isolate，并传入发送管道
  isolate = await Isolate.spawn(getMsg, receivePort.sendPort);
  //监听管道消息
  receivePort.listen((data) {
    print('Data：$data');
    receivePort.close();//关闭管道
    isolate?.kill(priority: Isolate.immediate);//杀死并发Isolate
    isolate = null;
  });
}
//并发Isolate往管道发送一个字符串
getMsg(sendPort) => sendPort.send("Hello");
```

这里需要注意的是，在Isolate中，发送管道是单向的：我们启动了一个Isolate执行某项任务，Isolate执行完毕后，发送消息告知我们。如果Isolate执行任务时，需要依赖主Isolate给它发送参数，执行完毕后再发送执行结果给主Isolate，这样**双向通信的场景我们如何实现呢**？答案也很简单，让并发Isolate也回传一个发送管道即可。

接下来，我们以一个**并发计算阶乘**的例子来说明如何实现双向通信。

在下面的例子中，我们创建了一个异步函数计算阶乘。在这个异步函数内，创建了一个并发Isolate，传入主Isolate的发送管道；并发Isolate也回传一个发送管道；主Isolate收到回传管道后，发送参数N给并发Isolate，然后立即返回一个Future；并发Isolate用参数N，调用同步计算阶乘的函数，返回执行结果；最后，主Isolate打印了返回结果：

```
//并发计算阶乘
Future<dynamic> asyncFactoriali(n) async{
  final response = ReceivePort();//创建管道
  //创建并发Isolate，并传入管道
  await Isolate.spawn(_isolate,response.sendPort);
  //等待Isolate回传管道
  final sendPort = await response.first as SendPort;
  //创建了另一个管道answer
  final answer = ReceivePort();
  //往Isolate回传的管道中发送参数，同时传入answer管道
  sendPort.send([n,answer.sendPort]);
  return answer.first;//等待Isolate通过answer管道回传执行结果
}

//Isolate函数体，参数是主Isolate传入的管道
_isolate(initialReplyTo) async {
  final port = ReceivePort();//创建管道
  initialReplyTo.send(port.sendPort);//往主Isolate回传管道
  final message = await port.first as List;//等待主Isolate发送消息(参数和回传结果的管道)
  final data = message[0] as int;//参数
  final send = message[1] as SendPort;//回传结果的管道
  send.send(syncFactorial(data));//调用同步计算阶乘的函数回传结果
}

//同步计算阶乘
int syncFactorial(n) => n < 2 ? n : n * syncFactorial(n-1);
main() async => print(await asyncFactoriali(4));//等待并发计算阶乘结果
```

看完这段代码你是什么感觉呢？我们只是为了并发计算一个阶乘，这样是不是太繁琐了？

没错，确实太繁琐了。在Flutter中，像这样执行并发计算任务我们可以采用更简单的方式。Flutter提供了支持并发计算的compute函数，其内部对Isolate的创建和双向通信进行了封装抽象，屏蔽了很多底层细节，我们在调用时只需要传入函数入口和函数参数，就能够实现并发计算和消息通知。

我们试着用compute函数改造一下并发计算阶乘的代码：

```
//同步计算阶乘
int syncFactorial(n) => n < 2 ? n : n * syncFactorial(n-1);
//使用compute函数封装Isolate的创建和结果的返回
main() async => print(await compute(syncFactorial, 4));
```

可以看到，用compute函数改造以后，整个代码就变成了两行，现在并发计算阶乘的代码看起来就清爽多了。

#### 总结

好了，今天关于Dart的异步与并发机制、实现原理的分享就到这里了，我们来简单回顾一下主要内容。

Dart是单线程的，但通过事件循环可以实现异步。而Future是异步任务的封装，借助于await与async，我们可以通过事件循环实现非阻塞的同步等待；Isolate是Dart中的多线程，可以实现并发，有自己的事件循环与Queue，独占资源。Isolate之间可以通过消息机制进行单向通信，这些传递的消息通过对方的事件循环驱动对方进行异步处理。

在UI编程过程中，异步和多线程是两个相伴相生的名词，也是很容易混淆的概念。对于异步方法调用而言，代码不需要等待结果的返回，而是通过其他手段（比如通知、回调、事件循环或多线程）在后续的某个时刻主动（或被动）地接收执行结果。

因此，从辩证关系上来看，异步与多线程并不是一个同等关系：异步是目的，多线程只是我们实现异步的一个手段之一。而在Flutter中，借助于UI框架提供的事件循环，我们可以不用阻塞的同时等待多个异步任务，因此并不需要开多线程。我们一定要记住这一点。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/23_dart_async)中，你可以下载下来，反复运行几次，加深理解。

#### 思考题

最后，我给你留下两道思考题吧。

1. 在通过并发Isolate计算阶乘的例子中，我在asyncFactoriali方法里先后发给了并发Isolate两个SendPort。你能否解释下这么做的原因？可以只发一个SendPort吗？
2. 请改造以下代码，在不改变整体异步结构的情况下，实现输出结果为f1、f2、f3、f4。

```
Future(() => print('f1'))
  .then((_) async => await Future(() => print('f2')))
  .then((_) => print('f3'));
Future(() => print('f4'));
```

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### HTTP网络编程与JSON解析

你好，我是陈航。

在上一篇文章中，我带你一起学习了Dart中异步与并发的机制及实现原理。与其他语言类似，Dart的异步是通过事件循环与队列实现的，我们可以使用Future来封装异步任务。而另一方面，尽管Dart是基于单线程模型的，但也提供了Isolate这样的“多线程”能力，这使得我们可以充分利用系统资源，在并发Isolate中搞定CPU密集型的任务，并通过消息机制通知主Isolate运行结果。

异步与并发的一个典型应用场景，就是网络编程。一个好的移动应用，不仅需要有良好的界面和易用的交互体验，也需要具备和外界进行信息交互的能力。而通过网络，信息隔离的客户端与服务端间可以建立一个双向的通信通道，从而实现资源访问、接口数据请求和提交、上传下载文件等操作。

为了便于我们快速实现基于网络通道的信息交换实时更新App数据，Flutter也提供了一系列的网络编程类库和工具。因此在今天的分享中，我会通过一些小例子与你讲述在Flutter应用中，如何实现与服务端的数据交互，以及如何将交互响应的数据格式化。

#### Http网络编程

我们在通过网络与服务端数据交互时，不可避免地需要用到三个概念：定位、传输与应用。

其中，**定位**，定义了如何准确地找到网络上的一台或者多台主机（即IP地址）；**传输**，则主要负责在找到主机后如何高效且可靠地进行数据通信（即TCP、UDP协议）；而**应用**，则负责识别双方通信的内容（即HTTP协议）。

我们在进行数据通信时，可以只使用传输层协议。但传输层传递的数据是二进制流，如果没有应用层，我们无法识别数据内容。如果想要使传输的数据有意义，则必须要用到应用层协议。移动应用通常使用HTTP协议作应用层协议，来封装HTTP信息。

在编程框架中，一次HTTP网络调用通常可以拆解为以下步骤：

1. 创建网络调用实例client，设置通用请求行为（如超时时间）；
2. 构造URI，设置请求header、body；
3. 发起请求, 等待响应；
4. 解码响应的内容。

当然，Flutter也不例外。在Flutter中，Http网络编程的实现方式主要分为三种：dart:io里的HttpClient实现、Dart原生http请求库实现、第三方库dio实现。接下来，我依次为你讲解这三种方式。

##### HttpClient

HttpClient是dart:io库中提供的网络请求类，实现了基本的网络编程功能。

接下来，我将和你分享一个实例，对照着上面提到的网络调用步骤，来演示HttpClient如何使用。

在下面的代码中，我们创建了一个HttpClien网络调用实例，设置了其超时时间为5秒。随后构造了Flutter官网的URI，并设置了请求Header的user-agent为Custom-UA。然后发起请求，等待Flutter官网响应。最后在收到响应后，打印出返回结果：

```
get() async {
  //创建网络调用示例，设置通用请求行为(超时时间)
  var httpClient = HttpClient();
  httpClient.idleTimeout = Duration(seconds: 5);

  //构造URI，设置user-agent为"Custom-UA"
  var uri = Uri.parse("https://flutter.dev");
  var request = await httpClient.getUrl(uri);
  request.headers.add("user-agent", "Custom-UA");

  //发起请求，等待响应
  var response = await request.close();

  //收到响应，打印结果
  if (response.statusCode == HttpStatus.ok) {
    print(await response.transform(utf8.decoder).join());
  } else {
    print('Error: \nHttp status ${response.statusCode}');
  }
}
```

可以看到，使用HttpClient来发起网络调用还是相对比较简单的。

这里需要注意的是，由于网络请求是异步行为，因此**在Flutter中，所有网络编程框架都是以Future作为异步请求的包装**，所以我们需要使用await与async进行非阻塞的等待。当然，你也可以注册then，以回调的方式进行相应的事件处理。

##### http

HttpClient使用方式虽然简单，但其接口却暴露了不少内部实现细节。比如，异步调用拆分得过细，链接需要调用方主动关闭，请求结果是字符串但却需要手动解码等。

http是Dart官方提供的另一个网络请求类，相比于HttpClient，易用性提升了不少。同样，我们以一个例子来介绍http的使用方法。

首先，我们需要将http加入到pubspec中的依赖里：

```
dependencies:
  http: '>=0.11.3+12'
```

在下面的代码中，与HttpClient的例子类似的，我们也是先后构造了http网络调用实例和Flutter官网URI，在设置user-agent为Custom-UA后，发出请求，最后打印请求结果：

```
httpGet() async {
  //创建网络调用示例
  var client = http.Client();

  //构造URI
  var uri = Uri.parse("https://flutter.dev");

  //设置user-agent为"Custom-UA"，随后立即发出请求
  http.Response response = await client.get(uri, headers : {"user-agent" : "Custom-UA"});

  //打印请求结果
  if(response.statusCode == HttpStatus.ok) {
    print(response.body);
  } else {
    print("Error: ${response.statusCode}");
  }
}
```

可以看到，相比于HttpClient，http的使用方式更加简单，仅需一次异步调用就可以实现基本的网络通信。

##### dio

HttpClient和http使用方式虽然简单，但其暴露的定制化能力都相对较弱，很多常用的功能都不支持（或者实现异常繁琐），比如取消请求、定制拦截器、Cookie管理等。因此对于复杂的网络请求行为，我推荐使用目前在Dart社区人气较高的第三方dio来发起网络请求。

接下来，我通过几个例子来和你介绍dio的使用方法。与http类似的，我们首先需要把dio加到pubspec中的依赖里：

```
dependencies:
  dio: '>2.1.3'
```

在下面的代码中，与前面HttpClient与http例子类似的，我们也是先后创建了dio网络调用实例、创建URI、设置Header、发出请求，最后等待请求结果：

```
void getRequest() async {
  //创建网络调用示例
  Dio dio = new Dio();

  //设置URI及请求user-agent后发起请求
  var response = await dio.get("https://flutter.dev", options:Options(headers: {"user-agent" : "Custom-UA"}));

 //打印请求结果
  if(response.statusCode == HttpStatus.ok) {
    print(response.data.toString());
  } else {
    print("Error: ${response.statusCode}");
  }
}
```

> 这里需要注意的是，创建URI、设置Header及发出请求的行为，都是通过dio.get方法实现的。这个方法的options参数提供了精细化控制网络请求的能力，可以支持设置Header、超时时间、Cookie、请求方法等。这部分内容不是今天分享的重点，如果你想深入理解的话，可以访问其[API文档](https://github.com/flutterchina/dio#dio-apis)学习具体使用方法。

对于常见的上传及下载文件需求，dio也提供了良好的支持：文件上传可以通过构建表单FormData实现，而文件下载则可以使用download方法搞定。

在下面的代码中，我们通过FormData创建了两个待上传的文件，通过post方法发送至服务端。download的使用方法则更为简单，我们直接在请求参数中，把待下载的文件地址和本地文件名提供给dio即可。如果我们需要感知下载进度，可以增加onReceiveProgress回调函数：

```
//使用FormData表单构建待上传文件
FormData formData = FormData.from({
  "file1": UploadFileInfo(File("./file1.txt"), "file1.txt"),
  "file2": UploadFileInfo(File("./file2.txt"), "file1.txt"),

});
//通过post方法发送至服务端
var responseY = await dio.post("https://xxx.com/upload", data: formData);
print(responseY.toString());

//使用download方法下载文件
dio.download("https://xxx.com/file1", "xx1.zip");

//增加下载进度回调函数
dio.download("https://xxx.com/file1", "xx2.zip", onReceiveProgress: (count, total) {
	//do something
});
```

有时，我们的页面由多个并行的请求响应结果构成，这就需要等待这些请求都返回后才能刷新界面。在dio中，我们可以结合Future.wait方法轻松实现：

```
//同时发起两个并行请求
List<Response> responseX= await Future.wait([dio.get("https://flutter.dev"),dio.get("https://pub.dev/packages/dio")]);

//打印请求1响应结果
print("Response1: ${responseX[0].toString()}");
//打印请求2响应结果
print("Response2: ${responseX[1].toString()}");
```

此外，与Android的okHttp一样，dio还提供了请求拦截器，通过拦截器，我们可以在请求之前，或响应之后做一些特殊的操作。比如可以为请求option统一增加一个header，或是返回缓存数据，或是增加本地校验处理等等。

在下面的例子中，我们为dio增加了一个拦截器。在请求发送之前，不仅为每个请求头都加上了自定义的user-agent，还实现了基本的token认证信息检查功能。而对于本地已经缓存了请求uri资源的场景，我们可以直接返回缓存数据，避免再次下载：

```
//增加拦截器
dio.interceptors.add(InterceptorsWrapper(
    onRequest: (RequestOptions options){
      //为每个请求头都增加user-agent
      options.headers["user-agent"] = "Custom-UA";
      //检查是否有token，没有则直接报错
      if(options.headers['token'] == null) {
        return dio.reject("Error:请先登录");
      }
      //检查缓存是否有数据
      if(options.uri == Uri.parse('http://xxx.com/file1')) {
        return dio.resolve("返回缓存数据");
      }
      //放行请求
      return options;
    }
));

//增加try catch，防止请求报错
try {
  var response = await dio.get("https://xxx.com/xxx.zip");
  print(response.data.toString());
}catch(e) {
  print(e);
}
```

需要注意的是，由于网络通信期间有可能会出现异常（比如，域名无法解析、超时等），因此我们需要使用try-catch来捕获这些未知错误，防止程序出现异常。

除了这些基本的用法，dio还支持请求取消、设置代理，证书校验等功能。不过，这些高级特性不属于本次分享的重点，故不再赘述，详情可以参考dio的[GitHub主页](https://github.com/flutterchina/dio/blob/master/README-ZH.md)了解具体用法。

#### JSON解析

移动应用与Web服务器建立好了连接之后，接下来的两个重要工作分别是：服务器如何结构化地去描述返回的通信信息，以及移动应用如何解析这些格式化的信息。

##### 如何结构化地描述返回的通信信息？

在如何结构化地去表达信息上，我们需要用到JSON。JSON是一种轻量级的、用于表达由属性值和字面量组成对象的数据交换语言。

一个简单的表示学生成绩的JSON结构，如下所示：

```
String jsonString = '''
{
  "id":"123",
  "name":"张三",
  "score" : 95
}
''';
```

需要注意的是，由于Flutter不支持运行时反射，因此并没有提供像Gson、Mantle这样自动解析JSON的库来降低解析成本。在Flutter中，JSON解析完全是手动的，开发者要做的事情多了一些，但使用起来倒也相对灵活。

接下来，我们就看看Flutter应用是如何解析这些格式化的信息。

##### 如何解析格式化的信息？

所谓手动解析，是指使用dart:convert库中内置的JSON解码器，将JSON字符串解析成自定义对象的过程。使用这种方式，我们需要先将JSON字符串传递给JSON.decode方法解析成一个Map，然后把这个Map传给自定义的类，进行相关属性的赋值。

以上面表示学生成绩的JSON结构为例，我来和你演示手动解析的使用方法。

首先，我们根据JSON结构定义Student类，并创建一个工厂类，来处理Student类属性成员与JSON字典对象的值之间的映射关系：

```
class Student{
  //属性id，名字与成绩
  String id;
  String name;
  int score;
  //构造方法
  Student({
    this.id,
    this.name,
    this.score
  });
  //JSON解析工厂类，使用字典数据为对象初始化赋值
  factory Student.fromJson(Map<String, dynamic> parsedJson){
    return Student(
        id: parsedJson['id'],
        name : parsedJson['name'],
        score : parsedJson ['score']
    );
  }
}
```

数据解析类创建好了，剩下的事情就相对简单了，我们只需要把JSON文本通过JSON.decode方法转换成Map，然后把它交给Student的工厂类fromJson方法，即可完成Student对象的解析：

```
loadStudent() {
  //jsonString为JSON文本
  final jsonResponse = json.decode(jsonString);
  Student student = Student.fromJson(jsonResponse);
  print(student.name);
}
```

在上面的例子中，JSON文本所有的属性都是基本类型，因此我们直接从JSON字典取出相应的元素为对象赋值即可。而如果JSON下面还有嵌套对象属性，比如下面的例子中，Student还有一个teacher的属性，我们又该如何解析呢？

```
String jsonString = '''
{
  "id":"123",
  "name":"张三",
  "score" : 95,
  "teacher": {
    "name": "李四",
    "age" : 40
  }
}
''';
```

这里，teacher不再是一个基本类型，而是一个对象。面对这种情况，我们需要为每一个非基本类型属性创建一个解析类。与Student类似，我们也需要为它的属性teacher创建一个解析类Teacher：

```
class Teacher {
  //Teacher的名字与年龄
  String name;
  int age;
  //构造方法
  Teacher({this.name,this.age});
  //JSON解析工厂类，使用字典数据为对象初始化赋值
  factory Teacher.fromJson(Map<String, dynamic> parsedJson){
    return Teacher(
        name : parsedJson['name'],
        age : parsedJson ['age']
    );
  }
}
```

然后，我们只需要在Student类中，增加teacher属性及对应的JSON映射规则即可：

```
class Student{
  ...
  //增加teacher属性
  Teacher teacher;
  //构造函数增加teacher
  Student({
    ...
    this.teacher
  });
  factory Student.fromJson(Map<String, dynamic> parsedJson){
    return Student(
        ...
        //增加映射规则
        teacher: Teacher.fromJson(parsedJson ['teacher'])
    );
  }
}
```

完成了teacher属性的映射规则添加之后，我们就可以继续使用Student来解析上述的JSON文本了：

```
final jsonResponse = json.decode(jsonString);//将字符串解码成Map对象
Student student = Student.fromJson(jsonResponse);//手动解析
print(student.teacher.name);
```

可以看到，通过这种方法，无论对象有多复杂的非基本类型属性，我们都可以创建对应的解析类进行处理。

不过到现在为止，我们的JSON数据解析还是在主Isolate中完成。如果JSON的数据格式比较复杂，数据量又大，这种解析方式可能会造成短期UI无法响应。对于这类CPU密集型的操作，我们可以使用上一篇文章中提到的compute函数，将解析工作放到新的Isolate中完成：

```
static Student parseStudent(String content) {
  final jsonResponse = json.decode(content);
  Student student = Student.fromJson(jsonResponse);
  return student;
}
doSth() {
 ...
 //用compute函数将json解析放到新Isolate
 compute(parseStudent,jsonString).then((student)=>print(student.teacher.name));
}
```

通过compute的改造，我们就不用担心JSON解析时间过长阻塞UI响应了。

#### 总结

好了，今天的分享就到这里了，我们简单回顾一下主要内容。

首先，我带你学习了实现Flutter应用与服务端通信的三种方式，即HttpClient、http与dio。其中dio提供的功能更为强大，可以支持请求拦截、文件上传下载、请求合并等高级能力。因此，我推荐你在实际项目中使用dio的方式。

然后，我和你分享了JSON解析的相关内容。JSON解析在Flutter中相对比较简单，但由于不支持反射，所以我们只能手动解析，即：先将JSON字符串转换成Map，然后再把这个Map给到自定义类，进行相关属性的赋值。

如果你有原生Android、iOS开发经验的话，可能会觉得Flutter提供的JSON手动解析方案并不好用。在Flutter中，没有像原生开发那样提供了Gson或Mantle等库，用于将JSON字符串直接转换为对应的实体类。而这些能力无一例外都需要用到运行时反射，这是Flutter从设计之初就不支持的，理由如下：

1. 运行时反射破坏了类的封装性和安全性，会带来安全风险。就在前段时间，Fastjson框架就爆出了一个巨大的安全漏洞。这个漏洞使得精心构造的字符串文本，可以在反序列化时让服务器执行任意代码，直接导致业务机器被远程控制、内网渗透、窃取敏感信息等操作。
2. 运行时反射会增加二进制文件大小。因为搞不清楚哪些代码可能会在运行时用到，因此使用反射后，会默认使用所有代码构建应用程序，这就导致编译器无法优化编译期间未使用的代码，应用安装包体积无法进一步压缩，这对于自带Dart虚拟机的Flutter应用程序是难以接受的。

反射给开发者编程带来了方便，但也带来了很多难以解决的新问题，因此Flutter并不支持反射。而我们要做的就是，老老实实地手动解析JSON吧。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/24_network_demo)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留两道思考题吧。

1. 请使用dio实现一个自定义拦截器，拦截器内检查header中的token：如果没有token，需要暂停本次请求，同时访问”[http://xxxx.com/token](http://xxxx.com/token)“，在获取新token后继续本次请求。
2. 为以下Student JSON写相应的解析类：

```
String jsonString = '''
  {
    "id":"123",
    "name":"张三",
    "score" : 95,
    "teachers": [
       {
         "name": "李四",
         "age" : 40
       },
       {
         "name": "王五",
         "age" : 45
       }
    ]
  }
  ''';
```

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 本地存储与数据库的使用和优化

你好，我是陈航。

在上一篇文章中，我带你一起学习了Flutter的网络编程，即如何建立与Web服务器的通信连接，以实现数据交换，以及如何解析结构化后的通信信息。

其中，建立通信连接在Flutter中有三种基本方案，包括HttpClient、http与dio。考虑到HttpClient与http并不支持复杂的网络请求行为，因此我重点介绍了如何使用dio实现资源访问、接口数据请求与提交、上传及下载文件、网络拦截等高级操作。

而关于如何解析信息，由于Flutter并不支持反射，因此只提供了手动解析JSON的方式：把JSON转换成字典，然后给自定义的类属性赋值即可。

正因为有了网络，我们的App拥有了与外界进行信息交换的通道，也因此具备了更新数据的能力。不过，经过交换后的数据通常都保存在内存中，而应用一旦运行结束，内存就会被释放，这些数据也就随之消失了。

因此，我们需要把这些更新后的数据以一定的形式，通过一定的载体保存起来，这样应用下次运行时，就可以把数据从存储的载体中读出来，也就实现了**数据的持久化**。

数据持久化的应用场景有很多。比如，用户的账号登录信息需要保存，用于每次与Web服务验证身份；又比如，下载后的图片需要缓存，避免每次都要重新加载，浪费用户流量。

由于Flutter仅接管了渲染层，真正涉及到存储等操作系统底层行为时，还需要依托于原生Android、iOS，因此与原生开发类似的，根据需要持久化数据的大小和方式不同，Flutter提供了三种数据持久化方法，即文件、SharedPreferences与数据库。接下来，我将与你详细讲述这三种方式。

#### 文件

文件是存储在某种介质（比如磁盘）上指定路径的、具有文件名的一组有序信息的集合。从其定义看，要想以文件的方式实现数据持久化，我们首先需要确定一件事儿：数据放在哪儿？这，就意味着要定义文件的存储路径。

Flutter提供了两种文件存储的目录，即**临时（Temporary）目录与文档（Documents）目录**：

- 临时目录是操作系统可以随时清除的目录，通常被用来存放一些不重要的临时缓存数据。这个目录在iOS上对应着NSTemporaryDirectory返回的值，而在Android上则对应着getCacheDir返回的值。
- 文档目录则是只有在删除应用程序时才会被清除的目录，通常被用来存放应用产生的重要数据文件。在iOS上，这个目录对应着NSDocumentDirectory，而在Android上则对应着AppData目录。

接下来，我通过一个例子与你演示如何在Flutter中实现文件读写。

在下面的代码中，我分别声明了三个函数，即创建文件目录函数、写文件函数与读文件函数。这里需要注意的是，由于文件读写是非常耗时的操作，所以这些操作都需要在异步环境下进行。另外，为了防止文件读取过程中出现异常，我们也需要在外层包上try-catch：

```
//创建文件目录
Future<File> get _localFile async {
  final directory = await getApplicationDocumentsDirectory();
  final path = directory.path;
  return File('$path/content.txt');
}
//将字符串写入文件
Future<File> writeContent(String content) async {
  final file = await _localFile;
  return file.writeAsString(content);
}
//从文件读出字符串
Future<String> readContent() async {
  try {
    final file = await _localFile;
    String contents = await file.readAsString();
    return contents;
  } catch (e) {
    return "";
  }
}
```

有了文件读写函数，我们就可以在代码中对content.txt这个文件进行读写操作了。在下面的代码中，我们往这个文件写入了一段字符串后，隔了一会又把它读了出来：

```
writeContent("Hello World!");
...
readContent().then((value)=>print(value));
```

除了字符串读写之外，Flutter还提供了二进制流的读写能力，可以支持图片、压缩包等二进制文件的读写。这些内容不是本次分享的重点，如果你想要深入研究的话，可以查阅[官方文档](https://api.flutter.dev/flutter/dart-io/File-class.html)。

#### SharedPreferences

文件比较适合大量的、有序的数据持久化，如果我们只是需要缓存少量的键值对信息（比如记录用户是否阅读了公告，或是简单的计数），则可以使用SharedPreferences。

SharedPreferences会以原生平台相关的机制，为简单的键值对数据提供持久化存储，即在iOS上使用NSUserDefaults，在Android使用SharedPreferences。

接下来，我通过一个例子来演示在Flutter中如何通过SharedPreferences实现数据的读写。在下面的代码中，我们将计数器持久化到了SharedPreferences中，并为它分别提供了读方法和递增写入的方法。

这里需要注意的是，setter（setInt）方法会同步更新内存中的键值对，然后将数据保存至磁盘，因此我们无需再调用更新方法强制刷新缓存。同样地，由于涉及到耗时的文件读写，因此我们必须以异步的方式对这些操作进行包装：

```
//读取SharedPreferences中key为counter的值
Future<int>_loadCounter() async {
  SharedPreferences prefs = await SharedPreferences.getInstance();
  int  counter = (prefs.getInt('counter') ?? 0);
  return counter;
}

//递增写入SharedPreferences中key为counter的值
Future<void>_incrementCounter() async {
  SharedPreferences prefs = await SharedPreferences.getInstance();
    int counter = (prefs.getInt('counter') ?? 0) + 1;
    prefs.setInt('counter', counter);
}
```

在完成了计数器存取方法的封装后，我们就可以在代码中随时更新并持久化计数器数据了。在下面的代码中，我们先是读取并打印了计数器数据，随后将其递增，并再次把它读取打印：

```
//读出counter数据并打印
_loadCounter().then((value)=>print("before:$value"));

//递增counter数据后，再次读出并打印
_incrementCounter().then((_) {
  _loadCounter().then((value)=>print("after:$value"));
});
```

可以看到，SharedPreferences的使用方式非常简单方便。不过需要注意的是，以键值对的方式只能存储基本类型的数据，比如int、double、bool和string。

#### 数据库

SharedPrefernces的使用固然方便，但这种方式只适用于持久化少量数据的场景，我们并不能用它来存储大量数据，比如文件内容（文件路径是可以的）。

如果我们需要持久化大量格式化后的数据，并且这些数据还会以较高的频率更新，为了考虑进一步的扩展性，我们通常会选用sqlite数据库来应对这样的场景。与文件和SharedPreferences相比，数据库在数据读写上可以提供更快、更灵活的解决方案。

接下来，我就以一个例子分别与你介绍数据库的使用方法。

我们以上一篇文章中提到的Student类为例：

```
class Student{
  String id;
  String name;
  int score;
  //构造方法
  Student({this.id, this.name, this.score,});
  //用于将JSON字典转换成类对象的工厂类方法
  factory Student.fromJson(Map<String, dynamic> parsedJson){
    return Student(
      id: parsedJson['id'],
      name : parsedJson['name'],
      score : parsedJson ['score'],
    );
  }
}
```

JSON类拥有一个可以将JSON字典转换成类对象的工厂类方法，我们也可以提供将类对象反过来转换成JSON字典的实例方法。因为最终存入数据库的并不是实体类对象，而是字符串、整型等基本类型组成的字典，所以我们可以通过这两个方法，实现数据库的读写。同时，我们还分别定义了3个Student对象，用于后续插入数据库：

```
class Student{
  ...
  //将类对象转换成JSON字典，方便插入数据库
  Map<String, dynamic> toJson() {
    return {'id': id, 'name': name, 'score': score,};
  }
}

var student1 = Student(id: '123', name: '张三', score: 90);
var student2 = Student(id: '456', name: '李四', score: 80);
var student3 = Student(id: '789', name: '王五', score: 85);
```

有了实体类作为数据库存储的对象，接下来就需要创建数据库了。在下面的代码中，我们通过openDatabase函数，给定了一个数据库存储地址，并通过数据库表初始化语句，创建了一个用于存放Student对象的students表：

```
final Future<Database> database = openDatabase(
  join(await getDatabasesPath(), 'students_database.db'),
  onCreate: (db, version)=>db.execute("CREATE TABLE students(id TEXT PRIMARY KEY, name TEXT, score INTEGER)"),
  onUpgrade: (db, oldVersion, newVersion){
     //dosth for migration
  },
  version: 1,
);
```

以上代码属于通用的数据库创建模板，有三个地方需要注意：

1. 在设定数据库存储地址时，使用join方法对两段地址进行拼接。join方法在拼接时会使用操作系统的路径分隔符，这样我们就无需关心路径分隔符究竟是“/”还是“\”了。
2. 创建数据库时，传入了一个version 1，在onCreate方法的回调里面也有一个version。这两个version是相等的。
3. 数据库只会创建一次，也就意味着onCreate方法在应用从安装到卸载的生命周期中只会执行一次。如果我们在版本升级过程中，想对数据库的存储字段进行改动又该如何处理呢？- sqlite提供了onUpgrade方法，我们可以根据这个方法传入的oldVersion和newVersion确定升级策略。其中，前者代表用户手机上的数据库版本，而后者代表当前版本的数据库版本。比如，我们的应用有1.0、1.1和1.2三个版本，在1.1把数据库version升级到了2。考虑到用户的升级顺序并不总是连续的，可能会直接从1.0升级到1.2，因此我们可以在onUpgrade函数中，对数据库当前版本和用户手机上的数据库版本进行比较，制定数据库升级方案。

数据库创建好了之后，接下来我们就可以把之前创建的3个Student对象插入到数据库中了。数据库的插入需要调用insert方法，在下面的代码中，我们将Student对象转换成了JSON，在指定了插入冲突策略（如果同样的对象被插入两次，则后者替换前者）和目标数据库表后，完成了Student对象的插入：

```
Future<void> insertStudent(Student std) async {
  final Database db = await database;
  await db.insert(
    'students',
    std.toJson(),
    //插入冲突策略，新的替换旧的
    conflictAlgorithm: ConflictAlgorithm.replace,
  );
}
//插入3个Student对象
await insertStudent(student1);
await insertStudent(student2);
await insertStudent(student3);
```

数据完成插入之后，接下来我们就可以调用query方法把它们取出来了。需要注意的是，写入的时候我们是一个接一个地有序插入，读的时候我们则采用批量读的方式（当然也可以指定查询规则读特定对象）。读出来的数据是一个JSON字典数组，因此我们还需要把它转换成Student数组。最后，别忘了把数据库资源释放掉：

```
Future<List<Student>> students() async {
  final Database db = await database;
  final List<Map<String, dynamic>> maps = await db.query('students');
  return List.generate(maps.length, (i)=>Student.fromJson(maps[i]));
}

//读取出数据库中插入的Student对象集合
students().then((list)=>list.forEach((s)=>print(s.name)));
//释放数据库资源
final Database db = await database;
db.close();
```

可以看到，在面对大量格式化的数据模型读取时，数据库提供了更快、更灵活的持久化解决方案。

除了基础的数据库读写操作之外，sqlite还提供了更新、删除以及事务等高级特性，这与原生Android、iOS上的SQLite或是MySQL并无不同，因此这里就不再赘述了。你可以参考sqflite插件的[API文档](https://pub.dev/documentation/sqflite/latest/)，或是查阅[SQLite教程](http://www.sqlitetutorial.net/)了解具体的使用方法。

#### 总结

好了，今天的分享就这里。我们简单回顾下今天学习的内容吧。

首先，我带你学习了文件，这种最常见的数据持久化方式。Flutter提供了两类目录，即临时目录与文档目录。我们可以根据实际需求，通过写入字符串或二进制流，实现数据的持久化。

然后，我通过一个小例子和你讲述了SharedPreferences，这种适用于持久化小型键值对的存储方案。

最后，我们一起学习了数据库。围绕如何将一个对象持久化到数据库，我与你介绍了数据库的创建、写入和读取方法。可以看到，使用数据库的方式虽然前期准备工作多了不少，但面对持续变更的需求，适配能力和灵活性都更强了。

数据持久化是CPU密集型运算，因此数据存取均会大量涉及到异步操作，所以请务必使用异步等待或注册then回调，正确处理读写操作的时序关系。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/25_data_persistence)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留下两道思考题吧。

1. 请你分别介绍一下文件、SharedPreferences和数据库，这三种持久化数据存储方式的适用场景。
2. 我们的应用经历了1.0、1.1和1.2三个版本。其中，1.0版本新建了数据库并创建了Student表，1.1版本将Student表增加了一个字段age（ALTER TABLE students ADD age INTEGER）。请你写出1.1版本及1.2版本的数据库升级代码。

```
//1.0版本数据库创建代码
final Future<Database> database = openDatabase(
  join(await getDatabasesPath(), 'students_database.db'),
  onCreate: (db, version)=>db.execute("CREATE TABLE students(id TEXT PRIMARY KEY, name TEXT, score INTEGER)"),
  onUpgrade: (db, oldVersion, newVersion){
     //dosth for migration
  },
  version: 1,
);
```

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

## 平台互操作与适配

### 如何在Dart层兼容Android_iOS平台特定实现？（一）

你好，我是陈航。

在上一篇文章中，我与你介绍了在Flutter中实现数据持久化的三种方式，即文件、SharedPreferences与数据库。

其中，文件适用于字符串或者二进制流的数据持久化，我们可以根据访问频次，决定将它存在临时目录或是文档目录。而SharedPreferences则适用于存储小型键值对信息，可以应对一些轻量配置缓存的场景。数据库则适用于频繁变化的、结构化的对象存取，可以轻松应对数据的增删改查。

依托于与Skia的深度定制及优化，Flutter给我们提供了很多关于渲染的控制和支持，能够实现绝对的跨平台应用层渲染一致性。但对于一个应用而言，除了应用层视觉显示和对应的交互逻辑处理之外，有时还需要原生操作系统（Android、iOS）提供的底层能力支持。比如，我们前面提到的数据持久化，以及推送、摄像头硬件调用等。

由于Flutter只接管了应用渲染层，因此这些系统底层能力是无法在Flutter框架内提供支持的；而另一方面，Flutter还是一个相对年轻的生态，因此原生开发中一些相对成熟的Java、C++或Objective-C代码库，比如图片处理、音视频编解码等，可能在Flutter中还没有相关实现。

因此，为了解决调用原生系统底层能力以及相关代码库复用问题，Flutter为开发者提供了一个轻量级的解决方案，即逻辑层的方法通道（Method Channel）机制。基于方法通道，我们可以将原生代码所拥有的能力，以接口形式暴露给Dart，从而实现Dart代码与原生代码的交互，就像调用了一个普通的Dart API一样。

接下来，我就与你详细讲述Flutter的方法通道机制吧。

#### 方法通道

Flutter作为一个跨平台框架，提供了一套标准化的解决方案，为开发者屏蔽了操作系统的差异。但，Flutter毕竟不是操作系统，因此在某些特定场景下（比如推送、蓝牙、摄像头硬件调用时），也需要具备直接访问系统底层原生代码的能力。为此，Flutter提供了一套灵活而轻量级的机制来实现Dart和原生代码之间的通信，即方法调用的消息传递机制，而方法通道则是用来传递通信消息的信道。

一次典型的方法调用过程类似网络调用，由作为客户端的Flutter，通过方法通道向作为服务端的原生代码宿主发送方法调用请求，原生代码宿主在监听到方法调用的消息后，调用平台相关的API来处理Flutter发起的请求，最后将处理完毕的结果通过方法通道回发至Flutter。调用过程如下图所示：

![b43dc63802c44167afafe495593dcaad](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/b43dc63802c44167afafe495593dcaad.jpg)

图1 方法通道示意图

从上图中可以看到，方法调用请求的处理和响应，在Android中是通过FlutterView，而在iOS中则是通过FlutterViewController进行注册的。FlutterView与FlutterViewController为Flutter应用提供了一个画板，使得构建于Skia之上的Flutter通过绘制即可实现整个应用所需的视觉效果。因此，它们不仅是Flutter应用的容器，同时也是Flutter应用的入口，自然也是注册方法调用请求最合适的地方。

接下来，我通过一个例子来演示如何使用方法通道实现与原生代码的交互。

#### 方法通道使用示例

在实际业务中，提示用户跳转到应用市场（iOS为App Store、Android则为各类手机应用市场）去评分是一个高频需求，考虑到Flutter并未提供这样的接口，而跳转方式在Android和iOS上各不相同，因此我们需要分别在Android和iOS上实现这样的功能，并暴露给Dart相关的接口。

我们先来看看作为客户端的Flutter，怎样实现一次方法调用请求。

##### Flutter如何实现一次方法调用请求？

首先，我们需要确定一个唯一的字符串标识符，来构造一个命名通道；然后，在这个通道之上，Flutter通过指定方法名“openAppMarket”来发起一次方法调用请求。

可以看到，这和我们平时调用一个Dart对象的方法完全一样。因为方法调用过程是异步的，所以我们需要使用非阻塞（或者注册回调）来等待原生代码给予响应。

```
//声明MethodChannel
const platform = MethodChannel('samples.chenhang/utils');

//处理按钮点击
handleButtonClick() async{
  int result;
  //异常捕获
  try {
    //异步等待方法通道的调用结果
    result = await platform.invokeMethod('openAppMarket');
  }
  catch (e) {
    result = -1;
  }
  print("Result：$result");
}
```

需要注意的是，与网络调用类似，方法调用请求有可能会失败（比如，Flutter发起了原生代码不支持的API调用，或是调用过程出错等），因此我们需要把发起方法调用请求的语句用try-catch包装起来。

调用方的实现搞定了，接下来就需要在原生代码宿主中完成方法调用的响应实现了。由于我们需要适配Android和iOS两个平台，所以我们分别需要在两个平台上完成对应的接口实现。

##### 在原生代码中完成方法调用的响应

首先，**我们来看看Android端的实现方式**。在上一小结最后我提到，在Android平台，方法调用的处理和响应是在Flutter应用的入口，也就是在MainActivity中的FlutterView里实现的，因此我们需要打开Flutter的Android宿主App，找到MainActivity.java文件，并在其中添加相关的逻辑。

调用方与响应方都是通过命名通道进行信息交互的，所以我们需要在onCreate方法中，创建一个与调用方Flutter所使用的通道名称一样的MethodChannel，并在其中设置方法处理回调，响应openAppMarket方法，打开应用市场的Intent。同样地，考虑到打开应用市场的过程可能会出错，我们也需要增加try-catch来捕获可能的异常：

```
protected void onCreate(Bundle savedInstanceState) {
  ...
  //创建与调用方标识符一样的方法通道
  new MethodChannel(getFlutterView(), "samples.chenhang/utils").setMethodCallHandler(
   //设置方法处理回调
    new MethodCallHandler() {
      //响应方法请求
      @Override
      public void onMethodCall(MethodCall call, Result result) {
        //判断方法名是否支持
        if(call.method.equals("openAppMarket")) {
          try {
            //应用市场URI
            Uri uri = Uri.parse("market://details?id=com.hangchen.example.flutter_module_page.host");
            Intent intent = new Intent(Intent.ACTION_VIEW, uri);
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            //打开应用市场
            activity.startActivity(intent);
            //返回处理结果
            result.success(0);
          } catch (Exception e) {
            //打开应用市场出现异常
            result.error("UNAVAILABLE", "没有安装应用市场", null);
          }
        }else {
          //方法名暂不支持
          result.notImplemented();
        }
      }
    });
}
```

现在，方法调用响应的Android部分已经搞定，接下来我们来看一下**iOS端的方法调用响应如何实现。**

在iOS平台，方法调用的处理和响应是在Flutter应用的入口，也就是在Applegate中的rootViewController（即FlutterViewController）里实现的，因此我们需要打开Flutter的iOS宿主App，找到AppDelegate.m文件，并添加相关逻辑。

与Android注册方法调用响应类似，我们需要在didFinishLaunchingWithOptions:方法中，创建一个与调用方Flutter所使用的通道名称一样的MethodChannel，并在其中设置方法处理回调，响应openAppMarket方法，通过URL打开应用市场：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  //创建命名方法通道
  FlutterMethodChannel* channel = [FlutterMethodChannel methodChannelWithName:@"samples.chenhang/utils" binaryMessenger:(FlutterViewController *)self.window.rootViewController];
  //往方法通道注册方法调用处理回调
  [channel setMethodCallHandler:^(FlutterMethodCall* call, FlutterResult result) {
    //方法名称一致
    if ([@"openAppMarket" isEqualToString:call.method]) {
      //打开App Store(本例打开微信的URL)
      [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"itms-apps://itunes.apple.com/xy/app/foo/id414478124"]];
      //返回方法处理结果
      result(@0);
    } else {
      //找不到被调用的方法
      result(FlutterMethodNotImplemented);
    }
  }];
  ...
}
```

这样，iOS端的方法调用响应也已经实现了。

接下来，我们就可以在Flutter应用里，通过调用openAppMarket方法，实现打开不同操作系统提供的应用市场功能了。

需要注意的是，在原生代码处理完毕后将处理结果返回给Flutter时，**我们在Dart、Android和iOS分别用了三种数据类型**：Android端返回的是java.lang.Integer、iOS端返回的是NSNumber、Dart端接收到返回结果时又变成了int类型。这是为什么呢？

这是因为在使用方法通道进行方法调用时，由于涉及到跨系统数据交互，Flutter会使用StandardMessageCodec对通道中传输的信息进行类似JSON的二进制序列化，以标准化数据传输行为。这样在我们发送或者接收数据时，这些数据就会根据各自系统预定的规则自动进行序列化和反序列化。看到这里，你是不是对这样类似网络调用的方法通道技术有了更深刻的印象呢。

对于上面提到的例子，类型为java.lang.Integer或NSNumber的返回值，先是被序列化成了一段二进制格式的数据在通道中传输，然后当该数据传递到Flutter后，又被反序列化成了Dart语言中的int类型的数据。

关于Android、iOS和Dart平台间的常见数据类型转换，我总结成了下面一张表格，帮助你理解与记忆。你只要记住，像null、布尔、整型、字符串、数组和字典这些基本类型，是可以在各个平台之间以平台定义的规则去混用的，就可以了。

![1ab26f5b754846eba9a43dd5fee1e6ba](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/1ab26f5b754846eba9a43dd5fee1e6ba.jpg)

图2 Android、iOS和Dart平台间的常见数据类型转换

#### 总结

好了，今天的分享就到这里，我们来总结一下主要内容吧。

方法通道解决了逻辑层的原生能力复用问题，使得Flutter能够通过轻量级的异步方法调用，实现与原生代码的交互。一次典型的调用过程由Flutter发起方法调用请求开始，请求经由唯一标识符指定的方法通道到达原生代码宿主，而原生代码宿主则通过注册对应方法实现、响应并处理调用请求，最后将执行结果通过消息通道，回传至Flutter。

需要注意的是，方法通道是非线程安全的。这意味着原生代码与Flutter之间所有接口调用必须发生在主线程。Flutter是单线程模型，因此自然可以确保方法调用请求是发生在主线程（Isolate）的；而原生代码在处理方法调用请求时，如果涉及到异步或非主线程切换，需要确保回调过程是在原生系统的UI线程（也就是Android和iOS的主线程）中执行的，否则应用可能会出现奇怪的Bug，甚至是Crash。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/26_native_method)中，你可以下载下来，反复运行几次，加深理解。

#### 思考题

最后，我给你留下一道思考题吧。

请扩展方法通道示例，让openAppMarket支持传入AppID和包名，使得我们可以跳转到任意一个App的应用市场。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何在Dart层兼容Android_iOS平台特定实现？（二）

你好，我是陈航。

在上一篇文章中，我与你介绍了方法通道，这种在Flutter中实现调用原生Android、iOS代码的轻量级解决方案。使用方法通道，我们可以把原生代码所拥有的能力，以接口形式提供给Dart。

这样，当发起方法调用时，Flutter应用会以类似网络异步调用的方式，将请求数据通过一个唯一标识符指定的方法通道传输至原生代码宿主；而原生代码处理完毕后，会将响应结果通过方法通道回传至Flutter，从而实现Dart代码与原生Android、iOS代码的交互。这，与调用一个本地的Dart 异步API并无太多区别。

通过方法通道，我们可以把原生操作系统提供的底层能力，以及现有原生开发中一些相对成熟的解决方案，以接口封装的形式在Dart层快速搞定，从而解决原生代码在Flutter上的复用问题。然后，我们可以利用Flutter本身提供的丰富控件，做好UI渲染。

底层能力+应用层渲染，看似我们已经搞定了搭建一个复杂App的所有内容。但，真的是这样吗？

#### 构建一个复杂App都需要什么？

别急，在下结论之前，我们先按照四象限分析法，把能力和渲染分解成四个维度，分析构建一个复杂App都需要什么。

![38cf2fbb91584a4799815e41e3b11fd3](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/38cf2fbb91584a4799815e41e3b11fd3.jpg)

图1 四象限分析法

经过分析，我们终于发现，原来构建一个App需要覆盖那么多的知识点，通过Flutter和方法通道只能搞定应用层渲染、应用层能力和底层能力，对于那些涉及到底层渲染，比如浏览器、相机、地图，以及原生自定义视图的场景，自己在Flutter上重新开发一套显然不太现实。

在这种情况下，使用混合视图看起来是一个不错的选择。我们可以在Flutter的Widget树中提前预留一块空白区域，在Flutter的画板中（即FlutterView与FlutterViewController）嵌入一个与空白区域完全匹配的原生视图，就可以实现想要的视觉效果了。

但是，采用这种方案极其不优雅，因为嵌入的原生视图并不在Flutter的渲染层级中，需要同时在Flutter侧与原生侧做大量的适配工作，才能实现正常的用户交互体验。

幸运的是，Flutter提供了一个平台视图（Platform View）的概念。它提供了一种方法，允许开发者在Flutter里面嵌入原生系统（Android和iOS）的视图，并加入到Flutter的渲染树中，实现与Flutter一致的交互体验。

这样一来，通过平台视图，我们就可以将一个原生控件包装成Flutter控件，嵌入到Flutter页面中，就像使用一个普通的Widget一样。

接下来，我就与你详细讲述如何使用平台视图。

#### 平台视图

如果说方法通道解决的是原生能力逻辑复用问题，那么平台视图解决的就是原生视图复用问题。Flutter提供了一种轻量级的方法，让我们可以创建原生（Android和iOS）的视图，通过一些简单的Dart层接口封装之后，就可以将它插入Widget树中，实现原生视图与Flutter视图的混用。

一次典型的平台视图使用过程与方法通道类似：

- 首先，由作为客户端的Flutter，通过向原生视图的Flutter封装类（在iOS和Android平台分别是UIKitView和AndroidView）传入视图标识符，用于发起原生视图的创建请求；
- 然后，原生代码侧将对应原生视图的创建交给平台视图工厂（PlatformViewFactory）实现；
- 最后，在原生代码侧将视图标识符与平台视图工厂进行关联注册，让Flutter发起的视图创建请求可以直接找到对应的视图创建工厂。

至此，我们就可以像使用Widget那样，使用原生视图了。整个流程，如下图所示：

![ab585fd02fdc419f815f310ee1a540a6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ab585fd02fdc419f815f310ee1a540a6.jpg)

图2 平台视图示例

接下来，我以一个具体的案例，也就是将一个红色的原生视图内嵌到Flutter中，与你演示如何使用平台视图。这部分内容主要包括两部分：

- 作为调用发起方的Flutter，如何实现原生视图的接口调用？
- 如何在原生（Android和iOS）系统实现接口？

接下来，我将分别与你讲述这两个问题。

##### Flutter如何实现原生视图的接口调用？

在下面的代码中，我们在SampleView的内部，分别使用了原生Android、iOS视图的封装类AndroidView和UIkitView，并传入了一个唯一标识符，用于和原生视图建立关联：

```
class SampleView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //使用Android平台的AndroidView，传入唯一标识符sampleView
    if (defaultTargetPlatform == TargetPlatform.android) {
      return AndroidView(viewType: 'sampleView');
    } else {
      //使用iOS平台的UIKitView，传入唯一标识符sampleView
      return UiKitView(viewType: 'sampleView');
    }
  }
}
```

可以看到，平台视图在Flutter侧的使用方式比较简单，与普通Widget并无明显区别。而关于普通Widget的使用方式，你可以参考第[12](https://time.geekbang.org/column/article/110292)、[13](https://time.geekbang.org/column/article/110859)篇的相关内容进行复习。

调用方的实现搞定了。接下来，我们需要在原生代码中完成视图创建的封装，建立相关的绑定关系。同样的，由于需要同时适配Android和iOS平台，我们需要分别在两个系统上完成对应的接口实现。

##### 如何在原生系统实现接口？

首先，我们来看看**Android端的实现**。在下面的代码中，我们分别创建了平台视图工厂和原生视图封装类，并通过视图工厂的create方法，将它们关联起来：

```
//视图工厂类
class SampleViewFactory extends PlatformViewFactory {
    private final BinaryMessenger messenger;
    //初始化方法
    public SampleViewFactory(BinaryMessenger msger) {
        super(StandardMessageCodec.INSTANCE);
        messenger = msger;
    }
    //创建原生视图封装类，完成关联
    @Override
    public PlatformView create(Context context, int id, Object obj) {
        return new SimpleViewControl(context, id, messenger);
    }
}
//原生视图封装类
class SimpleViewControl implements PlatformView {
    private final View view;//缓存原生视图
    //初始化方法，提前创建好视图
    public SimpleViewControl(Context context, int id, BinaryMessenger messenger) {
        view = new View(context);
        view.setBackgroundColor(Color.rgb(255, 0, 0));
    }

    //返回原生视图
    @Override
    public View getView() {
        return view;
    }
    //原生视图销毁回调
    @Override
    public void dispose() {
    }
}
```

将原生视图封装类与原生视图工厂完成关联后，接下来就需要将Flutter侧的调用与视图工厂绑定起来了。与上一篇文章讲述的方法通道类似，我们仍然需要在MainActivity中进行绑定操作：

```
protected void onCreate(Bundle savedInstanceState) {
  ...
  Registrar registrar =    registrarFor("samples.chenhang/native_views");//生成注册类
  SampleViewFactory playerViewFactory = new SampleViewFactory(registrar.messenger());//生成视图工厂

registrar.platformViewRegistry().registerViewFactory("sampleView", playerViewFactory);//注册视图工厂
}
```

完成绑定之后，平台视图调用响应的Android部分就搞定了。

接下来，我们再来看看**iOS端的实现**。

与Android类似，我们同样需要分别创建平台视图工厂和原生视图封装类，并通过视图工厂的create方法，将它们关联起来：

```
//平台视图工厂
@interface SampleViewFactory : NSObject<FlutterPlatformViewFactory>
- (instancetype)initWithMessenger:(NSObject<FlutterBinaryMessenger>*)messager;
@end

@implementation SampleViewFactory{
  NSObject<FlutterBinaryMessenger>*_messenger;
}

- (instancetype)initWithMessenger:(NSObject<FlutterBinaryMessenger> *)messager{
  self = [super init];
  if (self) {
    _messenger = messager;
  }
  return self;
}

-(NSObject<FlutterMessageCodec> *)createArgsCodec{
  return [FlutterStandardMessageCodec sharedInstance];
}

//创建原生视图封装实例
-(NSObject<FlutterPlatformView> *)createWithFrame:(CGRect)frame viewIdentifier:(int64_t)viewId arguments:(id)args{
  SampleViewControl *activity = [[SampleViewControl alloc] initWithWithFrame:frame viewIdentifier:viewId arguments:args binaryMessenger:_messenger];
  return activity;
}
@end

//平台视图封装类
@interface SampleViewControl : NSObject<FlutterPlatformView>
- (instancetype)initWithWithFrame:(CGRect)frame viewIdentifier:(int64_t)viewId arguments:(id _Nullable)args binaryMessenger:(NSObject<FlutterBinaryMessenger>*)messenger;
@end

@implementation SampleViewControl{
    UIView * _templcateView;
}
//创建原生视图
- (instancetype)initWithWithFrame:(CGRect)frame viewIdentifier:(int64_t)viewId arguments:(id)args binaryMessenger:(NSObject<FlutterBinaryMessenger> *)messenger{
  if ([super init]) {
    _templcateView = [[UIView alloc] init];
    _templcateView.backgroundColor = [UIColor redColor];
  }
  return self;
}

-(UIView *)view{
  return _templcateView;
}

@end
```

然后，我们同样需要把原生视图的创建与Flutter侧的调用关联起来，才可以在Flutter侧找到原生视图的实现：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSObject<FlutterPluginRegistrar>* registrar = [self registrarForPlugin:@"samples.chenhang/native_views"];//生成注册类
  SampleViewFactory* viewFactory = [[SampleViewFactory alloc] initWithMessenger:registrar.messenger];//生成视图工厂
    [registrar registerViewFactory:viewFactory withId:@"sampleView"];//注册视图工厂
 ...
}
```

需要注意的是，在iOS平台上，Flutter内嵌UIKitView目前还处于技术预览状态，因此我们还需要在Info.plist文件中增加一项配置，把内嵌原生视图的功能开关设置为true，才能打开这个隐藏功能：

```
<dict>
   ...
  <key>io.flutter.embedded_views_preview</key>
  <true/>
  ....
</dict>
```

经过上面的封装与绑定，Android端与iOS端的平台视图功能都已经实现了。接下来，我们就可以在Flutter应用里，像使用普通Widget一样，去内嵌原生视图了：

```
 Scaffold(
        backgroundColor: Colors.yellowAccent,
        body:  Container(width: 200, height:200,
            child: SampleView(controller: controller)
        ));
```

如下所示，我们分别在iOS和Android平台的Flutter应用上，内嵌了一个红色的原生视图：

![89abfd6ac28a4d9f9df94e5c629bd500](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/89abfd6ac28a4d9f9df94e5c629bd500.jpg)

图3 内嵌原生视图示例

在上面的例子中，我们将原生视图封装在一个StatelessWidget中，可以有效应对静态展示的场景。如果我们需要在程序运行时动态调整原生视图的样式，又该如何处理呢？

#### 如何在程序运行时，动态地调整原生视图的样式？

与基于声明式的Flutter Widget，每次变化只能以数据驱动其视图销毁重建不同，原生视图是基于命令式的，可以精确地控制视图展示样式。因此，我们可以在原生视图的封装类中，将其持有的修改视图实例相关的接口，以方法通道的方式暴露给Flutter，让Flutter也可以拥有动态调整视图视觉样式的能力。

接下来，我以一个具体的案例来演示如何在程序运行时动态调整内嵌原生视图的背景颜色。

在这个案例中，我们会用到原生视图的一个初始化属性，即onPlatformViewCreated：原生视图会在其创建完成后，以回调的形式通知视图id，因此我们可以在这个时候注册方法通道，让后续的视图修改请求通过这条通道传递给原生视图。

由于我们在底层直接持有了原生视图的实例，因此理论上可以直接在这个原生视图的Flutter封装类上提供视图修改方法，而不管它到底是StatelessWidget还是StatefulWidget。但为了遵照Flutter的Widget设计理念，我们还是决定将视图展示与视图控制分离，即：将原生视图封装为一个StatefulWidget专门用于展示，通过其controller初始化参数，在运行期修改原生视图的展示效果。如下所示：

```
//原生视图控制器
class NativeViewController {
  MethodChannel _channel;
  //原生视图完成创建后，通过id生成唯一方法通道
  onCreate(int id) {
    _channel = MethodChannel('samples.chenhang/native_views_$id');
  }
  //调用原生视图方法，改变背景颜色
  Future<void> changeBackgroundColor() async {
    return _channel.invokeMethod('changeBackgroundColor');
  }
}

//原生视图Flutter侧封装，继承自StatefulWidget
class SampleView extends StatefulWidget {
  const SampleView({
    Key key,
    this.controller,
  }) : super(key: key);

  //持有视图控制器
  final NativeViewController controller;
  @override
  State<StatefulWidget> createState() => _SampleViewState();
}

class _SampleViewState extends State<SampleView> {
  //根据平台确定返回何种平台视图
  @override
  Widget build(BuildContext context) {
    if (defaultTargetPlatform == TargetPlatform.android) {
      return AndroidView(
        viewType: 'sampleView',
        //原生视图创建完成后，通过onPlatformViewCreated产生回调
        onPlatformViewCreated: _onPlatformViewCreated,
      );
    } else {
      return UiKitView(viewType: 'sampleView',
        //原生视图创建完成后，通过onPlatformViewCreated产生回调
        onPlatformViewCreated: _onPlatformViewCreated
      );
    }
  }
  //原生视图创建完成后，调用control的onCreate方法，传入view id
  _onPlatformViewCreated(int id) {
    if (widget.controller == null) {
      return;
    }
    widget.controller.onCreate(id);
  }
}
```

Flutter的调用方实现搞定了，接下来我们分别看看Android和iOS端的实现。

程序的整体结构与之前并无不同，只是在进行原生视图初始化时，我们需要完成方法通道的注册和相关事件的处理；在响应方法调用消息时，我们需要判断方法名，如果完全匹配，则修改视图背景，否则返回异常。

Android端接口实现代码如下所示：

```
class SimpleViewControl implements PlatformView, MethodCallHandler {
    private final MethodChannel methodChannel;
    ...
    public SimpleViewControl(Context context, int id, BinaryMessenger messenger) {
        ...
        //用view id注册方法通道
        methodChannel = new MethodChannel(messenger, "samples.chenhang/native_views_" + id);
        //设置方法通道回调
        methodChannel.setMethodCallHandler(this);
    }
    //处理方法调用消息
    @Override
    public void onMethodCall(MethodCall methodCall, MethodChannel.Result result) {
        //如果方法名完全匹配
        if (methodCall.method.equals("changeBackgroundColor")) {
            //修改视图背景，返回成功
            view.setBackgroundColor(Color.rgb(0, 0, 255));
            result.success(0);
        }else {
            //调用方发起了一个不支持的API调用
            result.notImplemented();
        }
    }
  ...
}
```

iOS端接口实现代码：

```
@implementation SampleViewControl{
    ...
    FlutterMethodChannel* _channel;
}

- (instancetype)initWithWithFrame:(CGRect)frame viewIdentifier:(int64_t)viewId arguments:(id)args binaryMessenger:(NSObject<FlutterBinaryMessenger> *)messenger{
    if ([super init]) {
        ...
        //使用view id完成方法通道的创建
        _channel = [FlutterMethodChannel methodChannelWithName:[NSString stringWithFormat:@"samples.chenhang/native_views_%lld", viewId] binaryMessenger:messenger];
        //设置方法通道的处理回调
        __weak __typeof__(self) weakSelf = self;
        [_channel setMethodCallHandler:^(FlutterMethodCall* call, FlutterResult result) {
            [weakSelf onMethodCall:call result:result];
        }];
    }
    return self;
}

//响应方法调用消息
- (void)onMethodCall:(FlutterMethodCall*)call result:(FlutterResult)result {
    //如果方法名完全匹配
    if ([[call method] isEqualToString:@"changeBackgroundColor"]) {
        //修改视图背景色，返回成功
        _templcateView.backgroundColor = [UIColor blueColor];
        result(@0);
    } else {
        //调用方发起了一个不支持的API调用
        result(FlutterMethodNotImplemented);
    }
}
 ...
@end
```

通过注册方法通道，以及暴露的changeBackgroundColor接口，Android端与iOS端修改平台视图背景颜色的功能都已经实现了。接下来，我们就可以在Flutter应用运行期间，修改原生视图展示样式了：

```
class DefaultState extends State<DefaultPage> {
  NativeViewController controller;
  @override
  void initState() {
    controller = NativeViewController();//初始化原生View控制器
	super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
          ...
          //内嵌原生View
          body:  Container(width: 200, height:200,
              child: SampleView(controller: controller)
          ),
         //设置点击行为：改变视图颜色
         floatingActionButton: FloatingActionButton(onPressed: ()=>controller.changeBackgroundColor())
    );
  }
}
```

运行一下，效果如下所示：

![7dffd34126e04771a82ef98521f22f9b](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/7dffd34126e04771a82ef98521f22f9b.jpg)

图4 动态修改原生视图样式

#### 总结

好了，今天的分享就到这里。我们总结一下今天的主要内容吧。

平台视图解决了原生渲染能力的复用问题，使得Flutter能够通过轻量级的代码封装，把原生视图组装成一个Flutter控件。

Flutter提供了平台视图工厂和视图标识符两个概念，因此Dart层发起的视图创建请求可以通过标识符直接找到对应的视图创建工厂，从而实现原生视图与Flutter视图的融合复用。对于需要在运行期动态调用原生视图接口的需求，我们可以在原生视图的封装类中注册方法通道，实现精确控制原生视图展示的效果。

需要注意的是，由于Flutter与原生渲染方式完全不同，因此转换不同的渲染数据会有较大的性能开销。如果在一个界面上同时实例化多个原生控件，就会对性能造成非常大的影响，所以我们要避免在使用Flutter控件也能实现的情况下去使用内嵌平台视图。

因为这样做，一方面需要分别在Android和iOS端写大量的适配桥接代码，违背了跨平台技术的本意，也增加了后续的维护成本；另一方面毕竟除去地图、WebView、相机等涉及底层方案的特殊情况外，大部分原生代码能够实现的UI效果，完全可以用Flutter实现。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/27_native_view)中，你可以下载下来，反复运行几次，加深理解。

#### 思考题

最后，我给你留下一道思考题吧。

请你在动态调整原生视图样式的代码基础上，增加颜色参数，以实现动态变更原生视图颜色的需求。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何在原生应用中混编Flutter工程？

你好，我是陈航。今天，我来和你聊聊如何在原生应用中接入Flutter。

在前面两篇文章中，我与你分享了如何在Dart层引入Android/iOS平台特定的能力，来提升App的功能体验。

使用Flutter从头开始写一个App，是一件轻松惬意的事情。但，对于成熟产品来说，完全摒弃原有App的历史沉淀，而全面转向Flutter并不现实。用Flutter去统一iOS/Android技术栈，把它作为已有原生App的扩展能力，通过逐步试验有序推进从而提升终端开发效率，可能才是现阶段Flutter最具吸引力的地方。

那么，Flutter工程与原生工程该如何组织管理？不同平台的Flutter工程打包构建产物该如何抽取封装？封装后的产物该如何引入原生工程？原生工程又该如何使用封装后的Flutter能力？

这些问题使得在已有原生App中接入Flutter看似并不是一件容易的事情。那接下来，我就和你介绍下如何在原生App中以最自然的方式接入Flutter。

#### 准备工作

既然是要在原生应用中混编Flutter，相信你一定已经准备好原生应用工程来实施今天的改造了。如果你还没有准备好也没关系，我会以一个最小化的示例和你演示这个改造过程。

首先，我们分别用Xcode与Android Studio快速建立一个只有首页的基本工程，工程名分别为iOSDemo与AndroidDemo。

这时，Android工程就已经准备好了；而对于iOS工程来说，由于基本工程并不支持以组件化的方式管理项目，因此我们还需要多做一步，将其改造成使用CocoaPods管理的工程，也就是要在iOSDemo根目录下创建一个只有基本信息的Podfile文件：

```
use_frameworks!
platform :ios, '8.0'
target 'iOSDemo' do
#todo
end
```

然后，在命令行输入pod install后，会自动生成一个iOSDemo.xcworkspace文件，这时我们就完成了iOS工程改造。

#### Flutter混编方案介绍

如果你想要在已有的原生App里嵌入一些Flutter页面，有两个办法：

- 将原生工程作为Flutter工程的子工程，由Flutter统一管理。这种模式，就是统一管理模式。
- 将Flutter工程作为原生工程共用的子模块，维持原有的原生工程管理方式不变。这种模式，就是三端分离模式。

![28ff7c1a0ab44377bff8f9688671a5eb](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/28ff7c1a0ab44377bff8f9688671a5eb.jpg)

图1 Flutter混编工程管理方式

由于Flutter早期提供的混编方式能力及相关资料有限，国内较早使用Flutter混合开发的团队大多使用的是统一管理模式。但是，随着功能迭代的深入，这种方案的弊端也随之显露，不仅三端（Android、iOS、Flutter）代码耦合严重，相关工具链耗时也随之大幅增长，导致开发效率降低。

所以，后续使用Flutter混合开发的团队陆续按照三端代码分离的模式来进行依赖治理，实现了Flutter工程的轻量级接入。

除了可以轻量级接入，三端代码分离模式把Flutter模块作为原生工程的子模块，还可以快速实现Flutter功能的“热插拔”，降低原生工程的改造成本。而Flutter工程通过Android Studio进行管理，无需打开原生工程，可直接进行Dart代码和原生代码的开发调试。

**三端工程分离模式的关键是抽离Flutter工程，将不同平台的构建产物依照标准组件化的形式进行管理**，即Android使用aar、iOS使用pod。换句话说，接下来介绍的混编方案会将Flutter模块打包成aar和pod，这样原生工程就可以像引用其他第三方原生组件库那样快速接入Flutter了。

听起来是不是很兴奋？接下来，我们就开始正式采用三端分离模式来接入Flutter模块吧。

#### 集成Flutter

我曾在前面的文章中提到，Flutter的工程结构比较特殊，包括Flutter工程和原生工程的目录（即iOS和Android两个目录）。在这种情况下，原生工程就会依赖于Flutter相关的库和资源，从而无法脱离父目录进行独立构建和运行。

原生工程对Flutter的依赖主要分为两部分：

- Flutter库和引擎，也就是Flutter的Framework库和引擎库；
- Flutter工程，也就是我们自己实现的Flutter模块功能，主要包括Flutter工程lib目录下的Dart代码实现的这部分功能。

在已经有原生工程的情况下，我们需要在同级目录创建Flutter模块，构建iOS和Android各自的Flutter依赖库。这也很好实现，Flutter就为我们提供了这样的命令。我们只需要在原生项目的同级目录下，执行Flutter命令创建名为flutter_library的模块即可：

```
Flutter create -t module flutter_library
```

这里的Flutter模块，也是Flutter工程，我们用Android Studio打开它，其目录如下图所示：

![d7f154a2e5f244e384802f3cd746fc7f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d7f154a2e5f244e384802f3cd746fc7f.jpg)

图2 Flutter模块工程结构

可以看到，和传统的Flutter工程相比，Flutter模块工程也有内嵌的Android工程与iOS工程，因此我们可以像普通工程一样使用Android Studio进行开发调试。

仔细查看可以发现，**Flutter模块有一个细微的变化**：Android工程下多了一个Flutter目录，这个目录下的build.gradle配置就是我们构建aar的打包配置。这就是模块工程既能像Flutter传统工程一样使用Android Studio开发调试，又能打包构建aar与pod的秘密。

实际上，iOS工程的目录结构也有细微变化，但这个差异并不影响打包构建，因此我就不再展开了。

然后，我们打开main.dart文件，将其逻辑更新为以下代码逻辑，即一个写着“Hello from Flutter”的全屏红色的Flutter Widget：

```
import 'package:flutter/material.dart';
import 'dart:ui';

void main() => runApp(_widgetForRoute(window.defaultRouteName));//独立运行传入默认路由

Widget _widgetForRoute(String route) {
  switch (route) {
    default:
      return MaterialApp(
        home: Scaffold(
          backgroundColor: const Color(0xFFD63031),//ARGB红色
          body: Center(
            child: Text(
              'Hello from Flutter', //显示的文字
              textDirection: TextDirection.ltr,
              style: TextStyle(
                fontSize: 20.0,
                color: Colors.blue,
              ),
            ),
          ),
        ),
      );
  }
}
```

注意：我们创建的Widget实际上是包在一个switch-case语句中的。这是因为封装的Flutter模块一般会有多个页面级Widget，原生App代码则会通过传入路由标识字符串，告诉Flutter究竟应该返回何种Widget。为了简化案例，在这里我们忽略标识字符串，统一返回一个MaterialApp。

接下来，我们要做的事情就是把这段代码编译打包，构建出对应的Android和iOS依赖库，实现原生工程的接入。

现在，我们首先来看看Android工程如何接入。

##### Android模块集成

之前我们提到原生工程对Flutter的依赖主要分为两部分，对应到Android平台，这两部分分别是：

- Flutter库和引擎，也就是icudtl.dat、libFlutter.so，还有一些class文件。这些文件都封装在Flutter.jar中。
- Flutter工程产物，主要包括应用程序数据段isolate_snapshot_data、应用程序指令段isolate_snapshot_instr、虚拟机数据段vm_snapshot_data、虚拟机指令段vm_snapshot_instr、资源文件Flutter_assets。

搞清楚Flutter工程的Android编译产物之后，我们对Android的Flutter依赖抽取步骤如下：

首先在Flutter_library的根目录下，执行aar打包构建命令：

```
Flutter build apk --debug
```

这条命令的作用是编译工程产物，并将Flutter.jar和工程产物编译结果封装成一个aar。你很快就会想到，如果是构建release产物，只需要把debug换成release就可以了。

**其次**，打包构建的flutter-debug.aar位于.android/Flutter/build/outputs/aar/目录下，我们把它拷贝到原生Android工程AndroidDemo的app/libs目录下，并在App的打包配置build.gradle中添加对它的依赖:

```
...
repositories {
    flatDir {
        dirs 'libs'   // aar目录
    }
}
android {
    ...
    compileOptions {
        sourceCompatibility 1.8 //Java 1.8
        targetCompatibility 1.8 //Java 1.8
    }
    ...
}

dependencies {
    ...
    implementation(name: 'flutter-debug', ext: 'aar')//Flutter模块aar
    ...
}
```

Sync一下，Flutter模块就被添加到了Android项目中。

再次，我们试着改一下MainActivity.java的代码，把它的contentView改成Flutter的widget：

```
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    View FlutterView = Flutter.createView(this, getLifecycle(), "defaultRoute"); //传入路由标识符
    setContentView(FlutterView);//用FlutterView替代Activity的ContentView
}
```

最后点击运行，可以看到一个写着“Hello from Flutter”的全屏红色的Flutter Widget就展示出来了。至此，我们完成了Android工程的接入。

![66f1a9f681b84e0c972db14fe5c7983b](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/66f1a9f681b84e0c972db14fe5c7983b.jpg)

图3 Android工程接入示例

##### iOS模块集成

iOS工程接入的情况要稍微复杂一些。在iOS平台，原生工程对Flutter的依赖分别是：

- Flutter库和引擎，即Flutter.framework；
- Flutter工程的产物，即App.framework。

iOS平台的Flutter模块抽取，实际上就是通过打包命令生成这两个产物，并将它们封装成一个pod供原生工程引用。

类似地，首先我们在Flutter_library的根目录下，执行iOS打包构建命令：

```
Flutter build ios --debug
```

这条命令的作用是编译Flutter工程生成两个产物：Flutter.framework和App.framework。同样，把debug换成release就可以构建release产物（当然，你还需要处理一下签名问题）。

**其次**，在iOSDemo的根目录下创建一个名为FlutterEngine的目录，并把这两个framework文件拷贝进去。iOS的模块化产物工作要比Android多一个步骤，因为我们需要把这两个产物手动封装成pod。因此，我们还需要在该目录下创建FlutterEngine.podspec，即Flutter模块的组件定义：

```
Pod::Spec.new do |s|
  s.name             = 'FlutterEngine'
  s.version          = '0.1.0'
  s.summary          = 'XXXXXXX'
  s.description      = <<-DESC
TODO: Add long description of the pod here.
                       DESC
  s.homepage         = 'https://github.com/xx/FlutterEngine'
  s.license          = { :type => 'MIT', :file => 'LICENSE' }
  s.author           = { 'chenhang' => '[email protected]' }
  s.source       = { :git => "", :tag => "#{s.version}" }
  s.ios.deployment_target = '8.0'
  s.ios.vendored_frameworks = 'App.framework', 'Flutter.framework'
end
```

pod lib lint一下，Flutter模块组件就已经做好了。趁热打铁，我们再修改Podfile文件把它集成到iOSDemo工程中：

```
...
target 'iOSDemo' do
    pod 'FlutterEngine', :path => './'
end
```

pod install一下，Flutter模块就集成进iOS原生工程中了。

再次，我们试着修改一下AppDelegate.m的代码，把window的rootViewController改成FlutterViewController：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions

{
    self.window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
    FlutterViewController *vc = [[FlutterViewController alloc]init];
    [vc setInitialRoute:@"defaultRoute"]; //路由标识符
    self.window.rootViewController = vc;
    [self.window makeKeyAndVisible];
    return YES;
}
```

最后点击运行，一个写着“Hello from Flutter”的全屏红色的Flutter Widget也展示出来了。至此，iOS工程的接入我们也顺利搞定了。

![50ae2b3e7fa847308a4e427b11d0c132](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/50ae2b3e7fa847308a4e427b11d0c132.jpg)

图4 iOS工程接入示例

#### 总结

通过分离Android、iOS和Flutter三端工程，抽离Flutter库和引擎及工程代码为组件库，以Android和iOS平台最常见的aar和pod形式接入原生工程，我们就可以低成本地接入Flutter模块，愉快地使用Flutter扩展原生App的边界了。

但，我们还可以做得更好。

如果每次通过构建Flutter模块工程，都是手动搬运Flutter编译产物，那很容易就会因为工程管理混乱导致Flutter组件库被覆盖，从而引发难以排查的Bug。而要解决此类问题的话，我们可以引入CI自动构建框架，把Flutter编译产物构建自动化，原生工程通过接入不同版本的构建产物，实现更优雅的三端分离模式。

而关于自动化构建，我会在后面的文章中和你详细介绍，这里就不再赘述了。

接下来，我们简单回顾一下今天的内容。

原生工程混编Flutter的方式有两种。一种是，将Flutter工程内嵌Android和iOS工程，由Flutter统一管理的集中模式；另一种是，将Flutter工程作为原生工程共用的子模块，由原生工程各自管理的三端工程分离模式。目前，业界采用的基本都是第二种方式。

而对于三端工程分离模式最主要的则是抽离Flutter工程，将不同平台的构建产物依照标准组件化的形式进行管理，即：针对Android平台打包构建生成aar，通过build.gradle进行依赖管理；针对iOS平台打包构建生成framework，将其封装成独立的pod，并通过podfile进行依赖管理。

我把今天分享所涉及到的知识点打包到了GitHub（[flutter_module_page](https://github.com/cyndibaby905/28_module_page)、[iOS_demo](https://github.com/cyndibaby905/28_iOSDemo)、[Android_Demo](https://github.com/cyndibaby905/28_AndroidDemo)）中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你下留一个思考题吧。

对于有资源依赖的Flutter模块工程而言，其打包构建的产物，以及抽离Flutter组件库的过程会有什么不同吗？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 混合开发，该用何种方案管理导航栈？

你好，我是陈航。

为了把Flutter引入到原生工程，我们需要把Flutter工程改造为原生工程的一个组件依赖，并以组件化的方式管理不同平台的Flutter构建产物，即Android平台使用aar、iOS平台使用pod进行依赖管理。这样，我们就可以在Android工程中通过FlutterView，iOS工程中通过FlutterViewController，为Flutter搭建应用入口，实现Flutter与原生的混合开发方式。

我在[第26篇](https://time.geekbang.org/column/article/127601)文章中提到，FlutterView与FlutterViewController是初始化Flutter的地方，也是应用的入口。可以看到，以混合开发方式接入Flutter，与开发一个纯Flutter应用在运行机制上并无任何区别，只需要原生工程为它提供一个画板容器（Android为FlutterView，iOS为FlutterViewController），Flutter就可以自己管理页面导航栈，从而实现多个复杂页面的渲染和切换。

关于纯Flutter应用的页面路由与导航，我已经在[第21篇文章](https://time.geekbang.org/column/article/118421)中与你介绍过了。今天这篇文章，我会为你讲述在混合开发中，应该如何管理混合导航栈。

对于混合开发的应用而言，通常我们只会将应用的部分模块修改成Flutter开发，其他模块继续保留原生开发，因此应用内除了Flutter的页面之外，还会有原生Android、iOS的页面。在这种情况下，Flutter页面有可能会需要跳转到原生页面，而原生页面也可能会需要跳转到Flutter页面。这就涉及到了一个新的问题：如何统一管理原生页面和Flutter页面跳转交互的混合导航栈。

接下来，我们就从这个问题入手，开始今天的学习吧。

#### 混合导航栈

混合导航栈，指的是原生页面和Flutter页面相互掺杂，存在于用户视角的页面导航栈视图中。

以下图为例，Flutter与原生Android、iOS各自实现了一套互不相同的页面映射机制，即原生采用单容器单页面（一个ViewController/Activity对应一个原生页面）、Flutter采用单容器多页面（一个ViewController/Activity对应多个Flutter页面）的机制。Flutter在原生的导航栈之上又自建了一套Flutter导航栈，这使得Flutter页面与原生页面之间涉及页面切换时，我们需要处理跨引擎的页面切换。

![ff00e6653b5f4c24b2e93ce90d7ad887](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ff00e6653b5f4c24b2e93ce90d7ad887.jpg)

图1 混合导航栈示意图

接下来，我们就分别看看从原生页面跳转至Flutter页面，以及从Flutter页面跳转至原生页面，应该如何处理吧。

##### 从原生页面跳转至Flutter页面

从原生页面跳转至Flutter页面，实现起来比较简单。

因为Flutter本身依托于原生提供的容器（iOS为FlutterViewController，Android为Activity中的FlutterView），所以我们通过初始化Flutter容器，为其设置初始路由页面之后，就可以以原生的方式跳转至Flutter页面了。

如下代码所示。对于iOS，我们初始化一个FlutterViewController的实例，为其设置初始化页面路由后，将其加入原生的视图导航栈中完成跳转。

对于Android而言，则需要多加一步。因为Flutter页面的入口并不是原生视图导航栈的最小单位Activity，而是一个View（即FlutterView），所以我们还需要把这个View包装到Activity的contentView中。在Activity内部设置页面初始化路由之后，在外部就可以采用打开一个普通的原生视图的方式，打开Flutter页面了。

```
//iOS 跳转至Flutter页面
FlutterViewController *vc = [[FlutterViewController alloc] init];
[vc setInitialRoute:@"defaultPage"];//设置Flutter初始化路由页面
[self.navigationController pushViewController:vc animated:YES];//完成页面跳转


//Android 跳转至Flutter页面

//创建一个作为Flutter页面容器的Activity
public class FlutterHomeActivity extends AppCompatActivity {
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    //设置Flutter初始化路由页面
    View FlutterView = Flutter.createView(this, getLifecycle(), "defaultRoute"); //传入路由标识符
    setContentView(FlutterView);//用FlutterView替代Activity的ContentView
  }
}
//用FlutterPageActivity完成页面跳转
Intent intent = new Intent(MainActivity.this, FlutterHomeActivity.class);
startActivity(intent);
```

##### 从Flutter页面跳转至原生页面

从Flutter页面跳转至原生页面，则会相对麻烦些，我们需要考虑以下两种场景：

- 从Flutter页面打开新的原生页面；
- 从Flutter页面回退到旧的原生页面。

首先，我们来看看Flutter如何打开原生页面。

Flutter并没有提供对原生页面操作的方法，所以不可以直接调用。我们需要通过方法通道（你可以再回顾下[第26篇](https://time.geekbang.org/column/article/127601)文章的相关内容），在Flutter和原生两端各自初始化时，提供Flutter操作原生页面的方法，并注册方法通道，在原生端收到Flutter的方法调用时，打开新的原生页面。

接下来，我们再看看如何从Flutter页面回退到原生页面。

因为Flutter容器本身属于原生导航栈的一部分，所以当Flutter容器内的根页面（即初始化路由页面）需要返回时，我们需要关闭Flutter容器，从而实现Flutter根页面的关闭。同样，Flutter并没有提供操作Flutter容器的方法，因此我们依然需要通过方法通道，在原生代码宿主为Flutter提供操作Flutter容器的方法，在页面返回时，关闭Flutter页面。

Flutter跳转至原生页面的两种场景，如下图所示：

![9989af3fb77c4c20a347fe20018e18dc](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/9989af3fb77c4c20a347fe20018e18dc.jpg)

图2 Flutter页面跳转至原生页面示意图

**接下来，我们一起看看这两个需要通过方法通道实现的方法，即打开原生页面openNativePage，与关闭Flutter页面closeFlutterPage，在Android和iOS平台上分别如何实现。**

注册方法通道最合适的地方，是Flutter应用的入口，即在FlutterViewController（iOS端）和Activity中的FlutterView（Android端）这两个容器内部初始化Flutter页面前。为了将Flutter相关的行为封装到容器内部，我们需要分别继承FlutterViewController和Activity，在其viewDidLoad和onCreate初始化容器时，注册openNativePage和closeFlutterPage这两个方法。

iOS端的实现代码如下所示：

```
@interface FlutterHomeViewController : FlutterViewController
@end

@implementation FlutterHomeViewController
- (void)viewDidLoad {
    [super viewDidLoad];
    //声明方法通道
    FlutterMethodChannel* channel = [FlutterMethodChannel methodChannelWithName:@"samples.chenhang/navigation" binaryMessenger:self];
    //注册方法回调
    [channel setMethodCallHandler:^(FlutterMethodCall* call, FlutterResult result) {
        //如果方法名为打开新页面
        if([call.method isEqualToString:@"openNativePage"]) {
            //初始化原生页面并打开
            SomeOtherNativeViewController *vc = [[SomeOtherNativeViewController alloc] init];
            [self.navigationController pushViewController:vc animated:YES];
            result(@0);
        }
        //如果方法名为关闭Flutter页面
        else if([call.method isEqualToString:@"closeFlutterPage"]) {
            //关闭自身(FlutterHomeViewController)
            [self.navigationController popViewControllerAnimated:YES];
            result(@0);
        }
        else {
            result(FlutterMethodNotImplemented);//其他方法未实现
        }
    }];
}
@end
```

Android端的实现代码如下所示：

```
//继承AppCompatActivity来作为Flutter的容器
public class FlutterHomeActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //初始化Flutter容器
        FlutterView flutterView = Flutter.createView(this, getLifecycle(), "defaultPage"); //传入路由标识符
        //注册方法通道
        new MethodChannel(flutterView, "samples.chenhang/navigation").setMethodCallHandler(
            new MethodCallHandler() {
                @Override
                public void onMethodCall(MethodCall call, Result result) {
                    //如果方法名为打开新页面
                    if(call.method.equals("openNativePage")) {
                        //新建Intent，打开原生页面
                        Intent intent = new Intent(FlutterHomeActivity.this, SomeNativePageActivity.class);
                        startActivity(intent);
                        result.success(0);
                    }
                    //如果方法名为关闭Flutter页面
                    else if(call.method.equals("closeFlutterPage")) {
                        //销毁自身(Flutter容器)
                        finish();
                        result.success(0);
                    }
                    else {
                        //方法未实现
                        result.notImplemented();
                    }
                }
            });
        //将flutterView替换成Activity的contentView
        setContentView(flutterView);
    }
}
```

经过上面的方法注册，我们就可以在Flutter层分别通过openNativePage和closeFlutterPage方法，来实现Flutter页面与原生页面之间的切换了。

在下面的例子中，Flutter容器的根视图DefaultPage包含有两个按钮：

- 点击左上角的按钮后，可以通过closeFlutterPage返回原生页面；
- 点击中间的按钮后，会打开一个新的Flutter页面PageA。PageA中也有一个按钮，点击这个按钮之后会调用openNativePage来打开一个新的原生页面。

```
void main() => runApp(_widgetForRoute(window.defaultRouteName));
//获取方法通道
const platform = MethodChannel('samples.chenhang/navigation');

//根据路由标识符返回应用入口视图
Widget _widgetForRoute(String route) {
  switch (route) {
    default://返回默认视图
      return MaterialApp(home:DefaultPage());
  }
}

class PageA extends StatelessWidget {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
            body: RaisedButton(
                    child: Text("Go PageB"),
                    onPressed: ()=>platform.invokeMethod('openNativePage')//打开原生页面
            ));
  }
}

class DefaultPage extends StatelessWidget {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
            title: Text("DefaultPage Page"),
            leading: IconButton(icon:Icon(Icons.arrow_back), onPressed:() => platform.invokeMethod('closeFlutterPage')//关闭Flutter页面
        )),
        body: RaisedButton(
                  child: Text("Go PageA"),
                  onPressed: ()=>Navigator.push(context, MaterialPageRoute(builder: (context) => PageA())),//打开Flutter页面 PageA
        ));
  }
}
```

整个混合导航栈示例的代码流程，如下图所示。通过这张图，你就可以把这个示例的整个代码流程串起来了。

![0f92fe6622d14bc88b3ff9ead63e1f13](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0f92fe6622d14bc88b3ff9ead63e1f13.jpg)

图3 混合导航栈示例

在我们的混合应用中，RootViewController与MainActivity分别是iOS和Android应用的原生页面入口，可以初始化为Flutter容器的FlutterHomeViewController（iOS端）与FlutterHomeActivity（Android端）。

在为其设置初始路由页面DefaultPage之后，就可以以原生的方式跳转至Flutter页面。但是，Flutter并未提供接口，来支持从Flutter的DefaultPage页面返回到原生页面，因此我们需要利用方法通道来注册关闭Flutter容器的方法，即closeFlutterPage，让Flutter容器接收到这个方法调用时关闭自身。

在Flutter容器内部，我们可以使用Flutter内部的页面路由机制，通过Navigator.push方法，完成从DefaultPage到PageA的页面跳转；而当我们想从Flutter的PageA页面跳转到原生页面时，因为涉及到跨引擎的页面路由，所以我们仍然需要利用方法通道来注册打开原生页面的方法，即openNativePage，让 Flutter容器接收到这个方法调用时，在原生代码宿主完成原生页面SomeOtherNativeViewController（iOS端）与SomeNativePageActivity（Android端）的初始化，并最终完成页面跳转。

#### 总结

好了，今天的分享就到这里。我们一起总结下今天的主要内容吧。

对于原生Android、iOS工程混编Flutter开发，由于应用中会同时存在Android、iOS和Flutter页面，所以我们需要妥善处理跨渲染引擎的页面跳转，解决原生页面如何切换Flutter页面，以及Flutter页面如何切换到原生页面的问题。

在原生页面切换到Flutter页面时，我们通常会将Flutter容器封装成一个独立的ViewController（iOS端）或Activity（Android端），在为其设置好Flutter容器的页面初始化路由（即根视图）后，原生的代码就可以按照打开一个普通的原生页面的方式，来打开Flutter页面了。

而如果我们想在Flutter页面跳转到原生页面，则需要同时处理好打开新的原生页面，以及关闭自身回退到老的原生页面两种场景。在这两种场景下，我们都需要利用方法通道来注册相应的处理方法，从而在原生代码宿主实现新页面的打开和Flutter容器的关闭。

需要注意的是，与纯Flutter应用不同，原生应用混编Flutter由于涉及到原生页面与Flutter页面之间切换，因此导航栈内可能会出现多个Flutter容器的情况，即多个Flutter实例。

Flutter实例的初始化成本非常高昂，每启动一个Flutter实例，就会创建一套新的渲染机制，即Flutter Engine，以及底层的Isolate。而这些实例之间的内存是不互相共享的，会带来较大的系统资源消耗。

因此我们在实际业务开发中，应该尽量用Flutter去开发闭环的业务模块，原生只需要能够跳转到Flutter模块，剩下的业务都应该在Flutter内部完成，而**尽量避免Flutter页面又跳回到原生页面，原生页面又启动新的Flutter实例的情况**。

为了解决混编工程中Flutter多实例的问题，业界有两种解决方案：

- 以今日头条为代表的[修改Flutter Engine源码](https://mp.weixin.qq.com/s/-vyU1JQzdGLUmLGHRImIvg)，使多FlutterView实例对应的多Flutter Engine能够在底层共享Isolate；
- 以闲鱼为代表的[共享FlutterView](https://www.infoq.cn/article/VBqfCIuwdjtU_CmcKaEu)，即由原生层驱动Flutter层渲染内容的方案。

坦白说，这两种方案各有不足：

- 前者涉及到修改Flutter源码，不仅开发维护成本高，而且增加了线程模型和内存回收出现异常的概率，稳定性不可控。
- 后者涉及到跨渲染引擎的hack，包括Flutter页面的新建、缓存和内存回收等机制，因此在一些低端机或是处理页面切换动画时，容易出现渲染Bug。
- 除此之外，这两种方式均与Flutter的内部实现绑定较紧，因此在处理Flutter SDK版本升级时往往需要耗费较大的适配成本。

综合来说，目前这两种解决方案都不够完美。所以，在Flutter官方支持多实例单引擎之前，我们还是尽量在产品模块层面，保证应用内不要出现多个Flutter容器实例吧。

我把今天分享所涉及到的知识点打包到了GitHub（[flutter_module_page](https://github.com/cyndibaby905/29_flutter_module_page)、[android_demo](https://github.com/cyndibaby905/29_android_hybrid_demo)、[iOS_demo](https://github.com/cyndibaby905/29_ios_hybrid_demo)）中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留两道思考题吧。

1. 请在openNativePage方法的基础上，增加页面id的功能，可以支持在Flutter页面打开任意的原生页面。
2. 混编工程中会出现两种页面过渡动画：原生页面之间的切换动画、Flutter页面之间的切换动画。请你思考下，如何能够确保这两种页面过渡动画在应用整体的效果是一致的。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 为什么需要做状态管理，怎么做？

你好，我是陈航。

在上一篇文章中，我与你分享了如何在原生混编Flutter工程中管理混合导航栈，应对跨渲染引擎的页面跳转，即解决原生页面如何切换到Flutter页面，以及Flutter页面如何切换到原生页面的问题。

如果说跨渲染引擎页面切换的关键在于，如何确保页面跳转的渲染体验一致性，那么跨组件（页面）之间保持数据共享的关键就在于，如何清晰地维护组件共用的数据状态了。在第20篇文章“[关于跨组件传递数据，你只需要记住这三招](https://time.geekbang.org/column/article/116382)”中，我已经与你介绍了InheritedWidget、Notification和EventBus这3种数据传递机制，通过它们可以实现组件间的单向数据传递。

如果我们的应用足够简单，数据流动的方向和顺序是清晰的，我们只需要将数据映射成视图就可以了。作为声明式的框架，Flutter可以自动处理数据到渲染的全过程，通常并不需要状态管理。

但，随着产品需求迭代节奏加快，项目逐渐变得庞大时，我们往往就需要管理不同组件、不同页面之间共享的数据关系。当需要共享的数据关系达到几十上百个的时候，我们就很难保持清晰的数据流动方向和顺序了，导致应用内各种数据传递嵌套和回调满天飞。在这个时候，我们迫切需要一个解决方案，来帮助我们理清楚这些共享数据的关系，于是状态管理框架便应运而生。

Flutter在设计声明式UI上借鉴了不少React的设计思想，因此涌现了诸如flutter_redux、flutter_mobx 、fish_redux等基于前端设计理念的状态管理框架。但这些框架大都比较复杂，且需要对框架设计概念有一定理解，学习门槛相对较高。

而源自Flutter官方的状态管理框架Provider则相对简单得多，不仅容易理解，而且框架的入侵性小，还可以方便地组合和控制UI刷新粒度。因此，在Google I/O 2019大会一经面世，Provider就成为了官方推荐的状态管理方式之一。

那么今天，我们就来聊聊Provider到底怎么用吧。

#### Provider

从名字就可以看出，Provider是一个用来提供数据的框架。它是InheritedWidget的语法糖，提供了依赖注入的功能，允许在Widget树中更加灵活地处理和传递数据。

那么，什么是依赖注入呢？通俗地说，依赖注入是一种可以让我们在需要时提取到所需资源的机制，即：预先将某种“资源”放到程序中某个我们都可以访问的位置，当需要使用这种“资源”时，直接去这个位置拿即可，而无需关心“资源”是谁放进去的。

所以，为了使用Provider，我们需要解决以下3个问题：

- 资源（即数据状态）如何封装？
- 资源放在哪儿，才都能访问得到？
- 具体使用时，如何取出资源？

接下来，我通过一个例子来与你演示如何使用Provider。

在下面的示例中，我们有两个独立的页面FirstPage和SecondPage，它们会共享计数器的状态：其中FirstPage负责读，SecondPage负责读和写。

在使用Provider之前，我们**首先需要在pubspec.yaml文件中添加Provider的依赖**：

```
dependencies:
  flutter:
    sdk: flutter
  provider: 3.0.0+1  #provider依赖
```

添加好Provider的依赖后，我们就可以进行数据状态的封装了。这里，我们只有一个状态需要共享，即count。由于第二个页面还需要修改状态，因此我们还需要在数据状态的封装上包含更改数据的方法：

```
//定义需要共享的数据模型，通过混入ChangeNotifier管理听众
class CounterModel with ChangeNotifier {
  int _count = 0;
  //读方法
  int get counter => _count;
  //写方法
  void increment() {
    _count++;
    notifyListeners();//通知听众刷新
  }
}
```

可以看到，我们在资源封装类中使用mixin混入了ChangeNotifier。这个类能够帮助我们管理所有依赖资源封装类的听众。当资源封装类调用notifyListeners时，它会通知所有听众进行刷新。

**资源已经封装完毕，接下来我们就需要考虑把它放到哪儿了。**

因为Provider实际上是InheritedWidget的语法糖，所以通过Provider传递的数据从数据流动方向来看，是由父到子（或者反过来）。这时我们就明白了，原来需要把资源放到FirstPage和SecondPage的父Widget，也就是应用程序的实例MyApp中（当然，把资源放到更高的层级也是可以的，比如放到main函数中）：

```
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
     //通过Provider组件封装数据资源
    return ChangeNotifierProvider.value(
        value: CounterModel(),//需要共享的数据资源
        child: MaterialApp(
          home: FirstPage(),
        )
    );
  }
}
```

可以看到，既然Provider是InheritedWidget的语法糖，因此它也是一个Widget。所以，我们直接在MaterialApp的外层使用Provider进行包装，就可以把数据资源依赖注入到应用中。

这里需要注意的是，由于封装的数据资源不仅需要为子Widget提供读的能力，还要提供写的能力，因此我们需要使用Provider的升级版ChangeNotifierProvider。而如果只需要为子Widget提供读能力，直接使用Provider即可。

**最后，在注入数据资源完成之后，我们就可以在FirstPage和SecondPage这两个子Widget完成数据的读写操作了。**

关于读数据，与InheritedWidget一样，我们可以通过Provider.of方法来获取资源数据。而如果我们想写数据，则需要通过获取到的资源数据，调用其暴露的更新数据方法（本例中对应的是increment），代码如下所示：

```
//第一个页面，负责读数据
class FirstPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //取出资源
    final _counter = Provider.of<CounterModel>(context);
    return Scaffold(
      //展示资源中的数据
      body: Text('Counter: ${_counter.counter}'),
      //跳转到SecondPage
      floatingActionButton: FloatingActionButton(
        onPressed: () => Navigator.of(context).push(MaterialPageRoute(builder: (context) => SecondPage()))
      ));
  }
}

//第二个页面，负责读写数据
class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //取出资源
    final _counter = Provider.of<CounterModel>(context);
    return Scaffold(
      //展示资源中的数据
      body: Text('Counter: ${_counter.counter}'),
      //用资源更新方法来设置按钮点击回调
      floatingActionButton:FloatingActionButton(
          onPressed: _counter.increment,
          child: Icon(Icons.add),
     ));
  }
}
```

运行代码，试着多点击几次第二个界面的“+”按钮，关闭第二个界面，可以看到第一个界面也同步到了按钮的点击数。

![f000b66c231943f0b2059129f2a24565](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/f000b66c231943f0b2059129f2a24565.jpg)

图1 Provider使用示例

#### Consumer

通过上面的示例可以看到，使用Provider.of获取资源，可以得到资源暴露的数据的读写接口，在实现数据的共享和同步上还是比较简单的。但是，**滥用Provider.of方法也有副作用，那就是当数据更新时，页面中其他的子Widget也会跟着一起刷新。**

为验证这一点，我们以第二个界面右下角FloatingActionButton中的子Widget “+”Icon为例做个测试。

首先，为了打印出Icon控件每一次刷新的情况，我们需要自定义一个控件TestIcon，并在其build方法中返回Icon实例的同时，打印一句话：

```
//用于打印build方法执行情况的自定义控件
class TestIcon extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    print("TestIcon build");
    return Icon(Icons.add);//返回Icon实例
  }
}
```

然后，我们用TestIcon控件，替换掉SecondPage中FloatingActionButton的Icon子Widget：

```
class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //取出共享的数据资源
    final _counter = Provider.of<CounterModel>(context);
    return Scaffold(
     ...
      floatingActionButton:FloatingActionButton(
          onPressed: _counter.increment,
          child: TestIcon(),//替换掉原有的Icon(Icons.add)
     ));
  }
```

运行这段实例，然后在第二个页面多次点击“+”按钮，观察控制台输出：

```
I/flutter (21595): TestIcon build
I/flutter (21595): TestIcon build
I/flutter (21595): TestIcon build
I/flutter (21595): TestIcon build
I/flutter (21595): TestIcon build
```

可以看到，TestIcon控件本来是一个不需要刷新的StatelessWidget，但却因为其父Widget FloatingActionButton所依赖的数据资源counter发生了变化，导致它也要跟着刷新。

那么，**有没有办法能够在数据资源发生变化时，只刷新对资源存在依赖关系的Widget，而其他Widget保持不变呢？**

答案当然是可以的。

在本次分享一开始时，我曾说Provider可以精确地控制UI刷新粒度，而这一切是基于Consumer实现的。Consumer使用了Builder模式创建UI，收到更新通知就会通过builder重新构建Widget。

接下来，我们就看看**如何使用Consumer来改造SecondPage**吧。

在下面的例子中，我们在SecondPage中去掉了Provider.of方法来获取counter的语句，在其真正需要这个数据资源的两个子Widget，即Text和FloatingActionButton中，使用Consumer来对它们进行了一层包装：

```
class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //使用Consumer来封装counter的读取
      body: Consumer<CounterModel>(
        //builder函数可以直接获取到counter参数
        builder: (context, CounterModel counter, _) => Text('Value: ${counter.counter}')),
      //使用Consumer来封装increment的读取
      floatingActionButton: Consumer<CounterModel>(
        //builder函数可以直接获取到increment参数
        builder: (context, CounterModel counter, child) => FloatingActionButton(
          onPressed: counter.increment,
          child: child,
        ),
        child: TestIcon(),
      ),
    );
  }
}
```

可以看到，Consumer中的builder实际上就是真正刷新UI的函数，它接收3个参数，即context、model和child。其中：context是Widget的build方法传进来的BuildContext，model是我们需要的数据资源，而child则用来构建那些与数据资源无关的部分。在数据资源发生变更时，builder会多次执行，但child不会重建。

运行这段代码，可以发现，不管我们点击了多少次“+”按钮，TestIcon控件始终没有发生销毁重建。

#### 多状态的资源封装

通过上面的例子，我们学习了Provider是如何共享一个数据状态的。那么，如果有多个数据状态需要共享，我们又该如何处理呢？

其实也不难。接下来，我就**按照封装、注入和读写这3个步骤，与你介绍多个数据状态的共享**。

在处理多个数据状态共享之前，我们需要先扩展一下上面计数器状态共享的例子，让两个页面之间展示计数器数据的Text能够共享App传递的字体大小。

**首先，我们来看看如何封装**。

多个数据状态与单个数据的封装并无不同，如果需要支持数据的读写，我们需要一个接一个地为每一个数据状态都封装一个单独的资源封装类；而如果数据是只读的，则可以直接传入原始的数据对象，从而省去资源封装的过程。

**接下来，我们再看看如何实现注入。**

在单状态的案例中，我们通过Provider的升级版ChangeNotifierProvider实现了可读写资源的注入，而如果我们想注入多个资源，则可以使用Provider的另一个升级版MultiProvider，来实现多个Provider的组合注入。

在下面的例子中，我们通过MultiProvider往App实例内注入了double和CounterModel这两个资源Provider：

```
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(providers: [
      Provider.value(value: 30.0),//注入字体大小
      ChangeNotifierProvider.value(value: CounterModel())//注入计数器实例
    ],
    child: MaterialApp(
      home: FirstPage(),
    ));
  }
}
```

在完成了多个资源的注入后，最后我们来看看**如何获取这些资源**。

这里，我们还是使用Provider.of方式来获取资源。相较于单状态资源的获取来说，获取多个资源时，我们只需要依次读取每一个资源即可：

```
final _counter = Provider.of<CounterModel>(context);//获取计时器实例
final textSize = Provider.of<double>(context);//获取字体大小
```

而如果以Consumer的方式来获取资源的话，我们只要使用Consumer2对象（这个对象提供了读取两个数据资源的能力），就可以一次性地获取字体大小与计数器实例这两个数据资源：

```
//使用Consumer2获取两个数据资源
Consumer2<CounterModel,double>(
  //builder函数以参数的形式提供了数据资源
  builder: (context, CounterModel counter, double textSize, _) => Text(
      'Value: ${counter.counter}',
      style: TextStyle(fontSize: textSize))
)
```

可以看到，Consumer2与Consumer的使用方式基本一致，只不过是在builder方法中多了一个数据资源参数。事实上，如果你希望在子Widget中共享更多的数据，我们最多可以使用到Consumer6，即共享6个数据资源。

#### 总结

好了，今天的分享就到这里，我们总结一下今天的主要内容吧。

我与你介绍了在Flutter中通过Provider进行状态管理的方法，Provider以InheritedWidget语法糖的方式，通过数据资源封装、数据注入和数据读写这3个步骤，为我们实现了跨组件（跨页面）之间的数据共享。

我们既可以用Provider来实现静态的数据读传递，也可以使用ChangeNotifierProvider来实现动态的数据读写传递，还可以通过MultiProvider来实现多个数据资源的共享。

在具体使用数据时，Provider.of和Consumer都可以实现数据的读取，并且Consumer还可以控制UI刷新的粒度，避免与数据无关的组件的无谓刷新。

可以看到，通过Provider来实现数据传递，无论在单个页面内还是在整个App之间，我们都可以很方便地实现状态管理，搞定那些通过StatefulWidget无法实现的场景，进而开发出简单、层次清晰、可扩展性高的应用。事实上，当我们使用Provider后，我们就再也不需要使用StatefulWidget了。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/30_provider_demo)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留一道思考题吧。

使用Provider可以实现2个同样类型的对象共享，你知道应该如何实现吗？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何实现原生推送能力？

你好，我是陈航。

在上一篇文章中，我与你分享了如何使用Provider去维护Flutter组件共用的数据状态。在Flutter中状态即数据，通过数据资源封装、注入和读写这三步，我们不仅可以实现跨组件之间的数据共享，还能精确控制UI刷新粒度，避免无关组件的刷新。

其实，数据共享不仅存在于客户端内部，同样也存在于服务端与客户端之间。比如，有新的微博评论，或者是发生了重大新闻，我们都需要在服务端把这些状态变更的消息实时推送到客户端，提醒用户有新的内容。有时，我们还会针对特定的用户画像，通过推送实现精准的营销信息触达。

可以说，消息推送是增强用户黏性，促进用户量增长的重要手段。那么，消息推送的流程是什么样的呢？

#### 消息推送流程

手机推送每天那么多，导致在我们看来这很简单啊。但其实，消息推送是一个横跨业务服务器、第三方推送服务托管厂商、操作系统长连接推送服务、用户终端、手机应用五方的复杂业务应用场景。

在iOS上，苹果推送服务（APNs）接管了系统所有应用的消息通知需求；而Android原生，则提供了类似Firebase的云消息传递机制（FCM），可以实现统一的推送托管服务。

当某应用需要发送消息通知时，这则消息会由应用的服务器先发给苹果或Google，经由APNs或FCM被发送到设备，设备操作系统在完成解析后，最终把消息转给所属应用。这个流程的示意图，如下所示。

![e202650fb9ef47e1b37d3d18f05aa002](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e202650fb9ef47e1b37d3d18f05aa002.jpg)

图1 原生消息推送流程

不过，Google服务在大陆地区使用并不稳定，因此国行Android手机通常会把Google服务换成自己的服务，定制一套推送标准。而这对开发者来说，无疑是增大了适配负担。所以针对Android端，我们通常会使用第三方推送服务，比如极光推送、友盟推送等。

虽然这些第三方推送服务使用自建的长连接，无法享受操作系统底层的优化，但它们会对所有使用推送服务的App共享推送通道，只要有一个使用第三方推送服务的应用没被系统杀死，就可以让消息及时送达。

而另一方面，这些第三方服务简化了业务服务器与手机推送服务建立连接的操作，使得我们的业务服务器通过简单的API调用就可以完成消息推送。

而为了保持Android/iOS方案的统一，在iOS上我们也会使用封装了APNs通信的第三方推送服务。

第三方推送的服务流程，如下图所示。

![59fb25d6099b4507946086096957b9a0](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/59fb25d6099b4507946086096957b9a0.jpg)

图2 第三方推送服务流程

这些第三方推送服务厂商提供的能力和接入流程大都一致，考虑到极光的社区和生态相对活跃，所以今天我们就以极光为例，来看看在Flutter应用中如何才能引用原生的推送能力。

#### 原生推送接入流程

要想在Flutter中接收推送消息，我们需要把原生的推送能力暴露给Flutter应用，即在原生代码宿主实现推送能力（极光SDK）的接入，并通过方法通道提供给Dart层感知推送消息的机制。

##### 插件工程

在[第26篇](https://time.geekbang.org/column/article/127601)文章中，我们学习了如何在原生工程中的Flutter应用入口注册原生代码宿主回调，从而实现Dart层调用原生接口的方案。这种方案简单直接，适用于Dart层与原生接口之间交互代码量少、数据流动清晰的场景。

但对于推送这种涉及Dart与原生多方数据流转、代码量大的模块，这种与工程耦合的方案就不利于独立开发维护了。这时，我们需要使用Flutter提供的插件工程对其进行单独封装。

Flutter的插件工程与普通的应用工程类似，都有android和ios目录，这也是我们完成平台相关逻辑代码的地方，而Flutter工程插件的注册，则仍会在应用的入口完成。除此之外，插件工程还内嵌了一个example工程，这是一个引用了插件代码的普通Flutter应用工程。我们通过example工程，可以直接调试插件功能。

![4abb1d7b6c454e46a27af0c4d2065639](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4abb1d7b6c454e46a27af0c4d2065639.jpg)

图3 插件工程目录结构

在了解了整体工程的目录结构之后，接下来我们需要去Dart插件代码所在的flutter_push_plugin.dart文件，实现Dart层的推送接口封装。

##### Dart接口实现

为了实现消息的准确触达，我们需要提供一个可以标识手机上App的地址，即token或id。一旦完成地址的上报，我们就可以等待业务服务器给我们发消息了。

因为我们需要使用极光这样的第三方推送服务，所以还得进行一些前置的应用信息关联绑定，以及SDK的初始化工作。可以看到，对于一个应用而言，接入推送的过程可以拆解为以下三步：

1. 初始化极光SDK；
2. 获取地址id；
3. 注册消息通知。

这三步对应着在Dart层需要封装的3个原生接口调用：setup、registrationID和setOpenNotificationHandler。

前两个接口是在方法通道上调用原生代码宿主提供的方法，而注册消息通知的回调函数setOpenNotificationHandler则相反，是原生代码宿主在方法通道上调用Dart层所提供的事件回调，因此我们需要在方法通道上为原生代码宿主注册反向回调方法，让原生代码宿主收到消息后可以直接通知它。

另外，考虑到推送是整个应用共享的能力，因此我们将FlutterPushPlugin这个类封装成了单例：

```
//Flutter Push插件
class FlutterPushPlugin  {
  //单例
  static final FlutterPushPlugin _instance = new FlutterPushPlugin.private(const MethodChannel('flutter_push_plugin'));
  //方法通道
  final MethodChannel _channel;
  //消息回调
  EventHandler _onOpenNotification;
  //构造方法
  FlutterPushPlugin.private(MethodChannel channel) : _channel = channel {
    //注册原生反向回调方法，让原生代码宿主可以执行onOpenNotification方法
    _channel.setMethodCallHandler(_handleMethod);
  }
  //初始化极光SDK
  setupWithAppID(String appID) {
    _channel.invokeMethod("setup", appID);
  }
  //注册消息通知
  setOpenNotificationHandler(EventHandler onOpenNotification) {
    _onOpenNotification = onOpenNotification;
  }

  //注册原生反向回调方法，让原生代码宿主可以执行onOpenNotification方法
  Future<Null> _handleMethod(MethodCall call) {
    switch (call.method) {
      case "onOpenNotification":
        return _onOpenNotification(call.arguments);
      default:
        throw new UnsupportedError("Unrecognized Event");
    }
  }
  //获取地址id
  Future<String> get registrationID async {
    final String regID = await _channel.invokeMethod('getRegistrationID');
    return regID;
  }
}
```

Dart层是原生代码宿主的代理，可以看到这一层的接口设计算是简单。接下来，我们分别去接管推送的Android和iOS平台上完成相应的实现。

##### Android接口实现

考虑到Android平台的推送配置工作相对较少，因此我们先用Android Studio打开example下的android工程进行插件开发工作。需要注意的是，由于android子工程的运行依赖于Flutter工程编译构建产物，所以在打开android工程进行开发前，你需要确保整个工程代码至少build过一次，否则IDE会报错。

> 备注：以下操作步骤参考[极光Android SDK集成指南](https://docs.jiguang.cn//jpush/client/Android/android_guide/)。

首先，我们需要在插件工程下的build.gradle引入极光SDK，即jpush与jcore：

```
dependencies {
    implementation 'cn.jiguang.sdk:jpush:3.3.4'
    implementation 'cn.jiguang.sdk:jcore:2.1.2'
}
```

然后，在原生接口FlutterPushPlugin类中，依次把Dart层封装的3个接口调用，即setup、getRegistrationID与onOpenNotification，提供极光Android SDK的实现版本。

需要注意的是，由于极光Android SDK的信息绑定是在应用的打包配置里设置，并不需要通过代码完成（iOS才需要），因此setup方法的Android版本是一个空实现：

```
public class FlutterPushPlugin implements MethodCallHandler {
  //注册器，通常为MainActivity
  public final Registrar registrar;
  //方法通道
  private final MethodChannel channel;
  //插件实例
  public static FlutterPushPlugin instance;
  //注册插件
  public static void registerWith(Registrar registrar) {
    //注册方法通道
    final MethodChannel channel = new MethodChannel(registrar.messenger(), "flutter_push_plugin");
    instance = new FlutterPushPlugin(registrar, channel);
    channel.setMethodCallHandler(instance);
    //把初始化极光SDK提前至插件注册时
    JPushInterface.setDebugMode(true);
    JPushInterface.init(registrar.activity().getApplicationContext());
  }
  //私有构造方法
  private FlutterPushPlugin(Registrar registrar, MethodChannel channel) {
    this.registrar = registrar;
    this.channel = channel;
  }
  //方法回调
  @Override
  public void onMethodCall(MethodCall call, Result result) {
    if (call.method.equals("setup")) {
      //极光Android SDK的初始化工作需要在App工程中配置，因此不需要代码实现
      result.success(0);
    }
    else if (call.method.equals("getRegistrationID")) {
      //获取极光推送地址标识符
        result.success(JPushInterface.getRegistrationID(registrar.context()));
    } else {
      result.notImplemented();
    }
  }

  public void callbackNotificationOpened(NotificationMessage message) {
    //将推送消息回调给Dart层
      channel.invokeMethod("onOpenNotification",message.notificationContent);
  }
}
```

可以看到，我们的FlutterPushPlugin类中，仅提供了callbackNotificationOpened这个工具方法，用于推送消息参数回调给Dart，但这个类本身并没有去监听极光SDK的推送消息。

为了获取推送消息，我们分别需要继承极光SDK提供的两个类：JCommonService和JPushMessageReceiver。

- JCommonService是一个后台Service，实际上是极光共享长连通道的核心，可以在多手机平台上使得推送通道更稳定。
- JPushMessageReceiver则是一个BroadcastReceiver，推送消息的获取都是通过它实现的。我们可以通过覆盖其onNotifyMessageOpened方法，从而在用户点击系统推送消息时获取到通知。

作为BroadcastReceiver的JPushMessageReceiver，可以长期在后台存活，监听远端推送消息，但Flutter可就不行了，操作系统会随时释放掉后台应用所占用的资源。因此，**在用户点击推送时，我们在收到相应的消息回调后，需要做的第一件事情不是立刻通知Flutter，而是应该启动应用的MainActivity。**在确保Flutter已经完全初始化后，才能通知Flutter有新的推送消息。

因此在下面的代码中，我们在打开MainActivity后，等待了1秒，才执行相应的Flutter回调通知：

```
//JPushXCustomService.java
//长连通道核心，可以使推送通道更稳定
public class JPushXCustomService extends JCommonService {
}

//JPushXMessageReceiver.java
//获取推送消息的Receiver
public class JPushXMessageReceiver extends JPushMessageReceiver {
    //用户点击推送消息回调
    @Override
    public void onNotifyMessageOpened(Context context, final NotificationMessage message) {
        try {
            //找到MainActivity
            String mainClassName = context.getApplicationContext().getPackageName() + ".MainActivity";
            Intent i = new Intent(context, Class.forName(mainClassName));
            i.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_SINGLE_TOP);
            //启动主Activity
            context.startActivity(i);
        } catch (Exception e) {
            Log.e("tag","找不到MainActivity");
        }
        new Timer().schedule(new TimerTask() {
            @Override
            public void run() {
                FlutterPushPlugin.instance.callbackNotificationOpened(message);
            }
        },1000); // 延迟1秒通知Dart
    }
}
```

最后，我们还需要在插件工程的AndroidManifest.xml中，分别声明receiver JPushXMessageReceiver和service JPushXCustomService，完成对系统的注册：

```
...
<application>
    <!--注册推送消息接收类 -->
    <receiver android:name=".JPushXMessageReceiver">
        <intent-filter>
            <action android:name="cn.jpush.android.intent.RECEIVE_MESSAGE" />
            <category android:name="${applicationId}" />
        </intent-filter>
    </receiver>
    <!--注册长连通道Service -->
    <service android:name=".JPushXCustomService"
        android:enabled="true"
        android:exported="false"
        android:process=":pushcore">
        <intent-filter>
            <action android:name="cn.jiguang.user.service.action" />
        </intent-filter>
    </service>
</application>
...
```

接收消息和回调消息的功能完成后，FlutterPushPlugin插件的Android部分就搞定了。接下来，我们去开发插件的iOS部分。

##### iOS接口实现

与Android类似，我们需要使用Xcode打开example下的ios工程进行插件开发工作。同样，在打开ios工程前，你需要确保整个工程代码至少build过一次，否则IDE会报错。

> 备注：以下操作步骤参考[极光iOS SDK集成指南](https://docs.jiguang.cn//jpush/client/iOS/ios_guide_new/)

首先，我们需要在插件工程下的flutter_push_plugin.podspec文件中引入极光SDK，即jpush。这里，我们选用了不使用广告id的版本：

```
Pod::Spec.new do |s|
  ...
  s.dependency 'JPush', '3.2.2-noidfa'
end
```

然后，在原生接口FlutterPushPlugin类中，同样依次为setup、getRegistrationID与onOpenNotification，提供极光 iOS SDK的实现版本。

需要注意的是，APNs的推送消息是在ApplicationDelegate中回调的，所以我们需要在注册插件时，为插件提供同名的回调函数，让极光SDK把推送消息转发到插件的回调函数中。

与Android类似，在极光SDK收到推送消息时，我们的应用可能处于后台，因此在用户点击了推送消息，把Flutter应用唤醒时，我们应该在确保Flutter已经完全初始化后，才能通知Flutter有新的推送消息。

因此在下面的代码中，我们在用户点击了推送消息后也等待了1秒，才执行相应的Flutter回调通知：

```
@implementation FlutterPushPlugin
//注册插件
+ (void)registerWithRegistrar:(NSObject<FlutterPluginRegistrar>*)registrar {
    //注册方法通道
    FlutterMethodChannel* channel = [FlutterMethodChannel methodChannelWithName:@"flutter_push_plugin" binaryMessenger:[registrar messenger]];
    //初始化插件实例，绑定方法通道
    FlutterPushPlugin* instance = [[FlutterPushPlugin alloc] init];
    instance.channel = channel;
    //为插件提供ApplicationDelegate回调方法
    [registrar addApplicationDelegate:instance];
    //注册方法通道回调函数
    [registrar addMethodCallDelegate:instance channel:channel];
}
//处理方法调用
- (void)handleMethodCall:(FlutterMethodCall*)call result:(FlutterResult)result {
    if([@"setup" isEqualToString:call.method]) {
        //极光SDK初始化方法
        [JPUSHService setupWithOption:self.launchOptions appKey:call.arguments channel:@"App Store" apsForProduction:YES advertisingIdentifier:nil];
    } else if ([@"getRegistrationID" isEqualToString:call.method]) {
        //获取极光推送地址标识符
        [JPUSHService registrationIDCompletionHandler:^(int resCode, NSString *registrationID) {
            result(registrationID);
        }];
    } else {
        //方法未实现
        result(FlutterMethodNotImplemented);
  }
}
//应用程序启动回调
-(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    //初始化极光推送服务
    JPUSHRegisterEntity * entity = [[JPUSHRegisterEntity alloc] init];
    //设置推送权限
    entity.types = JPAuthorizationOptionAlert|JPAuthorizationOptionBadge|JPAuthorizationOptionSound;
    //请求推送服务
    [JPUSHService registerForRemoteNotificationConfig:entity delegate:self];
    //存储App启动状态，用于后续初始化调用
    self.launchOptions = launchOptions;
    return YES;
}
//推送token回调
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    ///注册DeviceToken，换取极光推送地址标识符
    [JPUSHService registerDeviceToken:deviceToken];
}
//推送被点击回调
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void(^)(void))completionHandler {
    //获取推送消息
    NSDictionary * userInfo = response.notification.request.content.userInfo;
    NSString *content = userInfo[@"aps"][@"alert"];
    if ([content isKindOfClass:[NSDictionary class]]) {
        content = userInfo[@"aps"][@"alert"][@"body"];
    }
    //延迟1秒通知Flutter，确保Flutter应用已完成初始化
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
        [self.channel invokeMethod:@"onOpenNotification" arguments:content];
    });
    //清除应用的小红点
    UIApplication.sharedApplication.applicationIconBadgeNumber = 0;
    //通知系统，推送回调处理完毕
    completionHandler();
}
//前台应用收到了推送消息
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(NSInteger options))completionHandler {
    //通知系统展示推送消息提示
    completionHandler(UNNotificationPresentationOptionAlert);
}
@end
```

至此，在完成了极光iOS SDK的接口封装之后，FlutterPushPlugin插件的iOS部分也搞定了。

FlutterPushPlugin插件为Flutter应用提供了原生推送的封装，不过要想example工程能够真正地接收到推送消息，我们还需要对exmaple工程进行最后的配置，即：为它提供应用推送证书，并关联极光应用配置。

##### 应用工程配置

在单独为Android/iOS应用进行推送配置之前，我们首先需要去[极光的官方网站](https://www.jiguang.cn/dev2/#/overview/appCardList)，为example应用注册一个唯一标识符（即AppKey）：

![e2474ca2d4504b76a397b9ef0e58d65b](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e2474ca2d4504b76a397b9ef0e58d65b.jpg)

图4 极光应用注册

在得到了AppKey之后，我们需要**依次进行Android与iOS的配置工作**。

Android的配置工作相对简单，整个配置过程完全是应用与极光SDK的关联工作。

首先，根据example的Android工程包名，完成Android工程的推送注册：

![e005fff9e8d047f2976fe77539cb0816](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e005fff9e8d047f2976fe77539cb0816.jpg)

图5 example Android推送注册

然后，通过AppKey，在app的build.gradle文件中实现极光信息的绑定：

```
defaultConfig {
   ...
   //ndk支持架构
    ndk {
        abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a'
    }

    manifestPlaceholders = [
            JPUSH_PKGNAME : applicationId, //包名
            JPUSH_APPKEY : "f861910af12a509b34e266c2", //JPush 上注册的包名对应的Appkey
            JPUSH_CHANNEL : "developer-default", //填写默认值即可
    ]
}
```

至此，Android部分的所有配置工作和接口实现都已经搞定了。接下来，我们再来看看iOS的配置实现。

**iOS的应用配置相对Android会繁琐一些**，因为整个配置过程涉及应用、苹果APNs服务、极光三方之间的信息关联。

除了需要在应用内绑定极光信息之外（即handleMethodCall中的setup方法），还需要在[苹果的开发者官网](https://developer.apple.com/)提前申请苹果的推送证书。关于申请证书，苹果提供了.p12证书和APNs Auth Key两种鉴权方式。

这里，我推荐使用更为简单的Auth Key方式。申请推送证书的过程，极光官网提供了详细的[注册步骤](https://docs.jiguang.cn//jpush/client/iOS/ios_cer_guide/)，这里我就不再赘述了。需要注意的是，申请iOS的推送证书时，你只能使用付费的苹果开发者账号。

在拿到了APNs Auth Key之后，我们同样需要去极光官网，根据Bundle ID进行推送设置，并把Auth Key上传至极光进行托管，由它完成与苹果的鉴权工作：

![0f06712c393a4b449c3f57e02bedb842](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0f06712c393a4b449c3f57e02bedb842.jpg)

图6 example iOS推送注册

通过上面的步骤，我们已经完成了将推送证书与极光信息绑定的操作，接下来，我们**回到Xcode打开的example工程，进行最后的配置工作**。

首先，我们需要为example工程开启Application Target的Capabilities->Push Notifications选项，启动应用的推送能力支持，如下图所示：

![c86be878d064468eb5f00c39b04afdb6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c86be878d064468eb5f00c39b04afdb6.jpg)

图7 example iOS推送配置

然后，我们需要切换到Application Target的Info面板，手动配置NSAppTransportSecurity键值对，以支持极光SDK非https域名服务：

![6da62f949d42436dac0b2eb74b735701](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/6da62f949d42436dac0b2eb74b735701.jpg)

图8 example iOS支持Http配置

最后，在Info tab下的Bundle identifier项，把我们刚刚在极光官网注册的Bundle ID显式地更新进去：

![ab911b12ac754fd09c1143c67b4ea69e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ab911b12ac754fd09c1143c67b4ea69e.jpg)

图9 Bundle ID配置

至此，example工程运行所需的所有原生配置工作和接口实现都已经搞定了。接下来，我们就可以在example工程中的main.dart文件中，使用FlutterPushPlugin插件来实现原生推送能力了。

在下面的代码中，我们在main函数的入口，使用插件单例注册了极光推送服务，随后在应用State初始化时，获取了极光推送地址，并设置了消息推送回调：

```
//获取推送插件单例
FlutterPushPlugin fpush = FlutterPushPlugin();
void main() {
  //使用AppID注册极光推送服务(仅针对iOS平台)
  fpush.setupWithAppID("f861910af12a509b34e266c2");
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  //极光推送地址regID
  String _regID = 'Unknown';
  //接收到的推送消息
  String _notification = "";

  @override
  initState() {
    super.initState();
    //注册推送消息回调
    fpush.setOpenNotificationHandler((String message) async {
      //刷新界面状态，展示推送消息
      setState(() {
        _notification = message;
      });
    });
    //获取推送地址regID
    initPlatformState();
  }

  initPlatformState() async {
    //调用插件封装的regID
    String regID = await fpush.registrationID;
    //刷新界面状态，展示regID
    setState(() {
      _regID = regID;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Column(
            children: <Widget>[
              //展示regID，以及收到的消息
              Text('Running on: $_regID\n'),
              Text('Notification Received: $_notification')
            ],
          ),
        ),
      ),
    );
  }
}
```

点击运行，可以看到，我们的应用已经可以获取到极光推送地址了：

![aaa59bff08bc410ca2bd0986067a0d65](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/aaa59bff08bc410ca2bd0986067a0d65.jpg)

图10 iOS运行示例

![5fe1bfb8c0be47aba43069a10c65abf7](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/5fe1bfb8c0be47aba43069a10c65abf7.jpg)

图11 Android运行示例

接下来，我们再去[极光开发者服务后台](https://www.jiguang.cn/dev2/#/overview/appCardList)发一条真实的推送消息。在服务后台选择我们的App，随后进入极光推送控制台。这时，我们就可以进行消息推送测试了。

在发送通知一栏，我们把通知标题改为“测试”，通知内容设置为“极光推送测试”；在目标人群一栏，由于是测试账号，我们可以直接选择“广播所有人”，如果你希望精确定位到接收方，也可以提供在应用中获取到的极光推送地址（即Registration ID）：

![4b0f21319bb84d6185e9d7ba8c866186](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4b0f21319bb84d6185e9d7ba8c866186.jpg)

图12 极光推送后台

点击发送预览并确认，可以看到，我们的应用不仅可以被来自极光的推送消息唤醒，还可以在Flutter应用内收到来自原生宿主转发的消息内容：

![82048905509b41408ef8b3a093105372](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/82048905509b41408ef8b3a093105372.jpg)

图13 iOS推送消息

![d015d04a7c71424f8164418046292924](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d015d04a7c71424f8164418046292924.jpg)

图 14 Android推送消息

#### 总结

好了，今天的分享就到这里。我们一起来小结一下吧。

我们以Flutter插件工程的方式，为极光SDK提供了一个Dart层的封装。插件工程同时提供了iOS和Android目录，我们可以在这两个目录下完成原生代码宿主封装，不仅可以为Dart层提供接口正向回调（比如，初始化、获取极光推送地址），还可以通过方法通道以反向回调的方式将推送消息转发给Dart。

今天，我和你分享了很多原生代码宿主的配置、绑定、注册的逻辑。不难发现，推送过程链路长、涉众多、配置复杂，要想在Flutter完全实现原生推送能力，工作量主要集中在原生代码宿主，Dart层能做的事情并不多。

我把今天分享所改造的[Flutter_Push_Plugin](https://github.com/cyndibaby905/31_flutter_push_plugin)放到了GitHub中，你可以把插件工程下载下来，多运行几次，体会插件工程与普通Flutter工程的异同，并加深对消息推送全流程的认识。其中，Flutter_Push_Plugin提供了实现原生推送功能的最小集合，你可以根据实际需求完善这个插件。

需要注意的是，我们今天的实际工程演示是通过内嵌的example工程示例所完成的，如果你有一个独立的Flutter工程（比如[Flutter_Push_Demo](https://github.com/cyndibaby905/31_flutter_push_demo)）需要接入Flutter_Push_Plugin，其配置方式与example工程并无不同，唯一的区别是，需要在pubspec.yaml文件中将对插件的依赖显示地声明出来而已：

```
dependencies:
  flutter_push_plugin:
    git:
      url: https://github.com/cyndibaby905/31_flutter_push_plugin.git
```

#### 思考题

在Flutter_Push_Plugin的原生实现中，用户点击了推送消息把Flutter应用唤醒时，为了确保Flutter完成初始化，我们等待了1秒才执行相应的Flutter回调通知。这段逻辑有需要优化的地方吗？为了让Flutter代码能够更快地收到推送消息，你会如何优化呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 适配国际化，除了多语言我们还需要注意什么_

你好，我是陈航。今天，我们来聊聊Flutter应用的国际化。

借助于App Store与Google Play，我们能够把应用发布到全世界的任何一个应用商店里。应用的（潜在）使用者可能来自于不同国家、说着不同的语言。如果我们想为全世界的使用者提供统一而标准的体验，那么首先就需要让App能够支持多种语言。而这一过程，一般被称为“国际化”。

提起国际化，你可能会认为这等同于翻译App内所有用户可见的文本。其实，这个观点不够精确。**更为准确地描述国际化的工作职责，应该是“涉及语言及地区差异的适配改造过程”。**

比如，如果我们要显示金额，同样的面值，在中国会显示为￥100，而在美国则会显示为$100；又比如，App的引导图，在中国我们可能会选用长城作为背景，而在美国我们则可能会选择金门大桥作为背景。

因此，对一款App做国际化的具体过程，除了翻译文案之外，还需要将货币单位和背景图等资源也设计成可根据不同地区自适应的变量。这也就意味着，我们在设计App架构时，需要提前将语言与地区的差异部分独立出来。

其实，这也是在Flutter中进行国际化的整体思路，即语言差异配置抽取+国际化代码生成。而在语言差异配置抽取的过程中，文案、货币单位，以及背景图资源的处理，其实并没有本质区别。所以在今天的分享中，我会以多语言文案为主，为你讲述在Flutter中如何实现语言与地区差异的独立化，相信在学习完这部分的知识之后，对于其他类型的语言差异你也能够轻松搞定国际化了。

#### Flutter i18n

在Flutter中，国际化的语言和地区的差异性配置，是应用程序代码的一部分。如果要在Flutter中实现文本的国际化，我们需要执行以下几步：

- 首先，实现一个LocalizationsDelegate（即翻译代理），并将所有需要翻译的文案全部声明为它的属性；
- 然后，依次为需要支持的语言地区进行手动翻译适配；
- 最后，在应用程序MaterialApp初始化时，将这个代理类设置为应用程序的翻译回调。

如果我们中途想要新增或者删除某个语系或者文案，都需要修改程序代码。

看到这里你会发现，如果我们想要使用官方提供的国际化方案来设计App架构，不仅工作量大、繁琐，而且极易出错。所以，要开始Flutter应用的国际化道路，我们不如把官方的解决方案扔到一边，直接**从Android Studio中的Flutter i18n插件开始学习**。这个插件在其内部提供了不同语言地区的配置封装，能够帮助我们自动地从翻译稿生成Dart代码。

为了安装Flutter i18n插件，我们需要打开Android Studio的Preference选项，在左边的tab中，切换到Plugins选项，搜索这个插件，点击install即可。安装完成之后再重启Android Studio，这个插件就可以使用了。

![ee5aacb5b239481f924a3cd047bbfb9a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ee5aacb5b239481f924a3cd047bbfb9a.jpg)

图1 Flutter i18n插件安装

Flutter i18n依赖flutter_localizations插件包，所以我们还需要在pubspec.yaml文件里，声明对它的依赖，否则程序会报错：

```
dependencies:
  flutter_localizations:
    sdk: flutter
```

这时，我们会发现在res文件夹下，多了一个values/strings_en.arb的文件。

arb文件是JSON格式的配置，用来存放文案标识符和文案翻译的键值对。所以，我们只要修改了res/values下的arb文件，i18n插件就会自动帮我们生成对应的代码。

strings_en文件，则是系统默认的英文资源配置。为了支持中文，我们还需要在values目录下再增加一个strings_zh.arb文件：

![b0f63491c97e4b83828c8b0ecddc47dd](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/b0f63491c97e4b83828c8b0ecddc47dd.jpg)

图2 arb文件格式

试着修改一下strings_zh.arb文件，可以看到，Flutter i18n插件为我们自动生成了generated/i18n.dart。这个类中不仅以资源标识符属性的方式提供了静态文案的翻译映射，对于通过参数来实现动态文案的message_tip标识符，也自动生成了一个同名内联函数：

![37af717a0b7845ef8f291b19e3a8cd3f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/37af717a0b7845ef8f291b19e3a8cd3f.jpg)

图3 Flutter i18n插件自动生成代码

我们把strings_en.arb继续补全，提供英文版的文案。需要注意的是，i18n.dart是由插件自动生成的，每次arb文件有新的变更都会自动更新，所以切忌手动编辑这个文件。

接下来，我们**以Flutter官方的工程模板，即计数器demo来演示如何在Flutter中实现国际化**。

在下面的代码中，我们在应用程序的入口，即MaterialApp初始化时，为其设置了支持国际化的两个重要参数，即localizationsDelegates与supportedLocales。前者为应用的翻译回调，而后者则为应用所支持的语言地区属性。

S.delegate是Flutter i18n插件自动生成的类，包含了所支持的语言地区属性，以及对应的文案翻译映射。理论上，通过这个类就可以完全实现应用的国际化，但为什么我们在配置应用程序的翻译回调时，除了它之外，还加入了GlobalMaterialLocalizations.delegate与GlobalWidgetsLocalizations.delegate这两个回调呢？

这是因为Flutter提供的Widget，其本身已经支持了国际化，所以我们没必要再翻译一遍，直接用官方的就可以了，而这两个类则就是官方所提供的翻译回调。事实上，我们刚才在pubspec.yaml文件中声明的flutter_localizations插件包，就是Flutter提供的翻译套装，而这两个类就是套装中的著名成员。

在完成了应用程序的国际化配置之后，我们就可以在程序中通过S.of(context)，直接获取arb文件中翻译的文案了。

不过需要注意的是，**提取翻译文案的代码需要在能获取到翻译上下文的前提下才能生效，也就是说只能针对MaterialApp的子Widget生效。**因此，在这种配置方式下，我们是无法对MaterialApp的title属性进行国际化配置的。不过，好在MaterialApp提供了一个回调方法onGenerateTitle，来提供翻译上下文，因此我们可以通过它，实现title文案的国际化：

```
//应用程序入口
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      localizationsDelegates: const [
        S.delegate,//应用程序的翻译回调
        GlobalMaterialLocalizations.delegate,//Material组件的翻译回调
        GlobalWidgetsLocalizations.delegate,//普通Widget的翻译回调
      ],
      supportedLocales: S.delegate.supportedLocales,//支持语系
      //title的国际化回调
      onGenerateTitle: (context){
        return S.of(context).app_title;
      },
      home: MyHomePage(),
    );
  }
}
```

应用的主界面文案的国际化，则相对简单得多了，直接通过S.of(context)方法就可以拿到arb声明的翻译文案了：

```
Widget build(BuildContext context) {
  return Scaffold(
    //获取appBar title的翻译文案
    appBar: AppBar(
      title: Text(S.of(context).main_title),
    ),
    body: Center(
      //传入_counter参数，获取计数器动态文案
      child: Text(
        S.of(context).message_tip(_counter.toString())
          )
    ),
    floatingActionButton: FloatingActionButton(
      onPressed: _incrementCounter,//点击回调
      tooltip: 'Increment',
      child: Icon(Icons.add),
    ),
  );
}
```

在Android手机上，分别切换英文和中文系统，可以看到，计数器应用已经正确地处理了多语言的情况。

![82f938afedd14fedb6eb92a53767524e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/82f938afedd14fedb6eb92a53767524e.jpg)

图4 计数器示例（Android英文系统）

![3ca73ad931bf40d888b3e50917443d9d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/3ca73ad931bf40d888b3e50917443d9d.jpg)

图5 计数器示例（Android中文系统）

由于iOS应用程序有一套自建的语言环境管理机制，默认是英文。为了让iOS应用正确地支持国际化，我们还需要在原生的iOS工程中进行额外的配置。我们打开iOS原生工程，切换到工程面板。在Localization这一项配置中，我们看到iOS工程已经默认支持了英文，所以还需要点击“+”按钮，新增中文：

![c5a59278f7334222a0feb8955dc598be](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c5a59278f7334222a0feb8955dc598be.jpg)

图6 iOS工程中文配置

完成iOS的工程配置后，我们回到Flutter工程，选择iOS手机运行程序。可以看到，计数器的iOS版本也可以正确地支持国际化了。

![f7447f4e3ba243fc8323499f8adee729](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/f7447f4e3ba243fc8323499f8adee729.jpg)

图7 计数器示例（iOS英文系统）

![31c609d45a1d41baaa8a1cc8f90ce66e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/31c609d45a1d41baaa8a1cc8f90ce66e.jpg)

图8 计数器示例（iOS中文系统）

#### 原生工程配置

上面介绍的国际化方案，其实都是在Flutter应用内实现的。而在Flutter框架运行之前，我们是无法访问这些国际化文案的。

Flutter需要原生环境才能运行，但有些文案，比如应用的名称，我们需要在Flutter框架运行之前就为它提供多个语言版本（比如英文版本为computer，中文版本为计数器），这时就需要在对应的原生工程中完成相应的国际化配置了。

**我们先去Android工程下进行应用名称的配置。**

首先，在Android工程中，应用名称是在AndroidManifest.xml文件中application的android:label属性声明的，所以我们需要将其修改为字符串资源中的一个引用，让其能够根据语言地区自动选择合适的文案：

```
<manifest ... >
    ...
    <!-- 设置应用名称 -->
	<application
        ...
	    android:label="@string/title"
        ...
    >
	</application>
</manifest>
```

然后，我们还需要在android/app/src/main/res文件夹中，为要支持的语言创建字符串strings.xml文件。这里由于默认文件是英文的，所以我们只需要为中文创建一个文件即可。字符串资源的文件目录结构，如下图所示：

![f2630d55027748a7b68919cdb545e83a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/f2630d55027748a7b68919cdb545e83a.jpg)

图9 strings.xml文件目录结构

values与values-zh文件夹下的strings.xml内容如下所示：

```
<!--英文(默认)字符串资源-->
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="title">Computer</string>
</resources>


<!--中文字符串资源-->
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="title">计数器</string>
</resources>
```

完成Android应用标题的工程配置后，我们回到Flutter工程，选择Android手机运行程序，可以看到，计数器的Android应用标题也可以正确地支持国际化了。

接下来，我们再看**iOS工程下如何实现应用名称的配置**。

与Android工程类似，iOS工程中的应用名称是在Info.list文件的Bundle name属性声明的，所以我们也需要将其修改为字符串资源中的一个引用，使其能够根据语言地区自动选择文案：

![da0db3fa9c334ef29c189b74e19fb4ac](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/da0db3fa9c334ef29c189b74e19fb4ac.jpg)

图10 iOS工程应用名称配置

由于应用名称默认是不可配置的，所以工程并没有提供英文或者中文的可配置项，这些都需要通过新建与字符串引用对应的资源文件去搞定的。

我们右键单击Runner文件夹，然后选择New File来添加名为InfoPlist.strings的字符串资源文件，并在工程面板的最右侧文件检查器中的Localization选项中，添加英文和中文两种语言。InfoPlist.strings的英文版和中文版内容如下所示：

```
//英文版
"CFBundleName" = "Computer";

//中文版
"CFBundleName" = "计数器";
```

至此，我们也完成了iOS应用标题的工程配置。我们回到Flutter工程，选择iOS手机运行程序，发现计数器的iOS应用标题也支持国际化了。

#### 总结

好了，今天的分享就到这里。我们来总结下核心知识点吧。

在今天的分享中，我与你介绍了Flutter应用国际化的解决方案，即在代码中实现一个LocalizationsDelegate，在这个类中将所有需要翻译的文案全部声明为它的属性，然后依次进行手动翻译适配，最后将这个代理类设置为应用程序的翻译回调。

而为了简化手动翻译到代码转换的过程，我们通常会使用多个arb文件存储文案在不同语言地区的映射关系，并使用Flutter i18n插件来实现代码的自动转换。

国际化的核心就是语言差异配置抽取。在原生Android和iOS系统中进行国际化适配，我们只需为需要国际化的资源（比如，字符串文本、图片、布局等）提供不同的文件夹目录，就可以在应用层代码访问国际化资源时，自动根据语言地区进行适配。

但，Flutter的国际化能力就相对原始很多，不同语言和地区的国际化资源既没有存放在单独的xml或者JSON上，也没有存放在不同的语言和地区文件夹中。幸好有Flutter i18n插件的帮助，否则为一个应用提供国际化的支持将会是件极其繁琐的事情。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/32_i18n_demo)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留下一道思考题吧。

在Flutter中，如何实现图片类资源的国际化呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何适配不同分辨率的手机屏幕？

你好，我是陈航。

在上一篇文章中，我与你分享了在Flutter中实现国际化的基本原理。与原生Android和iOS只需为国际化资源提供不同的目录，就可以在运行时自动根据语言和地区进行适配不同，Flutter的国际化是完全在代码中实现的。

即通过代码声明的方式，将应用中所有需要翻译的文案都声明为LocalizationsDelegate的属性，然后针对不同的语言和地区进行手动翻译适配，最后在初始化应用程序时，将这个代理设置为国际化的翻译回调。而为了简化这个过程，也为了将国际化资源与代码实现分离，我们通常会使用arb文件存储不同语言地区的映射关系，并通过Flutter i18n插件来实现代码的自动生成。

可以说，国际化为全世界的用户提供了统一而标准的体验。那么，为不同尺寸、不同旋转方向的手机提供统一而标准的体验，就是屏幕适配需要解决的问题了。

在移动应用的世界中，页面是由控件组成的。如果我们支持的设备只有普通手机，可以确保同一个页面、同一个控件，在不同的手机屏幕上的显示效果是基本一致的。但，随着平板电脑和类平板电脑等超大屏手机越来越普及，很多原本只在普通手机上运行的应用也逐渐跑在了平板上。

但，由于平板电脑的屏幕非常大，展示适配普通手机的界面和控件时，可能会出现UI异常的情况。比如，对于新闻类手机应用来说，通常会有新闻列表和新闻详情两个页面，如果我们把这两个页面原封不动地搬到平板电脑上，就会出现控件被拉伸、文字过小过密、图片清晰度不够、屏幕空间被浪费的异常体验。

而另一方面，即使对于同一台手机或平板电脑来说，屏幕的宽高配置也不是一成不变的。因为加速度传感器的存在，所以当我们旋转屏幕时，屏幕宽高配置会发生逆转，即垂直方向与水平方向的布局行为会互相交换，从而导致控件被拉伸等UI异常问题。

因此，为了让用户在不同的屏幕宽高配置下获得最佳的体验，我们不仅需要对平板进行屏幕适配，充分利用额外可用的屏幕空间，也需要在屏幕方向改变时重新排列控件。即，我们需要优化应用程序的界面布局，为用户提供新功能、展示新内容，以将拉伸变形的界面和控件替换为更自然的布局，将单一的视图合并为复合视图。

在原生Android或iOS中，这种在同一页面实现不同布局的行为，我们通常会准备多个布局文件，通过判断当前屏幕分辨率来决定应该使用哪套布局方式。在Flutter中，屏幕适配的原理也非常类似，只不过Flutter并没有布局文件的概念，我们需要准备多个布局来实现。

那么今天，我们就来分别来看一下如何通过多个布局，实现适配屏幕旋转与平板电脑。

#### 适配屏幕旋转

在屏幕方向改变时，屏幕宽高配置也会发生逆转：从竖屏模式变成横屏模式，原来的宽变成了高（垂直方向上的布局空间更短了），而高则变成了宽（水平方向上的布局空间更长了）。

通常情况下，由于ScrollView和ListView的存在，我们基本上不需要担心垂直方向上布局空间更短的问题，大不了一屏少显示几个控件元素，用户仍然可以使用与竖屏模式同样的交互滚动视图来查看其他控件元素；但水平方向上布局空间更长，界面和控件通常已被严重拉伸，原有的布局方式和交互方式都需要做较大调整。

从横屏模式切回竖屏模式，也是这个道理。

为了适配竖屏模式与横屏模式，我们需要准备两个布局方案，一个用于纵向，一个用于横向。当设备改变方向时，Flutter会通知我们重建布局：Flutter提供的OrientationBuilder控件，可以在设备改变方向时，通过builder函数回调告知其状态。这样，我们就可以根据回调函数提供的orientation参数，来识别当前设备究竟是处于横屏（landscape）还是竖屏（portrait）状态，从而刷新界面。

如下所示的代码演示了OrientationBuilder的具体用法。我们在其builder回调函数中，准确地识别出了设备方向，并对横屏和竖屏两种模型加载了不同的布局方式，而_buildVerticalLayout和_buildHorizontalLayout是用于创建相应布局的方法：

```
@override
Widget build(BuildContext context) {
  return Scaffold(
    //使用OrientationBuilder的builder模式感知屏幕旋转
    body: OrientationBuilder(
      builder: (context, orientation) {
        //根据屏幕旋转方向返回不同布局行为
        return orientation == Orientation.portrait
            ? _buildVerticalLayout()
            : _buildHorizontalLayout();
      },
    ),
  );
}
```

OrientationBuilder提供了orientation参数可以识别设备方向，而如果我们在OrientationBuilder之外，希望根据设备的旋转方向设置一些组件的初始化行为，也可以使用MediaQueryData提供的orientation方法：

```
if(MediaQuery.of(context).orientation == Orientation.portrait) {
  //dosth
}
```

需要注意的是，Flutter应用默认支持竖屏和横屏两种模式。如果我们的应用程序不需要提供横屏模式，也可以直接调用SystemChrome提供的setPreferredOrientations方法告诉Flutter，这样Flutter就可以固定视图的布局方向了：

```
SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
```

#### 适配平板电脑

当适配更大的屏幕尺寸时，我们希望App上的内容可以适应屏幕上额外的可用空间。如果我们在平板中使用与手机相同的布局，就会浪费大量的可视空间。与适配屏幕旋转类似，最直接的方法是为手机和平板电脑创建两种不同的布局。然而，考虑到平板电脑和手机为用户提供的功能并无差别，因此这种实现方式将会新增许多不必要的重复代码。

为解决这个问题，我们可以采用另外一种方法：**将屏幕空间划分为多个窗格，即采用与原生Android、iOS类似的Fragment、ChildViewController概念，来抽象独立区块的视觉功能。**

多窗格布局可以在平板电脑和横屏模式上，实现更好的视觉平衡效果，增强App的实用性和可读性。而，我们也可以通过独立的区块，在不同尺寸的手机屏幕上快速复用视觉功能。

如下图所示，分别展示了普通手机、横屏手机与平板电脑，如何使用多窗格布局来改造新闻列表和新闻详情交互：

![e9d0076a66694e57b01d3b0b4d9dbf54](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e9d0076a66694e57b01d3b0b4d9dbf54.jpg)

图1 多窗格布局示意图

首先，我们需要分别为新闻列表与新闻详情创建两个可重用的独立区块：

- 新闻列表，可以在元素被点击时通过回调函数告诉父Widget元素索引；
- 而新闻详情，则用于展示新闻列表中被点击的元素索引。

对于手机来说，由于空间小，所以新闻列表区块和新闻详情区块都是独立的页面，可以通过点击新闻元素进行新闻详情页面的切换；而对于平板电脑（和手机横屏布局）来说，由于空间足够大，所以我们把这两个区块放置在同一个页面，可以通过点击新闻元素去刷新同一页面的新闻详情。

页面的实现和区块的实现是互相独立的，通过区块复用就可以减少编写两个独立布局的工作：

```
//列表Widget
class ListWidget extends StatefulWidget {
  final ItemSelectedCallback onItemSelected;
  ListWidget(
    this.onItemSelected,//列表被点击的回调函数
  );
  @override
  _ListWidgetState createState() => _ListWidgetState();
}

class _ListWidgetState extends State<ListWidget> {
  @override
  Widget build(BuildContext context) {
    //创建一个20项元素的列表
    return ListView.builder(
      itemCount: 20,
      itemBuilder: (context, position) {
        return ListTile(
            title: Text(position.toString()),//标题为index
            onTap:()=>widget.onItemSelected(position),//点击后回调函数
        );
      },
    );
  }
}

//详情Widget
class DetailWidget extends StatefulWidget {
  final int data; //新闻列表被点击元素索引
  DetailWidget(this.data);
  @override
  _DetailWidgetState createState() => _DetailWidgetState();
}

class _DetailWidgetState extends State<DetailWidget> {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.red,//容器背景色
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(widget.data.toString()),//居中展示列表被点击元素索引
          ],
        ),
      ),
    );
  }
}
```

然后，我们只需要检查设备屏幕是否有足够的宽度来同时展示列表与详情部分。为了获取屏幕宽度，我们可以使用MediaQueryData提供的size方法。

在这里，我们将平板电脑的判断条件设置为宽度大于480。这样，屏幕中就有足够的空间可以切换到多窗格的复合布局了：

```
if(MediaQuery.of(context).size.width > 480) {
  //tablet
} else {
  //phone
}
```

最后，如果宽度够大，我们就会使用Row控件将列表与详情包装在同一个页面中，用户可以点击左侧的列表刷新右侧的详情；如果宽度比较小，那我们就只展示列表，用户可以点击列表，导航到新的页面展示详情：

```
class _MasterDetailPageState extends State<MasterDetailPage> {
  var selectedValue = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: OrientationBuilder(builder: (context, orientation) {
        //平板或横屏手机，页面内嵌列表ListWidget与详情DetailWidget
        if (MediaQuery.of(context).size.width > 480) {
          return Row(children: <Widget>[
            Expanded(
              child: ListWidget((value) {//在列表点击回调方法中刷新右侧详情页
                setState(() {selectedValue = value;});
              }),
            ),
            Expanded(child: DetailWidget(selectedValue)),
          ]);

        } else {//普通手机，页面内嵌列表ListWidget
          return ListWidget((value) {//在列表点击回调方法中打开详情页DetailWidget
            Navigator.push(context, MaterialPageRoute(
              builder: (context) {
                return Scaffold(
                  body: DetailWidget(value),
                );
              },
            ));

          });
        }
      }),
    );
  }
}
```

运行一下代码，可以看到，我们的应用已经完全适配不同尺寸、不同方向的设备屏幕了。

![318779bd51a744b59c5702c7086b0fee](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/318779bd51a744b59c5702c7086b0fee.jpg)

图2 竖屏手机版列表详情

![debff681cad4457db664e5f284470d89](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/debff681cad4457db664e5f284470d89.jpg)

图3 横屏手机版列表详情

![b5027327bf274c33ace28efd718680a8](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/b5027327bf274c33ace28efd718680a8.jpg)

图4 竖屏平板列表详情

![a404bde59c7d4d068622fd107d2bcf91](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a404bde59c7d4d068622fd107d2bcf91.jpg)

图5 横屏平板列表详情

#### 总结

好了，今天的分享就到这里。我们总结一下今天的核心知识点吧。

在Flutter中，为了适配不同设备屏幕，我们需要提供不同的布局方式。而将独立的视觉区块进行封装，通过OrientationBuilder提供的orientation回调参数，以及MediaQueryData提供的屏幕尺寸，以多窗格布局的方式为它们提供不同的页面呈现形态，能够大大降低编写独立布局所带来的重复工作。如果你的应用不需要支持设备方向，也可以通过SystemChrome提供的setPreferredOrientations方法，强制竖屏。

做好应用开发，我们除了要保证产品功能正常，还需要兼容碎片化（包括设备碎片化、品牌碎片化、系统碎片化、屏幕碎片化等方面）可能带来的潜在问题，以确保良好的用户体验。

与其他维度碎片化可能带来功能缺失甚至Crash不同，屏幕碎片化不至于导致功能完全不可用，但控件显示尺寸却很容易在没有做好适配的情况下产生变形，让用户看到异形甚至不全的UI信息，影响产品形象，因此也需要重点关注。

在应用开发中，我们可以分别在不同屏幕尺寸的主流机型和模拟器上运行我们的程序，来观察UI样式和功能是否异常，从而写出更加健壮的布局代码。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/33_multi_screen_demo)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留下一道思考题吧

setPreferredOrientations方法是全局生效的，如果你的应用程序中有两个相邻的页面，页面A仅支持竖屏，页面B同时支持竖屏和横屏，你会如何实现呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

## 构建、调试、测试与发布

### 如何理解Flutter的编译模式？

你好，我是陈航。今天，我们来聊聊Flutter的编译模式吧。

在开发移动应用程序时，一个App的完整生命周期包括开发、测试和上线3个阶段。在每个阶段，开发者的关注点都不一样。

比如，在开发阶段，我们希望调试尽可能方便、快速，尽可能多地提供错误上下文信息；在测试阶段，我们希望覆盖范围尽可能全面，能够具备不同配置切换能力，可以测试和验证还没有对外发布的新功能；而在发布阶段，我们则希望能够去除一切测试代码，精简调试信息，使运行速度尽可能快，代码足够安全。

这就要求开发者在构建移动应用时，不仅要在工程内提前准备多份配置环境，还要利用编译器提供的编译选项，打包出符合不同阶段优化需求的App。

对于Flutter来说，它既支持常见的Debug、Release等工程物理层面的编译模式，也支持在工程内提供多种配置环境入口。今天，我们就来学习一下Flutter提供的编译模式，以及如何在App中引用开发环境和生产环境，使得我们在不破坏任何生产环境代码的情况下，能够测试处于开发期的新功能。

#### Flutter的编译模式

Flutter支持3种运行模式，包括Debug、Release和Profile。在编译时，这三种模式是完全独立的。首先，我们先来看看这3种模式的具体含义吧。

- Debug模式对应Dart的JIT模式，可以在真机和模拟器上同时运行。该模式会打开所有的断言（assert），以及所有的调试信息、服务扩展和调试辅助（比如Observatory）。此外，该模式为快速开发和运行做了优化，支持亚秒级有状态的Hot reload（热重载），但并没有优化代码执行速度、二进制包大小和部署。flutter run –debug命令，就是以这种模式运行的。
- Release模式对应Dart的AOT模式，只能在真机上运行，不能在模拟器上运行，其编译目标为最终的线上发布，给最终的用户使用。该模式会关闭所有的断言，以及尽可能多的调试信息、服务扩展和调试辅助。此外，该模式优化了应用快速启动、代码快速执行，以及二级制包大小，因此编译时间较长。flutter run –release命令，就是以这种模式运行的。
- Profile模式，基本与Release模式一致，只是多了对Profile模式的服务扩展的支持，包括支持跟踪，以及一些为了最低限度支持所需要的依赖（比如，可以连接Observatory到进程）。该模式用于分析真实设备实际运行性能。flutter run –profile命令，就是以这种模式运行的。

由于Profile与Release在编译过程上几乎无差异，因此我们今天只讨论Debug和Release模式。

在开发应用时，为了便于快速发现问题，我们通常会在运行时识别当前的编译模式，去改变代码的部分执行行为：在Debug模式下，我们会打印详细的日志，调用开发环境接口；而在Release模式下，我们会只记录极少的日志，调用生产环境接口。

在运行时识别应用的编译模式，有两种解决办法：

- 通过断言识别；
- 通过Dart VM所提供的编译常数识别。

我们先来看看**如何通过断言识别应用的编译模式**。

通过Debug与Release模式的介绍，我们可以得出，Release与Debug模式的一个重要区别就是，Release模式关闭了所有的断言。因此，我们可以借助于断言，写出只在Debug模式下生效的代码。

如下所示，我们在断言里传入了一个始终返回true的匿名函数执行结果，这个匿名函数的函数体只会在Debug模式下生效：

```
assert(() {
  //Do sth for debug
  return true;
}());
```

需要注意的是，匿名函数声明调用结束时追加了小括号（）。 这是因为断言只能检查布尔值，所以我们必须使用括号强制执行这个始终返回true的匿名函数，以确保匿名函数体的代码可以执行。

接下来，我们再看看**如何通过编译常数识别应用的编译模式**。

如果说通过断言只能写出在Debug模式下运行的代码，而通过Dart提供的编译常数，我们还可以写出只在Release模式下生效的代码。Dart提供了一个布尔型的常量kReleaseMode，用于反向指示当前App的编译模式。

如下所示，我们通过判断这个常量，可以准确地识别出当前的编译模式：

```
if(kReleaseMode){
  //Do sth for release
} else {
  //Do sth for debug
}
```

#### 分离配置环境

通过断言和kReleaseMode常量，我们能够识别出当前App的编译环境，从而可以在运行时对某个代码功能进行局部微调。而如果我们想在整个应用层面，为不同的运行环境提供更为统一的配置（比如，对于同一个接口调用行为，开发环境会使用dev.example.com域名，而生产环境会使用api.example.com域名），则需要在应用启动入口提供可配置的初始化方式，根据特定需求为应用注入配置环境。

在Flutter构建App时，为应用程序提供不同的配置环境，总体可以分为抽象配置、配置多入口、读配置和编译打包4个步骤：

1. 抽象出应用程序的可配置部分，并使用InheritedWidget对其进行封装；
2. 将不同的配置环境拆解为多个应用程序入口（比如，开发环境为main-dev.dart、生产环境为main.dart），把应用程序的可配置部分固化在各个入口处；
3. 在运行期，通过InheritedWidget提供的数据共享机制，将配置部分应用到其子Widget对应的功能中；
4. 使用Flutter提供的编译打包选项，构建出不同配置环境的安装包。

**接下来，我将依次为你介绍具体的实现步骤。**

在下面的示例中，我会把应用程序调用的接口和标题进行区分实现，即开发环境使用dev.example.com域名，应用主页标题为dev；而生产环境使用api.example.com域名，主页标题为example。

首先是**配置抽象**。根据需求可以看出，应用程序中有两个需要配置的部分，即接口apiBaseUrl和标题appName，因此我定义了一个继承自InheritedWidget的类AppConfig，对这两个配置进行封装：

```
class AppConfig extends InheritedWidget {
  AppConfig({
    @required this.appName,
    @required this.apiBaseUrl,
    @required Widget child,
  }) : super(child: child);

  final String appName;//主页标题
  final String apiBaseUrl;//接口域名

  //方便其子Widget在Widget树中找到它
  static AppConfig of(BuildContext context) {
    return context.inheritFromWidgetOfExactType(AppConfig);
  }

  //判断是否需要子Widget更新。由于是应用入口，无需更新
  @override
  bool updateShouldNotify(InheritedWidget oldWidget) => false;
}
```

接下来，我们需要**为不同的环境创建不同的应用入口**。

在这个例子中，由于只有两个环境，即开发环境与生产环境，因此我们将文件分别命名为main_dev.dart和main.dart。在这两个文件中，我们会使用不同的配置数据来对AppConfig进行初始化，同时把应用程序实例MyApp作为其子Widget，这样整个应用内都可以获取到配置数据：

```
//main_dev.dart
void main() {
  var configuredApp = AppConfig(
    appName: 'dev',//主页标题
    apiBaseUrl: 'http://dev.example.com/',//接口域名
    child: MyApp(),
  );
  runApp(configuredApp);//启动应用入口
}

//main.dart
void main() {
  var configuredApp = AppConfig(
    appName: 'example',//主页标题
    apiBaseUrl: 'http://api.example.com/',//接口域名
    child: MyApp(),
  );
  runApp(configuredApp);//启动应用入口
}
```

完成配置环境的注入之后，接下来就可以**在应用内获取配置数据**，来实现定制化的功能了。由于AppConfig是整个应用程序的根节点，因此我可以通过调用AppConfig.of方法，来获取到相关的数据配置。

在下面的代码中，我分别获取到了应用主页的标题，以及接口域名，并显示了出来：

```
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var config = AppConfig.of(context);//获取应用配置
    return MaterialApp(
      title: config.appName,//应用主页标题
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var config = AppConfig.of(context);//获取应用配置
    return Scaffold(
      appBar: AppBar(
        title: Text(config.appName),//应用主页标题
      ),
      body:  Center(
        child: Text('API host: ${config.apiBaseUrl}'),//接口域名
      ),
    );
  }
}
```

现在，我们已经完成了分离配置环境的代码部分。最后，我们可以使用Flutter提供的编译选项，来**构建出不同配置的安装包**了。

如果想要在模拟器或真机上运行这段代码，我们可以在flutter run命令后面，追加–target或-t参数，来指定应用程序初始化入口：

```
//运行开发环境应用程序
flutter run -t lib/main_dev.dart

//运行生产环境应用程序
flutter run -t lib/main.dart
```

如果我们想在Android Studio上为应用程序创建不同的启动配置，则可以**通过Flutter插件为main_dev.dart增加启动入口**。

首先，点击工具栏上的Config Selector，选择Edit Configurations进入编辑应用程序启动选项：

![bd4e38bfba0740e3baa1ca34f9c1f836](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/bd4e38bfba0740e3baa1ca34f9c1f836.jpg)

图1 Config Selector新增入口

然后，点击位于工具栏面板左侧顶部的“+”按钮，在弹出的菜单中选择Flutter选项，为应用程序新增一项启动入口：

![ad0beae98d1344c5a408a2e65818eaad](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ad0beae98d1344c5a408a2e65818eaad.jpg)

图2 选择新增类型

最后，在入口的编辑面板中，为main_dev选择程序的Dart入口，点击OK后，就完成了入口的新增工作：

![bc04cd184f7b4743873c3d3860fe8867](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/bc04cd184f7b4743873c3d3860fe8867.jpg)

图3 编辑启动入口

接下来，我们就可以**在Config Selector中切换不同的启动入口，从而直接在Android Studio中注入不同的配置环境了**：

![4ca3893ac8f64ebe94b20b813b4c641c](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4ca3893ac8f64ebe94b20b813b4c641c.jpg)

图4 Config Selector切换启动入口

我们试着在不同的入口中进行切换和运行，可以看到，App已经可以识别出不同的配置环境了：

![c0f1a31040754533a5abe82c8d5c67d0](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/c0f1a31040754533a5abe82c8d5c67d0.jpg)

图5 开发环境运行示例

![e3eaf9e7e29447dbbf864dc21718295f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e3eaf9e7e29447dbbf864dc21718295f.jpg)

图6 生产环境运行示例

而如果我们想要打包构建出适用于Android的APK，或是iOS的IPA安装包，则可以在flutter build 命令后面，同样追加–target或-t参数，指定应用程序初始化入口：

```
//打包开发环境应用程序
flutter build apk -t lib/main_dev.dart
flutter build ios -t lib/main_dev.dart

//打包生产环境应用程序
flutter build apk -t lib/main.dart
flutter build ios -t lib/main.dart
```

#### 总结

好了，今天的分享就到这里。我们来总结一下今天的主要内容吧。

Flutter支持Debug与Release的编译模式，并且这两种模式在构建时是完全独立的。Debug模式下会打开所有的断言和调试信息，而Release模式下则会关闭这些信息，因此我们可以通过断言，写出只在Debug模式下生效的代码。而如果我们想更精准地识别出当前的编译模式，则可以利用Dart所提供的编译常数kReleaseMode，写出只在Release模式下生效的代码。

除此之外，Flutter对于常见的分环境配置能力也提供了支持，我们可以使用InheritedWidget为应用中可配置部分进行封装抽象，通过配置多入口的方式为应用的启动注入配置环境。

需要注意的是，虽然断言和kReleaseMode都能够识别出Debug编译模式，但它们对二进制包的打包构建影响是不同的。

采用断言的方式，其相关代码会在Release构建中被完全剔除；而如果使用kReleaseMode常量来识别Debug环境，虽然这段代码永远不会在Release环境中执行，但却会被打入到二进制包中，增大包体积。因此，如果没有特殊需求的话，一定要使用断言来实现Debug特有的逻辑，或是在发布期前将使用kReleaseMode判断的Debug逻辑完全删除。

我把今天分享所涉及到的知识点打包到了[GitHub](https://github.com/cyndibaby905/34_multi_env)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留一道思考题吧。

在保持生产环境代码不变的情况下，如果想在开发环境中支持不同配置的切换，我们应该如何实现？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### Hot Reload是怎么做到的？

你好，我是陈航。

在上一篇文章中，我与你分享了Flutter的Debug与Release编译模式，以及如何通过断言与编译常数来精准识别当前代码所运行的编译模式，从而写出只在Debug或Release模式下生效的代码。

另外，对于在开发期与发布期分别使用不同的配置环境，Flutter也提供了支持。我们可以将应用中可配置的部分进行封装抽象，使用配置多入口的方式，通过InheritedWidget来为应用的启动注入环境配置。

如果你有过原生应用的开发经历，那你一定知道在原生应用开发时，如果我们想要在硬件设备上看到调整后的运行效果，在完成了代码修改后，必须要经过漫长的重新编译，才能同步到设备上。

而Flutter则不然，由于Debug模式支持JIT，并且为开发期的运行和调试提供了大量优化，因此代码修改后，我们可以通过亚秒级的热重载（Hot Reload）进行增量代码的快速刷新，而无需经过全量的代码编译，从而大大缩短了从代码修改到看到修改产生的变化之间所需要的时间。

比如，在开发页面的过程中，当我们点击按钮出现一个弹窗的时候，发现弹窗标题没有对齐，这时候只要修改标题的对齐样式，然后保存，在代码并没有重新编译的情况下，标题样式就发生了改变，感觉就像是在UI编辑面板中直接修改元素样式一样，非常方便。

那么，Flutter的热重载到底是如何实现的呢？

#### 热重载

热重载是指，在不中断App正常运行的情况下，动态注入修改后的代码片段。而这一切的背后，离不开Flutter所提供的运行时编译能力。为了更好地理解Flutter的热重载实现原理，我们先简单回顾一下Flutter编译模式背后的技术吧。

- JIT（Just In Time），指的是即时编译或运行时编译，在Debug模式中使用，可以动态下发和执行代码，启动速度快，但执行性能受运行时编译影响；

![1e61446b08884b9195b5409458620e63](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/1e61446b08884b9195b5409458620e63.jpg)

图1 JIT编译模式示意图

- AOT（Ahead Of Time），指的是提前编译或运行前编译，在Release模式中使用，可以为特定的平台生成稳定的二进制代码，执行性能好、运行速度快，但每次执行均需提前编译，开发调试效率低。

![1ecb4333501a4f56ada17807bcbd14b6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/1ecb4333501a4f56ada17807bcbd14b6.jpg)

图2 AOT编译模式示意图

可以看到，Flutter提供的两种编译模式中，AOT是静态编译，即编译成设备可直接执行的二进制码；而JIT则是动态编译，即将Dart代码编译成中间代码（Script Snapshot），在运行时设备需要Dart VM解释执行。

而热重载之所以只能在Debug模式下使用，是因为Debug模式下，Flutter采用的是JIT动态编译（而Release模式下采用的是AOT静态编译）。JIT编译器将Dart代码编译成可以运行在Dart VM上的Dart Kernel，而Dart Kernel是可以动态更新的，这就实现了代码的实时更新功能。

![e0fc7e5da8004eda9e14854511d64538](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e0fc7e5da8004eda9e14854511d64538.jpg)

图3 热重载流程

总体来说，**热重载的流程可以分为扫描工程改动、增量编译、推送更新、代码合并、Widget重建5个步骤：**

1. 工程改动。热重载模块会逐一扫描工程中的文件，检查是否有新增、删除或者改动，直到找到在上次编译之后，发生变化的Dart代码。
2. 增量编译。热重载模块会将发生变化的Dart代码，通过编译转化为增量的Dart Kernel文件。
3. 推送更新。热重载模块将增量的Dart Kernel文件通过HTTP端口，发送给正在移动设备上运行的Dart VM。
4. 代码合并。Dart VM会将收到的增量Dart Kernel文件，与原有的Dart Kernel文件进行合并，然后重新加载新的Dart Kernel文件。
5. Widget重建。在确认Dart VM资源加载成功后，Flutter会将其UI线程重置，通知Flutter Framework重建Widget。

可以看到，Flutter提供的热重载在收到代码变更后，并不会让App重新启动执行，而只会触发Widget树的重新绘制，因此可以保持改动前的状态，这就大大节省了调试复杂交互界面的时间。

比如，我们需要为一个视图栈很深的页面调整UI样式，若采用重新编译的方式，不仅需要漫长的全量编译时间，而为了恢复视图栈，也需要重复之前的多次点击交互，才能重新进入到这个页面查看改动效果。但如果是采用热重载的方式，不仅没有编译时间，而且页面的视图栈状态也得以保留，完成热重载之后马上就可以预览UI效果了，相当于局部界面刷新。

#### 不支持热重载的场景

Flutter提供的亚秒级热重载一直是开发者的调试利器。通过热重载，我们可以快速修改UI、修复Bug，无需重启应用即可看到改动效果，从而大大提升了UI调试效率。

不过，Flutter的热重载也有一定的局限性。因为涉及到状态保存与恢复，所以并不是所有的代码改动都可以通过热重载来更新。

接下来，我就与你介绍几个不支持热重载的典型场景：

- 代码出现编译错误；
- Widget状态无法兼容；
- 全局变量和静态属性的更改；
- main方法里的更改；
- initState方法里的更改；
- 枚举和泛类型更改。

现在，我们就具体看看这几种场景的问题，应该如何解决吧。

#### 代码出现编译错误

当代码更改导致编译错误时，热重载会提示编译错误信息。比如下面的例子中，代码中漏写了一个反括号，在使用热重载时，编译器直接报错：

```
Initializing hot reload...
Syncing files to device iPhone X...

Compiler message:
lib/main.dart:84:23: Error: Can't find ')' to match '('.
    return MaterialApp(
                      ^
Reloaded 1 of 462 libraries in 301ms.
```

在这种情况下，只需更正上述代码中的错误，就可以继续使用热重载。

#### Widget状态无法兼容

当代码更改会影响Widget的状态时，会使得热重载前后Widget所使用的数据不一致，即应用程序保留的状态与新的更改不兼容。这时，热重载也是无法使用的。

比如下面的代码中，我们将某个类的定义从 StatelessWidget改为StatefulWidget时，热重载就会直接报错：

```
//改动前
class MyWidget extends StatelessWidget {
  Widget build(BuildContext context) {
    return GestureDetector(onTap: () => print('T'));
  }
}

//改动后
class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => MyWidgetState();
}
class MyWidgetState extends State<MyWidget> { /*...*/ }
```

当遇到这种情况时，我们需要重启应用，才能看到更新后的程序。

#### 全局变量和静态属性的更改

在Flutter中，全局变量和静态属性都被视为状态，在第一次运行应用程序时，会将它们的值设为初始化语句的执行结果，因此在热重载期间不会重新初始化。

比如下面的代码中，我们修改了一个静态Text数组的初始化元素。虽然热重载并不会报错，但由于静态变量并不会在热重载之后初始化，因此这个改变并不会产生效果：

```
//改动前
final sampleText = [
  Text("T1"),
  Text("T2"),
  Text("T3"),
  Text("T4"),
];

//改动后
final sampleText = [
  Text("T1"),
  Text("T2"),
  Text("T3"),
  Text("T10"),    //改动点
];
```

如果我们需要更改全局变量和静态属性的初始化语句，重启应用才能查看更改效果。

#### main方法里的更改

在Flutter中，由于热重载之后只会根据原来的根节点重新创建控件树，因此main函数的任何改动并不会在热重载后重新执行。所以，如果我们改动了main函数体内的代码，是无法通过热重载看到更新效果的。

在第1篇文章“[预习篇 · 从零开始搭建Flutter开发环境](https://time.geekbang.org/column/article/104051)”中，我与你介绍了这种情况。在更新前，我们通过MyApp封装了一个展示“Hello World”的文本，在更新后，直接在main函数封装了一个展示“Hello 2019”的文本：

```
//更新前
class MyAPP extends StatelessWidget {
@override
  Widget build(BuildContext context) {
    return const Center(child: Text('Hello World', textDirection: TextDirection.ltr));
  }
}

void main() => runApp(new MyAPP());

//更新后
void main() => runApp(const Center(child: Text('Hello, 2019', textDirection: TextDirection.ltr)));
```

由于main函数并不会在热重载后重新执行，因此以上改动是无法通过热重载查看更新的。

#### initState方法里的更改

在热重载时，Flutter会保存Widget的状态，然后重建Widget。而initState方法是Widget状态的初始化方法，这个方法里的更改会与状态保存发生冲突，因此热重载后不会产生效果。

在下面的例子中，我们将计数器的初始值由10改为100：

```
//更改前
class _MyHomePageState extends State<MyHomePage> {
  int _counter;
  @override
  void initState() {
    _counter = 10;
    super.initState();
  }
  ...
}

//更改后
class _MyHomePageState extends State<MyHomePage> {
  int _counter;
  @override
  void initState() {
    _counter = 100;
    super.initState();
  }
  ...
}
```

由于这样的改动发生在initState方法中，因此无法通过热重载查看更新，我们需要重启应用，才能看到更改效果。

#### 枚举和泛型类型更改

在Flutter中，枚举和泛型也被视为状态，因此对它们的修改也不支持热重载。比如在下面的代码中，我们将一个枚举类型改为普通类，并为其增加了一个泛型参数：

```
//更改前
enum Color {
  red,
  green,
  blue
}

class C<U> {
  U u;
}

//更改后
class Color {
  Color(this.r, this.g, this.b);
  final int r;
  final int g;
  final int b;
}

class C<U, V> {
  U u;
  V v;
}
```

这两类更改都会导致热重载失败，并生成对应的提示消息。同样的，我们需要重启应用，才能查看到更改效果。

#### 总结

好了，今天的分享就到这里，我们总结一下今天的主要内容吧。

Flutter的热重载是基于JIT编译模式的代码增量同步。由于JIT属于动态编译，能够将Dart代码编译成生成中间代码，让Dart VM在运行时解释执行，因此可以通过动态更新中间代码实现增量同步。

热重载的流程可以分为5步，包括：扫描工程改动、增量编译、推送更新、代码合并、Widget重建。Flutter在接收到代码变更后，并不会让App重新启动执行，而只会触发Widget树的重新绘制，因此可以保持改动前的状态，大大缩短了从代码修改到看到修改产生的变化之间所需要的时间。

而另一方面，由于涉及到状态保存与恢复，因此涉及状态兼容与状态初始化的场景，热重载是无法支持的，比如改动前后Widget状态无法兼容、全局变量与静态属性的更改、main方法里的更改、initState方法里的更改、枚举和泛型的更改等。

可以发现，热重载提高了调试UI的效率，非常适合写界面样式这样需要反复查看修改效果的场景。但由于其状态保存的机制所限，热重载本身也有一些无法支持的边界。

如果你在写业务逻辑的时候，不小心碰到了热重载无法支持的场景，也不需要进行漫长的重新编译加载等待，只要点击位于工程面板左下角的热重启（Hot Restart）按钮，就可以以秒级的速度进行代码重新编译以及程序重启了，同样也很快。

#### 思考题

最后，我给你留下一道思考题吧。

你是否了解其他框架（比如React Native、Webpack）的热重载机制？它们的热重载机制与Flutter有何区别？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何通过工具链优化开发调试效率？

你好，我是陈航。今天我们来聊聊如何调试Flutter App。

软件开发通常是一个不断迭代、螺旋式上升的过程。在迭代的过程中，我们不可避免地会经常与Bug打交道，特别是在多人协作的项目中，我们不仅要修复自己的Bug，有时还需要帮别人解决Bug。

而修复Bug的过程，不仅能帮我们排除代码中的隐患，也能帮助我们更快地上手项目。因此，掌握好调试这门技能，就显得尤为重要了。

在Flutter中，调试代码主要分为输出日志、断点调试和布局调试3类。所以，在今天这篇文章中，我将会围绕这3个主题为你详细介绍Flutter应用的代码调试。

我们先来看看，如何通过输出日志调试应用代码吧。

#### 输出日志

为了便于跟踪和记录应用的运行情况，我们在开发时通常会在一些关键步骤输出日志（Log），即使用print函数在控制台打印出相关的上下文信息。通过这些信息，我们可以定位代码中可能出现的问题。

在前面的很多篇文章里，我们都大量使用了print函数来输出应用执行过程中的信息。不过，由于涉及I/O操作，使用print来打印信息会消耗较多的系统资源。同时，这些输出数据很可能会暴露App的执行细节，所以我们需要在发布正式版时屏蔽掉这些输出。

说到操作方法，你想到的可能是在发布版本前先注释掉所有的print语句，等以后需要调试时，再取消这些注释。但，这种方法无疑是非常无聊且耗时的。那么，Flutter给我们提供了什么更好的方式吗？

为了根据不同的运行环境来开启日志调试功能，我们可以使用Flutter提供的debugPrint来代替print。**debugPrint函数同样会将消息打印至控制台，但与print不同的是，它提供了定制打印的能力。**也就是说，我们可以向debugPrint函数，赋值一个函数声明来自定义打印行为。

比如在下面的代码中，我们将debugPrint函数定义为一个空函数体，这样就可以实现一键取消打印的功能了：

```
debugPrint = (String message, {int wrapWidth}) {};//空实现
```

在Flutter 中，我们可以使用不同的main文件来表示不同环境下的入口。比如，在第34篇文章“[如何理解Flutter的编译模式？](https://time.geekbang.org/column/article/135865)”中，我们就分别用main.dart与main-dev.dart实现了生产环境与开发环境的分离。同样，我们可以通过main.dart与main-dev.dart，去分别定义生产环境与开发环境不同的打印日志行为。

在下面的例子中，我们将生产环境的debugPrint定义为空实现，将开发环境的debugPrint定义为同步打印数据：

```
//main.dart
void main() {
  // 将debugPrint指定为空的执行体, 所以它什么也不做
  debugPrint = (String message, {int wrapWidth}) {};
  runApp(MyApp());
}

//main-dev.dart
void main() async {
  // 将debugPrint指定为同步打印数据
  debugPrint = (String message, {int wrapWidth}) => debugPrintSynchronously(message, wrapWidth: wrapWidth);
  runApp(MyApp());
}
```

可以看到，在代码实现上，我们只要将应用内所有的print都替换成debugPrint，就可以满足开发环境下打日志的需求，也可以保证生产环境下应用的执行信息不会被意外打印。

#### 断点调试

输出日志固然方便，但如果要想获取更为详细，或是粒度更细的上下文信息，静态调试的方式非常不方便。这时，我们需要更为灵活的动态调试方法，即断点调试。断点调试可以让代码在目标语句上暂停，让程序逐条执行后续的代码语句，来帮助我们实时关注代码执行上下文中所有变量值的详细变化过程。

Android Studio提供了断点调试的功能，调试Flutter应用与调试原生Android代码的方法完全一样，具体可以分为三步，即**标记断点、调试应用、查看信息**。

接下来，我们以Flutter默认的计数器应用模板为例，观察代码中_counter值的变化，体会断点调试的全过程。

**首先是标记断点。**既然我们要观察_counter值的变化，因此在界面上展示最新的_counter值时添加断点，去观察其数值变化是最理想的。因此，我们在行号右侧点击鼠标，可以把断点加载到初始化Text控件所示的位置。

在下图的例子中，我们为了观察_counter在等于20的时候是否正常，还特意设置了一个条件断点_counter==20，这样调试器就只会在第20次点击计数器按钮时暂停下来：

![14662196ab0d442882556e05a109ee7a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/14662196ab0d442882556e05a109ee7a.jpg)

图1 标记断点

添加断点后，对应的行号将会出现圆形的断点标记，并高亮显示整行代码。到此，断点就添加好了。当然，我们还可以同时添加多个断点，以便更好地观察代码的执行过程。

**接下来则是调试应用了。**和之前通过点击run按钮的运行方式不同，这一次我们需要点击工具栏上的虫子图标，以调试模式启动App，如下图所示：

![8aa157c472ce4760a2046d6e3b461571](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/8aa157c472ce4760a2046d6e3b461571.jpg)

图2 调试App

等调试器初始化好后，我们的程序就启动了。由于我们的断点设置在了_counter为20时，因此在第20次点击了“+”按钮后，代码运行到了断点位置，自动进入了Debug视图模式。

![fb4a0879ef2346539d49837005aa0292](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/fb4a0879ef2346539d49837005aa0292.jpg)

图3 Debug视图模式

如图所示，我把Debug视图模式划分为4个区域，即A区控制调试工具、B区步进调试工具、C区帧调试窗口、D区变量查看窗口。

**A区的按钮**，主要用来控制调试的执行情况：

![992b60cbf0bd48bebc79e529a21dc214](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/992b60cbf0bd48bebc79e529a21dc214.jpg)

图4 A区按钮

- 比如，我们可以点击继续执行按钮来让程序继续运行、点击终止执行按钮来让程序终止运行、点击重新执行按钮来让程序重新启动，或是在程序正常执行时，点击暂停执行按钮按钮来让程序暂停运行。
- 又比如，我们可以点击编辑断点按钮来编辑断点信息，或是点击禁用断点按钮来取消断点。

**B区的按钮**，主要用来控制断点的步进情况：

![8a7c34bf81cb41d3b3885d2aee49552a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/8a7c34bf81cb41d3b3885d2aee49552a.jpg)

图5 B区按钮

- 比如，我们可以点击单步跳过按钮来让程序单步执行（但不会进入方法体内部）、点击单步进入或强制单步进入按钮让程序逐条语句执行，甚至还可以点击运行到光标处按钮让程序执行到在光标处（相当于新建临时断点）。
- 比如，当我们认为断点所在的方法体已经无需执行时，则可以点击单步跳出按钮让程序立刻执行完当前进入的方法，从而返回方法调用处的下一行。
- 又比如，我们可以点击表达式计算按钮来通过赋值或表达式方式修改任意变量的值。如下图所示，我们通过输入表达式_counter+=100，将计数器更新为120：

![2d718831c99f4d8cba762a626ebff891](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/2d718831c99f4d8cba762a626ebff891.jpg)

图6 Evaluate计算表达式

**C区**用来指示当前断点所包含的函数执行堆栈，**D区**则是其堆栈中的函数帧所对应的变量。

在这个例子中，我们的断点是在_MyHomePageState类中的build方法设置的，因此D区显示的也是build方法上下文所包含的变量信息（比如_counter、_widget、this、_element等）。如果我们想切换到_MyHomePageState的build方法执行堆栈中的其他函数（比如StatefulElement.build），查看相关上下文的变量信息时，只需要在C区中点击对应的方法名即可。

![0cc2f92929e44bbf9bce72d0dcb97205](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0cc2f92929e44bbf9bce72d0dcb97205.jpg)

图7 切换函数执行堆栈

可以看到，Android Studio提供的Flutter调试能力很丰富，我们可以通过这些基本步骤的组合，更为灵活地调整追踪步长，观察程序的执行情况，揪出代码中的Bug。

#### 布局调试

通过断点调试，我们在Android Studio的调试面板中，可以随时查看执行上下文有关的变量的值，根据逻辑来做进一步的判断，确定跟踪执行的步骤。不过在更多时候，我们使用Flutter的目的是实现视觉功能，而视觉功能的调试是无法简单地通过Debug视图模式面板来搞定的。

在上一篇文章中，我们通过Flutter提供的热重载机制，已经极大地缩短了从代码编写到界面运行所耗费的时间，可以更快地发现代码与目标界面的明显问题，但**如果想要更快地发现界面中更为细小的问题，比如对齐、边距等，则需要使用Debug Painting这个界面调试工具**。

Debug Painting能够以辅助线的方式，清晰展示每个控件元素的布局边界，因此我们可以根据辅助线快速找出布局出问题的地方。而Debug Painting的开启也比较简单，只需要将debugPaintSizeEnabled变量置为true即可。如下所示，我们在main函数中，开启了Debug Painting调试开关：

```
import 'package:flutter/rendering.dart';

void main() {
  debugPaintSizeEnabled = true;      //打开Debug Painting调试开关
  runApp(new MyApp());
}
```

运行代码后，App在iPhone X中的执行效果如下：

![634a0640dde94b69b2cdd12e7db5116d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/634a0640dde94b69b2cdd12e7db5116d.jpg)

图8 Debug Painting运行效果

可以看到，计数器示例中的每个控件元素都已经被标尺辅助线包围了。

辅助线提供了基本的Widget可视化能力。通过辅助线，我们能够感知界面中是否存在对齐或边距的问题，但却没有办法获取到布局信息，比如Widget距离父视图的边距信息、Widget宽高尺寸信息等。

**如果我们想要获取到Widget的可视化信息（比如布局信息、渲染信息等）去解决渲染问题，就需要使用更强大的Flutter Inspector了。**Flutter Inspector对控件布局详细数据提供了一种强大的可视化手段，来帮助我们诊断布局问题。

为了使用Flutter Inspector，我们需要回到Android Studio，通过工具栏上的“Open DevTools”按钮启动Flutter Inspector：

![49f8e946473a49e399dcc8e322572f11](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/49f8e946473a49e399dcc8e322572f11.jpg)

图9 Flutter Inspector启动按钮

随后，Android Studio会打开浏览器，将计数器示例中的Widget树结构展示在面板中。可以看到，Flutter Inspector所展示的Widget树结构，与代码中实现的Widget层次是一一对应的。

![e905a92ecb3546bcbedc46b0da070662](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e905a92ecb3546bcbedc46b0da070662.jpg)

图10 Flutter Inspector示意图

我们的App运行在iPhone X之上，其分辨率为375*812。接下来，我们以Column组件的布局信息为例，通过确认其水平方向为居中布局、垂直方向为充满父Widget剩余空间的过程，来说明**Flutter Inspector的具体用法**。

为了确认Column在垂直方向是充满其父Widget剩余空间的，我们首先需要确定其父Widget在垂直方向上的另一个子Widget，即AppBar的信息。我们点击Flutter Inspector面板左侧中的AppBar控件，右侧对应显示了它的具体视觉信息。

可以看到AppBar控件距离左边距为0，上边距也为0；宽为375，高为100：

![2b8cc11b2aa74b48a8553e3cca6d3134](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/2b8cc11b2aa74b48a8553e3cca6d3134.jpg)

图11 Flutter Inspector之AppBar

然后，我们将Flutter Inspector面板左侧选择的控件更新为Column，右侧也更新了它的具体视觉信息，比如排版方向、对齐模式、渲染信息，以及它的两个子Widget-Text。

可以看到，Column控件的距离左边距为38.5，上边距为0；宽为298，高为712：

![91820dbbcada448baf1fc1815ef06f1a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/91820dbbcada448baf1fc1815ef06f1a.jpg)

图12 Flutter Inspector之Columnn

通过上面的数据我们可以得出：

- Column的右边距=父Widget宽度（即iPhone X宽度375）-Column左边距（即38.5）- Column宽（即298）=38.5，即左右边距相等，因此Column是水平方向居中的；
- Column的高度=父Widget的高度（即iPhone X高度812）- AppBar上边距（即0）- AppBar高度（即100） - Column上边距（即0）= 712.0，即Column在垂直方向上完全填满了父Widget除去AppBar之后的剩余空间。

因此，Column的布局行为是完全符合预期的。

#### 总结

好了，今天的分享就到这里，我们总结一下今天的主要内容吧。

首先，我带你学习了如何实现定制日志的输出能力。Flutter提供了debugPrint函数，这是一个可以被覆盖的打印函数。我们可以分别定义生产环境与开发环境的日志输出行为，来满足开发期打日志需求的同时，保证发布期日志执行信息不会被意外打印。

然后，我与你介绍了Android Studio提供的Flutter调试功能，并通过观察计数器工程的计数器变量为例，与你讲述了具体的调试方法。

最后，我们一起学习了Flutter的布局调试能力，即通过Debug Paiting来定义辅助线，以及通过Flutter Inspector这种可视化手段来更为准确地诊断布局问题。

写代码不可避免会出现Bug，出现时就需要Debug（调试）。调试代码本质上就是一个不断收敛问题发生范围的过程，因此排查问题的一个最基本思路，就是二分法。

所谓二分调试法，是指通过某种稳定复现的特征（比如Crash、某个变量的值、是否出现某个现象等任何明显的迹象），加上一个能把问题出现的范围划分为两半的手段（比如断点、assert、日志等），两者结合反复迭代不断将问题可能出现的范围一分为二（比如能判断出引发问题的代码出现在断点之前等）。通过二分法，我们可以快速缩小问题范围，这样一来调试的效率也就上去了。

#### 思考题

最后，我给你留下一道思考题吧。

请将debugPrint在生产环境下的打印日志行为更改为写日志文件。其中，日志文件一共5个（0-4），每个日志文件不能超过2MB，但可以循环写。如果日志文件已满，则循环至下一个日志文件，清空后重新写入。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何检测并优化Flutter App的整体性能表现？

你好，我是陈航。

在上一篇文章中，我与你分享了调试Flutter代码的3种基本方式，即输出日志、断点调试与布局调试。

通过可定制打印行为的debugPrint函数，我们可以实现生产环境与开发环境不同的日志输出行为，从而保证在开发期打印的调试信息不会被发布至线上；借助于IDE（Android Studio）所提供的断点调试选项，我们可以不断调整代码执行步长和代码暂停条件，收敛问题发生范围，直至找到问题根源；而如果我们想找出代码中的布局渲染类Bug，则可以通过Debug Painting和Flutter Inspector提供的辅助线和视图可视化信息，来更为精准地定位视觉问题。

除了代码逻辑Bug和视觉异常这些功能层面的问题之外，移动应用另一类常见的问题是性能问题，比如滑动操作不流畅、页面出现卡顿丢帧现象等。这些问题虽然不至于让移动应用完全不可用，但也很容易引起用户反感，从而对应用质量产生质疑，甚至失去耐心。

那么，如果应用渲染并不流畅，出现了性能问题，我们该如何检测，又该从哪里着手处理呢？

在Flutter中，性能问题可以分为GPU线程问题和UI线程（CPU）问题两类。这些问题的确认都需要先通过性能图层进行初步分析，而一旦确认问题存在，接下来就需要利用Flutter提供的各类分析工具来定位问题了。

所以在今天这篇文章中，我会与你一起学习分析Flutter应用性能问题的基本思路和工具，以及常见的优化办法。

#### 如何使用性能图层？

要解决问题，我们首先得了解如何去度量问题，性能分析也不例外。Flutter提供了度量性能问题的工具和手段，来帮助我们快速定位代码中的性能问题，而性能图层就是帮助我们确认问题影响范围的利器。

**为了使用性能图层，我们首先需要以分析（Profile）模式启动应用。**与调试代码可以通过模拟器在调试模式下找到代码逻辑Bug不同，性能问题需要在发布模式下使用真机进行检测。

这是因为，相比发布模式而言，调试模式增加了很多额外的检查（比如断言），这些检查可能会耗费很多资源；更重要的是，调试模式使用JIT模式运行应用，代码执行效率较低。这就使得调试模式运行的应用，无法真实反映出它的性能问题。

而另一方面，模拟器使用的指令集为x86，而真机使用的指令集是ARM。这两种方式的二进制代码执行行为完全不同，因此模拟器与真机的性能差异较大：一些x86指令集擅长的操作模拟器会比真机快，而另一些操作则会比真机慢。这也使得我们无法使用模拟器来评估真机才能出现的性能问题。

**为了调试性能问题，我们需要在发布模式的基础之上，为分析工具提供少量必要的应用追踪信息，这就是分析模式**。除了一些调试性能问题必须的追踪方法之外，Flutter应用的分析模式和发布模式的编译和运行是类似的，只是启动参数变成了profile而已：我们既可以在Android Studio中通过菜单栏点击Run->Profile ‘main.dart’ 选项启动应用，也可以通过命令行参数flutter run –profile运行Flutter应用。

#### 分析渲染问题

在完成了应用启动之后，接下来我们就可以利用Flutter提供的渲染问题分析工具，即性能图层（Performance Overlay），来分析渲染问题了。

性能图层会在当前应用的最上层，以Flutter引擎自绘的方式展示GPU与UI线程的执行图表，而其中每一张图表都代表当前线程最近 300帧的表现，如果UI产生了卡顿（跳帧），这些图表可以帮助我们分析并找到原因。

下图演示了性能图层的展现样式。其中，GPU线程的性能情况在上面，UI线程的情况显示在下面，蓝色垂直的线条表示已执行的正常帧，绿色的线条代表的是当前帧：

![0454578b888a45038e1e23d8111eb872](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0454578b888a45038e1e23d8111eb872.jpg)

图1 性能图层

为了保持60Hz的刷新频率，GPU线程与UI线程中执行每一帧耗费的时间都应该小于16ms（1/60秒）。在这其中有一帧处理时间过长，就会导致界面卡顿，图表中就会展示出一个红色竖条。下图演示了应用出现渲染和绘制耗时的情况下，性能图层的展示样式：

![95559c0e75c2452ca06db383e096a032](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/95559c0e75c2452ca06db383e096a032.jpg)

图2 渲染和绘制耗时异常

如果红色竖条出现在GPU线程图表，意味着渲染的图形太复杂，导致无法快速渲染；而如果是出现在了UI线程图表，则表示Dart代码消耗了大量资源，需要优化代码执行时间。

接下来，我们就先看看GPU问题定位吧。

#### GPU问题定位

GPU问题主要集中在底层渲染耗时上。有时候Widget树虽然构造起来容易，但在GPU线程下的渲染却很耗时。涉及Widget裁剪、蒙层这类多视图叠加渲染，或是由于缺少缓存导致静态图像的反复绘制，都会明显拖慢GPU的渲染速度。

我们可以使用性能图层提供的两项参数，即检查多视图叠加的视图渲染开关checkerboardOffscreenLayers，和检查缓存的图像开关checkerboardRasterCacheImages，来检查这两种情况。

##### checkerboardOffscreenLayers

多视图叠加通常会用到Canvas里的savaLayer方法，这个方法在实现一些特定的效果（比如半透明）时非常有用，但由于其底层实现会在GPU渲染上涉及多图层的反复绘制，因此会带来较大的性能问题。

对于saveLayer方法使用情况的检查，我们只要在MaterialApp的初始化方法中，将checkerboardOffscreenLayers开关设置为true，分析工具就会自动帮我们检测多视图叠加的情况了：使用了saveLayer的Widget会自动显示为棋盘格式，并随着页面刷新而闪烁。

不过，saveLayer是一个较为底层的绘制方法，因此我们一般不会直接使用它，而是会通过一些功能性Widget，在涉及需要剪切或半透明蒙层的场景中间接地使用。所以一旦遇到这种情况，我们需要思考一下是否一定要这么做，能不能通过其他方式来实现呢。

比如下面的例子中，我们使用CupertinoPageScaffold与CupertinoNavigationBar实现了一个动态模糊的效果。

```
CupertinoPageScaffold(
  navigationBar: CupertinoNavigationBar(),//动态模糊导航栏
    child: ListView.builder(
      itemCount: 100,
      //为列表创建100个不同颜色的RowItem
      itemBuilder: (context, index)=>TabRowItem(
            index: index,
            lastItem: index == 100 - 1,
            color: colorItems[index],//设置不同的颜色
            colorName: colorNameItems[index],
          )
    )
);
```

![2432e7c4b3a8475eb56045d9004c26d3](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/2432e7c4b3a8475eb56045d9004c26d3.jpg)

图3 动态模糊效果

由于视图滚动过程中频繁涉及视图蒙层效果的更新，因此checkerboardOffscreenLayers检测图层也感受到了对GPU的渲染压力，频繁的刷新闪烁。

![bb102613312b48c4b447b8bd177a4b49](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/bb102613312b48c4b447b8bd177a4b49.jpg)

图4 检测saveLayer使用

如果我们没有对动态模糊效果的特殊需求，则可以使用不带模糊效果的Scaffold和白色的AppBar实现同样的产品功能，来解决这个性能问题：

```
Scaffold(
  //使用普通的白色AppBar
  appBar: AppBar(title: Text('Home', style: TextStyle(color:Colors.black),),backgroundColor: Colors.white),
  body: ListView.builder(
      itemCount: 100,
      //为列表创建100个不同颜色的RowItem
      itemBuilder: (context, index)=>TabRowItem(
        index: index,
        lastItem: index == 100 - 1,
        color: colorItems[index],//设置不同的颜色
        colorName: colorNameItems[index],
      )
  ),
);
```

运行一下代码，可以看到，在去掉了动态模糊效果之后，GPU的渲染压力得到了缓解，checkerboardOffscreenLayers检测图层也不再频繁闪烁了。

![d53ab174a6ca4ca1be91118a24354d23](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d53ab174a6ca4ca1be91118a24354d23.jpg)

图5 去掉动态模糊效果

##### checkerboardRasterCacheImages

从资源的角度看，另一类非常消耗性能的操作是，渲染图像。这是因为图像的渲染涉及I/O、GPU存储，以及不同通道的数据格式转换，因此渲染过程的构建需要消耗大量资源。为了缓解GPU的压力，Flutter提供了多层次的缓存快照，这样Widget重建时就无需重新绘制静态图像了。

与检查多视图叠加渲染的checkerboardOffscreenLayers参数类似，Flutter也提供了检查缓存图像的开关checkerboardRasterCacheImages，来检测在界面重绘时频繁闪烁的图像（即没有静态缓存）。

我们可以把需要静态缓存的图像加到RepaintBoundary中，RepaintBoundary可以确定Widget树的重绘边界，如果图像足够复杂，Flutter引擎会自动将其缓存，避免重复刷新。当然，因为缓存资源有限，如果引擎认为图像不够复杂，也可能会忽略RepaintBoundary。

如下代码展示了通过RepaintBoundary，将一个静态复合Widget加入缓存的具体用法。可以看到，RepaintBoundary在使用上与普通Widget并无区别：

```
RepaintBoundary(//设置静态缓存图像
  child: Center(
    child: Container(
      color: Colors.black,
      height: 10.0,
      width: 10.0,
    ),
));
```

#### UI线程问题定位

如果说GPU线程问题定位的是渲染引擎底层渲染异常，那么UI线程问题发现的则是应用的性能瓶颈。比如在视图构建时，在build方法中使用了一些复杂的运算，或是在主Isolate中进行了同步的I/O操作。这些问题，都会明显增加CPU的处理时间，拖慢应用的响应速度。

这时，我们可以使用Flutter提供的Performance工具，来记录应用的执行轨迹。Performance是一个强大的性能分析工具，能够以时间轴的方式展示CPU的调用栈和执行时间，去检查代码中可疑的方法调用。

在点击了Android Studio底部工具栏中的“Open DevTools”按钮之后，系统会自动打开Dart DevTools的网页，将顶部的tab切换到Performance后，我们就可以开始分析代码中的性能问题了。

![5109468520bb4efaab4c7b4d4938c7c5](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/5109468520bb4efaab4c7b4d4938c7c5.jpg)

图6 打开Performance工具

![a296fb0905ba465fbcc146460acfe902](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a296fb0905ba465fbcc146460acfe902.jpg)

图7 Performance主界面

接下来，我们通过一个ListView中计算MD5的例子，来演示Performance的具体分析过程。

考虑到在build函数中进行渲染信息的组装是一个常见的操作，为了演示这个知识点，我们故意放大了计算MD5的耗时，循环迭代计算了1万次：

```
class MyHomePage extends StatelessWidget {
  MyHomePage({Key key}) : super(key: key);

  String generateMd5(String data) {
    //MD5固定算法
    var content = new Utf8Encoder().convert(data);
    var digest = md5.convert(content);
    return hex.encode(digest.bytes);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('demo')),
      body: ListView.builder(
          itemCount: 30,// 列表元素个数
          itemBuilder: (context, index) {
            //反复迭代计算MD5
            String str = '1234567890abcdefghijklmnopqrstuvwxyz';
            for(int i = 0;i<10000;i++) {
              str = generateMd5(str);
            }
            return ListTile(title: Text("Index : $index"), subtitle: Text(str));
          }// 列表项创建方法
      ),
    );
  }
}
```

与性能图层能够自动记录应用执行情况不同，使用Performance来分析代码执行轨迹，我们需要手动点击“Record”按钮去主动触发，在完成信息的抽样采集后，点击“Stop”按钮结束录制。这时，我们就可以得到在这期间应用的执行情况了。

Performance记录的应用执行情况叫做CPU帧图，又被称为火焰图。火焰图是基于记录代码执行结果所产生的图片，用来展示CPU的调用栈，表示的是CPU 的繁忙程度。

其中，y轴表示调用栈，其每一层都是一个函数。调用栈越深，火焰就越高，底部就是正在执行的函数，上方都是它的父函数；x轴表示单位时间，一个函数在x轴占据的宽度越宽，就表示它被采样到的次数越多，即执行时间越长。

所以，我们要检测CPU耗时问题，皆可以查看火焰图底部的哪个函数占据的宽度最大。只要有“平顶”，就表示该函数可能存在性能问题。比如，我们这个案例的火焰图如下所示：

![4791e7971c9e4f8eb50a7564ece4a370](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/4791e7971c9e4f8eb50a7564ece4a370.jpg)

图8 CPU帧图/火焰图

可以看到，_MyHomePage.generateMd5函数的执行时间最长，几乎占满了整个火焰图的宽，而这也与代码中存在的问题是一致的。

在找到了问题之后，我们就可以使用Isolate（或compute）将这些耗时的操作挪到并发主Isolate之外去完成了。

#### 总结

好了，今天的分享就到这里。我们总结一下今天的主要内容吧。

在Flutter中，性能分析过程可以分为GPU线程问题定位和UI线程（CPU）问题定位，而它们都需要在真机上以分析模式（Profile）启动应用，并通过性能图层分析大致的渲染问题范围。一旦确认问题存在，接下来就需要利用Flutter所提供的分析工具来定位问题原因了。

关于GPU线程渲染问题，我们可以重点检查应用中是否存在多视图叠加渲染，或是静态图像反复刷新的现象。而UI线程渲染问题，我们则是通过Performance工具记录的火焰图（CPU帧图），分析代码耗时，找出应用执行瓶颈。

通常来说，由于Flutter采用基于声明式的UI设计理念，以数据驱动渲染，并采用Widget->Element->RenderObject三层结构，屏蔽了无谓的界面刷新，能够保证绝大多数情况下我们构建的应用都是高性能的，所以在使用分析工具检测出性能问题之后，通常我们并不需要做太多的细节优化工作，只需要在改造过程中避开一些常见的坑，就可以获得优异的性能。比如：

- 控制build方法耗时，将Widget拆小，避免直接返回一个巨大的Widget，这样Widget会享有更细粒度的重建和复用；
- 尽量不要为Widget设置半透明效果，而是考虑用图片的形式代替，这样被遮挡的Widget部分区域就不需要绘制了；
- 对列表采用懒加载而不是直接一次性创建所有的子Widget，这样视图的初始化时间就减少了。

#### 思考题

最后，我给你留下一道思考题吧。

请你改造ListView计算MD5的示例，在保证原有功能的情况下，使用并发Isolate（或compute）完成MD5的计算。提示：计算过程可以使用CircularProgressIndicator来展示加载动画。

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何通过自动化测试提高交付质量？

你好，我是陈航。

在上一篇文章中，我与你分享了如何分析并优化Flutter应用的性能问题。通过在真机上以分析模式运行应用，我们可以借助于性能图层的帮助，找到引起性能瓶颈的两类问题，即GPU渲染问题和CPU执行耗时问题。然后，我们就可以使用Flutter提供的渲染开关和CPU帧图（火焰图），来检查应用中是否存在过度渲染或是代码执行耗时长的情况，从而去定位并着手解决应用的性能问题了。

在完成了应用的开发工作，并解决了代码中的逻辑问题和性能问题之后，接下来我们就需要测试验收应用的各项功能表现了。移动应用的测试工作量通常很大，这是因为为了验证真实用户的使用体验，测试往往需要跨越多个平台（Android/iOS）及不同的物理设备手动完成。

随着产品功能不断迭代累积，测试工作量和复杂度也随之大幅增长，手动测试变得越来越困难。那么，在为产品添加新功能，或者修改已有功能时，如何才能确保应用可以继续正常工作呢？

答案是，通过编写自动化测试用例。

所谓自动化测试，是把由人驱动的测试行为改为由机器执行。具体来说就是，通过精心设计的测试用例，由机器按照执行步骤对应用进行自动测试，并输出执行结果，最后根据测试用例定义的规则确定结果是否符合预期。

也就是说，自动化测试将重复的、机械的人工操作变为自动化的验证步骤，极大的节省人力、时间和硬件资源，从而提高了测试效率。

在自动化测试用例的编写上，Flutter提供了包括单元测试和UI测试的能力。其中，单元测试可以方便地验证单个函数、方法或类的行为，而UI测试则提供了与Widget进行交互的能力，确认其功能是否符合预期。

接下来，我们就具体看看这两种自动化测试用例的用法吧。

#### 单元测试

单元测试是指，对软件中的最小可测试单元进行验证的方式，并通过验证结果来确定最小单元的行为是否与预期一致。所谓最小可测试单元，一般来说，就是人为规定的、最小的被测功能模块，比如语句、函数、方法或类。

在Flutter中编写单元测试用例，我们可以在pubspec.yaml文件中使用test包来完成。其中，test包提供了编写单元测试用例的核心框架，即定义、执行和验证。如下代码所示，就是test包的用法：

```
dev_dependencies:
  test:
```

> 备注：test包的声明需要在dev_dependencies下完成，在这个标签下面定义的包只会在开发模式生效。

与Flutter应用通过main函数定义程序入口相同，Flutter单元测试用例也是通过main函数来定义测试入口的。不过，**这两个程序入口的目录位置有些区别**：应用程序的入口位于工程中的lib目录下，而测试用例的入口位于工程中的test目录下。

一个有着单元测试用例的Flutter工程目录结构，如下所示：

![67da2a4e8bb647589f7b4383d9a7e55d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/67da2a4e8bb647589f7b4383d9a7e55d.jpg)

图1 Flutter工程目录结构

接下来，我们就可以在main.dart中声明一个用来测试的类了。在下面的例子中，我们声明了一个计数器类Counter，这个类可以支持以递增或递减的方式修改计数值count：

```
class Counter {
  int count = 0;
  void increase() => count++;
  void decrease() => count--;
}
```

实现完待测试的类，我们就可以为它编写测试用例了。**在Flutter中，测试用例的声明包含定义、执行和验证三个部分：**定义和执行决定了被测试对象提供的、需要验证的最小可测单元；而验证则需要使用expect函数，将最小可测单元的执行结果与预期进行比较。

所以，在Flutter中编写一个测试用例，通常包含以下两大步骤：

1. 实现一个包含定义、执行和验证步骤的测试用例；
2. 将其包装在test内部，test是Flutter提供的测试用例封装类。

在下面的例子中，我们定义了两个测试用例，其中第一个用例用来验证调用increase函数后的计数器值是否为1，而第二个用例则用来判断1+1是否等于2：

```
import 'package:test/test.dart';
import 'package:flutter_app/main.dart';

void main() {
  //第一个用例，判断Counter对象调用increase方法后是否等于1
  test('Increase a counter value should be 1', () {
    final counter = Counter();
    counter.increase();
    expect(counter.value, 1);
  });
  //第二个用例，判断1+1是否等于2
  test('1+1 should be 2', () {
    expect(1+1, 2);
  });
}
```

选择widget_test.dart文件，在右键弹出的菜单中选择“Run ‘tests in widget_test’”，就可以启动测试用例了。

![92cfc8bd0f8a46839d19a841f728f9e9](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/92cfc8bd0f8a46839d19a841f728f9e9.jpg)

图2 启动测试用例入口

稍等片刻，控制台就会输出测试用例的执行结果了。当然，这两个用例都能通过测试：

```
22:05	Tests passed: 2
```

**如果测试用例的执行结果是不通过，Flutter会给我们怎样的提示呢？**我们试着修改一下第一个计数器递增的用例，将它的期望结果改为2：

```
test('Increase a counter value should be 1', () {
  final counter = Counter();
  counter.increase();
  expect(counter.value, 2);//判断Counter对象调用increase后是否等于2
});
```

运行测试用例，可以看到，Flutter在执行完计数器的递增方法后，发现其结果1与预期的2不匹配，于是报错：

![ba9c9153fe8e486991a0963775e209fd](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ba9c9153fe8e486991a0963775e209fd.jpg)

图3 单元测试失败示意图

上面的示例演示了单个测试用例的编写方法，而**如果有多个测试用例**，它们之间是存在关联关系的，我们可以在最外层使用group将它们组合在一起。

在下面的例子中，我们定义了计数器递增和计数器递减两个用例，验证递增的结果是否等于1的同时判断递减的结果是否等于-1，并把它们组合在了一起：

```
import 'package:test/test.dart';
import 'package:counter_app/counter.dart';
void main() {
  //组合测试用例，判断Counter对象调用increase方法后是否等于1，并且判断Counter对象调用decrease方法后是否等于-1
  group('Counter', () {
    test('Increase a counter value should be 1', () {
      final counter = Counter();
      counter.increase();
      expect(counter.value, 1);
    });

    test('Decrease a counter value should be -1', () {
      final counter = Counter();
      counter.decrease();
      expect(counter.value, -1);
    });
  });
}
```

同样的，这两个测试用例的执行结果也是通过。

**在对程序的内部功能进行单元测试时，我们还可能需要从外部依赖（比如Web服务）获取需要测试的数据。**比如下面的例子，Todo对象的初始化就是通过Web服务返回的JSON实现的。考虑到调用Web服务的过程中可能会出错，所以我们还处理了请求码不等于200的其他异常情况：

```
import 'package:http/http.dart' as http;

class Todo {
  final String title;
  Todo({this.title});
  //工厂类构造方法，将JSON转换为对象
  factory Todo.fromJson(Map<String, dynamic> json) {
    return Todo(
      title: json['title'],
    );
  }
}

Future<Todo> fetchTodo(http.Client client) async {
  final response =
  await client.get('https://xxx.com/todos/1');

  if (response.statusCode == 200) {
    //请求成功，解析JSON
    return Todo.fromJson(json.decode(response.body));
  } else {
    //请求失败，抛出异常
    throw Exception('Failed to load post');
  }
}
```

考虑到这些外部依赖并不是我们的程序所能控制的，因此很难覆盖所有可能的成功或失败方案。比如，对于一个正常运行的Web服务来说，我们基本不可能测试出fetchTodo这个接口是如何应对403或502状态码的。因此，更好的一个办法是，在测试用例中“模拟”这些外部依赖（对应本例即为http.client），让这些外部依赖可以返回特定结果。

在单元测试用例中模拟外部依赖，我们需要在pubspec.yaml文件中使用mockito包，以接口实现的方式定义外部依赖的接口：

```
dev_dependencies:
  test:
  mockito:
```

要**使用mockito包来模拟fetchTodo的依赖http.client**，我们首先需要定义一个继承自Mock（这个类可以模拟任何外部依赖），并以接口定义的方式实现了http.client的模拟类；然后，在测试用例的声明中，为其制定任意的接口返回。

在下面的例子中，我们定义了一个模拟类MockClient，这个类以接口声明的方式获取到了http.Client的外部接口。随后，我们就可以使用when语句，在其调用Web服务时，为其注入相应的数据返回了。在第一个用例中，我们为其注入了JSON结果；而在第二个用例中，我们为其注入了一个403的异常。

```
import 'package:mockito/mockito.dart';
import 'package:http/http.dart' as http;

class MockClient extends Mock implements http.Client {}

void main() {
  group('fetchTodo', () {
  test('returns a Todo if successful', () async {
    final client = MockClient();

    //使用Mockito注入请求成功的JSON字段
    when(client.get('https://xxx.com/todos/1'))
        .thenAnswer((_) async => http.Response('{"title": "Test"}', 200));
    //验证请求结果是否为Todo实例
    expect(await fetchTodo(client), isInstanceOf<Todo>());
  });

  test('throws an exception if error', () {
    final client = MockClient();

    //使用Mockito注入请求失败的Error
    when(client.get('https://xxx.com/todos/1'))
        .thenAnswer((_) async => http.Response('Forbidden', 403));
    //验证请求结果是否抛出异常
    expect(fetchTodo(client), throwsException);
  });
});
}
```

运行这段测试用例，可以看到，我们在没有调用真实Web服务的情况下，成功模拟出了正常和异常两种结果，同样也是顺利通过验证了。

接下来，我们再看看UI测试吧。

#### UI测试

UI测试的目的是模仿真实用户的行为，即以真实用户的身份对应用程序执行UI交互操作，并涵盖各种用户流程。相比于单元测试，UI测试的覆盖范围更广、更关注流程和交互，可以找到单元测试期间无法找到的错误。

在Flutter中编写UI测试用例，我们需要在pubspec.yaml中使用flutter_test包，来提供编写**UI测试的核心框架**，即定义、执行和验证：

- 定义，即通过指定规则，找到UI测试用例需要验证的、特定的子Widget对象；
- 执行，意味着我们要在找到的子Widget对象中，施加用户交互事件；
- 验证，表示在施加了交互事件后，判断待验证的Widget对象的整体表现是否符合预期。

如下代码所示，就是flutter_test包的用法：

```
dev_dependencies:
  flutter_test:
    sdk: flutter
```

接下来，我以Flutter默认的计时器应用模板为例，与你说明**UI测试用例的编写方法**。

在计数器应用中，有两处地方会响应外部交互事件，包括响应用户点击行为的按钮Icon，与响应渲染刷新事件的文本Text。按钮点击后，计数器会累加，文本也随之刷新。

![f359811a93e241078f2824875250e4f4](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/f359811a93e241078f2824875250e4f4.jpg)

图4 计数器示例

为确保程序的功能正常，我们希望编写一个UI测试用例，来验证按钮的点击行为是否与文本的刷新行为完全匹配。

与单元测试使用test对用例进行包装类似，**UI测试使用testWidgets对用例进行包装**。testWidgets提供了tester参数，我们可以使用这个实例来操作需要测试的Widget对象。

在下面的代码中，我们**首先**声明了需要验证的MyApp对象。在通过pumpWidget触发其完成渲染后，使用find.text方法分别查找了字符串文本为0和1的Text控件，目的是验证响应刷新事件的文本Text的初始化状态是否为0。

**随后**，我们通过find.byIcon方法找到了按钮控件，并通过tester.tap方法对其施加了点击行为。在完成了点击后，我们使用tester.pump方法强制触发其完成渲染刷新。**最后**，我们使用了与验证Text初始化状态同样的语句，判断在响应了刷新事件后的文本Text其状态是否为1：

```
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_app_demox/main.dart';

void main() {
  testWidgets('Counter increments UI test', (WidgetTester tester) async {
  //声明所需要验证的Widget对象(即MyApp)，并触发其渲染
  await tester.pumpWidget(MyApp());

  //查找字符串文本为'0'的Widget，验证查找成功
  expect(find.text('0'), findsOneWidget);
  //查找字符串文本为'1'的Widget，验证查找失败
  expect(find.text('1'), findsNothing);

  //查找'+'按钮，施加点击行为
  await tester.tap(find.byIcon(Icons.add));
  //触发其渲染
  await tester.pump();

  //查找字符串文本为'0'的Widget，验证查找失败
  expect(find.text('0'), findsNothing);
  //查找字符串文本为'1'的Widget，验证查找成功
  expect(find.text('1'), findsOneWidget);
});
}
```

运行这段UI测试用例代码，同样也顺利通过验证了。

除了点击事件之外，tester还支持其他的交互行为，比如文字输入enterText、拖动drag、长按longPress等，这里我就不再一一赘述了。如果你想深入理解这些内容，可以参考WidgetTester的[官方文档](https://api.flutter.dev/flutter/flutter_test/WidgetTester-class.html)进行学习。

#### 总结

好了，今天的分享就到这里，我们总结一下今天的主要内容吧。

在Flutter中，自动化测试可以分为单元测试和UI测试。

单元测试的步骤，包括定义、执行和验证。通过单元测试用例，我们可以验证单个函数、方法或类，其行为表现是否与预期一致。而UI测试的步骤，同样是包括定义、执行和验证。我们可以通过模仿真实用户的行为，对应用进行交互操作，覆盖更广的流程。

如果测试对象存在像Web服务这样的外部依赖，为了让单元测试过程更为可控，我们可以使用mockito为其定制任意的数据返回，实现正常和异常两种测试用例。

需要注意的是，尽管UI测试扩大了应用的测试范围，可以找到单元测试期间无法找到的错误，不过相比于单元测试用例来说，UI测试用例的开发和维护代价非常高。因为一个移动应用最主要的功能其实就是UI，而UI的变化非常频繁，UI测试需要不断的维护才能保持稳定可用的状态。

“投入和回报”永远是考虑是否采用UI测试，以及采用何种级别的UI测试，需要最优先考虑的问题。我推荐的原则是，项目达到一定的规模，并且业务特征具有一定的延续规律性后，再考虑UI测试的必要性。

我把今天分享涉及的知识点打包到了[GitHub](https://github.com/cyndibaby905/38_test_app)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留下一道思考题吧。

在下面的代码中，我们定义了SharedPreferences的更新和递增方法。请你使用mockito模拟SharedPreferences的方式，来为这两个方法实现对应的单元测试用例。

```
Future<bool>updateSP(SharedPreferences prefs, int counter) async {
  bool result = await prefs.setInt('counter', counter);
  return result;
}

Future<int>increaseSPCounter(SharedPreferences prefs) async {
  int counter = (prefs.getInt('counter') ?? 0) + 1;
  await updateSP(prefs, counter);
  return counter;
}
```

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 线上出现问题，该如何做好异常捕获与信息采集？

你好，我是陈航。

在上一篇文章中，我与你分享了如何为一个Flutter工程编写自动化测试用例。设计一个测试用例的基本步骤可以分为3步，即定义、执行和验证，而Flutter提供的单元测试和UI测试框架则可以帮助我们简化这些步骤。

其中，通过单元测试，我们可以很方便地验证单个函数、方法或类的行为，还可以利用mockito定制外部依赖返回任意数据，从而让测试更可控；而UI测试则提供了与Widget交互的能力，我们可以模仿用户行为，对应用进行相应的交互操作，确认其功能是否符合预期。

通过自动化测试，我们可以把重复的人工操作变成自动化的验证步骤，从而在开发阶段更及时地发现问题。但终端设备的碎片化，使得我们终究无法在应用开发期就完全模拟出真实用户的运行环境。所以，无论我们的应用写得多么完美、测试得多么全面，总是无法完全避免线上的异常问题。

这些异常，可能是因为不充分的机型适配、用户糟糕的网络状况；也可能是因为Flutter框架自身的Bug，甚至是操作系统底层的问题。这些异常一旦发生，Flutter应用会无法响应用户的交互事件，轻则报错，重则功能无法使用甚至闪退，这对用户来说都相当不友好，是开发者最不愿意看到的。

所以，我们要想办法去捕获用户的异常信息，将异常现场保存起来，并上传至服务器，这样我们就可以分析异常上下文，定位引起异常的原因，去解决此类问题了。那么今天，我们就一起来学习下Flutter异常的捕获和信息采集，以及对应的数据上报处理。

#### Flutter异常

Flutter异常指的是，Flutter程序中Dart代码运行时意外发生的错误事件。我们可以通过与Java类似的try-catch机制来捕获它。但**与Java不同的是，Dart程序不强制要求我们必须处理异常**。

这是因为，Dart采用事件循环的机制来运行任务，所以各个任务的运行状态是互相独立的。也就是说，即便某个任务出现了异常我们没有捕获它，Dart程序也不会退出，只会导致当前任务后续的代码不会被执行，用户仍可以继续使用其他功能。

Dart异常，根据来源又可以细分为App异常和Framework异常。Flutter为这两种异常提供了不同的捕获方式，接下来我们就一起看看吧。

#### App异常的捕获方式

App异常，就是应用代码的异常，通常由未处理应用层其他模块所抛出的异常引起。根据异常代码的执行时序，App异常可以分为两类，即同步异常和异步异常：同步异常可以通过try-catch机制捕获，异步异常则需要采用Future提供的catchError语句捕获。

这两种异常的捕获方式，如下代码所示：

```
//使用try-catch捕获同步异常
try {
  throw StateError('This is a Dart exception.');
}
catch(e) {
  print(e);
}

//使用catchError捕获异步异常
Future.delayed(Duration(seconds: 1))
    .then((e) => throw StateError('This is a Dart exception in Future.'))
    .catchError((e)=>print(e));

//注意，以下代码无法捕获异步异常
try {
  Future.delayed(Duration(seconds: 1))
      .then((e) => throw StateError('This is a Dart exception in Future.'))
}
catch(e) {
  print("This line will never be executed. ");
}
```

需要注意的是，这两种方式是不能混用的。可以看到，在上面的代码中，我们是无法使用try-catch去捕获一个异步调用所抛出的异常的。

同步的try-catch和异步的catchError，为我们提供了直接捕获特定异常的能力，而如果我们想集中管理代码中的所有异常，Flutter也提供了Zone.runZoned方法。

我们可以给代码执行对象指定一个Zone，在Dart中，Zone表示一个代码执行的环境范围，其概念类似沙盒，不同沙盒之间是互相隔离的。如果我们想要观察沙盒中代码执行出现的异常，沙盒提供了onError回调函数，拦截那些在代码执行对象中的未捕获异常。

在下面的代码中，我们将可能抛出异常的语句放置在了Zone里。可以看到，在没有使用try-catch和catchError的情况下，无论是同步异常还是异步异常，都可以通过Zone直接捕获到：

```
runZoned(() {
  //同步抛出异常
  throw StateError('This is a Dart exception.');
}, onError: (dynamic e, StackTrace stack) {
  print('Sync error caught by zone');
});

runZoned(() {
  //异步抛出异常
  Future.delayed(Duration(seconds: 1))
      .then((e) => throw StateError('This is a Dart exception in Future.'));
}, onError: (dynamic e, StackTrace stack) {
  print('Async error aught by zone');
});
```

因此，如果我们想要集中捕获Flutter应用中的未处理异常，可以把main函数中的runApp语句也放置在Zone中。这样在检测到代码中运行异常时，我们就能根据获取到的异常上下文信息，进行统一处理了：

```
runZoned<Future<Null>>(() async {
  runApp(MyApp());
}, onError: (error, stackTrace) async {
 //Do sth for error
});
```

接下来，我们再看看Framework异常应该如何捕获吧。

#### Framework异常的捕获方式

Framework异常，就是Flutter框架引发的异常，通常是由应用代码触发了Flutter框架底层的异常判断引起的。比如，当布局不合规范时，Flutter就会自动弹出一个触目惊心的红色错误界面，如下所示：

![f4cd2664be3249bab0fcde62d23c299c](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/f4cd2664be3249bab0fcde62d23c299c.jpg)

图1 Flutter布局错误提示

这其实是因为，Flutter框架在调用build方法构建页面时进行了try-catch 的处理，并提供了一个ErrorWidget，用于在出现异常时进行信息提示：

```
@override
void performRebuild() {
  Widget built;
  try {
    //创建页面
    built = build();
  } catch (e, stack) {
    //使用ErrorWidget创建页面
    built = ErrorWidget.builder(_debugReportException(ErrorDescription("building $this"), e, stack));
    ...
  }
  ...
}
```

这个页面反馈的信息比较丰富，适合开发期定位问题。但如果让用户看到这样一个页面，就很糟糕了。因此，我们通常会重写ErrorWidget.builder方法，将这样的错误提示页面替换成一个更加友好的页面。

下面的代码演示了自定义错误页面的具体方法。在这个例子中，我们直接返回了一个居中的Text控件：

```
ErrorWidget.builder = (FlutterErrorDetails flutterErrorDetails){
  return Scaffold(
    body: Center(
      child: Text("Custom Error Widget"),
    )
  );
};
```

运行效果如下所示：

![92ca932871d64a7cb932d5c6af1786d6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/92ca932871d64a7cb932d5c6af1786d6.jpg)

图2 自定义错误提示页面

比起之前触目惊心的红色错误页面，白色主题的自定义页面看起来稍微友好些了。需要注意的是，ErrorWidget.builder方法提供了一个参数details用于表示当前的错误上下文，为避免用户直接看到错误信息，这里我们并没有将它展示到界面上。但是，我们不能丢弃掉这样的异常信息，需要提供统一的异常处理机制，用于后续分析异常原因。

为了集中处理框架异常，**Flutter提供了FlutterError类，这个类的onError属性会在接收到框架异常时执行相应的回调**。因此，要实现自定义捕获逻辑，我们只要为它提供一个自定义的错误处理回调即可。

在下面的代码中，我们使用Zone提供的handleUncaughtError语句，将Flutter框架的异常统一转发到当前的Zone中，这样我们就可以统一使用Zone去处理应用内的所有异常了：

```
FlutterError.onError = (FlutterErrorDetails details) async {
  //转发至Zone中
  Zone.current.handleUncaughtError(details.exception, details.stack);
};

runZoned<Future<Null>>(() async {
  runApp(MyApp());
}, onError: (error, stackTrace) async {
 //Do sth for error
});
```

#### 异常上报

到目前为止，我们已经捕获到了应用中所有的未处理异常。但如果只是把这些异常在控制台中打印出来还是没办法解决问题，我们还需要把它们上报到开发者能看到的地方，用于后续分析定位并解决问题。

关于开发者数据上报，目前市面上有很多优秀的第三方SDK服务厂商，比如友盟、Bugly，以及开源的Sentry等，而它们提供的功能和接入流程都是类似的。考虑到Bugly的社区活跃度比较高，因此我就以它为例，与你演示在抓取到异常后，如何实现自定义数据上报。

##### Dart接口实现

目前Bugly仅提供了原生Android/iOS的SDK，因此我们需要采用与第31篇文章“[如何实现原生推送能力](https://time.geekbang.org/column/article/132818)？”中同样的插件工程，为Bugly的数据上报提供Dart层接口。

与接入Push能力相比，接入数据上报要简单得多，我们只需要完成一些前置应用信息关联绑定和SDK初始化工作，就可以使用Dart层封装好的数据上报接口去上报异常了。可以看到，对于一个应用而言，接入数据上报服务的过程，总体上可以分为两个步骤：

1. 初始化Bugly SDK；
2. 使用数据上报接口。

这两步对应着在Dart层需要封装的2个原生接口调用，即setup和postException，它们都是在方法通道上调用原生代码宿主提供的方法。考虑到数据上报是整个应用共享的能力，因此我们将数据上报类FlutterCrashPlugin的接口都封装成了单例：

```
class FlutterCrashPlugin {
  //初始化方法通道
  static const MethodChannel _channel =
      const MethodChannel('flutter_crash_plugin');

  static void setUp(appID) {
    //使用app_id进行SDK注册
    _channel.invokeMethod("setUp",{'app_id':appID});
  }
  static void postException(error, stack) {
    //将异常和堆栈上报至Bugly
    _channel.invokeMethod("postException",{'crash_message':error.toString(),'crash_detail':stack.toString()});
  }
}
```

Dart层是原生代码宿主的代理，可以看到这一层的接口设计还是比较简单的。接下来，我们分别去接管数据上报的Android和iOS平台上完成相应的实现。

##### iOS接口实现

考虑到iOS平台的数据上报配置工作相对较少，因此我们先用Xcode打开example下的iOS工程进行插件开发工作。需要注意的是，由于iOS子工程的运行依赖于Flutter工程编译构建产物，所以在打开iOS工程进行开发前，你需要确保整个工程代码至少build过一次，否则IDE会报错。

> 备注：以下操作步骤参考[Bugly异常上报iOS SDK接入指南](https://bugly.qq.com/docs/user-guide/instruction-manual-ios/?v=20190712210424)。

**首先**，我们需要在插件工程下的flutter_crash_plugin.podspec文件中引入Bugly SDK，即Bugly，这样我们就可以在原生工程中使用Bugly提供的数据上报功能了：

```
Pod::Spec.new do |s|
  ...
  s.dependency 'Bugly'
end
```

**然后**，在原生接口FlutterCrashPlugin类中，依次初始化插件实例、绑定方法通道，并在方法通道中先后为setup与postException提供Bugly iOS SDK的实现版本：

```
@implementation FlutterCrashPlugin
+ (void)registerWithRegistrar:(NSObject<FlutterPluginRegistrar>*)registrar {
    //注册方法通道
    FlutterMethodChannel* channel = [FlutterMethodChannel
      methodChannelWithName:@"flutter_crash_plugin"
            binaryMessenger:[registrar messenger]];
    //初始化插件实例，绑定方法通道
    FlutterCrashPlugin* instance = [[FlutterCrashPlugin alloc] init];
    //注册方法通道回调函数
    [registrar addMethodCallDelegate:instance channel:channel];
}

- (void)handleMethodCall:(FlutterMethodCall*)call result:(FlutterResult)result {
    if([@"setUp" isEqualToString:call.method]) {
        //Bugly SDK初始化方法
        NSString *appID = call.arguments[@"app_id"];
        [Bugly startWithAppId:appID];
    } else if ([@"postException" isEqualToString:call.method]) {
      //获取Bugly数据上报所需要的各个参数信息
      NSString *message = call.arguments[@"crash_message"];
      NSString *detail = call.arguments[@"crash_detail"];

      NSArray *stack = [detail componentsSeparatedByString:@"\n"];
      //调用Bugly数据上报接口
      [Bugly reportExceptionWithCategory:4 name:message reason:stack[0] callStack:stack extraInfo:@{} terminateApp:NO];
      result(@0);
  }
  else {
    //方法未实现
    result(FlutterMethodNotImplemented);
  }
}

@end
```

至此，在完成了Bugly iOS SDK的接口封装之后，FlutterCrashPlugin插件的iOS部分也就搞定了。接下来，我们去看看Android部分如何实现吧。

##### Android接口实现

与iOS类似，我们需要使用Android Studio打开example下的android工程进行插件开发工作。同样，在打开android工程前，你需要确保整个工程代码至少build过一次，否则IDE会报错。

> 备注：以下操作步骤参考[Bugly异常上报Android SDK接入指南](https://bugly.qq.com/docs/user-guide/instruction-manual-android/)

**首先**，我们需要在插件工程下的build.gradle文件引入Bugly SDK，即crashreport与nativecrashreport，其中前者提供了Java和自定义异常的的数据上报能力，而后者则是JNI的异常上报封装 ：

```
dependencies {
    implementation 'com.tencent.bugly:crashreport:latest.release'
    implementation 'com.tencent.bugly:nativecrashreport:latest.release'
}
```

**然后**，在原生接口FlutterCrashPlugin类中，依次初始化插件实例、绑定方法通道，并在方法通道中先后为setup与postException提供Bugly Android SDK的实现版本：

```
public class FlutterCrashPlugin implements MethodCallHandler {
  //注册器，通常为MainActivity
  public final Registrar registrar;
  //注册插件
  public static void registerWith(Registrar registrar) {
    //注册方法通道
    final MethodChannel channel = new MethodChannel(registrar.messenger(), "flutter_crash_plugin");
    //初始化插件实例，绑定方法通道，并注册方法通道回调函数
    channel.setMethodCallHandler(new FlutterCrashPlugin(registrar));
  }

  private FlutterCrashPlugin(Registrar registrar) {
    this.registrar = registrar;
  }

  @Override
  public void onMethodCall(MethodCall call, Result result) {
    if(call.method.equals("setUp")) {
      //Bugly SDK初始化方法
      String appID = call.argument("app_id");

      CrashReport.initCrashReport(registrar.activity().getApplicationContext(), appID, true);
      result.success(0);
    }
    else if(call.method.equals("postException")) {
      //获取Bugly数据上报所需要的各个参数信息
      String message = call.argument("crash_message");
      String detail = call.argument("crash_detail");
      //调用Bugly数据上报接口
      CrashReport.postException(4,"Flutter Exception",message,detail,null);
      result.success(0);
    }
    else {
      result.notImplemented();
    }
  }
}
```

在完成了Bugly Android接口的封装之后，由于Android系统的权限设置较细，考虑到Bugly还需要网络、日志读取等权限，因此我们还需要在插件工程的AndroidManifest.xml文件中，将这些权限信息显示地声明出来，完成对系统的注册：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.hangchen.flutter_crash_plugin">
    <!-- 电话状态读取权限 -->
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <!-- 网络权限 -->
    <uses-permission android:name="android.permission.INTERNET" />
    <!-- 访问网络状态权限 -->
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <!-- 访问wifi状态权限 -->
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <!-- 日志读取权限 -->
    <uses-permission android:name="android.permission.READ_LOGS" />
</manifest>
```

至此，在完成了极光Android SDK的接口封装和权限配置之后，FlutterCrashPlugin插件的Android部分也搞定了。

FlutterCrashPlugin插件为Flutter应用提供了数据上报的封装，不过要想Flutter工程能够真正地上报异常消息，我们还需要为Flutter工程关联Bugly的应用配置。

##### 应用工程配置

在单独为Android/iOS应用进行数据上报配置之前，我们首先需要去[Bugly的官方网站](https://bugly.qq.com)，为应用注册唯一标识符（即AppKey）。这里需要注意的是，在Bugly中，Android应用与iOS应用被视为不同的产品，所以我们需要分别注册：

![43bdfe91f7994563a1f404a873c2fcde](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/43bdfe91f7994563a1f404a873c2fcde.jpg)

图3 Android应用Demo配置

![a843301fa04348fe8fd9c7aad160221b](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a843301fa04348fe8fd9c7aad160221b.jpg)

图4 iOS应用Demo配置

在得到了AppKey之后，我们需要**依次进行Android与iOS的配置工作**。

iOS的配置工作相对简单，整个配置过程完全是应用与Bugly SDK的关联工作，而这些关联工作仅需要通过Dart层调用setUp接口，访问原生代码宿主所封装的Bugly API就可以完成，因此无需额外操作。

而Android的配置工作则相对繁琐些。由于涉及NDK和Android P网络安全的适配，我们还需要分别在build.gradle和AndroidManifest.xml文件进行相应的配置工作。

**首先**，由于Bugly SDK需要支持NDK，因此我们需要在App的build.gradle文件中为其增加NDK的架构支持：

```
defaultConfig {
    ndk {
        // 设置支持的SO库架构
        abiFilters 'armeabi' , 'x86', 'armeabi-v7a', 'x86_64', 'arm64-v8a'
    }
}
```

**然后**，由于Android P默认限制http明文传输数据，因此我们需要为Bugly声明一项网络安全配置network_security_config.xml，允许其使用http传输数据，并在AndroidManifest.xml中新增同名网络安全配置：

```
//res/xml/network_security_config.xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 网络安全配置 -->
<network-security-config>
    <!-- 允许明文传输数据 -->
    <domain-config cleartextTrafficPermitted="true">
        <!-- 将Bugly的域名加入白名单 -->
        <domain includeSubdomains="true">android.bugly.qq.com</domain>
    </domain-config>
</network-security-config>

//AndroidManifest/xml
<application
  ...
  android:networkSecurityConfig="@xml/network_security_config"
  ...>
</application>
```

至此，Flutter工程所需的原生配置工作和接口实现，就全部搞定了。

接下来，我们就可以在Flutter工程中的main.dart文件中，**使用FlutterCrashPlugin插件来实现异常数据上报能力了**。当然，我们**首先**还需要在pubspec.yaml文件中，将工程对它的依赖显示地声明出来：

```
dependencies:
  flutter_push_plugin:
    git:
      url: https://github.com/cyndibaby905/39_flutter_crash_plugin
```

在下面的代码中，我们在main函数里为应用的异常提供了统一的回调，并在回调函数内使用postException方法将异常上报至Bugly。

而在SDK的初始化方法里，由于Bugly视iOS和Android为两个独立的应用，因此我们判断了代码的运行宿主，分别使用两个不同的App ID对其进行了初始化工作。

此外，为了与你演示具体的异常拦截功能，我们还在两个按钮的点击事件处理中分别抛出了同步和异步两类异常：

```
//上报数据至Bugly
Future<Null> _reportError(dynamic error, dynamic stackTrace) async {
  FlutterCrashPlugin.postException(error, stackTrace);
}

Future<Null> main() async {
  //注册Flutter框架的异常回调
  FlutterError.onError = (FlutterErrorDetails details) async {
    //转发至Zone的错误回调
    Zone.current.handleUncaughtError(details.exception, details.stack);
  };
  //自定义错误提示页面
  ErrorWidget.builder = (FlutterErrorDetails flutterErrorDetails){
    return Scaffold(
      body: Center(
        child: Text("Custom Error Widget"),
      )
    );
  };
  //使用runZone方法将runApp的运行放置在Zone中，并提供统一的异常回调
  runZoned<Future<Null>>(() async {
    runApp(MyApp());
  }, onError: (error, stackTrace) async {
    await _reportError(error, stackTrace);
  });
}

class MyApp extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    //由于Bugly视iOS和Android为两个独立的应用，因此需要使用不同的App ID进行初始化
    if(Platform.isAndroid){
      FlutterCrashPlugin.setUp('43eed8b173');
    }else if(Platform.isIOS){
      FlutterCrashPlugin.setUp('088aebe0d5');
    }
    super.initState();
  }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Crashy'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            RaisedButton(
              child: Text('Dart exception'),
              onPressed: () {
                //触发同步异常
                throw StateError('This is a Dart exception.');
              },
            ),
            RaisedButton(
              child: Text('async Dart exception'),
              onPressed: () {
                //触发异步异常
                Future.delayed(Duration(seconds: 1))
                      .then((e) => throw StateError('This is a Dart exception in Future.'));
              },
            )
          ],
        ),
      ),
    );
  }
}
```

运行这段代码，分别点击Dart exception按钮和async Dart exception按钮几次，可以看到我们的应用以及控制台并没有提示任何异常信息。

![085571920aea4083a24f200d55f1ee05](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/085571920aea4083a24f200d55f1ee05.jpg)

图5 异常拦截演示示例（iOS）

![409e8d1bc6034aed9167a85d9d2072d5](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/409e8d1bc6034aed9167a85d9d2072d5.jpg)

图6 异常拦截演示示例（Android）

**然后**，我们打开[Bugly开发者后台](https://bugly.qq.com/v2/workbench/apps)，选择对应的App，切换到错误分析选项查看对应的面板信息。可以看到，Bugly已经成功接收到上报的异常上下文了。

![cfe6b39603814783997ff278f6e4806e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/cfe6b39603814783997ff278f6e4806e.jpg)

图7 Bugly iOS错误分析上报数据查看

![65c58cceaf564932a6caaa1957162d58](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/65c58cceaf564932a6caaa1957162d58.jpg)

图8 Bugly Android错误分析上报数据查看

#### 总结

好了，今天的分享就到这里，我们来小结下吧。

对于Flutter应用的异常捕获，可以分为单个异常捕获和多异常统一拦截两种情况。

其中，单异常捕获，使用Dart提供的同步异常try-catch，以及异步异常catchError机制即可实现。而对多个异常的统一拦截，可以细分为如下两种情况：一是App异常，我们可以将代码执行块放置到Zone中，通过onError回调进行统一处理；二是Framework异常，我们可以使用FlutterError.onError回调进行拦截。

在捕获到异常之后，我们需要上报异常信息，用于后续分析定位问题。考虑到Bugly的社区活跃度比较高，所以我以Bugly为例，与你讲述了以原生插件封装的形式，如何进行异常信息上报。

需要注意的是，Flutter提供的异常拦截只能拦截Dart层的异常，而无法拦截Engine层的异常。这是因为，Engine层的实现大部分是C++的代码，一旦出现异常，整个程序就直接Crash掉了。不过通常来说，这类异常出现的概率极低，一般都是Flutter底层的Bug，与我们在应用层的实现没太大关系，所以我们也无需过度担心。

如果我们想要追踪Engine层的异常（比如，给Flutter提Issue），则需要借助于原生系统提供的Crash监听机制。这，就是一个很繁琐的工作了。

幸运的是，我们使用的数据上报SDK Bugly就提供了这样的能力，可以自动收集原生代码的Crash。而在Bugly收集到对应的Crash之后，我们需要做的事情就是，将Flutter Engine层对应的符号表下载下来，使用Android提供的ndk-stack、iOS提供的symbolicatecrash或atos命令，对相应Crash堆栈进行解析，从而得出Engine层崩溃的具体代码。

关于这些步骤的详细说明，你可以参考Flutter[官方文档](https://github.com/flutter/flutter/wiki/Crashes)。

我把今天分享涉及的知识点打包到了[GitHub](https://github.com/cyndibaby905/39_crashy_demo)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留下两道思考题吧。

第一个问题，请扩展_reportError和自定义错误提示页面的实现，在Debug环境下将异常数据打印至控制台，并保留原有系统错误提示页面实现。

```
//上报数据至Bugly
Future<Null> _reportError(dynamic error, dynamic stackTrace) async {
  FlutterCrashPlugin.postException(error, stackTrace);
}

//自定义错误提示页面
ErrorWidget.builder = (FlutterErrorDetails flutterErrorDetails){
  return Scaffold(
    body: Center(
      child: Text("Custom Error Widget"),
    )
  );
};
```

第二个问题，并发Isolate的异常可以通过今天分享中介绍的捕获机制去拦截吗？如果不行，应该怎么做呢？

```
//并发Isolate
doSth(msg) => throw ConcurrentModificationError('This is a Dart exception.');

//主Isolate
Isolate.spawn(doSth, "Hi");
```

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 衡量Flutter App线上质量，我们需要关注这三个指标

你好，我是陈航。

在上一篇文章中，我与你分享了如何捕获Flutter应用的未处理异常。所谓异常，指的是Dart代码在运行时意外发生的错误事件。对于单一异常来说，我们可以使用try-catch，或是catchError去处理；而如果我们想对异常进行集中的拦截治理，则需要使用Zone，并结合FlutterError进行统一管理。异常一旦被抓取，我们就可以利用第三方数据上报服务（比如Bugly），上报其上下文信息了。

这些线上异常的监控数据，对于开发者尽早发现线上隐患，确定问题根因至关重要。如果我们想进一步评估应用整体的稳定性的话，就需要把异常信息与页面的渲染关联起来。比如，页面渲染过程是否出现了异常，而导致功能不可用？

而对于以“丝般顺滑”著称的Flutter应用而言，页面渲染的性能同样需要我们重点关注。比如，界面渲染是否出现会掉帧卡顿现象，或者页面加载是否会出现性能问题导致耗时过长？这些问题，虽不至于让应用完全不能使用，但也很容易引起用户对应用质量的质疑，甚至是反感。

通过上面的分析，可以看到，衡量线上Flutter应用整体质量的指标，可以分为以下3类：

- 页面异常率；
- 页面帧率；
- 页面加载时长。

其中，页面异常率反应了页面的健康程度，页面帧率反应了视觉效果的顺滑程度，而页面加载时长则反应了整个渲染过程中点对点的延时情况。

这三项数据指标，是度量Flutter应用是否优秀的重要质量指标。通过梳理这些指标的统计口径，建立起Flutter应用的质量监控能力，这样一来我们不仅可以及早发现线上隐患，还可以确定质量基线，从而持续提升用户体验。

所以在今天的分享中，我会与你详细讲述这3项指标是如何采集的。

#### 页面异常率

页面异常率指的是，页面渲染过程中出现异常的概率。它度量的是页面维度下功能不可用的情况，其统计公式为：**页面异常率=异常发生次数/整体页面PV数**。

在了解了页面异常率的统计口径之后，接下来我们分别来看一下这个公式中的分子与分母应该如何统计吧。

我们先来看看**异常发生次数的统计方法**。通过上一篇文章，我们已经知道了在Flutter中，未处理异常需要通过Zone与FlutterError去捕获。所以，如果我们想统计异常发生次数的话，依旧是利用这两个方法，只不过要在异常拦截的方法中，通过一个计数器进行累加，统一记录。

下面的例子演示了异常发生次数的具体统计方法。我们使用全局变量exceptionCount，在异常捕获的回调方法_reportError中持续地累加捕获到的异常次数：

```
int exceptionCount = 0;
Future<Null> _reportError(dynamic error, dynamic stackTrace) async {
  exceptionCount++; //累加异常次数
  FlutterCrashPlugin.postException(error, stackTrace);
}

Future<Null> main() async {
  FlutterError.onError = (FlutterErrorDetails details) async {
    //将异常转发至Zone
    Zone.current.handleUncaughtError(details.exception, details.stack);
  };

  runZoned<Future<Null>>(() async {
    runApp(MyApp());
  }, onError: (error, stackTrace) async {
    //拦截异常
    await _reportError(error, stackTrace);
  });
}
```

接下来，我们再看看**整体页面PV数如何统计**吧。整体页面PV数，其实就是页面的打开次数。通过第21篇文章“[路由与导航，Flutter是这样实现页面切换的](https://time.geekbang.org/column/article/118421)”，我们已经知道了Flutter页面的切换需要经过Navigator来实现，所以页面切换状态也需要通过Navigator才能感知到。

与注册页面路由类似的，在MaterialApp中，我们可以通过NavigatorObservers属性，去监听页面的打开与关闭。下面的例子演示了**NavigatorObserver的具体用法**。在下面的代码中，我们定义了一个继承自NavigatorObserver的观察者，并在其didPush方法中，去统计页面的打开行为：

```
int totalPV = 0;
//导航监听器
class MyObserver extends NavigatorObserver{
  @override
  void didPush(Route route, Route previousRoute) {
    super.didPush(route, previousRoute);
    totalPV++;//累加PV
  }
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return  MaterialApp(
    //设置路由监听
       navigatorObservers: [
         MyObserver(),
       ],
       home: HomePage(),
    );
  }
}
```

现在，我们已经收集到了异常发生次数和整体页面PV数这两个参数，接下来我们就可以计算出页面异常率了：

```
double pageException() {
  if(totalPV == 0) return 0;
  return exceptionCount/totalPV;
}
```

可以看到，页面异常率的计算还是相对比较简单的。

#### 页面帧率

页面帧率，即FPS，是图像领域中的定义，指的是画面每秒传输帧数。由于人眼的视觉暂留特质，当所见到的画面传输帧数高于一定数量的时候，就会认为是连贯性的视觉效果。因此，对于动态页面而言，每秒钟展示的帧数越多，画面就越流畅。

由此我们可以得出，**FPS的计算口径为单位时间内渲染的帧总数**。在移动设备中，FPS的推荐数值通常是60Hz，即每秒刷新页面60次。

为什么是60Hz，而不是更高或更低的值呢？这是因为显示过程，是由VSync信号周期性驱动的，而VSync信号的周期就是每秒60次，这也是FPS的上限。

CPU与GPU在接收到VSync信号后，就会计算图形图像，准备渲染内容，并将其提交到帧缓冲区，等待下一次VSync信号到来时显示到屏幕上。如果在一个VSync时间内，CPU或者GPU没有完成内容提交，这一帧就会被丢弃，等待下一次机会再显示，而这时页面会保留之前的内容不变，造成界面卡顿。因此，FPS低于60Hz时就会出现掉帧现象，而如果低于45Hz则会有比较严重的卡顿现象。

为方便开发者统计FPS，Flutter在全局window对象上提供了帧回调机制。我们可以**在window对象上注册onReportTimings方法**，将最近绘制帧耗费的时间（即FrameTiming），以回调的形式告诉我们。有了每一帧的绘制时间后，我们就可以计算FPS了。

需要注意的是，onReportTimings方法只有在有帧被绘制时才有数据回调，如果用户没有和App发生交互，界面状态没有变化时，是不会产生新的帧的。考虑到单个帧的绘制时间差异较大，逐帧计算可能会产生数据跳跃，所以为了让FPS的计算更加平滑，我们需要保留最近25个FrameTiming用于求和计算。

而另一方面，对于FPS的计算，我们并不能孤立地只考虑帧绘制时间，而应该结合VSync信号的周期，即1/60秒（即16.67毫秒）来综合评估。

由于帧的渲染是依靠VSync信号驱动的，如果帧绘制的时间没有超过16.67毫秒，我们也需要把它当成16.67毫秒来算，因为绘制完成的帧必须要等到下一次VSync信号来了之后才能渲染。而如果帧绘制时间超过了16.67毫秒，则会占用后续的VSync信号周期，从而打乱后续的绘制次序，产生卡顿现象。这里有两种情况：

- 如果帧绘制时间正好是16.67的整数倍，比如50，则代表它花费了3个VSync信号周期，即本来可以绘制3帧，但实际上只绘制了1帧；
- 如果帧绘制时间不是16.67的整数倍，比如51，那么它花费的VSync信号周期应该向上取整，即4个，这意味着本来可以绘制4帧，实际上只绘制了1帧。

所以我们的FPS计算公式最终确定为：**FPS=60*实际渲染的帧数/本来应该在这个时间内渲染完成的帧数**。

下面的示例演示了如何通过onReportTimings回调函数实现FPS的计算。在下面的代码中，我们定义了一个容量为25的列表，用于存储最近的帧绘制耗时FrameTiming。在FPS的计算函数中，我们将列表中每帧绘制时间与VSync周期frameInterval进行比较，得出本来应该绘制的帧数，最后两者相除就得到了FPS指标。

需要注意的是，Android Studio提供的Flutter插件里展示的FPS信息，其实也来自于onReportTimings回调，所以我们在注册回调时需要保留原始回调引用，否则插件就读不到FPS信息了。

```
import 'dart:ui';

var orginalCallback;

void main() {
  runApp(MyApp());
  //设置帧回调函数并保存原始帧回调函数
  orginalCallback = window.onReportTimings;
  window.onReportTimings = onReportTimings;
}

//仅缓存最近25帧绘制耗时
const maxframes = 25;
final lastFrames = List<FrameTiming>();
//基准VSync信号周期
const frameInterval = const Duration(microseconds: Duration.microsecondsPerSecond ~/ 60);

void onReportTimings(List<FrameTiming> timings) {
  lastFrames.addAll(timings);
  //仅保留25帧
  if(lastFrames.length > maxframes) {
    lastFrames.removeRange(0, lastFrames.length - maxframes);
  }
  //如果有原始帧回调函数，则执行
  if (orginalCallback != null) {
    orginalCallback(timings);
  }
}

double get fps {
  int sum = 0;
  for (FrameTiming timing in lastFrames) {
    //计算渲染耗时
    int duration = timing.timestampInMicroseconds(FramePhase.rasterFinish) - timing.timestampInMicroseconds(FramePhase.buildStart);
    //判断耗时是否在Vsync信号周期内
    if(duration < frameInterval.inMicroseconds) {
      sum += 1;
    } else {
      //有丢帧，向上取整
      int count = (duration/frameInterval.inMicroseconds).ceil();
      sum += count;
    }
  }
  return lastFrames.length/sum * 60;
}
```

运行这段代码，可以看到，我们统计的FPS指标和Flutter插件展示的FPS走势是一致的。

![10ca7dd6b08849fb8924d55ef79c5664](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/10ca7dd6b08849fb8924d55ef79c5664.jpg)

图1 FPS指标走势

#### 页面加载时长

页面加载时长，指的是页面从创建到可见的时间。它反应的是代码中创建页面视图是否存在过度绘制，或者绘制不合理导致创建视图时间过长的情况。

从定义可以看出，**页面加载时长的统计口径为页面可见的时间-页面创建的时间**。获取页面创建的时间比较容易，我们只需要在页面的初始化函数里记录时间即可。那么，**页面可见的时间应该如何统计**呢？

在第11篇文章“[提到生命周期，我们是在说什么？](https://time.geekbang.org/column/article/109490)”中，我在介绍Widget的生命周期时，曾向你介绍过Flutter的帧回调机制。WidgetsBinding提供了单次Frame回调addPostFrameCallback方法，它会在当前Frame绘制完成之后进行回调，并且只会回调一次。一旦监听到Frame绘制完成回调后，我们就可以确认页面已经被渲染出来了，因此我们可以借助这个方法去获取页面可见的时间。

下面的例子演示了如何通过帧回调机制获取页面加载时长。在下面的代码中，我们在页面MyPage的初始化方法中记录了页面的创建时间startTime，然后在页面状态的初始化方法中，通过addPostFrameCallback注册了单次帧绘制回调，并在回调函数中记录了页面的渲染完成时间endTime。将这两个时间做减法，我们就得到了MyPage的页面加载时长：

```
class MyHomePage extends StatefulWidget {
  int startTime;
  int endTime;
  MyHomePage({Key key}) : super(key: key) {
    //页面初始化时记录启动时间
    startTime = DateTime.now().millisecondsSinceEpoch;
  }
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  void initState() {
    super.initState();
    //通过帧绘制回调获取渲染完成时间
    WidgetsBinding.instance.addPostFrameCallback((_) {
      widget.endTime = DateTime.now().millisecondsSinceEpoch;
      int timeSpend = widget.endTime - widget.startTime;
      print("Page render time:${timeSpend} ms");
    });
  }
  ...
}
```

试着运行一下代码，观察命令行输出：

```
flutter: Page render time:548 ms
```

可以看到，通过单次帧绘制回调统计得出的页面加载时间为548毫秒。

至此，我们就已经得到了页面异常率、页面帧率和页面加载时长这3个指标了。

#### 总结

好了，今天的分享就到这里，我们来总结下主要内容吧。

今天我们一起学习了衡量Flutter应用线上质量的3个指标，即页面异常率、页面帧率和页面加载时长，以及分别对应的数据采集方式。

其中，页面异常率表示页面渲染过程中的稳定性，可以通过集中捕获未处理异常，结合NavigatorObservers观察页面PV，计算得出页面维度下功能不可用的概率。

页面帧率则表示了页面的流畅情况，可以利用Flutter提供的帧绘制耗时回调onReportTimings，以加权的形式计算出本应该绘制的帧数，得到更为准确的FPS。

而页面加载时长，反应的是渲染过程的延时情况。我们可以借助于单次帧回调机制，来获取页面渲染完成时间，从而得到整体页面的加载时长。

通过这3个数据指标统计方法，我们再去评估Flutter应用的性能时，就有一个具体的数字化标准了。而有了数据之后，我们不仅可以及早发现问题隐患，准确定位及修复问题，还可以根据它们去评估应用的健康程度和页面的渲染性能，从而确定后续的优化方向。

我把今天分享涉及的知识点打包到了[GitHub](https://github.com/cyndibaby905/40_peformance_demo)中，你可以下载下来，反复运行几次，加深理解与记忆。

#### 思考题

最后，我给你留一道思考题吧。

如果页面的渲染需要依赖单个或多个网络接口数据，这时的页面加载时长应该如何统计呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 组件化和平台化，该如何组织合理稳定的Flutter工程结构？

你好，我是陈航。今天，我们来聊一聊Flutter应用的工程架构这个话题。

在软件开发中，我们不仅要在代码实现中遵守常见的设计模式，更需要在架构设计中遵从基本的设计原则。而在这其中，DRY（即Don’t Repeat Yourself）原则可以算是最重要的一个。

通俗来讲，DRY原则就是“不要重复”。这是一个很朴素的概念，因为即使是最初级的开发者，在写了一段时间代码后，也会不自觉地把一些常用的重复代码抽取出来，放到公用的函数、类或是独立的组件库中，从而实现代码复用。

在软件开发中，我们通常从架构设计中就要考虑如何去管理重复性（即代码复用），即如何将功能进行分治，将大问题分解为多个较为独立的小问题。而在这其中，组件化和平台化就是客户端开发中最流行的分治手段。

所以今天，我们就一起来学习一下这两类分治复用方案的中心思想，这样我们在设计Flutter应用的架构时也就能做到有章可循了。

#### 组件化

组件化又叫模块化，即基于可重用的目的，将一个大型软件系统（App）按照关注点分离的方式，拆分成多个独立的组件或模块。每个独立的组件都是一个单独的系统，可以单独维护、升级甚至直接替换，也可以依赖于别的独立组件，只要组件提供的功能不发生变化，就不会影响其他组件和软件系统的整体功能。

![0ee6844dcc8e4b2e836c24f3212842d5](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0ee6844dcc8e4b2e836c24f3212842d5.jpg)

图1 组件化示意图

可以看到，组件化的中心思想是将独立的功能进行拆分，而在拆分粒度上，组件化的约束则较为松散。一个独立的组件可以是一个软件包（Package）、页面、UI控件，甚至可能是封装了一些函数的模块。

**组件的粒度可大可小，那我们如何才能做好组件的封装重用呢？哪些代码应该被放到一个组件中？**这里有一些基本原则，包括单一性原则、抽象化原则、稳定性原则和自完备性原则。

接下来，我们先看看这些原则具体是什么意思。

**单一性原则指的是**，每个组件仅提供一个功能。分而治之是组件化的中心思想，每个组件都有自己固定的职责和清晰的边界，专注地做一件事儿，这样这个组件才能良性发展。

一个反例是Common或Util组件，这类组件往往是因为在开发中出现了定义不明确、归属边界不清晰的代码：“哎呀，这段代码放哪儿好像都不合适，那就放Common（Util）吧”。久而久之，这类组件就变成了无人问津的垃圾堆。所以，再遇到不知道该放哪儿的代码时，就需要重新思考组件的设计和职责了。

**抽象化原则**指的是，组件提供的功能抽象应该尽量稳定，具有高复用度。而稳定的直观表现就是对外暴露的接口很少发生变化，要做到这一点，需要我们提升对功能的抽象总结能力，在组件封装时做好功能抽象和接口设计，将所有可能发生变化的因子都在组件内部做好适配，不要暴露给它的调用方。

**稳定性原则**指的是，不要让稳定的组件依赖不稳定的组件。比如组件1依赖了组件5，如果组件1很稳定，但是组件5经常变化，那么组件1也就会变得不稳定了，需要经常适配。如果组件5里确实有组件1不可或缺的代码，我们可以考虑把这段代码拆出来单独做成一个新的组件X，或是直接在组件1中拷贝一份依赖的代码。

**自完备性**，即组件需要尽可能地做到自给自足，尽量减少对其他底层组件的依赖，达到代码可复用的目的。比如，组件1只是依赖某个大组件5中的某个方法，这时更好的处理方法是，剥离掉组件1对组件5的依赖，直接把这个方法拷贝到组件1中。这样一来组件1就能够更好地应对后续的外部变更了。

在理解了组件化的基本原则之后，**我们再来看看组件化的具体实施步骤**，即剥离基础功能、抽象业务模块和最小化服务能力。

首先，我们需要剥离应用中与业务无关的基础功能，比如网络请求、组件中间件、第三方库封装、UI组件等，将它们封装为独立的基础库；然后，我们在项目里用pub进行管理。如果是第三方库，考虑到后续的维护适配成本，我们最好再封装一层，使项目不直接依赖外部代码，方便后续更新或替换。

基础功能已经封装成了定义更清晰的组件，接下来我们就可以按照业务维度，比如首页、详情页、搜索页等，去拆分独立的模块了。拆分的粒度可以先粗后细，只要能将大体划分清晰的业务组件进行拆分，后续就可以通过分布迭代、局部微调，最终实现整个业务项目的组件化。

在业务组件和基础组件都完成拆分封装后，应用的组件化架构就基本成型了，最后就可以按照刚才我们说的4个原则，去修正各个组件向下的依赖，以及最小化对外暴露的能力了。

#### 平台化

从组件的定义可以看到，组件是个松散的广义概念，其规模取决于我们封装的功能维度大小，而各个组件之间的关系也仅靠依赖去维持。如果组件之间的依赖关系比较复杂，就会在一定程度上造成功能耦合现象。

如下所示的组件示意图中，组件2和组件3同时被多个业务组件和基础功能组件直接引用，甚至组件2和组件5、组件3和组件4之间还存在着循环依赖的情况。一旦这些组件的内部实现和外部接口发生变化，整个App就会陷入不稳定的状态，即所谓牵一发而动全身。

![a02bb13b4d2f4766a68c54898128b091](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a02bb13b4d2f4766a68c54898128b091.jpg)

图2 循环依赖现象

平台化是组件化的升级，即在组件化的基础上，对它们提供的功能进行分类，统一分层划分，增加依赖治理的概念。为了对这些功能单元在概念上进行更为统一的分类，我们按照四象限分析法，把应用程序的组件按照业务和UI分解为4个维度，来分析组件可以分为哪几类。

![450d77e043ce4a65bac23b39db1fde74](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/450d77e043ce4a65bac23b39db1fde74.jpg)

图3 组件划分原则

可以看出，经过业务与UI的分解之后，这些组件可以分为4类：

1. 具备UI属性的独立业务模块；
2. 不具备UI属性的基础业务功能；
3. 不具备业务属性的UI控件
4. 不具备业务属性的基础功能

按照自身定义，这4类组件其实隐含着分层依赖的关系。比如，处于业务模块中的首页，依赖位于基础业务模块中的账号功能；再比如，位于UI控件模块中的轮播卡片，依赖位于基础功能模块中的存储管理等功能。我们将它们按照依赖的先后顺序从上到下进行划分，就是一个完整的App了。

![d31275debfa445519d2f45ecf557922e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d31275debfa445519d2f45ecf557922e.jpg)

图4 组件化分层

可以看到，平台化与组件化最大的差异在于增加了分层的概念，每一层的功能均基于同层和下层的功能之上，这使得各个组件之间既保持了独立性，同时也具有一定的弹性，在不越界的情况下按照功能划分各司其职。

**与组件化更关注组件的独立性相比，平台化更关注的是组件之间关系的合理性，而这也是在设计平台化架构时需要重点考虑的单向依赖原则。**

所谓单向依赖原则，指的是组件依赖的顺序应该按照应用架构的层数从上到下依赖，不要出现下层模块依赖上层模块这样循环依赖的现象。这样可以最大限度地避免复杂的耦合，减少组件化时的困难。如果我们每个组件都只是单向依赖其他组件，各个组件之间的关系都是清晰的，代码解耦也就会变得非常轻松了。

平台化强调依赖的顺序性，除了不允许出现下层组件依赖上层组件的情况，跨层组件和同层组件之间的依赖关系也应当严格控制，因为这样的依赖关系往往会带来架构设计上的混乱。

**如果下层组件确实需要调用上层组件的代码怎么办？**

这时，我们可以采用增加中间层的方式，比如Event Bus、Provider或Router，以中间层转发的形式实现信息同步。比如，位于第4层的网络引擎中，会针对特定的错误码跳转到位于第1层的统一错误页，这时我们就可以利用Router提供的命名路由跳转，在不感知错误页的实现情况下来完成。又比如，位于第2层的账号组件中，会在用户登入登出时主动刷新位于第1层的首页和我的页面，这时我们就可以利用Event Bus来触发账号切换事件，在不需要获取页面实例的情况下通知它们更新界面。关于这部分内容，你可以参考第[20](https://time.geekbang.org/column/article/116382)和[21](https://time.geekbang.org/column/article/118421)篇文章中的相关内容，这里就不再赘述了。

**平台化架构是目前应用最广的软件架构设计，其核心在于如何将离散的组件依照单向依赖的原则进行分层。**而关于具体的分层逻辑，除了我们上面介绍的业务和UI四象限法则之外，你也可以使用其他的划分策略，只要整体结构层次清晰明确，不存在难以确定归属的组件就可以了。

比如，Flutter就采用Embedder（操作系统适配层）、Engine（渲染引擎及Dart VM层）和Framework（UI SDK层）整体三层的划分。可以看到，Flutter框架每一层的组件定义都有着明确的边界，其向上提供的功能和向下依赖的能力也非常明确。

![0f755b4fad6644c9beaa179c4f0ed94b](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0f755b4fad6644c9beaa179c4f0ed94b.jpg)

图5 Flutter框架架构

备注：此图引自[Flutter System Overview](https://flutter.dev/docs/resources/technical-overview)

#### 总结

好了，今天的分享就到这里，我们总结一下主要内容吧。

组件化和平台化都是软件开发中流行的分治手段，能够将App内的功能拆分成多个独立的组件或模块。

其中，组件化更关注如何保持组件的独立性，只要拆分的功能独立即可，约束较为松散，在中大型App中容易造成一定程度的功能耦合现象。而平台化则更强调组件之间关系的合理性，增加了分层的概念，使得组件之间既有边界，也有一定的弹性。只要满足单向依赖原则，各个组件之间的关系都是清晰的。

分治是一种与技术无关的架构思想，有利于降低工程的复杂性，从而提高App的可扩展和可维护性。今天这篇文章，我重点与你分享的是组件化与平台化这两种架构设计的思路，并没有讲解它们的具体实现。而关于组件化与平台化的实现细节，网络上已经有很多文章了，你可以在网上自行搜索了解。如果你还有关于组件化和平台化的其他问题，那就在评论区中给我留言吧。

其实，你也可以琢磨出，今天这篇文章的目的是带你领会App架构设计的核心思想。因为，理解思想之后剩下的就是去实践了，当你需要设计App架构时再回忆起这些内容，或是翻出这篇文章一定会事半功倍。

#### 思考题

最后，我给你留一道思考题吧。

在App架构设计中，你会采用何种方式去管理涉及资源类的依赖呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何构建高效的Flutter App打包发布环境？

你好，我是陈航。今天，我们来聊一聊Flutter应用的交付这个话题。

软件项目的交付是一个复杂的过程，任何原因都有可能导致交付过程失败。中小型研发团队经常遇到的一个现象是，App在开发测试时没有任何异常，但一到最后的打包构建交付时就问题频出。所以，每到新版本发布时，大家不仅要等候打包结果，还经常需要加班修复临时出现的问题。如果没有很好地线上应急策略，即使打包成功，交付完成后还是非常紧张。

可以看到，产品交付不仅是一个令工程师头疼的过程，还是一个高风险动作。其实，失败并不可怕，可怕的是每次失败的原因都不一样。所以，为了保障可靠交付，我们需要关注从源代码到发布的整个流程，提供一种可靠的发布支撑，确保App是以一种可重复的、自动化的方式构建出来的。同时，我们还应该将打包过程提前，将构建频率加快，因为这样不仅可以尽早发现问题，修复成本也会更低，并且能更好地保证代码变更能够顺利发布上线。

其实，这正是持续交付的思路。

所谓持续交付，指的是建立一套自动监测源代码变更，并自动实施构建、测试、打包和相关操作的流程链机制，以保证软件可以持续、稳定地保持在随时可以发布的状态。 持续交付可以让软件的构建、测试与发布变得更快、更频繁，更早地暴露问题和风险，降低软件开发的成本。

你可能会觉得，大型软件工程里才会用到持续交付。其实不然，通过运用一些免费的工具和平台，中小型项目也能够享受到开发任务自动化的便利。而Travis CI就是这类工具之中，市场份额最大的一个。所以接下来，我就以Travis CI为例，与你分享如何为Flutter工程引入持续交付的能力。

#### Travis CI

Travis CI 是在线托管的持续交付服务，用Travis来进行持续交付，不需要自己搭服务器，在网页上点几下就好，非常方便。

Travis和GitHub是一对配合默契的工作伙伴，只要你在Travis上绑定了GitHub上的项目，后续任何代码的变更都会被Travis自动抓取。然后，Travis会提供一个运行环境，执行我们预先在配置文件中定义好的测试和构建步骤，并最终把这次变更产生的构建产物归档到GitHub Release上，如下所示：

![6121850fd6f941f0a806fa8e6d7412cd](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/6121850fd6f941f0a806fa8e6d7412cd.jpg)

图1 Travis CI持续交付流程示意图

可以看到，通过Travis提供的持续构建交付能力，我们可以直接看到每次代码的更新的变更结果，而不需要累积到发布前再做打包构建。这样不仅可以更早地发现错误，定位问题也会更容易。

要想为项目提供持续交付的能力，我们首先需要在Travis上绑定GitHub。我们打开[Travis官网](https://travis-ci.com/)，使用自己的GitHub账号授权登陆就可以了。登录完成后页面中会出现一个“Activate”按钮，点击按钮会跳回到GitHub中进行项目访问权限设置。我们保留默认的设置，点击“Approve&Install”即可。

![ab512d5548684590836667db9dd01fc9](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ab512d5548684590836667db9dd01fc9.jpg)

图2 激活Github集成

![8c15f8e2cc0247f8b63bcd652747390f](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/8c15f8e2cc0247f8b63bcd652747390f.jpg)

图3 授权Travis读取项目变更记录

完成授权之后，页面会跳转到Travis。Travis主页上会列出GitHub上你的所有仓库，以及你所属于的组织，如下图所示：

![5556abfbd1a24e0a9d377df27b45e13a](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/5556abfbd1a24e0a9d377df27b45e13a.jpg)

图4 完成Github项目绑定

完成项目绑定后，接下来就是**为项目增加Travis配置文件**了。配置的方法也很简单，只要在项目的根目录下放一个名为.travis.yml的文件就可以了。

.travis.yml是Travis的配置文件，指定了Travis应该如何应对代码变更。代码commit上去之后，一旦Travis检测到新的变更，Travis就会去查找这个文件，根据项目类型（language）确定执行环节，然后按照依赖安装（install）、构建命令（script）和发布（deploy）这三大步骤，依次执行里面的命令。一个Travis构建任务流程如下所示：

![7fb3dbc6f3ab4aaab19c58e6210d560d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/7fb3dbc6f3ab4aaab19c58e6210d560d.jpg)

图5 Travis工作流

可以看到，为了更精细地控制持续构建过程，Travis还为install、script和deploy提供了对应的钩子（before_install、before_script、after_failure、after_success、before_deploy、after_deploy、after_script），可以前置或后置地执行一些特殊操作。

如果你的项目比较简单，没有其他的第三方依赖，也不需要发布到GitHub Release上，只是想看看构建会不会失败，那么你可以省略配置文件中的install和deploy。

#### 如何为项目引入Travis？

可以看到，一个最简单的配置文件只需要提供两个字段，即language和script，就可以让Travis帮你自动构建了。下面的例子演示了如何为一个Dart命令行项目引入Travis。在下面的配置文件中，我们将language字段设置为Dart，并在script字段中，将dart_sample.dart定义为程序入口启动运行：

```
#.travis.yml
language: dart
script:
  - dart dart_sample.dart
```

将这个文件提交至项目中，我们就完成了Travis的配置工作。

Travis会在每次代码提交时自动运行配置文件中的命令，如果所有命令都返回0，就表示验证通过，完全没有问题，你的提交记录就会被标记上一个绿色的对勾。反之，如果命令运行过程中出现了异常，则表示验证失败，你的提交记录就会被标记上一个红色的叉，这时我们就要点击红勾进入Travis构建详情，去查看失败原因并尽快修复问题了。

![d8983c69b06d46b488db827b99dff202](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d8983c69b06d46b488db827b99dff202.jpg)

图6 代码变更验证

可以看到，为一个工程引入自动化任务的能力，只需要提炼出能够让工程自动化运行需要的命令就可以了。

在[第38篇文章](https://time.geekbang.org/column/article/140079)中，我与你介绍了Flutter工程运行自动化测试用例的命令，即flutter test，所以如果我们要为一个Flutter工程配置自动化测试任务，直接把这个命令放置在script字段就可以了。

但需要注意的是，Travis并没有内置Flutter运行环境，所以我们还需要在install字段中，为自动化任务安装Flutter SDK。下面的例子演示了**如何为一个Flutter工程配置自动化测试能力**。在下面的配置文件中，我们将os字段设置为osx，在install字段中clone了Flutter SDK，并将Flutter命令设置为环境变量。最后，我们在script字段中加上flutter test命令，就完成了配置工作：

```
os:
  - osx
install:
  - git clone https://github.com/flutter/flutter.git
  - export PATH="$PATH:`pwd`/flutter/bin"
script:
  - flutter doctor && flutter test
```

其实，为Flutter工程的代码变更引入自动化测试能力相对比较容易，但考虑到Flutter的跨平台特性，**要想在不同平台上验证工程自动化构建的能力（即iOS平台构建出ipa包、Android平台构建出apk包）又该如何处理呢**？

我们都知道Flutter打包构建的命令是flutter build，所以同样的，我们只需要把构建iOS的命令和构建Android的命令放到script字段里就可以了。但考虑到这两条构建命令执行时间相对较长，所以我们可以利用Travis提供的并发任务选项matrix，来把iOS和Android的构建拆开，分别部署在独立的机器上执行。

下面的例子演示了如何使用matrix分拆构建任务。在下面的代码中，我们定义了两个并发任务，即运行在Linux上的Android构建任务执行flutter build apk，和运行在OS X上的iOS构建任务flutter build ios。

考虑到不同平台的构建任务需要提前准备运行环境，比如Android构建任务需要设置JDK、安装Android SDK和构建工具、接受相应的开发者协议，而iOS构建任务则需要设置Xcode版本，因此我们分别在这两个并发任务中提供对应的配置选项。

最后需要注意的是，由于这两个任务都需要依赖Flutter环境，所以install字段并不需要拆到各自任务中进行重复设置：

```
matrix:
  include:
    #声明Android运行环境
    - os: linux
      language: android
      dist: trusty
      licenses:
        - 'android-sdk-preview-license-.+'
        - 'android-sdk-license-.+'
        - 'google-gdk-license-.+'
      #声明需要安装的Android组件
      android:
        components:
          - tools
          - platform-tools
          - build-tools-28.0.3
          - android-28
          - sys-img-armeabi-v7a-google_apis-28
          - extra-android-m2repository
          - extra-google-m2repository
          - extra-google-android-support
      jdk: oraclejdk8
      sudo: false
      addons:
        apt:
          sources:
            - ubuntu-toolchain-r-test
          packages:
            - libstdc++6
            - fonts-droid
      #确保sdkmanager是最新的
      before_script:
        - yes | sdkmanager --update
      script:
        - yes | flutter doctor --android-licenses
        - flutter doctor && flutter -v build apk

    #声明iOS的运行环境
    - os: osx
      language: objective-c
      osx_image: xcode10.2
      script:
        - flutter doctor && flutter -v build ios --no-codesign
install:
    - git clone https://github.com/flutter/flutter.git
    - export PATH="$PATH:`pwd`/flutter/bin"
```

#### 如何将打包好的二进制文件自动发布出来？

在这个案例中，我们构建任务的命令是打包，那打包好的二进制文件可以自动发布出来吗？

答案是肯定的。我们只需要为这两个构建任务增加deploy字段，设置skip_cleanup字段告诉Travis在构建完成后不要清除编译产物，然后通过file字段把要发布的文件指定出来，最后就可以通过GitHub提供的API token上传到项目主页了。

下面的示例演示了deploy字段的具体用法，在下面的代码中，我们获取到了script字段构建出的app-release.apk，并通过file字段将其指定为待发布的文件。考虑到并不是每次构建都需要自动发布，所以我们在下面的配置中，增加了on选项，告诉Travis仅在对应的代码更新有关联tag时，才自动发布一个release版本：

```
...
#声明构建需要执行的命令
script:
  - yes | flutter doctor --android-licenses
  - flutter doctor && flutter -v build apk
#声明部署的策略，即上传apk至github release
deploy:
  provider: releases
  api_key: xxxxx
  file:
    - build/app/outputs/apk/release/app-release.apk
  skip_cleanup: true
  on:
    tags: true
...
```

需要注意的是，由于我们的项目是开源库，因此GitHub的API token不能明文放到配置文件中，需要在Travis上配置一个API token的环境变量，然后把这个环境变量设置到配置文件中。

我们先打开GitHub，点击页面右上角的个人头像进入Settings，随后点击Developer Settings进入开发者设置。

![0b0578d31cc0456294941c5a1735f657](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0b0578d31cc0456294941c5a1735f657.jpg)

图7 进入开发者设置

在开发者设置页面中，我们点击左下角的Personal access tokens选项，生成访问token。token设置页面提供了比较丰富的访问权限控制，比如仓库限制、用户限制、读写限制等，这里我们选择只访问公共的仓库，填好token名称cd_demo，点击确认之后，GitHub会将token的内容展示在页面上。

![52627ed4f4cb4401bee94813572495bb](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/52627ed4f4cb4401bee94813572495bb.jpg)

图8 生成访问token

需要注意的是，这个token 你只会在GitHub上看到一次，页面关了就再也找不到了，所以我们先把这个token复制下来。

![7e393e303a244094917e82d559cf6dad](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/7e393e303a244094917e82d559cf6dad.jpg)

图9 访问token界面

接下来，我们打开Travis主页，找到我们希望配置自动发布的项目，然后点击右上角的More options选择Settings打开项目配置页面。

![e2f4c969431e4e2b835a1a005bf66473](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e2f4c969431e4e2b835a1a005bf66473.jpg)

图10 打开Travis项目设置

在Environment Variable里，把刚刚复制的token改名为GITHUB_TOKEN，加到环境变量即可。

![e317995a2daa4dd7adb390a0f8bb7a0d](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/e317995a2daa4dd7adb390a0f8bb7a0d.jpg)

图11 加入Travis环境变量

最后，我们只要把配置文件中的api_key替换成${GITHUB_TOKEN}就可以了。

```
...
deploy:
  api_key: ${GITHUB_TOKEN}
...
```

这个案例介绍的是Android的构建产物apk发布。而对于iOS而言，我们还需要对其构建产物app稍作加工，让其变成更通用的ipa格式之后才能发布。这里我们就需要用到deploy的钩子before_deploy字段了，这个字段能够在正式发布前，执行一些特定的产物加工工作。

下面的例子演示了**如何通过before_deploy字段加工构建产物**。由于ipa格式是在app格式之上做的一层包装，所以我们把app文件拷贝到Payload后再做压缩，就完成了发布前的准备工作，接下来就可以在deploy阶段指定要发布的文件，正式进入发布环节了：

```
...
#对发布前的构建产物进行预处理，打包成ipa
before_deploy:
  - mkdir app && mkdir app/Payload
  - cp -r build/ios/iphoneos/Runner.app app/Payload
  - pushd app && zip -r -m app.ipa Payload  && popd
#将ipa上传至github release
deploy:
  provider: releases
  api_key: ${GITHUB_TOKEN}
  file:
    - app/app.ipa
  skip_cleanup: true
  on:
    tags: true
...
```

将更新后的配置文件提交至GitHub，随后打一个tag。等待Travis构建完毕后可以看到，我们的工程已经具备自动发布构建产物的能力了。

![7e8d0004168c40f19129e53e3e7e0976](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/7e8d0004168c40f19129e53e3e7e0976.jpg)

图12 Flutter App发布构建产物

#### 如何为Flutter Module工程引入自动发布能力？

这个例子介绍的是传统的Flutter App工程（即纯Flutter工程），**如果我们想为Flutter Module工程（即混合开发的Flutter工程）引入自动发布能力又该如何设置呢？**

其实也并不复杂。Module工程的Android构建产物是aar，iOS构建产物是Framework。Android产物的自动发布比较简单，我们直接复用apk的发布，把file文件指定为aar文件即可；iOS的产物自动发布稍繁琐一些，需要将Framework做一些简单的加工，将它们转换成Pod格式。

下面的例子演示了Flutter Module的iOS产物是如何实现自动发布的。由于Pod格式本身只是在App.Framework和Flutter.Framework这两个文件的基础上做的封装，所以我们只需要把它们拷贝到统一的目录FlutterEngine下，并将声明了组件定义的FlutterEngine.podspec文件放置在最外层，最后统一压缩成zip格式即可。

```
...
#对构建产物进行预处理，压缩成zip格式的组件
before_deploy:
  - mkdir .ios/Outputs && mkdir .ios/Outputs/FlutterEngine
  - cp FlutterEngine.podspec .ios/Outputs/
  - cp -r .ios/Flutter/App.framework/ .ios/Outputs/FlutterEngine/App.framework/
  - cp -r .ios/Flutter/engine/Flutter.framework/ .ios/Outputs/FlutterEngine/Flutter.framework/
  - pushd .ios/Outputs && zip -r FlutterEngine.zip  ./ && popd
deploy:
  provider: releases
  api_key: ${GITHUB_TOKEN}
  file:
    - .ios/Outputs/FlutterEngine.zip
  skip_cleanup: true
  on:
    tags: true
...
```

将这段代码提交后可以看到，Flutter Module工程也可以自动的发布原生组件了。

![d7621a45216a446ba26cb0a2928a3ac5](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/d7621a45216a446ba26cb0a2928a3ac5.jpg)

图13 Flutter Module工程发布构建产物

通过这些例子我们可以看到，**任务配置的关键在于提炼出项目自动化运行需要的命令集合，并确认它们的执行顺序。**只要把这些命令集合按照install、script和deploy三个阶段安置好，接下来的事情就交给Travis去完成，我们安心享受持续交付带来的便利就可以了。

#### 总结

俗话说，“90%的故障都是由变更引起的”，这凸显了持续交付对于发布稳定性保障的价值。通过建立持续交付流程链机制，我们可以将代码变更与自动化手段关联起来，让测试和发布变得更快、更频繁，不仅可以提早暴露风险，还能让软件可以持续稳定地保持在随时可发布的状态。

在今天的分享中，我与你介绍了如何通过Travis CI，为我们的项目引入持续交付能力。Travis的自动化任务的工作流依靠.travis.yml配置文件驱动，我们可以在确认好构建任务需要的命令集合后，在这个配置文件中依照install、script和deploy这3个步骤拆解执行过程。完成项目的配置之后，一旦Travis检测到代码变更，就可以自动执行任务了。

简单清晰的发布流程是软件可靠性的前提。如果我们同时发布了100个代码变更，导致App性能恶化了，我们可能需要花费大量时间和精力，去定位究竟是哪些变更影响了App性能，以及它们是如何影响的。而如果以持续交付的方式发布App，我们能够以更小的粒度去测量和理解代码变更带来的影响，是改善还是退化，从而可以更早地找到问题，更有信心进行更快的发布。

**需要注意的是，**在今天的示例分析中，我们构建的是一个未签名的ipa文件，这意味着我们需要先完成签名之后，才能在真实的iOS设备上运行，或者发布到App Store。

iOS的代码签名涉及私钥和多重证书的校验，以及对应的加解密步骤，是一个相对繁琐的过程。如果我们希望在Travis上部署自动化签名操作，需要导出发布证书、私钥和描述文件，并提前将这些文件打包成一个压缩包后进行加密，上传至仓库。

然后，我们还需要在before_install时，将这个压缩包进行解密，并把证书导到Travis运行环境的钥匙串中，这样构建脚本就可以使用临时钥匙串对二进制文件进行签名了。完整的配置，你可以参考手机内侧服务厂商蒲公英提供的[集成文档](https://www.pgyer.com/doc/view/travis_ios)了解进一步的细节。

如果你不希望将发布证书、私钥暴露给Travis，也可以把未签名的ipa包下载下来，解压后通过codesign命令，分别对App.Framework、Flutter.Framework以及Runner进行重签名操作，然后重新压缩成ipa包即可。[这篇文章](https://www.yangshebing.com/2018/01/06/iOS%E9%80%86%E5%90%91%E5%BF%85%E5%A4%87%E7%BB%9D%E6%8A%80%E4%B9%8Bipa%E9%87%8D%E7%AD%BE%E5%90%8D/)介绍了详细的操作步骤，这里我们也不再赘述了。

我把今天分享涉及的Travis配置上传到了GitHub，你可以把这几个项目[Dart_Sample](https://github.com/cyndibaby905/08_Dart_Sample)、[Module_Page](https://github.com/cyndibaby905/28_module_page)、[Crashy_Demo](https://github.com/cyndibaby905/39_crashy_demo)下载下来，观察它们的配置文件，并在Travis网站上查看对应的构建过程，从而加深理解与记忆。

#### 思考题

最后，我给你留一道思考题吧。

在Travis配置文件中，如何选用特定的Flutter SDK版本（比如v1.5.4-hotfix.2）呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

## 混合开发框架

### 如何构建自己的Flutter混合开发框架（一）？

你好，我是陈航。在本次课程的最后一个主题里，我来和你聊聊如何设计自己的Flutter混合开发框架。

所谓混合开发，是指在App的整体架构继续使用原生技术栈的基础上，将Flutter运行环境嵌入到原生App工程中：由原生开发人员为Flutter运行提供宿主容器及基础能力支撑，而Flutter开发人员则负责应用层业务及App内大部分渲染工作。

这种开发模式的好处十分明显。对于工程师而言，跨平台的Flutter框架减少了对底层环境的依赖，使用完整的技术栈和工具链隔离了各个终端系统的差异，无论是Android、iOS甚至是前端工程师，都可以使用统一而标准化的能力进行业务开发，从而扩充了技能栈。而对于企业而言，这种方式不仅具备了原生App良好的用户体验，以及丰富的底层能力，还同时拥有了跨平台技术开发低成本和多端体验一致性的优势，直接节省研发资源。

那么，在原生工程中引入Flutter混合开发能力，我们应该如何设计工程架构，原生开发与Flutter开发的工作模式又是怎样的呢？

接下来，在今天的分享中，我会着重为你介绍这两个主题设计思路和建设方向；而在下一次分享中，我则会通过一个实际的案例，与你详细说明在业务落地中，我们需要重点考虑哪些技术细节，这样你在为自己的原生工程中设计混合开发框架时也就有迹可循了。

#### 混合开发架构

在[第41篇文章](https://time.geekbang.org/column/article/144121)中，我与你介绍了软件功能分治的两种手段，即组件化和平台化，以及如何在满足单向依赖原则的前提下，以分层的形式将软件功能进行分类聚合的方法。这些设计思想，能够让我们在设计软件系统架构时，降低整体工程的复杂性，提高App的可扩展性和可维护性。

与纯Flutter工程能够以自治的方式去分拆软件功能、管理工程依赖不同，**Flutter混合工程的功能分治**需要原生工程与Flutter工程一起配合完成，即：在Flutter模块的视角看来，一部分与渲染相关的基础能力完全由Flutter代码实现，而另一部分涉及操作系统底层、业务通用能力部分，以及整体应用架构支撑，则需要借助于原生工程给予支持。

在第41篇文章中，我们通过四象限分析法，把纯Flutter应用按照业务和UI分解成4类。同样的，混合工程的功能单元也可以按照这个分治逻辑分为4个维度，即不具备业务属性的原生基础功能、不具备业务属性的原生UI控件、不具备UI属性的原生基础业务功能和带UI属性的独立业务模块。

![3f02642552f04398ae5b2347ef83c5e6](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/3f02642552f04398ae5b2347ef83c5e6.jpg)

图1 四象限分析法

从图中可以看到，对于前3个维度（即原生UI控件、原生基础功能、原生基础业务功能）的定义，纯Flutter工程与混合工程并无区别，只不过实现方式由Flutter变成了原生；对于第四个维度（即独立业务模块）的功能归属，考虑到业务模块的最小单元是页面，而Flutter的最终呈现形式也是独立的页面，因此我们把Flutter模块也归为此类，我们的工程可以像依赖原生业务模块一样直接依赖它，为用户提供独立的业务功能。

我们把这些组件及其依赖按照从上到下的方式进行划分，就是一个完整的混合开发架构了。可以看到，原生工程和Flutter工程的边界定义清晰，双方都可以保持原有的分层管理依赖的开发模式不变。

![ef1746b2a85c4aee91f0e907356f83f0](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/ef1746b2a85c4aee91f0e907356f83f0.jpg)

图2 Flutter混合开发架构

需要注意的是，作为一个内嵌在原生工程的功能组件，Flutter模块的运行环境是由原生工程提供支持的，这也就意味着在渲染交互能力之外的部分基础功能（比如网络、存储），以及和原生业务共享的业务通用能力（比如支付、账号）需要原生工程配合完成，即原生工程以分层的形式提供上层调用接口，Flutter模块以插件的形式直接访问原生代码宿主对应功能实现。

因此，不仅不同归属定义的原生组件之前存在着分层依赖的关系，Flutter模块与原生组件之前也隐含着分层依赖的关系。比如，Flutter模块中处于基础业务模块的账号插件，依赖位于原生基础业务模块中的账号功能；Flutter模块中处于基础业务模块的网络插件，依赖位于原生基础功能的网络引擎。

可以看到，在混合工程架构中，像原生工程依赖Flutter模块、Flutter模块又依赖原生工程这样跨技术栈的依赖管理行为，我们实际上是通过**将双方抽象为彼此对应技术栈的依赖，从而实现分层管理**的：即将原生对Flutter的依赖抽象为依赖Flutter模块所封装的原生组件，而Flutter对原生的依赖则抽象为依赖插件所封装的原生行为。

#### Flutter混合开发工作流

对于软件开发而言，工程师的职责涉及从需求到上线的整个生命周期，包含需求阶段->方案阶段->开发阶段->发布阶段->线上运维阶段。可以看出，这其实就是一种抽象的工作流程。

其中，**和工程化关联最为紧密的是开发阶段和发布阶段**。我们将工作流中和工程开发相关的部分抽离，定义为开发工作流，根据生命周期中关键节点和高频节点，可以将整个工作流划分为如下七个阶段，即初始化->开发/调试->构建->测试->发布->集成->原生工具链：

![32ebcf0f0f944fb78eb7c672f98a7afe](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/32ebcf0f0f944fb78eb7c672f98a7afe.jpg)

图3 Flutter混合开发工作流

前6个阶段是Flutter的标准工作流，最后一个阶段是原生开发的标准工作流。

可以看到，**在混合开发工作模式中，Flutter的开发模式与原生开发模式之间有着清晰的分工边界**：Flutter模块是原生工程的上游，其最终产物是原生工程依赖。从原生工程视角看，其开发模式与普通原生应用并无区别，因此这里就不再赘述了，我们**重点讨论Flutter开发模式**。

对于Flutter标准工作流的6个阶段而言，每个阶段都会涉及业务或产品特性提出的特异性要求，技术方案的选型，各阶段工作成本可用性、可靠性的衡量，以及监控相关基础服务的接入和配置等。

每件事儿都是一个固定的步骤，而当开发规模随着文档、代码、需求增加时，我们会发现重复的步骤越来越多。此时，**如果我们把这些步骤像抽象代码一样，抽象出一些相同操作，就可以大大提升开发效率。**

优秀的程序员会发掘工作中的问题，从中探索提高生产力的办法，而**转变思维模式就是一个不错的起点**。以持续交付的指导思想来看待这些问题，我们希望整体方案能够以可重复、可配置化的形式，来保障整个工作流的开发体验、效率、稳定性和可靠性，而这些都离不开Flutter对命令行工具支持。

比如，对于测试阶段的Dart代码分析，我们可以使用flutter analyze命令对代码中可能存在的语法或语义问题进行检查；又比如，在发布期的package发布环节，我们可以使用flutter packages pub publish –dry-run命令对待发布的包进行发布前检查，确认无误后使用去掉dry-run参数的publish命令将包提交至Pub站点。

这些基本命令对各个开发节点的输入、输出以及执行过程进行了抽象，熟练掌握它们及对应的扩展参数用法，我们不仅可以在本地开发时打造一个易用便捷的工程开发环境，还可以将这些命令部署到云端，实现工程构建及部署的自动化。

我把这六个阶段涉及的关键命令总结为了一张表格，你可以结合这张表格，体会落实在具体实现中的Flutter标准工作流。

表1 Flutter标准工作流命令

![0bdc4d0a780b45ff9bcef8ed2b44d80e](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/0bdc4d0a780b45ff9bcef8ed2b44d80e.jpg)

#### 总结

对于Flutter混合开发而言，如何处理好原生与Flutter之间的关系，需要从工程架构与工作模式上定义清晰的分工边界。

在架构层面，将Flutter模块定义为原生工程的独立业务层，以原生基础业务层向Flutter模块提供业务通用能力、原生基础能力层向Flutter模块提供基础功能支持这样的方式去分层管理依赖。

在工作模式层面，将作为原生工程上游的Flutter模块开发，抽象为原生依赖产物的工程管理，并提炼出对应的工作流，以可重复、配置化的命令行方式对各个阶段进行统一管理。

可以看到，在原生App工程中引入Flutter运行环境，由原生开发主做应用架构和基础能力赋能、Flutter开发主做应用层业务的混合开发协作方式，能够综合原生App与Flutter框架双方的特点和优势，不仅可以直接节省研发资源，也符合目前行业人才能力模型的发展趋势。

#### 思考题

除了工程依赖之外，我们还需要管理Flutter SDK自身的依赖。考虑到Flutter SDK升级非常频繁，对于多人协作的团队模式中，如何保证每个人使用的Flutter SDK版本完全一致呢？

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

### 如何构建自己的Flutter混合开发框架（二）？

你好，我是陈航。

在上一篇文章中，我从工程架构与工作模式两个层面，与你介绍了设计Flutter混合框架需要关注的基本设计原则，即确定分工边界。

在工程架构维度，由于Flutter模块作为原生工程的一个业务依赖，其运行环境是由原生工程提供的，因此我们需要将它们各自抽象为对应技术栈的依赖管理方式，以分层依赖的方式确定二者的边界。

而在工作模式维度，考虑到Flutter模块开发是原生开发的上游，因此我们只需要从其构建产物的过程入手，抽象出开发过程中的关键节点和高频节点，以命令行的形式进行统一管理。构建产物是Flutter模块的输出，同时也是原生工程的输入，一旦产物完成构建，我们就可以接入原生开发的工作流了。

可以看到，在Flutter混合框架中，Flutter模块与原生工程是相互依存、互利共赢的关系：

- Flutter跨平台开发效率高，渲染性能和多端体验一致性好，因此在分工上主要专注于实现应用层的独立业务（页面）的渲染闭环；
- 而原生开发稳定性高，精细化控制力强，底层基础能力丰富，因此在分工上主要专注于提供整体应用架构，为Flutter模块提供稳定的运行环境及对应的基础能力支持。

那么，在原生工程中为Flutter模块提供基础能力支撑的过程中，面对跨技术栈的依赖管理，我们该遵循何种原则呢？对于Flutter模块及其依赖的原生插件们，我们又该如何以标准的原生工程依赖形式进行组件封装呢？

在今天的文章中，我就通过一个典型案例，与你讲述这两个问题的解决办法。

#### 原生插件依赖管理原则

在前面[第26](https://time.geekbang.org/column/article/127601)和[31篇](https://time.geekbang.org/column/article/132818)文章里，我与你讲述了为Flutter应用中的Dart代码提供原生能力支持的两种方式，即：在原生工程中的Flutter应用入口注册原生代码宿主回调的轻量级方案，以及使用插件工程进行独立拆分封装的工程化解耦方案。

无论使用哪种方式，Flutter应用工程都为我们提供了一体化的标准解决方案，能够在集成构建时自动管理原生代码宿主及其相应的原生依赖，因此我们只需要在应用层使用pubspec.yaml文件去管理Dart的依赖。

但**对于混合工程而言，依赖关系的管理则会复杂一些**。这是因为，与Flutter应用工程有着对原生组件简单清晰的单向依赖关系不同，混合工程对原生组件的依赖关系是多向的：Flutter模块工程会依赖原生组件，而原生工程的组件之间也会互相依赖。

如果继续让Flutter的工具链接管原生组件的依赖关系，那么整个工程就会陷入不稳定的状态之中。因此，对于混合工程的原生依赖，Flutter模块并不做介入，完全交由原生工程进行统一管理。而Flutter模块工程对原生工程的依赖，体现在依赖原生代码宿主提供的底层基础能力的原生插件上。

接下来，我就以网络通信这一基础能力为例，与你展开说明原生工程与Flutter模块工程之间应该如何管理依赖关系。

#### 网络插件依赖管理实践

在第24篇文章“[HTTP网络编程与JSON解析](https://time.geekbang.org/column/article/121163)”中，我与你介绍了在Flutter中，我们可以通过HttpClient、http与dio这三种通信方式，实现与服务端的数据交换。

但在混合工程中，考虑到其他原生组件也需要使用网络通信能力，所以通常是由原生工程来提供网络通信功能的。因为这样不仅可以在工程架构层面实现更合理的功能分治，还可以统一整个App内数据交换的行为。比如，在网络引擎中为接口请求增加通用参数，或者是集中拦截错误等。

关于原生网络通信功能，目前市面上有很多优秀的第三方开源SDK，比如iOS的AFNetworking和Alamofire、Android的OkHttp和Retrofit等。考虑到AFNetworking和OkHttp在各自平台的社区活跃度相对最高，因此我就以它俩为例，与你演示混合工程的原生插件管理方法。

#### 网络插件接口封装

要想搞清楚如何管理原生插件，我们需要先使用方法通道来建立Dart层与原生代码宿主之间的联系。

原生工程为Flutter模块提供原生代码能力，我们同样需要使用Flutter插件工程来进行封装。关于这部分内容，我在第[31](https://time.geekbang.org/column/article/132818)和[39](https://time.geekbang.org/column/article/141164)篇文章中，已经分别为你演示了推送插件和数据上报插件的封装方法，你也可以再回过头来复习下相关内容。所以，今天我就不再与你过多介绍通用的流程和固定的代码声明部分了，而是重点与你讲述与接口相关的实现细节。

**首先，我们来看看Dart代码部分。**

对于插件工程的Dart层代码而言，由于它仅仅是原生工程的代码宿主代理，所以这一层的接口设计比较简单，只需要提供一个可以接收请求URL和参数，并返回接口响应数据的方法doRequest即可：

```
class FlutterPluginNetwork {
  ...
  static Future<String> doRequest(url,params)  async {
    //使用方法通道调用原生接口doRequest，传入URL和param两个参数
    final String result = await _channel.invokeMethod('doRequest', {
      "url": url,
      "param": params,
    });
    return result;
  }
}
```

Dart层接口封装搞定了，我们再来看看**接管真实网络调用的Android和iOS代码宿主如何响应Dart层的接口调用**。

我刚刚与你提到过，原生代码宿主提供的基础通信能力是基于AFNetworking（iOS）和OkHttp（Android）做的封装，所以为了在原生代码中使用它们，我们**首先**需要分别在flutter_plugin_network.podspec和build.gradle文件中将工程对它们的依赖显式地声明出来：

在flutter_plugin_network.podspec文件中，声明工程对AFNetworking的依赖：

```
Pod::Spec.new do |s|
  ...
  s.dependency 'AFNetworking'
end
```

在build.gradle文件中，声明工程对OkHttp的依赖：

```
dependencies {
    implementation "com.squareup.okhttp3:okhttp:4.2.0"
}
```

**然后**，我们需要在原生接口FlutterPluginNetworkPlugin类中，完成例行的初始化插件实例、绑定方法通道工作。

最后，我们还需要在方法通道中取出对应的URL和query参数，为doRequest分别提供AFNetworking和OkHttp的实现版本。

对于iOS的调用而言，由于AFNetworking的网络调用对象是AFHTTPSessionManager类，所以我们需要这个类进行实例化，并定义其接口返回的序列化方式（本例中为字符串）。然后剩下的工作就是用它去发起网络请求，使用方法通道通知Dart层执行结果了：

```
@implementation FlutterPluginNetworkPlugin
...
//方法通道回调
- (void)handleMethodCall:(FlutterMethodCall*)call result:(FlutterResult)result {
    //响应doRequest方法调用
    if ([@"doRequest" isEqualToString:call.method]) {
        //取出query参数和URL
        NSDictionary *arguments = call.arguments[@"param"];
        NSString *url = call.arguments[@"url"];
        [self doRequest:url withParams:arguments andResult:result];
    } else {
        //其他方法未实现
        result(FlutterMethodNotImplemented);
    }
}
//处理网络调用
- (void)doRequest:(NSString *)url withParams:(NSDictionary *)params andResult:(FlutterResult)result {
    //初始化网络调用实例
    AFHTTPSessionManager *manager = [AFHTTPSessionManager manager];
    //定义数据序列化方式为字符串
    manager.responseSerializer = [AFHTTPResponseSerializer serializer];
    NSMutableDictionary *newParams = [params mutableCopy];
    //增加自定义参数
    newParams[@"ppp"] = @"yyyy";
    //发起网络调用
    [manager GET:url parameters:params progress:nil success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject) {
        //取出响应数据，响应Dart调用
        NSString *string = [[NSString alloc] initWithData:responseObject encoding:NSUTF8StringEncoding];
        result(string);
    } failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error) {
        //通知Dart调用失败
        result([FlutterError errorWithCode:@"Error" message:error.localizedDescription details:nil]);
    }];
}
@end
```

Android的调用也类似，OkHttp的网络调用对象是OkHttpClient类，所以我们同样需要这个类进行实例化。OkHttp的默认序列化方式已经是字符串了，所以我们什么都不用做，只需要URL参数加工成OkHttp期望的格式，然后就是用它去发起网络请求，使用方法通道通知Dart层执行结果了：

```
public class FlutterPluginNetworkPlugin implements MethodCallHandler {
  ...
  @Override
  //方法通道回调
  public void onMethodCall(MethodCall call, Result result) {
    //响应doRequest方法调用
    if (call.method.equals("doRequest")) {
      //取出query参数和URL
      HashMap param = call.argument("param");
      String url = call.argument("url");
      doRequest(url,param,result);
    } else {
      //其他方法未实现
      result.notImplemented();
    }
  }
  //处理网络调用
  void doRequest(String url, HashMap<String, String> param, final Result result) {
    //初始化网络调用实例
    OkHttpClient client = new OkHttpClient();
    //加工URL及query参数
    HttpUrl.Builder urlBuilder = HttpUrl.parse(url).newBuilder();
    for (String key : param.keySet()) {
      String value = param.get(key);
      urlBuilder.addQueryParameter(key,value);
    }
    //加入自定义通用参数
    urlBuilder.addQueryParameter("ppp", "yyyy");
    String requestUrl = urlBuilder.build().toString();

    //发起网络调用
    final Request request = new Request.Builder().url(requestUrl).build();
    client.newCall(request).enqueue(new Callback() {
      @Override
      public void onFailure(Call call, final IOException e) {
        //切换至主线程，通知Dart调用失败
        registrar.activity().runOnUiThread(new Runnable() {
          @Override
          public void run() {
            result.error("Error", e.toString(), null);
          }
        });
      }

      @Override
      public void onResponse(Call call, final Response response) throws IOException {
        //取出响应数据
        final String content = response.body().string();
        //切换至主线程，响应Dart调用
        registrar.activity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
              result.success(content);
            }
        });
      }
    });
  }
}
```

需要注意的是，**由于方法通道是非线程安全的，所以原生代码与Flutter之间所有的接口调用必须发生在主线程。**而OktHtp在处理网络请求时，由于涉及非主线程切换，所以需要调用runOnUiThread方法以确保回调过程是在UI线程中执行的，否则应用可能会出现奇怪的Bug，甚至是Crash。

有些同学可能会比较好奇，**为什么doRequest的Android实现需要手动切回UI线程，而iOS实现则不需要呢？**这其实是因为doRequest的iOS实现背后依赖的AFNetworking，已经在数据回调接口时为我们主动切换了UI线程，所以我们自然不需要重复再做一次了。

在完成了原生接口封装之后，Flutter工程所需的网络通信功能的接口实现，就全部搞定了。

#### Flutter模块工程依赖管理

通过上面这些步骤，我们以插件的形式提供了原生网络功能的封装。接下来，我们就需要在Flutter模块工程中使用这个插件，并提供对应的构建产物封装，提供给原生工程使用了。这部分内容主要包括以下3大部分：

- 第一，如何使用FlutterPluginNetworkPlugin插件，也就是模块工程功能如何实现；
- 第二，模块工程的iOS构建产物应该如何封装，也就是原生iOS工程如何管理Flutter模块工程的依赖；
- 第三，模块工程的Android构建产物应该如何封装，也就是原生Android工程如何管理Flutter模块工程的依赖。

接下来，我们具体看看每部分应该如何实现。

#### 模块工程功能实现

为了使用FlutterPluginNetworkPlugin插件实现与服务端的数据交换能力，我们首先需要在pubspec.yaml文件中，将工程对它的依赖显示地声明出来：

```
flutter_plugin_network:
    git:
      url: https://github.com/cyndibaby905/44_flutter_plugin_network.git
```

然后，我们还得在main.dart文件中为它提供一个触发入口。在下面的代码中，我们在界面上展示了一个RaisedButton按钮，并在其点击回调函数时，使用FlutterPluginNetwork插件发起了一次网络接口调用，并把网络返回的数据打印到了控制台上：

```
RaisedButton(
  child: Text("doRequest"),
  //点击按钮发起网络请求，打印数据
  onPressed:()=>FlutterPluginNetwork.doRequest("https://jsonplaceholder.typicode.com/posts", {'userId':'2'}).then((s)=>print('Result:$s')),
)
```

运行这段代码，点击doRequest按钮，观察控制台输出，可以看到，接口返回的数据信息能够被正常打印，证明Flutter模块的功能表现是完全符合预期的。

![a6c9b86b3f534b2c95e3f3df6c2744d2](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/a6c9b86b3f534b2c95e3f3df6c2744d2.jpg)

图1 Flutter模块工程运行示例

#### 构建产物应该如何封装？

我们都知道，模块工程的Android构建产物是aar，iOS构建产物是Framework。而在第[28](https://time.geekbang.org/column/article/129754)和[42](https://time.geekbang.org/column/article/144156)篇文章中，我与你介绍了不带插件依赖的模块工程构建产物的两种封装方案，即手动封装方案与自动化封装方案。这两种封装方案，最终都会输出同样的组织形式（Android是aar，iOS则是带podspec的Framework封装组件）。

如果你已经不熟悉这两种封装方式的具体操作步骤了，可以再复习下这两篇文章的相关内容。接下来，我重点与你讲述的问题是：**如果我们的模块工程存在插件依赖，封装过程是否有区别呢？**

答案是，对于模块工程本身而言，这个过程没有区别；但对于模块工程的插件依赖来说，我们需要主动告诉原生工程，哪些依赖是需要它去管理的。

由于Flutter模块工程把所有原生的依赖都交给了原生工程去管理，因此其构建产物并不会携带任何原生插件的封装实现，所以我们需要遍历模块工程所使用的原生依赖组件们，为它们逐一生成插件代码对应的原生组件封装。

在第18篇文章“[依赖管理（二）：第三方组件库在Flutter中要如何管理？](https://time.geekbang.org/column/article/114180)”中，我与你介绍了Flutter工程管理第三方依赖的实现机制，其中.packages文件存储的是依赖的包名与系统缓存中的包文件路径。

类似的，插件依赖也有一个类似的文件进行统一管理，即**.flutter-plugins**。我们可以通过这个文件，找到对应的插件名字（本例中即为flutter_plugin_network）及缓存路径：

```
flutter_plugin_network=/Users/hangchen/Documents/flutter/.pub-cache/git/44_flutter_plugin_network-9b4472aa46cf20c318b088573a30bc32c6961777/
```

插件缓存本身也可以被视为一个Flutter模块工程，所以我们可以采用与模块工程类似的办法，为它生成对应的原生组件封装。

对于iOS而言，这个过程相对简单些，所以我们先来看看模块工程的iOS构建产物封装过程。

##### iOS构建产物应该如何封装？

在插件工程的ios目录下，为我们提供了带podspec文件的源码组件，podspec文件提供了组件的声明（及其依赖），因此我们可以把这个目录下的文件拷贝出来，连同Flutter模块组件一起放到原生工程中的专用目录，并写到Podfile文件里。

原生工程会识别出组件本身及其依赖，并按照声明的依赖关系依次遍历，自动安装：

```
#Podfile
target 'iOSDemo' do
  pod 'Flutter', :path => 'Flutter'
  pod 'flutter_plugin_network', :path => 'flutter_plugin_network'
end
```

然后，我们就可以像使用不带插件依赖的模块工程一样，把它引入到原生工程中，为其设置入口，在FlutterViewController中展示Flutter模块的页面了。

不过需要注意的是，由于FlutterViewController并不感知这个过程，因此不会主动初始化项目中的插件，所以我们还需要在入口处手动将工程里所有的插件依次声明出来：

```
//AppDelegate.m:
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    self.window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
    //初始化Flutter入口
    FlutterViewController *vc = [[FlutterViewController alloc]init];
    //初始化插件
    [FlutterPluginNetworkPlugin registerWithRegistrar:[vc registrarForPlugin:@"FlutterPluginNetworkPlugin"]];
    //设置路由标识符
    [vc setInitialRoute:@"defaultRoute"];
    self.window.rootViewController = vc;
    [self.window makeKeyAndVisible];
    return YES;
}
```

在Xcode中运行这段代码，点击doRequest按钮，可以看到，接口返回的数据信息能够被正常打印，证明我们已经可以在原生iOS工程中顺利的使用Flutter模块了。

![60988d63786a4b71b654a1d58996f843](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/60988d63786a4b71b654a1d58996f843.jpg)

图2 原生iOS工程运行示例

我们再来看看模块工程的Android构建产物应该如何封装。

##### Android构建产物应该如何封装？

与iOS的插件工程组件在ios目录类似，Android的插件工程组件在android目录。对于iOS的插件工程，我们可以直接将源码组件提供给原生工程，但对于Andriod的插件工程来说，我们只能将aar组件提供给原生工程，所以我们不仅需要像iOS操作步骤那样进入插件的组件目录，还需要借助构建命令，为插件工程生成aar：

```
cd android
./gradlew flutter_plugin_network:assRel
```

命令执行完成之后，aar就生成好了。aar位于android/build/outputs/aar目录下，我们打开插件缓存对应的路径，提取出对应的aar（本例中为flutter_plugin_network-debug.aar）就可以了。

我们把生成的插件aar，连同Flutter模块aar一起放到原生工程的libs目录下，最后在build.gradle文件里将它显式地声明出来，就完成了插件工程的引入。

```
//build.gradle
dependencies {
    ...
    implementation(name: 'flutter-debug', ext: 'aar')
    implementation(name: 'flutter_plugin_network-debug', ext: 'aar')
    implementation "com.squareup.okhttp3:okhttp:4.2.0"
    ...
}
```

然后，我们就可以在原生工程中为其设置入口，在FlutterView中展示Flutter页面，愉快地使用Flutter模块带来的高效开发和高性能渲染能力了：

```
//MainActivity.java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        View FlutterView = Flutter.createView(this, getLifecycle(), "defaultRoute");
        setContentView(FlutterView);
    }
}
```

不过**需要注意的是**，与iOS插件工程的podspec能够携带组件依赖不同，Android插件工程的封装产物aar本身不携带任何配置信息。所以，如果插件工程本身存在原生依赖（像flutter_plugin_network依赖OkHttp这样），我们是无法通过aar去告诉原生工程其所需的原生依赖的。

面对这种情况，我们需要在原生工程中的build.gradle文件里手动地将插件工程的依赖（即OkHttp）显示地声明出来。

```
//build.gradle
dependencies {
    ...
    implementation(name: 'flutter-debug', ext: 'aar')
    implementation(name: 'flutter_plugin_network-debug', ext: 'aar')
    implementation "com.squareup.okhttp3:okhttp:4.2.0"
    ...
}
```

**至此，将模块工程及其插件依赖封装成原生组件的全部工作就完成了，原生工程可以像使用一个普通的原生组件一样，去使用Flutter模块组件的功能了。**

在Android Studio中运行这段代码，并点击doRequest按钮，可以看到，我们可以在原生Android工程中正常使用Flutter封装的页面组件了。

![184e5feaa174413fb37f16bf8dde3864](https://raw.githubusercontent.com/Yvan0329/lianglianglee/4afe4a62c4e105a59d41319a29e523eee3bd82c4/book/%E4%B8%93%E6%A0%8F/Flutter%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/assets/184e5feaa174413fb37f16bf8dde3864.jpg)

图3 原生Android工程运行示例

当然，考虑到手动封装模块工程及其构建产物的过程，繁琐且容易出错，我们可以把这些步骤抽象成命令行脚本，并把它部署到Travis上。这样在Travis检测到代码变更之后，就会自动将Flutter模块的构建产物封装成原生工程期望的组件格式了。

关于这部分内容，你可以参考我在[flutter_module_demo](https://github.com/cyndibaby905/44_flutter_module_demo)里的[generate_aars.sh](https://github.com/cyndibaby905/44_flutter_module_demo/blob/master/generate_aars.sh)与[generate_pods.sh](https://github.com/cyndibaby905/44_flutter_module_demo/blob/master/generate_pods.sh)实现。如果关于这部分内容有任何问题，都可以直接留言给我。

#### 总结

好了，关于Flutter混合开发框架的依赖管理部分我们就讲到这里。接下来，我们一起总结下今天的主要内容吧。

Flutter模块工程的原生组件封装形式是aar（Android）和Framework（Pod）。与纯Flutter应用工程能够自动管理插件的原生依赖不同，这部分工作在模块工程中是完全交给原生工程去管理的。因此，我们需要查找记录了插件名称及缓存路径映射关系的.flutter-plugins文件，提取出每个插件所对应的原生组件封装，集成到原生工程中。

从今天的分享可以看出，对于有着插件依赖的Android组件封装来说，由于aar本身并不携带任何配置信息，因此其操作以手工为主：我们不仅要执行构建命令依次生成插件对应的aar，还需要将插件自身的原生依赖拷贝至原生工程，其步骤相对iOS组件封装来说要繁琐一些。

为了解决这一问题，业界出现了一种名为[fat-aar](https://github.com/adwiv/android-fat-aar)的打包手段，它能够将模块工程本身，及其相关的插件依赖统一打包成一个大的aar，从而省去了依赖遍历和依赖声明的过程，实现了更好的功能自治性。但这种解决方案存在一些较为明显的不足：

- 依赖冲突问题。如果原生工程与插件工程都引用了同样的原生依赖组件（OkHttp），则原生工程的组件引用其依赖时会产生合并冲突，因此在发布时必须手动去掉原生工程的组件依赖。
- 嵌套依赖问题。fat-aar只会处理embedded关键字指向的这层一级依赖，而不会处理再下一层的依赖。因此，对于依赖关系复杂的插件支持，我们仍需要手动处理依赖问题。
- Gradle版本限制问题。fat-aar方案对Gradle插件版本有限制，且实现方式并不是官方设计考虑的点，加之Gradle API变更较快，所以存在后续难以维护的问题。
- 其他未知问题。fat-aar项目已经不再维护了，最近一次更新还是2年前，在实际项目中使用“年久失修”的项目存在较大的风险。

考虑到这些因素，fat-aar并不是管理插件工程依赖的好的解决方案，所以**我们最好还是得老老实实地去遍历插件依赖，以持续交付的方式自动化生成aar。**

我把今天分享涉及知识点打包上传到了GitHub中，你可以把[插件工程](https://github.com/cyndibaby905/44_flutter_plugin_network)、[Flutter模块工程](https://github.com/cyndibaby905/44_flutter_module_demo)、[原生Android](https://github.com/cyndibaby905/44_AndroidDemo)和[iOS工程](https://github.com/cyndibaby905/44_iOSDemo)下载下来，查看其Travis持续交付配置文件的构建执行命令，体会在混合框架中如何管理跨技术栈的组件依赖。

#### 思考题

最后，我给你留一道思考题吧。

原生插件的开发是一个需要Dart层代码封装，以及原生Android、iOS代码层实现的长链路过程。如果需要支持的基础能力较多，开发插件的过程就会变得繁琐且容易出错。我们都知道Dart是不支持反射的，但是原生代码可以。我们是否可以利用原生的反射去实现插件定义的标准化呢？

提示：在Dart层调用不存在的接口（或未实现的接口），可以通过noSuchMethod方法进行统一处理。

```
class FlutterPluginDemo {
  //方法通道
  static const MethodChannel _channel =
      const MethodChannel('flutter_plugin_demo');
  //当调用不存在接口时，Dart会交由该方法进行统一处理
  @override
  Future<dynamic> noSuchMethod(Invocation invocation) {
    //从字符串Symbol("methodName")中取出方法名
    String methodName = invocation.memberName.toString().substring(8, string.length - 2);
    //参数
    dynamic args = invocation.positionalArguments;
    print('methodName:$methodName');
    print('args:$args');
    return methodTemplate(methodName, args);
  }

  //某未实现的方法
  Future<dynamic> someMethodNotImplemented();
  //某未实现的带参数方法
  Future<dynamic> someMethodNotImplementedWithParameter(param);
}
```

欢迎你在评论区给我留言分享你的观点，我会在下一篇文章中等待你！感谢你的收听，也欢迎你把这篇文章分享给更多的朋友一起阅读。

## 特别放送与结束语

### 特别放送   温故而知新，与你说说专栏的那些思考题

你好，我是陈航。专栏上线以来，我在评论区看到了很多同学写的心得、经验和建议，当然更多的还是大家提的问题。

为了能够让大家更好地理解我们专栏的核心知识点，我今天特意整理了每篇文章的课后思考题，并结合大家在留言区的回答情况做一次分析与扩展。

当然 ，我也希望你能把这篇答疑文章作为对整个专栏所讲知识点的一次复习，如果你在学习或者使用Flutter的过程中，遇到哪些问题，欢迎继续给我留言。我们一起交流，共同进步！

需要注意的是，这些课后题并不存在标准答案。就算是同一个功能、同一个界面，不同人也会有完全不一样的实现方案，只要你的解决方案的输入和输出满足题目要求，在我看来你就已经掌握了相应的知识点。因此，**在这篇文章中，我会更侧重于介绍方案、实现思路、原理和关键细节，而不是讲具体实操的方方面面。**

接下来，我们就具体看看这些思考题的答案吧。

问题1：直接在build函数里以内联的方式实现Scaffold页面元素的构建，好处是什么？

这个问题选自第5篇文章“[从标准模板入手，体会Flutter代码是如何运行在原生系统上的](https://time.geekbang.org/column/article/106199)”，你可以先回顾下这篇文章的相关知识点。

然后，我来说说这样做的最大好处是，各个组件之间可以直接共享页面的状态和方法，页面和组件间不再需要把状态数据传来传去、多级回调了。

不过这种方式也有缺点，一旦数据发生变更，Flutter会重建整个大Widget（而不是变化的那部分），所以会对性能产生些影响。

问题2：对于集合类型List和Map，如何让其内部元素支持多种类型？

这个问题来自第6篇文章“[基础语法与类型变量：Dart是如何表示信息的？](https://time.geekbang.org/column/article/106816)”，你可以先回顾下这篇文章的相关知识点。

如果集合中多个类型之间存在共同的父类（比如double和int），可以使用父类进行容器类型声明，从而增加类型的安全校验，在取出对象时根据runtimeType转换成实际类型即可。如果容器中的类型比较多，想省掉类型转换的步骤，也可以使用动态类型dynamic为元素添加不同类型的元素。

而在判断元素真实类型时，我们可以使用is关键字或runtimeType。

问题3：继承、接口与混入的相关问题。

这个问题来自第7篇文章“[函数、类与运算符：Dart是如何处理信息的？](https://time.geekbang.org/column/article/107399)”，你可以先回顾下这篇文章的相关知识点。

**第一**，你是怎样理解父类继承、接口实现和混入的？我们应该在什么场景下使用它们？

父类继承、接口实现和混入都是实现代码复用的手段，我们在代码中应该根据不同的需求去使用。其中：

- 在父类继承中，子类复用了父类的实现，适用于两个类的整体存在逻辑层次关系的场景；
- 在接口实现中，类复用了接口的参数、返回值和方法名，但不复用其方法实现，适用于接口和类在行为存在逻辑层次关系的场景；
- 而混入则可以使一个类复用多个类的实现，这些类之间无需存在父子关系，适用于多个类的局部存在逻辑层次关系的场景。

**第二**，在父类继承的场景中，父类子类之间的构造函数执行顺序是怎样的？如果父类有多个构造函数，子类也有多个构造函数，如何从代码层面确保父类子类之间构造函数的正确调用？

默认情况下，子类的构造函数会自动调用父类的默认构造函数，如果需要显式地调用父类的构造函数，则需要在子类构造函数的函数体开头位置调用。但，如果子类提供了初始化参数列表，则初始化参数列表会在父类构造函数之前执行。

构造函数之间，有时候会有一些相同的逻辑。如果把这些逻辑分别写在各个构造函数中，会有些累赘，所以构造函数之间是可以传递的，相当于填充了某个构造函数的参数，从而实现类的初始化。因此可以传递的构造函数是没有方法体的，它们只会在初始化列表中，去调用另一个构造函数。

如果子类与父类存在多个构造函数，通常是为了简化类的初始化代码，将部分不需要的属性设置为默认值。因此，我们只要能确保每条构造函数的初始化路径都不会有属性被遗漏即可。**一个好的做法是**，依照构造函数的参数个数，将参数少的构造函数转发至参数多的构造函数中，由参数最多的构造函数统一调用父类参数最多的那个构造函数。

问题4：扩展购物车案例的程序，使其支持商品数量属性，并输出商品列表信息（包括商品名称、数量及单价）。

这个问题来自第8篇文章“[综合案例：掌握Dart核心特性](https://time.geekbang.org/column/article/107315)”，你可以先回顾下这篇文章的相关知识点。

要实现这个扩展功能，如我所说，每个人都可能有完全不一样的解决方案。在这里，我给你的提示是，在Item类中增加数量属性，在做小票打印时，循环购物车内的商品信息即可实现。

需要注意的是，增加数量属性后，商品在做合并计算价格时，count需要置为1，而不能做累加。比如，五斤苹果和三盒巧克力做合并，结果是一份巧克力苹果套餐，而不是八份巧克力苹果套餐。

问题5：Widget、Element 和 RenderObject之间是什么关系？你能否在Android/iOS/Web中找到对应的概念呢？

这个问题来自第9篇文章“[Widget，构建Flutter界面的基石](https://time.geekbang.org/column/article/108522)”。

Widget是数据配置，RenderObject负责渲染，而Element是一个介于它们之间的中间类，用于渲染资源复用。

Widget和Element是一一对应的，但RenderObject不是，只有实际需要布局和绘制的控件才会有RenderObject。

这三个概念在iOS、Android和Web开发中，对应的概念分别是：

- 在iOS中，Xib相当于Widget，UIView相当于Element，CALayer相当于renderObject；
- 在Android中，XML相当于Widget，View相当于Element，Canvas相当于renderObject；
- 在Web中，以Vue为例，Vue的模板相当于Widget，virtual DOM相当于Element，DOM相当于RenderObject。

问题6：State构造函数和initState的差异是什么？

这个问题来自第11篇文章“[提到生命周期，我们是在说什么？](https://time.geekbang.org/column/article/109490)”。

State构造函数调用时，Widget还未完成初始化，因此仅适用于一些与UI无关的数据初始化，比如父类传入的参数加工。

而initState函数调用时，StatefulWidget已经完成了Widget树的插入工作，因此与Widget相关的一些初始化工作，比如设置滚动监听器则必须放在initState。

问题7：Text、Image以及按钮控件，真正承载其视觉功能的控件分别是什么？

这个问题来自第12篇文章“[经典控件（一）：文本、图片和按钮在Flutter中怎么用？](https://time.geekbang.org/column/article/110292)”。

Text是封装了RichText的StatelessWidget，Image是封装了RawImage的StatefulWidget，而按钮则是封装了RawMaterialButton的StatelessWidget。

可以看到，StatelessWidget和StatefulWidget只是封装了控件的容器，并不参与实际绘制，真正负责渲染的是继承自RenderObject的视觉功能组件们，比如RichText与RawImage。

问题8：在ListView中，如何提前缓存子元素？

这个问题来自第13篇文章“[经典控件（二）：UITableView/ListView在Flutter中是什么？](https://time.geekbang.org/column/article/110859)”。

ListView构造函数中有一个cacheExtent参数，即预渲染区域长度。ListView会在其可视区域的两边留一个cacheExtent长度的区域作为预渲染区域，相当于提前缓存些元素，这样当滑动时就可以迅速呈现了。

问题9：Row与Column自身的大小是如何决定的？当它们嵌套时，又会出现怎样的情况呢？

这个问题来自第14篇文章“[经典布局：如何定义子控件在父容器中排版的位置？](https://time.geekbang.org/column/article/110848)”。

Row与Column自身的大小由父Widget的大小、子Widget的大小，以及mainSize共同决定。

Row和Column只会在主轴方向占用尽可能大的空间（max：屏幕方向主轴大小或父Widget主轴方向大小；min：所有子Widget组合在一起的主轴方向大小），而纵轴的长度则取决于它们最大子元素的长度。

如果Row里面嵌套Row，或者Column里面嵌套Column，只有最外层的Row或Colum才会占用尽可能大的空间，里层Row或Column占用的空间为实际大小。

问题10：在 UpdatedItem 控件的基础上，增加切换夜间模式的功能。

这个问题来自第16篇文章“[从夜间模式说起，如何定制不同风格的App主题？](https://time.geekbang.org/column/article/112148)”。

这是一道实践题。同样地，我在这里也只提示你实现思路：你可以在ThemeData中，通过增加变量来判断当前使用何种主题，然后在State中驱动变量更新即可。

问题11：像素密度为3.0及1.0设备，如何根据资源图片像素进行处理？

这个问题来自第17篇文章“[依赖管理（一）：图片、配置和字体在Flutter中怎么用？](https://time.geekbang.org/column/article/113495)”。

设备根据资源图片像素进行适配的原则是：调整为使用最合适的分辨率资源，即像素密度为3.0的设备会选择2.0而不是1.0的资源图片；而像素密度为1.0的设备，对于像素密度大于1.0的资源图片会进行压缩。

问题12：.packages 与 pubspec.lock 是否需要做代码版本管理？

这个问题来自第18篇文章“[依赖管理（二）：第三方组件库在Flutter中要如何管理？](https://time.geekbang.org/column/article/114180)”。

pubspec.lock需要做版本管理，因为lock文件记录了Dart在计算项目依赖时，当前工程所有显式和隐私的依赖关系。我们可以直接使用这个结果去统一工程开发环境。

而.packages不需要版本管理，因为这个文件记录了Dart在计算项目依赖时，当前工程所有依赖的本地缓存文件。与本地环境有关，无需统一。

问题13：GestureDetector内嵌FlatButton后，事件是如何响应的？

这个问题来自第19篇文章“[用户交互事件该如何响应？](https://time.geekbang.org/column/article/116326)”。

对于一个父容器中存在按钮FlatButton的界面，在父容器使用GestureDetector监听了onTap事件的情况下，我们点击按钮是不会被父Widget响应的。因为，手势竞技场只会同时响应一个（子Widget）。

如果监听的是onDoubleTap事件，在按钮上双击后，父容器的双击事件会被识别。因为，子Widget没有处理双击事件，不需要经历手势竞技场的PK过程。

问题14：请分别概括属性传值、InheritedWidget、Notification 与 EventBus的特点。

这个问题来自第20篇文章“[关于跨组件传递数据，你只需要记住这三招](https://time.geekbang.org/column/article/116382)”。

**属性传值**适合在同一个视图树中使用，传递方向由父及子，通过构造方法将值以属性的方式传递过去，简单高效。其缺点是，涉及跨层传递时，属性可能需要跨越很多层才能传递给子组件，导致中间很多并不需要这个属性的组件，也得接收其子Widget的数据，繁琐且冗余。

**InheritedWidget**适用于子Widget主动向上层拿数据的场景，传递方向由父及子，可以实现跨层的数据读共享。InheritedWidget也可以实现写共享，需要在上层封装写数据的方法供下层调用。其优点是，数据传输方便，无代码侵入即可达到逻辑和视图解耦的效果；而其缺点是，如果层次较深，刷新范围过大会影响性能。

**Notification**适用于子Widget向父Widget推送数据的场景，传递方向由子及父，可以实现跨层的数据变更共享。其优点是，多个子元素的同一事件可由父元素统一处理，多对一简单；而其缺点是，Notification的自定义过程略繁琐。

**EventBus**适用于无需存在父子关系的实体之间通信，订阅者需要显式地订阅和取消。其优点是，能够支持任意对象的传递，一对多的方式实现简单；而其缺点是，订阅管理略显繁琐。

问题15：实现一个计算页面，这个页面可以对前一个页面传入的 2 个数值参数进行求和，并在该页面关闭时告知上一页面计算的结果。

这个问题来自第21篇文章“[路由与导航，Flutter是这样实现页面切换的](https://time.geekbang.org/column/article/118421)”。

这是一个实践题，还需要你动手去实现。这里，我给你的提示是：基本路由可以通过构造函数属性传值的方式，或是在MaterialPageRoute中加入参数setting，来传递页面参数。

打开页面时，我们可以使用上述机制为基本路由传递参数（2个数值），并注册then回调监听页面的关闭事件；而页面需要关闭时，我们将2个数值参数取出，求和后调用pop函数即可。

问题16：AnimatedBuilder中，外层的child参数与内层builder函数中的child参数的作用分别是什么？

```
AnimatedBuilder(
  animation: animation,
  child:FlutterLogo(),
  builder: (context, child) => Container(
    width: animation.value,
    height: animation.value,
    child: child
  )
)
```

这个问题来自第22篇文章“[如何构造炫酷的动画效果？](https://time.geekbang.org/column/article/119148)”。

外层的child参数定义渲染，内层builder中的child参数定义动画，实现了动画和渲染的分离。通过builder函数，限定了重建rebuild的范围，做动画时不必每次重新构建整个Widget。

问题17：并发 Isolate 计算阶乘例子里给并发Isolate两个SendPort的原因？

```
//并发计算阶乘
Future<dynamic> asyncFactoriali(n) async{
  final response = ReceivePort();//创建管道
  //创建并发Isolate，并传入管道
  await Isolate.spawn(_isolate,response.sendPort);
  //等待Isolate回传管道
  final sendPort = await response.first as SendPort;
  //创建了另一个管道answer
  final answer = ReceivePort();
  //往Isolate回传的管道中发送参数，同时传入answer管道
  sendPort.send([n,answer.sendPort]);
  return answer.first;//等待Isolate通过answer管道回传执行结果
}

//Isolate函数体，参数是主Isolate传入的管道
_isolate(initialReplyTo) async {
  final port = ReceivePort();//创建管道
  initialReplyTo.send(port.sendPort);//往主Isolate回传管道
  final message = await port.first as List;//等待主Isolate发送消息(参数和回传结果的管道)
  final data = message[0] as int;//参数
  final send = message[1] as SendPort;//回传结果的管道
  send.send(syncFactorial(data));//调用同步计算阶乘的函数回传结果
}

//同步计算阶乘
int syncFactorial(n) => n < 2 ? n : n * syncFactorial(n-1);
main() async => print(await asyncFactoriali(4));//等待并发计算阶乘结果
```

这个问题来自第23篇文章“[单线程模型怎么保证UI运行流畅？](https://time.geekbang.org/column/article/120014)”。

SendPort/ReceivePort是一个单向管道，帮助我们**实现并发Isolate往主Isolate回传执行结果**：并发Isolate负责用SendPort发，而主Isolate负责用ReceivePort收。对于回传执行结果这个过程而言，主Isolate除了被动等待没有别的办法。

在这个例子中，并发Isolate用SendPort发了两次数据，意味着主Isolate也需要用SendPort对应的ReceivePort等待两次。如果并发Isolate用SenderPort发了三次数据，那主Isolate也需要用ReceivePort等待三次。

那么，主Isolate怎么知道自己需要等待几次呢，总不能一直等着吧？

所以更好的办法是，只使用SendPort/ReceivePort一次，发/收完了就不用了。但，如果下次还要发/收怎么办？

这时，我们就可以参考这个计算阶乘案例的做法，在发数据的时候把下一次用到的SendPort也当做参数传过去。

问题18：自定义dio拦截器，检查并刷新token。

这个问题来自第24篇文章“[HTTP网络编程与JSON解析](https://time.geekbang.org/column/article/121163)”。

这也是一个实践题，我同样只提示你关键思路：在拦截器的onRequest方法中，检查header中是否存在token，如果没有，则发起一个新的请求去获取token，更新header。考虑到可能会有多个request同时发出，token会请求多次，我们可以通过调用拦截器的 lock/unlock 方法来锁定/解锁拦截器。

一旦请求/响应拦截器被锁定，接下来的请求/响应将会在进入请求/响应拦截器之前排队等待，直到解锁后，这些入队的请求才会继续执行（进入拦截器）。

问题19：持久化存储的相关问题。

这个问题来自来第25篇文章“[本地存储与数据库的使用和优化](https://time.geekbang.org/column/article/126460)”。

**首先**，我们先看看文件、SharedPreferences 和数据库，这三种持久化数据存储方式的适用场景。

- 文件比较适合大量的、有序的数据持久化；
- SharedPreferences，适用于缓存少量键值对信息；
- 数据库，则用来存储大量格式化后的数据，并且这些数据需要以较高频率更新。

**接下来**，我们看看如何做数据库跨版本升级？

数据库升级，实际上就是改表结构。如果升级过程是连续的，我们只需要在每个版本执行修改表结构的语句就可以了。如果升级过程不是连续的，比如直接从1.0升到5.0，中间2.0、3.0和4.0都直接跳过的：

```
1.0->2.0：执行表结构修改语句A
2.0->3.0：执行表结构修改语句B
3.0->4.0：执行表结构修改语句C
4.0->5.0：执行表结构修改语句D
```

因此，我们在5.0的数据库迁移中，不能只考虑5.0的表结构，单独执行4.0的升级逻辑D，还需要考虑2.0、3.0、4.0的表结构，把1.0升级到4.0之间的所有升级逻辑执行一遍：

```
switch(oldVersion) {
 case '1.0': do A;
 case '2.0': do B;
 case '3.0': do C;
 case '4.0': do D;
 default: print('done');
}
```

这样就万无一失了。

不过需要注意的是，在Dart的switch里，条件判断break语句是不能省的。关于如何在Dart中写出类似C++的fallthrough switch，你可以再思考一下。

问题20：扩展openAppMarket的实现，使得我们可以跳转到任意一个App的应用市场。

这个问题来自第26篇文章“[如何在Dart层兼容Android/iOS平台特定实现？（一）](https://time.geekbang.org/column/article/127601)”。

对于这个问题，我给你的提示是：Dart调用invokeMethod方法时，可传入Map类型的键值对参数（包含iOS的bundleID和Android包名），然后在原生代码宿主将参数取出即可。

问题21：扩展内嵌原生视图的实现，实现动态变更原生视图颜色的需求。

这个问题来自第27篇文章“[如何在Dart层兼容Android/iOS平台特定实现？（二）](https://time.geekbang.org/column/article/128510)”。

对于这个问题，我给你提示与上一问题类似：Dart调用invokeMethod方法时，可传入Map类型的键值对参数（颜色的RGB信息），然后在原生代码宿主将参数取出即可。

问题22：对于有资源依赖的Flutter模块工程，其打包构建的产物，以及抽离组件库的过程是否有不同？

这个问题来自第28篇文章“[如何在原生应用中混编Flutter工程？](https://time.geekbang.org/column/article/129754)”。

答案是没什么不同。因为Flutter模块的文件本身就包含了资源文件。

如果模块工程有原生插件依赖，则其抽离过程还需要借助记录了插件本地依赖缓存地址的.flutter-plugins文件，来实现组件依赖的原生部分的封装。具体细节，你可以参考[第44篇文章](https://time.geekbang.org/column/article/129754)。

问题23：如何确保混合工程中两种页面过渡动画在应用整体的效果一致？

这个问题来自第29篇文章“[混合开发，该用何种方案管理导航栈？](https://time.geekbang.org/column/article/131234)”

首先，这两种页面过渡动画分别是：原生页面之间的切换动画和Flutter页面之间的切换动画。

保证整体效果一致，有两种方案：

- 一是，分别定制原生工程（主要是Android）的切换动画，及Flutter的切换动画；
- 二是，使用类似闲鱼的共享FlutterView的机制，将页面切换统一交由原生处理，FlutterView只负责刷新界面。

问题24：如何使用Provider实现2个同样类型的对象共享？

这个问题来自第30篇文章“[为什么需要做状态管理，怎么做？](https://time.geekbang.org/column/article/131890)”

答案很简单，你可以封装1个大对象，将2个同样类型的对象封装为其内部属性。

问题25：如何让Flutter代码能够更快地收到推送消息？

这个问题来自第31篇文章“[如何实现原生推送能力？](https://time.geekbang.org/column/article/132818)”。

我们需要先判断当前应用是处于前台还是后台，然后再用对应的方式去处理：

- 如果应用处于前台，并且已经完成初始化，则原生代码直接调用方法通道通知Flutter；如果应用未完成初始化，则原生代码将消息存在本地，待Flutter应用初始化完成后，调用方法通道主动拉取。
- 如果应用处于后台，则原生代码将消息存在本地，唤醒Flutter应用，待Flutter应用初始化完成后，调用方法通道主动拉取。

问题26：如何实现图片资源的国际化？

这个问题来自第32篇文章“[适配国际化，除了多语言我们还需要注意什么？](https://time.geekbang.org/column/article/134163)”。

其实，图片资源国际化与文本资源，本质上并无区别，只需要在arb文件中对不同的图片进行单独声明即可。具体的实现细节，你可以再回顾下这篇文章的相关内容。

问题27：相邻页面的横竖屏切换如何实现？

这个问题来自第33篇文章“[如何适配不同分辨率的手机屏幕？](https://time.geekbang.org/column/article/135098)”。

这个实现方式很简单。你可以在initState中设置屏幕支持方向，在dispose时将屏幕方向还原即可。

问题28：在保持生产环境代码不变的情况下，如何支持不同配置的切换？

这个问题来自第34篇文章“[如何理解Flutter的编译模式？](https://time.geekbang.org/column/article/135865)”。

与配置夜间模式类似，我们可以通过增加状态开关来判断当前使用何种配置，设置入口，然后在State中驱动变量更新即可。关于夜间模式的配置，你可以再回顾下第16篇文章“[从夜间模式说起，如何定制不同风格的App主题？](https://time.geekbang.org/column/article/112148)”中的相关内容。

问题29：将debugPrint改为循环写日志。

这个问题来自第36篇文章“[如何通过工具链优化开发调试效率？](https://time.geekbang.org/column/article/137789)”

关于这个问题，我给你的提示是，用不同的main文件定义debugPrint行为：main-dev.dart定义为日志输出至控制台，而main.dart定义为输出至文件。当前操作的文件名默认为0，写满后文件名按5取模递增，同步更新至SharedPreferences中，并将文件清空，重新写入。

问题30：使用并发Isolate完成MD5的计算。

这个问题来自第37篇文章“[如何检测并优化Flutter App的整体性能表现？](https://time.geekbang.org/column/article/138877)”。

关于这个问题，我给你的提示是：将界面改造为StatefulWidget，把MD5的计算启动放在StatefulWidget的初始化中，使用compute去启动计算。在build函数中，判断是否存在MD5数据，如果没有，展示CircularProgressIndicator，如果有，则展示ListView。

问题31：如何使用mockito为SharedPreferences增加单元测试用例？

```
Future<bool>updateSP(SharedPreferences prefs, int counter) async {
  bool result = await prefs.setInt('counter', counter);
  return result;
}

Future<int>increaseSPCounter(SharedPreferences prefs) async {
  int counter = (prefs.getInt('counter') ?? 0) + 1;
  await updateSP(prefs, counter);
  return counter;
}
```

这个问题来自第38篇文章“[如何通过自动化测试提高交付质量？](https://time.geekbang.org/column/article/140079)”。

待测函数updateSP与increaseSPCounter，其内部依赖了SharedPreferences的setInt方法与getInt方法，其中前者是异步函数，后者是同步函数。

因此，我们只需要为setInt与getInt模拟对应的数据返回即可。对于setInt，我们只需要在参数为1的时候返回true：

```
when(prefs.setInt('counter', 1)).thenAnswer((_) async => true);
```

对于getInt，我们只需要返回2：

```
when(prefs.getInt('counter')).thenAnswer((_) => 2);
```

其他部分与普通的单元测试并无不同。

问题32：并发Isolate的异常如何采集？

这个问题来自第39篇文章“[线上出现问题，该如何做好异常捕获与信息采集？](https://time.geekbang.org/column/article/141164)”。

并发Isolate的异常是无法通过try-catch来捕获的。并发Isolate与主Isolate通信是采用SendPort的消息机制，而异常本质上也可以视作一种消息传递机制。所以，如果主Isolate想要捕获并发Isolate中的异常消息，可以给并发Isolate传入SendPort。

而创建Isolate的函数spawn中就恰好有一个类型为SendPort的onError参数，因此并发Isolate可以通过往这个参数里发送消息，实现异常通知。

问题33：依赖单个或多个网络接口数据的页面加载时长应该如何统计？

这个问题来自第40篇文章“[衡量Flutter App线上质量，我们需要关注这三个指标](https://time.geekbang.org/column/article/142509)”。

页面加载时长=页面完成渲染的时间-页面初始化的时间。所以，我们只需要在进入页面时记录启动页面初始化时间，在接口返回数据刷新界面的同时，开启单次帧绘制回调，检测到页面完成渲染后记录页面渲染完成时间，两者相减即可。如果页面的渲染涉及到多个接口也类似。

问题34：如何设置Travis的Flutter版本？

这个问题来自第42篇文章“[如何构建高效的Flutter App打包发布环境？](https://time.geekbang.org/column/article/144156)”。

设置方式很简单。在before_install字段里，克隆Flutter SDK时，直接指定特定的分支即可：

```
git clone -b 'v1.5.4-hotfix.2' --depth 1 https://github.com/flutter/flutter.git
```

问题35：如何通过反射快速实现插件定义的标准化？

这个问题来自第44篇文章“[如何构建自己的Flutter混合开发框架（二）？](https://time.geekbang.org/column/article/144243)”。

在Dart层调用不存在的接口（或未实现的接口），可以通过noSuchMethod方法进行统一处理。这个方法会携带一个类型为Invocation的参数invocation，我们可以通过它得到调用的函数名及参数：

```
//获取方法名
String methodName = invocation.memberName.toString().substring(8, string.length - 2);
//获取参数
dynamic args = invocation.positionalArguments;
```

其中，参数args是一个List类型的变量，我们可以在原生代码宿主把相关的参数依次解析出来。有了函数名和参数，我们在插件类实例上，就可以利用反射去动态地调用原生方法了。

与传统的方法调用相比，以反射的方式执行方法调用，其步骤相对繁琐一些，我们需要依次找到并初始化反射调用过程的类示例对象、方法对象、参数列表对象，然后执行反射调用，并根据方法声明获取执行结果。不过这些步骤都是固定的，我们依葫芦画瓢就好。

Android端的调用方式：

```
public void onMethodCall(MethodCall call, Result result) {
  ...
  String method = call.argument("method"); //获取函数名
  ArrayList params = call.argument("params"); //获取参数列表
  Class<?> c = FlutterPluginDemoPlugin.class; //反射施加对象
  Method m = c.getMethod(method, ArrayList.class); //获取方法对象
  Object ret = m.invoke(this,params); //在插件实例上调用反射方法，获取返回值
  result.success(ret); //返回执行结果
  ...
}
```

iOS端的调用方式：

```
- (void)handleMethodCall:(FlutterMethodCall*)call result:(FlutterResult)result {
 ...
  NSArray *arguments = call.arguments[@"params"]; //获取函数名
  NSString *methodName = call.arguments[@"method"]; //获取参数列表
  SEL selector = NSSelectorFromString([NSString stringWithFormat:@"%@:",methodName]); //获取函数对应的Slector
  NSMethodSignature *signature = [[self class] instanceMethodSignatureForSelector:selector]; //在插件实例上获取方法签名
  NSInvocation *invocation = [NSInvocation invocationWithMethodSignature:signature]; //通过方法签名生成反射的invocation对象

  invocation.target = self; //设置invocation的执行对象
  invocation.selector = selector; //设置invocation的selector
  [invocation setArgument:&arguments atIndex:2]; //设置invocation的参数

  [invocation invoke]; //执行反射

  NSObject *ret = nil;
  if (signature.methodReturnLength) {
      void *returnValue = nil;
      [invocation getReturnValue:&returnValue];
      ret = (__bridge NSObject *)returnValue; //获取反射调用结果
  }

  result(ret); //返回执行结果
  ...
}
```

以上，就是“Flutter核心技术与实战”专栏，全部思考题的答案了。你如果还有其他问题的话，欢迎给我留言，我们一起讨论。

### 结束语 勿畏难，勿轻略

你好，我是陈航。

三个多月的时间转瞬即逝，转眼间《Flutter核心技术与实战》已经走到了尾声。在这里，**我要感谢你对我和这个专栏的鼓励和支持，也要向你表示祝贺**：你已经完整地学习了专栏的全部课程，实现了从入门到进阶Flutter技术的目标，你的坚持一定有所收获。现在专栏课程已经结束了，但还不能松懈，我们的Flutter学习旅程并未结束，从进阶到精通还有很长的一段路需要走，希望你能保持持续学习的习惯。

在这三个月的时间里，我们先后扫清了Dart语言基础语法及常用特性障碍；系统学习了Flutter框架原理和核心设计思想，掌握了构建炫酷页面从底层原理到上层应用的关键技术；学习了Flutter疑难问题及高阶特性的背后原理，并通过一些围绕效率和质量典型的场景，分析了在企业级应用迭代中，如何构建自己的Flutter开发体系。

专栏正文虽然已经更新完毕了，但我们的交流还会继续。同时**针对专栏前面的课后题及留言，我也会从中专门挑选一些有代表性的问题进行深入讲解**。

与此同时，我也很高兴地看到，在Google针对前端和移动端的布局愿景和强力带动的形势下，Flutter的发展方向愈加清晰。

在2019年，Flutter有了越来越多的知名公司加持背书，其开发者生态正在日益繁荣，开发者体验越来越好，支持的终端类型越来越广，使用的项目也越来越多。在开源社区里，Flutter是目前最火的大前端技术，正在经历着从小范围验证到大面积商业应用的过程。

大前端的技术更新迭代快、东西多，很容易让人挑花了眼。如果仅仅停留在对应用层API的使用上，不仅容易滋生学不动的困扰，也会让人产生工程师杂而不精的观点。**大前端技术都是相似相通的，我认为一名优秀的大前端工程师应该具备以下特征：**

- 在技术层面应该抛开对开发框架的站队，除了应用层API之外，能够更多地关注其底层原理、设计思路和通用理念，对中短期技术发展方向有大致思路，并思考如何与过往的开发经验相结合，融汇进属于自己的知识体系抽象网络；
- 而在业务上应该跳出自身职能的竖井，更多关注产品交互设计层面背后的决策思考，在推进项目时，能够结合大前端直面用户的优势，将自己的专业性和影响力辐射到协作方上下游，综合提升自己统筹项目的能力。

**做好一件事从来都不是一蹴而就的。**

以我写专栏的过程来说，我自认为在大前端领域摸爬滚打多年，撰写专栏应该是一件驾轻就熟的事情。但从一开始的筹备阶段，我就慢慢发现这个事情远比我想象的要困难。与之前零散的总结输出相比，专栏的组织形式和交付方式需要花费数倍的精力。

为了把每一个知识点讲透，我需要花费大量的时间和精力去构思文章结构、验证设计、准备素材、代码实践。期间也不乏为了确认一个知识细节，花费数天时间去查阅资料、阅读源码、验证实现。

就这样从初春写到深秋，整整7个月，几乎每个工作日的夜晚和周末，都用在了学习、写作和录音上，这个过程虽然很痛苦，但对我来说收获是巨大的。可以说，《Flutter核心技术与实战》这个专栏对我自己也是一个认知重塑的过程。

**进步很难，其实是因为那些可以让人进步的事情往往都是那些让人焦虑、带来压力的。**而人生的高度，可能就在于你怎么面对困难，真正能够减轻焦虑的办法就是走出舒适区，迎难而上，去搞定那些给你带来焦虑和压力的事情，这样人生的高度才能被一点点垫起来。解决问题的过程通常并不是一帆风顺的，这就需要坚持。所谓胜利者，往往是能比别人多坚持一分钟的人。

勿畏难，勿轻略，让我们在技术路上继续扩大自己的边界，保持学习，持续成长。
