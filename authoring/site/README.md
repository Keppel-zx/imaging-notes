# Imaging Notes 图文版：上传 GitHub 与阅读说明

网站对应仓库 `keppel-zx/imaging-notes`，部署后保留 `https://keppel-zx.github.io/imaging-notes/` 和全部56讲原有URL。

## 一、解压后哪些文件要上传

本ZIP的最外层就是网站根目录。将下列内容放到仓库根目录，不要再套一层ZIP同名文件夹。

| 文件或目录 | 用途 | 是否上传 |
|---|---|---|
| `index.html` | 56讲目录、关键词全文搜索、模块筛选 | 必须 |
| `articles/` | 全部56讲完整正文 | 必须，整个目录 |
| `assets/` | CSS、搜索与原文对照脚本、所有配图 | 必须，整个目录；尤其不能漏掉figures |
| `data/` | 搜索数据与课程信息 | 必须，整个目录 |
| `references.html` | 文献、章节、页码、公式、图号索引 | 必须 |
| `sources.html` | 七份原书的本地关联管理 | 必须 |
| `supplement.html` | openISP、Imatest工程延伸 | 必须 |
| `source_catalog.json` | 七份资料的版本、页序和章节信息 | 必须 |
| `citation_index.json` | 包含图文阅读卡片的统一引用索引 | 必须 |
| `visual_index.json` | 每讲短摘、图片、重点公式和变量来源 | 建议保留 |
| `progress.json`、`QUALITY_REPORT.md` | 逐讲状态与核查范围 | 建议保留 |
| `404.html`、`.nojekyll` | 错误页与静态站点设置 | 必须；注意.nojekyll是隐藏文件 |
| `file_manifest.json` | 文件大小和SHA-256清单 | 建议保留 |
| `README.md` | 本说明 | 建议保留 |
| `authoring.zip` | 编写源文件、图文素材、构建脚本与审校报告 | 可上传或另存；阅读网站不依赖它 |

不要上传原书PDF、原书全页截图、`evidence/`提取文本、临时QA页面。这些均未放入网站包。

## 二、在GitHub网页上传

1. 先下载仓库备份，或新建更新分支。
2. 打开仓库 Code 页面，选择 Add file → Upload files。将解压后的文件与目录上传到仓库根目录。目录上传受浏览器支持限制，漏文件时建议使用Git客户端。
3. 检查根目录直接有 `index.html`，`articles/`有day-01至day-56，`assets/figures/`有PNG和SVG图片。不要只上传HTML而漏掉CSS、JS、JSON和图片。
4. 若网页上传未包含隐藏的`.nojekyll`，用 Add file → Create new file 建立同名空文件。
5. 提交更改。Settings → Pages 保留当前发布方式。若从分支发布，选择实际发布分支（通常main）和 `/ (root)`；若使用Actions，沿用已有工作流并确认发布目录为根目录。
6. 在Actions或Pages检查部署成功，再打开原地址强制刷新。先检查第3讲的双语短摘、公式卡片和三张配图，再检查搜索与前后跳转。

若使用Git客户端：在本地仓库备份后，将本包根目录内容覆盖进去，检查差异，运行 `git add -A`、`git commit -m "Upgrade 56 lessons with source excerpts, figures and equations"`、`git push`。不要覆盖仓库现有的身份配置或无关工作流。

## 三、怎样在网页学习

每讲包含：完整中文精读正文、英文原文短摘与中文译读、就地配图及分析、独立居中的关键公式、符号/意义/单位表、来源与核心结论。图像标注“原图局部”或“自绘图解”，点击即可放大。正文的重要关系式已单独成行。

短摘、译文、图解和公式都已内嵌，不需要关联PDF。需要看完整上下文时：打开“原文对照”，为相应书关联自己持有的PDF；之后点击课程中的页码或“对照原页”按钮。文件仅存于当前浏览器，不上传服务器或GitHub。更换浏览器、清除网站数据后需要重新关联。不同版本会提示核对页码。

PDF页码一律按阅读器从1开始的页序。完整PDF显示依赖浏览器内置阅读器；若内嵌区域无法显示，使用“在新标签页打开原文”，或在自己的PDF阅读器中跳转到标明页序。手机浏览器可能改为下载或外部打开，不能保证各浏览器原生PDF行为相同。

## 四、本地预览与维护

普通双击HTML可阅读正文；全文搜索、PDF关联和数据读取请通过HTTP访问。例如解压后在该目录运行 `python3 -m http.server 8000`，然后访问 `http://localhost:8000/`。访客无需安装Python；GitHub Pages直接支持这些功能。

公式是构建时生成的原生MathML，不使用外部CDN。网站兼容项目子路径 `/imaging-notes/`。维护源文件见 `authoring.zip`；修改后按其中MAINTENANCE说明重建与复核。

当前交付是ZIP，尚未写入现有GitHub仓库或更新线上站点。
