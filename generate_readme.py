# -*- coding: utf-8 -*-
"""Generate allProject README.md using Gitee API and local project catalog."""

from __future__ import annotations

import json
import os
import urllib.request
import urllib.parse

GITEE_USER = os.environ.get("GITEE_USER", "ccw-ccw")
GITEE_TOKEN = os.environ.get("GITEE_TOKEN", "")

PROJECT_TAGS = "源码+数据库+UML全套图+论文+答辩PPT+说明文档"

PROJECTS = [
    (1, "智慧公交管理系统", "SmartBus", "SpringBoot+Vue"),
    (2, "汽车商城系统", "CarShop", "SpringBoot+Vue"),
    (3, "问卷调查系统", "InsightForm", "SpringBoot+Vue"),
    (4, "宠物寄养家庭版系统", "PetHaven", "SpringBoot+Vue"),
    (5, "宠物寄养机构版管理系统", "PetBoarding", "SpringBoot+Vue"),
    (6, "宠物用品租赁系统", "PetSupplies", "SpringBoot+Vue"),
    (7, "电脑配件商城系统", "TechMart", "SpringBoot+Vue"),
    (8, "甜品商城系统", "sweetstore", "SpringBoot+Vue"),
    (9, "智慧物业管理系统", "SmartProperty", "SpringBoot+Vue"),
    (10, "智慧路灯管理系统", "SmartLighting", "SpringBoot+Vue"),
    (11, "酒吧管理系统", "barpro", "SpringBoot+Vue"),
    (12, "流浪动物救助系统", "StrayAnimalRescueSystem", "SpringBoot+Vue"),
    (13, "美甲预约管理系统", "nailstyle", "SpringBoot+Vue"),
    (14, "OA协同办公管理系统", "oa-system", "SpringBoot+Vue"),
    (15, "校园车辆管理系统", "voltRide", "SpringBoot+Vue"),
    (16, "在线学习系统", "personalized_learning", "SpringBoot+Vue"),
    (17, "毕业论文管理系统", "GTManagementSystem", "SpringBoot+Vue"),
    (18, "火车购票管理系统", "trainticker", "SpringBoot+Vue"),
    (19, "智能健康饮食系统", "comingwindy-healthy-diet", "SpringBoot+Vue"),
    (20, "酒店客房预订管理系统", "hotel-room-system", "SpringBoot+Vue3"),
    (21, "留守儿童爱心帮扶系统", "children-love", "SpringBoot+Vue"),
    (22, "旅游景区购票管理系统", "tourism-ticket-system", "SpringBoot+Vue3"),
    (23, "旅游网站门户系统", "travelManage", "SpringBoot+Vue"),
    (24, "社区健康管理系统", "commHealth", "SpringBoot+Vue"),
    (25, "社区志愿服务匹配系统", "VolunMatch", "SpringBoot+Vue"),
    (26, "校园景观树木养护系统", "CampusCanopy", "SpringBoot+Vue"),
    (27, "助农电商服务平台", "Agriculture", "SpringBoot+Vue"),
    (28, "在线音乐平台系统", "music-recommendation-system", "SpringBoot+Vue"),
    (29, "高校学生请假管理系统", "student_leave_system", "SpringBoot+Vue"),
    (30, "图书管理系统", "book-management-system", "SpringBoot+Vue"),
    (31, "高校宿舍管理系统", "dormitory", "SpringBoot+Vue"),
    (32, "宠物健康管理系统", "PetHealthy", "SpringBoot+Vue"),
    (33, "动物园综合管理系统", "ZooManage", "SpringBoot+Vue"),
    (34, "电影院购票选座系统", "CinemaSystem", "SpringBoot+Vue"),
    (35, "自习室座位预约管理系统", "StudyRoomManage", "SpringBoot+Vue"),
    (36, "仓储WMS管理系统", "WarehouseManage", "SpringBoot+Vue"),
    (37, "校园流浪宠物救助系统", "CampusPetRescue", "SpringBoot+Vue"),
    (38, "校园二手市场交易系统", "SecondHandMarket", "SpringBoot+Vue"),
    (39, "智能进销存管理系统", "SmartPSI", "SpringBoot+Vue"),
    (40, "网上生鲜/超市商城系统", "OnlineMart", "SpringBoot+Vue"),
    (41, "智能药品进销存管理系统", "DrugManagement", "SpringBoot+Vue"),
    (42, "智慧医院门诊预约挂号系统", "HospitalRegistration", "SpringBoot+Vue"),
    (43, "鲜花商城系统", "FlowerMall", "SpringBoot+Vue"),
    (44, "校园跑腿系统", "CampusErrand", "SpringBoot+Vue"),
    (45, "健身房预约系统", "GymReservation", "SpringBoot+Vue"),
    (46, "房屋租赁系统", "HouseRental", "SpringBoot+Vue"),
    (47, "招聘网站系统", "RecruitmentSite", "SpringBoot+Vue"),
    (48, "体育馆预约系统", "StadiumReservation", "SpringBoot+Vue"),
    (49, "校园论坛系统", "CampusForum", "SpringBoot+Vue"),
    (50, "外卖点餐系统", "TakeoutOrder", "SpringBoot+Vue"),
    (51, "养老院管理系统", "NursingHome", "SpringBoot+Vue"),
    (52, "智慧停车场系统", "SmartParking", "SpringBoot+Vue"),
    (53, "文化遗产管理系统", "CulturalHeritage", "SpringBoot+Vue"),
    (54, "海洋文化科普网站", "MarineCulture", "SpringBoot+Vue"),
]


