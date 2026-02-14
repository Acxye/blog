---
date: 2026-02-14
description: ""
draft: false
title: "2.3"
weight: 4
tags: []
series: ["汇编语言,王爽,第4版：检测点"]
series_order: 4
---

![](./1.png)

| 指令 | 修改IP的时候 |
| :--- | :----------- |
| `mov ax, bx` | 指令被读入指令缓冲器后 |
| `sub ax, ax` | 指令被读入指令缓冲器后 |
| `jmp ax` | 指令被读入指令缓冲器后和指令执行后 |

一共修改了4次IP寄存器，最后IP中的值等于0。