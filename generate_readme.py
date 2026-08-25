# -*- coding: utf-8 -*-
"""Generate allProject README.md from project catalog."""

import os

GITEE_USER = os.environ.get("GITEE_USER", "YOUR_GITEE_USERNAME")

PROJECTS = [
    (1, "智慧公交管理系统", "smartbus-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (2, "汽车商城系统", "carshop-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (3, "问卷调查系统", "insightform-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (4, "宠物寄养家庭版系统", "pethaven-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (5, "宠物寄养机构版管理系统", "petboarding-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (6, "宠物用品租赁系统", "petsupplies-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (7, "电脑配件商城系统", "techmart-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (8, "甜品商城系统", "sweetstore-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (9, "智慧物业管理系统", "smartproperty-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (10, "智慧路灯管理系统", "smartlighting-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (11, "酒吧管理系统", "barpro-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (12, "流浪动物救助系统", "animalrescue-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (13, "美甲预约管理系统", "nailstyle-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (14, "OA协同办公管理系统", "oa-system-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (15, "校园车辆管理系统", "voltride-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (16, "在线学习系统", "onlinelearning-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (17, "毕业论文管理系统", "gtmanagement-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (18, "火车购票管理系统", "trainticket-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (19, "智能健康饮食系统", "diethealth-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (20, "酒店客房预订管理系统", "hotelroom-public", "SpringBoot+Vue3", "源码+数据库+论文+答辩PPT+文档"),
    (21, "留守儿童爱心帮扶系统", "childrenlove-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (22, "旅游景区购票管理系统", "scenicticket-public", "SpringBoot+Vue3", "源码+数据库+论文+答辩PPT+文档"),
    (23, "旅游网站门户系统", "travelportal-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (24, "社区健康管理系统", "commhealth-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (25, "社区志愿服务匹配系统", "volunmatch-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (26, "校园景观树木养护系统", "campuscanopy-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (27, "助农电商服务平台", "agriculture-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (28, "在线音乐平台系统", "music-system-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (29, "高校学生请假管理系统", "studentleave-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (30, "图书管理系统", "bookmanage-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (31, "高校宿舍管理系统", "dormitory-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (32, "宠物健康管理系统", "pethealthy-public", "SpringBoot+Vue", "源码+数据库+答辩PPT+文档"),
    (33, "动物园综合管理系统", "zoomanage-public", "SpringBoot+Vue", "源码+数据库+答辩PPT+文档"),
    (34, "电影院购票选座系统", "cinemasystem-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (35, "自习室座位预约管理系统", "studyroom-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (36, "仓储WMS管理系统", "warehouse-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (37, "校园流浪宠物救助系统", "campuspetrescue-public", "SpringBoot+Vue", "源码+数据库+答辩PPT+文档"),
    (38, "校园二手市场交易系统", "secondhandmarket-public", "SpringBoot+Vue", "源码+数据库+答辩PPT+文档"),
    (39, "智能进销存管理系统", "smartpsi-public", "SpringBoot+Vue", "源码+数据库+开发文档"),
    (40, "网上生鲜/超市商城系统", "onlinemart-public", "SpringBoot+Vue", "源码+数据库+论文+答辩PPT+文档"),
    (41, "智能药品进销存管理系统", "drugmanage-public", "SpringBoot+Vue", "源码+数据库"),
    (42, "智慧医院门诊预约挂号系统", "hospitalregister-public", "SpringBoot+Vue", "源码+数据库"),
]


def repo_url(slug: str) -> str:
    return f"https://gitee.com/{GITEE_USER}/{slug}"


def main() -> None:
    lines = [
        "# 毕业设计项目合集",
        "",
        "> 本仓库汇总了 **SpringBoot + Vue** 系列毕业设计项目的 Gitee 地址，方便快速检索与访问。",
        "",
        "## 项目列表",
        "",
        "| 序号 | 项目 | Gitee 地址 |",
        "| ---- | ---- | ---------- |",
    ]

    for num, name, slug, stack, tags in PROJECTS:
        title = f"基于 {stack} 的{name}({tags})"
        url = repo_url(slug)
        lines.append(
            f"| {num:03d} | [{title}]({url}) | {url} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            f"共 **{len(PROJECTS)}** 个项目。",
            "",
            "如需修改 Gitee 用户名，可设置环境变量后重新生成：",
            "",
            "```bash",
            "set GITEE_USER=你的Gitee用户名",
            "python generate_readme.py",
            "```",
        ]
    )

    output = "\n".join(lines) + "\n"
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(output)
    print(f"Generated {readme_path} with GITEE_USER={GITEE_USER}")


if __name__ == "__main__":
    main()
