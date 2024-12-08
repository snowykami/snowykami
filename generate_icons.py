# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/4 下午4:53
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : generate_icons.py.py
@Software: PyCharm
"""

# 生成github readme的图标，用html标签，一个set一个p，一个图标一个img

size = (40, 40)

icon_sets = {
        "tools1"  : [  # 生产工具
                "vscode",
                "visualstudio",
                "jetbrains",
                "androidstudio",
                "pycharm",
                "intellij",
                "goland",
                "webstorm",
                "clion",
                "datagrip",
                "photoshop",
                "aftereffects",
                "illustrator-plain",
                "premierepro",
                "dreamweaver",
                "blender",
                "chrome",
        ],
        "tools2-" : [  # 技术性工具
                "jaegertracing",
                "bash",
                "anaconda",
                "cloudflare",
                "cloudflareworkers",
                "git",
                "github",
                "gitlab",
                "githubcodespaces",
                "githubactions",
                "gcc",
                "docker",
                "kubernetes",
                "k3s",
                "mariadb",
                "matlab",
                "mongodb",
                "mysql",
                "nano",
                "neovim",
                "nginx",
                "npm-original-wordmark",
                "playwright",
                "pnpm",
                "poetry",
                "postgresql",
                "postman",
                "powershell",
                "puppeteer",
                "pypi",
                "sqlite",
                "ssh",
                "vim",
                "vite",
                "vitejs",
                "vuejs",
                "vercel",
                "wordpress",
        ],
        "libs-"   : [
                "latex",
                "grpc",
                "axios-plain",
                "bootstrap",
                'devicon',
                "django-plain",
                "fastapi",
                "flask",
                "matplotlib",
                "openal",
                "opencv",
                "opengl",
                "pandas",
                "pytorch",
                "selenium",
                "sqlalchemy",
                "numpy",
        ],
        "langs-"  : [
                "go",
                "python",
                "c",
                "cpp",
                "nodejs",
                "javascript",
                "typescript",
                "java",
                "html5",
                "css3",
                "markdown",
        ],
        "systems-": [
                "windows11",
                "android",
                "arduino",
                "linux",
                "archlinux",
                "debian",
                "centos",
                "fedora",
                "opensuse",
                "ubuntu",
        ]
}

content = ""
for name, data in icon_sets.items():
    content += f"<p align='center'>"
    # 按照字母顺序排序
    if name.endswith("-"):
        data.sort()
        name = name[:-1]
    for icon in data:
        content += f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{icon.split('-')[0]}/{icon}{'-original' if '-' not in icon else ''}.svg' alt='{icon}' width='{size[0]}px' height='{size[1]}px' />"
    content += f"</p>\n"
    content += "\n"

with open("README.md", "r", encoding="utf-8") as f:
    # 找到<!--START_SECTION:tools-->和<!--END_SECTION:tools-->的行数
    lines = f.readlines()
    
    start = -1
    end = -1
    for i in range(len(lines)):
        if "<!--START_SECTION:tools-->" in lines[i]:
            start = i
        if "<!--END_SECTION:tools-->" in lines[i]:
            end = i
            break
    if start == -1 or end == -1:
        raise ValueError("Can't find <!--START_SECTION:tools--> or <!--END_SECTION:tools-->")
    # 替换中间的内容，保留标记
    lines = lines[:start + 1] + [content] + lines[end:]
    # 写入文件
    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(lines)