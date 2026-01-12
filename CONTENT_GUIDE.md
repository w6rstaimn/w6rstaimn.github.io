# Content Writing Guide

This guide explains how to write blog posts and CTF writeups for your blog.

## 📁 Directory Structure

All content is located in `src/content/blog/`. Each post should have its own directory:

```text
src/content/blog/
└── my-awesome-post/
    ├── index.mdx       # Main post entry point
    ├── 0.mdx           # (Optional) First subpost/challenge
    ├── 1.mdx           # (Optional) Second subpost/challenge
    └── assets/         # Images and other files for this post
        └── banner.png
```

## 📝 Writing a Post

### 1. Create a New Directory
Create a folder inside `src/content/blog/` with a URL-friendly name (slug), e.g., `my-first-pwn-writeup`.

### 2. Create `index.mdx`
Add a file named `index.mdx` inside your new folder. Every post must have frontmatter at the top:

```markdown
---
title: 'My First Pwn Writeup'
description: 'A detailed walkthrough of how I solved X challenge.'
date: 2026-01-12
tags: ['pwn', 'ctf', 'writeup']
imageWithText: 'assets/banner.png'        # Optional: banner with text
imageWithoutText: 'assets/banner.png'     # Optional: banner without text
authors: ['w6rst']                       # Use your author ID (defined in src/content/authors)
draft: false                              # Set to true to hide while writing
---

## Introduction

Hello! This is my first writeup...
```

## 🚩 Writing a CTF Writeup (with Subposts)

For long series (like a CTF with many challenges), you can split the post into subposts.

1.  **Main Page**: Use `index.mdx` as the overview.
2.  **Subposts**: Create `0.mdx`, `1.mdx`, etc., in the same directory.
3.  **Frontmatter for Subposts**: They use the same frontmatter as `index.mdx`. The system sorts them by the `order` field if provided, or by date.

### Navigation Between Subposts
You can use the `<FirstSubpost />` component in your `index.mdx` to link to the first challenge:

```mdx
import FirstSubpost from '@/components/mdx/FirstSubpost.astro'

<FirstSubpost title="Challenge 1: Warmup" href="/blog/my-ctf-writeup/0" />
```

## 🛠️ Custom Components

You can use several custom components in your `.mdx` files:

### Challenges
Use the `<Challenge />` component to display CTF challenge details:

```mdx
import Challenge from '@/components/mdx/Challenge.astro'

<Challenge
  name="Warmup"
  category="Pwn"
  points={100}
  solves={500}
  files={['/static/warmup.zip']}
/>
```

### Callouts
Use the `<Callout />` component for notes, warnings, or tips:

```mdx
import Callout from '@/components/mdx/Callout.astro'

<Callout type="info">
  This is a useful tip!
</Callout>

<Callout type="warning">
  Be careful with this step.
</Callout>
```

## 🖼️ Assets

Always place images inside the `assets/` folder within your post directory. Reference them in MDX like this:

```markdown
![My Screenshot](assets/screenshot.png)
```
