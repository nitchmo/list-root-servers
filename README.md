# djbdns用のroot servers情報を更新するツールを作りました。

動作の概要を説明すると、`https://www.internic.net/domain/named.root`にアクセスして、その中のIPを取得しただけです。  

## 使い方

IP一覧を標準出力しているだけなので、設定ファイルに対してリダイレクトしてください。

```sh
# 多くの場合、root servers情報を更新するには rootになるはず。
sudo su

# n-djbdnsの場合
python list-root-servers.py > /etc/ndjbdns/servers/roots

# djbdnsの場合
python list-root-servers.py > /var/dnscache/root/servers/@
```

※ Python3な方は`list-root-servers3.py`を使ってください。

詳しくは[こちら](https://nitchmo.com/djbdns-root-data.html)
