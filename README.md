# Imaging Notes — GitHub Pages 部署

适用仓库：`keppel-zx/imaging-notes`；保留现有地址 `https://keppel-zx.github.io/imaging-notes/`。

## 替换网站

1. 先备份仓库内容，或在 GitHub 新建一个分支进行更新。
2. 将此目录中的 `index.html`、`references.html`、`supplement.html`、`404.html`、`.nojekyll`、`assets/`、`articles/`、`data/` 与各 JSON 索引放在仓库根目录。不要再套一层文件夹。
3. 一并提交所有文件；如使用命令行，运行 `git add -A`、`git commit`，再推送到原有 Pages 分支。
4. 保持仓库 Settings → Pages 的原有发布来源。若从分支发布，应选择 `main` / `(root)`；若原仓库使用 Actions，则沿用该工作流。
5. 等待 Pages 部署完成，刷新网站。旧缓存可通过强制刷新清除。

所有站内链接均使用相对路径，兼容 `/imaging-notes/` 项目路径。原有 `articles/day-01.html` 至 `day-56.html` 地址保持不变。

## 阅读与检索

直接打开 HTML 可阅读正文与公式；全文搜索需通过 HTTP 访问，GitHub Pages 默认支持。公式使用构建时生成的 MathML，不依赖 MathJax 或外部 CDN。支持原生 MathML 的现代浏览器可直接显示。

本站不附带原书 PDF、连续原书截图或原始实验数据。请结合自己持有的教材，按 PDF 页序与图号查阅。PDF 页序从 1 开始，与印刷页码不同。

## 项目文件

`progress.json` 是逐讲验收状态，`citation_index.json` 是逐条引用索引，`source_catalog.json` 记录资料版本与页码规则。质量报告说明自动检查和人工核查的范围。

`authoring.zip` 是维护用源文件及检查记录；保留或另存均不影响站点阅读。`QUALITY_REPORT.md` 说明全部检查及其范围。
