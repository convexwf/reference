---
title: "Google JavaScript 风格指南"
authors:
  - "Google Style Guide contributors"
  - "zh-google-styleguide translators"
language: "zh-CN"
tags:
  - "google"
  - "style-guide"
  - "javascript"
published_at: "2013-09-25"
updated_at: "2024-12-08"
---

# Google JavaScript 风格指南

## 文档信息

| 项目 | 内容 |
| --- | --- |
| 文档标题 | Google JavaScript 风格指南 |
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
  - [Javascript语言规范](#javascript语言规范)
  - [Javascript风格规范](#javascript风格规范)

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

在Google的开源项目中，JavaScript是最主要的客户端脚本语言。本指南是使用JavaScript时建议和不建议做法的清单。

### Javascript语言规范

#### var关键字

总是用 `var` 关键字定义变量。

##### 描述

如果不显式使用 `var` 关键字定义变量，变量会进入到全局上下文中，可能会和已有的变量发生冲突。另外，如果不使用var声明，很难说变量存在的作用域是哪个（可能在局部作用域里，也可能在document或者window上）。所以，要一直使用 `var` 关键字定义变量。

#### 常量

- 使用字母全部大写（如 `NAMES_LIKE_THIS` ）的方式命名
- 可以使用 `@const` 来标记一个常量 *指针* （指向变量或属性，自身不可变）
- 由于IE的兼容问题，不要使用 [const关键字](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const?redirectlocale=en-US&redirectslug=JavaScript%2FReference%2FStatements%2Fconst)

##### 描述

###### 常量值

如果一个值是恒定的，它命名中的字母要全部大写（如 `CONSTANT_VALUE_CASE` ）。字母全部大写意味着这个值不可以被改写。

原始类型（ `number` 、 `string` 、 `boolean` ）是常量值。

对象的表现会更主观一些，当它们没有暴露出变化的时候，应该认为它们是常量。但是这个不是由编译器决定的。

###### 常量指针（变量和属性）

用 `@const` 注释的变量和属性意味着它是不能更改的。使用const关键字可以保证在编译的时候保持一致。使用 [const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const?redirectlocale=en-US&redirectslug=JavaScript%2FReference%2FStatements%2Fconst) 效果相同，但是由于IE的兼容问题，我们不使用const关键字。

另外，不应该修改用 `@const` 注释的方法。

###### 例子

注意， `@const` 不一定是常量值，但命名类似 `CONSTANT_VALUE_CASE` 的 *一定* 是常量指针。

    /**
    * 以毫秒为单位的超时时长
    * @type {number}
    */
    goog.example.TIMEOUT_IN_MILLISECONDS = 60;

1分钟60秒永远也不会改变，这是个常量。全部大写的命名意味其为常量值，所以它不能被重写。 开源的编译器允许这个符号被重写，这是因为 *没有* `@const` 标记。

    /**
    * Map of URL to response string.
    * @const
    */
    MyClass.fetchedUrlCache_ = new goog.structs.Map();

在这个例子中，指针没有变过，但是值却是可以变化的，所以这里用了驼峰式的命名，而不是全部大写的命名。

#### 分号

一定要使用分号。

依靠语句间隐式的分割，可能会造成细微的调试的问题，千万不要这样做。

很多时候不写分号是很危险的：

    // 1.
    MyClass.prototype.myMethod = function() {
        return 42;
    }  // 这里没有分号.

    (function() {
        // 一些局部作用域中的初始化代码
    })();

    var x = {
        'i': 1,
        'j': 2
    }  //没有分号.

    // 2.  试着在IE和firefox下做一样的事情.
    //没人会这样写代码，别管他.
    [normalVersion, ffVersion][isIE]();

    var THINGS_TO_EAT = [apples, oysters, sprayOnCheese]  //这里没有分号

    // 3. 条件语句
    -1 == resultOfOperation() || die();

##### 发生了什么？

1.  js错误。返回42的函数运行了，因为后面有一对括号，而且传入的参数是一个方法，然后返回的42被调用，导致出错了。
2.  你可能会得到一个“no sush property in undefined”的错误，因为在执行的时候，解释器将会尝试执行 `x[normalVersion, ffVersion][isIE]()` 这个方法。
3.  `die` 这个方法只有在 `resultOfOperation()` 是 `NaN` 的时候执行，并且 `THINGS_TO_EAT` 将会被赋值为 `die()` 的结果。

##### 为什么？

js语句要求以分号结尾，除非能够正确地推断分号的位置。在这个例子当中，函数声明、对象和数组字面量被写在了一个语句当中。右括号（")"、"}"、"\]"）不足以证明这条语句已经结束了，如果下一个字符是运算符或者"("、"{"、"\["，js将不会结束语句。

这个错误让人震惊，所以一定要确保用分号结束语句。

##### 澄清：分号和函数

函数表达式后面要分号结束，但是函数声明就不需要。例如：

    var foo = function() {
        return true;
    };  // 这里要分号

    function foo() {
        return true;
    }  // 这里不用分号

#### 嵌套函数

可以使用。

嵌套函数非常有用，比如在创建持续任务或者隐藏工具方法的时候。可以放心的使用。

#### 块内函数声明

不要使用块内函数声明。

不要这样做：

    if (x) {
        function foo() {}
    }

虽然大多数脚本引擎支持功能区块内声明，但ECMAScript并未认可（见 [ECMA-262](https://www.ecma-international.org/publications/standards/Ecma-262.htm) ，第13条和第14）。若与他人的及EcmaScript所建议的不一致，即可视为不好的实现方式。ECMAScript只允许函数声明语句列表, 在根语句列表脚本或者函数。相反，使用一个变量初始化函数表达式在块内定义一个函数块：

    if (x) {
        var foo = function() {}
    }

#### 异常

可以抛出异常。

如果你做一些比较复杂的项目你基本上无法避免异常，比如使用一个应用程序开发框架。可以大胆试一试。

#### 自定义异常

可以自定义异常。

如果没有自定义异常，返回的错误信息来自一个有返回值的函数是难处理的，是不雅的。坏的解决方案包括传递引用的类型来保存错误信息或总是返回有一个潜在的错误成员的对象。这些基本上为原始的异常处理hack。在适当的时候使用自定义的异常。

#### 标准功能

总是优先于非标准功能。

为了最大的可移植性和兼容性，总是使用标准功能而不是非标准功能（例如，采用 <span class="title-ref">string.charAt(3)</span> 而非 <span class="title-ref">string\[3\]</span> ，用DOM的功能访问元素而不是使用特定于一个具体应用的简写）。

#### 原始类型的包装对象

没有理由使用原始类型的包装对象，更何况他们是危险的：

    var x = new Boolean(false);
    if (x) {
        alert('hi');  //显示“hi”。
    }

不要这样做！

然而类型转换是可以的。

    var x = Boolean(0);
    if (x) {
        alert('hi');  //永远都不显示。
    }
    typeof Boolean(0) == 'boolean';
    typeof new Boolean(0) == 'object';

这是非常有用的进行数字、字符串和布尔值转换的方式。

#### 多重的原型继承

不可取。

多重原型继承是Javascript实现继承的方式。如果你有一个以用户定义的class B作为原型的用户自定义class D，则得到多重原型继承。这样的继承出现容易但难以正确创造！

出于这个原因，最好是使用 [Closure库](https://developers.google.com/closure/library/?csw=1) 中的 `goog.inherits()` 或类似的东西。

    function D() {
        goog.base(this)
    }
    goog.inherits( D, B );

    D.prototype.method =function() {
        ...
    };

#### 方法和属性定义

`/**构造函数*/ function SomeConstructor() { this.someProperty = 1; } Foo.prototype.someMethod = function() { ... };`

虽然有多种使用“new”关键词来创建对象方法和属性的途径，首选的创建方法的途径是：

    Foo.prototype.bar = function() {
        /* ... */
    };

其他特性的首选创建方式是在构造函数中初始化字段：

    /** @constructor */
    function Foo() {
        this.bar = value;
    }

##### 为什么？

当前的JavaScript引擎优化基于一个对象的“形状”， [给对象添加一个属性（包括覆盖原型设置的值）改变了形式，会降低性能](https://developers.google.com/v8/design#prop_access) 。

#### 删除

请使用 `this.foo = null` 。

    o.prototype.dispose = function() {
        this.property_ = null;
    };

而不是：

    Foo.prototype.dispose = function() {
        delete his.property_;
    };

在现代的JavaScript引擎中，改变一个对象属性的数量比重新分配值慢得多。应该避免删除关键字，除非有必要从一个对象的迭代的关键字列表删除一个属性，或改变 `if (key in obj)` 结果。

#### 闭包

可以使用，但是要小心。

创建闭包可能是JS最有用的和经常被忽视的功能。在 [这里](https://jibbering.com/faq/notes/closures/) 很好地描述说明了闭包的工作。

要记住的一件事情，一个闭包的指针指向包含它的范围。因此，附加一个闭包的DOM元素，可以创建一个循环引用，所以，内存会泄漏。例如，下面的代码：

    function foo(element, a, b) {
        element.onclick = function() { /* 使用 a 和 b */ };
    }

闭包能保持元素a和b的引用即使它从未使用。因为元素还保持对闭包的一个引用，我们有一个循环引用，不会被垃圾收集清理。在这些情况下，代码的结构可以如下：

    function foo(element, a, b) {
        element.onclick = bar(a, b);
    }

    function bar(a, b) {
        return function() { /* 使用 a 和 b */ }
    }

#### eval()函数

只用于反序列化（如评估RPC响应）。

若用于 `eval()` 的字符串含有用户输入，则 `eval()` 会造成混乱的语义，使用它有风险。通常有一个更好 更清晰、更安全的方式来编写你的代码，所以一般是不会允许其使用的。然而，eval相对比非eval使反序列化更容易，因此它的使用是可以接受的（例如评估RPC响应）。

反序列化是将一系列字节存到内存中的数据结构转化过程。例如，你可能会写的对象是：

    users = [
        {
            name: 'Eric',
            id: 37824,
            email: 'jellyvore@myway.com'
        },
        {
            name: 'xtof',
            id: 31337,
            email: 'b4d455h4x0r@google.com'
        },
        ...
    ];

将这些数据读入内存跟得出文件的字符串表示形式一样容易。

同样， `eval()` 函数可以简化解码RPC的返回值。例如，您可以使用 `XMLHttpRequest` 生成RPC，在响应时服务器返回JavaScript：

    var userOnline = false;
    var user = 'nusrat';
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', 'https://chat.google.com/isUserOnline?user=' + user, false);
    xmlhttp.send('');
    // 服务器返回：
    // userOnline = true;
    if (xmlhttp.status == 200) {
          eval(xmlhttp.responseText);
    }
    // userOnline 现在为 true

#### with()

不建议使用。

使用 `with` 会影响程序的语义。因为 `with` 的目标对象可能会含有和局部变量冲突的属性，使你程序的语义发生很大的变化。例如，这是做什么用？

    with (foo) {
        var x = 3;
        return x;
    }

答案：什么都有可能。局部变量 `x` 可能会被 `foo` 的一个属性覆盖，它甚至可能有setter方法，在此情况下将其赋值为3可能会执行很多其他代码。不要使用 `with` 。

#### this

只在构造函数对象、方法，和创建闭包的时候使用。

`this` 的语义可能会非常诡异。有时它指向全局对象（很多时候）、调用者的作用域链（在 `eval` 里）、DOM树的一个节点（当使用HTML属性来做为事件句柄时）、新创建的对象（在一个构造函数中）、或者其他的对象（如果函数被 `call()` 或 `apply()` 方式调用）。

正因为 `this` 很容易被弄错，故将其使用限制在以下必须的地方：

- 在构造函数中
- 在对象的方法中（包括闭包的创建）

#### for-in 循环

只使用在对象、映射、哈希的键值迭代中。

`for-in` 循环经常被不正确的用在元素数组的循环中。由于并不是从 `0` 到 `length-1` 进行循环，而是遍历对象中和它原型链上的所有的键，所以很容易出错。这里有一些失败的例子：

    function printArray(arr) {
        for (var key in arr) {
            print(arr[key]);
        }
    }

    printArray([0,1,2,3]);  //这样可以

    var a = new Array(10);
    printArray(a);  //这样不行

    a = document.getElementsByTagName('*');
    printArray(a);  //这样不行

    a = [0,1,2,3];
    a.buhu = 'wine';
    printArray(a);  //这样不行

    a = new Array;
    a[3] = 3;
    printArray(a);  //这样不行

在数组循环时常用的一般方式：

    function printArray(arr) {
        var l = arr.length;
        for (var i = 0; i < l; i++) {
            print(arr[i]);
        }
    }

#### 关联数组

不要将映射，哈希，关联数组当作一般数组来使用。

不允许使用关联数组……确切的说在数组，你不可以使用非数字的索引。如果你需要一个映射或者哈希，在这种情况下你应该使用对象来代替数组，因为在功能上你真正需要的是对象的特性而不是数组的。

数组仅仅是用来拓展对象的（像在JS中你曾经使用过的 `Date` 、 `RegExp` 和 `String` 对象一样的）。

#### 多行的字符串字面量

不要使用。

不要这样做：

    var myString = 'A rather long string of English text, an error message \
                  actually that just keeps going and going -- an error \
                  message to make the Energizer bunny blush (right through \
                  those Schwarzenegger shades)! Where was I? Oh yes, \
                  you\'ve got an error and all the extraneous whitespace is \
                  just gravy.  Have a nice day.';

在编译时每一行头部的空白符不会被安全地去除掉；斜线后的空格也会导致棘手的问题；虽然大部分脚本引擎都会支持，但是它不是ECMAScript规范的一部分。

使用字符串连接来代替：

    var myString = 'A rather long string of English text, an error message ' +
       'actually that just keeps going and going -- an error ' +
       'message to make the Energizer bunny blush (right through ' +
       'those Schwarzenegger shades)! Where was I? Oh yes, ' +
       'you\'ve got an error and all the extraneous whitespace is ' +
       'just gravy.  Have a nice day.';

#### 数组和对象字面量

建议使用。

使用数组和对象字面量来代替数组和对象构造函数。

数组构造函数容易在参数上出错。

    // 长度为3
    var a1 = new Array(x1, x2, x3);

    // 长度为 2
    var a2 = new Array(x1, x2);

    // If x1 is a number and it is a natural number the length will be x1.
    // If x1 is a number but not a natural number this will throw an exception.
    // Otherwise the array will have one element with x1 as its value.
    var a3 = new Array(x1);

    // 长度为0
    var a4 = new Array();

由此，如果有人将代码从2个参数变成了一个参数，那么这个数组就会有一个错误的长度。

为了避免这种怪异的情况，永远使用可读性更好的数组字面量。

    var a = [x1, x2, x3];
    var a2 = [x1, x2];
    var a3 = [x1];
    var a4 = [];

对象构造函数虽然没有相同的问题，但是对于可读性和一致性，还是应该使用对象字面量。

    var o = new Object();

    var o2 = new Object();
    o2.a = 0;
    o2.b = 1;
    o2.c = 2;
    o2['strange key'] = 3;

应该写成：

    var o = {};

    var o2 = {
        a: 0,
        b: 1,
        c: 2,
        'strange key': 3
    };

#### 修改内置对象原型

不建议。

强烈禁止修改如 `Object.prototype` 和 `Array.prototype` 等对象的原型。修改其他内置原型如 `Function.prototype` 危险性较小，但在生产环境中还是会引发一些难以调试的问题，也应当避免。

#### Internet Explorer中的条件注释

不要使用。

不要这样做：

    var f = function () {
        /*@cc_on if (@_jscript) { return 2* @*/  3; /*@ } @*/
    };

条件注释会在运行时改变JavaScript语法树，阻碍自动化工具。

### Javascript风格规范

#### 命名

通常来说，使用 `functionNamesLikeThis` ， `variableNamesLikeThis` ， `ClassNamesLikeThis` ， `EnumNamesLikeThis` ， `methodNamesLikeThis` ， `CONSTANT_VALUES_LIKE_THIS` ， `foo.namespaceNamesLikeThis.bar` 和 `filenameslikethis.js` 这种格式的命名方式。

##### 属性和方法

- *私有* 属性和方法应该以下划线开头命名。
- *保护* 属性和方法应该以无下划线开头命名（像公共属性和方法一样）。

了解更多关于私有成员和保护成员的信息，请阅读 [可见性](https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Visibility__private_and_protected_fields_) 部分。

##### 方法和函数参数

可选函数参数以 `opt_` 开头。

参数数目可变的函数应该具有以 `var_args` 命名的最后一个参数。你可能不会在代码里引用 `var_args` ；使用 `arguments` 对象。

可选参数和数目可变的参数也可以在注释 `@param` 中指定。尽管这两种惯例都被编译器接受，但更加推荐两者一起使用。

##### getter和setter

EcmaScript 5 不鼓励使用属性的getter和setter。然而，如果使用它们，那么getter就不要改变属性的可见状态。

    /**
    *错误--不要这样做.
    */
    var foo = { get next() { return this.nextId++; } };
    };

##### 存取函数

属性的getter和setter方法不是必需的。然而，如果使用它们，那么读取方法必须以 `getFoo()` 命名，并且写入方法必须以 `setFoo(value)` 命名。（对于布尔型的读取方法，也可以使用 `isFoo()` ，并且这样往往听起来更自然。）

##### 命名空间

JavaScript没有原生的对封装和命名空间的支持。

全局命名冲突难以调试，并且当两个项目尝试整合的时候可能引起棘手的问题。为了能共享共用的JavaScript代码，我们采用一些约定来避免冲突。

###### 为全局代码使用命名空间

在全局范围内 *总是* 使用唯一的项目或库相关的伪命名空间进行前缀标识。如果你正在进行“Project Sloth”项目，一个合理的伪命名空间为 `sloth.*` 。

    var sloth = {};

    sloth.sleep = function() {
      ...
    };

很多JavaScript库，包括 [the Closure Library](https://developers.google.com/closure/library/?csw=1) 和 [Dojo toolkit](https://dojotoolkit.org/) 给你高级功能来声明命名空间。保持你的命名空间声明一致。

    goog.provide('sloth');

    sloth.sleep = function() {
      ...
    };

###### 尊重命名空间所有权

当选择一个子命名空间的时候，确保父命名空间知道你在做什么。如果你开始了一个为sloths创建hats的项目，确保Sloth这一组命名空间知道你在使用 `sloth.hats` 。

###### 外部代码和内部代码使用不同的命名空间

“外部代码”指的是来自你的代码库外并独立编译的代码。内部名称和外部名称应该严格区分开。如果你正在使用一个能调用 `foo.hats.*` 中的东西的外部库，你的内部代码不应该定义 `foo.hats.*` 中的所有符号，因为如果其他团队定义新符号就会把它打破。

    foo.require('foo.hats');
    /**
    *错误--不要这样做。
    * @constructor
    * @extends {foo.hats.RoundHat}
    */
    foo.hats.BowlerHat = function() {
    };

如果你在外部命名空间中需要定义新的API，那么你应该明确地导出且仅导出公共的API函数。为了一致性和编译器更好的优化你的内部代码，你的内部代码应该使用内部API的内部名称调用它们。

    foo.provide('googleyhats.BowlerHat');

    foo.require('foo.hats');
    /**
    * @constructor
    * @extends {foo.hats.RoundHat}
    */
    googleyhats.BowlerHat = function() {
      ...
    };
    goog.exportSymbol('foo.hats.BowlerHat', googleyhats.BowlerHat);

###### 为长类型的名称提供别名提高可读性

如果对完全合格的类型使用本地别名可以提高可读性，那么就这样做。本地别名的名称应该符合类型的最后一部分。

    /**
    * @constructor
    */
    some.long.namespace.MyClass = function() {
    };

    /**
    * @param {some.long.namespace.MyClass} a
    */
    some.long.namespace.MyClass.staticHelper = function(a) {
      ...
    };

    myapp.main = function() {
      var MyClass = some.long.namespace.MyClass;
      var staticHelper = some.long.namespace.MyClass.staticHelper;
      staticHelper(new MyClass());
    };

不要为命名空间起本地别名。命名空间应该只能使用 [goog.scope](https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#goog-scope) 命名别名。

    myapp.main = function() {
      var namespace = some.long.namespace;
      namespace.MyClass.staticHelper(new namespace.MyClass());
    };

避免访问一个别名类型的属性，除非它是一个枚举。

    /** @enum {string} */
    some.long.namespace.Fruit = {
      APPLE: 'a',
      BANANA: 'b'
    };

    myapp.main = function() {
      var Fruit = some.long.namespace.Fruit;
      switch (fruit) {
        case Fruit.APPLE:
          ...
        case Fruit.BANANA:
          ...
      }
    };

    myapp.main = function() {
      var MyClass = some.long.namespace.MyClass;
      MyClass.staticHelper(null);
    };

永远不要在全局环境中创建别名。只在函数体内使用它们。

##### 文件名

为了避免在大小写敏感的平台上引起混淆，文件名应该小写。文件名应该以 `.js` 结尾，并且应该不包含除了 `-` 或 `_` （相比较 `_` 更推荐 `-` ）以外的其它标点。

#### 自定义 toString() 方法

必须确保无误，并且无其他副作用。

你可以通过自定义 `toString()` 方法来控制对象如何字符串化他们自己。这没问题，但是你必须确保你的方法执行无误，并且无其他副作用。如果你的方法没有达到这个要求，就会很容易产生严重的问题。比如，如果 `toString()` 方法调用一个方法产生一个断言，断言可能要输出对象的名称，就又需要调用 `toString()` 方法。

#### 延时初始化

可以使用。

并不总在变量声明的地方就进行变量初始化，所以延时初始化是可行的。

#### 明确作用域

时常。

经常使用明确的作用域加强可移植性和清晰度。例如，在作用域链中不要依赖 `window` 。你可能想在其他应用中使用你的函数，这时此 `window` 就非彼 `window` 了。

#### 代码格式

我们原则上遵循 [C++格式规范](https://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Formatting) ，并且进行以下额外的说明。

##### 大括号

由于隐含分号的插入，无论大括号括起来的是什么，总是在同一行上开始你的大括号。例如：

    if (something) {
      // ...
    } else {
      // …
    }

##### 数组和对象初始化表达式

当单行数组和对象初始化表达式可以在一行写开时，写成单行是允许的。

    var arr = [1, 2, 3];  //之后无空格[或之前]
    var obj = {a: 1, b: 2, c: 3};  //之后无空格[或之前]

多行数组和对象初始化表达式缩进两个空格，括号的处理就像块一样单独成行。

    //对象初始化表达式
    var inset = {
      top: 10,
      right: 20,
      bottom: 15,
      left: 12
    };

    //数组初始化表达式
    this.rows_ = [
      '"Slartibartfast" <fjordmaster@magrathea.com>',
      '"Zaphod Beeblebrox" <theprez@universe.gov>',
      '"Ford Prefect" <ford@theguide.com>',
      '"Arthur Dent" <has.no.tea@gmail.com>',
      '"Marvin the Paranoid Android" <marv@googlemail.com>',
      'the.mice@magrathea.com'
    ];

    //在方法调用中使用
    goog.dom.createDom(goog.dom.TagName.DIV, {
      id: 'foo',
      className: 'some-css-class',
      style: 'display:none'
    }, 'Hello, world!');

长标识符或值在对齐的初始化列表中存在问题，所以初始化值不必对齐。例如：

    CORRECT_Object.prototype = {
      a: 0,
      b: 1,
      lengthyName: 2
    };

不要像这样：

    WRONG_Object.prototype = {
      a          : 0,
      b          : 1,
      lengthyName: 2
    };

##### 函数参数

如果可能，应该在同一行上列出所有函数参数。如果这样做将超出每行80个字符的限制，参数必须以一种可读性较好的方式进行换行。为了节省空间，在每一行你可以尽可能的接近80个字符，或者把每一个参数单独放在一行以提高可读性。缩进可能是四个空格，或者和括号对齐。下面是最常见的参数换行形式：

    // 四个空格，每行包括80个字符。适用于非常长的函数名，
    // 重命名不需要重新缩进，占用空间小。
    goog.foo.bar.doThingThatIsVeryDifficultToExplain = function(
        veryDescriptiveArgumentNumberOne, veryDescriptiveArgumentTwo,
        tableModelEventHandlerProxy, artichokeDescriptorAdapterIterator) {
        // ...
    };

    //四个空格，每行一个参数。适用于长函数名，
    // 允许重命名，并且强调每一个参数。
    goog.foo.bar.doThingThatIsVeryDifficultToExplain = function(
        veryDescriptiveArgumentNumberOne,
        veryDescriptiveArgumentTwo,
        tableModelEventHandlerProxy,
        artichokeDescriptorAdapterIterator) {
        // ...
    };

    // 缩进和括号对齐，每行80字符。 看上去是分组的参数，
    // 占用空间小。
    function foo(veryDescriptiveArgumentNumberOne, veryDescriptiveArgumentTwo,
                tableModelEventHandlerProxy, artichokeDescriptorAdapterIterator) {
        // ...
    }

    // 和括号对齐，每行一个参数。看上去是分组的并且
    // 强调每个单独的参数。
    function bar(veryDescriptiveArgumentNumberOne,
                veryDescriptiveArgumentTwo,
                tableModelEventHandlerProxy,
                artichokeDescriptorAdapterIterator) {
        // ...
    }

当函数调用本身缩进，你可以自由地开始相对于原始声明的开头或者相对于当前函数调用的开头，进行4个空格的缩进。以下都是可接受的缩进风格。

    if (veryLongFunctionNameA(
            veryLongArgumentName) ||
        veryLongFunctionNameB(
        veryLongArgumentName)) {
      veryLongFunctionNameC(veryLongFunctionNameD(
          veryLongFunctioNameE(
              veryLongFunctionNameF)));
    }

##### 匿名函数传递

当在一个函数的参数列表中声明一个匿名函数时，函数体应该与声明的左边缘缩进两个空格，或者与function关键字的左边缘缩进两个空格。这是为了匿名函数体更加可读（即不被挤在屏幕的右侧）。

    prefix.something.reallyLongFunctionName('whatever', function(a1, a2) {
      if (a1.equals(a2)) {
        someOtherLongFunctionName(a1);
      } else {
        andNowForSomethingCompletelyDifferent(a2.parrot);
      }
    });

    var names = prefix.something.myExcellentMapFunction(
        verboselyNamedCollectionOfItems,
        function(item) {
          return item.name;
        });

##### 使用goog.scope命名别名

[goog.scope](https://docs.google.com/document/d/1ETFAuh2kaXMVL-vafUYhaWlhl6b5D9TOvboVg7Zl68Y/pub) 可用于在使用 [the Closure Library](https://developers.google.com/closure/library/?csw=1) 的工程中缩短命名空间的符号引用。

每个文件只能添加一个 `goog.scope` 调用。始终将它放在全局范围内。

开放的 `goog.scope(function() {` 调用必须在之前有一个空行，并且紧跟 `goog.provide` 声明、 `goog.require` 声明或者顶层的注释。调用必须在文件的最后一行闭合。在scope声明闭合处追加 `// goog.scope` 。注释与分号间隔两个空格。

和C++命名空间相似，不要在 `goog.scope` 声明下面缩进。相反，从第0列开始。

只取不会重新分配给另一个对象（例如大多数的构造函数、枚举和命名空间）的别名。不要这样做：

    goog.scope(function() {
    var Button = goog.ui.Button;

    Button = function() { ... };
    ...

别名必须和全局中的命名的最后一个属性相同。

    goog.provide('my.module');

    goog.require('goog.dom');
    goog.require('goog.ui.Button');

    goog.scope(function() {
    var Button = goog.ui.Button;
    var dom = goog.dom;

    // Alias new types after the constructor declaration.
    my.module.SomeType = function() { ... };
    var SomeType = my.module.SomeType;

    // Declare methods on the prototype as usual:
    SomeType.prototype.findButton = function() {
      // Button as aliased above.
      this.button = new Button(dom.getElement('my-button'));
    };
    ...
    });  // goog.scope

##### 更多的缩进

事实上，除了 [初始化数组和对象](https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Array_and_Object_literals) 和传递匿名函数外，所有被拆开的多行文本应与之前的表达式左对齐，或者以4个（而不是2个）空格作为一缩进层次。

    someWonderfulHtml = '' +
                        getEvenMoreHtml(someReallyInterestingValues, moreValues,
                                        evenMoreParams, 'a duck', true, 72,
                                        slightlyMoreMonkeys(0xfff)) +
                        '';

    thisIsAVeryLongVariableName =
        hereIsAnEvenLongerOtherFunctionNameThatWillNotFitOnPrevLine();

    thisIsAVeryLongVariableName = 'expressionPartOne' + someMethodThatIsLong() +
        thisIsAnEvenLongerOtherFunctionNameThatCannotBeIndentedMore();

    someValue = this.foo(
        shortArg,
        'Some really long string arg - this is a pretty common case, actually.',
        shorty2,
        this.bar());

    if (searchableCollection(allYourStuff).contains(theStuffYouWant) &&
        !ambientNotification.isActive() && (client.isAmbientSupported() ||
                                            client.alwaysTryAmbientAnyways())) {
      ambientNotification.activate();
    }

##### 空行

使用新的空行来划分一组逻辑上相关联的代码片段。例如：

    doSomethingTo(x);
    doSomethingElseTo(x);
    andThen(x);

    nowDoSomethingWith(y);

    andNowWith(z);

##### 二元和三元操作符

操作符始终跟随着前行, 这样你就不用顾虑分号的隐式插入问题。否则换行符和缩进还是遵循其他谷歌规范指南。

    var x = a ? b : c;  // All on one line if it will fit.

    // Indentation +4 is OK.
    var y = a ?
        longButSimpleOperandB : longButSimpleOperandC;

    // Indenting to the line position of the first operand is also OK.
    var z = a ?
            moreComplicatedB :
            moreComplicatedC;

点号也应如此处理。

    var x = foo.bar().
        doSomething().
        doSomethingElse();

#### 括号

只用在有需要的地方。

通常只在语法或者语义需要的地方有节制地使用。

绝对不要对一元运算符如 `delete` 、 `typeof` 和 `void` 使用括号或者在关键词如 `return` 、 `throw` 和其他的（ `case` 、 `in` 或者 `new` ）之后使用括号。

#### 字符串

使用 `'` 代替 `"` 。

使用单引号（ `'` ）代替双引号（ `"` ）来保证一致性。当我们创建包含有HTML的字符串时这样做很有帮助。

    var msg = 'This is some HTML';

#### 可见性（私有和保护类型字段）

鼓励使用 `@private` 和 `@protected` JSDoc注释。

我们建议使用JSDoc注释 `@private` 和 `@protected` 来标识出类、函数和属性的可见程度。

设置 `--jscomp_warning=visibility` 可令编译器对可见性的违规进行编译器警告。可见 [封闭的编译器警告](https://code.google.com/p/closure-compiler/wiki/Warnings) 。

加了 `@private` 标记的全局变量和函数只能被同一文件中的代码所访问。

被标记为 `@private` 的构造函数只能被同一文件中的代码或者它们的静态和实例成员实例化。 `@private` 标记的构造函数可以被相同文件内它们的公共静态属性和 `instanceof` 运算符访问。

全局变量、函数和构造函数不能注释 `@protected` 。

    // 文件1
    // AA_PrivateClass_ 和 AA_init_ 是全局的并且在同一个文件中所以能被访问

    /**
    * @private
    * @constructor
    */
    AA_PrivateClass_ = function() {
    };

    /** @private */
    function AA_init_() {
      return new AA_PrivateClass_();
    }

    AA_init_();

标记 `@private` 的属性可以被同一文件中的所有的代码访问，如果属性属于一个类，那么所有自身含有属性的类的静态方法和实例方法也可访问。它们不能被不同文件下的子类访问或者重写。

标记 `@protected` 的属性可以被同一文件中的所有的代码访问，任何含有属性的子类的静态方法和实例方法也可访问。

注意这些语义和C++、JAVA中private 和 protected的不同，其许可同一文件中的所有代码访问的权限，而不是仅仅局限于同一类或者同一类层次。此外，不像C++中，子类不可重写私有属性。

    // File 1.

    /** @constructor */
    AA_PublicClass = function() {
      /** @private */
      this.privateProp_ = 2;

      /** @protected */
      this.protectedProp = 4;
    };

    /** @private */
    AA_PublicClass.staticPrivateProp_ = 1;

    /** @protected */
    AA_PublicClass.staticProtectedProp = 31;

    /** @private */
    AA_PublicClass.prototype.privateMethod_ = function() {};

    /** @protected */
    AA_PublicClass.prototype.protectedMethod = function() {};

    // File 2.

    /**
    * @return {number} The number of ducks we've arranged in a row.
    */
    AA_PublicClass.prototype.method = function() {
      // Legal accesses of these two properties.
      return this.privateProp_ + AA_PublicClass.staticPrivateProp_;
    };

    // File 3.

    /**
    * @constructor
    * @extends {AA_PublicClass}
    */
    AA_SubClass = function() {
      // Legal access of a protected static property.
      AA_PublicClass.staticProtectedProp = this.method();
    };
    goog.inherits(AA_SubClass, AA_PublicClass);

    /**
    * @return {number} The number of ducks we've arranged in a row.
    */
    AA_SubClass.prototype.method = function() {
      // Legal access of a protected instance property.
      return this.protectedProp;
    };

注意在Javascript中，一个类（如 `AA_PrivateClass_` ）和其构造函数类型是没有区别的。没办法确定一种类型是public而它的构造函数是private。（因为构造函数很容易重命名从而躲避隐私检查）。

#### JavaScript类型

鼓励和强制执行的编译器。

JSDoc记录类型时，要尽可能具体和准确。我们支持的类型是基于 [EcmaScript 4规范](https://wiki.ecmascript.org/doku.php?id=spec:spec) 。

##### JavaScript类型语言

ES4提案包含指定JavaScript类型的语言。我们使用JsDoc这种语言表达函数参数和返回值的类型。

随着ES4提议的发展，这种语言已经改变了。编译器仍然支持旧的语法类型，但这些语法已经被弃用了。

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 31%" />
<col style="width: 52%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>语法名称</th>
<th>语法</th>
<th>描述</th>
<th>弃用语法</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>原始类型</td>
<td>在JavaScript中有5种原始类型： <code>{null}</code> ， <code>{undefined}</code> ， <code>{boolean}</code> ， <code>{number}</code> ，和 <code>{string}</code></td>
<td>类型的名称。</td>
<td></td>
</tr>
<tr class="even">
<td>实例类型</td>
<td><code>{Object}</code> 实例对象或空。
<code>{Function}</code> 一个实例函数或空。
<code>{EventTarget}</code> 构造函数实现的EventTarget接口，或者为null的一个实例。</td>
<td>一个实例构造函数或接口函数。构造函数是 <code>@constructor</code> JSDoc标记定义的函数 。接口函数是 <code>@interface</code> JSDoc标记定义的函数。
默认情况下，实例类型将接受空。这是唯一的类型语法，使得类型为空。此表中的其他类型的语法不会接受空。</td>
<td></td>
</tr>
<tr class="odd">
<td>枚举类型</td>
<td><code>{goog.events.EventType}</code> 字面量初始化对象的属性之一 <code>goog.events.EventType</code> 。</td>
<td>一个枚举必须被初始化为一个字面量对象，或作为另一个枚举的别名,加注 <code>@enum</code> JSDoc标记。这个属性是枚举实例。 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#enums">下面</a> 是枚举语法的定义。
请注意，这是我们的类型系统中为数不多的ES4规范以外的事情之一。</td>
<td></td>
</tr>
<tr class="even">
<td>应用类型</td>
<td><code>{Array.&lt;string&gt;}</code> 字符串数组。
<code>{Object.&lt;string, number&gt;}</code> 一个对象，其中键是字符串，值是数字。</td>
<td>参数化类型，该类型应用一组参数类型。这个想法是类似于Java泛型。</td>
<td></td>
</tr>
<tr class="odd">
<td>联合类型</td>
<td><code>{(number|boolean)}</code> 一个数字或布尔值。</td>
<td>表明一个值可能有A型或B型。
括号在顶层表达式可以省略，但在子表达式不能省略，以避免歧义。
<code>{number|boolean}</code>
<code>{function(): (number|boolean)}</code></td>
<td><code>{(number,boolean)}</code> ， <code>{(number||boolean)}</code></td>
</tr>
<tr class="even">
<td>可为空的类型</td>
<td><code>{?number}</code>
一个数字或空。</td>
<td>空类型与任意其他类型组合的简称。这仅仅是语法糖（syntactic sugar）。</td>
<td><code>{number?}</code></td>
</tr>
<tr class="odd">
<td>非空类型</td>
<td><code>{!Object}</code>
一个对象，值非空。</td>
<td>从非空类型中过滤掉null。最常用于实例类型，默认可为空。</td>
<td><code>{Object!}</code></td>
</tr>
<tr class="even">
<td>记录类型</td>
<td><code>{{myNum: number, myObject}}</code>
给定成员类型的匿名类型。</td>
<td>表示该值有指定的类型的成员。在这种情况下， <code>myNum</code> 是 <code>number</code> 类型而 <code>myObject</code> 可为任何类型。
注意花括号是语法类型的一部分。例如，表示一个数组对象有一个 <code>length</code> 属性，你可以写 <code>Array.&lt;{length}&gt;</code> 。</td>
<td></td>
</tr>
<tr class="odd">
<td>函数类型</td>
<td><code>{function(string, boolean)}</code>
一个函数接受两个参数（一个字符串和一个布尔值），并拥有一个未知的返回值。</td>
<td>指定一个函数。</td>
<td></td>
</tr>
<tr class="even">
<td>函数返回类型</td>
<td><code>{function(): number}</code>
一个函数没有参数并返回一个数字。</td>
<td>指定函数的返回类型。</td>
<td></td>
</tr>
<tr class="odd">
<td>函数 <code>this</code> 类型</td>
<td><code>{function(this:goog.ui.Menu, string)}</code>
一个需要一个参数（字符串）的函数，执行上下文是 <code>goog.ui.Menu</code></td>
<td>指定函数类型的上下文类型。</td>
<td></td>
</tr>
<tr class="even">
<td>函数 <code>new</code> 类型</td>
<td><code>{function(new:goog.ui.Menu, string)}</code>
一个构造函数接受一个参数（一个字符串），并在使用“new”关键字时创建一个 <code>goog.ui.Menu</code> 新实例。</td>
<td>指定构造函数所构造的类型。</td>
<td></td>
</tr>
<tr class="odd">
<td>可变参数</td>
<td><code>{function(string, ...[number]): number}</code>
一个函数，它接受一个参数（一个字符串），然后一个可变数目的参数，必须是数字。</td>
<td>指定函数的变量参数。</td>
<td></td>
</tr>
<tr class="even">
<td>可变参数（ <code>@param</code> 注释）</td>
<td><code>@param {...number} var_args</code>
带注释函数的可变数目参数。</td>
<td>指定带注释函数接受一个可变数目的参数。</td>
<td></td>
</tr>
<tr class="odd">
<td>函数 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#optional">可选参数</a></td>
<td><code>{function(?string=, number=)}</code>
一个函数，它接受一个可选的、可以为空的字符串和一个可选的数字作为参数。“=”只用于函数类型声明。</td>
<td>指定函数的可选参数。</td>
<td></td>
</tr>
<tr class="even">
<td>函数 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#optional">可选参数</a> （ <code>@param</code> 注释）</td>
<td><code>@param {number=} opt_argument</code>
<code>number</code> 类型的可选参数。</td>
<td>指定带注释函数接受一个可选的参数。</td>
<td></td>
</tr>
<tr class="odd">
<td>所有类型</td>
<td><code>{*}</code></td>
<td>表明该变量可以接受任何类型。</td>
<td></td>
</tr>
<tr class="even">
<td>未知类型</td>
<td><code>{?}</code></td>
<td>表明该变量可以接受任何类型，编译器不应该检查其类型。</td>
<td></td>
</tr>
</tbody>
</table>

##### JavaScript中的类型

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>类型举例</th>
<th>取值举例</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>number</td>
<td><pre><code>1
1.0
-5
1e5
Math.PI</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td>Number</td>
<td><pre><code>new Number(true)</code></pre></td>
<td><a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Wrapper_objects_for_primitive_types">Number对象</a></td>
</tr>
<tr class="odd">
<td>string</td>
<td><pre><code>&#39;Hello&#39;
&quot;World&quot;
String(42)</code></pre></td>
<td>字符串</td>
</tr>
<tr class="even">
<td>String</td>
<td><pre><code>new String(&#39;Hello&#39;)
new String(42)</code></pre></td>
<td><a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Wrapper_objects_for_primitive_types">String对象</a></td>
</tr>
<tr class="odd">
<td>boolean</td>
<td><pre><code>true
false
Boolean(0)</code></pre></td>
<td>Boolean值</td>
</tr>
<tr class="even">
<td>Boolean</td>
<td><pre><code>new Boolean(true)</code></pre></td>
<td><a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Wrapper_objects_for_primitive_types">Boolean对象</a></td>
</tr>
<tr class="odd">
<td>RegExp</td>
<td><pre><code>new RegExp(&#39;hello&#39;)
/world/g</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td>Date</td>
<td><pre><code>new Date
new Date()</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td>null</td>
<td><pre><code>null</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td>undefined</td>
<td><pre><code>undefined</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td>void</td>
<td><pre><code>function f() {
  return;
}</code></pre></td>
<td>没有返回值</td>
</tr>
<tr class="even">
<td>Array</td>
<td><pre><code>[&#39;foo&#39;, 0.3, null]
[]</code></pre></td>
<td>无类型数组</td>
</tr>
<tr class="odd">
<td>Array.&lt;number&gt;</td>
<td><pre><code>[11, 22, 33]</code></pre></td>
<td>数字数组</td>
</tr>
<tr class="even">
<td>Array.&lt;Array.&lt;string&gt;&gt;</td>
<td><pre><code>[[&#39;one&#39;, &#39;two&#39;, &#39;three&#39;], [&#39;foo&#39;, &#39;bar&#39;]]</code></pre></td>
<td>以字符串为元素的数组，作为另一个数组的元素</td>
</tr>
<tr class="odd">
<td>Object</td>
<td><pre><code>{}
{foo: &#39;abc&#39;, bar: 123, baz: null}</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td>Object.&lt;string&gt;</td>
<td><pre><code>{&#39;foo&#39;: &#39;bar&#39;}</code></pre></td>
<td>值为字符串的对象</td>
</tr>
<tr class="odd">
<td>Object.&lt;number, string&gt;</td>
<td><pre><code>var obj = {};
obj[1] = &#39;bar&#39;;</code></pre></td>
<td>键为整数，值为字符串的对象。 注意，js当中键总是会隐式转换为字符串。所以 <code>obj['1'] == obj[1]</code> 。键在for…in…循环中，总是字符串类型。但在对象中索引时编译器会验证键的类型。</td>
</tr>
<tr class="even">
<td>Function</td>
<td><pre><code>function(x, y) {
  return x * y;
}</code></pre></td>
<td><a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Wrapper_objects_for_primitive_types">Function对象</a></td>
</tr>
<tr class="odd">
<td>function(number, number): number</td>
<td><pre><code>function(x, y) {
  return x * y;
}</code></pre></td>
<td>函数值</td>
</tr>
<tr class="even">
<td>类</td>
<td><pre><code>/** @constructor */
function SomeClass() {}
&#10;new SomeClass();</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td>接口</td>
<td><pre><code>/** @interface */
function SomeInterface() {}
&#10;SomeInterface.prototype.draw = function() {};</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td>project.MyClass</td>
<td><pre><code>/** @constructor */
project.MyClass = function () {}
&#10;new project.MyClass()</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td>project.MyEnum</td>
<td><pre><code>/** @enum {string} */
project.MyEnum = {
  /** The color blue. */
  BLUE: &#39;#0000dd&#39;,
  /** The color red. */
  RED: &#39;#dd0000&#39;
};</code></pre></td>
<td>枚举
JSDoc中枚举的值都是可选的.</td>
</tr>
<tr class="even">
<td>Element</td>
<td><pre><code>document.createElement(&#39;div&#39;)</code></pre></td>
<td>DOM元素</td>
</tr>
<tr class="odd">
<td>Node</td>
<td><pre><code>document.body.firstChild</code></pre></td>
<td>DOM节点</td>
</tr>
<tr class="even">
<td>HTMLInputElement</td>
<td><pre><code>htmlDocument.getElementsByTagName(&#39;input&#39;)[0]</code></pre></td>
<td>指明类型的DOM元素</td>
</tr>
</tbody>
</table>

##### 类型转换

在类型检测不准确的情况下，有可能需要添加类型的注释，并且把类型转换的表达式写在括号里，括号是必须的。如：

    /** @type {number} */ (x)

##### 可为空与可选的参数和属性

因为Javascript是一个弱类型的语言，明白函数参数、类属性的可选、可为空和未定义之间的细微差别是非常重要的。

对象类型和引用类型默认可为空。如以下表达式：

    /**
    * 传入值初始化的类
    * @param {Object} value某个值
    * @constructor
    */
    function MyClass(value) {
      /**
       * Some value.
       * @type {Object}
       * @private
       */
      this.myValue_ = value;
    }

告诉编译器 `myValue_` 属性为一对象或null。如果 `myValue_` 永远都不会为null, 就应该如下声明:

    /**
    * 传入非null值初始化的类
    * @param {!Object} value某个值
    * @constructor
    */
    function MyClass(value) {
      /**
       * Some value.
       * @type {!Object}
       * @private
       */
      this.myValue_ = value;
    }

这样，如果编译器可以识别出 `MyClass` 初始化传入值为null，就会发出一个警告。

函数的可选参数在运行时可能会是undefined，所以如果他们是类的属性，那么必须声明：

    /**
    * 传入可选值初始化的类
    * @param {Object=} opt_value某个值（可选）
    * @constructor
    */
    function MyClass(opt_value) {
      /**
       * Some value.
       * @type {Object|undefined}
       * @private
       */
      this.myValue_ = opt_value;
    }

这告诉编译器 `myValue_` 可能是一个对象，或 `null` ，或 `undefined` 。

注意: 可选参数 `opt_value` 被声明成 `{Object=}` ，而不是 `{Object|undefined}` 。这是因为可选参数可能是undefined。虽然直接写undefined也并无害处，但鉴于可阅读性还是写成上述的样子。

最后，属性的可为空和可选并不矛盾，下面的四种声明各不相同：

    /**
    * 接受四个参数，两个可为空，两个可选
    * @param {!Object} nonNull 必不为null
    * @param {Object} mayBeNull 可为null
    * @param {!Object=} opt_nonNull 可选但必不为null
    * @param {Object=} opt_mayBeNull 可选可为null
    */
    function strangeButTrue(nonNull, mayBeNull, opt_nonNull, opt_mayBeNull) {
      // ...
    };

##### 类型定义

有时类型可以变得复杂。一个函数，它接受一个元素的内容可能看起来像：

    /**
    * @param {string} tagName
    * @param {(string|Element|Text|Array.<Element>|Array.<Text>)} contents
    * @return {!Element}
    */
    goog.createElement = function(tagName, contents) {
      ...
    };

你可以定义带 `@typedef` 标记的常用类型表达式。例如：

    /** @typedef {(string|Element|Text|Array.<Element>|Array.<Text>)} */
    goog.ElementContent;

    /**
    * @param {string} tagName
    * @param {goog.ElementContent} contents
    * @return {!Element}
    */
    goog.createElement = function(tagName, contents) {
    ...
    };

##### 模板类型

编译器对模板类型提供有限支持。它只能从字面上通过 `this` 参数的类型和 `this` 参数是否丢失推断匿名函数的 `this` 类型。

    /**
    * @param {function(this:T, ...)} fn
    * @param {T} thisObj
    * @param {...*} var_args
    * @template T
    */
    goog.bind = function(fn, thisObj, var_args) {
    ...
    };
    //可能出现属性丢失警告
    goog.bind(function() { this.someProperty; }, new SomeClass());
    //出现this未定义警告
    goog.bind(function() { this.someProperty; });

#### 注释

使用JSDoc。

我们使用 [c++的注释风格](https://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Comments) 。 所有的文件、类、方法和属性都应该用合适的 [JSDoc](https://code.google.com/p/jsdoc-toolkit/) 的 [标签](https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#JSDoc_Tag_Reference) 和 [类型](https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#JsTypes) 注释。除了直观的方法名称和参数名称外，方法的描述、方法的参数以及方法的返回值也要包含进去。

行内注释应该使用 `//` 的形式。

为了避免出现语句片段，要使用正确的大写单词开头，并使用正确的标点符号作为结束。

##### 注释语法

JSDoc的语法基于 [JavaDoc](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html) ，许多编译工具从JSDoc注释中获取信息从而进行代码验证和优化，所以这些注释必须符合语法规则。

    /**
    * A JSDoc comment should begin with a slash and 2 asterisks.
    * Inline tags should be enclosed in braces like {@code this}.
    * @desc Block tags should always start on their own line.
    */

##### JSDoc 缩进

如果你不得不进行换行，那么你应该像在代码里那样，使用四个空格进行缩进。

    /**
    * Illustrates line wrapping for long param/return descriptions.
    * @param {string} foo This is a param with a description too long to fit in
    *     one line.
    * @return {number} This returns something that has a description too long to
    *     fit in one line.
    */
    project.MyClass.prototype.method = function(foo) {
      return 5;
    };

不必在 `@fileoverview` 标记中使用缩进。

虽然不建议，但依然可以对描述文字进行排版。

    /**
    * This is NOT the preferred indentation method.
    * @param {string} foo This is a param with a description too long to fit in
    *                     one line.
    * @return {number} This returns something that has a description too long to
    *                  fit in one line.
    */
    project.MyClass.prototype.method = function(foo) {
      return 5;
    };

##### JSDoc中的HTML

像JavaDoc一样, JSDoc 支持很多的HTML标签，像 `<code>` ， `<pre>` ， `<tt>` ， `**` ， `<ul>` ， `<ol>` ， `<li>` ， `<a>` 等。

这就意味着不建议采用纯文本的格式。所以，不要在JSDoc里使用空白符进行格式化。

    /**
    * Computes weight based on three factors:
    *  items sent
    *  items received
    *  last timestamp
    */

上面的注释会变成这样：

    Computes weight based on three factors: items sent items received items received last timestamp

所以，用下面的方式代替：

    /**
    * Computes weight based on three factors:
    * <ul>
    * <li>items sent
    * <li>items received
    * <li>last timestamp
    * </ul>
    */

[JavaDoc](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html) 风格指南对于如何编写良好的doc注释是非常有帮助的。

##### 顶层/文件层注释

[版权声明](https://google-styleguide.googlecode.com/svn/trunk/copyright.html) 和作者信息是可选的。顶层注释的目的是为了让不熟悉代码的读者了解文件中有什么。它需要描述文件内容，依赖关系以及兼容性的信息。例如：

    /**
    * @fileoverview Description of file, its uses and information
    * about its dependencies.
    */

##### Class评论

类必须记录说明与描述和 [一个类型的标签](https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#constructor-tag) ，标识的构造函数。类必须加以描述，若是构造函数则需标注出。

    /**
    * Class making something fun and easy.
    * @param {string} arg1 An argument that makes this more interesting.
    * @param {Array.<number>} arg2 List of numbers to be processed.
    * @constructor
    * @extends {goog.Disposable}
    */
    project.MyClass = function(arg1, arg2) {
      // ...
    };
    goog.inherits(project.MyClass, goog.Disposable);

##### 方法和功能注释

参数和返回类型应该被记录下来。如果方法描述从参数或返回类型的描述中明确可知则可以省略。方法描述应该由一个第三人称表达的句子开始。

    /**
    * Operates on an instance of MyClass and returns something.
    * @param {project.MyClass} obj Instance of MyClass which leads to a long
    *    comment that needs to be wrapped to two lines.
    * @return {boolean} Whether something occured.
    */
    function PR_someMethod(obj) {
      // ...
    }

##### 属性评论

    /** @constructor */
    project.MyClass = function() {
    /**
      * Maximum number of things per pane.
      * @type {number}
      */
      this.someProperty = 4;
    }

##### JSDoc标签参考

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>标签</th>
<th>模板及实例</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>@author</td>
<td>@author <a href="mailto:username@google.com">username@google.com</a> (first last)
例如：
<pre><code>/**
* @fileoverview Utilities for handling textareas.
* @author kuth@google.com (Uthur Pendragon)
*/</code></pre></td>
<td>说明文件的作者是谁，一般只会在 <code>@fileoverview</code> 里用到。</td>
</tr>
<tr class="even">
<td>@code</td>
<td>{@code ...}
例如：
<pre><code>/**</code></pre>
<blockquote>
<ul>
<li>Moves to the next position in the selection.</li>
<li>Throws {@code goog.iter.StopIteration} when it</li>
<li>passes the end of the range.</li>
</ul>
* @return {Node} The node at the next position. */ goog.dom.RangeIterator.prototype.next = function() { // ... };
</blockquote></td>
<td>表示这是一段代码，他能在文档中正确的格式化。</td>
</tr>
<tr class="odd">
<td>@const</td>
<td>@const @const {type}
例如：
<pre><code>/** @const \*/ var MY_BEER = &#39;stout&#39;;
/**
* My namespace&#39;s favorite kind of beer.
* @const {string}
*/
mynamespace.MY_BEER = &#39;stout&#39;;
&#10;/** @const \*/ MyClass.MY_BEER = &#39;stout&#39;;
&#10;/**
* Initializes the request.
* @const
*/
mynamespace.Request.prototype.initialize = function() {
  // This method cannot be overriden in a subclass.
}</code></pre></td>
<td>说明变量或者属性是只读的，适合内联。
标记为 <code>@const</code> 的变量是不可变的。如果变量或属性试图覆盖他的值，那么js编译器会给出警告。
如果某一个值可以清楚地分辨出是不是常量，可以省略类型声明。变量附加的注释是可选的。
当一个方法被标记为 <code>@const</code> ，意味着这个方法不仅不可以被覆盖，而且也不能在子类中重写。
<code>@const</code> 的更多信息，请看 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Constants">常量</a> 部分</td>
</tr>
<tr class="even">
<td>@constructor</td>
<td>@constructor
例如：
<pre><code>/**
* A rectangle.
* @constructor
*/
function GM_Rect() {
  ...
}</code></pre></td>
<td>在一个类的文档中表示构造函数。</td>
</tr>
<tr class="odd">
<td>@define</td>
<td>@define {Type} description
例如：
<pre><code>/** @define {boolean} */
var TR_FLAGS_ENABLE_DEBUG = true;
&#10;/** @define {boolean} */
goog.userAgent.ASSUME_IE = false;</code></pre></td>
<td>指明一个在编译时可以被覆盖的常量。
在这个例子中，编译器标志 <code>--define='goog.userAgent.ASSUME_IE=true'</code> 表明在构建文件的时侯变量 <code>goog.userAgent.ASSUME_IE</code> 可以被赋值为 <code>true</code> 。</td>
</tr>
<tr class="even">
<td>@deprecated</td>
<td>@deprecated Description
例如：
<pre><code>/**
* Determines whether a node is a field.
* @return {boolean} True if the contents of
*    the element are editable, but the element
*    itself is not.
* @deprecated Use isField().
*/
BN_EditUtil.isTopEditableField = function(node) {
  // ...
};</code></pre></td>
<td>说明函数、方法或者属性已经不可用，常说明替代方法或者属性。</td>
</tr>
<tr class="odd">
<td>@dict</td>
<td>@dict Description
例如：
<pre><code>/**
* @constructor
* @dict
*/
function Foo(x) {
  this[&#39;x&#39;] = x;
}
var obj = new Foo(123);
var num = obj.x;  // warning
(/** @dict \*/ { x: 1 }).x = 123;  // warning</code></pre></td>
<td>当构造函数 (例子里的Foo)被标记为 <code>@dict</code> ，你只能使用括号表示法访问 <code>Foo</code> 的属性。这个注释也可以直接使用对象表达式。</td>
</tr>
<tr class="even">
<td>@enum</td>
<td>@enum {Type}
例如：
<pre><code>/**
* Enum for tri-state values.
* @enum {number}
*/
project.TriState = {
  TRUE: 1,
  FALSE: -1,
  MAYBE: 0
};</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td>@export</td>
<td>@export
例如：
<pre><code>/** @export */
foo.MyPublicClass.prototype.myPublicMethod = function() {
  // ...
};</code></pre></td>
<td>对于例子中的代码，当编译到 <code>--generate_exports</code> 标记时，将会产生以下代码：
<pre><code>goog.exportSymbol(&#39;foo.MyPublicClass.prototype.myPublicMethod&#39;,
    foo.MyPublicClass.prototype.myPublicMethod);</code></pre>
也就是输出了没有编译的代码。使用@export标签时，应该：
<ol type="1">
<li>包含 <code>//javascript/closure/base.js</code> , 或者</li>
<li>同时定义 <code>goog.exportSymbol</code> 和 <code>goog.exportProperty</code> 并且要使用相同的调用方法。</li>
</ol></td>
</tr>
<tr class="even">
<td>@expose</td>
<td>@expose
例如：
<pre><code>/** @expose */</code></pre>
MyClass.prototype.exposedProperty = 3;</td>
<td>声明一个公开的属性，表示这个属性不可以被删除、重命名或者由编译器进行优化。相同名称的属性也不能由编译器通过任何方式进行优化。
<code>@expose</code> 不可以出现在代码库里，因为他会阻止这个属性被删除。</td>
</tr>
<tr class="odd">
<td>@extends</td>
<td>@extends Type @extends {Type}
例如：
<pre><code>/**</code></pre>
<blockquote>
<ul>
<li>Immutable empty node list.</li>
<li>@constructor</li>
</ul>
* @extends goog.ds.BasicNodeList */
</blockquote>
<dl>
<dt>goog.ds.EmptyNodeList = function() {</dt>
<dd>
...
</dd>
</dl>
};</td>
<td>和 <code>@constructor</code> 一起使用，表示从哪里继承过来的。类型外的大括号是可选的。</td>
</tr>
<tr class="even">
<td>@externs</td>
<td>@externs
例如：
<pre><code>/**</code></pre>
<blockquote>
<ul>
<li>@fileoverview This is an externs file.</li>
</ul>
* @externs */
</blockquote>
var document;</td>
<td>声明一个外部文件。</td>
</tr>
<tr class="odd">
<td>@fileoverview</td>
<td>@fileoverview Description
例如：
<pre><code>/**</code></pre>
<blockquote>
<ul>
<li>@fileoverview Utilities for doing things that require this very long</li>
<li>but not indented comment.</li>
</ul>
* @author <a href="mailto:kuth@google.com">kuth@google.com</a> (Uthur Pendragon) */
</blockquote></td>
<td>使注释提供文件级别的信息。</td>
</tr>
<tr class="even">
<td>@implements</td>
<td>@implements Type @implements {Type}
例如：
<pre><code>/**</code></pre>
<blockquote>
<ul>
<li>A shape.</li>
</ul>
* @interface */
</blockquote>
function Shape() {}; Shape.prototype.draw = function() {};
<dl>
<dt>/**</dt>
<dd>
<ul>
<li>@constructor</li>
</ul>
* @implements {Shape} */
</dd>
</dl>
function Square() {}; Square.prototype.draw = function() { ... };</td>
<td>使用 <code>@constructor</code> 来表示一个类实现了某个接口。类型外的大括号是可选的。</td>
</tr>
<tr class="odd">
<td>@inheritDoc</td>
<td>@inheritDoc
例如：
<pre><code>/** @inheritDoc */
project.SubClass.prototype.toString() {
  // ...
};</code></pre></td>
<td>**已废弃。使用@override代替**
表示一个子类中的方法或者属性覆盖父类的方法或者属性，并且拥有相同的文档。注意， <code>@inheritDoc</code> 等同 <code>@override</code></td>
</tr>
<tr class="even">
<td>@interface</td>
<td>@interface
例如：
<pre><code>/**
* A shape.
* @interface
*/
function Shape() {};
Shape.prototype.draw = function() {};
&#10;/**
* A polygon.
* @interface
* @extends {Shape}
*/
function Polygon() {};
Polygon.prototype.getSides = function() {};</code></pre></td>
<td>表示一个函数定义了一个接口。</td>
</tr>
<tr class="odd">
<td>@lends</td>
<td>@lends objectName @lends {objectName}
例如：
<pre><code>goog.object.extend(
    Button.prototype,
    /** @lends {Button.prototype} */ {
    isButton: function() { return true; }
    });</code></pre></td>
<td>表示对象的键是另外一个对象的属性。这个标记只能出现在对象字面量中。
注意，括号中的名称和其他标记中的类型名称不一样，它是一个对象名，表明是从哪个对象“借过来”的属性。例如， <code>@type {Foo}</code> 意味着Foo的一个实例，但是 <code>@lends {Foo}</code> 意味着“Foo构造函数”.
<a href="https://code.google.com/p/jsdoc-toolkit/wiki/TagLends">JSDoc Toolkit docs</a> 中有关于更多此标记的信息。</td>
</tr>
<tr class="even">
<td>@license or @preserve</td>
<td>@license Description
例如：
<pre><code>/**
* @preserve Copyright 2009 SomeThirdParty.
* Here is the full license text and copyright
* notice for this file. Note that the notice can span several
* lines and is only terminated by the closing star and slash:
*/</code></pre></td>
<td>由 <code>@licenseor</code> 或 <code>@preserve</code> 标记的内容，会被编译器保留并放到文件的顶部。
这个标记会让被标记的重要内容（例如法律许可或版权文本）原样输出，换行也是。</td>
</tr>
<tr class="odd">
<td>@noalias</td>
<td>@noalias
例如：
<pre><code>/** @noalias */
function Range() {}</code></pre></td>
<td>用在外部文件当中，告诉编译器，这里的变量或者方法不可以重命名。</td>
</tr>
<tr class="even">
<td>@nosideeffects</td>
<td>@nosideeffects
例如：
<pre><code>/** @nosideeffects */
function noSideEffectsFn1() {
  // ...
};
/** @nosideeffects */
var noSideEffectsFn2 = function() {
  // ...
};
/** @nosideeffects */
a.prototype.noSideEffectsFn3 = function() {
  // ...
};</code></pre></td>
<td>用于函数和构造函数，说明调用这个函数没有副作用。如果返回值未被使用，此注释允许编译器移除对该函数的调用。</td>
</tr>
<tr class="odd">
<td>@override</td>
<td>@override
例如：
<pre><code>/**
* @return {string} Human-readable representation of project.SubClass.
* @override
*/
project.SubClass.prototype.toString() {
  // ...
};</code></pre></td>
<td>表示子类的方法或者属性故意隐藏了父类的方法或属性。如果子类没有其他的文档，方法或属性也会从父类那里继承文档。</td>
</tr>
<tr class="even">
<td>@param</td>
<td>@param {Type} varname Description
例如：
<pre><code>/**
* Queries a Baz for items.
* @param {number} groupNum Subgroup id to query.
* @param {string|number|null} term An itemName,
*    or itemId, or null to search everything.
*/
goog.Baz.prototype.query = function(groupNum, term) {
  // ...
};</code></pre></td>
<td>给方法、函数、构造函数的参数添加文档说明。
<a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#JsTypes">参数类型</a> 一定要写在大括号里。如果类型被省略，编译器将不做类型检测。</td>
</tr>
<tr class="odd">
<td>@private</td>
<td>@private @private {type}
例如：
<pre><code>/**
* Handlers that are listening to this logger.
* @private {!Array.&lt;Function&gt;}
*/
this.handlers\_ = [];</code></pre></td>
<td>与方法或属性名结尾使用一个下划线来联合表明该成员是 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Visibility__private_and_protected_fields_">私有的</a> 。随着工具对 <code>@private</code> 的认可，结尾的下划线可能最终被废弃。</td>
</tr>
<tr class="even">
<td>@protected</td>
<td>@protected @protected {type}
例如：
<pre><code>/**
* Sets the component&#39;s root element to the given element.  Considered
* protected and final.
* @param {Element} element Root element for the component.
* @protected
*/
goog.ui.Component.prototype.setElementInternal = function(element) {
  // ...
};</code></pre></td>
<td>用来表明成员或属性是 <code>受保护的 &lt;https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Visibility__private_and_protected_fields_&gt;</code>_ 。成员或属性应使用没有跟随下划线的名称。</td>
</tr>
<tr class="odd">
<td>@return</td>
<td>@return {Type} Description
例如：
<pre><code>/**
* @return {string} The hex ID of the last item.
*/
goog.Baz.prototype.getLastId = function() {
  // ...
  return id;
};</code></pre></td>
<td>在方法或函数调用时使用，来说明返回类型。给布尔值写注释时，写成类似“这个组件是否可见”比“如果组件可见则为true，否则为false”要好。如果没有返回值，不使用 <code>@return</code> 标签。
<a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#JsTypes">类型</a> 名称必须包含在大括号内。如果省略类型，编译器将不会检查返回值的类型。</td>
</tr>
<tr class="even">
<td>@see</td>
<td>@see Link
例如：
<pre><code>/**
* Adds a single item, recklessly.
* @see #addSafely
* @see goog.Collect
* @see goog.RecklessAdder#add
...</code></pre></td>
<td>参考查找另一个类或方法。</td>
</tr>
<tr class="odd">
<td>@struct</td>
<td>@struct Description
例如：
<pre><code>/**
* @constructor
* @struct
*/
function Foo(x) {
  this.x = x;
}
var obj = new Foo(123);
var num = obj[&#39;x&#39;];  // warning
obj.y = &quot;asdf&quot;;  // warning
&#10;Foo.prototype = /** @struct */ {
  method1: function() {}
};
Foo.prototype.method2 = function() {};  // warning</code></pre></td>
<td>当一个构造函数（在本例中 <code>Foo</code> ）注释为 <code>@struct</code> ，你只能用点符号访问Foo对象的属性。此外，Foo对象创建后不能加新的属性。此注释也可以直接使用于对象字面量。</td>
</tr>
<tr class="even">
<td>@supported</td>
<td>@supported Description
例如：
<pre><code>/**
* @fileoverview Event Manager
* Provides an abstracted interface to the
* browsers&#39; event systems.
* @supported So far tested in IE6 and FF1.5
*/</code></pre></td>
<td>用于在文件信息中说明该文档被哪些浏览器支持</td>
</tr>
<tr class="odd">
<td>@suppress</td>
<td>@suppress {warning1|warning2}
例如：
<pre><code>/**
* @suppress {deprecated}
*/
function f() {
  deprecatedVersionOfF();
}</code></pre></td>
<td>标明禁止工具发出的警告。警告类别用|分隔。</td>
</tr>
<tr class="even">
<td>@template</td>
<td>@template
例如：
<pre><code>/**
* @param {function(this:T, ...)} fn
* @param {T} thisObj
* @param {...*} var_args
* @template T
*/
goog.bind = function(fn, thisObj, var_args) {
  ...
};</code></pre></td>
<td>这个注释可以用来声明一个 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Template_types">模板类型名</a> 。</td>
</tr>
<tr class="odd">
<td>@this</td>
<td>@this Type @this {Type}
例如：
<pre><code>pinto.chat.RosterWidget.extern(&#39;getRosterElement&#39;,
/**
* Returns the roster widget element.
* @this pinto.chat.RosterWidget
* @return {Element}
*/
function() {
  return this.getWrappedComponent_().getElement();
});</code></pre></td>
<td>标明一个特定方法在其上下文中被调用的对象类型。用于 <code>this</code> 关键字是从一个非原型方法中使用时</td>
</tr>
<tr class="even">
<td>@type</td>
<td>@type Type @type {Type}
例如：
<pre><code>/**</code></pre>
<blockquote>
<ul>
<li>The message hex ID.</li>
</ul>
* @type {string} */
</blockquote>
var hexId = hexId;</td>
<td>标识变量，属性或表达式的 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#JsTypes">类型</a> 。大多数类型不需要大括号，但有些项目为了保持一致性而要求所有类型都使用大括号。</td>
</tr>
<tr class="odd">
<td>@typedef</td>
<td>@typedef
例如：
<pre><code>/** @typedef {(string|number)} */
goog.NumberLike;
/** @param {goog.NumberLike} x A number or a string. */
goog.readNumber = function(x) {
  ...
}</code></pre></td>
<td>使用此注释来声明一个更 <a href="https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml#Typedefs">复杂的类型</a> 的别名。</td>
</tr>
</tbody>
</table>

你也许在第三方代码中看到其他类型JSDoc注释，这些注释出现在 [JSDoc Toolkit标签的参考](https://code.google.com/p/jsdoc-toolkit/wiki/TagReference) ，但目前在谷歌的代码中不鼓励使用。你应该将他们当作“保留”字，他们包括：

- @augments
- @argument
- @borrows
- @class
- @constant
- @constructs
- @default
- @event
- @example
- @field
- @function
- @ignore
- @inner
- @link
- @memberOf
- @name
- @namespace
- @property
- @public
- @requires
- @returns
- @since
- @static
- @version

#### 为goog.provide提供依赖

只提供顶级符号。

一个类上定义的所有成员应该放在一个文件中。所以，在一个在相同类中定义的包含多个成员的文件中只应该提供顶级的类（例如枚举、内部类等）。

要这样写：

    goog.provide('namespace.MyClass');

不要这样写：

    goog.provide('namespace.MyClass');
    goog.provide('namespace.MyClass.Enum');
    goog.provide('namespace.MyClass.InnerClass');
    goog.provide('namespace.MyClass.TypeDef');
    goog.provide('namespace.MyClass.CONSTANT');
    goog.provide('namespace.MyClass.staticMethod');

命名空间的成员也应该提供：

    goog.provide('foo.bar');
    goog.provide('foo.bar.method');
    goog.provide('foo.bar.CONSTANT');

#### 编译

必需。

对于所有面向客户的代码来说，使用JS编辑器是必需的，如使用 [Closure Compiler](https://developers.google.com/closure/compiler/?csw=1) 。

#### 技巧和诀窍

JavaScript帮助信息

##### True和False布尔表达式

下边的布尔表达式都返回false：

- null
- undefined
- ''空字符串
- 数字0

但是要小心，因为以下这些返回true：

- 字符串"0"
- \[\]空数组
- {}空对象

下面这样写不好：

    while (x != null) {

你可以写成这种更短的代码（只要你不期望x为0、空字符串或者false）：

    while (x) {

如果你想检查字符串是否为null或空，你可以这样写：

    if (y != null && y != '') {

但是以下这样会更简练更好：

    if (y) {

注意：还有很多不直观的关于布尔表达式的例子，这里是一些：

- Boolean('0') == true '0' != true
- 0 != null 0 == \[\] 0 == false
- Boolean(null) == false null != true null != false
- Boolean(undefined) == false undefined != true undefined != false
- Boolean(\[\]) == true \[\] != true \[\] == false
- Boolean({}) == true {} != true {} != false

##### 条件（三元）操作符（？：）

以下这种写法可以三元操作符替换：

    if (val != 0) {
      return foo();
    } else {
      return bar();
    }

你可以这样写来代替：

    return val ? foo() : bar();

三元操作符在生成HTML代码时也是很有用的：

    var html = '<input type="checkbox"' +
        (isChecked ? ' checked' : '') +
        (isEnabled ? '' : ' disabled') +
        ' name="foo">';

##### && 和 \|\|

二元布尔操作符是可短路的,，只有在必要时才会计算到最后一项。

"\|\|" 被称作为 'default' 操作符，因为可以这样：

    /** @param {*=} opt_win */
    function foo(opt_win) {
      var win;
      if (opt_win) {
        win = opt_win;
      } else {
        win = window;
      }
      // ...
    }

你可以这样写：

    /** @param {*=} opt_win */
    function foo(opt_win) {
      var win = opt_win || window;
      // ...
    }

"&&" 也可以用来缩减代码。例如，以下这种写法可以被缩减：

    if (node) {
      if (node.kids) {
        if (node.kids[index]) {
          foo(node.kids[index]);
        }
      }
    }

你可以这样写：

    if (node && node.kids && node.kids[index]) {
      foo(node.kids[index]);
    }

或者这样写：

    var kid = node && node.kids && node.kids[index];
      if (kid) {
        foo(kid);
    }

然而以下这样写就有点过头了：

    node && node.kids && node.kids[index] && foo(node.kids[index]);

##### 遍历节点列表

节点列表是通过给节点迭代器加一个过滤器来实现的。这表示获取他的属性，如length的时间复杂度为O(n)，通过length来遍历整个列表需要O(n^2)。

    var paragraphs = document.getElementsByTagName('p');
    for (var i = 0; i < paragraphs.length; i++) {
      doSomething(paragraphs[i]);
    }

这样写更好：

    var paragraphs = document.getElementsByTagName('p');
    for (var i = 0, paragraph; paragraph = paragraphs[i]; i++) {
      doSomething(paragraph);
    }

这种方法对所有的集合和数组(只要数组不包含被认为是false值的元素) 都适用。

在上面的例子中，你也可以通过firstChild和nextSibling属性来遍历子节点。

    var parentNode = document.getElementById('foo');
    for (var child = parentNode.firstChild; child; child = child.nextSibling) {
      doSomething(child);
    }
