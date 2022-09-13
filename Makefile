HEROKU_APP_NAME=myshop-mrkiura
HEROKU_FRONTEND_APP_NAME=myshop-mrkiura-fe
COMMIT_ID=$(shell git rev-parse HEAD)


heroku-login:
	HEROKU_API_KEY=${HEROKU_API_KEY} heroku auth:token

heroku-container-login:
	HEROKU_API_KEY=${HEROKU_API_KEY} heroku container:login

build-app-heroku: heroku-container-login
	docker build -t registry.heroku.com/$(HEROKU_APP_NAME)/web ./backend

push-app-heroku: heroku-container-login
	docker push registry.heroku.com/$(HEROKU_APP_NAME)/web

release-heroku: heroku-container-login
	heroku container:release web --app $(HEROKU_APP_NAME)

deploy-frontend-heroku: heroku-login
	git subtree push --prefix frontend https://git.heroku.com/$(HEROKU_FRONTEND_APP_NAME).git master


deploy-frontend-herokuu: heroku-login
	git subtree push --prefix frontend https://heroku:${HEROKU_API_KEY}@git.heroku.com/$(HEROKU_FRONTEND_APP_NAME).git master


.PHONY: heroku-login heroku-container-login build-app-heroku push-app-heroku deploy-frontend-heroku
