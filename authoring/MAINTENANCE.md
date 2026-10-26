# 图文版维护

网站根目录可直接部署；访客不需要构建依赖。

1. 安装requirements.txt。修改lessons/week-NN/day-NN.html完整正文，同步citations/week-NN.json。
2. 图文卡片在visuals/week-NN.json，必须保持AUTHORING_VISUAL.md所列引用字段与来源区分。配图在site/assets/figures/，不可遗漏。
3. 运行python3 scripts/build.py，输出site/。
4. 完整来源验证需自己持有对应PDF，并重建evidence/{source_id}/NNNN.txt。随后运行scripts/validate.py及scripts/validate_visual.py。本包不提供原书提取全文。
5. 重新核查更改课程的原文、公式、图片、桌面与手机布局，更新progress.json。scripts/package.py是本次验收后封装脚本，不能代替审校。

引用索引citation_index.json由基础引用与新增图文来源合并生成。visual_index.json保存图片、短摘及重点公式；source_catalog.json标明版本和章节，source_inventory.json仅为自动定位候选。

新增PDF原文对照使用浏览器IndexedDB。完整PDF不公开发布，网页内嵌依赖各浏览器原生PDF能力；保留新标签页与手动页序回退。
