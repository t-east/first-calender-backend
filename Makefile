# イメージのビルド
build:
	docker-compose -f docker-compose.yml build

del:
	docker stop fastapi mysql
	docker rm fastapi mysql
	rm -rf mysql/mysql_data/*

# 開発用サーバー立ち上げ
dev:
	docker-compose -f docker-compose.yml up

# Flake8のLinter実行
flake8:
	docker-compose -f docker-compose.yml run --rm fastapi flake8 app

# mypyによる型チェックの実行
mypy:
	docker-compose -f docker-compose.yml run --rm fastapi mypy app

# blackによるフォーマット修正
black:
	docker-compose -f docker-compose.yml run --rm fastapi black app

# テスト実行
test:
	docker-compose -f docker-compose.yml run --rm fastapi coverage run -m pytest -v -s /app/
