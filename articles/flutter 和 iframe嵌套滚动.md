# flutter 和 iframe嵌套滚动

## 1、禁止网页滚动

```css
html,body{
  overflow: hidden;
  height: 100%;
}
```

## 2、捕获网页滚动事件

首先需要引入jquery

然后script添加如下代码

```js
window._counter=0;

$( document ).ready(function() { window.top.postMessage({'type':'setstate','h':$(document).height(),'counter':window._counter}, '*');
      window._counter++;
    });

window.addEventListener('mousewheel', function (e, delta) {
        // var name=e.target.className;
        console.log(e.target.className);
        console.log(e['deltaY']);
    window.top.postMessage({'type':'scroll','h':$(document).height(),'y':e['deltaY'],'counter':window._counter}, '*');
        window._counter++;
        // if(name=='white_color' | name=='scrollmenu' | name=='my_checkbox'){
        //   window.scrollWidget.scrollLeft += e['deltaY'];
        // // console.log(e);
        //   window.scroll_position=window.scrollWidget.scrollLeft;
        //   e.preventDefault();
        // }
      }, {passive: false});
```

## 3、flutter监听接收消息

```dart
typedef ScrollListener = void Function(int y);
@override
void initState() {
  super.initState();
  html.window.onMessage.listen((event) {
      //data 就是要接收的消息
    callback = event.data;
    if (callback['type'] == 'setstate') {
      if (mounted) setState(() {});
    } else if (callback['type'] == 'scroll') {
      widget.scrollListener?.call(callback['y']);
    }
  });
}
```

# 4、注册iframe和使用

```dart
void register(mId) {
    // ignore: undefined_prefixed_name
    ui.platformViewRegistry.registerViewFactory(
        '$mId',
        (int viewId) => html.EmbedElement()
          ..height = "100%"
          ..width = "100%"
          ..style.height = '100%'
          ..style.width = '100%'
          ..src = url
          ..style.border = 'none');
}
HtmlElementView(viewType: '$mId');
//注意套一层sizedbox
//在3、中的回调后调正sizebox的高度
```

