# MakeAPI V3

> [!IMPORTANT]
> このAPIは信頼のもとに親切心で提供されているものです。そのことを忘れないで( ˙꒳​˙  )ིྀ
> 文字化け・バグ・要望は[Issue](https://github.com/MocA-Love/miq-api-doc/issues)どうぞ

> [!CAUTION]
> 以下の行為を禁止します
> - apikeyを別の人に配布
> - makeのnameパラメーターをほかの人の名前にする
> - パラメーターの改変(name, mid, id, meta, stamp)
> - 上記による意図的にな偽のめいくの生成(開発段階の動作テストは除く)
> - APIへの意図的な不正なリクエスト
> - API鯖への悪意のある攻撃
> - API鯖のIPアドレスの公開


## APIKey
まぐろに頼んでAPIキーを作成してもらいます(運が良ければ)


## めいく
"{host}/make"エンドポイントへのリクエスト

必要なパラメーターは以下
> [!WARNING]
> valueは全てstringです

| パラメーター | 説明                          | 必須 |
|--------------|-------------------------------|------|
| `key`        | API Key                       | はい  |
| `param`      | パラメーター ("めいくmono" など) | はい  |
| `name`       | DisplayName                    | はい  |
| `text`       | Text        | はい  |
| `id`         | Message ID                     | はい  |
| `mid`        | MID                 | はい  |
| `meta`       | LINE 絵文字描画用 | いいえ |
| `stamp`      | LINE スタンプ描画用   | いいえ |

### LINE絵文字の描画について
Metaデータに含まれるデータをstringに変換してリクエストします
あくまで例なので適宜変更してください

```python
emojiData    = eval(msg.contentMetadata["REPLACE"])
param["meta"] = str(emojiData["sticon"]["resources"])
```

### LINEスタンプの描画について
Metaデータに含まれるデータをstringに変換してリクエストします
あくまで例なので適宜変更してください

```python
stamp_id       = msg.contentMetadata["STKID"]
stamp_pkg      = msg.contentMetadata["STKPKGID"]
param["stamp"] = f"{stamp_pkg}_{stamp_id}"
```


## 参戦
"{host}/smash"エンドポイントへのリクエスト

必要なパラメーターは以下
> [!WARNING]
> valueは全てstringです

| パラメーター | 説明                          | 必須 |
|--------------|-------------------------------|------|
| `key`        | API Key                       | はい  |
