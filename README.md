# Vue 3 + Vite + Flask + Pymsql

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (previously Volar) and disable Vetur

## Environment

請先安裝 python3, pip3, nodejs, npm, appserv

資料庫建置指令使用SOCAMS2.sql


## Project setup

``` bash
cd front-end
npm install

cd back-end
pip3 install -r requirements.txt
```

## Compiles and hot-reloads for development

``` bash
cd front-end
npm run dev

cd back-end
python3 app.py

cd back-end
python app.py
```



# account 
1 管理員
2 房東
3 老師
4 學生


# 從所有版本中刪除某檔案
git rm -r --cached .env
git filter-repo --invert-paths --path .env

git remote add origin https://github.com/0rain0/Student-Off-Campus-Accommodation-Management-System.git
git remote -v

git push origin --force --all
git push origin --force --tags
