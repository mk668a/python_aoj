# 問題

    - 下記のような検索フォームがあります
    - `input` に検索ワードを入力して`button` を押すと API にリクエストを送ります
        - 送信の形式は`https://api.example.com/search?q=〇〇` とします
            - サーバーからは下記のような JSON が返ってくるのでその内容をdivに展開します
                - `{ id: number, title: string }[]` とします
                    - クエリが空の時は何も返ってきません
                    - サーバーはとても貧弱です、極力サーバーに優しくなるよう処理を書いてください
                        - CSSに関しては一切考慮しなくてよいです

                            ```
+-----------+  +--------+
| input     |  | button |
+-----------+  +--------+
+-----------------------+
| div                   |
+-----------------------+
```

# 対象回答者

JavaScriptかけます、って言ってる人

# 備考

    - 表示には何のライブラリを使っても良いものとします（ jQuery、React、Vue、Angular、生 JS ）。
- Ajax リクエストにも何を使っても良いものとします（ axios、$.ajax、fetch、生 XHR ）
- メソッド名は多少間違っててもいいですし、設問者に聞いて教えてもらって構いません。
- `input` や`button` の`class` や`id` は適当に補って構いません

------

    ```typescript
document.getElementById("button").onclick = function(){
    var word = getElementByID("input").value
    $.ajax(`https://api.example.com/search?q=${word}`).done(function(data){
for (var i = 0; i < data.length; i++) {
    $('#div').append(
        $('<p></p>').text($(data[i]['title']))
    )
}
        
    })
}


```

```typescript
$('button').click()
$('button').on('click', () => { })

const button = document.getElementById('button')
button.addEventListener('click', (e: ClickEvent) => {
    button.setAttribute('disabled', true)
    $.ajax(...).done(() => {
        ....
    }).finally(() => {
        button.setAttribute('disabled', false)
    })
});

```
