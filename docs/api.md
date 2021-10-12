# Create User
新規Userを作成する
### エンドポイント
```
POST /api/users
```
```
{
    "id": 1,
    "created_at": "2021-07-28T07:31:52.418Z",
    "updated_at": "2021-07-28T07:31:52.418Z",
    "deleted_at": null,
    "email": "a@example.com",
    "name": "田中"
}

```
### リクエストとレスポンスの例
```
$ curl -X POST -H "Content-Type: application/json" -d '{"email":"a@example.com", "name":"田中"}' localhost:8080/api/users
```
