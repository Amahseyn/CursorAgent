---
name: html-css
description: Write and review HTML and CSS in any repository that already contains it. Use when the repo has HTML, CSS, or a styling setup already in the repo.
---

# HTML and CSS

Use this only when the repository already contains HTML and CSS. Do not add it, and do not switch the file to another language.

Look for:

- A new CSS framework beside the one this repo already loads.
- A click handler on a non-interactive element when a button exists in the design system.
- A style that bypasses the token or class the neighboring component uses.
- A document that drops the language or title the other pages set.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add a second CSS framework for one page.
GOOD: Use the class the component beside this one already uses.
```
