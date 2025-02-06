# Remote Procedure Call
## 概要
異なるプログラミング言語で書かれたクライアントとサーバが共通の方法で通信し、特定の関数を実行できるようにするシステム。

今回はサーバがPython、クライアントがJavaScript(Node.js)で書かれています。

サーバが提供する関数は次の通り：
- floor(double x): 10進数xを最も近い整数に切り捨て、その結果を整数で返す。
- nroot(int n, int): 方程式r**n = xにおける、r(xのn乗根)の値を計算する。
- revrse(string s): 文字列sを入力として受け取り、入力文字列の逆である新しい文字列を返す。
- validAnagram(string str1, string str2): 2つの文字列を入力として受け取り、2つの文字列が互いにアナグラムであるかどうかを示すブール値を返す。
- sort(string[] strArr): 文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。

### 入出力例
- floor<br>
    クライアント
    ```
    Input Method --> floor
    Input params --> 6.9
    Input id --> 1
    ```
    サーバからのレスポンス
    ```
    { results: 6, result_type: "<class 'int'>", id: '1}
    ```
- nroot<br>
    クライアント
    ```
    Input Method --> nroot
    Input params --> 2, 16
    Input id --> 2
    ```
    サーバからのレスポンス
    ```
    { results: 4, result_type: "<class 'int'>", id: '2'}
    ```
- reverse<br>
    クライアント
    ```
    Input Method --> reverse
    Input params --> hello
    Input Id --> 3
    ```
    サーバからのレスポンス
    ```
    { results: 'olleh', result_type: "<class 'str'>", id: '2'}
    ```
- validAnagram<br>
    クライアント
    ```
    Input Method --> validAnagram
    Input params --> listen, silent
    Input id --> 4
    ```
    サーバからのレスポンス
    ```
    { results: true, result_type: "<class 'bool'>", id: '4'}
    ```
- sort<br>
    クライアント
    ```
    Input Method --> sort
    Input params --> London, Paris, Berlin, Rome
    Input id --> 5
    ```
    サーバからのレスポンス
    ```
    {
        results: [ 'Berlin', 'London', 'Paris', 'Rome'],
        result_type: "<class 'list'>",
        id: '5'
    }
    ```