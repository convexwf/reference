---
title: "Google HTML/CSS 风格指南"
authors:
  - "Google Style Guide contributors"
  - "zh-google-styleguide translators"
language: "zh-CN"
tags:
  - "google"
  - "style-guide"
  - "html-css"
published_at: "2013-05-27"
updated_at: "2024-12-08"
---

# Google HTML/CSS 风格指南

## 文档信息

| 项目 | 内容 |
| --- | --- |
| 文档标题 | Google HTML/CSS 风格指南 |
| 文档类型 | zh-CN 整合 Markdown |
| 上游仓库 | [zh-google-styleguide/zh-google-styleguide](https://github.com/zh-google-styleguide/zh-google-styleguide) |
| 锁定提交 | [c1f8ac9138bc](https://github.com/zh-google-styleguide/zh-google-styleguide/commit/c1f8ac9138bce1b829fdffcfa03e8df44584ef22) |
| 提交时间 | 2025-03-15T12:29:23+08:00 |
| 生成器版本 | `google_styleguide@1;engine@12;pandoc@3.1.8` |

> 本指南为 zh-google-styleguide 社区维护的非官方中文译本，内容据 Google Style Guides 原版翻译并转换为 Markdown；原指南文本采用 [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) 许可；原作者、译者及来源信息见各指南前言。

## 目录

- [风格指南](#风格指南)
  - [0. 扉页](#0-扉页)
  - [背景](#背景)
  - [整体样式规则](#整体样式规则)
  - [总体排版规则](#总体排版规则)
  - [整体的元数据规则](#整体的元数据规则)
  - [HTML样式规则](#html样式规则)
  - [HTML格式规则](#html格式规则)
  - [css样式规则](#css样式规则)
  - [CSS格式化规则](#css格式化规则)
  - [CSS元规则](#css元规则)
  - [赠言](#赠言)

---

## 风格指南

### 0. 扉页

原作者

详细作者列表请参见英文原版的 Git 仓库.

翻译

- [Google 开源项目风格指南 - 中文版](https://github.com/zh-google-styleguide/zh-google-styleguide)

项目主页

> - [Google Style Guide](https://google-styleguide.googlecode.com)

### 背景

本文档定义了HTML/CSS的排版以及风格的规则。旨在促进合作编程、提高代码质量并且支持基本的架构。它适用于原生的HTML和CSS文件，包括GSS文件。只要保证代码的整体质量，就可以很容易地使用工具进行混淆、压缩和合并。

### 整体样式规则

#### 协议

嵌入式资源省略协议头。

省略图片、媒体文件、样式表以及脚本的URL协议头部分（http:、https:），不使用这两个协议的文件则不省略。 省略协议头，即让URL变成相对地址，可以避免协议混合及小文件重复下载。

``` html
<!-- 不推荐 -->
<script src="https://www.google.com/js/gweb/analytics/autotrack.js"></script>

<!-- 推荐 -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js"></script>
```

``` css
/* 不推荐 */
.example {
 background: url(https://www.google.com/images/example);
}

/* 推荐 */
.example {
  background: url(//www.google.com/images/example);
}
```

### 总体排版规则

#### 缩进

每次缩进使用两个空格。

不使用TAB键或者混合使用TAB键和空格进行缩进。

``` html
<ul>
 <li>Fantastic
 <li>Great
</ul>
```

``` css
.example {
 color: blue;
}
```

#### 大小写

只使用小写字母。

所有的代码都使用小写字母：适用于HTML元素、属性、属性值（除了text/CDATA）、CSS选择器、属性名以及属性值（字符串除外）。

``` html
<!-- 不推荐 -->
<A HREF="/">Home</A>

<!-- 推荐 -->
<img src="google.png" alt="Google">
```

``` css
/* 不推荐 */
color: #E5E5E5;

/* 推荐 */
color: #e5e5e5;
```

#### 尾部的空格

删除尾部的空格。

尾部的空格是多余的，不删除则形成无意义的文件差异。

``` html
<!-- 不推荐 -->
<p>What?_

<!-- 推荐 -->
<p>Yes please.
```

### 整体的元数据规则

#### 编码

使用UTF-8无BOM编码。

让你的编辑器使用无字节顺序标记的UTF-8编码。

在HTML模板和文档中使用 `<meta charset=”utf-8”>` 指定编码。不需要为样式表指定编码，它默认是UTF-8。

（想了解更多关于应该何时并如何指定编码，请查看 [Handling character encodings in HTML and CSS](https://www.w3.org/International/tutorials/tutorial-char-enc/)）

#### 注释

在需要时尽可能去解释你的代码。

用注释去解释你的代码，包括它的应用范围、用途、此方案的选择理由等。

（这一条是可选的，没必要为每个文件写上详细的注释，会增重HTML/CSS的代码，主要取决于项目的复杂度。）

#### 处理内容

用TODO标记待办事宜和处理内容。

只用TODO来标记待办事宜，不要使用其他格式，例如@@。

在括号里添加联系方式（姓名或邮箱），格式为TODO（联系方式）。

在冒号后面添加处理内容，格式为TODO：处理内容。

``` html
{# TODO(john.doe): 重新处理水平居中 #}
<center>Test</center>

<!-- TODO: 移除可选的标签 -->
<ul>
 <li>Apples</li>
 <li>Oranges</li>
</ul>
```

### HTML样式规则

#### 文档类型

使用HTML5。

HTML5（HTML语法）是所有HTML文档的首选： `<!DOCTYPE html>` 。

（推荐使用HTML，即text/html。不要使用XHTML。XHTML，即 [application/xhtml+xml](https://hixie.ch/advocacy/xhtml)，缺乏浏览器和基础结构的支持，并且优化的空间比HTML小。） 虽然HTML闭合标签没有问题，但是不要自闭合空标签。即写 `<br>` 而不是 `<br />` 。

#### HTML合法性

在可能的情况下使用合法的HTML。

使用合法的HTML代码，除非由于文件大小导致的不可达到的性能目标而不能使用。

利用已用工具对合法性进行测试，例如 [W3C HTML validator](https://validator.w3.org/nu/)。

使用合法的HTML是一个可度量的基准质量属性，该属性有助于了解技术需求和约束，从而确保合理的HTML使用。

``` html
<!-- 不推荐 -->
<title>Test</title>
<article>This is only a test.

<!-- 推荐 -->
<!DOCTYPE html>
<meta charset="utf-8">
<title>Test</title>
<article>This is only a test.</article>
```

#### 语义化

根据HTML的目的使用它。

根据元素（有时被错误的叫做“标签”）被创造的用途使用他们。比如，对标题使用标题元素，对段落使用 `p` 元素，对锚点使用 `a` 元素等。

语义化的使用HTML对于可访问性、复用性和代码的高效性等因素非常重要。

``` html
<!-- 不推荐 -->
<div onclick="goToRecommendations();">All recommendations</div>

<!-- 推荐 -->
<a href="recommendations/">All recommendations</a>
```

#### 多媒体降级

为多媒体提供替代内容。

对于图片、视频、通过 `canvas` 实现的动画等多媒体来说，确保提供可访问的替代内容。对于图片，可提供有意义的替代文本（ `alt` ）；对于视频和音频，如有条件可提供对白和字幕。

提供替代内容对辅助功能很重要：没有 `alt` ，一位盲人用户很难知道一张图片的内容，其他用户可能不能了解视频和音频的内容。 （对于 `alt` 属性会引起冗余的图片和你不打算添加CSS的纯粹装饰性的图片，不用添加替代文本，写成 `alt=""` 即可。）

``` html
<!-- 不推荐 -->
<img src="spreadsheet.png">

<!-- 推荐 -->
<img src="spreadsheet.png" alt="Spreadsheet screenshot.">
```

#### 关注点分离

将结构、表现、行为分离。

严格保持结构（标识），表现（样式），行为（脚本）分离，尽量使三者之间的相互影响最小。

就是说，确保文档和模板只包含HTML，并且HTML只用来表现结构。把任何表现性的东西都移到样式表，任何行为性的东西都移到脚本中。

此外，尽可能少的从文档和模板中引用样式表和脚本来减少三者的相互影响。

结构、表现、行为分离对维护非常重要。更改HTML文档和模板总是比更新样式表和脚本成本更高。

``` html
<!-- 不推荐 -->
<!DOCTYPE html>
<title>HTML sucks</title>
<link rel="stylesheet" href="base.css" media="screen">
<link rel="stylesheet" href="grid.css" media="screen">
<link rel="stylesheet" href="print.css" media="print">
<h1 style="font-size: 1em;">HTML sucks</h1>
<p>I’ve read about this on a few sites but now I’m sure:
  <u>HTML is stupid!!1</u>
<center>I can’t believe there’s no way to control the styling of
  my website without doing everything all over again!</center>

<!-- 推荐 -->
<!DOCTYPE html>
<title>My first CSS-only redesign</title>
<link rel="stylesheet" href="default.css">
<h1>My first CSS-only redesign</h1>
<p>I’ve read about this on a few sites but today I’m actually
  doing it: separating concerns and avoiding anything in the HTML of
  my website that is presentational.
<p>It’s awesome!
```

#### 实体引用

不要使用实体引用。

假设文件、编辑器和团队之间使用相同的编码（UTF-8），则没有必要使用例如 `&mdash;` 、 `&rdquo;` 或 `&#x263a;` 这样的实体引用。

唯一的例外适用于HTML中具有特殊意义的字符（比如\<和&），和控制或者隐藏的字符（比如不换行空格）。

``` html
<!-- 不推荐 -->
The currency symbol for the Euro is &ldquo;&eur;&rdquo;.

<!-- 推荐 -->
The currency symbol for the Euro is "€".
```

#### 可选的标签

省略可选的标签（可选）。

为了优化文件大小和可扫描，考虑省略可选标签。 [HTML5规范](https://www.whatwg.org/specs/web-apps/current-work/multipage/syntax.html#syntax-tag-omission) 定义了哪些标签可以被省略。

（这种方法可能要求一段宽限期去建立一个更加广泛的准则，因为它和Web开发人员通常所了解的有着显著不同。考虑到一致性和简单性，最好省略所有可选标签。）

``` html
<!-- 不推荐 -->
<!DOCTYPE html>
<html>
 <head>
   <title>Spending money, spending bytes</title>
 </head>
 <body>
   <p>Sic.</p>
 </body>
</html>

<!-- 推荐 -->
<!DOCTYPE html>
<title>Saving money, saving bytes</title>
<p>Qed.
```

#### type属性

为样式表和脚本省略 `type` 属性。

引用样式表（除非不是使用CSS）和脚本（除非不是使用JavaScript）不要使用type属性。

HTML5将 [text/css](https://www.whatwg.org/specs/web-apps/current-work/multipage/semantics.html#attr-style-type) 和 [text/javascript](https://www.whatwg.org/specs/web-apps/current-work/multipage/scripting-1.html#attr-script-type) 设置为默认值，在这种情况下指定type属性并不必要。甚至同样兼容老版本的浏览器。

``` html
<!-- 不推荐 -->
<link rel="stylesheet" href="//www.google.com/css/maia.css" type="text/css">

<!-- 推荐 -->
<link rel="stylesheet" href="//www.google.com/css/maia.css">

<!-- 不推荐 -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js" type="text/javascript"></script>

<!-- 推荐 -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js"></script>
```

### HTML格式规则

#### 常规格式化

对每个块、列表、表格元素都另起一行，每个子元素都缩进。

每个块元素、列表元素或表格元素另起一行，而不必考虑元素的样式（因CSS可以改变元素的 `display` 属性）。

同样的，如果他们是块、列表或者表格元素的子元素，则将之缩进。

（如果你遇到列表项之间有空白的问题，可以把所有 `li` 元素放到一行。Linter鼓励抛出警告而不是错误。）

``` html
<blockquote>
  <p><em>Space</em>, the final frontier.</p>
</blockquote>

<ul>
  <li>Moe
  <li>Larry
  <li>Curly
</ul>

<table>
  <thead>
    <tr>
      <th scope="col">Income
      <th scope="col">Taxes
  <tbody>
    <tr>
      <td>$ 5.00
      <td>$ 4.50
</table>
```

#### HTML引号

当引用属性值时，使用双引号。

使用双引号而不是单引号来包裹属性值。

``` html
<!-- 不推荐 -->
<a class='maia-button maia-button-secondary'>Sign in</a>

<!-- 推荐 -->
<a class="maia-button maia-button-secondary">Sign in</a>
```

### css样式规则

#### CSS有效性

尽可能使用有效的CSS。

使用有效的CSS代码，除非在处理css验证器bug或者是专有的语法时。

使用诸如 [W3C CSS validator](https://jigsaw.w3.org/css-validator/) 等工具验证测试。

使用有效的CSS代码是一个可衡量CSS代码质量的指标，可帮你找出不起作用可被删除的CSS代码，从而确保CSS的合理使用。

#### id与class的命名

使用有意义的或者通用的id和class名称

用能反映出元素目的或者通用的id、class名称，代替那些很表象的、难懂的名称。

如果名称需要是易懂的，或不容易被修改，应该首选特定的或者能反映出元素目的的名称。

通用的名称适用于非特殊元素或与兄弟元素无区别的元素。他们常被称为“辅助元素”。

使用功能性或者通用的名称，可减少不必要的文档或者模板变化。

``` css
/* 不推荐：无意义 */
#yee-1901 {}


/* 不推荐：表象 */
.button-green {}
.clear {}

/* 推荐：具体的 */
#gallery {}
#login {}
.video {}

/* 推荐：通用的 */
.aux {}
.alt {}
```

#### id与class的命名规范

ID和class命名要尽可能简短，但必要的话就别怕长。

尽可能简洁地传达id或者class名称的含义。

使用简洁的id或者class名称有助于提高可读性和代码效率。

``` css
/* 不推荐 */
#navigation {}
.atr {}

/* 推荐 */
#nav {}
.author {}
```

#### 选择器的类型

应当避免在id和class前添加类型选择器。

除了必要情况下（例如辅助的类），不要将元素与id或class名称结合做为选择器。

避免不必要的祖先选择器也是出于 [性能原因](https://www.stevesouders.com/blog/2009/06/18/simplifying-css-selectors/) 的考虑。

``` css
/* 不推荐 */
ul#example {}
div.error {}

/* 推荐 */
#example {}
.error {}
```

#### 简写属性

尽可能使用简写的属性书写方式。

CSS提供了多种属性 [简写](https://www.w3.org/TR/CSS21/about.html#shorthand) 的方式（如 `font` ），即使只显式设置一个值，也应该尽可能地使用。

使用简写属性有助于提高代码效率及可读性。

``` css
/* 不推荐 */
border-top-style: none;
font-family: palatino, georgia, serif;
font-size: 100%;
line-height: 1.6;
padding-bottom: 2em;
padding-left: 1em;
padding-right: 1em;
padding-top: 0;

/* 推荐 */
border-top: 0;
font: 100%/1.6 palatino, georgia, serif;
padding: 0 1em 2em;
```

#### 0与单位

省略“0”后的单位。

除非必需，否则0后不要加单位。

``` css
margin: 0;
padding: 0;
```

#### 前导0

省略前导“0”值。

在-1至1之间的值无需保留整数位的0。

``` css
font-size: .8em;
```

#### 十六进制表示法

在可能的情况下使用3个字符的十六进制表示法。

对于可用3字符十六进制表示的颜色值，按此规则书写更短、更简洁。

``` css
/* 不推荐 */
color: #eebbcc;

/* 推荐 */
color: #ebc;
```

#### 前缀选择器

加特定应用前缀（可选）

大型项目中以及嵌入在其它项目或外部网站上的代码需要给id和class添加前缀（命名空间）。使用短的、独特的标识符，并在其后跟一个破折号。 使用命名空间有助于防止命名冲突，可以让维护变得简单，例如在搜索和替换操作时。

``` css
.adw-help {} /* AdWords */
#maia-note {} /* Maia */
```

#### id与class名称分隔符

用连字符分隔ID和类名中的单词。

选择器中的词语和缩写中不要使用除了连字符以外的任何字符（包括空字符），以提高可理解性和可读性。

``` css
/* 不推荐: 单词未分开 */
.demoimage {}

/* 不推荐：使用下划线而不是连字符 */
.error_status {}

/* 推荐 */
#video-id {}
.ads-sample {}
```

#### Hacks

请先尝试其他的方法，避免用户代理检测以及CSS的“hacks”。

进行用户代理检测或使用特殊的CSS选择器及hacks看起来是处理样式差异的捷径。但为了实现和保持高效性以及代码的可维护性，这两种方案应该放到最后考虑。换句话说，用户代理检测和使用hacks会增大项目推进的阻力，所以从项目的长远利益考虑应尽力避免。一旦允许并无顾忌地使用用户代理检测和hacks便很容易滥用，最终一发而不可收。

### CSS格式化规则

#### 声明顺序

按字母顺序排列声明。

css文件书写按字母顺序排列的方式，容易记忆和维护，以达到一致的代码。

在排序时忽略浏览器特定的前缀。但是，特定CSS属性的多个浏览器前缀应按字母顺序排列（如-moz书写在-webkit前面）。

``` css
background: fuchsia;
border: 1px solid;
-moz-border-radius: 4px;
-webkit-border-radius: 4px;
border-radius: 4px;
color: black;
text-align: center;
text-indent: 2em;
```

#### 块内容的缩进

缩进块内容。

将包括嵌套及声明的 [块内容](https://www.w3.org/TR/CSS21/syndata.html#block) 进行缩进，以体现层次并提高可读性。

``` css
@media screen, projection {

  html {
    background: #fff;
    color: #444;
  }

}
```

#### 声明结束

每个属性后使用分号结束。

以分号结束每个属性，提高一致性和可扩展性。

``` css
/* 不推荐 */
.test {
  display: block;
  height: 100px
}

/* 推荐 */
.test {
  display: block;
  height: 100px;
}
```

#### CSS属性名结束

属性名称的冒号后有一个空格。

为保证一致性，在属性名与属性值之间添加一个空格（但是属性名和冒号间没有空格）。

``` css
/* 不推荐 */
h3 {
  font-weight:bold;
}

/* 推荐 */
h3 {
  font-weight: bold;
}
```

#### 声明块间隔

在选择器和后面的声明块之间使用一个空格。

最后一个选择器与表示 [声名块](https://www.w3.org/TR/CSS21/syndata.html#rule-sets) 开始的左大花括号在同行，中间有一个字符空格。

表示开始的左大花括号和选择器在同行。

``` css
/* 不推荐：缺少空间 */
#video{
  margin-top: 1em;
}


/* 不推荐：不必要的换行符 */
#video
{
  margin-top: 1em;
}

/* 推荐 */
#video {
  margin-top: 1em;
}
```

#### 选择器及声明分离

每个选择器和声明独立成行。

总是让每个选择器和声明单独成行。

``` css
/* 不推荐 */
a:focus, a:active {
  position: relative; top: 1px;
}

/* 推荐 */
h1,
h2,
h3 {
  font-weight: normal;
  line-height: 1.2;
}
```

#### CSS代码块分离

使用新空行分离规则。

始终把一个空行（两个换行符）放在代码块规则之间。

``` css
html {
  background: #fff;
}


body {
  margin: auto;
  width: 50%;
}
```

#### CSS引号

属性选择器和属性值中使用单引号。

在属性选择器及属性值中使用单引号（''）而不是双引号（""）。在 `url（）` 中不要使用引号。

特例：如果你确实需要定义 `@charset` ，由于 [不允许使用单引号](https://www.w3.org/TR/CSS21/syndata.html#charset) ，故请使用双引号。

``` css
/* 不推荐 */
@import url("//www.google.com/css/maia.css");

html {
  font-family: "open sans", arial, sans-serif;
}

/* 推荐 */
@import url(//www.google.com/css/maia.css);

html {
  font-family: 'open sans', arial, sans-serif;
}
```

### CSS元规则

#### 分段规则

组的分段由一段注释完成（可选）。

尽可能地用注释来将css分段，段与段之间采用新行。

``` css
/* Header */

#adw-header {}

/* Footer */

#adw-footer {}

/* Gallery */

.adw-gallery {}
```

### 赠言

请与周围保持一致。

如果你正在编辑代码，花几分钟时间看看上下文代码的格式，确定他们的编码风格。如果在上下文代码中，算术运算符前后有空格，或注释前后添加了“#”，你也应该这样做。

编写这个风格指导的目标是让人们可以专注于“我们在讨论什么”而不是“我们该怎么描述”。我们提供了一些通用的编码规范，大家就可以基于这些规范而继续，但特定情况下的规范也同样重要。如果你在一个文件中添加的代码看上去跟其他代码明显不同，你就把阅读此文件的人的节奏打乱了。避免这种情况出现。
