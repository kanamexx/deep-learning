# ゼロから作るディープラーニング

## Python コード規約

https://pep8-ja.readthedocs.io/ja/latest/

## 単体テスト

標準モジュールの `unittest`、サードパーティモジュールの `pytest` などがあるが、
今回は `pytest` を使う。

https://qiita.com/flcn-x/items/fcbbc2fb291b970290f2

## 小ネタ・Tips

- 文字のフォーマット
  - https://docs.python.org/ja/3.8/tutorial/inputoutput.html
```python
    // フォーマットを使わない
    def hello(self):
        print("Hello" + self.name + "!")
    // フォーマットを使う
    def helloTemplate(self):
        print(f"Hello{self.name}!")
```