# ゼロから作るディープラーニング

## Python コード規約

https://pep8-ja.readthedocs.io/ja/latest/

## 単体テスト

標準モジュールの `unittest`、サードパーティモジュールの `pytest` などがあるが、
今回は `pytest` を使う。

参考
https://qiita.com/flcn-x/items/fcbbc2fb291b970290f2

## モジュール管理ツール

モジュール管理ツールにもいろいろあるそうで、有名どころでは `pip` が最も古そう？
pip を使ってみたが、`npm` のようにローカルインストール（= ディレクトリごとにモジュールのインストールを行う）できなさそう `requirements.txt` なことが分かった。

[npm に慣れた Node 出身者が機械学習に入門しようと Python に手を出したら環境構築に丸 2 日掛かった話](https://qiita.com/rema424/items/a34e3eba559b980c3abf) によると、`pyenv` が `npm` に近い世界観を実現しようとしているものらしい。
ので `pip` ではなく `pyenv` でモジュールを管理することとする。

### モジュール管理ツールサマリ

https://mypaceshun.github.io/blog/2022/06/20220607-poetry%E3%81%AF%E3%81%84%E3%81%84%E3%81%9E/ を参考にまとめた。

- pip
  - モジュールの管理はできるが、依存ライブラリのバージョン管理まではしてくれない。ので事故が起きるのだとか。
- pipenv
  - pip と異なり、依存モジュールのバージョン管理も可能
  - [scripts] でタスクを定義可能
- poetry
  - pipenv 同様、依存モジュールのバージョン管理可能
  - pipenv とは異なり、タスク定義は不可能
  - pip で扱えるライブラリにするには `setup.py` の作成が必須だが、poetry は不要

### poetry の使い方

```sh
# poetry インストール
pip install --user poetry

# プロジェクト初期化
poetry init

# モジュール追加
poetry add <module-name>

# モジュールインストール
poetry install
```

### pip(Appendix)
#### 使用例

```sh
# モジュールの追加
pip install pytest
# インストール
pip install -r requirements.txt
```

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