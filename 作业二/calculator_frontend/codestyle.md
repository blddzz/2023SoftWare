[风格指南 — Vue.js (vuejs.org)](https://v2.cn.vuejs.org/v2/style-guide/)

### 多个 attribute 的元素

**多个 attribute 的元素应该分多行撰写，每个 attribute 一行。**

#### 反例

```
<img src="https://vuejs.org/images/logo.png" alt="Vue Logo">
```

```
<MyComponentfoo="a"bar="b"baz="c"/>
```

#### 好例子

```
<img
  src="https://vuejs.org/images/logo.png"
  alt="Vue Logo"
>
```

```
<MyComponent
  foo="a"
  bar="b"
  baz="c"
/>
```
