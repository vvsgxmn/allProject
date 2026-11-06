# -*- coding: utf-8 -*-
"""Generate a platform-specific allProject index."""
import argparse
import ast
import json
import os
from pathlib import Path
import re
import tempfile
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
GITEE_USER = os.environ.get("GITEE_USER", "ccw-ccw")
GITHUB_USER = os.environ.get("GITHUB_USER", "vvsgxmn")
DEFAULT_PLATFORM = "github"
GITHUB_SLUG_OVERRIDES = {}

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
    (55, "顺风车管理系统", "RideShare", "SpringBoot+Vue"),
    (56, "服装售卖商城", "ClothingMall", "SpringBoot+Vue"),
    (57, "网约车出行系统", "CarHailing", "SpringBoot+Vue"),
    (58, "教务系统", "EduAdmin", "SpringBoot+Vue"),
    (59, "汽车租赁系统", "CarRental", "SpringBoot+Vue"),
    (60, "报刊征订系统", "PressSub", "SpringBoot+Vue"),
    (61, "电器商城系统", "ApplianceMall", "SpringBoot+Vue"),
    (62, "在线拍卖系统", "OnlineAuction", "SpringBoot+Vue"),
    (63, "垃圾分类系统", "WasteSort", "SpringBoot+Vue"),
    (64, "档案管理系统", "ArchiveManage", "SpringBoot+Vue"),
    (65, "游乐场购票系统", "ParkTicket", "SpringBoot+Vue"),
    (66, "汽车零部件销售系统", "AutoParts", "SpringBoot+Vue"),
    (67, "博物馆管理系统", "MuseumManage", "SpringBoot+Vue"),
    (68, "少儿编程管理系统", "KidsCode", "SpringBoot+Vue"),
    (69, "手办销售系统", "FigureShop", "SpringBoot+Vue"),
    (70, "宠物洗护预约系统", "PetGrooming", "SpringBoot+Vue"),
    (75, "民宿管理系统", "HomestayManage", "SpringBoot+Vue"),
]

def request_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"{urllib.parse.urlsplit(url).hostname} API: HTTP {exc.code}") from None

def fetch_repos(platform, owner):
    rows = {}
    if platform == "github":
        token = os.environ.get("GITHUB_TOKEN")
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "allProject-index"}
        if token:
            headers["Authorization"] = "Bearer " + token
    else:
        token = os.environ.get("GITEE_TOKEN")
        if not token:
            raise SystemExit("Missing GITEE_TOKEN")
    for page in range(1, 100):
        if platform == "github":
            query = urllib.parse.urlencode({"type": "owner", "per_page": 100, "page": page})
            batch = request_json(f"https://api.github.com/users/{owner}/repos?{query}", headers)
        else:
            query = urllib.parse.urlencode({"access_token": token, "affiliation": "owner", "per_page": 100, "page": page})
            batch = request_json(f"https://gitee.com/api/v5/user/repos?{query}")
        if not isinstance(batch, list):
            raise SystemExit(f"{platform}: unexpected API response")
        for repo in batch:
            if repo.get("private") is not False or (repo.get("owner") or {}).get("login", "").casefold() != owner.casefold():
                continue
            slug = repo.get("path") if platform == "gitee" else repo.get("name")
            if slug:
                rows[slug.casefold()] = slug
        if len(batch) < 100:
            return rows
    raise SystemExit(f"{platform}: pagination exceeded the expected repository count")

def platform_slugs(platform):
    mapping = dict(GITHUB_SLUG_OVERRIDES) if platform == "github" else {}
    for path in (ROOT / "projects_git_map.json", ROOT.parent / "projects_git_map.json"):
        if path.is_file():
            mapping.update({int(item["num"]): item[platform] for item in json.loads(path.read_text(encoding="utf-8")) if item.get(platform)})
            break
    return mapping

def render(platform, owner, repositories):
    host = {"github": "github.com", "gitee": "gitee.com"}[platform]
    home = f"https://{host}/{owner}"
    mapping = platform_slugs(platform)
    linked = 0
    lines = [
        "# 毕业设计项目合集", "",
        f"> 账号主页：[{home}]({home})", "",
        "> 本仓库仅作项目索引，收录 SpringBoot + Vue 前后端分离示例仓库地址。", "",
        "> 站点：[https://www.vvxx.love](https://www.vvxx.love)", "",
        "## 说明", "",
        f"当前共收录 **{len(PROJECTS)}** 个项目，详见下表。", "",
        "## 项目列表", "",
        "| 序号 | 项目 | 地址 |",
        "| ---- | ---- | ---- |",
    ]
    for num, name, fallback, _stack in PROJECTS:
        slug = mapping.get(num, fallback)
        canonical = repositories.get(slug.casefold()) if slug else None
        if canonical:
            addr = f"{home}/{urllib.parse.quote(canonical, safe='-._')}"
            linked += 1
        else:
            addr = "待上传"
        lines.append(f"| {num:03d} | {name} | {addr} |")
    lines.extend(["", f"合计 {len(PROJECTS)} 个，已关联 {linked} 个。"])
    output = "\n".join(lines) + "\n"
    validate(output, platform, owner)
    return output, linked

def validate(output, platform, owner):
    forbidden = "gitee.com" if platform == "github" else "github.com"
    home = f"https://{platform}.com/{owner}"
    if forbidden in output.casefold() or f"账号主页：[{home}]({home})" not in output:
        raise SystemExit(f"{platform}: index contains a cross-platform URL or incorrect account home")
    for link in re.findall(r"(?m)^\|\s*\d+\s*\|[^|]+\|\s*(https?://[^\s|]+)", output):
        if not link.startswith(home + "/"):
            raise SystemExit(f"{platform}: project link has an unexpected owner or domain")

def write_atomic(path, output):
    path = Path(path).resolve()
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent, prefix=".index-", suffix=".tmp", delete=False) as handle:
        tmp = Path(handle.name)
        handle.write(output)
    try:
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Generate one platform's allProject index")
    parser.add_argument("--platform", choices=("gitee", "github"), default=DEFAULT_PLATFORM, required=DEFAULT_PLATFORM is None)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    platform = args.platform
    owner = GITHUB_USER if platform == "github" else GITEE_USER
    output, linked = render(platform, owner, fetch_repos(platform, owner))
    out = args.out or ROOT / ("README.github.md" if DEFAULT_PLATFORM is None and platform == "github" else "README.md")
    write_atomic(out, output)
    print(f"Generated {out}")
    print(f"{platform}: Linked {linked}/{len(PROJECTS)} projects")

if __name__ == "__main__":
    main()
