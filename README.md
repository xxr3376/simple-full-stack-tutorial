# 做 Demo 的 N 种方法 a.k.a. 前后端是怎么回事？

## 前端后端分别是啥？

### 1-simple

```sequence
participant Backend
participant Frontend

Frontend->Backend: request /
Backend->Frontend: HTML
Note right of Frontend: Execute Javascript...
```

* HTML
* CSS
* Javascript

### 2-multi-file

```sequence
participant Backend
participant Frontend

Frontend->Backend: request /index1
Backend->Frontend: HTML
Note right of Frontend: Page1 done


Frontend->Backend: request /index2
Backend->Frontend: HTML
Note right of Frontend: Parse HTML
Frontend->Backend: request /static/style.css
Backend->Frontend: CSS File
Frontend->Backend: request /static/index.js
Backend->Frontend: JS File
Note right of Frontend: Execute Javascript...

```

---

#### HTML 是如何实现登陆的
```sequence
participant Backend
participant Frontend

Frontend->Backend: request /login
Backend->Frontend: HTML
Frontend->Backend: POST /login (userA with password)
Note left of Backend: Check with DB
Note left of Backend: Save in session: abcd -> userA
Backend->Frontend: HTML with Header Set-Cookies 'abcd'
Note right of Frontend: Login Success


Frontend->Backend: request /secret with Header Cookies: abcd
Note left of Backend: Check in session: abcd

Backend->Frontend: Secret data
```

#### XHR

### 前端的世界

#### 传统艺能

* JQuery
* BootStrap
* 各种花式 CSS
* ChartJS / EChart / HighChart / D3JS ...

#### 前端渲染

* Vue / React: MVVC
* 一切皆 XHR
* 问题：SEO 不友好
* webpack and .......

### Some Fancy Thing and Why

* MCD
* Jupyter
* https://streamlit.io
* https://gradio.app