def fetch_repos() -> dict[str, str]:
    if not GITEE_TOKEN:
        return {}
    repos: dict[str, str] = {}
    page = 1
    while True:
        query = urllib.parse.urlencode({
            "access_token": GITEE_TOKEN,
            "affiliation": "owner",
            "per_page": 100,
            "page": page,
        })
        url = f"https://gitee.com/api/v5/user/repos?{query}"
        with urllib.request.urlopen(url, timeout=30) as resp:
            batch = json.loads(resp.read().decode("utf-8"))
        if not batch:
            break
        for repo in batch:
            html_url = repo.get("html_url", "")
            if html_url.endswith(".git"):
                html_url = html_url[:-4]
            repos[repo["path"].lower()] = html_url
            repos[repo["name"].lower()] = html_url
        if len(batch) < 100:
            break
        page += 1
    return repos


def repo_url(slug: str | None, repos: dict[str, str]) -> str | None:
    if not slug:
        return None
    return repos.get(slug.lower()) or f"https://gitee.com/{GITEE_USER}/{slug}"


def main() -> None:
    repos = fetch_repos()
    linked = 0
    lines = [
        "# 毕业设计项目合集",
        "",
        f"> Gitee 主页：[https://gitee.com/{GITEE_USER}](https://gitee.com/{GITEE_USER})",
        "",
        "> 本仓库汇总 **SpringBoot + Vue** 系列毕业设计项目的 Gitee 地址，方便快速检索与访问。",
        "",
        "> **购买地址**：[https://www.vvxx.love](https://www.vvxx.love)（vv毕设网）",
        ">",
        "> 提供 **免费配套软件下载 + 安装说明 + 部署教程**；支持 **一键生成 UML 图**：上传项目压缩包即可自动产出功能模块图、用例图、流程图、E-R 图、时序图等全套毕设图表。",
        "",
        "![vv毕设网 - 一键画图](https://fanhua-yingcai.oss-cn-shanghai.aliyuncs.com/uml-draw.png)",
        "",
        "## 仓库简介",
        "",
        "所有项目均为 **SpringBoot + Vue** 前后端分离毕设项目，当前共收录 **{}** 个：".format(len(PROJECTS)),
        "",
        "；".join(f"{num:02d}.{name}" for num, name, *_ in PROJECTS) + "。",
        "",
        "## 项目列表",
        "",
        "| 序号 | 项目 | Gitee 地址 |",
        "| ---- | ---- | ---------- |",
    ]
    for num, name, slug, stack in PROJECTS:
        title = f"基于 {stack} 的{name}({PROJECT_TAGS})"
        url = repo_url(slug, repos)
        if url and slug and slug.lower() in repos:
            linked += 1
            lines.append(f"| {num:03d} | {title} | {url} |")
        elif url:
            lines.append(f"| {num:03d} | {title} | {url} |")
        else:
            lines.append(f"| {num:03d} | {title} | 待上传 |")
    lines.extend(["", "---", "", f"共 **{len(PROJECTS)}** 个项目，已关联 Gitee **{linked}** 个。"])
    output = "\n".join(lines) + "\n"
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(output)
    print(f"Generated {readme_path}")
    print(f"Linked {linked}/{len(PROJECTS)} projects")


if __name__ == "__main__":
    main()
