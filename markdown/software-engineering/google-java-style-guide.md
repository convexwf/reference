---
title: "Google Java 风格指南"
authors:
  - "Google Style Guide contributors"
  - "zh-google-styleguide translators"
language: "zh-CN"
tags:
  - "google"
  - "style-guide"
  - "java"
published_at: "2023-09-28"
updated_at: "2025-03-09"
---

# Google Java 风格指南

## 文档信息

| 项目 | 内容 |
| --- | --- |
| 文档标题 | Google Java 风格指南 |
| 文档类型 | zh-CN 整合 Markdown |
| 上游仓库 | [zh-google-styleguide/zh-google-styleguide](https://github.com/zh-google-styleguide/zh-google-styleguide) |
| 锁定提交 | [c1f8ac9138bc](https://github.com/zh-google-styleguide/zh-google-styleguide/commit/c1f8ac9138bce1b829fdffcfa03e8df44584ef22) |
| 提交时间 | 2025-03-15T12:29:23+08:00 |
| 生成器版本 | `google_styleguide@1;engine@12;pandoc@3.1.8` |

> 本指南为 zh-google-styleguide 社区维护的非官方中文译本，内容据 Google Style Guides 原版翻译并转换为 Markdown；原指南文本采用 [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) 许可；原作者、译者及来源信息见各指南前言。

## 目录

- [风格指南](#风格指南)
  - [0. 扉页](#0-扉页)
  - [1. 介绍](#1-介绍)
  - [2. 源文件基础](#2-源文件基础)
  - [3. 源文件结构](#3-源文件结构)
  - [4. 格式](#4-格式)
  - [5. 命名](#5-命名)
  - [6. 编程习惯](#6-编程习惯)
  - [7. Javadoc](#7-javadoc)

---

## 风格指南

### 0. 扉页

原作者
Liam Miller-Cushon
Ted Osborne

详细作者列表请参见英文原版的 Git 仓库.

翻译

项目主页

> - [Google Style Guide](https://google-styleguide.googlecode.com)
> - [Google 开源项目风格指南 - 中文版](https://github.com/zh-google-styleguide/zh-google-styleguide)

### 1. 介绍

本文档是Google的Java™语言的代码风格的 **完整定义** 。只有当Java源文件遵循这里的规则时，才可以说它算遵循了Google的编程风格。

与其他编程风格指南一样，该文档涵盖的问题不仅仅是格式的审美问题，还包括其他类型的约定或代码标准。然而，本文档主要关注的是 **我们普遍遵循的硬性规则** ，并避免提供无法明确执行的建议（无论是对于人还是工具来说）。

#### 1.1. 术语说明

在本文档中，除非另有说明：

- 1.  术语“类”（class）被广泛地用来指代“普通”类、枚举类、接口或注解类型（ `@interface` ）。

- 2.  术语“(类的)成员”（member）被广泛地用来指代嵌套类、字段、方法或构造函数，即除了初始化块和注释之外类的所有顶级内容。

- 3.  术语“注释”（comment）始终指的是实现注释。我们不使用“文档注释”这种说法，而是使用另一常见的说法“Javadoc”代替。

其他的“术语说明”也将在整个文档中偶尔出现。

#### 1.2. 指南说明

此文档中的示例代码 **并不是规范性的** 。也就是说，尽管示例是按照Google风格编写的，但它们可能并不是实现代码的唯一优雅方式。示例中做出的选择性的格式不应被强制作为规则。

### 2. 源文件基础

#### 2.1. 文件名

源文件的文件名由其包含的 `唯一的 <one-top-level>` 顶级类的名称（大小写敏感）加上 `.java` 扩展名构成。

#### 2.2. 文件编码：UTF-8

源文件应使用 **UTF-8** 编码。

#### 2.3. 特殊字符

##### 2.3.1. 空白字符

除了换行符之外，源文件中唯一能够出现的空白字符是 **ASCII的水平空格字符（0x20）** 。这意味着：

- 1.  字符串和字符组成的文本中的所有其他空白字符都应该被转义

- 2.  Tab字符 **不能** 用于缩进

##### 2.3.2 特殊转义序列

对于任何 [有特殊转义序列](https://docs.oracle.com/javase/tutorial/java/data/characters.html) 的字符（ `\b` 、 `\t` 、 `\n` 、 `\f`、 `\r`、 `\"`、 `\'`和 `\\`），应使用以上序列，而不是相应的八进制（例如 `\012`）或Unicode（例如 `\u000a`）转义。

##### 2.3.3. 非ASCII字符

对于其余的非ASCII字符，可以使用实际的Unicode字符（例如 ∞）或等效的Unicode转义（例如 `\u221e`），这只取决于哪种方式使代码 **更容易阅读和理解** ，尽管我们强烈不建议在字符串文本和注释之外使用Unicode转义。

<div class="note">

<div class="title">

Note

</div>

在使用Unicode转义的情况下，即使在偶尔使用实际的Unicode字符的时候，添加一个解释性的注释可能会非常有帮助。

</div>

示例：

<table>
<thead>
<tr class="header">
<th>例子</th>
<th>点评</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<code>String unitAbbrev = "μs";</code>
</blockquote></td>
<td><blockquote>
最佳：即使没有注释也完全清晰明了
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<code>String unitAbbrev = "\u03bcs"; // "μs"</code>
</blockquote></td>
<td><blockquote>
可以，但没有理由这样做
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<code>String unitAbbrev = "\u03bcs"; // Greek letter mu, "s"</code>
</blockquote></td>
<td><blockquote>
可以，但这样不够优雅且容易出错
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<code>String unitAbbrev = "\u03bcs";</code>
</blockquote></td>
<td><blockquote>
差：读者完全不知道这是什么
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<code>return '\ufeff' + content; // byte order mark</code>
</blockquote></td>
<td><blockquote>
好：对不可打印的字符使用转义，并在必要时加上注释
</blockquote></td>
</tr>
</tbody>
</table>

<div class="note">

<div class="title">

Note

</div>

永远不要仅仅因为担心某些程序可能无法正确处理非ASCII字符而去降低代码的可读性。如果真的发生这种情况，那么说明这些程序是有问题的，你应该修复它们。

</div>

### 3. 源文件结构

源文件应由以下部分 **按顺序** 组成：

- 1.  许可或版权信息（如果有的话）

- 2.  包的声明

- 3.  导入语句 （Import statements）

- 4.  有且仅有一个顶级类

每个部分之间用 **一个** 空白行隔开。

#### 3.1. 许可或版权信息（如果有的话）

如果文件中应包含许可证或版权信息，那么它应被放在此处。

#### 3.2. 包声明

包声明 **不换行**。列限制（4.4节，`Column limit: 100 <column-limit>`）不适用于包声明。

#### 3.3. 导入语句

##### 3.3.1. 不使用通配符导入

**不使用** 任何形式的 **通配符导入** ，无论是静态的还是其他形式。

##### 3.3.2. 不换行

导入语句 **不换行** 。列限制（4.4节， `Column limit: 100 <column-limit>` ）不适用于导入语句。

##### 3.3.3. 排序和间距

按以下顺序导入：

- 所有的静态导入都在一个单独的块中。
- 所有非静态导入都在一个单独的块中。

如果既有静态导入又有非静态导入，则两个块之间有一个空白行。导入语句之间没有其他空白行。

在每个块中，导入的名称按ASCII排序顺序出现。（ **注意** ：这不等同于按整个导入语句的ASCII排序，因为'.'排在';'之前。） （译者注：这种情况只会出现在包名结尾为'.'时，所以实际上可以忽略不计。例如： `import packageA.ClassA; import packageA.ClassA.;` ，如果按整个语句的ASCII排序，后句应排在前句之前，因为'.'在ASCII中排在';'前。除此之外其他情况按包名排序和按整个语句排序应得到相同的结果）

##### 3.3.4. 不对类使用静态导入

不使用静态导入来导入静态嵌套类，而是使用常规导入。

#### 3.4. 类的声明

##### 3.4.1. 有且仅有一个顶级类声明

每个顶级类都位于其自己的源文件中。

##### 3.4.2. 类中内容的顺序

类中成员和初始化器的顺序对于代码的可读性有很大影响。然而，并没有一个唯一正确的顺序，不同的类可能会以不同的方式排列其内容。

重要的是，每个类都使用 **某种逻辑顺序** ，并且在被问及时，其维护者可以做出相应的解释。例如，新方法不仅仅是习惯性地添加到类的末尾，因为那会导致内容是“按添加时间排序”的，这并不是一个有逻辑的排序方式。

###### 3.4.2.1. 重载：永不分割

类中拥有同一名称的方法应出现在一个连续的组中，中间不应该有任何其他成员。对于多个构造函数（它们的名称总是相同的）也是如此。即使在方法之间的修饰符（如 `static` 或 `private` ）不同时，此规则仍然适用。

### 4. 格式

**术语说明** ：块状结构指的是类、方法或构造器的主体。注意，根据4.8.3.1节关于 `数组初始化器 <array-initializers>` 的内容，任何数组初始化器都可以选择性地被视为块状结构。

#### 4.1. 花括号

##### 4.1.1. 选择性的花括号的使用

在 `if`、 `else` 、 `for` 、 `do` 和 `while` 语句中，即使主体为空或只包含一个语句，也应该写出花括号。

其他选择性的花括号，比如lambda表达式中的花括号，依然不是必须写出的。

##### 4.1.2. 非空块：K & R 风格

非空块和块状结构中的花括号遵循Kernighan & Ritchie风格（“ [埃及括号](https://www.codinghorror.com/blog/2012/07/new-programming-jargon.html) ”）：

- 在打开花括号之前不换行，除非下面有详细说明。
- 在打开花括号之后换行。
- 在关闭花括号之前换行。
- 仅在该花括号终止一个语句或终止方法、构造器或命名类的主体时，在关闭花括号之后才需要换行。例如，如果花括号后面跟的是 `else` 或逗号，则不换行。

例外：在某些场景下，尽管规则允许你简单地使用一个以分号（ `;` ）结束的语句，但你仍可以在此选择使用一个语句块。在这种情况下，这个语句块开头的花括号前会有一个换行。这种特殊的语句块通常用于限定局部变量的作用范围，例如在switch语句中。

例子：

``` java
return () -> {
    while (condition()) {
        method();
    }
};

return new MyClass() {
    @Override public void method() {
        if (condition()) {
            try {
                something();
            } catch (ProblemException e) {
                recover();
            }
        } else if (otherCondition()) {
            somethingElse();
        } else {
            lastThing();
        }
        {
            int x = foo();
            frob(x);
        }
    }
};
```

关于枚举类的一些例外情况，请参见第4.8.1节, `枚举类 <enum-classes>` 。

##### 4.1.3. 空代码块：应简洁表示

一个空的代码块或类似块的结构可以按照K & R风格（如第4.1.2节 `非空块：K & R风格 <nonempty-blocks>` 所描述）。或者，你也可以在打开后立即关闭它，中间没有字符也不需要换行（即 `{}` ）， **除非** 它是多块语句的一部分（直接包含多个块的语句，例如 `if` / `else` 或 `try` / `catch` / `finally` ）。

例如：

``` java
// 这是可以的
void doNothing() {}

// 这同样也是可以的
void doNothingElse() {
}
```

``` java
// 不可以这样：多块语句中不能出现打开即关闭的简略花括号
try {
    doSomething();
} catch (Exception e) {}
```

#### 4.2. 代码块缩进：增加2个空格

每次打开一个新的代码块或块状结构时，缩进增加两个空格。当块结束时，缩进返回到之前的缩进级别。这种缩进级别同时适用于块中的代码以及注释。（参见第4.1.2节中的示例， `非空块：K & R风格 <nonempty-blocks>` 。）

#### 4.3. 一行一个语句

每个语句后都应换行。

#### 4.4. 列限制：100

Java代码的列限制为100个字符。这里的“字符”指的是任何Unicode码位。除非以下特别说明，任何超出此限制的行都必须换行，如第4.5节 `换行 <line-wrapping>` 中所解释的。

<div class="note">

<div class="title">

Note

</div>

每个Unicode码位都算作一个字符，即使其显示宽度大于或小于一个字符。例如，如果使用 [全角字符](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) ，你可能会选择在此规则严格要求的位置之前就换行。

</div>

例外：

- 在某些情况下，遵循列限制是不可能的（例如，Javadoc中的长URL，或者一个长的JSNI方法引用）。
- 包声明和导入语句（参见第3.2节 `包声明 <package-statement>` 和第3.3节 `导入语句 <import-statements>` ）。
- 注释中可能会被复制并粘贴到shell的中命令行。
- 在极少数情况下需要使用的非常长的标识符是允许超过列限制的。在这种情况下，周围代码的换行方式应遵循 [google-java-format](https://github.com/google/google-java-format) 。

#### 4.5. 换行

**术语说明：** 将可以在一行内书写的代码分成多行的操作被称为换行。

没有全面且确定的公式明确指出在所有情况下如何进换行。很多时候，同一段代码有多种正确的换行方式。

<div class="note">

<div class="title">

Note

</div>

**注意：** 尽管进换行的典型原因是为了避免超过列限制，但实际上在列限制内的代码也可以根据作者的判断进换行。

</div>

<div class="note">

<div class="title">

Note

</div>

**提示：** 有时重构一个方法或定义一个局部变量可以解决超过列限制的问题，而不需要换行。

</div>

##### 4.5.1. 换行的位置

换行的首要准则是：倾向于在 **更高级的句法层次** 进换行。此外：

- 1.  当一行在非赋值运算符处断开时，换行的位置位于符号之前。（注意，这与Google为其他语言所采用的风格不同，如C++和JavaScript。）

  > - 这同样适用于以下"类运算符"的符号：
  >
  >   > - 点分隔符（ `.` ）
  >   > - 方法引用的两个冒号（ `::` ）
  >   > - 类型约束中的与符号（ `<T extends Foo & Bar>` ）
  >   > - catch块中的管道符号（ `catch (FooException | BarException e)` ）

- 2.  当一行在赋值运算符处断开时，换行位置通常位于符号之后，但两种方式都是可以接受的。

  > - 这也适用于增强的 `for` 循环（"foreach"）语句中的"类赋值运算符"————冒号。

- 3.  方法或构造函数的名称应紧挨着其后的左括号（ `(` ）。

- 4.  逗号（ `,` ）应紧挨着它前面的标记。

- 5.  lambda箭头旁绝不换行，但是如果lambda的主体仅由单个未括起来的表达式组成，那么可以紧跟在箭头后面换行。示例：

  > ``` java
  > MyLambda<String, Long, Object> lambda =
  >     (String label, Long value, Object obj) -> {
  >         ...
  >     };
  >
  > Predicate<String> predicate = str ->
  >     longExpressionInvolving(str);
  > ```

<div class="note">

<div class="title">

Note

</div>

**注意：** 换行的主要目的是使代码更清晰，其不一定是行数最少的。

</div>

##### 4.5.2. 行缩进至少4个空格

换行时，第一行之后的每一行（每一个连续的行）至少从原行缩进4个空格。

当有多个连续行时，根据需要，缩进可以在4个空格之外变化。通常，只有当两个连续行从语法上开始于平行的元素时，它们才使用相同的缩进级别。

第4.6.3节关于 `水平对齐 <horizontal-alignment>` 讨论了一种不鼓励使用的做法————用数量变化的空格来使某些标记与前面的行对齐。

#### 4.6. 空白字符

##### 4.6.1. 垂直空白

单个空白行始终应出现在：

- 1.  一个类的连续成员或初始化器之间：字段、构造函数、方法、嵌套类、静态初始化器和实例初始化器。

  > - **例外：** 两个连续字段之间（它们之间没有其他代码）的空白行是可选的。这样的空行一般根据需要用于创建字段的逻辑分组。
  > - **例外：** 枚举常量之间的空白行在 `第4.8.1节 <enum-classes>` 中有描述。

- 2.  此文档的其他部分所要求的（例如第3节， `源文件结构 <source-file-structure>` ，和第3.3节 `导入语句 <import-statements>` ）。

单个空白行也可以出现在任何使用它可以提高代码可读性的位置，例如在语句之间以将代码组织成逻辑子部分。类的第一个成员或初始化器之前，或者最后一个成员或初始化器之后的空白行既不被鼓励也不被反对。

多个连续的空白行是允许的，但从不被要求（或鼓励）。

##### 4.6.2. 水平空白

除了语言或其他风格规则所要求的地方，以及字符串文本、注释和Javadoc之外，单个ASCII空格字符也 **仅** 出现在以下位置。

- 1.  将任何保留字，如 `if` 、 `for` 或 `catch` ，与其后面的左括号（ `(` ）隔开

- 2.  将任何保留字，如 `else` 或 `catch` ，与其前面的右花括号（ `}` ）隔开

- 3.  在任何左花括号（ `{` ）之前，但有两个例外：

  > - `@SomeAnnotation({a, b})` （无空格）
  > - `String[][] x = {{"foo"}};` （根据下面的第9项， `{{` 之间不需要空格）

- 4.  在任何二元或三元运算符的两侧。这也适用于以下的"类运算符"的符号：

  > - 并行类型约束中的与符号： `<T extends Foo & Bar>`
  > - 处理多个异常的catch块中的管道符号： `catch (FooException | BarException e)`
  > - 增强的 `for` （"foreach"）语句中的冒号（ `:` ）
  > - lambda表达式中的箭头： `(String str) -> str.length()`
  >
  > 但不包括：
  >
  > - 方法引用中的两个冒号（ `::` ），正确的写法应类似 `Object::toString`
  > - 点分隔符（ `.` ），正确的写法应类似 `object.toString()`

- 5.  在 `,` 、 `:` 、 `;` 或类型转换的右括号 `)` 之后

- 6.  在代码中任何内容和开始注释的双斜杠 `//` 之间。允许多个空格。

- 7.  在开始注释的双斜杠 `//` 和注释内容之间。允许多个空格。

- 8.  在声明的类型和变量名之间： `List<String> list`

- 9.  在数组初始化器的两个花括号内部（可选）

  > - `new int[] {5, 6}` and `new int[] { 5, 6 }` 都是可行的

- 10. 在类型注解和 `[]` 或 `...` 之间

此规则不应被解读为在行的开始或结束时要求或禁止额外的空格；它只涉及内部空格。

##### 4.6.3. 水平对齐：永远不是必要的

**术语说明：** 水平对齐是指在代码中添加变化数量的额外空格，目的是使某些标记直接出现在前面几行的某些其他标记的下方

这种做法是允许的，但Google风格永远不要求它。即使在已经使用了水平对齐的地方，也不要求保持水平对齐。

以下是一个不使用对齐的例子，然后是一个使用对齐的例子：

``` java
private int x;      // 这样很好
private Color color; // 这也是

private int   x;      // 这是允许的，但未来的编辑
private Color color;  // 可能会使它不再对齐
```

<div class="note">

<div class="title">

Note

</div>

**提示：** 对齐确实可以帮助提高可读性，但它为未来的维护带来了问题。考虑一个将来需要触碰某一行的更改，该更改可能会使之前令人满意的格式变得混乱（当然这种混乱是允许的）。更常见的是，它会促使编码者（也许是你）也调整附近行的空白，可能会触发一系列新的格式化。如此一来，那一行的更改现在就有了一个“爆炸半径”。在最坏的情况下，这可能导致毫无意义的繁忙工作，但即使在最好的情况下，它仍然会破坏版本历史信息，减慢审查者的速度，并加剧合并冲突（merge conflicts）。

</div>

#### 4.7. 分组括号：推荐使用

对于非必须的分组括号，只有当作者和审查者都认为代码在没有它们的情况下不可能被误解，且它们不会使代码更易于阅读时，才能省略它们。假设每个读者都记住了整个Java运算符优先级表是不合理的。

#### 4.8. 具体结构

##### 4.8.1. 枚举类

在枚举常量后面的每个逗号后，换行是可选的。也允许额外的空白行（通常只有一行）。以下是一种可能的写法：

``` java
private enum Answer {
    YES {
        @Override public String toString() {
            return "yes";
        }
    },

    NO,
    MAYBE
}
```

一个没有方法且其常量上没有文档注释的枚举类可以选择按照数组初始化器的格式进行编写（参见4.8.3.1节有关 `数组初始化器 <array-initializers>` 的内容）。

``` java
private enum Suit { CLUBS, HEARTS, SPADES, DIAMONDS }
```

由于枚举类是类，因此编写类的所有其他格式规则都适用于它。

##### 4.8.2. 变量声明

###### 4.8.2.1. 一次只声明一个变量

每个变量声明（字段或局部变量）只声明一个变量：不能使用 `int a, b;` 这样的声明。

**例外：** `for` 循环的头部中，多个变量的声明是可以接受的。

###### 4.8.2.2. 按需声明

局部变量一般不在其所在的块或块状结构的开始处声明。相反，局部变量在首次使用的地方附近（合理范围内）声明，以最小化它们的作用域。局部变量声明时通常会设定其初始值，或在声明后立即进行初始化。

##### 4.8.3. 数组

###### 4.8.3.1. 数组初始化器：可以是“块状”的

任何数组初始化器都可以选择按照“块状结构”的格式进行编写。例如，以下写法都是可以接受的（这里 **并未** 列出所有可行的写法）：

``` java
new int[] {
    0, 1, 2, 3
}

new int[] {
    0, 1,
    2, 3
}

new int[] {
    0,
    1,
    2,
    3
}

new int[]
    {0, 1, 2, 3}
```

###### 4.8.3.2. 不要使用C语言风格的声明

方括号是类型的一部分，而非变量的一部分：正确的写法应该为 `String[] args` ，而不是 `String args[]` 。

##### 4.8.4. switch语句

**术语说明：** 在switch语句块的花括号内有一个或多个语句组。每个语句组由一个或多个switch标签（要么是 `case FOO:` 要么是 `default:` ）组成，后面跟着一个或多个语句（对于最后一个语句组，可能是零个或多个语句）。

###### 4.8.4.1. 缩进

与任何其他块一样，switch块中内容的缩进为2格。

在switch标签后应有一个换行，且缩进级别增加2格，就好像一个块正在被打开一样。接下来的switch标签回到了之前的缩进级别，就好像一个块已经被关闭了一样。

###### 4.8.4.2. 贯穿：需要注释

在switch块内，每个语句组要么突然终止（使用 `break` 、 `continue`、 `return` 或抛出异常），要么用注释标记，以指示执行会或可能继续进入下一个语句组。任何传达贯穿意思的注释都是足够的（通常是 `// fall through` ）。在switch块的最后一个语句组中，不需要这个特殊注释。示例如下

``` java
switch (input) {
    case 1:
    case 2:
        prepareOneOrTwo();
        // fall through
    case 3:
        handleOneTwoOrThree();
        break;
    default:
        handleLargeNumber(input);
}
```

注意单个的switch标签 `case 1` 后面贯穿不需要做任何注释，只有在语句组的最后贯穿才需要注释。

###### 4.8.4.3. 必须要有 `default` 标签

每个switch语句都包括一个default语句组，即使其中不包含任何代码。

**例外：** 对于 `enum` 类的switch语句，如果它明确地包括覆盖该类型的所有可能值的情况，则可以省略 `default` 语句组。如果遗漏了任何可能值，这样做可以让IDE或其他静态分析工具能够发出警告。

##### 4.8.5. 注解

###### 4.8.5.1. 类型注解

应用于类型的注解直接出现在被注解的类型之前。如果注解是用 `@Target(ElementType.TYPE_USE)` 进行元注解的，那么它就是一个类型注解。示例如下：

``` java
final @Nullable String name;

public @Nullable Person getPersonByName(String name)
```

###### 4.8.5.2. 类注解

应用于类的注解紧跟在文档块之后，并且每个注解都列在自己的行上（也就是每行一个注解）。这些换行并不构成换行（见4.5节， `换行 <line-wrapping>`），所以缩进级别不增加。示例如下：

``` java
@Deprecated
@CheckReturnValue
public final class Frozzler { ... }
```

###### 4.8.5.3. 方法/构造函数注解

应用于方法或构造函数的注解的规则和 `上一节 <class-annotations>` 一样。实例如下：

``` java
@Deprecated
@Override
public String getNameIfPresent() { ... }
```

###### 4.8.5.4. 字段注解

应用于字段的注解也紧跟在文档块之后，但在这种情况下，多个注解（可能带参数）可以列在同一行上；例如：

``` java
@Partial @Mock DataLoader loader;
```

###### 4.8.5.5. 参数/局部变量注解

应用于参数或局部变量的注解没有一个具体的编写规则（当然，当注解是类型注解时除外）。

##### 4.8.6. 注释

本节讨论注释的实现。关于Javadoc的内容在第7节 `Javadoc <javadoc>` 中单独讨论。

尽管一行可能只包含注释和空白字符，但由于有注释的存在，它并不被视为一个完全的空白行。

###### 4.8.6.1. 块状注释

块状注释与周围的代码具有相同的缩进级别。它们可以是 `/* ... */` 或者 `// ...` 形式的。对于多行的 `/* ... */` 注释，后续的行必须以 `*` 开始，并且这个 `*` 要与上一行的 `*` 对齐。

``` java
/*
 * This is          // And so           /* Or you can
 * okay.            // is this.          * even do this. */
 */
```

注释不应被星号或其他字符所构成的框框起来。

<div class="note">

<div class="title">

Note

</div>

**提示：** 当编写多行注释时，如果你希望在必要时,自动的代码格式化工具能重新调整行的格式（段落样式），你应该使用 `/* ... */` 形式。大多数格式化工具不会重新调整 `// ...` 形式的注释块中的行。

</div>

##### 4.8.7. 修饰符

当存在类和成员的修饰符时，它们出现的顺序应遵循Java语言规范推荐的顺序：

``` java
public protected private abstract default static final transient volatile synchronized native strictfp
```

##### 4.8.8. 数值字面量

长整型（ `long` 类型）字面量使用大写的 `L` 作为后缀，而绝不能使用小写的（以避免与数字 `1` 混淆）。例如，应写为 `3000000000L` 而非 `3000000000l`。

### 5. 命名

#### 5.1. 所有标识符通用的规则

标识符只使用ASCII字母、数字以及在下面提到的极少数情况中才会使用的下划线。因此，每个有效的标识符名称都应与正则表达式 `\w+` 匹配。

在Google风格中， **不** 使用特殊的前缀或后缀。例如，以下都不是Google风格的命名： `name_` ， `mName` ， `s_name` 和 `kName` 。

#### 5.2. 不同类型标识符的规则

##### 5.2.1. 包名

包名只使用小写字母和数字（不使用下划线）。连续的单词直接连接在一起。例如 `com.example.deepspace` ，而不是 `com.example.deepSpace` 或 `com.example.deep_space` 。

##### 5.2.2. 类名

类名使用 `大驼峰命名法（UpperCamelCase） <camel-case>` 。

类名通常是名词或名词短语。例如 `Character` 、 `ImmutableList` 。接口名称也可能是名词或名词短语（例如 `List` ），但有时可能是形容词或形容词短语（例如 `Readable` ）。

对于注解的命名，至今还没有具体的规则，甚至也没有任何不成文的规定。

测试类的名称以 `Test` 结尾，例如， `HashIntegrationTest` 。如果它覆盖一个单一的类，其名称是该类的名称后加上 `Test`，例如 `HashImplTest` 。

##### 5.2.3. 方法名

方法名使用 `小驼峰命名法（lowerCamelCase） <camel-case>` 。

方法名通常是动词或动词短语。例如 `sendMessage` 、 `stop` 。

在JUnit测试方法名中，可以使用下划线来分隔名称的逻辑组件，每个组件都使用 `小驼峰命名法 <camel-case>` 编写，例如 `transferMoney_deductsFromSource` 。命名测试方法没有唯一正确的方式。

##### 5.2.4. 常量字段名

常量名使用 `UPPER_SNAKE_CASE` （大蛇式）：全部为大写字母，每个单词之间用单个下划线分隔。但是，什么才算是一个常量呢？

常量是指那些由 `static final` 修饰的字段，其内容是深度不可变（译者注：指该对象以及其内部所有可能的引用或对象都是不可变的，与“浅层不可变”相对）的，且其方法不会产生可检测到的副作用。例子包括基本数据类型、字符串、不可变的值类和设置为 `null` 的任何东西。如果实例的任何可观察状态可以被改变，那它就不是一个常量。仅有不改变对象的意图是不够的。例如：

``` java
// Constants
static final int NUMBER = 5;
static final ImmutableList<String> NAMES = ImmutableList.of("Ed", "Ann");
static final Map<String, Integer> AGES = ImmutableMap.of("Ed", 35, "Ann", 32);
static final Joiner COMMA_JOINER = Joiner.on(','); // because Joiner is immutable
static final SomeMutableType[] EMPTY_ARRAY = {};

// Not constants
static String nonFinal = "non-final";
final String nonStatic = "non-static";
static final Set<String> mutableCollection = new HashSet<String>();
static final ImmutableSet<SomeMutableType> mutableElements = ImmutableSet.of(mutable);
static final ImmutableMap<String, SomeMutableType> mutableValues =
    ImmutableMap.of("Ed", mutableInstance, "Ann", mutableInstance2);
static final Logger logger = Logger.getLogger(MyClass.getName());
static final String[] nonEmptyArray = {"these", "can", "change"};
```

常量名通常是名词或名词短语。

##### 5.2.5. 非常量字段名

非常量字段名，无论其是否为静态的，都使用 `小驼峰命名法 <camel-case>` 格式编写。

非常量字段名通常是名词或名词短语。例如， `computedValues` 或 `index` 。

##### 5.2.6. 参数名

参数名使用 `小驼峰命名法 <camel-case>` 格式编写。

公共（ `public`）方法中应避免使用单字符参数名。

##### 5.2.7. 局部变量名

局部变量名使用 `小驼峰命名法 <camel-case>` 格式编写。

即使是 final 且不可变的，局部变量也不被视为常量，因此不应按常量的风格命名。

##### 5.2.8. 类型变量名

每个类型变量的命名方式有两种：

- 单个大写字母，后面可选择性地跟一个数字（如 `E` , `T` , `X` , `T2` ）
- 按照类的命名方式命名（参见第5.2.2节，`类名 <class-names>`），然后跟一个大写字母 `T` （例如： `RequestT` , `FooBarT` ）。

#### 5.3. 驼峰命名法：明确规定

有时将英文短语转换为驼峰命名有多种合理的方式，例如当存在缩略词或如"IPv6"或"iOS"这样不寻常的结构时。为了提高可预测性，Google风格指定了以下的（几乎）明确的规定。

从名称的口头表达开始：

- 1.  将短语转换为纯ASCII并去除所有的撇号。例如，“Müller's algorithm”可能变为“Muellers algorithm”。

- 2.  将这个结果分割为单词，以空格和任何剩余的标点符号（通常是连字符）为分隔。

  > - 推荐：如果任何单词在常见用法中已经有一个传统的驼峰命名形式，那么将其分割成其组成部分（例如，"AdWords"变为"ad words"）。注意，像"iOS"这样的单词并不真的是驼峰命名，实际上它违反了任何惯例，所以这个建议不再适用。

- 3.  现在将所有内容（包括缩略词）全部转为小写，然后只将：

  > - ... 每个单词的第一个字母大写，得到大驼峰命名，或
  > - ... 除第一个单词外的每个单词的第一个字母大写，得到小驼峰命名

- 4.  最后，将所有的单词连接成一个标识符。

注意，原始单词的大小写几乎完全被忽略。示例：

<table>
<thead>
<tr class="header">
<th>口头表达</th>
<th>正确形式</th>
<th>错误形式</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
"XML HTTP request"
</blockquote></td>
<td><blockquote>
<code>XmlHttpRequest</code>
</blockquote></td>
<td><blockquote>
<code>XMLHTTPRequest</code>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
"new customer ID"
</blockquote></td>
<td><blockquote>
<code>newCustomerId</code>
</blockquote></td>
<td><blockquote>
<code>newCustomerID</code>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
"inner stopwatch"
</blockquote></td>
<td><blockquote>
<code>innerStopwatch</code>
</blockquote></td>
<td><blockquote>
<code>innerStopWatch</code>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
"supports IPv6 on iOS?" "YouTube importer"
</blockquote></td>
<td><blockquote>
<code>supportsIpv6OnIos</code> <code>YouTubeImporter</code> 、 <code>YoutubeImporter</code> *
</blockquote></td>
<td><blockquote>
<code>supportsIPv6OnIOS</code>
</blockquote></td>
</tr>
</tbody>
</table>

\*可以接受，但不推荐。

<div class="note">

<div class="title">

Note

</div>

**注意：** 在英文中，有些单词的连字符使用是模糊的：例如，“nonempty”和“non-empty”都是正确的，因此方法名 `checkNonempty` 和 `checkNonEmpty` 同样都是正确的。

</div>

### 6. 编程习惯

#### 6.1 `@Override` ：始终使用

只要合法，方法就应使用 `@Override` 注解进行标记。这包括一个类方法覆盖一个超类方法，一个类方法实现一个接口方法，以及一个接口方法重新指定一个超接口方法的情况。

**例外：** 当父方法被 `@Deprecated` 标记时，可以省略 `@Override` 。

#### 6.2. 捕获的异常：不应忽略

除了以下特别提到的情况，响应捕获的异常时什么也不做是非常少见的做法。（典型的响应是记录它，或者如果认为它是"不可能的"则将其重新抛出为 `AssertionError` 。）

当在 `catch` 块中确实合适地不采取任何行动时，应在注释中解释这样做的原因。

``` java
try {
    int i = Integer.parseInt(response);
    return handleNumericResponse(i);
} catch (NumberFormatException ok) {
    // it's not numeric; that's fine, just continue
}
return handleTextResponse(response);
```

**例外：** 在测试中，如果捕获的异常的名称是或以 `expected` 开头的，则可以在不进行注释的情况下忽略它。以下是一个确保测试中的代码抛出预期类型的异常的非常常见的习语，所以这里不需要注释。

``` java
try {
    emptyStack.pop();
    fail();
} catch (NoSuchElementException expected) {
}
```

#### 6.3. 静态成员：使用类名进行限定

当必须对静态类成员进行限定时，应使用该类的名称进行限定，而不是使用该类的类型引用或表达式进行限定。

``` java
Foo aFoo = ...;
Foo.aStaticMethod(); // 好
aFoo.aStaticMethod(); // 差
somethingThatYieldsAFoo().aStaticMethod(); // 非常差
```

#### 6.4. 析构方法：不使用

重写 `Object.finalize` 方法是 **极其罕见** 的。

<div class="note">

<div class="title">

Note

</div>

**提示：** 不要这样做。如果你确实必须这样做，首先仔细阅读并理解 [《Effective Java》第8条](https://www.google.com/search?hl=zh-CN&tbo=p&tbm=bks&q=isbn:0134686047) ："避免使用析构方法和清理器"，然后还是不要这样做。

</div>

### 7. Javadoc

#### 7.1. 格式

##### 7.1.1. 一般形式

Javadoc块的基本格式如下例所示：

``` java
/**
 * 这里写了多行Javadoc文本,
 * 像通常一样包裹起来...
 */
public int method(String p1) { ... }
```

或者如以下的单行示例所示：

``` java
/** 一段特别短的Javadoc文本。 */
```

基本格式始终是可以接受的。当整个Javadoc块（包括注释标记）可以放在一行时，可以使用单行格式。注意，这只适用于没有块标签（如 `@return` ）的情况。

##### 7.1.2. 段落

在段落之间，以及在存在的块标签组之前，有一个空白行————也就是说，一个只包含对齐的前导星号（ `*` ）的行。除了第一个段落，每个段落在第一个单词之前都有 `` ，其后没有空格。其他块级元素的HTML标签，如 `<ul>` 或 `<table>`，前面不加 `` 。

##### 7.1.3. 块标签

使用的任何标准“块标签”都按照 `@param` 、 `@return` 、 `@throws` 、 `@deprecated` 的顺序出现，这四种类型的标签的描述永远不会为空。当一个块标签不能放在一行上时，续行缩进4个（或更多）空格从 `@` 的位置开始。

#### 7.2. 摘要片段

每个Javadoc块都以一个简短的摘要片段开始。这个片段非常重要：它是在某些上下文中出现的唯一部分，如类和方法索引。

这应该是一个片段—————一个名词短语或动词短语，而不是一个完整的句子。它不是以 `A {@code Foo} is a...` 或 `This method returns...` 开头的，也不形成像 `Save the record.` 这样的完整祈使句。然而，这个片段就像是一个完整的句子一样需要首字母大写和相应的标点符号。

<div class="note">

<div class="title">

Note

</div>

**提示：** 一个常见的错误是以这种形式编写简单的Javadoc： `/** @return the customer ID */` 。这是不正确的，应该改为 `/** Returns the customer ID. */` 。

</div>

#### 7.3. Javadoc的使用位置

至少每一个 `public` 类以及这样的类中的每一个 `public` 或 `protected` 的成员都有Javadoc，除了下文中提到的一些例外。

如第7.3.4节 `非必需的Javadoc <non-required-javadoc>` 所述，还可能存在其他的Javadoc内容。

##### 7.3.1. 例外：不言自明的成员

对于简单且一目了然的成员，如 `getFoo()` ，在确实没有其他值得一提的内容的情况下，Javadoc是可选的，只需说明"Returns the foo"即可。

<div class="note">

<div class="title">

Note

</div>

**重要：** 如果某些典型的读者需要知道的相关信息被省略了，那么不适合用这个例外来为省略文档的错误做法辩护。例如，对于一个名为 `getCanonicalName` 的方法，如果读者很可能不知道"canonical name"是什么意思，那么不要省略其文档（以这里只需要说明 `/** Returns the canonical name. */` 为借口，但实际这里的成员名并非一目了然）！

</div>

##### 7.3.2. 例外：重写

当一个方法重写超类型的方法时，不必总是在该方法上附带Javadoc。

##### 7.3.4. 非必需的Javadoc（译者注：原文中并没有7.3.3节）

其他类和成员可根据需要或作者意愿添加Javadoc。

每当需要使用实现注释来定义类或成员的总体目的或行为时，该注释应以Javadoc的形式编写（使用 `/**` ）。

非必需的Javadoc并不严格要求遵循第7.1.1、7.1.2、7.1.3和7.2节的格式规则，尽管这样做当然是推荐的。
