# zendesk_searcher

簡易的なZendeskのチケット検索ツール

# How to use

## Installation

```bash
git clone git@github.com:hassaku63/simple_zendesk_searcher.git

cd '<cloned-dir>'

pip install .
```

or

```text
pip install git+https://github.com/hassaku63/simple_zendesk_searcher.git
```

## Set env


```text
export ZENDESK_SUBDOMAIN=<your-subdomain>
export ZENDESK_EMAIL=<your-email>
export ZENDESK_TOKEN=<your-token>
```

## Execte

execute `simple_zendesk_search` .

```text
usage: Zendesk ticket search [-h] --keyword KEYWORD [--subdomain SUBDOMAIN]
                             [--email EMAIL] [--token TOKEN] [--output OUTPUT]

Zendesk APIはsubdomain/email/token の3つを認証情報として要求します。 環境変数ZENDESK_SUBDOMAIN,
ZENDESK_EMAIL, ZENDESK_TOKENで定義するか、 コマンドライン引数で直接指定してください。
両方で指定した場合はコマンドライン引数を優先します。

optional arguments:
  -h, --help            show this help message and exit
  --keyword KEYWORD     keyword will serach from subject
  --subdomain SUBDOMAIN
                        zendesk subdomain
  --email EMAIL         zendesk email
  --token TOKEN         zendesk token
  --output OUTPUT       output file. default=output.csv

```
