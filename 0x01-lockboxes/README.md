# 0x01. Lockboxes

## Project Overview

In this project, we implement a solution to determine if all boxes in a sequence can be unlocked. Each box is locked but contains keys to other boxes. The goal is to determine if, starting from the first box (which is unlocked), you can unlock all other boxes.

## Problem Description

You are given `n` locked boxes numbered from `0` to `n - 1`. Each box may contain a list of keys, where each key is represented by an integer that corresponds to a box number. The first box is unlocked, and you need to write a function `canUnlockAll(boxes)` that determines whether all boxes can be opened.

### Prototype

```python
def canUnlockAll(boxes):
