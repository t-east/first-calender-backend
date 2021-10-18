# User

|  name  |  type  | nullable | details |  
| ---- | ---- | ---- | ---- |
|  id  |  int  | false | 識別子 | 
|  user_name  |  string  | false | ユーザ名 |
|  email  |  string  | false | メールアドレス |
|  password_hash  |  hash?  | false | パスワードのハッシュ値 |
|  birth_date  |  string  | false | 生年月日 |
|  registered_at  |  date  | false | ユーザ登録時刻 |
|  last_login_at  |  date  | true | 最終ログイン時刻 |


# Event
|  name  |  type  | nullable | details |  
| ---- | ---- | ---- | ---- |
|  id  |  int  | false | 識別子 | 
|  user_id  |  int  | false | ユーザ識別子 | 
|  title  |  string  | false | イベントタイトル | 
|  description  |  string  | true | イベント詳細 |
|  begin_date  |  string  | true | イベント開始時刻 |
|  is_all_day  |  boolen  | true | 終日判別子 |
|  end_date  |  string  | false | イベント開始時刻 |
|  created_at  |  date  | false | イベント作成時刻 | 
|  updated_at  |  date  | true | イベントアップデート時刻 | 
|  deleted_at  |  date  | true | イベント削除時刻 | 
|  color |  string  | false | イベントの色分け |
|  url  |  string  | true | オンライン会議用のURL | 


# Reminder
|  name  |  type  | nullable | details |  
| ---- | ---- | ---- | ---- |
|  id  |  int  | false | 識別子 | 
|  user_id  |  int  | false | ユーザ識別子 | 
|  event_id  |  int  | false | イベント識別子 | 
|  remind_time  |  date  | false | リマインド時刻 | 
|  color  |  string  | false | リマインドカラー（いる？） |
|  created_at  |  date  | false | リマインド作成時刻 | 
|  updated_at  |  date  | true | リマインドアップデート時刻 | 
|  deleted_at  |  date  | true | リマインド削除時刻 |


