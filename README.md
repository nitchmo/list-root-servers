# djbdns用のroot servers情報を更新するツールを作りました。

root servers情報って、[http://www.root-servers.org/news.html](このページ)を見ると年に一度くらいの頻度で変更されていますね。  
なので、djbdns内の dnscacheで設定されている root servers情報を更新するツールをPythonで作りました。  
空の行を含めても20行程度なので「作った」と言うほどでもないし、dnsqとawkを使って１行で成してしまう方法もあるみたいで、車輪をつくっちゃった感は否めないなぁ・・・

## 概要

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

